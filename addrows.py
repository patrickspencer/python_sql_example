from models import dbsession, EmployeeInfo
from datetime import datetime

year = '2004'
month = '05'
day = '03'
date = "{} {} {}".format(year, month, day)

employee_1 = EmployeeInfo(
        employee_id = 1,
        employee_name = 'Patrick',
        year = year,
        month = month,
        day = date, 
        date = datetime.strptime(date, '%Y %m %d'),
        agency = 'F'
)
dbsession.add(employee_1)
dbsession.commit()
