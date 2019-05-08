import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'yuki3',
    charset = 'utf8'
)

cursor = conn.cursor()

# insert_stu1 = 'insert into stuinfo VALUES(%s, %s,%s, %s, %s)'
# stus = [(1908, 'takako','aomori',14, 'female'),(1911, 'ginko', 'kyoto', 16,'female'),(1912, 'uchiha', 'kinoha', 15, 'male')]
# cursor.executemany(insert_stu1, stus)

# update_stu1 = 'update stuinfo set stu_name = %s WHERE stu_name = %s'
# new_info1 = ('mikuko', 'mika')
# cursor.execute(update_stu1, new_info1)

# delete1 = 'delete from stuinfo WHERE age <= 16'
# cursor.execute(delete1)

# query1 = 'select * from stuinfo'
# cursor.execute(query1)
# result1 = cursor.fetchone()
# result2 = cursor.fetchmany(2)
# result3 = cursor.fetchall()
#
# print(result1)
# print('*' * 50)
# print(result2)
# print('*' * 50)
# print(result3)
query2 = 'select * from stuinfo ORDER by stu_id DESC'
cursor.execute(query2)
# resultall = cursor.fetchall()
# print(resultall)
cursor.scroll(3, mode='absolute')
result1 = cursor.fetchmany(2)
print(result1)
cursor.scroll(-2, mode='relative')
result2 = cursor.fetchmany(2)
print(result2)

conn.commit()
cursor.close()
conn.close()