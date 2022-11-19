from flask import Blueprint, jsonify, url_for,render_template,request
from apps.user.models import User
from extend import db


user_bp =Blueprint('user', __name__)


@user_bp.route('/')
def user_center():
    return jsonify({'zhangda':'hao'})
    
@user_bp.route('/register',methods = ['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            user = User()
            user.username = username
            user.password = password
            user.phone = phone
            # 将对象给db的session，类似于一个缓存
            db.session.add(user)
            db.session.commit()
            return '用户注册成功'
            
        else:
            return '密码不一致'

    return render_template('user/register.html')

