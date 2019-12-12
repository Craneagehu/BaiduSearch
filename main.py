#-*- coding:utf-8 -*-
from multiprocessing import Process
from 定时器 import Schedule
import app


def exe():
    # 1.1 定义一个列表，用于存储要启动的进程
    process_list = []
    # 1.2 创建启动爬虫 的进程，添加到列表中
    process_list.append(Process(target=app.run))
    # 1.3 创建 定时器的进程，添加到列表中
    process_list.append(Process(target=Schedule.start))


    # 1.5 遍历进程列表，启动所有进程
    for process in process_list:
        process.daemon= True
        process.start()

    # 1.6 遍历进程列表，让主进程等待子进程的完成
    for process in process_list:
        process.join()


if __name__ == '__main__':
    exe()
