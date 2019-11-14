import os
dirpath = os.getcwd()
cmd4 = 'mkdir data log output'
cmd5 = 'touch '+dirpath+'/data/ipdb.json'
cmd6 = 'echo "{}"> '+dirpath+'/data/ipdb.json'
os.system(cmd4)
os.system(cmd5)
os.system(cmd6)
