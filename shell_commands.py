import subprocess
subprocess.run(["ls", "-l"])

proc = subprocess.run(['ls', '-l'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

print(proc.stdout.decode())

new_proc = subprocess.run(['cat', 'names.txt'], check=True)