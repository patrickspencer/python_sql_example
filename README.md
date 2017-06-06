# Make db table and adding rows

- Alter the file `models.py` so the attributes in the class
  `EmploymentInfo` match the columns you want in your data base. If you
  change the name `EmploymentInfo` in `models.py` then also change the
  references to it in `makedb.py` and `addrows.py`.
- Create your database. In this example it's called "fed_employment".
  With postgres you can go into your terminal, type `psql` and then
  enter `CREATE DATABASE fed_employment;` (don't forget the semicolon,
  like I do so often) 
- Change database connection info in `settings.py`. If you connect to
  postgres on your computer then the host is probably "localhost" and
  the port is probably "5432".
- Run `python makedb.py` in the terminal to tell postgres to make the
  table specified in your `models.py` file.
- Modify the `addrows.py` file to add rows to the database.

# Interacting with the db

## Getting data from sql table in the form of python objects

```python
from models import dbsession
third_employee = dbsession.query(EmployeeInfo).filter(employee_id == 3).first()
print(third_employee.employee_name)
>>> Bob
all_employees = dbsession.query(EmployeeInfo).all()
for employee in all_employees:
    print(employee.id)
>>> 1
>>> 2
.  
.  
.
```

[More sqlalchemy examples](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html)


## Using raw sql queries
```python
from models import engine
res = engine.execute('SELECT * FROM employee_info;').fetchall()
```

Here `res` is only a list of rows which are themselves lists. You can't
say something like `res.employee_id` because `res` is not an python object.

## Read sql table into Pandas

This is useful if you want to manipulate the data fast with Pandas.

```python
from models import engine
df = pd.read_sql_query('SELECT * FROM "employee_info"', con=engine)
```

