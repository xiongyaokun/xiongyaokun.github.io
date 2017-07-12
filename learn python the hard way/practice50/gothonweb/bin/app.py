#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/9 7:38
# @Author  : xiongyaokun
# @Site    : 
# @File    : app.py
# @Software: PyCharm


import web

urls = (
    '/', 'Index',
    '/hello', 'Hello',
)

app = web.application(urls, globals())
render = web.template.render('templates\\')

# 此类匹配urls中的Index
class Index(object):
    def GET(self):
        # greeting = "Hello World!"
        # # return greeting
        # return render.index(greeting=greeting)
        return render.hello_form()

class Hello(object):

    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "Hello, %s, %s" % (form.name, form.greet)
        return render.hello(greeting=greeting)


if __name__ == '__main__':
    app.run()