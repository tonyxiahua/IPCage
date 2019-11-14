# IPCage
Secure your port 22 and protect yourself from global attackers.

## Description

- The program will collect potential attacker information for your linux server. 
- Also you do not need to change the ssh connection port.
- (TO DO) Do a reverse attact to those controlled machine gaining the sudo premission

## Known Feature

- The ```autoban.py``` is able to detect and release the attacker IP
- Collected data inside output folder
- Collected machine useage data inside the log folder
- The ```iptables.py``` is able to execute iptables command and banning the attacker.
- Progress bar shows how much item we still need for iptables commands

## Useage 

Require Python to run the code 
``
python init.py`
python autoban.py
python iptables.py
```
It takes time if there are many attackers.

## TO DO
<del>Writing code for the iptables.py</del>
The iptables.py needs following functions
- <del>Read file from json/CSV from previous collected system data.</del>
- <del>Detect which IP fails connection 5 times, and put it into the banning list of iptable</del>
- <del>Promot to the system and process the banning instruction.</del>
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
git config --global user.name "???"
git config --global user.email "???@gmail.com"
```
