from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
# from app import app, db

# Create an application context



# class Base(DeclarativeBase):
#     pass

# db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Todo.db"
app.config['SQLALCHEMY_TRACK-MODIFICATIONS']=False

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()


class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"



@app.route('/')
def hello_world():
    todo = Todo(title = "First Todo", desc="Start investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
    # return 'Hello, World!'

@app.route('/Show')

def Show():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is Products page'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)