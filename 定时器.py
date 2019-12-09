# -*- coding:utf-8 -*-
import time
import schedule
from baidusearch import BaiduSearch



schedule.every().day.at("02:00").do(BaiduSearch.start)
while True:
    schedule.run_pending()
    time.sleep(1)
