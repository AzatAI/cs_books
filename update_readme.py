import os
from datetime import datetime

all_files_directories = os.listdir('.')

file_types = set()
# Get all file types.
for each in all_files_directories:
    file_types.add(os.path.splitext(each)[-1])

os.system("rm -rf README.md")
os.system("echo '# List of the Books'>>README.md")
count = 1
command = ''
full_command = ''
remove_list = ['.DS_Store', 'README.md', '.gitignore', '.github', 'process.py', '.git']

for each in all_files_directories:
    if ('.pdf' in each) or ('.Pdf' in each) or ('.PDF' in each) or ('.EPUB' in each) or ('.epub' in each):
        command = '{}. {}'.format(count, each)
        full_command = '''echo "{}">>README.md'''.format(command)
        os.system(full_command)
        count += 1

messages = [
    '\n\n\n'
    'THE BOOKS ARE COLLECTED FROM THE INTERNET AND SHOULD ONLY BE USED FOR EDUCATIONAL PURPOSES\n',
    'The markdown file itself is created by the process.py python script'
]

for message in messages:
    myCommand = "echo '{}' >>README.md".format(message)
    os.system(myCommand)


markdown = "### How to contribute?\nFork the repository and star it, clone OR download the repository, put your books inside. Finally, Do not forget to pull request.\n"
os.system('''echo "{}">>README.md'''.format(markdown))
