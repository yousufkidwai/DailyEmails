import requests, random, smtplib, ssl, pytemperature, tkinter
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from headlinegetter import get_choice, get_headlines
from weathergetter import get_description, get_status
from emailsender import send_email
from tkinter import*

zipcode = input("Please input your zipcode. \n> ")
countrycode = "US"
apikey = '3dad82ec0200d5e30cbdab1788cca74c'
link = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"
page = requests.get(link)
x = page.json()
weather = x['main']
if x['cod'] != "404":
    kelvin_temp = weather['temp']
    temperature = round(pytemperature.k2f(kelvin_temp))
else:
    print("An error occurred.")
area = zipcode
choice = get_choice()
results_str = get_headlines(choice)
capitalChoice = "%s%s" % (choice[0].upper(), choice[1:])
sender_email = "teenhacks.dailynews@gmail.com"
receiver_email = input("Please enter your email address. ")
password = "teenhacks.li"
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
text = f"""\
Hi,\
These are the {choice} daily headlines:\
{results_str}\
{random.choice(open("quotes.txt").readlines())}\
Today's weather is expected to be {get_status(zipcode)}. The expected temperature for today is {temperature}
degrees fahrenheit. Have a wonderful day!
"""
html = f"""\
<html>
  <body>
    <p>Hi,<br>
       <br>
       These are the {choice} daily headlines:<br>
       <br>
       {results_str}
       {random.choice(open("quotes.txt").readlines())}
       <br>
       <br>
       Today's weather is expected to be {get_description(zipcode)}. The expected temperature for today is {temperature}
       degrees fahrenheit. Have a wonderful day!
    </p>
  </body>
</html>
"""
message["Subject"] = "Daily Weather and {} Headlines".format(capitalChoice)
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()

send_email(sender_email, receiver_email, message, password)
