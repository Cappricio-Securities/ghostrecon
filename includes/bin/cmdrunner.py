import os
import subprocess


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True,
                                stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None
