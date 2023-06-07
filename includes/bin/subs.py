

import os

def subdomainenumuration(target_name, savepath):
    os.system('sh includes/bin/github-subs.sh ' + savepath+target_name +'/scope.txt >> ' + savepath+target_name + '/github.txt')
    os.system('subfinder -dL ' + savepath+target_name +'/scope.txt -o ' + savepath+target_name + '/subfinder.txt ')
    os.system('sh includes/bin/crt.sh ' + savepath+target_name + '/scope.txt >> ' + savepath+target_name +'/crtsh.txt')
    os.system('amass enum -passive -df ' + savepath+target_name +'/scope.txt -o ' + savepath+target_name + '/amass.txt')
    os.system('subsleuth -l ' + savepath+target_name +'/scope.txt -w includes/bin/wordlist.txt -o ' + savepath+target_name + '/subsleuth.txt')

def sort(target_name, savepath):
    os.system('cat ' + savepath+target_name +'/*.txt | sort -u | tee -a ' + savepath+target_name + '/all.txt')
    os.system('cat ' + savepath+target_name + '/all.txt | rev | cut -d "."  -f 1,2,3 | sort -u | rev >> ' +savepath+target_name + '/subs3rdlvl.txt')
    

def subsofsubs(target_name, savepath):
    os.system('sh includes/bin/crt.sh ' + savepath+target_name +'/subs3rdlvl.txt >> ' + savepath+target_name + '/crtsh-subs.txt')
    os.system('amass enum -passive -df ' + savepath+target_name +'/subs3rdlvl.txt -o ' + savepath+target_name + '/amass-subs.txt')

def sorts(target_name, savepath):
    os.system('cat ' + savepath+target_name +'/*.txt | sort -u | tee -a ' + savepath+target_name + '/alls.txt')
    
