import subprocess
import datetime
import time
import sys
import csv
import collections
import json
import os

dirpath = os.getcwd()
'''
Read from the csv/json file to check which ip we need to ban from
Banning the ip fail connects more than 5 times.
'''
def checker():
    BANNING=[]
    with open(dirpath+'/data/ipdb.json') as json_file:
        jsondic = json.load(json_file)
        ipList = jsondic.keys()
        for elem in ipList:
            if jsondic[elem] > 5:
                BANNING.append(elem)
    return BANNING

'''
Execute command from reading and ban the IP
This progam should be reguarly running to keep updated
Main program also print out the banned ip.
'''
def main():
    toBeBan = checker()
    #Clear the empty string
    while("" in toBeBan) : 
        toBeBan.remove("") 

    print("Welcome to system iptable banner")
    for elem in toBeBan:
        cmd1= 'iptables -A INPUT -s '+ elem + ' -j DROP'
        os.system(cmd1)
        text = str(toBeBan.index(elem))+'of'+str(len(toBeBan))
        sys.stdout.write(text+"\r")
        sys.stdout.flush()
    sys.stdout.write("]\n")
    print("Operation ends.")

if __name__ == "__main__":
    main()
