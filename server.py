# !/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from flask import Flask, render_template, request
from flask_babel import Babel

import settings
from mbti import MBTI_BP

SERVER = Flask(__name__)
SERVER.config.from_pyfile('settings.py')
babel = Babel(SERVER)


@SERVER.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@SERVER.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


@babel.localeselector
def get_locale():
    '''编写该方法后，会自动设置语言
    babel实例提供了一个localeselector装饰器。为每个请求调用装饰器函数以选择用于该请求的语言。
    Flask中request对象的属性accept_languages用于处理客户端发送的带Accept-Language头部的请求
    best_match()方法中了，该方法将应用提供的语言列表作为参数并返回最佳选择。
    '''
    # https://www.science.co.il/language/Locale-codes.php
    locale = request.cookies.get(settings.LOCALE_COOKIE_KEY)
    if locale == "":
        locale = request.accept_languages.best_match(['zh', 'en'])
    return locale


SERVER.register_blueprint(MBTI_BP)

if __name__ == '__main__':
    SERVER.run('0.0.0.0')
