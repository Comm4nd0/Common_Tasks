#!/usr/bin/python3

import os
import time
import sys
import subprocess
import getpass
import pexpect

def print_menu():
    print("""
       _____                                        _______        _         
      / ____|                                      |__   __|      | |        
     | |     ___  _ __ ___  _ __ ___   ___  _ __      | | __ _ ___| | _____  
     | |    / _ \| '_ ` _ \| '_ ` _ \ / _ \| '_ \     | |/ _` / __| |/ / __| 
     | |___| (_) | | | | | | | | | | | (_) | | | |    | | (_| \__ \   <\__ \ 
      \_____\___/|_| |_| |_|_| |_| |_|\___/|_| |_|    |_|\__,_|___/_|\_\___/ 
                                                                             
                                                                         
    [0] - Restart Network-Manager
    [1] - Start PyCharm
    [99]- Exit
    """)

def restart_nm():
    pswd = getpass.getpass('sudo password:')
    child = pexpect.spawn('sudo systemctl restart network-manager.service')
    child.expect(':')
    child.sendline(pswd)
    child.interact()

def pycharm():
    file_path = '{}/software/pycharm-community-2017.3.3/bin/pycharm.sh'.format(os.getcwd())
    subprocess.Popen(['bash', file_path, '&'])

def main():
    while True:
        os.system('clear')
        print_menu()
        option = input("Selection: ")

        try:
            option = int(option)
            return option
        except:
            print("Not a valid option")
            time.sleep(2)

if __name__ == '__main__':
    while True:
        option = main()
        if option == 99:
            sys.exit()
        elif option == 0:
            restart_nm()
        elif option == 1:
            pycharm()