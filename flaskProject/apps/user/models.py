import sys,os
sys.path.append(r'C:\Users\Administrator\Desktop\vscode练习\flaskProject')
import datetime


from extend import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement = True)
    username = db.Column(db.String(15),nullable = False)
    password = db.Column(db.String(12),nullable = False)
    phone = db.Column(db.String(11),unique = True)
    # rdatetime = db.Column(db.DateTime,default = datetime.datetime.now())
    email = db.Column(db.String(20),default ='guocxian@163.com')

    
    def __str__(self):
        return self.rdatetime



if __name__ == '__main__':
    User = User()
    print(User)
