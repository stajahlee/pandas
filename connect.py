import getpass

from database import connect

username = input('username: ')
password = getpass.getpass('password: ')

db = connect(username, password)