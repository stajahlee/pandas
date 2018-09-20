import urllib
from sqlalchemy import create_engine
from params import params

def connect(username, password):           
    conn_str = 'postgresql://{}:{}@{}:{}/{}'
    conn_str = conn_str.format(username, password, params['server'], str(params['port']), params['database'])

    db = create_engine(conn_str)
    return db