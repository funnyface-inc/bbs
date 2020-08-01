#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Base Model
モデル基底クラス
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-01'
import json
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.types import TypeDecorator, JSON
from app.extensions import db


class Model(db.Model):
    """ モデル基盤クラス
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, default=datetime.utcnow)

    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class JSON(TypeDecorator):
    impl = JSON

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        try:
            return json.loads(value)
        except TypeError:
            return None
