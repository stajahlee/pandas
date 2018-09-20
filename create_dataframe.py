import pandas as pd
from connect import db

# to get a dataframe showing all of the tables in the postgresql database
sql = '''
SELECT *
FROM information_schema.tables;
'''
df = pd.read_sql_query(sql, db)

# to get a dataframe showing all of the tables in the postgresql database
def chosen_table(table_name):
  query = '''
  SELECT *
  FROM {};
  '''.format(table_name)

  return pd.read_sql_query(query, db)
