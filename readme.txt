•相關網站
https://datatables.net/




CREATE TABLE employee (
	id serial PRIMARY KEY,
	name VARCHAR ( 100 ) NOT NULL,
	position VARCHAR ( 100 ) NOT NULL,
	office VARCHAR ( 100 ) NOT NULL,
	age INT NOT NULL,
	salary INT NOT NULL,
	photo VARCHAR ( 150 ) NOT NULL,
);


INSERT INTO
    employee(name, position, office, age, salary, photo)
VALUES
	('Tiger Wood', 'Accountant', 'Tokyo', 36, 5689, '01.jpg'),
	('Mark Oto Ednalan', 'Chief Executive Officer (CEO)', 'London', 56, 5648, '02.jpg'),
	('Jacob thompson', 'Junior Technical Author', 'San Francisco', 23, 5689, '03.jpg'),
	('cylde Ednalan', 'Software Engineer', 'Olongapo', 23, 54654, '04.jpg'),
	('Rhona Davidson', 'Software Engineer', 'San Francisco', 26, 5465, '05.jpg'),
	('Quinn Flynn', 'Integration Specialist', 'New York', 53, 56465, '06.jpg'),
	('Tiger Nixon', 'Software Engineer', 'London', 45, 456, '07.jpg'),
	('Airi Satou', 'Pre-Sales Support', 'New York', 25, 4568, '08.jpg'),
	('Angelica Ramos', 'Sales Assistant', 'New York', 45, 456, '09.jpg'),
	('Ashton updated', 'Senior Javascript Developer', 'Olongapo', 45, 54565, '01.jpg'),
	('Bradley Greer', 'Regional Director', 'San Francisco', 27, 5485, '02.jpg'),
	('Brenden Wagner', 'Javascript Developer', 'San Francisco', 38, 65468, '03.jpg'),
	('Brielle Williamson', 'Personnel Lead', 'Olongapo', 56, 354685, '04.jpg'),
	('Bruno Nash', 'Customer Support', 'New York', 36, 65465, '05.jpg'),
	('cairocoders', 'Sales Assistant', 'Sydney', 45, 56465, '06.jpg'),
	('Zorita Serrano', 'Support Engineer', 'San Francisco', 38, 6548, '07.jpg'),
	('Zenaida Frank', 'Chief Operating Officer (COO)', 'San Francisco', 39, 545, '08.jpg'),
	('Sakura Yamamoto', 'Support Engineer', 'Tokyo', 48, 5468, '05.jpg'),
	('Serge Baldwin', 'Data Coordinator', 'Singapore', 85, 5646, '05.jpg'),
	('Shad Decker', 'Regional Director', 'Tokyo', 45, 4545, '05.jpg');