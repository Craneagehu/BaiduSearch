# -*- coding:utf-8 -*-
import os
import time
import json
from flask import request
from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer

app = Flask(__name__)



@app.route('/baidu_search',methods=["GET","POST"])
def baidu_search():
    if request.method == "GET":
        date = request.args.get('date')

        if os.path.exists(date + '.json'):
            with open(date+'.json','r',encoding='utf-8') as f:
                result = json.load(f)
                resp = jsonify(result)
                resp.headers['Access-Control-Allow-Origin'] = '*'  # 防跨域请求
                return resp
        else:
            resp = jsonify({"data":"没找到该文件","date":time.strftime("%Y-%m-%d",time.localtime())})
            resp.headers['Access-Control-Allow-Origin'] = '*'  # 防跨域请求
            return resp


def run():
    app.config["JSON_AS_ASCII"] = False
    #app.run(debug=True, host='0.0.0.0', port=5001)
    WSGIServer(('0.0.0.0', 5001), app).serve_forever()

if __name__ == '__main__':
    run()