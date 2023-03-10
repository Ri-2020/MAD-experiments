import sqlalchemy
import os
from sqlalchemy import create_engine
from sqlalchemy import Table , Column , String, Integer , ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from flask import Flask
from flask import render_template
from flask import request


curr_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer , autoincrement=True , primary_key=True)
    username = Column(String , unique=True)
    email = Column(String , unique=True)
    # articles = relationship("Article" , secondary="article_authors")

class Article(Base):
    __tablename__ = "article"
    article_id = Column(Integer , autoincrement=True , primary_key=True)
    title = Column(String)
    content = Column(String)
    authors = relationship("User" , secondary="article_authors")

class Article_Author(Base):
    __tablename__ = "article_authors"
    user_id = Column(Integer , ForeignKey("user.user_id"), primary_key= True , nullable=False)
    article_id = Column(Integer , ForeignKey("article.article_id"), primary_key=True , nullable=False)

engine = create_engine("sqlite:///./newd.sqlite3")

def addArticle(article , user):
    with Session(engine , autoflush=False) as session:
        session.begin()
        try:
            print("--------- ADDING ARTICLE --------------")
            session.add(article)
            session.flush()

            print("Article id: " ,article.article_id)
            print("--------- ADDING ARTICLE AUTHOR --------------")
            article_author = Article_Author( user_id = user, article_id = article.article_id  )
            session.add(article_author)
        except:
            session.rollback()
        else:
            session.commit()
        session.close()

def addUser(user):
    with Session(engine , autoflush=False) as session:
        session.begin()
        try:
            print("Adding user")
            session.add(user)
            session.flush()
            print(user.user_id)
        except:
            print("Error while adding user")
            session.rollback()
        else:
            print("user created successfully ")
            session.commit()
    session.close()

def getAllArticles():
    stmt = select(Article)
    articles = []
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            # print(row)
            articles.append(row)
    return articles

def printAllUsers():
    stmt = select(User)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)



@app.route("/" , methods =["GET", "POST"])
def indexFunction():
    articles = getAllArticles()
    print("Ok tested")
    return render_template("index.html",  articles= articles)


if __name__ == "__main__":
    app.debug = True
    app.run()

