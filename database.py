import mysql.connector
DB = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "viru8000@",
    database = "STUDENT_DB"
)
print ("database connected successfully!")