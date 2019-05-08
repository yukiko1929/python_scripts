from my_alchemy import Department, Staff, Salary, Session

session = Session()
# hr = Department(dep_id = 1, dep_name = 'human resource')
# #session.add(hr)
# ops = Department(dep_id = 2, dep_name = 'operations')
# design = Department(dep_id = 3, dep_name = 'design')
# dev = Department(dep_id = 4, dep_name = 'development')
# finan = Department(dep_id = 5, dep_name = 'finance')
# session.add_all([ops, hr, dev, design, finan])
# session.commit()
# session.close()

# yuki = Staff(staff_id = 190101, staff_name = 'yuki', email = 'yuki@out.com', dep_id = 4)
# mihoko = Staff(staff_id = 190211, staff_name = 'miho', email = 'miho@devops.com', dep_id = 4)

#####################################################
# masami = Staff(
#     staff_id = 190304,
#     staff_name = 'masami',
#     email = 'masami@out.com',
#     dep_id = 3
# )
#
# shimizu = Staff(
#     staff_id = 190501,
#     staff_name = 'shimizu',
#     email = 'shimizu@out.com',
#     dep_id = 2
# )
# session.add_all([masami, shimizu])
# session.add_all([yuki,mihoko])
########################################################
# query1 = session.query(Department)
# print(query1)     # sql statement
# deps = query1.all()    # take all the query content
# print(deps)       # deps consist of instance generated by each line
# for dep in query1:
#     print(dep.dep_id, dep.dep_name)

# query2 = session.query(Staff)       # use class
# for staff in query2:       # list all the instances
#     print(staff.staff_id, staff.staff_name, staff.email, staff.dep_id)   # install.attribute

# query3 = session.query(Staff.staff_id, Staff.email)   #directly use class.attribute
# #print(query3)    # a sql statement
# # print(query3.all())   #  result in the form of tuple
# for name, email in query3:
#     #for i in range(2):
#     print(name, email)

# query4 = session.query(Staff).order_by(Staff.staff_id)
# for staff in query4:
#     print(staff.staff_id, staff.staff_name, staff.email)

# query5 = session.query(Department).order_by(Department.dep_id)[2:4]
# for dep in query5:
#     print(dep.dep_id, dep.dep_name)

# query6 = session.query(Department).filter(Department.dep_id<=3)
# #print(query6)
# for dep in query6:
#     print(dep.dep_id, dep.dep_name)
#
# query7 = session.query(Staff).filter(Staff.email.like('%devops.com'))
# for staff in query7:
#     print(staff.staff_id, staff.staff_name, staff.email)

# query8 = session.query(Staff).filter(Staff.staff_id.in_([190101,190201]))
# for staff in query8:
#     print(staff.staff_id,staff.staff_name)

# query9 = session.query(Department).filter(Department.dep_id.in_([1,3]))
# for dep in query9:
#     print(dep.dep_id, dep.dep_name)
#
# query10 = session.query(Department).filter(~Department.dep_id.in_([1,3]))
# for dep in query10:
#     print(dep.dep_id, dep.dep_name)

###############################################################################
from sqlalchemy import and_, or_

# queru11 = session.query(Department).filter(or_(Department.dep_id >=2, Department.dep_id < 4))
# for dep in queru11:
#     print(dep.dep_id, dep.dep_name)
#
# query12 = session.query(Department).filter(and_(Department.dep_id >=2, Department.dep_id <4))
# for dep in query12:
#     print(dep.dep_id,dep.dep_name)

# query13 = session.query(Department).count()
# print(query13)   # how many rows in the table
#
# query14 = session.query(Staff.staff_name, Department.dep_name).join(Department)
# for sta_name, dep_name in query14:
#     print(sta_name, dep_name)
#
# query15 = session.query(Department.dep_name, Staff.staff_name).join(Staff)
# for de_name, sta_name in query15:
#     print(de_name, sta_name)
#
# query16 = session.query(Department).filter(Department.dep_name == 'finance')
# print(query16.all())
# print(query16.one())
# fi = query16.one()
# fi.dep_name = 'financing'

query17 = session.query(Department).filter(Department.dep_id == 5)
item1 = query17.one()
session.delete(item1)
# query14 = session

session.commit()
session.close()