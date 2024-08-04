from app import db
from flask_login import UserMixin
from datetime import datetime


class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    middle_name = db.Column(db.String(50), unique=False, nullable=True)
    division = db.Column(db.String(150), unique=False, nullable=False)
    role = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    work_amount = db.Column(db.Integer, unique=False, nullable=False)
    salary = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(512), nullable=False)

    def __init__(self, last_name, first_name, middle_name, division, role, email, phone, work_amount, salary, status,
                 password):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.division = division
        self.role = role
        self.email = email
        self.phone = phone
        self.work_amount = work_amount
        self.salary = salary
        self.status = status
        self.password = password


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_number = db.Column(db.Integer, nullable=False)
    from_whom_id = db.Column(db.String, db.ForeignKey('employee.id'), nullable=True)
    description = db.Column(db.Text, nullable=True)
    send_time = db.Column(db.DateTime, default=datetime.utcnow)
    time_limit = db.Column(db.DateTime, default=datetime.utcnow)
    total_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), unique=False, nullable=False, default='wait')
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    image = db.Column(db.String(100))

    def __init__(self, work_number, from_whom_id, description, send_time, time_limit, total_time, status, employee_id, image):
        self.work_number = work_number
        self.from_whom_id = from_whom_id
        self.description = description
        self.send_time = send_time
        self.time_limit = time_limit
        self.total_time = total_time
        self.status = status
        self.employee_id = employee_id
        self.image = image


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    object_name = db.Column(db.String(50), unique=False, nullable=False)
    type = db.Column(db.String(50), unique=False, nullable=False)
    buy_date = db.Column(db.DateTime, default=datetime.utcnow)
    break_count = db.Column(db.Integer, nullable=False)
    recovery_date = db.Column(db.DateTime, default=datetime.utcnow)
    room_number = db.Column(db.String(50), nullable=False)

    def __init__(self, object_name, type, buy_date, break_count, recovery_date, room_number):
        self.object_name = object_name
        self.type = type
        self.buy_date = buy_date
        self.break_count = break_count
        self.recovery_date = recovery_date
        self.room_number = room_number



