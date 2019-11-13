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
def checker():
    with open('/data/ipdb.json') as json_file:
        jsondic = json.load(json_file)
        
        if IP-ADDRESS[1] > 5:
            BANNING-IP-ADDRESS = IPADDRESS[0]
        return BANNING-IP-ADDRESS

'''
Execute command from reading and ban the IP
This progam should be reguarly running to keep updated
'''
def command(IPADDRESS):
    cmd1= 'iptables -A INPUT -s '+ IP-ADDRESS + ' -j DROP'
    cmd3= ' '
    cmd4= ' '
    os.system(cmd1)
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
