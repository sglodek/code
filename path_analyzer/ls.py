import subprocess
output = subprocess.run("ls", stdout=subprocess.PIPE, shell=True)
print(output.stdout)