import os
import sys

target_name = sys.argv[1]
savepath = sys.argv[2]


os.system('mkdir '+savepath+' &>/dev/null') # creating folder for data
os.system('mkdir '+savepath+target_name) #creating foler with company name
