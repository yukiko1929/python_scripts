import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'yuki2',
    charset = 'utf8'
)

cursor = conn.cursor()
# insert_dep1 = 'insert into department VALUES(%s, %s) '
# deps = [(1, 'devops'), (2, 'marketing'), (3, 'general affairs'), (4, 'R&D')]
# cursor.executemany(insert_dep1, deps)

# insert_dep2 = 'insert into department VALUES (%s, %s)'
# deps = [(5,'finance'),(6, 'security'),(7, 'software'),(8, 'hardware')]
# cursor.executemany(insert_dep2, deps)

# update_dep1 = 'update department set dep_name = %s where dep_name = %s'
# denames = ('info_security', 'security')
# cursor.execute(update_dep1, denames)

# delete_dep1 = 'delete from department WHERE dep_name = %s'
# deps = ('finance',)    # do not forget to add comma
# cursor.execute(delete_dep1, deps)

# select = 'select * from department ORDER BY dep_id'
# cursor.execute(select)
# result1 = cursor.fetchone()
# result2 = cursor.fetchmany(2)
# result3 = cursor.fetchall()
# print(result1)
# print('*' * 50)
# print(result2)
# print('*' * 50)
# print(result3)

select2 = 'select * from department ORDER BY dep_id'
cursor.execute(select2)
cursor.scroll(3,mode='absolute')
result1 = cursor.fetchone()
cursor.scroll(-1, mode='relative')
result2 = cursor.fetchone()
print(result1)
print('*' * 50)
print(result2)

#cursor.execute()
conn.commit()
cursor.close()
conn.close()