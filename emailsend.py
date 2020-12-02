import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


maggie_email = 'morono@nssfug.org'
alvin_mail = 'akabwama@nssfug.org'
mail_account = 'nssfleavereminder@nssfug.org'
mail_password = 'ops@DQU*'


def twodayreminderemail(employee, supervisor, employee_email, supervisor_email, datestring):
    try:
        

        #SENDING TO THE EMPLOYEE
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        subject = "LEAVE REMINDER"
        body = 'Hello ' + employee + ', your leave will start in two days time on, ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = employee_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,employee_email, text)
        server.quit()
        
        #SENDING TO THE SUPERVISOR 
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        
        subject = "LEAVE REMINDER"
        body = 'Hello ' + supervisor + ', ' + employee + ' will take leave in two days starting on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = supervisor_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,supervisor_email, text)
        server.quit()
        
        
        #SENDING TO THE MAGGIE 
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        subject = "LEAVE REMINDER"
        body = 'Hello Maggie, ' + employee + ' will take leave in two days starting on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = maggie_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,maggie_email, text)
        server.quit()
        
        
        #SENDING TO THE ALVIN 
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        subject = "LEAVE REMINDER"
        body = 'Hello Alvin, ' + employee + ' will take leave in two days starting on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = alvin_mail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,alvin_mail, text)
        server.quit()      
        
        print('NSSF Successful')
        
        
    except Exception as e:
        print(e)
        print('Failed')
        
def sevendayreminderemail(employee, supervisor, employee_email, supervisor_email, datestring):
    try:
        
        #SENDING TO THE EMPLOYEE
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        
        subject = "LEAVE REMINDER"
        body = 'Hello ' + employee + ', your leave will start in seven days time on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = employee_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,employee_email, text)
        server.quit()
        
        #SENDING TO THE SUPERVISOR 
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        
        subject = "LEAVE REMINDER"
        body = 'Hello ' + supervisor + ', ' + employee + ' will take leave in seven days starting on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = supervisor_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,supervisor_email, text)
        server.quit()
        
        #SENDING TO THE MAGGIE 
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        
        subject = "LEAVE REMINDER"
        body = 'Hello Maggie, ' + employee + ' will take leave in seven days starting on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = maggie_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,maggie_email, text)
        server.quit()
        
        
        
        #SENDING TO THE ALVIN 
        server = smtplib.SMTP('192.168.192.151:25')
        server.ehlo()
        server.starttls()
        server.login(mail_account, mail_password)
        
        subject = "LEAVE REMINDER"
        body = 'Hello Alvin, ' + employee + ' will take leave in seven days starting on ' + datestring + ' .'
        
        msg = MIMEMultipart()
        msg['From'] = mail_account
        msg['To'] = alvin_mail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        server.sendmail(mail_account,alvin_mail, text)
        server.quit()
        
        print('NSSF Successful')
        
        
    except Exception as e:
        print(e)
        print('Failed')
        
        

