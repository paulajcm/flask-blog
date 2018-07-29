# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from flask_blog import app, db

# models
from flask_blog.author.models import *
from flask_blog.blog.models import *


class UserTest(unittest.TestCase):
    def setUp(self):
        print("Setup-------")
        db_username = app.config['DB_USERNAME']
        db_password = app.config['DB_PASSWORD']
        db_host = app.config['DB_HOST']
        self.db_uri = "mysql+pymysql://%s:%s@%s/" % (db_username, db_password, db_host)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['BLOG_DATABASE_NAME'] = 'test_blog'
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('CREATE DATABASE ' + app.config['BLOG_DATABASE_NAME'])
        self.app = app.test_client()

    def tearDown(self):
        print("Tear down-------")
        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('DROP DATABASE ' + app.config['BLOG_DATABASE_NAME'])

    def create_blog(self):
        return self.app.post('/setup', data=dict(
            name='my test blog',
            fullname='tester doe',
            email='tester3@email.com',
            username='tester2',
            password='tester',
            confirm='tester'
        ), follow_redirects=True)

    def test_create_blog(self):
        rv = self.create_blog()
        print(rv.data)
        assert 'Blog created' in str(rv.data)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), folow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        self.create_blog()
        rv = self.login('tester', "tester")
        assert 'User tester' in str(rv.data)

# TODO solve tearDown issue
if __name__ == '__main__':
    unittest.main()
