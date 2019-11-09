# IPCage
Siecure your port 22 and protect yourself from attackers

## Description

- The program will collect potential attacker for your linux server. 
- Also you do not need to change the ssh connection port.
- Do a reverse attact to those controlled machine gaining the sudo premssion

## Known Feature

- The autoban.py is able to detect and release the attacker IP
- Collected data inside output 

## Useage 

Require min => Python 3.6 to run the code 
```
python3 autoban.py
```
It takes time if there are many attackers.

## TO DO
writing code for the iptables.py
The iptables.py needs following functions
- Read file from json/CSV from previous collected system data. 
- Detect which IP fails connection 10 times, and put it into the banning list of iptable
- Promot to the system and process the banning instruction.
- Print a new table or txt file for banned ip. with date and history banning list.
- Considering put a banning relase function to the system. 

## How to make it auto commit?
There is the hidden folder .git in every repositories 
modify ```config``` file 
add the following to the bottom line
```
[credential]
    helper = store
```  

## why my Github commitment is root user?
Becasue you didn't change to this:
```
git config --global user.name "tonyxiahua"
git config --global user.email "@gmail.com"
```
