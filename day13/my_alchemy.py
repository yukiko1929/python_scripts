from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy import Date
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root@127.0.0.1/alchemy?charset=utf8',
    encoding = 'utf8',
    echo = True   #debug mode: show detailed data on screen. should be False in real working place
)

Base = declarative_base()   #create base class
Session = sessionmaker(bind=engine)   # create a session class and bind it to engine


class Department(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True)
    staff_name = Column(String(20))
    email = Column(String(20))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))



class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    sta_id = Column(Integer, ForeignKey('staff.staff_id'))
    sta_name = Column(String(20))
    basic = Column(Integer)
    bonus = Column(Integer)
    comment = Column(String(50))


if __name__ == '__main__':
    Base.metadata.create_all(engine)


