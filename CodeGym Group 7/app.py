from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from flaskwebgui import FlaskUI
import threading 
import index
import report
import notification
import update
import database

app = Flask(__name__)
#creating the database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///read.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#the first page that you'll land to once you run the server
#it contains the provisions for adding a task, deleting a task, updating a task and you can see the list of your tasks
#on the same page

@app.route('/',methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        new_task = request.form.get('task')
        time1 = request.form.get('time1')
        time2 = request.form.get('time2')
        index.Index().home( new_task = new_task,time1= time1, time2 = time2)
    tasks = database.Task.query.order_by(database.Task.time1).all()
    return render_template('index.html', tasks = tasks)


#the delete module which deletes a particular task from your list of tasks
@app.route('/delete/<int:id>')
def delete(id):
    database.Task().delete(id = id)
    return redirect('/')

#the update module which lets you update your existing task with a new task
@app.route('/update/<int:id>', methods = ['POST','GET'])
def change(id):    
    task = database.Task.query.get_or_404(id)
    if request.method == 'POST':
        t= request.form.get('task')
        time_1 = request.form.get('time1')
        time_2 = request.form.get('time2')
        return update.Update().update(id,t, time_1,time_2)
    else:
        return render_template('update.html',task=task)

#the done module which marks the task as completed   
@app.route('/done/<int:id>')
def done(id):
    database.Task().done(id)
    return redirect('/')

#module for report generation of your task list.
#this would ask the user to enter their email credentials, and their report will be mailed to that email address.
@app.route('/getreport', methods=['GET','POST'])
def getreport():
    tasks = database.Task.query.all()
    if request.method == 'POST':
        reciever = request.form.get('email')
        report.Report().send(reciever)
    return render_template('getrep.html', tasks = tasks)

#module to delete all tasks in the list
@app.route('/removeall')
def removeall():
    database.Task().removeall()
    return redirect('/')


if __name__ == "__main__":
    x = threading.Thread(target=notification.scheduler().notification_scheduler , args=(),daemon=True)
    x.start()
    app.run(debug=True,)