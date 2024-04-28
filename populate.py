import datetime
# from peewee import *
# from flask import Flask
# from flask_peewee import RestAPI
from flask import Flask

from peewee import *
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from models import User, Activity, Expense


db = MySQLDatabase('pollux', host='localhost', port=3306, user='pollux', password='password')

# app = Flask(__name__)
# app.config.from_object(__name__)
# db = Database(app)

db.connect()

db.create_tables([User, Activity, Expense])

User.insert(username='mothman', first_name='Moth', last_name='Man').execute()
User.insert(username='manmoth', first_name='Man', last_name='Moth').execute()
User.insert(username='sasquatch', first_name='Last', last_name='Link').execute()
User.insert(username='nessie', first_name='Loch', last_name='Ness').execute()
User.insert(username='dpool', first_name='Wade', last_name='Wilson').execute()

Activity.insert(description='Vacation', user=2).execute()
Activity.insert(description='Party', user=3).execute()
Activity.insert(description='Bills', user=4).execute()

Expense.insert(description='hotel', activity=1, paid_by=4).execute()
Expense.insert(description='restaurant', activity=1, paid_by=3).execute()
Expense.insert(description='snacks', activity=2, paid_by=1).execute()
Expense.insert(description='drinks', activity=2, paid_by=2).execute()
Expense.insert(description='rent', activity=3, paid_by=5).execute()
Expense.insert(description='electrical', activity=3, paid_by=1).execute()

