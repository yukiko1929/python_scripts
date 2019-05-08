import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'yuki3',
    charset = 'utf8'
)

cursor = conn.cursor()

# create_stuinfo = '''create table stuinfo(
# stu_id INT, stu_name CHAR(20),
# stu_city CHAR(10), age tinyint,
# gender enum('female', 'male'),
# PRIMARY KEY(stu_id)
# )'''
# cursor.execute(create_stuinfo)

create_score = '''create table scores(
stu_id INT, stu_name char(20),
exam_id INT,
score tinyint, ranking tinyint,
PRIMARY KEY(exam_id),
FOREIGN KEY(stu_id) REFERENCES stuinfo(stu_id)
)'''

cursor.execute(create_score)

conn.commit()
#cursor.commit()
cursor.close()
conn.close()

