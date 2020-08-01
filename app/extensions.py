#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
extensions.py
Flask拡張一覧
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-01'
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_cors import CORS

db = SQLAlchemy()
redis = FlaskRedis(decode_responses=True)
cors = CORS()
