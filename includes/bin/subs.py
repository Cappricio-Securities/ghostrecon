
from cmdrunner import run_command


def subdomain_enumuration(target_name, savepath, subs_conf, token):
    github_command = f'sh includes/bin/github-subs.sh {savepath}{target_name}/scope.txt >> {savepath}{target_name}/github.txt {token}'
    subfinder_command = f'subfinder -dL {savepath}{target_name}/scope.txt -o {savepath}{target_name}/subfinder.txt'
    crtsh_command = f'sh includes/bin/crt.sh {savepath}{target_name}/scope.txt >> {savepath}{target_name}/crtsh.txt'

    run_command(github_command)
    run_command(subfinder_command)
    run_command(crtsh_command)

    if not subs_conf:
        amass_command = f'amass enum -passive -df {savepath}{target_name}/scope.txt -o {savepath}{target_name}/amass.txt'
        subsleuth_command = f'subsleuth -l {savepath}{target_name}/scope.txt -w includes/bin/wordlist.txt -o {savepath}{target_name}/subsleuth.txt'

        run_command(amass_command)
        run_command(subsleuth_command)


def sort(target_name, savepath):
    sort_command = f'cat {savepath}{target_name}/*.txt | sort -u | tee -a {savepath}{target_name}/all.txt'
    subs3rdlvl_command = f'cat {savepath}{target_name}/all.txt | rev | cut -d "." -f 1,2,3 | sort -u | rev >> {savepath}{target_name}/subs3rdlvl.txt'

    run_command(sort_command)
    run_command(subs3rdlvl_command)


def subsofsubs(target_name, savepath):
    crtsh_subs_command = f'sh includes/bin/crt.sh {savepath}{target_name}/subs3rdlvl.txt >> {savepath}{target_name}/crtsh-subs.txt'
    amass_subs_command = f'amass enum -passive -df {savepath}{target_name}/subs3rdlvl.txt -o {savepath}{target_name}/amass-subs.txt'

    run_command(crtsh_subs_command)
    run_command(amass_subs_command)


def sorts(target_name, savepath):
    sorts_command = f'cat {savepath}{target_name}/*.txt | sort -u | tee -a {savepath}{target_name}/alls.txt'
    run_command(sorts_command)
