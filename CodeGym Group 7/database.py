from flask_sqlalchemy import SQLAlchemy
import app

db = SQLAlchemy(app.app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(), nullable=False,default="")
    time1 = db.Column( db.String(), nullable = False)
    time2 = db.Column( db.String(), nullable = False)
    status = db.Column( db.String(), nullable=False, default="incomplete")
    is_deleted = db.Column( db.String(), nullable = False, default = "no" )

    def __repr__(self):
        return("Hello")

    def delete(self, id):
        task = self.query.get(id)
        task.is_deleted = "yes"
        db.session.commit()

    def done(self,id):
        taask = self.query.get_or_404(id)   
        taask.status = "completed"
        db.session.commit()

    def removeall(self):
        tasks = self.query.all()
        try:
            for task in tasks:
                db.session.delete(task)
            db.session.commit()
        except:
            return "there was a problem"