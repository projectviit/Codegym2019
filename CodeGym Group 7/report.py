import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template
import database

#here we send the report as it is seen on the app to the user via mail using SMTP server
class Report():
    sender= "email"
    sender_password= r"password"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Daily Task Summary" 
    msg['From'] = sender
    s = smtplib.SMTP_SSL('smtp.gmail.com') #we use the gmail SMTP API here to initiate SSL connection
    flag = 0
    def _login_(self):
        self.s.login("email", r"password")

    def send(self,reciever):
        self._login_()
        try:
            tasks = database.Task.query.order_by(database.Task.time1).all()
            html = render_template('getrep.html',tasks=tasks)
            part2 = MIMEText(html, 'html')
            
            self.msg['To'] = reciever
            self.msg.attach(part2)
            self.s.sendmail(self.sender, reciever, self.msg.as_string())
            self.s.quit()
            return render_template('getrep.html',tasks=tasks)
        except:
            return "There was a problem with the credentials or the network"

        return render_template('getrep.html',tasks=tasks)