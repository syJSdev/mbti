# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import json
import random

import settings
from flask import (Blueprint, abort, flash, make_response, redirect,
                   render_template, request, send_from_directory)
from flask_babel import force_locale
from flask_babel import gettext as _

from utils import (get_questions, get_result, get_tested_count, get_types_desc,
                   incr_tested_count)

MBTI_BP = Blueprint('mbti', __name__)


@MBTI_BP.route('/')
def welcome():
    #  return render_template('mbti/welcome.html')
    tested_count = get_tested_count()

    arg_lang = request.args.get("lang")
    if arg_lang in settings.SUPPORT_LANGS:
        with force_locale(arg_lang):
            resp = make_response(
                render_template('mbti/home.html', tested_count=tested_count))
            resp.set_cookie(settings.LOCALE_COOKIE_KEY, arg_lang)
    else:
        resp = make_response(
            render_template('mbti/home.html', tested_count=tested_count))

    return resp


@MBTI_BP.route('/home/')
def home():
    '''首页'''
    return redirect("/")


@MBTI_BP.route('/about/')
def about():
    '''关于页面'''
    return render_template('mbti/about.html')


@MBTI_BP.route('/personalities/', defaults={'page': 'index'})
@MBTI_BP.route('/personalities/<page>/')
def personalities(page):
    '''SHOW MBTI TYPES'''
    page = page.lower()
    if page == 'index':
        return render_template('mbti/personalities/index.html',
                               types_desc=get_types_desc())
    return render_template('mbti/personalities/%s.html' % page)


@MBTI_BP.route('/test/', methods=('GET', 'POST'))
def test():
    '''测试页面视图'''
    if request.method == "POST":
        answers = json.loads(request.values.get('answers'))
        result = get_result(answers)
        flash(_("测试完成，你的性格分析结果为:") + result)
        incr_tested_count(result)
        return result.lower()
    questions = get_questions()
    random.shuffle(questions)
    return render_template('mbti/test.html', questions=questions)


@MBTI_BP.route('/messageboards/')
def messageboards():
    '''deer要求的留言板，偷懒用多说算了'''
    return render_template('mbti/disqus.html')


@MBTI_BP.route('/ads.txt')
def ads_txt():
    '''google 广告 ads.txt'''
    return send_from_directory("static", "ads.txt")
