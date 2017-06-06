from datetime import datetime
from models import dbsession, EmployeeInfo

employee_1 = EmployeeInfo(
        employee_id = 1,
        employee_name = 'Patrick',
        year = '2004',
        month = '05',
        day = '03', 
        date = datetime.strptime('2004 05 03', '%Y %m %d'),
        agency = 'F'
)
dbsession.add(employee_1)
dbsession.commit()
