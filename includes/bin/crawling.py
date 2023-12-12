import subprocess
from cmdrunner import run_command


input_file = 'crawl.txt'

# Define patterns and output file names
patterns = [
    ('aws-keys', 'aws-keys.txt'),
    ('base64', 'base64.txt'),
    ('cors', 'cors.txt'),
    ('debug-pages', 'debug-pages.txt'),
    ('debug_logic', 'debug_logic.txt'),
    ('firebase', 'firebase.txt'),
    ('fw', 'fw.txt'),
    ('go-functions', 'go-functions.txt'),
    ('http-auth', 'http-auth.txt'),
    ('idor', 'idor.txt'),
    ('img-traversal', 'img-traversal.txt'),
    ('interestingEXT', 'interestingEXT.txt'),
    ('interestingparams', 'interestingparams.txt'),
    ('interestingsubs', 'interestingsubs.txt'),
    ('ip', 'ip.txt'),
    ('json-sec', 'json-sec.txt'),
    ('jsvar', 'jsvar.txt'),
    ('lfi', 'lfi.txt'),
    ('meg-headers', 'meg-headers.txt'),
    ('php-curl', 'php-curl.txt'),
    ('php-errors', 'php-errors.txt'),
    ('php-serialized', 'php-serialized.txt'),
    ('php-sinks', 'php-sinks.txt'),
    ('php-sources', 'php-sources.txt'),
    ('rce', 'rce.txt'),
    ('redirect', 'redirect.txt'),
    ('s3-buckets', 's3-buckets.txt'),
    ('sec', 'sec.txt'),
    ('servers', 'servers.txt'),
    ('sqli', 'sqli.txt'),
    ('ssrf', 'ssrf.txt'),
    ('ssti', 'ssti.txt'),
    ('strings', 'strings.txt'),
    ('takeovers', 'takeovers.txt'),
    ('upload-fields', 'upload-fields.txt'),
    ('urls', 'urls.txt'),
    ('xss', 'xss.txt'),
]


def run_gf_command(target_name, savepath,input_file, pattern, output_file):
    command = f"cat {savepath}{target_name}/{input_file} | gf {pattern} >> {savepath}{target_name}/{output_file}"
    subprocess.run(command, shell=True)



def webcrawl(target_name, savepath):
    command = f'katana -list {savepath}{target_name}/live.txt-o {savepath}{target_name}/crawl.txt'
    run_command(command)


def partenmatch(target_name, savepath):
    # Run gf commands for each pattern
    for pattern, output_file in patterns:
        run_gf_command(target_name, savepath,input_file, pattern, output_file)
    
    cat_commands = [
        f'cat {savepath}{target_name}/nabu.txt >> {savepath}{target_name}/nlive.txt',
        f'cat {savepath}{target_name}/live.txt >> {savepath}{target_name}/nlive.txt'
    ]

    for cat_command in cat_commands:
        run_command(cat_command)






