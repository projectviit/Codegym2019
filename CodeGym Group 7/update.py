import database
from flask import redirect,render_template

class Update():

    def update(self,id,new_task, time_1,time_2 ):
        tasks = database.Task.query.all()
        old_task = database.Task.query.get_or_404(id)
        flag = 1
        for task in tasks:
            if time_1 == task.time1 and task.is_deleted=="no":
                flag = 0
        if flag :

            old_task.time1 = time_1
            old_task.time2=  time_2
            old_task.task  = new_task
            database.db.session.commit() 
            return redirect('/')


        return redirect('/') 