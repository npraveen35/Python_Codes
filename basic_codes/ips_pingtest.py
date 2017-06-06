#!/usr/bin/python
import subprocess
import os
import platform
'''
servers_ips.txt contains ip address in following format
192.168.1.1
192.168.1.2
'''
with open('servers_ips.txt', 'r') as f:
    '''
    for ip in f:
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
        result = os.system("ping  " + ping_str + " " + ip)
        if result:
            print(ip, "Inactive")
        else:
            print(ip, "Active")
    '''
    for ip in f:
        proc = subprocess.Popen( ['ping', '-c', '3', ip],stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            print 'Active %s' %ip
        else:
            print 'Inactive %s' %ip
