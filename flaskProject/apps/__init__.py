import settings
from apps.user.view import user_bp
from extend import db
from flask import Flask


def creat_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')

     # flask的配置
    app.config.from_object(settings.DevelopmentConfig)

    # 绑定蓝图
    app.register_blueprint(user_bp)

    # 把flask和映射绑定
    db.init_app(app)

    return app