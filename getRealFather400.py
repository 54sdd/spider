import requests
import random
import time

user_agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'mozilla/5.0(macintosh;u;intelmacosx10_6_8;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
    'mozilla/5.0(windows;u;windowsnt6.1;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
    'mozilla/5.0(macintosh;intelmacosx10.6;rv:2.0.1)gecko/20100101firefox/4.0.1',
    'mozilla/5.0(windowsnt6.1;rv:2.0.1)gecko/20100101firefox/4.0.1',
    'opera/9.80(macintosh;intelmacosx10.6.8;u;en)presto/2.8.131version/11.11',
    'opera/9.80(windowsnt6.1;u;en)presto/2.8.131version/11.11',

]


def main():
    realFatherLink = []

    with open('../spider_Files/fatherLink/exchangError.txt', 'r') as f:
        print("f 已打开")

        for line in f:
            if line:
                url = line;
                header = {"User-Agent": random.choice(user_agent)}
                try:
                    r = requests.get(url, headers=header)
                    url = r.request.url
                    realFatherLink.append(url)
                    print("len(realFatherLink)", len(realFatherLink))

                except:
                    with open('../spider_Files/fatherLink/exchangErrorAgalin.txt', 'a') as f2:
                        f2.write(url + '\n')
                    print('转换出错, 写入 exchangeErroragain.txt')

                if len(realFatherLink) > 100:
                    print("超过 100, 持久化, 删除")
                    with open('../spider_Files/fatherLink/realFatherLink.txt', 'a') as f1:
                        f1.write('\n'.join(realFatherLink))
                        realFatherLink = []
            else:
                continue
    print("****************完成*****************8")


main()
