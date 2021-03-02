# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 22:44
# @Author  : XU
# @File    : interface.py
# @Software: PyCharm
from flask import Flask, json, request, session, redirect, url_for, render_template, make_response
from my_api.lib.tools import my_db
from my_api.data.result import result

server = Flask(__name__)


@server.route('/')
def home():
    return render_template('home.html')


@server.route('/register', methods=['POST'])
def register():
    username = request.values.get('username')
    password = request.values.get('password')
    if username and password:
        sql = f"SELECT * from app where username={username};"
        res = my_db(sql)
        if res.lower() == 'ok':
            res = {'msg': '注册成功', 'msg_code': 0}
        else:
            if res:
                res = {'msg': '用户已存在', 'msg_code': 2001}
            else:
                pass
        return res
    else:
        res = {'msg': '请输入用户名和密码', 'msg_code': 1001}
        return json.dumps(res, ensure_ascii=False)


@server.route('/index', methods=['GET'])
def index():
    # res = {'msg': '这是一个接口', 'msg_code': 0}
    res = result
    return json.dumps(res, ensure_ascii=False)


@server.route('/hello')
@server.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@server.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get('user') == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return f"Hello {session['user']}"
    else:
        title = request.args.get('title', 'Default')
        response = make_response(render_template('login.html', title=title), 200)
        response.headers['key'] = 'value'
        return response


@server.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
