#!/usr/bin/python
import sys 
from PyQt4.QtGui import QPixmap, QApplication
import os
os.system("clear")
os.system("echo \"***************************************************************** \" ")
os.system("echo \"Machine Details \" ")
os.system("echo \"***************************************************************** \" ")
os.system("uname -a")
os.system("date")
os.system("hostname")
os.system("ifconfig | grep 'inet addr'")
os.system("echo \"***************************************************************** \" ")
os.system("echo \"Result Of The Test \" ")
os.system("echo \"***************************************************************** \" ")
os.system("env x='() { :;}; echo Machine is vulnerable to Shellshock' bash -c \"echo Tested by Silent Ethical Hacker\"")
app = QApplication(sys.argv)
QPixmap.grabWindow(QApplication.desktop().winId()).save('Shellshock_POC.png','png')


os.system("echo \"***************************************************************** \" ")
os.system("echo \"Shellshock Testing Script \" ")
os.system("echo \"Name:     shocking Shell \" ")
os.system("echo \"Author:   Shekhar Suman & Akriti Srivastava \" ")
os.system("echo \"URL:      http://silentethicalhacker.blogspot.com/ \" ")
os.system("echo \"Date:     October 2014\" ")

os.system("echo \"***************************************************************** \" ")
