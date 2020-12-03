from bs4 import BeautifulSoup
import os
import re

htmlList = []
for filename in os.listdir('./html'):
    htmlList.append(str(filename))
print(len(htmlList))
fatherLinks = []
h3 = []
for item in htmlList:
    if item.split('.')[-1] == 'html':
        filename = './html/' + str(item)
        print("正在打开" + filename)
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f, "html.parser")
            h3 = BeautifulSoup(str(soup.find_all('h3')), "html.parser")
            print("len(h3)", len(h3))
        for link in h3():
            father = link.get("href")
            if father is not None:
                fatherLinks.append(father)

            print("len(fatherLinks): ", len(fatherLinks))
        if len(fatherLinks) > 100:
            print("开始写文件")
            with open('./fatherLink/fatherLink.txt', 'a') as f:
                f.write('\n'.join(fatherLinks))
            fatherLinks = []