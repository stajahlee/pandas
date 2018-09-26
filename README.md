# pandas   

🐼🐼🐼
## Utilizing the pandas library for data analysis

### PostgreSQL version

* The driver script for this repo is `use_data.py` which is run concurrently with a locally hosted postgresql database.

* The data for the postgresql database is `data/dvdrental.tar` and pgAdmin 4 hosts this for the python script to connect.

* Once the database is hosted at `localhost:5432`, the `use_data.py` script can be run with `python use_data.py`.

* In this case, the database uses the username _postgres_ and no password as there isn't anything sensitive in this practice use case.

***

After the program begins, it will require you to input a regex pattern to search the database, then output those results to a new file titled `results.csv`.

_If further analysis should be done on the data, the dataframe `results` can be used directly in the IPython REPL, along with the `dfs` dictionary of all dataframes from the database, as can be seen in the following example._ 

***

### Here is an example of running the program with python, as well as interaction with IPython REPL

~~~
(base) C:\Users\stajah.hoeflich\python_projects\pandas>python postgresql/use_data.py
username: postgres
password:
What regular expression would you like to search for?:  James
Results were printed to the results.csv file.

(base) C:\Users\stajah.hoeflich\python_projects\pandas>ipython
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %run ./postgresql/use_data.py
username: postgres
password:
What regular expression would you like to search for?:  James

Results were printed to the results.csv file.

>> If in IPython you can use the original dictionary of dataframes
.. called dfs or the results dataframe called results.

In [2]: results.head()
Out[2]:
Entire database        3
Table-staff            0
Table-category         0
Table-film_category    0
Table-country          0
dtype: int64

In [3]: for df in dfs:
   ...:     print (df)
   ...:
staff
category
film_category
country
actor
language
inventory
payment
rental
city
store
film
address
film_actor
customer

In [4]: city = dfs['city']

In [5]: city.head()
Out[5]:
   city_id                city  country_id         last_update
0        1  A Corua (La Corua)          87 2006-02-15 09:45:25
1        2                Abha          82 2006-02-15 09:45:25
2        3           Abu Dhabi         101 2006-02-15 09:45:25
3        4                Acua          60 2006-02-15 09:45:25
4        5               Adana          97 2006-02-15 09:45:25

In [6]:
~~~

See this [postgresql tutorial](http://www.postgresqltutorial.com/postgresql-sample-database/) for more details about the schema and also to see where I downloaded the database.

***

***

### Local CSV version

* The driver script for this repo is `use_data.py` which uses a local `csv` file in the `local_csv` directory.
* The data for the local_csv version is `public-health.csv` which was downloaded from [Health IT Dashboard](https://dashboard.healthit.gov/api/api.php) .

***

After the program begins, it will require you to input a regex pattern to search the database, then output those results to a new file titled `results.csv`.

_If further analysis should be done on the data, the dataframe `results` can be used directly in the IPython REPL, along with the original `df` dataframe created from the csv data, as can be seen in the following example._ 

*** 

~~~
(base) C:\Users\stajah.hoeflich\python_projects\pandas>python local_csv/use_data.py
What regular expression would you like to search for?:  [0-9]+.[0-9]+

Results were printed to the results.csv file.

>> If in IPython you can use the original dataframe
.. called df or the results dataframe called results.

(base) C:\Users\stajah.hoeflich\python_projects\pandas>ipython
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %run ./local_csv/use_data.py
What regular expression would you like to search for?:  [0-9]+.[0-9]+

Results were printed to the results.csv file.

>> If in IPython you can use the original dataframe
.. called df or the results dataframe called results.

In [2]: results.head()
Out[2]:
Entire table                  988
Column-region                   0
Column-region_code              0
Column-period                 156
Column-atleast_one_measure    104
dtype: int64

In [3]: df.head()
Out[3]:
    region region_code               ...                stage_2_hospitals_all_measures  stage_1_hospitals_all_measures
0  Alabama          AL               ...                                          0.00                            0.00
1  Alabama          AL               ...                                          0.96                            0.17
2  Alabama          AL               ...                                           NaN                             NaN
3   Alaska          AK               ...                                          0.00                            0.00
4   Alaska          AK               ...                                          1.00                            0.00

[5 rows x 10 columns]

In [4]:
~~~

***
***

_Once again, this repo is meant for learning purposes only and is in no way meant to guide anyone to Pandas mastership._