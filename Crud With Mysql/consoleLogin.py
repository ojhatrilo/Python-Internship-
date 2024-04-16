# Before connecting with database
# create the credentials in workbench
# create database terminal;
# use terminal;
# create table data(name varchar(255), password varchar(255));



import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    passwd="root",
    database="terminal"
)
def register():
    fname=input("enter your name:")
    passwd=input("Create password:")
    cur=mydb.cursor() 
    sql="insert into data (name,password) values (%s,%s) "
    val=(fname,passwd)
    cur.execute(sql,val)
    mydb.commit()

def login():
    cur = mydb.cursor()
    fname = input("Enter your name: ")
    passwd = input("Enter password: ")
    
    # Use a parameterized query to check if the provided name and password exist in the database
    sql = "SELECT * FROM data WHERE name = %s AND password = %s"
    cur.execute(sql, (fname, passwd))
    result = cur.fetchone()
    
    if result:
        print("You are most welcome to the webinar.")
        
    else:
        print("Please register your name.")

while True:
    option="register-r\nlogin-l\nexit-e\n"
    user_option=input("Enter your option").lower()
    if user_option=="r":
        register()
    elif user_option=="l":
        login()
        break
    elif user_option=="e":
        break


    


 