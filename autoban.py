'''
Small Little Cage
Author : Xia Hua 
2019 Sep 12
https://www.freebuf.com/sectool/170779.html
'''
import subprocess
import datetime
import csv
import collections
import json
import os

dirpath = os.getcwd()
'''
Dictionary Class
Easy Add method for dictionary 
'''

'''
class dicTemplate(dict): 
    # __init__ function 
    def __init__(self): 
        self = dict() 
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value     
'''
'''
Text Handling ,dealing with text data
methods:
nameProcess()              return name dic function 
printNamebyAlphabet()      to dissplay and print the name
ipProcess()                return ip dic function
printIPbyAlphabet() to display and print the ips
1. copy the btmp file 
2. decode the btmp file and save to txt 
3. save ....
''' 

class text2Dic:
    def __init__(self):
        self.name = dict() 
        self.ip = dict() 
        self.orderedName = dict() 
        self.orderedIP = dict() 
        ''''''''''''''''''''''''''''''        
        cmd1 = 'lastb -a > btmp.txt'
        os.system(cmd1)
        cmd2 = 'cp /var/log/btmp '+dirpath+'/log/btmp'+str(datetime.datetime.now().date())+str(datetime.datetime.now().time())
        os.system(cmd2)
        cmd3 = '> /var/log/btmp'
        os.system(cmd3)
        ''''''''''''''''''''''''''''''
        if os.path.exists('data/namedb.json'):
            with open('data/namedb.json', 'r') as fp:
                self.name = json.load(fp)
        if os.path.exists('data/ipdb.json'):
            with open('data/ipdb.json', 'r') as fp:
                self.ip = json.load(fp)
        ''''''''''''''''''''''''''''''''''''''''''    
        with open("btmp.txt") as f:
            '''
            In the case you are working with Big Data using readlines() 
            is not very efficient as it can result in MemoryError. 
            '''
            for lines in f:
                if (lines == '\n'):
                    break
                if (lines[:7].rstrip() in self.name.keys()):
                    self.name[lines[:7].rstrip()] += 1
                else:
                    #self.name.add((lines[:7]).rstrip(),1)
                    self.name[(lines[:7]).rstrip()] = 1
                if (lines[60:].rstrip('\n') in self.ip.keys()):
                    self.ip[lines[60:].rstrip('\n')] += 1
                else:
                    self.ip[((lines[60:]).rstrip('\n'))] = 1
        ''''''''''''''''''''''''''''''''''''''''''            
        with open('data/ipdb.json', 'w') as fp:
            json.dump(self.ip, fp)    
        with open('data/namedb.json', 'w') as fp:
            json.dump(self.name, fp)        
    
    def nameProcess(self):
        return self.name
    def ipProcess(self):
        return self.ip
    '''
    Print the Name function 
    '''
    def printNamebyAlphabet(self):
        for key in sorted(self.name.keys()):
            print("%s: %s" % (key, self.name[key]))
    def printIPbyAlphabet(self):
        for key in sorted(self.ip.keys()):
            print("%s: %s" % (key, self.ip[key]))
    '''
    Group Process Rverse order of the Name & IP
    '''
    def sortNamebyValue(self):
        self.orderedName = collections.OrderedDict(sorted(self.name.items(), key=lambda kv: kv[1],reverse=True))
    def sortIPbyValue(self):
        self.orderedIP = collections.OrderedDict(sorted(self.ip.items(), key=lambda kv: kv[1],reverse=True))
    '''
    Export function to process the CSV
    '''
    def saveNametoCSV(self):
        self.sortNamebyValue()
        try:
            with open('output/NameOutput.csv', 'w') as f:
                for key in self.orderedName.keys():
                    f.write("%s,%s\n"%(key,self.orderedName[key]))
        except IOError:
            print("I/O error")  
    def saveIPtoCSV(self):
        self.sortIPbyValue()
        try:
            with open('output/IPoutput.csv', 'w') as f:
                for key in self.orderedIP.keys():
                    f.write("%s,%s\n"%(key,self.orderedIP[key]))
        except IOError:
            print("I/O error")
    '''==========================================
    JSON file for dealing with sytem process save
    =========================================='''
    def saveNametoJSON(self):
        try:
            with open('data/namedb.json', 'w') as fp:
                json.dump(self.name, fp) 
        except IOError:
            print("I/O error. FIle still using" )
    def saveIPtoJSON(self):
        try:
            with open('data/ipdb.json', 'w') as fp:
                json.dump(self.ip, fp)
        except IOError:
            print("I/O error. FIle still using" )            
    '''============================================
    JSON file load for deadling with system restore
    ============================================'''
    def loadNametoDic(self):
        try:
            with open('data/namedb.json', 'r') as fp:
                self.name = json.load(fp)
        except IOError:
            print("I/O error. FIle still using" )        
    def loadIPtoDic(self):
        try:
            with open('data/ipdb.json', 'r') as fp:
                self.ip = json.load(fp)
        except IOError:
            print("I/O error. FIle still using" )
            
            

'''
main function
'''
def main():
    #startime = datetime.datetime.now()
    """
    create new jobs object to text2Dic
    """
    jobs = text2Dic()
    #Output
    jobs.saveIPtoCSV()
    jobs.saveNametoCSV()

    print("AutoCollection has been done.")
    print("the lastb history has been cleared")
    print("the output file is inside the output folder")
    print("So long")
    #time
    #endtime = datetime.datetime.now()
    #print("Total time used: ",endtime - startime)
    #Github PUSH
    #subprocess.call(["git", "add", "."])
    #subprocess.call(["git", "commit", "-m", "auto import btmp snapshot " + str(datetime.datetime.now())])
    #subprocess.call(["git", "push"])      
    
if __name__ == "__main__":
    main()

'''
Example TEXT
upload   ssh:notty    Thu Sep 12 21:58 - 21:58  (00:00)     113.134.211.228
upload   ssh:notty    Thu Sep 12 21:58 - 21:58  (00:00)     113.134.211.228
oracle   ssh:notty    Thu Sep 12 21:56 - 21:56  (00:00)     h213-21-67-184.cust.a3fiber.se
oracle   ssh:notty    Thu Sep 12 21:56 - 21:56  (00:00)     h213-21-67-184.cust.a3fiber.se
'''
