import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['akabwama@nssfug.org']

mail_account = 'nssfleavereminder@nssfug.org'
mail_password = '@LmRa*hgoYUc'

msg = MIMEMultipart()    
sender = 'nssfleavereminder@nssfug.org'
subject = "LEAVE REMINDER"
body = "This is my email body"

try:
    msg['From'] = 'nssfleavereminder@nssfug.org'
    msg['To'] = ','.join(address_book)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text=msg.as_string()
    #print text
    # Send the message via our SMTP server
    
    server = smtplib.SMTP('192.168.192.151:25')
    server.ehlo()
    server.starttls()
    server.login(mail_account, mail_password)
    server.sendmail(sender,address_book, text)
    server.quit()
    print('Message Sent')    

except Exception as e:
        print(e)    


'''
mail_account = 'nssfleavereminder@nssfug.org'
mail_password = '@LmRa*hgoYUc'
receiver_list = [employee_email, supervisor_email]

print(supervisor_email)
print(employee_email)
   
message = 'Hello ' + employee + ', your leave will start in two days time on, ' + datestring + ' .'
print(message)


#server = smtplib.SMTP('smtp.gmail.com:587')
server = smtplib.SMTP('192.168.192.151:25')
server.ehlo()
server.starttls()
server.login(mail_account, mail_password)
server.sendmail(mail_account, 'akabwama@nssfug.org', message)
server.quit()
'''      