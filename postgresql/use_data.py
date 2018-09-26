import pandas as pd
import create_dataframes as cd

dfs = cd.get_dataframes()
regex_search = input('What regular expression would you like to search for?:  ')

each_col = {}
each_table = {}

# loop through every table in the database
for table_name in dfs:
  result_df = dfs[table_name].apply(lambda col: col.astype(str).str.contains(regex_search))

  # get the count of how many times the regex search was found in every column
  # looping through every row in each table and add to the each_col dictionary
  result_each_col = result_df.sum()
  for i, val in enumerate(result_each_col):
      each_col['Column-' + result_each_col.index[i] + ' (from Table-' + table_name + ')'] = val

  # get the counts of how many times the regex search was found in the table by summing up the
  # table's rows and add to the each_table dictionary
  each_table['Table-' + table_name] = result_each_col.sum()

# Now add all results to a new Dataframe
results = pd.Series()
results['Entire database'] = sum(each_table.values())
results = results.append(pd.Series(each_table))
results = results.append(pd.Series(each_col))

results.to_csv(r'.\\results.csv')
print('\nResults were printed to the results.csv file.' +
      '\n\n>> If in IPython you can use the original dictionary of dataframes' +
      '\n.. called dfs or the results dataframe called results.')