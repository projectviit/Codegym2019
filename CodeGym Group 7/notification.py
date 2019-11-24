import datetime
import database
import time
from win10toast import ToastNotifier

#generation of desktop notification using the win10toast library
class scheduler():
    def notification_scheduler(self):
        toast = ToastNotifier()
        while True:
            tasks = database.Task.query.order_by(database.Task.time1).all()
            for task in tasks: 
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                if task.time1 in current_time and task.is_deleted =="no":
                    try:
                        toast.show_toast(title=f"{task.task}", msg=f"{task.task}",threaded=True) #the pop-up message that'll be seen
                        time.sleep(30)
                    except:
                        pass
                    print(current_time)
            time.sleep(1)