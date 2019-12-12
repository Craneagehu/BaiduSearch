# -*- coding:utf-8 -*-
import time
import schedule
from baidusearch import BaiduSearch

class Schedule(object):

    def Timer(self):
        schedule.every().day.at("02:00").do(BaiduSearch.start)
        # schedule.every(2).minutes.do(BaiduSearch.start)
        while True:
            schedule.run_pending()
            time.sleep(1)

    @classmethod
    def start(cls):
        work = cls()
        work.Timer()

if __name__ == '__main__':
    Schedule.start()