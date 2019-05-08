from new_alchemy import Stu_info, Scores, Session
from sqlalchemy import and_, or_

session = Session()

# to add information
# masami = Stu_info(stu_id = 1913, stu_name = 'masami', gender = 'female', age = 11)
# mikiko = Stu_info(stu_id = 1914, stu_name = 'mikiko', gender = 'male', age = 17)
# ninji = Stu_info(stu_id = 1915, stu_name = 'ninji', gender = 'male', age = 13)
# session.add_all([masami, mikiko, ninji])
# session.commit()
# session.close()

# to query
# query1 = session.query(Stu_info)
# for student in query1:
#     print(student.stu_id, student.stu_name)

# query2 = session.query(Stu_info).order_by(Stu_info.age)
# for student in query2:
#     print(student.stu_id, student.stu_name, student.age)

# query3 = session.query(Stu_info).filter(Stu_info.age >= 15)
# for student in query3:
#     print(student.stu_id, student.stu_name, student.age)
#
# query4 = session.query(Stu_info).filter(Stu_info.stu_id == 1914)
# del1 = query4.one()
# # print(del1)
# session.delete(del1)
# session.commit()
# session.close()

# query5 = session.query(Stu_info).filter(and_(Stu_info.age >=11, Stu_info.age <= 14))
# for student in query5:
#     print(student.stu_id, student.stu_name, student.age)

# query6 = session.query(Stu_info).filter(or_(Stu_info.age <= 11, Stu_info.age > 14))
# for student in query6:
#     print(student.stu_name, student.age)

query7 = session.query(Stu_info).count()
print(query7)