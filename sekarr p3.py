import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = '',
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE latihan1")

print("database berhasil")
