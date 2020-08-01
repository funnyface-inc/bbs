#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
comment.py
掲示板へのコメント
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '2020-08-01'
from app.models import Model
from app.extensions import db


class Comment(Model):
    __tablename__ = 'comments'

    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    body = db.Column(db.String(255))

    topic = db.relationship('Topic', back_populates='comments')
