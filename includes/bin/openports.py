from cmdrunner import run_command

def portscan(target_name, savepath):
    command = f'naabu -list {savepath}{target_name}/alls.txt -o {savepath}{target_name}/nabu.txt'
    run_command(command)


def live(target_name, savepath):
    httpx_command = f'httpx -list {savepath}{target_name}/nabu.txt | tee -a {savepath}{target_name}/live.txt'
    cat_commands = [
        f'cat {savepath}{target_name}/nabu.txt >> {savepath}{target_name}/nlive.txt',
        f'cat {savepath}{target_name}/live.txt >> {savepath}{target_name}/nlive.txt'
    ]

    run_command(httpx_command)

    for cat_command in cat_commands:
        run_command(cat_command)
