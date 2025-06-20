import subprocess

subprocess.run(["python3", "copy_files.py"], check=True)
subprocess.run(["python3", "change_values.py"], check=True)