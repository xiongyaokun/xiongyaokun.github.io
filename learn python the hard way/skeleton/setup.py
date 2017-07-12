#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 16:42
# @Author  : xiongyaokun
# @Site    : 
# @File    : setup.py
# @Software: PyCharm


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'projecyname',
    'author': 'xiongyaokun',
    'url': '',
    'download_url': '',
    'author_email': 'bht_xyk@126.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
