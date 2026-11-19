import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS college")
cur.execute("USE college")

cur.execute("CREATE TABLE IF NOT EXISTS Student (id INT, name VARCHAR(50))")

cur.execute("DELETE FROM Student")

cur.execute("INSERT INTO Student VALUES (1, 'Amit')")
cur.execute("INSERT INTO Student VALUES (2, 'Riya')")

con.commit()

cur.execute("SELECT * FROM Student")

for row in cur.fetchall():
    print(row)

con.close()
