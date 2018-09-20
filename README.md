# pandas  

🐼🐼🐼
## Utilizing the pandas library for data analysis

* The driver script for this repo is `use_data.py` which I run concurrently with a locally hosted postgresql database.

* The data for the database is `data/dvdrental.tar` and I have used pgAdmin 4 to host this for my python script to connect.

* Once the database is hosted at localhost:5432, the use_data.py script can be run with `python use_data.py` however in order to use the resulting dataframe, I run this from within Anaconda Prompt > `ipython` using the command `%run ./use_data.py` 

*** 

After the script runs, I can use my newly generated dataframe `data` and analyze/manipulate the data.
