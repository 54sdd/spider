from collections import Counter
import requests
import random
import re

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
li = []
st = '1'+'$'+'2'+'$'+'3'
print(type(st))
with open('testing.txt','a') as f:

    for i in range(10):
        li.append(st)
        li.append('123')
        li.append('345')
    f.write('\n'.join(list(set(li)))+'\n')


