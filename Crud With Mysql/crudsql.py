# type this to install in terminal
# to open terminal in vscode ctrl + ~ 
# then type the bellow command 
# pip install mysql-connector-python

import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    port = 'port',
    database="mydatabase"
)
# Create table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

# insert Data
# mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("John Doe", "johndoe@example.com")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Read Data

# mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

result = mycursor.fetchall()

for row in result:
    print(row)

# Update Data

# mycursor = mydb.cursor()

sql = "UPDATE customers SET email = %s WHERE name = %s"
val = ("newemail@example.com", "John Doe")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) updated.")


# Delete the Data

# mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE name = %s"
val = ("John Doe",)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

mydb.close()


