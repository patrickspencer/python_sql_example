import models
from models import engine

#this next line creates the database if it doesn't exists already
models.EmployeeInfo.metadata.create_all(engine)
