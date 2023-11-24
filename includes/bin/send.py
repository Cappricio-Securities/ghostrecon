import os
import requests


def sdata(path, targ):
    with open(path + targ + '/nlive.txt', 'r') as f:
        with open(path + targ + '/live.txt', 'r') as l:
            with open(path + targ + '/alls.txt', 'r') as a:
                doms = f.read().strip().split('\n')
                live = l.read().strip().split('\n')
                subs = a.read().strip().split('\n')
                pload = {'ports[]': doms, 'subs[]': subs,
                         'live[]': live, 'name': targ, 'status': 'completed'}
                r = requests.post('http://localhost:8090/update', data=pload)


