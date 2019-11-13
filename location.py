import os
import time
import re
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/'
response = urlopen(url)
data = json.load(response)

#Find your own IP
def findYourOwnIP:
    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    print 'Your IP detail\n '
    print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)

def searchIP:
    
    print()
# print the ip location


