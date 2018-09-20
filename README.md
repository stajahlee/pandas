# pandas  

🐼🐼🐼
## Utilizing the pandas library for data analysis

* The driver script for this repo is `use_data.py` which I run concurrently with a locally hosted postgresql database.

* The data for the database is `data/dvdrental.tar` and I have used pgAdmin 4 to host this for my python script to connect.

* Once the database is hosted at localhost:5432, the use_data.py script can be run with `python use_data.py` however in order to use the resulting dataframe, I run this from within Anaconda Prompt > `ipython` using the command `%run ./use_data.py` 

* My database uses the username _postgres_ and no password as there isn't anything sensitive in this practice use case.

*** 

After the script runs, I can use my newly generated dataframe `data` and analyze/manipulate the data.

***

### Here is an example of interaction with Anaconda Prompt

~~~
In [1]: %run ./use_data.py
username: postgres
password:
First 20 tables in the database:
0                     actor_info
1                  customer_list
2                      film_list
3     nicer_but_slower_film_list
4         sales_by_film_category
5                          staff
6                   pg_statistic
7                        pg_type
8                 sales_by_store
9                     staff_list
10                      category
11                 film_category
12                       country
13                         actor
14                      language
15                     inventory
16                       payment
17                        rental
18                          city
19                         store
Name: table_name, dtype: object
Choose a table that exists in this database to get started practicing pandas: language
Your adorable pandas dataframe is ready to use.
It is named...
wait for it...
data

In [2]: data.head()
Out[2]:
   language_id                  name         last_update
0            1  English              2006-02-15 10:02:19
1            2  Italian              2006-02-15 10:02:19
2            3  Japanese             2006-02-15 10:02:19
3            4  Mandarin             2006-02-15 10:02:19
4            5  French               2006-02-15 10:02:19

In [3]: %run ./use_data.py
First 20 tables in the database:
0                     actor_info
1                  customer_list
2                      film_list
3     nicer_but_slower_film_list
4         sales_by_film_category
5                          staff
6                   pg_statistic
7                        pg_type
8                 sales_by_store
9                     staff_list
10                      category
11                 film_category
12                       country
13                         actor
14                      language
15                     inventory
16                       payment
17                        rental
18                          city
19                         store
Name: table_name, dtype: object
Choose a table that exists in this database to get started practicing pandas: actor
Your adorable pandas dataframe is ready to use.
It is named...
wait for it...
data

In [4]: data.head()
Out[4]:
   actor_id first_name     last_name             last_update
0         1   Penelope       Guiness 2013-05-26 14:47:57.620
1         2       Nick      Wahlberg 2013-05-26 14:47:57.620
2         3         Ed         Chase 2013-05-26 14:47:57.620
3         4   Jennifer         Davis 2013-05-26 14:47:57.620
4         5     Johnny  Lollobrigida 2013-05-26 14:47:57.620

In [5]:
~~~

As you can see, after creating a dataframe and performing whatever analysis you want, running the script again will allow you to select a different table to generate a new dataframe.
