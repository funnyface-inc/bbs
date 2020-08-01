#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
topic.py
掲示板本体
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '2020-08-01'
from app.models import Model
from app.extensions import db


class Topic(Model):
    __tablename__ = 'topics'

    title = db.Column(db.String(255))
    description = db.Column(db.String(255))

    comments = db.relationship('Comment', back_populates='topic')
