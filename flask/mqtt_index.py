#!/usr/bin/python3
from flask import Flask, render_template, jsonify, request
# 플라스크의 request와 python의 requests는 다른 모듈!

app = Flask(__name__)  # 플라스크 서버 만드는 태그


@app.route('/')
def home():
    # return 'Hello! world'
    return render_template('index.html')
    # return render_template('/home/bsmouse/work/flask/index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
