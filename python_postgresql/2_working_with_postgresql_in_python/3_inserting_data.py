import psycopg2

DBASE = "postgres"
USERNAME = "postgres"
PASSWORD = "0000"
HOSTNAME = "localhost"
PORT = "5432"

con = psycopg2.connect(database=DBASE, user=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT)
print("Database opened successfully")

cur = con.cursor()

cur.execute("INSERT INTO STUDENT "
            "(ADMISSION,NAME,AGE,COURSE,DEPARTMENT) "
            "VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")

con.commit()
print("Record inserted successfully")
con.close()
