# The PostgreSQL can be integrated with Python using psycopg2 module.
# psycopg2 is a PostgreSQL database adapter for the Python programming language.

import psycopg2

DBASE = "testDB"
USERNAME = "postgres"
PASSWORD = "0000"
HOSTNAME = "localhost"
PORT = "5432"

conn = psycopg2.connect(database=DBASE, user=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT)

print("Opened database successfully")
