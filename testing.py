from collections import Counter
import requests
import random
import re
from methods import tools
import os
import time
import signal

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


def getHtmlContent(url, failPath: '页面获取失败时写入 faledFile'):
    user_agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'mozilla/5.0(macintosh;u;intelmacosx10_6_8;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
        'mozilla/5.0(windows;u;windowsnt6.1;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
        'mozilla/5.0(macintosh;intelmacosx10.6;rv:2.0.1)gecko/20100101firefox/4.0.1',
        'mozilla/5.0(windowsnt6.1;rv:2.0.1)gecko/20100101firefox/4.0.1',
        'opera/9.80(macintosh;intelmacosx10.6.8;u;en)presto/2.8.131version/11.11',
        'opera/9.80(windowsnt6.1;u;en)presto/2.8.131version/11.11',

    ]
    header = {"User-Agent": random.choice(user_agent)}
    try:
        r = requests.get(url, headers=header, params={"Connection": "close"}, timeout=9.01)
        html = r.text
        print("获取成功—> len(html)", len(html), end='\t')
        return html
    except:
        with open(failPath, 'a+') as fLF:
            fLF.write(url + '\n')
        print("father获取错误—> ", '\t', url);


def getList(html: '页面内容', list: '接收资源的列表', url: '用于写 log', linkRe, failPath):
    num = 0
    t = ''
    html = html.replace('\n', '')
    for m in linkRe.finditer(html, re.S):
        if m:
            num += 1
            t = m.group(1) + '%' + m.group(2) + '%' + url
            # print(type(t),end='\t')
            list.append(t)
    if num == 0:
        with open(failPath, 'a+') as rMF:
            rMF.write(url + '\n')
            print("匹配为 0—> log is written.{}\t".format(url))
    else:
        print("{} —> resources added...!!!".format(num))


def hander(fli: '内存中被 pop 过的文件', path: '操作的主文件'):
    with open(path, 'w') as f:
        f.writelines(fli)

    print("写 {} 成功".format(path))


def main():
    reslist = []  # 资源
    fli = []  # 打开文件, pop 操作用
    path = '../spider_Files/resource/resourceMatchFailed.txt'  # 被操作的主文件
    failPath = '../spider_Files/resource/resourceMatchFailed_time_2.txt'  # 存失败的文件
    targetPath = '../spider_Files/resource/B_Resource.txt'  # 存资源的文件
    linkRe = re.compile(
        r'(https://pan.baidu.com/s/.{23}|https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;.{23}|https:&#47;&#47;pan.baidu.com&#47;s&#47;.{23}|https：pan.baidu.com s ).*?(提取码: .{4}|提取码：.{4}|\n提取码:.{4})')  # 回头加入完整的

    with open(path, 'r') as f:
        fli = f.readlines()

    while fli:
        s = fli.pop()
        url = s.replace('\n', '')
        if 'baidu.com' in url:
            t = random.random()
            print("百度大撒比, 等待{[.2f]}秒", format(t))
            time.sleep(t)

        html = getHtmlContent(url, failPath)

        getList(str(html), reslist, url, linkRe, failPath)
        print("表项剩余: {} , 资源获取: {}".format(len(fli), len(reslist)))
        if len(reslist) >= 1000:
            reslistSet = set(reslist)
            reslist = list(reslistSet)
            with open(targetPath, 'a+')as BR:
                BR.write('\n'.join(list(set(reslist))) + '\n')
                print('满 10000, 写文件!!!', len(reslist))

            hander(fli, path)
            reslist = []

    signal.signal(signal.SIGTERM, hander)
    signal.signal(signal.SIGINT, hander)
    signal.signal(signal.SIGTSTP, hander)
    print("******全部完成 —> 至此 realFatherLink.txt 获取 pan 资源 —>*********** ")


main()
