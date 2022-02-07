import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

cur = con.cursor()

cur.execute("CREATE DATABASE mydatabase")

