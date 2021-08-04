from flask import Flask, render_template, request, jsonify
import psycopg2
import psycopg2.extras


app = Flask(__name__)
app.secret_key = "SkillChen_Secret_Key"

DB_HOST = 'localhost'
DB_PORT = '5433'
DB_NAME = 'sampledb'
DB_USER = 'postgres'
DB_PASS = 'dba'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajaxfile",methods=["POST","GET"])
def ajaxfile():
    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if request.method == 'POST':
            draw = request.form['draw'] 
            row = int(request.form['start'])
            rowperpage = int(request.form['length'])
            searchValue = request.form["search[value]"]
            #print(draw)
            #print(row)
            #print(rowperpage)
            #print(searchValue)
  
            ## Total number of records without filtering
            cursor.execute("select count(*) as allcount from employee")
            rsallcount = cursor.fetchone()
            totalRecords = rsallcount['allcount']
            #print(totalRecords) 
  
            ## Total number of records with filtering
            #likeString = "%" + searchValue + "%"
 
            likeString = "{}%".format(searchValue)
 
            #print(likeString)
            cursor.execute("SELECT count(*) as allcount from employee WHERE UPPER(name) LIKE UPPER(%s)", (likeString,))
            rsallcount = cursor.fetchone()
            totalRecordwithFilter = rsallcount['allcount']
            #print(totalRecordwithFilter) 
  
            ## Fetch records
            if searchValue=='':
                cursor.execute('SELECT * FROM employee LIMIT {limit} OFFSET {offset}'.format(limit=rowperpage, offset=row))
                employeelist = cursor.fetchall()
            else:        
                cursor.execute("SELECT * FROM employee WHERE UPPER(name) LIKE UPPER(%s) LIMIT %s OFFSET %s;", (likeString, rowperpage, row,))
 
                employeelist = cursor.fetchall()
  
            data = []
            for row in employeelist:
                data.append({
                    'name': row['name'],
                    'position': row['position'],
                    'age': row['age'],
                    'salary': row['salary'],
                    'office': row['office'],
                })
  
            response = {
                'draw': draw,
                'iTotalRecords': totalRecords,
                'iTotalDisplayRecords': totalRecordwithFilter,
                'aaData': data,
            }
            return jsonify(response)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 

if __name__ == '__main__':
    app.run(debug=True)