# contacts
Simple Python Contact Book

Runs in Python3. Make sure you've initialized "contacts.db" in the same folder as the script, or clone the empty database from this repository.

To check contacts in sqlite3:

$ cd /path/to/directory
$ sqlite3 
> .open contacts.db
> SELECT * FROM contacts;

Note: the database in this repo is empty, so you'll need to run the script to add entries.
