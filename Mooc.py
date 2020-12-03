import re
from methods import tools
import random
import requests


# 打开文件, 读取到变量,
# re.search()

# 打开文件
# 预设正则

def getURLContent(url):
    user_agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'mozilla/5.0(macintosh;u;intelmacosx10_6_8;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
        'mozilla/5.0(windows;u;windowsnt6.1;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
        'mozilla/5.0(macintosh;intelmacosx10.6;rv:2.0.1)gecko/20100101firefox/4.0.1',
        'mozilla/5.0(windowsnt6.1;rv:2.0.1)gecko/20100101firefox/4.0.1',
        'opera/9.80(macintosh;intelmacosx10.6.8;u;en)presto/2.8.131version/11.11',
        'opera/9.80(windowsnt6.1;u;en)presto/2.8.131version/11.11',

    ]
    agent = random.choice(user_agent)
    header = {'User-Agent': agent}
    try:
        r = requests.get(url, headers=header)
        r.encoding = r.apparent_encoding
        demo = r.text
        print("return html...", end='')
        return demo
    except:
        with open('./resource/resourceMatchFailed.txt', 'a') as f:
            f.write(url + '\n')
        print("Failed connection —> but was written ", url)


def findAndAppend(html, list, linkPat, codePat, url):
    links = re.findall(linkPat, html)
    codes = re.findall(codePat, html)

    with open('./resource/B_Resource.txt', 'a') as f1:
        if len(links) == len(codes) and len(links) != 0:
            for i in range(len(links)):
                list.append([str(links[i]), str(codes[i]), url])
            f1.write('\n'.join(str(list)))
            print("resources have been written!!!{}".format(len(list)))
            list = []

        else:
            with open('./resource/resourceMatchFailed.txt', 'a') as f:
                f.write(url + '\n')
            print("Failed matchs —>but was written ", url)


def main():
    resList = []
    # allPat = re.compile(r'pan.baidu.com/s/.{23}', '(提取码：.{4})')
    linkpat = re.compile(r'pan.baidu.com.{26}')
    codepat = re.compile(r'提取码：|提取码:.{4}')
    with open('./fatherLink/realFatherLink.txt', 'r+') as f:
        for url in f:

            html = getURLContent(url.replace('\n',''))
            print("Loading—> {}", format(url))
            findAndAppend(str(html), resList, linkpat, codepat, url)


main()
