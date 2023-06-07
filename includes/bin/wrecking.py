import os 
import sys


from subs import *
from openports import *
from send import *

target_name = sys.argv[1]
path = sys.argv[2]
print(path)
subdomainenumuration(target_name,path)
sort(target_name, path)
subsofsubs(target_name, path)
sorts(target_name, path)
portscan(target_name, path)
live(target_name, path)
sdata(path,target_name)
