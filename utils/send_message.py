import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

from_email = "qaxramonovashahzoda001@gmail.com"


def send_email(to_email):
    email_message = MIMEMultipart()
    email_message['From'] = from_email
    email_message['To'] = to_email
    email_message['Subject'] = "Salom"
    email_message.attach(MIMEText("Nima gap", 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    server.login(from_email, 'cqrr dnaj wlaa vvyd')
    try:
        server.sendmail(from_email, to_email, email_message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


users = [
    "sanjarbeksocial@gmail.com",
    "shukrullonosirov@gmail.com",
    "uzalisherov@gmail.com",
    "maftuna200412@gmail.com",
    "boxodirazimov683@gmail.com",
    "shohpad@gmail.com",
    "muhammadrahimiminjonov@gmail.com"
]


def send_email_to_users():
    for user in users:
        send_email(user)


t1 = threading.Thread(target=send_email_to_users)
t1.start()

user_name = input("Enter your name: ")
print(user_name)