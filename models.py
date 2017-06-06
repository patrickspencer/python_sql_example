import settings
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, \
        String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect, desc, exists

engine = create_engine(settings.DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
dbsession = Session()

Base = declarative_base()

class EmployeeInfo(Base):
    __tablename__ = 'employee_info'

    id                = Column(Integer, primary_key=True)
    employee_id       = Column(String)
    employee_name     = Column(String)
    year              = Column(String)
    month             = Column(String)
    day               = Column(String)
    date              = Column(DateTime)
    agency            = Column(String)
    sub_agency        = Column(String)
    state             = Column(Integer)
    country           = Column(String)
    age               = Column(String)
    education_level   = Column(String)
    pay_plan          = Column(String)
    years_since       = Column(String)
    occupation        = Column(String)
    occupational_cat  = Column(String)
    adjusted_basic_pay = Column(Float)
    supervisory_status = Column(Integer)
    type_of_appointment = Column(Integer)
    work_schedule     = Column(String)
    NSFTP             = Column(Integer)

    def __repr__(self):
       return "<EmployeeInfo(employee_id='%s', employee_name='%s')>" \
               % (self.employee_id, self.employee_name)
