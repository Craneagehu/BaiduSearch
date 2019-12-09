# -*- coding:utf-8 -*-
import time
import schedule
from baidusearch import BaiduSearch

schedule.every(1).minutes.do(BaiduSearch.start)
while True:
    schedule.run_pending()
    time.sleep(1)