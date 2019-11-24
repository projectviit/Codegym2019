from flask import Flask, render_template,redirect
import database

class Index():
    
    tasks = database.Task.query.order_by(database.Task.time1).all()

    def home(self,new_task, time1,time2):
        tasks = self.tasks
        if tasks==[] and new_task!="" and time1!="" and time2!="":
            
            try:
                t = database.Task(task=new_task, time1 = time1,time2= time2 )              
                database.db.session.add(t)
                database.db.session.commit()
            except:
                return "There was a problem"
            return redirect('/')
        
        elif tasks!= [] and new_task!="" and time1!="" and time2!="":
            flag=0
            for task in self.tasks:
                if time1==task.time1 and time2==task.time2 and task.is_deleted=="no":
                    flag=1
            if flag==0:
                    try:
                        t = database.Task(task=new_task, time1 = time1,time2= time2 )              
                        database.db.session.add(t)
                        database.db.session.commit()
                    except:
                        return "There was a problem"
                    return redirect('/')