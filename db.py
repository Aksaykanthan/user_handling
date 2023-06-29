import mysql.connector as mysql
import datetime

db = mysql.connect(host = 'localhost',user='root',password = '123456',database = 'aksay')
c = db.cursor()


def User(name,email,password):
    
    script = f'INSERT INTO users(name,email,password) VALUES("{name}","{email}","{password}");'
    c.execute(script)
    db.commit()
    print('done')

def login(user,password):
    c.execute('SELECT name, password FROM user WHERE name = "{user}" AND password = "{password}";')
    data = c.fetchall()
    
    if data:
        c.execute(f'INSERT INTO log VALUES("{user}","{}")')
        
    