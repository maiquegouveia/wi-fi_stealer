import subprocess
import os
import sys

#Creating a file to store passwords
password_file = open('passwords.txt', 'w')
password_file.write("Saved Wi-Fis:\n\n")
password_file.close()

#Lists
wifi_files = []
wifi_names = []
wifi_passwords = []

#Executing a Windows Command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#Grabing current directory
path = os.getcwd()

#Getting the wi-fi files with the ssid and password
for filename in os.listdir(path):
    if filename.startswith('Wi-Fi') and filename.endswith('.xml'):
        wifi_files.append(filename)

#Getting the wi-fi ssid and password
for i in wifi_files:
    with open(i, 'r') as f:
        lines = f.readlines()
        name = []

        for line in lines:
            if 'name' in line:
                line = line.strip()
                line = line[6:]
                line = line[:-7]
                if line not in name:
                    name.append(line)

            if 'keyMaterial' in line:
                line = line.strip()
                line = line[13:]
                line = line[:-14]
                wifi_passwords.append(line)
                wifi_names.append(name[0])

#Writing wi-fi ssid and password to file
for x,y in zip(wifi_names, wifi_passwords):
    sys.stdout = open('passwords.txt', 'a')
    print("SSID: " + x + " / PASSWORD: " + y,sep='\n')
    sys.stdout.close()
