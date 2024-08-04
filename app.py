from flask import Flask
from flask_babel import Babel
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

babel = Babel()

app = Flask(__name__)
app.config.from_object('config.Config')

babel.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

# from routes import *
# from api import *
# from admin import admin  # добавляем импорт

if __name__ == '__main__':
    app.run(debug=True)
