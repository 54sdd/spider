from collections import Counter
import requests
import random
import re
import time


def getHtmlContent(url):
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
        r = requests.get(url, headers=header, params={"Connection": "close"},timeout=9.01)
        html = r.text
        print("获取成功—> len(html)", len(html), end='\t')
        return html
    except:
        with open('resource/fatherLinkFailed.txt', 'a+') as fLF:
            fLF.write(url + '\n')
        print("father获取错误—> ");


def getList(html, list, url, linkRe):
    # linkRe2000 = re.compile(r'pan.baidu.com/s/.{323}|pan.baidu.com&amp;#47;s&amp;#47;.{323}')  # 回头加入完整的
    # linkRe2000 = re.compile(r'(https://pan.baidu.com/s/.{23}|https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;.{23}|https:&#47;&#47;pan.baidu.com&#47;s&#47;.{23}|https：pan.baidu.com s ).*?(提取码: .{4}|提取码：.{4}|提取码:.{4})')  # 回头加入完整的

    # linkRe23 = re.compile(r'pan.baidu.com/s/.{23}|pan.baidu.com&amp;#47;s&amp;#47;.{23}')
    # codeRe = re.compile(r'提取码：.{4}|提取码:.{4}')
    num = 0
    t = ''
    for m in linkRe.finditer(html):
        if m:
            num += 1
            t = m.group(1) + '%' + m.group(2) + '%' + url
            # print(type(t),end='\t')
            list.append(t)
    if num == 0:
        with open('resource/resourceMatchFailed.txt', 'a+') as rMF:
            rMF.write(url + '\n')
            print("匹配为 0—> URL 已写入. URL:  ", url)
    else:
        print("{} —> resources added...!!!".format(num))


def main():
    reslist = []
    linkRe = re.compile(
        r'(https://pan.baidu.com/s/.{23}|https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;.{23}|https:&#47;&#47;pan.baidu.com&#47;s&#47;.{23}|https：pan.baidu.com s ).*?(提取码: .{4}|提取码：.{4}|提取码:.{4})')  # 回头加入完整的
    with open('fatherLink/realFatherLink2.txt', 'r') as rFL:
        for rfl in rFL:
            url = rfl.replace('\n', '')
            html = getHtmlContent(url)

            time.sleep(1)

            getList(str(html), reslist, url, linkRe)
            if len(reslist) >= 100:
                with open('resource/B_Resource.txt', 'a+')as BR:
                    BR.write('\n'.join(list(set(reslist)))+'\n')
                    print('满 100, 写文件')
                reslist = []

        print("******全部完成 —> 至此 realFatherLink.txt 获取 pan 资源 —>*********** ")


main()
