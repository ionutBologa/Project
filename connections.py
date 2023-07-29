import os
import smtplib,ssl
from flask import Flask, request
import mysql.connector
from email.message import EmailMessage

connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="p0r0dica",
        database="project",
        auth_plugin='mysql_native_password'
    )
cursor=connect.cursor()
app= Flask(__name__)

def send_email(to, subject, message):

    email_address = "bologa.ionut13@gmail.com"
    email_password = "ozotlvccastoqrhb"

    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    msg.set_content(message)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)



