import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
print("Opened database successfully")

cur = con.cursor()

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
con.commit()
print("Total number of rows updated :", cur.rowcount)

cur.execute("SELECT id, name, address, salary from COMPANY")
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
con.close()
