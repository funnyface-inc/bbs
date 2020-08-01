#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
development.py
development config
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '2020-08-01'
from config import Config


class Development(Config):
    HOST = 'http://localhost:5000'

    FLASK_ENV = 'development'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/bbs_dev?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_URL = 'redis://:@redis:6379/0'

    BUNDLE_ERRORS = True
