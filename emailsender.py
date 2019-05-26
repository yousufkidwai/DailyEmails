import smtplib, ssl
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

