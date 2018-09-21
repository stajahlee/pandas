# pandas  

🐼🐼🐼
## Utilizing the pandas library for data analysis

* The driver script for this repo is `use_data.py` which is run concurrently with a locally hosted postgresql database.

* The data for the database is `data/dvdrental.tar` and pgAdmin 4 hosts this for the python script to connect.

* Once the database is hosted at `localhost:5432`, the `use_data.py` script can be run with `python use_data.py` however in order to use the resulting dataframe, run this from within Anaconda Prompt > `ipython` using the command `%run ./use_data.py` 

* In this case, the database uses the username _postgres_ and no password as there isn't anything sensitive in this practice use case.

*** 

After the script runs, use the newly generated python dictionary of dataframes `dfs`.

By using the key of the table data desired, create a dataframe as in the following example.

***

### Here is an example of interaction with Anaconda Prompt

~~~
%run ./use_data.py
username: postgres
password:
You now have a dictionary of dataframes called dfs with the following keys:
dict_keys(['staff', 'category', 'film_category', 'country', 'actor', 'language', 'inventory', 'payment', 'rentatal', 'city', 'store', 'film', 'address', 'film_actor', 'customer'])

In [2]: language_df = dfs['language']

In [3]: language_df.head()
Out[3]:
   language_id                  name         last_update
0            1  English              2006-02-15 10:02:19
1            2  Italian              2006-02-15 10:02:19
2            3  Japanese             2006-02-15 10:02:19
3            4  Mandarin             2006-02-15 10:02:19
4            5  French               2006-02-15 10:02:19
~~~
