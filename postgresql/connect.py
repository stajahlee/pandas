import getpass

from database import get_engine

username = input('username: ')
password = getpass.getpass('password: ')

db = get_engine(username, password)