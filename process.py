import os
import subprocess
from datetime import datetime
all_files_directories = os.listdir('.')


file_types = set()
# Get all file types.
for each in all_files_directories:
    file_types.add(os.path.splitext(each)[-1])
os.system("rm -rf README.md")
os.system("echo '# List of the Books'>>README.md")
count = int()
count = 1
command = ''
full_command = ''
for each in all_files_directories:
    if ('.pdf' or '.Pdf' or '.epub') in each:
        command = '{}. {}'.format(count, each)
        full_command = '''echo "{}">>README.md'''.format(command)
        os.system(full_command)
        count = count + 1

messages = [
    '\n\n\n'
    'THE BOOKS ARE COLLECTED FROM THE INTERNET AND ONLY USED FOR EDUCATIONAL PURPOSE\n',
    'The mark down file itself is created by process.py python script'
]
for message in messages:
    myCommand = "echo '{}' >>README.md".format(message)
    os.system(myCommand)
os.system("echo '\n\n #### Last updated in:{}'>>README.md\n\n\n".format(datetime.now()))
        


markdown = "### How to contribute?\nFork the repository and star it, clone OR download the reposiitory, put your books inside, run the python script process.py, the script will automatically do the rest. Finally, Do not forget to pull request.\n### 如何贡献?\nFork这个仓库,记得同时点个Star,将仓库下载克隆或者下载到本地,将您的图书放到该目录,运行 prosecc.py 脚本,其余的就交给脚本自动处理吧! 对了,不要忘记 Full Request 哈!"
os.system('''echo "{}">>README.md'''.format(markdown))