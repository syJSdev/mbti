# mbti-test

<http://mbti.axiaoxin.com>

A website for doing the Myers-Briggs Type Indicator Test.

MBTI 职业性格测试

     __  __ ____ _____ ___    _____ _____ ____ _____
    |  \/  | __ )_   _|_ _|  |_   _| ____/ ___|_   _|
    | |\/| |  _ \ | |  | |_____| | |  _| \___ \ | |
    | |  | | |_) || |  | |_____| | | |___ ___) || |
    |_|  |_|____/ |_| |___|    |_| |_____|____/ |_|

# Run for dev

```
# create your virtualenv then ...
virtualenv venv --python=python2.7
source venv/bin/activate
pip install -r requirements.txt
venv/bin/python server.py
```

# 多语言配置

https://wizardforcel.gitbooks.io/the-flask-mega-tutorial-2017-zh/content/docs/13.html

1. 编辑多语言模板: `{{ _("text") }}` (Use `%%` to escape `%`.)
2. 生成翻译 pot 模板: `pybabel extract -F babel.cfg -o messages.pot .`
3. 创建翻译 po 文件: `pybabel init -i messages.pot -d translations -l en`
4. 翻译 po 文件中 msgid 对应的 msgstr
5. 编译翻译结果得到 mo 文件: `pybabel compile -d translations`

修改多语言模板后更新翻译：

先用上面的命令重新生产 pot 文件，然后更新翻译: `pybabel update -i messages.pot -d translations`

# Stargazers over time

[![Stargazers over time](https://starchart.cc/axiaoxin/mbti.svg)](https://starchart.cc/axiaoxin/mbti)
