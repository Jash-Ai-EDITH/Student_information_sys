import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jash@2512",
        database="sisdb"
    )
    print("Connection successful!")
    conn.close()
except mysql.connector.Error as err:
    print("Connection failed:", err)
