import os


def portscan(target_name, savepath):
    print("naabu")
    os.system('naabu -list '+ savepath+target_name +'/alls.txt -o '+ savepath+target_name +'/nabu.txt')


def live(target_name, savepath):
    os.system('httpx -list ' + savepath+target_name +'/nabu.txt | tee -a ' + savepath+target_name + '/live.txt')
    os.system('cat ' + savepath+target_name +'/nabu.txt >> ' + savepath+target_name + '/nlive.txt')
    os.system('cat ' + savepath+target_name + '/live.txt >> ' + savepath+target_name + '/nlive.txt')

