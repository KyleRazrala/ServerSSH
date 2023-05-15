#!/usr/bin/env python

import os
import sys
import time
import subprocess

os.system('clear')

print('Installing Needed Files... Please wait!\n')

subprocess.call('pip install halo >/dev/null 2>&1', shell=True)

from halo import Halo

with Halo(text='\033[1m\033[33mInstalling Required Files!\033[0m', spinner='dots'):
    subprocess.call('pkg install tur-repo >/dev/null 2>&1 && pkg install x11-repo >/dev/null 2>&1 && pkg install root-repo >/dev/null 2>&1 && pkg install python >/dev/null 2>&1 && pkg install python-pip >/dev/null 2>&1 && pip install Cython pip >/dev/null 2>&1 && pkg install termux-api >/dev/null 2>&1 && pip install tqdm >/dev/null 2>&1 && pip install termux-api >/dev/null 2>&1 && pkg install openssh >/dev/null 2>&1 && pkg install figlet >/dev/null 2>&1 && pkg install toilet >/dev/null 2>&1 && pkg install grep >/dev/null 2>&1 && pkg install termux-am >/dev/null 2>&1 && pkg install termux-tools >/dev/null 2>&1 && pkg install wireless-tools >/dev/null 2>&1 && pkg install unzip >/dev/null 2>&1', shell=True)

print('Packages Successfully Installed!\n')

time.sleep(1)

spinner = Halo(text='\033[1m\033[33mUnpacking Server SSH!\033[0m', spinner='dots')
spinner.start()
time.sleep(5)
spinner.stop()

print('Successfully Unpacked!\n')

alias_name = 'server'
command = 'python /data/data/com.termux/files/usr/Server/ServerSSH'

with Halo(text='\033[1m\033[33mInstalling Server SSH!\033[0m', spinner='dots'):
    subprocess.call('unzip Server.zip >/dev/null 2>&1', shell=True)
    os.system('cd Server && chmod +x ServerSSH && chmod +x install')
    with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
        bashrc.write(f"\nalias {alias_name}='{command}'\n")
    os.system('cd $Home && ssh-keygen -A')
    os.system('cd $Home && cd ServerSSH && mv Server /data/data/com.termux/files/usr && cd $Home && rm -rf ServerSSH')

print('Server SSH Installation Successfully!\n')

spinner = Halo(text='\033[1m\033[33mRunning Setup!\033[0m', spinner='dots')
spinner.start()
time.sleep(5)
spinner.stop()

print('Setup Finish!\n')

time.sleep(1)

print('Close or Exit the Termux App by running command "exit" to be applied successfully and Open or Launch again the Termux App and Execute the Server SSH Script by running the command "server"\n')

print("Enjoy The Script Created By Tech'Yle")

os.system('source ~/.bashrc')
