#!/usr/bin/env python3

from dialog import Dialog
import subprocess
import os

d = Dialog(dialog="dialog")

def clear():
    os.system("clear")

def run(command, output=1):
  proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  if output == 1:
    while proc.poll() is None:
      temp = str(proc.stdout.readline()).split("'")
      temp = temp[1].split("\\")
      print(temp[0])
  commandResult = proc.wait()
  if commandResult == 0:
    return True
  else:
    return False

if d.yesno("Install Updates?") == d.OK:
    clear()
    if run("sudo apt-get update && sudo apt-get full-upgrade -y && sudo apt-get autoremove -y") == False:
        d.msgbox("There was an error updating!")
        exit()

if d.yesno("Install Thunderbird Mail Client?") == d.OK:
    clear()
    if run("sudo apt-get install thunderbird -y") == False:
        d.msgbox("There was an error installing!")
        exit()

if d.yesno("Install Games Package?") == d.OK:
    clear()
    if run("sudo apt-get install gnome-games lightsoff -y") == False:
        d.msgbox("There was an error installing!")
        exit()

if d.yesno("Install Snap Store?") == d.OK:
    clear()
    if run("sudo apt-get install snapd -y") == False:
        d.msgbox("There was an error installing!")
        exit()

if d.yesno("Install Java Development Kit?") == d.OK:
    clear()
    if run("sudo apt-get install default-jdk -y") == False:
        d.msgbox("There was an error installing!")
        exit()        

if d.yesno("Install VS Code?") == d.OK:
    clear()
    if run("sudo apt-get install code -y") == False:
        d.msgbox("There was an error installing!")
        exit()

if d.yesno("Make changes to config.txt?") == d.OK:
    clear()
    if run("sudo gedit /boot/config.txt") == False:
        d.msgbox("There was an error opening the config.txt!")
        exit()

if d.yesno("Configure System using raspi-config?") == d.OK:
    clear()
    if run("sudo raspi-config") == False:
        d.msgbox("There was an error running the raspi-config!")
        exit()

clear()
