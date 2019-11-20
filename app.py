from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
import webbrowser
from threading import Timer

app = Flask(__name__)

import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(), nullable=False)
    time = db.Column( db.String(), nullable = False, default = "30.2155")

    def __repr__(self):
        return f"id:{self.id}, task:{self.task},time:{self.time}"

@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        new_task1 = request.form.get('task')
        time = request.form.get('time')
        try:
            t =Task(task=new_task1, time = time )              
            db.session.add(t)
            db.session.commit()
        except:
            return "There was a problem"
        return redirect('/')
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods = ['POST','GET'])
def update(id):
    taask = Task.query.get_or_404(id)    
    if request.method == 'POST':
        taask.task = request.form['task']
        try:
            db.session.commit()
            return redirect('/')  
        except:
            return "there was a problem" 
    else:
        return render_template('update.html',task=taask)

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
      Timer(1, open_browser).start();
      app.run(debug=True)
