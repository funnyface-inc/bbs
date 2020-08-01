#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
wsgi.py
サーバ起動スクリプト
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '2020-08-01'
import os
from app import create_app


app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
