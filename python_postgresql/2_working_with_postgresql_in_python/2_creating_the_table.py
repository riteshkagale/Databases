import psycopg2

DBASE = "postgres"
USERNAME = "postgres"
PASSWORD = "0000"
HOSTNAME = "localhost"
PORT = "5432"

con = psycopg2.connect(database=DBASE, user=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT)
print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT
      (ADMISSION INT PRIMARY KEY    NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      COURSE        CHAR(50),
      DEPARTMENT        CHAR(50));''')
print("Table created successfully")

con.commit()
con.close()
