from create_dataframe import df, chosen_table

def get_table(dataframe):
  while True:
    table_choice = input('Choose a table that exists ' 
                         'in this database to get started ' 
                         'practicing pandas: ')
    if table_choice in dataframe['table_name'].values:
      return table_choice
    else:
      continue  

print('First 20 tables in the database:')
print(df['table_name'].head(20))

table_choice = get_table(df)

data = chosen_table(table_choice)
print('Your adorable pandas dataframe is ready to use.\n'
      'It is named...\nwait for it...\ndata')