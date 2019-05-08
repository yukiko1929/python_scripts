import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'yuki2',
    charset = 'utf8'
)

cursor = conn.cursor()
# create_dep = '''create table department(
# dep_id int, dep_name varchar(20),
# PRIMARY KEY(dep_id)
# )'''
# cursor.execute(create_dep)
# create_staff = '''create table staff(
# staff_id int,
# dep_id int,
# staff_name varchar(20),
# email char(20),
# PRIMARY KEY(staff_id), FOREIGN KEY(dep_id) REFERENCES department(dep_id)
# )'''
# # cursor.execute(create_staff)
create_salary = '''create table salary(
auto_id int, staff_id int,
day date, basic int,
bonus int, primary key(auto_id),
FOREIGN KEY(staff_id) REFERENCES staff(staff_id)
) 
'''
cursor.execute(create_salary)
conn.commit()
cursor.close()
conn.close()

# create tables staff(id int(5) primary key, name char(8),
# gender enum('female', 'male'), age tinyint unsigned,
# birth date, phone int(11), email char(20) )

# create table department(id char(10) primary key, )

