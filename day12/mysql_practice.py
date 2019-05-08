import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'yuki1',
    charset = 'utf8'
)

cursor = conn.cursor()
# create_staff = '''create table staffs(
# staff_id int,name varchar(10),
# gender enum('female','male'),
# birth DATE, contatc INT, email char(20),
# PRIMARY KEY(staff_id)
# )'''
# cursor.execute(create_staff)

# create_depart = '''create table departments(
# depart_id INT, depart_name char(10),staff_id INT,
# PRIMARY KEY(depart_id), FOREIGN KEY(staff_id) REFERENCES staff(staff_id)
# )'''
# cursor.execute(create_depart)
#
# create_salary = '''create table salaries(
# auto_id int,
# staf_id INT, dep_id INT,
# basic INT, extra INT,
# PRIMARY KEY(auto_id),
# FOREIGN KEY(dep_id) REFERENCES departments(depart_id)
# )'''
# cursor.execute(create_salary)

create_score = '''create table score(
exam_id INT, depart_id INT,
subject SET('devops', 'dba', 'python'), score tinyint,
ranking tinyint unsigned,
PRIMARY KEY(exam_id),
FOREIGN KEY(exam_id) REFERENCES departments(depart_id)
)'''
cursor.execute(create_score)
conn.commit()
cursor.close()
conn.close()