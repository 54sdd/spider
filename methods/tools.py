import signal

import requests
import random
import os
import time


# 写百度 father 失败的链接
# 这是在程序退出时写
def hander(signum, frame):
    with open('./failed_url.txt', 'a+') as f:
        f.write(str(failed_url))

    print("写 failed_url 成功")
    print(signum, frame)


signal.signal(signal.SIGTERM, hander)
signal.signal(signal.SIGINT, hander)
signal.signal(signal.SIGTSTP, hander)

user_agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'mozilla/5.0(macintosh;u;intelmacosx10_6_8;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
    'mozilla/5.0(windows;u;windowsnt6.1;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
    'mozilla/5.0(macintosh;intelmacosx10.6;rv:2.0.1)gecko/20100101firefox/4.0.1',
    'mozilla/5.0(windowsnt6.1;rv:2.0.1)gecko/20100101firefox/4.0.1',
    'opera/9.80(macintosh;intelmacosx10.6.8;u;en)presto/2.8.131version/11.11',
    'opera/9.80(windowsnt6.1;u;en)presto/2.8.131version/11.11',

]


# 百度的 getPage, 特殊—> KV, 翻页方式
def getBaiduPage(url, kv, count):
    # header = {'User-Agent': user_agent[3]}
    '''   header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

    if count > 20:
        agent = random.choice(user_agent)
        header = {'User-Agent': agent}
        staticmethod.count = 0
        print("Set Count—>  = 0")
        print("Header 更换—> User-Agent 更换为{} ".format(agent))
        
'''
    agentgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',

    agent = random.choice(user_agent)
    header = {'User-Agent': agent}

    r = requests.get(url, headers=header, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    print("return demo...", end='')
    return demo

    # print(r.request.headers)


# 百度用的 KV 生成
def joinKV(kv1, kv2):
    kv = kv1.copy()
    kv.update(kv2)
    kv.update({"Connection": "close"})
    return kv


# 百度—> 写 html 到本地
def writeBaiduPage(content, word, pn):
    root = './html/'
    path = word + str(pn['pn'])
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(root + path + '.html', 'w') as f:
            f.write(content)
            # print("Finished—> {} has been written!!!".format(root + path + '.html'))

    return root + path + '.html'


failed_url = []


# 百度—> 被 ban, 休息 90s
def sleep_90(w, p):
    failed_url.append(w + str(p))
    print("\033[0;31;10m\t警告—> 小于 2000 被隔离, 等待 90 秒\033[0m")
    time.sleep(90)


# ******************  上面是百度的工具   *********************


# 列表去重
def deDup(fileName: '要修改的文件名(产生 deDup 文件)'):
    try:
        with open(fileName, 'r') as f:
            li = f.readlines()
        sli = set(li)
        li = list(sli)
        with open(fileName + '_deDup', 'w') as f:
            f.writelines(li)
    except:
        print('文件去重错误')

# 去重目录中所有文件的重复项
