from create_dataframes import get_dataframes

for idx, df in enumerate(get_dataframes()):
  # we now have all of the tables in the database contained in a list of pandas dataframes
  # we can iterate through this list and do whatever needs to be done with the data in 
  # all of the dataframes
  
  print ('Dataframe ' + str(idx) + ':')
  print (df.head(1))
