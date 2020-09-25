import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import os



def sendEmail():

    os.system("sudo fswebcam -r 300x200 image.jpeg")
    
    email = 'stayawaythieves@gmail.com'
    password = 'hahayoutried'
    send_to_email = 'stayawaythieves@gmail.com'
    subject = 'THIEF DETECTED'
    message = 'Potential Thief has tried to open your box!'
    file_location ='/home/pi/Downloads/image.jpeg' #remember to save python file in this directory as the photo will also be saved here

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Setup the attachment
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()





#!/usr/bin/env python
import RPi.GPIO as GPIO

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def alert(ev = None):
    print ("Tilt Detected")#for debugging purposes
    sendEmail()

def loop():
    GPIO.add_event_detect(channel, GPIO.FALLING, callback = alert, bouncetime = 100)
    while True:
        pass

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
'''


