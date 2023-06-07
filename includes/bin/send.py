import os 
import requests


def sdata(path,targ):
    f = open(path+targ+'/nlive.txt', 'r')
    l = open(path+targ+'/live.txt', 'r')
    a = open(path+targ+'/alls.txt', 'r')
   
    doms = f.read().decode('utf8').strip().split('\n')
    live = l.read().decode('utf8').strip().split('\n')
    subs = a.read().decode('utf8').strip().split('\n')
    pload = {'ports[]': doms, 'subs[]':subs,'live[]':live,'name':targ,'status':'completed'}
    r = requests.post('http://localhost:8090/update',data=pload)
