import subprocess
comand = 'cat /etc/os-release'
if __name__ == '__main__':
result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
result_out = result.stdout
if 'text' in result_out
print('TRUE')
else:
print('FAIL')