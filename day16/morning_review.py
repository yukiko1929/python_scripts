import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import String, Integer, ForeignKey, Column, Enum
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root@127.0.0.1/yuki4?charset=utf8',
    encoding = 'utf8',
    echo=True
)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'student'
    stu_id = Column(Integer, primary_key=True)
    stu_name = Column(String(20))
    stu_age = Column(Integer)

class Score(Base):
    __tablename__ = 'score'
    exam_id = Column(Integer, primary_key=True)
    stu_id = Column(Integer, ForeignKey('student.stu_id'))
    scores = Column(Integer)
    scholarship = Column(Enum('level-1', 'level-2', 'level-3'))

class College(Base):
    __tablename__ = 'college'
    college_id = Column(Integer,primary_key=True)
    exam_id = Column(Integer,ForeignKey('score.exam_id'))
    college = Column(String(20))
    threshold = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)