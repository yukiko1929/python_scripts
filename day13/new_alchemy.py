import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String, Column, Integer, ForeignKey, Enum

engine = create_engine(
    'mysql+pymysql://root@127.0.0.1/yuki4?charset=utf8',
    encoding = 'utf8',
    echo = True    #should be false in working place
)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Stu_info(Base):
    __tablename__ = 'stuinfo'
    stu_name = Column(String(20))
    stu_id = Column(Integer,primary_key=True)
    #gender = Column(enumerate('female', 'male'))
    gender = Column(Enum('female', 'male'))
    age = Column(Integer)

class Scores(Base):
    __tablename__ = 'score'
    stu_id = Column(Integer, ForeignKey('stuinfo.stu_id'))
    exam_id = Column(Integer, primary_key=True)
    score = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
