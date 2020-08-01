#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Config.py
設定ファイル基底クラス
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-01'


class Config(object):
    HOST = '0.0.0.0'

    FLASK_ENV = 'test'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/bbs_dev?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_URL = 'redis://:@redis:6379/0'

    # 各種期限の設定値
    MAIL_VERIFICATION_EXPIRE = 30 * 24 * 60 * 60
    PASSWORD_RESET_EXPIRE = 30 * 60
    SESSION_EXPIRE = 30 * 24 * 60 * 60
    PREVIEW_EXPIRE = 60 * 60
