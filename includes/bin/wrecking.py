import os ,yaml
import sys


from subs import *
from openports import *
from send import *
from bot import *


file_path = 'config.yaml'

with open(file_path, 'r') as file:
    data = yaml.safe_load(file)


Config = data.get('config', {})
github_token = Config.get('github_token', '')
ChatId = Config.get('chat_ID', '')
subs_conf = Config.get('Subs_Scan_Fast', '')
subsof = Config.get('Subs_of_Subs', '')

target_name = sys.argv[1]
path = sys.argv[2]


Started(target_name, ChatId)

subdomainenumuration(target_name, path, subs_conf)
sort(target_name, path)
if subsof == False:
    subsofsubs(target_name, path)
sorts(target_name, path)
portscan(target_name, path)
live(target_name, path)
sdata(path,target_name)
Done(target_name, ChatId)
