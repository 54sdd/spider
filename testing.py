from collections import Counter
import requests
import random
import re
from methods import tools
import os

'''
print("\033[0;31;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;32;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;33;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;34;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;35;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;36;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;39;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;38;10m\tFinished—> {} has been written!!!\033[0m")
print("\033[0;30;10m\tFinished—> {} has been written!!!\033[0m")
'''
'''
path1 = './testing.txt'
path2 = './testing2.txt'
content_read = ''
contentReadline = ''
contentReadlines = []
with open(path1, 'r') as f:
    # contentReadlines = f.readlines()
    # f.seek(0)
    # content_read = f.read()
    # f.seek(0)
    # contentReadline = f.readline()
    contentReadlines = f.readlines()
# print(type(content_read))
# print(type(content_readline))
# print(type(contentReadlines))
s = set(contentReadlines)
# print(content_read)
# print(contentReadline)
# print(contentReadlines)

with open(path2, 'w') as f:
    f.writelines(tools.deDup(contentReadlines))
'''


# 去重目录中所有文件的重复项

print(tools.deDup.__annotations__)
