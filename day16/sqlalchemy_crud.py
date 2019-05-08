from morning_review import Student, Score, College
from morning_review import Session
from sqlalchemy import or_, and_

session = Session()

# masami = Student(stu_id = 1901, stu_name = 'masami', stu_age = 18)
# hikaru = Student(stu_id = 1902, stu_name = 'hikaru', stu_age = 17)
# itsuki = Student(stu_id = 1903, stu_name = 'itsuki', stu_age = 16)
# session.add_all([masami, hikaru, itsuki])

# query1 = session.query(Student)
# for student in query1:
#     print(student.stu_id, student.stu_name, student.stu_name)

# masami = Score(exam_id = 190001, stu_id = 1901, scores = 657, scholarship = 'level-1')
# hikaru = Score(exam_id = 190002, stu_id = 1902, scores = 677, scholarship = 'level-1')
# itsuki = Score(exam_id = 190003, stu_id = 1903, scores = 601, scholarship = 'level-2')
# genji = Score(exam_id = 190004, stu_id = 1904, scores = 581, scholarship = 'level-2')
# fuji = Score(exam_id = 190005, stu_id = 1905, scores = 549, scholarship = 'level-3')
# session.add_all([masami,hikaru, itsuki])
query2 = session.query(Score).filter(and_(Score.exam_id < 190003, Score.scores > 655))
for student in query2:
    print(student.exam_id, student.stu_id, student.scores)


session.commit()
session.close()

