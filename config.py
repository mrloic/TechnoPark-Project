import os


class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://loic:12345@localhost/technopark'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER_IMAGES = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'images')
    UPLOAD_FOLDER_AVATARS = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'avatars')
