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
            "VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')")
cur.execute("INSERT INTO STUDENT "
            "(ADMISSION,NAME,AGE,COURSE,DEPARTMENT) "
            "VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')")
cur.execute("INSERT INTO STUDENT "
            "(ADMISSION,NAME,AGE,COURSE,DEPARTMENT) "
            "VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')")
cur.execute("INSERT INTO STUDENT "
            "(ADMISSION,NAME,AGE,COURSE,DEPARTMENT) "
            "VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')")

con.commit()
print("Records inserted successfully")
con.close()
