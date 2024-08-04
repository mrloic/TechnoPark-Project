from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_required

from app import app, db
from models import User, Message


class MyAdminIndexView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    @expose('/')
    def index(self):
        users = User.query.all()
        return self.render('admin/index.html', users=users)


class UserAdmin(ModelView):
    column_list = ('username', 'email', 'password', 'avatar', 'admin')
    column_labels = dict(
        username='Username',
        email='Email',
        password='Password',
        avatar='Avatar',
        admin='Admin'
    )
    column_sortable_list = ('username', 'email', 'password', 'avatar', 'admin')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    @expose('/')
    def index(self):
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        users = User.query.all()
        return self.render('admin/user_view.html', users=users)


class MessageAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

    column_list = ('sender.username', 'receiver.username', 'text', 'image', 'timestamp')
    column_labels = {
        'sender.username': 'Sender',
        'receiver.username': 'Receiver',
        'text': 'Message Text',
        'image': 'Image',
        'timestamp': 'Timestamp'
    }

    @expose('/')
    def index(self):
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        users = User.query.all()
        return self.render('admin/message_view.html', messages=messages)


admin = Admin(app, name='MyAdmin', index_view=MyAdminIndexView(), template_mode='bootstrap4')
admin.add_view(UserAdmin(User, db.session, name='Users'))
admin.add_view(MessageAdmin(Message, db.session, name='Messages'))
