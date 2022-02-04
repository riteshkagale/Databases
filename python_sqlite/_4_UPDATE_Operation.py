import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cur = conn.cursor()

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cur.execute("SELECT id, name, address, salary from COMPANY")
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
