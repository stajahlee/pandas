from create_dataframes import get_dataframes
import user_choices as user

dfs = get_dataframes()
print ('You now have a dictionary of dataframes called dfs with the following keys:\n' + str(dfs.keys()))
