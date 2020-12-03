import signal
# is this here???
from methods import tools
import random
import time

rootURL = "http://baidu.com:q" \
          "" \
          "/s"
words = [
         'q',
         'r',
         's',
         't',
         'u',
         'v',
         'w',
         'x',
         'y',
         'z',
         '1',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         'A',
         'B',
         'C',
         'D',
         'E',
         'F',
         'G',
         'H',
         'I',
         'J',
         'K',
         'L',
         'M',
         'N',
         'O',
         'P',
         'Q',
         'R',
         'S',
         'T',
         'U',
         'V',
         'W',
         'X',
         'Y',
         'Z', ]
pnNum = 130
count = 0
tmp = ""
for word in words:
    kw = {'wd': 'pan.baidu.com' + ' ' + word + ' ' + '提取码'}
    while 1:
        if pnNum < 760 or pnNum == 0:
            pn = {'pn': pnNum}
            pnNum += 10
            for i in range(10):
                if i == 9:
                    tools.sleep_90(word, pnNum)
                    break
                try:
                    tmp = tools.getBaiduPage(rootURL, tools.joinKV(kw, pn), count)

                    if len(tmp) > 5000:
                        print("文件大小", len(tmp))
                        fileName = tools.writeBaiduPage(tmp, word, pn)
                        print("\033[0;32;10m\tFinished—> {} has been written!!!\033[0m".format(fileName))
                        break
                    else:
                        tools.sleep_90(word, pnNum)

                except:
                    time.sleep(3)
                    print("重试—> {}{}重试第{}次".format(word, pnNum, i + 1))

            t = random.random() * 10 + 12
            print("\033[0;33;10m\t间隔—> 抓取间隔 {:.3f} s\033[0m".format(t))
            time.sleep(t)
            count += 1
            print(count)
        else:
            pnNum = 0
            print("************ Next letter ************")
            break
