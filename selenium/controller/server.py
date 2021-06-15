# -*- coding:utf-8 -*-
from flask import Flask

import util.CmmUtil as cu
import service.seleniumService as ta
from service.seleniumService import seleniumCrawling
import json

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1> 파이썬!! </h1>"


@application.route('/crawlingAPI', methods=['POST','GET'])
def crawling():
    print("crawling start!!")
    # 입력받을 문장

    rList = seleniumCrawling()
    print("rList : ", rList)
    print("2")
    div = json.dumps(rList, ensure_ascii=False)
    print("2")
    print("crawling end!!")
    return div


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
    # application.run(host="127.0.0.1")
