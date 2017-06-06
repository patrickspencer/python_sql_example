# Make db

- Alter the file `models.py` so the attributes in the class
  `EmploymentInfo` match the columns you want in your data base. If you
  change the name `EmploymentInfo` in `models.py` then also change it in
  `makedb.py` `addrows.py`.
- Create a database called `fed_employment`. With postgres you can go
  into your terminal, type `psql` and then enter `CREATE DATABASE
  fed_employment;` (don't forget the semicolon, like I did) 
- Change database connection info in `settings.py`. If postgres is on
    your computer then
- Run `python makedb.py` in the terminal to tell postgres to make the
  table specified in your `models.py` file.
- Modify the `addrows.py` file to add rows to the database.

# Interacting with the db

## Getting data from sql table in the form of python objects

```python
from models import dbsession
third_employee = dbsession.query(EmployeeInfo) \
               .filter(emploee_id == 3).first()
print(third_employee.employee_name)
>>> Bob
all_employess = dbsession.query(EmployeeInfo).all()
```

## Using raw sql
```python
from models import engine
res = engine.execute('SELECT * FROM employee_info;').fetchall()
```

## Read sql table into Pandas
```python
from models import engine
df = pd.read_sql_query('SELECT * FROM "employee_info"', con=engine)
```

