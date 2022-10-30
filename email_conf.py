import socket
import smtplib
import datetime
import time
from email.message import EmailMessage


host = "127.0.0.1"
port = 1237

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    while True:
        s.listen() #listening for request to connect
        conn, addr = s.accept()
        data = conn.recv(1024)
        data = data.decode()

        if data == 'finished': #need to send server kill message otherwise socket will lock up and computer will have to be restarted to fix
            mail_server.quit()
            s.close()
            exit()

        else:
            print(data)
            from_email = 'storetest99a@gmail.com'
            app_pass = "ahddhdaojjvmdaxn"

            mail_server = smtplib.SMTP('smtp.gmail.com', 587)
            mail_server.starttls()
            mail_server.login(from_email, app_pass)

            todays_date = datetime.date.today()
            now = time.localtime()
            now = time.strftime("%H:%M:%S")

            message = (f"""From: Store Test Program                        
            This is your email confirmation of your order from: 'Store name here'.
            Thank you for shopping with us today!
            time of order: {now}
            date of order: {todays_date}
            """)

            subj = 'Order Confirmation'
            email_msg = EmailMessage()
            email_msg.set_content(message)
            email_msg['subject'] = subj
            email_msg['to'] = data
            email_msg['from'] = from_email

            mail_server.send_message(email_msg)
            
            conn.send(b'True')

            
