import smtplib, ssl
import os


#def send_email(message):
     host = 'smtp.gmail.com'
     port = 465
     username = 'shadowysupercoderssc@gmail.com'
     password = os.environ.get('SSCPW')
     receiver = 'shadowysupercoderssc@gmail.com'
     context = ssl.create_default_context()

     with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
          server.login(username, password)
          server.sendmail(username, receiver, message)

