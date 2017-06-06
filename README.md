# Make db

- Create a database called `fed_employment`. With postgres you can go
  into your terminal, type `psql` and then enter `CREATE DATABASE fed_employment` 
- Change database connection info in `settings.py`
- Run `python makedb.py` in the terminal to tell postgres to make the
  table specified in your `models.py` file.
- Modify the `addrows.py` file to add rows to the database.
