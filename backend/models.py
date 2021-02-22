import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
'''
if this your first test uncomment
this to setup the test db then comment it again
'''
# database_name = "trivia_test"
'''
to start test for first time comment
the database var below after finish uncomment it
'''
database_name = "trivia"
database_path = "postgresql://{}:{}@{}/{}".format(
    'noob', '123', 'localhost:5432', database_name
    )

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
    os added in config file can be accessed from any file
'''
os.environ['SQLALCHEMY_DATABASE_URI'] = database_path
os.environ['SQLALCHEMY_DATABASE_URI'] = 'False'
db_path = os.getenv('SQLALCHEMY_DATABASE_URI')


def setup_db(app, database_path=database_path):

    # os.environ['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Question(db.Model):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    category = Column(String)
    difficulty = Column(Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
            }


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type):
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }
