import smtplib, ssl


def send_email(message):
     host = 'smtp.gmail.com'
     port = 465
     username = 'shophop247@gmail.com'
     password = 'idoksrxjgcpifzbz'
     receiver = 'shophop247@gmail.com'
     context = ssl.create_default_context()

     with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
          server.login(username, password)
          server.sendmail(username, receiver, message)
