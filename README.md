# 在百度搜索关键词并返回 数据条数
操作如下：

1. 需要配置Python运行环境，python 3.x 以上的版本，准备好配置文件keywords.txt ( 注: 此文件为需要搜索的关键词, 每个词之间需要用英文逗号隔开)

2. 运行两个.py程序(定时器.py和app.py),通过执行 python3 定时器.py 和 python3 app.py 即可

3. 程序 定时器.py 主要是每天 02:00 定时的爬取配置文件中的关键词的条数，并以当天日期为文件名保存为json文档, 如 20191209.json

4. 程序 app.py 主要是提供外部调用API ( http://xx.xx.xx.xx : 5001/baidu_search?date=20191209) ,date是唯一参数，可以通过修改date的值，得到相应的json文件，
   如果没有该文件，会返回：‘没有该文件’。


nohup python3 定时器.py >/dev/null 2>&1 &   执行次命令可以让 定时器.py 一直运行在Linux服务器后台
nohup python3 app.py >/dev/null 2>&1 &      执行次命令可以让 app.py 一直运行在Linux服务器后台
