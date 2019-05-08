import pymysql

connect = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    db = 'yuki4',
    charset = 'utf8'
)

cursor = connect.cursor()
# create_service = '''create table service(
#   server_id INT,
#   service char(20),
#   price INT,
#   provider CHAR(20)
# )'''
# cursor.execute(create_service)


#
create_customer = '''create table customer(
  cus_id INT,
  serve_id INT,
  cus_name CHAR(20)
)'''
cursor.execute(create_customer)
connect.commit()
cursor.close()
connect.close()