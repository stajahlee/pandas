import sqlite3
import pandas as pd
from connect import db

def get_dataframes():
  dataframes = []
  for table_name in db.table_names():
     table = pd.read_sql_query("SELECT * from %s" % table_name, db)
     dataframes.append(table)

  return dataframes
