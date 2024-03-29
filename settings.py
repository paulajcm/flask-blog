import os


SECRET_KEY = 'secretkey'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'admin'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_IMAGES_DEST = '/home/paula/projects/devops/flask_blog/flask_blog/static/images'
UPLOADED_IMAGES_URL = '/static/images/'