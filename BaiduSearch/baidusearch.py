# -*- coding:utf-8 -*-
import os
import re
import json
import time
import requests
import schedule
from lxml import etree

class BaiduSearch(object):

    def __init__(self):
        self.base_url = "https://www.baidu.com/s?wd="
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'BAIDUID=BB0C6EF0DCEC4D3FA6C2ADDB30DA7238:FG=1; BIDUPSID=BB0C6EF0DCEC4D3FA6C2ADDB30DA7238; BD_UPN=12314753; __cfduid=dec453d5a7965af966b33c367c4ed5ca01568703635; BDUSS=ZUWTUzZ3NjMlJSRU1ER2I2TkpUM3RWWjdhMFI2Q2dJNUh1RHFWMERMU3NhTTVkRVFBQUFBJCQAAAAAAAAAAAEAAADEwKSS0KFNc2kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKzbpl2s26ZdRD; MCITY=-132%3A; ispeed_lsm=2; PSTM=1573809092; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sugstore=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1453_21107_30210_30191; H_PS_645EC=5f10I3X6an0bhcUjf3HJvaMvSNjSQZdjk%2FLRyVtkx57ajBIqFZWxs2rJuNLw%2B9ozDzRY; BDSVRTM=151; COOKIE_SESSION=997_5_5_3_3_7_0_0_3_4_3_0_0_18_4_0_1575854175_1575603226_1575855168%7C9%232833_7_1575603131%7C2',
            'Host': 'www.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        self.items=[]

    def save2json(self):
        date = time.strftime("%Y-%m-%d",time.localtime())
        file_name = time.strftime("%Y%m%d",time.localtime())
        file_name = str(time.time())[10]
        with open(file_name+'.json','w',encoding='utf-8') as f:
            f.write(json.dumps({"data":self.items,"date":date},ensure_ascii=False))

    def run(self,kw):
        full_url = self.base_url+kw
        response = requests.get(full_url,headers=self.headers)
        response.encoding = "utf-8"
        e = etree.HTML(response.text)
        # 解析搜索关键词结果
        counts = e.xpath('//div[@class="nums"]/span[1]/text()')[0]
        # 提取关键词个数
        counts = ''.join(re.findall('\d+',counts))
        if counts:
            dic = {}
            dic[kw] = counts
            self.items.append(dic)



    def read_keywords(self):
        with open("keywords.txt",'r',encoding='utf-8') as f:
            keywords = f.read()
            keywords_list = keywords.split(',')
            for kw in keywords_list:
                self.run(kw)

    def main(self):
        self.read_keywords()
        self.save2json()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    @classmethod
    def start(cls):
        baidu = cls()
        baidu.main()


if __name__ == '__main__':
    BaiduSearch.start()





