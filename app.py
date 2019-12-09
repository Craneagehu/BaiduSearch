
from flask import Flask, jsonify
from flask import request
import json

from gevent.pywsgi import WSGIServer

app = Flask(__name__)



@app.route('/baidu_search',methods=["GET","POST"])
def baidu_search():
    if request.method == "GET":
        date = request.args.get('date')
        with open(date+'.json','r',encoding='utf-8') as f:
            result = json.load(f)
            print(result)
            resp = jsonify(result)
            resp.headers['Access-Control-Allow-Origin'] = '*'  # 防跨域请求
            return resp


if __name__ == '__main__':
    app.config["JSON_AS_ASCII"] = False
    app.run(debug=True, host='0.0.0.0', port=5001)
    #WSGIServer(('0.0.0.0', 5001), app).serve_forever()
