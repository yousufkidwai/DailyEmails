import requests, random, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from headlinegetter import get_choice, get_headlines
from weathergetter import get_description, get_status, get_temperature
from smtplib import SMTPAuthenticationError


def send_email(sender_email, receiver_email, message, password="None"):
    if password is "None":
        print("You must enter the password of the sender email. Try again.")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print("The email was successfully sent.")
    except SMTPAuthenticationError:
        print("The email and password combination you entered was incorrect.")
    except:
        print("The email was not successfully sent. Try again.")


area = input("Please input your zip code. ")
choice = get_choice()
results_str = get_headlines(choice)
capitalChoice = "%s%s" % (choice[0].upper(), choice[1:])
sender_email = "yousufpython@gmail.com"
receiver_email = input("Please enter your email address. ")
password = "Dhiren6969"
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
text = f"""\
Hi,\
These are the {choice} daily headlines:\
{results_str}\
"""
html = f"""\
<html>
  <body>
    <p>Hi,<br>
       <br>
       These are the daily headlines:<br>
       <br>
       {results_str}
       {random.choice(open("quotes.txt").readlines())}
       <br>
       <br>
       Have a wonderful day!
    </p>
  </body>
</html>
"""
message["Subject"] = "Daily {} Headlines".format(capitalChoice)
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()

send_email(sender_email, receiver_email, message, password)