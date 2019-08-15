"""
Plz be informed that the rule for comment your changes in Github for repository is 
simply based on the books target language, for example:
For adding a book named 'professional python programming.pdf' plz just comment 'python'
and thats all!

备注: 为了保持该仓库的简洁和高效,在提交新的书籍时候的评论规则统一为如下: 
请您使用书本的目标程序语言为 Git 的评论,比如您在上传一本有关 Python 和 MySQL 的书籍时候,
您的 Git 评论应该是 'Python, Mysql' 仅此而已!
"""
import os
from github import Github
import time
new_comers = [
    'PythonNotesForProfessionals.pdf',
    'CNotesForProfessionals.pdf',
    'AlgorithmsNotesForProfessionals.pdf',
    'CSharpNotesForProfessionals.pdf',
    'BashNotesForProfessionals.pdf',
    'CPlusPlusNotesForProfessionals.pdf',
    'CSSNotesForProfessionals.pdf',
    'GitNotesForProfessionals.pdf',
    'iOSNotesForProfessionals.pdf',
    'HTML5CanvasNotesForProfessionals.pdf',
    'JavaScriptNotesForProfessionals.pdf',
    'JavaNotesForProfessionals.pdf',
    'jQueryNotesForProfessionals.pdf',
    'LinuxNotesForProfessionals.pdf',
    'LaTeXNotesForProfessionals.pdf',
    'MATLABNotesForProfessionals.pdf',
    'MongoDBNotesForProfessionals.pdf',
    'ObjectiveCNotesForProfessionals.pdf',
    'NodeJSNotesForProfessionals.pdf',
    'MySQLNotesForProfessionals.pdf',
    'PHPNotesForProfessionals.pdf',
    'PerlNotesForProfessionals.pdf',
    'ReactNativeNotesForProfessionals.pdf',
]


# Remove the duplicated items from the list simply by converting the list to set in python
# 去掉重读的数据. 上面的新书籍是通过脚本自动添加的,有时候会有重复的书籍,需要移除
# 将一个 Python 的 list 转化成 set 可以简单有效地去重.

temp_set = set(new_comers)
final_list = list(temp_set)

print('总共有{}本书需要上传,正在准备!'.format(len(final_list)))

token = []

# NOTE: YOU HAVE TO FILL YOUR GITHUB TOKEN IN token.azt FILE FIRST!
#注意: 所有书籍的上传与下载全部用 Python 完成.为此您需要在 token.azt 文件中填写您的 Github token


with open('token.azt') as f:
    lines = f.readlines()
    for line in lines:
        token.append(line)


g = Github(token[0])
user = g.get_user()
repo = g.get_repo("yaakovazat/cs_books")
print("Current working repository:\n {}".format(repo))


os.system('git add .')
os.system("git commit -m 'new books uploaded'")
os.system('git push')
