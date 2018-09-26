import sqlite3
import pandas as pd
from connect import db

def get_dataframes():
  dataframes = {}
  tables = db.table_names()
  for table in tables:
    sql_query = 'SELECT * from {}'.format(table)
    df = pd.read_sql_query(sql_query, db)
    dataframes[table] = df

  return dataframes
