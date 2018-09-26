import pandas as pd

df = pd.read_csv(R'C:\Users\stajah.hoeflich\python_projects\pandas\local_csv\data\public-health.csv')

regex_search = input('What regular expression would you like to search for?:  ')

each_col = {}

result_df = df.apply(lambda col: col.astype(str).str.contains(regex_search))

# get the count of how many times the regex search was found in every column
# looping through every row in each table and add to the each_col dictionary
result_each_col = result_df.sum()
for i, val in enumerate(result_each_col):
    each_col['Column-' + result_each_col.index[i]] = val

# Now add all results to a new Dataframe
results = pd.Series()
results['Entire table'] = sum(each_col.values())
results = results.append(pd.Series(each_col))

results.to_csv(r'.\\results.csv')
print('\nResults were printed to the results.csv file.' +
      '\n\n>> If in IPython you can use the original dataframe' +
      '\n.. called df or the results dataframe called results.')
