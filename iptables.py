import subprocess
import datetime
import csv
import collections
import json
import os

'''
Read from the csv/json file to check which ip we need to ban from
Banning the ip fail connects more than 5 times.
'''
def checker:

    if IP-ADDRESS[1] > 5:
        BANNING-IP-ADDRESS = IPADDRESS[0]
    return BANNING-IP-ADDRESS

'''
Execute command from reading and ban the IP
This progam should be reguarly running to keep updated
'''
def command(IPADDRESS):
    cmd1= 'iptables -A INPUT -s '+ IP-ADDRESS + ' -j DROP'
    cmd2= ' '
    cmd3= ' '
    cmd4= ' '
    os.system()
    os.system()
    os.system()
    os.system()
'''
Main program also print out the banned ip.
'''
def main:
    checker()
    command()

if __name__ == "__main__":
    main()
