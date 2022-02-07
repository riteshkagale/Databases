import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

cur = con.cursor()

cur.execute("SHOW DATABASES")

for x in cur:
  print(x)
  