from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'        
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)
csrf = CSRFProtect(app) 
app.secret_key = b'_53oi3uriq9pifpff;apl'

@app.route('/',methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']
        password = userdetails['password']
        phone = userdetails['phone']
        cur = mysql.connection.cursor()
        cur.execute("insert into data(name, email,password,phone) VALUES(%s, %s,%s,%s)", (name, email,password,phone))
        mysql.connection.commit()
        cur.close()
        return redirect('/login')

    return render_template('Register.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        logindetails = request.form
        name = logindetails['name']
        password = logindetails['password']
        cur = mysql.connection.cursor()
        sql = "select * from data WHERE name=%s AND password=%s"
        cur.execute(sql, (name, password))
        result = cur.fetchone()
        mysql.connection.commit()
        cur.close()

        if result:
            return '<h1>LOGIN IS SUCESSFULL</h1>'
        else:
            return redirect('/')

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)













