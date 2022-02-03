import psycopg2

DBASE = "postgres"
USERNAME = "postgres"
PASSWORD = "0000"
HOSTNAME = "localhost"
PORT = "5432"

con = psycopg2.connect(database=DBASE, user=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT)
print("Database opened successfully")

cur = con.cursor()

cur.execute("DELETE from STUDENT where ADMISSION=3420;")
con.commit()
print("Total deleted rows:", cur.rowcount)

cur.execute("SELECT admission, name, age, course, department from STUDENT")
rows = cur.fetchall()
for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Deletion successful")
con.close()
