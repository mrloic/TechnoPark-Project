from app import app


# from models import User, Message


@app.route('/api/register', methods=['POST'])
def api_register():
    pass
    # data = request.get_json()
    # hashed_password = generate_password_hash(data['password'])
    # new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    # db.session.add(new_user)
    # db.session.commit()
    # return jsonify({'message': 'New user created!'})


@app.route('/api/login', methods=['POST'])
def api_login():
    pass
    # data = request.get_json()
    # user = User.query.filter_by(email=data['email']).first()
    # if user and check_password_hash(user.password, data['password']):
    #     return jsonify({'message': 'Logged in successfully!'})
    # else:
    #     return jsonify({'message': 'Login failed!'}), 401


@app.route('/api/messages', methods=['GET'])
def api_get_messages():
    pass
    # messages = Message.query.all()
    # output = []
    # for message in messages:
    #     message_data = {'text': message.text, 'image': message.image, 'user_id': message.user_id,
    #                     'timestamp': message.timestamp}
    #     output.append(message_data)
    # return jsonify({'messages': output})


@app.route('/api/message', methods=['POST'])
def api_send_message():
    pass
    # data = request.get_json()
    # new_message = Message(text=data['text'], user_id=data['user_id'])
    # db.session.add(new_message)
    # db.session.commit()
    # return jsonify({'message': 'New message sent!'})
