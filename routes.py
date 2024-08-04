from flask import render_template, redirect, url_for
# from models import User, Message
# from forms import RegistrationForm, LoginForm, MessageForm, UpdateUsernameForm, SettingsForm
from flask_login import current_user, logout_user, login_required

from app import app, login_manager


@login_manager.user_loader
def load_user(user_id):
    pass
    # return User.query.get(int(user_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    #form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_password = generate_password_hash(form.password.data)
    #     user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Your account has been created!', 'success')
    #     return redirect(url_for('login'))
    # return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass
    # if current_user.is_authenticated:
    #     return redirect(url_for('chat'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and check_password_hash(user.password, form.password.data):
    #         login_user(user)
    #         return redirect(url_for('chat'))
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')
    # return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    pass


#     message_form = MessageForm()
#     if message_form.validate_on_submit():
#         image = message_form.image.data
#         filename = None
#         if image:
#             filename = secure_filename(image.filename)
#             image.save(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename))
#             print(filename)
#
#         message = Message(
#             sender_id=current_user.id,
#             receiver_id=message_form.receiver.data,
#             text=message_form.text.data,
#             image=filename
#         )
#         db.session.add(message)
#         db.session.commit()
#         flash('Message sent!', 'success')
#         return redirect(url_for('chat'))
#
#     messages = Message.query.filter(
#         (Message.receiver_id == current_user.id) | (Message.sender_id == current_user.id)).all()
#     return render_template('chat.html', message_form=message_form, messages=messages)


@app.route('/get_messages', methods=['GET'])
@login_required
def get_messages():
    pass
    # messages = Message.query.filter(
    #     (Message.receiver_id == current_user.id) | (Message.sender_id == current_user.id)
    # ).all()
    # messages_data = [{
    #     'sender': message.sender.username,
    #     'receiver': message.receiver.username,
    #     'text': message.text,
    #     'image': message.image
    # } for message in messages]
    # return jsonify(messages_data)


@app.route('/clear_messages', methods=['POST'])
@login_required
def clear_messages():
    pass
    # Message.query.filter(
    #     (Message.receiver_id == current_user.id) | (Message.sender_id == current_user.id)
    # ).delete()
    # db.session.commit()
    # return '', 204


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    pass
    # settings_form = SettingsForm(obj=current_user)
    # if settings_form.validate_on_submit():
    #     avatar = settings_form.avatar.data
    #     if avatar:
    #         if avatar:
    #             filename = secure_filename(avatar.filename)
    #             unique_filename = f"{current_user.username}_avatar.{filename.split('.')[1]}"
    #             avatar.save(os.path.join(app.config['UPLOAD_FOLDER_AVATARS'], unique_filename))
    #             current_user.avatar = unique_filename
    #     current_user.username = settings_form.username.data
    #     current_user.email = settings_form.email.data
    #     if settings_form.password.data:
    #         current_user.password = generate_password_hash(settings_form.password.data)
    #     db.session.commit()
    #     flash('Your changes have been saved.', 'success')
    #     return redirect(url_for('chat'))
    # elif request.method == 'GET':
    #     settings_form.username.data = current_user.username
    #     settings_form.email.data = current_user.email
    # return render_template('settings.html', title='Settings', settings_form=settings_form)


@app.route('/admin')
@login_required
def admin_dashboard():
    pass
    # if not current_user.is_admin():
    #     return redirect(url_for('chat'))
    # users = User.query.all()
    # return redirect(url_for('admin.index'))


@app.route('/admin/make_admin/<int:user_id>')
@login_required
def make_admin(user_id):
    pass
    # if not current_user.is_admin():
    #     return redirect(url_for('chat'))
    # user = User.query.get(user_id)
    # if user:
    #     user.admin = True
    #     db.session.commit()
    # return redirect(url_for('admin.index'))


@app.route('/admin/remove_admin/<int:user_id>')
@login_required
def remove_admin(user_id):
    pass
    # if not current_user.is_admin():
    #     return redirect(url_for('chat'))
    # user = User.query.get(user_id)
    # if user:
    #     user.admin = False
    #     db.session.commit()
    # return redirect(url_for('admin.index'))


@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html'), 401


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
