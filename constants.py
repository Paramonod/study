from sqlalchemy.orm import sessionmaker
import creditionals

db_user = creditionals.db_user
db_password = creditionals.db_password
db_host = 'it108.org'
db_name = 'study'

Session = sessionmaker()
session = Session()