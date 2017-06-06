import models
from models import engine

# This next line creates the table if it doesn't exists already.
# The database specified in setting.py must already exist before you run this.
models.EmployeeInfo.metadata.create_all(engine)
