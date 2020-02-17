from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)



class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200), nullable=False)
  completed = db.Column(db.Integer, default=0)
  data_created = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Task %r>' % self.id



@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method=='POST':
    task_content = request.form['content']
    new_task = Todo(content=task_content)
    
    
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')

    except:
      return 'There was an issue adding your task'

  else:
    tasks = Todo.query.order_by(Todo.data_created).all()
    return render_template('index.html', tasks=tasks)


# Run Server
if __name__=="main":
    app.run(debug=True)


