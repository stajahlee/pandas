import sqlite3
import pandas as pd
from connect import db


def get_dataframes():
  cursor = db.cursor()
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  tables = cursor.fetchall()
  dataframes = []
  for table_name in tables:
    table_name = table_name[0]
    table = pd.read_sql_query("SELECT * from %s" % table_name, db)
    dataframes.append(table)

  return dataframes
