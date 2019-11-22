from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
#from flaskwebgui import FlaskUI
import threading 
import time
from win10toast import ToastNotifier
#import webbrowser
from threading import Timer

app = Flask(__name__)
#ui=FlaskUI(app)
import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///read.db'
db = SQLAlchemy(app)
toast = ToastNotifier()

class Task(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(), nullable=False,default="")
    time1 = db.Column( db.String(), nullable = False)
    time2 = db.Column( db.String(), nullable = False)
    status = db.Column( db.String(), nullable=False, default="incomplete")

    def __repr__(self):
        return("Hello")

@app.route('/',methods = ['POST','GET'])
def index():
    flag = 0
    if request.method == 'POST':
        new_task1 = request.form.get('task')
        time1 = request.form.get('time1')
        time2 = request.form.get('time2')
        tasks = Task.query.order_by(Task.time1).all()
        if tasks==[] and new_task1!="" and time1!="" and time2!="":
            
            try:
                t =Task(task=new_task1, time1 = time1,time2= time2 )              
                db.session.add(t)
                db.session.commit()
                #toast.show_toast(title=f"{t.task}", msg=f"{t.task}",threaded=True)
            except:
                return "There was a problem"
            return redirect('/')

        elif tasks != [] and new_task1!="" and time1!="" and time2!="":
            flag2=0
            for task in tasks:
                if time1==task.time1 and time2==task.time2:
                    flag2=1
            if flag2==0:
                    try:
                        t =Task(task=new_task1, time1 = time1,time2= time2 )              
                        db.session.add(t)
                        db.session.commit()
                        #toast.show_toast(title=f"{t.task}", msg=f"{t.task}",threaded=True)
                    except:
                        return "There was a problem"
                    return redirect('/')


    tasks = Task.query.order_by(Task.time1).all()
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
    tasks = Task.query.order_by(Task.time1).all()
    if request.method == 'POST':
        t= request.form.get('task')
        time_1 = request.form.get('time1')
        time_2 = request.form.get('time2')
        flag = 1
        for task in tasks:
            if time_1 == task.time1 :
                flag = 0
        if flag :
            try:
                taask.time1 = time_1
                taask.time2=  time_2
                taask.task  = t
                db.session.commit()
                return redirect('/')  
            except:
                return "there was a problem"
        else:
            return redirect('/') 

    else:
        return render_template('update.html',task=taask)
@app.route('/done/<int:id>')
def done(id):
    taask = Task.query.get_or_404(id)   
    taask.status = "completed"
    db.session.commit()
    return redirect('/')
@app.route('/getreport')
def getreport():
    tasks = Task.query.order_by(Task.time1).all()
    return render_template('getrep.html',tasks=tasks)


def notification_scheduler():
    toast = ToastNotifier()
    import datetime
    while True:
        tasks = Task.query.order_by(Task.time1).all()
        for task in tasks: 
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if task.time1 in current_time:
                toast.show_toast(title=f"{task.task}", msg=f"{task.task}",threaded=True)
                time.sleep(30)
                print(current_time)
            time.sleep(1)


if __name__ == "__main__":
    x = threading.Thread(target=notification_scheduler , args=(),daemon=True)
    x.start()
    app.run(debug=True,)