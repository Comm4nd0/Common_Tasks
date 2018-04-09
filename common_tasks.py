#!/usr/bin/python3

import os
import time
import sys
import subprocess
import getpass
import pexpect
import shutil

pswd = ''

def print_ascii():
    print("""
           _____                                        _______        _         
          / ____|                                      |__   __|      | |        
         | |     ___  _ __ ___  _ __ ___   ___  _ __      | | __ _ ___| | _____  
         | |    / _ \| '_ ` _ \| '_ ` _ \ / _ \| '_ \     | |/ _` / __| |/ / __| 
         | |___| (_) | | | | | | | | | | | (_) | | | |    | | (_| \__ \   <\__ \ 
          \_____\___/|_| |_| |_|_| |_| |_|\___/|_| |_|    |_|\__,_|___/_|\_\___/ 
    """)

def print_menu(info):
    print_ascii()
    print("""
                                                                         
    [0] - Restart Network-Manager
    [1] - Start PyCharm
    [99]- Exit
    """)
    if info:
        print('Info: {}\n'.format(info))

def ansible_installed():
    global pswd
    yes_ans = ['Y', 'y', '']
    if not shutil.which('ansible'):
        print_ascii()
        print('You must install Ansible for this tool to work!\n')
        print('Would you like to install it now?')
        while True:
            try:
                ans = input('[Y/n] ')
                if ans in yes_ans:
                    os.system('clear')
                    print_ascii()
                    print('Installing Ansible')
                    pswd = getpass.getpass('sudo password:')
                    child = pexpect.spawn('sudo apt install ansible')
                    child.expect(':')
                    child.sendline(pswd)
                    child.expect(']')
                    child.sendline('Y')
                    child.interact()
                    break
                elif ans == 'n':
                    print('\nPlease install Ansible and restart the Common Tasks program!')
                    sys.exit()
                else:
                    print("Not a valid input, please enter (Y)es or (n)o.")
            except KeyboardInterrupt:
                print("""
Oh i see how it is! Goodbye!! 
     .-',',''-.
   .'          '.
  /   O      O   |
 :           `    :
 |                |   
 :    .------.    :
  \  '        '  /
   '.          .'
     '-......-'
""")
                sys.exit()

def restart_nm():
    global pswd
    if not pswd:
        try:
            pswd = getpass.getpass('sudo password:')
        except KeyboardInterrupt:
            print("\n\nIt's ok I didn't want to know you password anyway. Goodbye (⌣_⌣”)")
            sys.exit()
    child = pexpect.spawn('sudo systemctl restart network-manager.service')
    child.expect(':')
    child.sendline(pswd)
    child.interact()

    return 'network-manager restarted'

def pycharm():
    file_path = '{}/software/pycharm-community-2017.3.3/bin/pycharm.sh'.format(os.getcwd())
    subprocess.Popen(['bash', file_path, '&'])

    return 'PyCharm started'

def main(info):
    while True:
        os.system('clear')
        print_menu(info)
        try:
            option = input("Selection: ")
            try:
                option = int(option)
                return option
            except ValueError:
                info = "Not a valid option"
        except KeyboardInterrupt:
            info = "Hit '99' to exit, my friend."

if __name__ == '__main__':
    os.system('clear')
    ansible_installed()
    info = ''
    while True:
       option = main(info)
       if option == 99:
           sys.exit()
       elif option == 0:
           info = restart_nm()
       elif option == 1:
           info = pycharm()