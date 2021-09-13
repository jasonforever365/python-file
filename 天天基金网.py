import requests
import time
import 正则表达式

class EastMoneySpider:
    def request(self,page):
        dt = int(round(time.time()*1000))
        #通过把秒转换毫秒的方法获得13位的时间戳
        url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,200&dt=1615823350044&atfc=&onlySale=0".format(page, dt)
        heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        reponse = requests.get(url, headers=heads)
        self.convertStr2List(reponse.text)

    #把网页截取的字符串转化为列表
    def convertStr2List(self,resText):
        pattern = 正则表达式.compile(r'datas:(.*),count')
        resStr = pattern.search(resText).group(1)
        resStr = 正则表达式.sub(r"\[", '', resStr)
        resStr = 正则表达式.sub(r"\]", '', resStr)
        resStrList = resStr.split(',')
        result=[]
        tmpList=[]
        i = 0
        for resStr in resStrList:
            tmpList.append(resStr)
            i= i+1
            if i %21 ==0:
                result.append(tmpList)
                tmpList =[]
            print("将字符串转换为列表", result)

if __name__ == '__main__':
    moneySpider = EastMoneySpider()
    for page in range(1,3):
        print("spider page{0}---".format(page))
        moneySpider.request(page)