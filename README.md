PySearch
========

- A web-based search engine made from my class project
- Uses query likelihood model to score documents
- Performs no query processing, e.g. stemming, removing stopwords (yet)
- Uses Django for backend, jQuery/Bootstrap in front end
- Inverted index stored in MySQL database, along with full document text

To run
======

- Install Python, Django, and [MySQL-python](https://pypi.python.org/pypi/MySQL-python/)
- Install MySQL
- Load database files using db.sql (must be able to create schemas and tables and truncate tables) Note: database files must be placed in database directory (on my Windows machine this is C:\ProgramData\MySQL\MySQL Server 5.6\data\PySearch)
- Start Django server
- Open a web browser and navigate to `localhost:5000/search` and start searching
