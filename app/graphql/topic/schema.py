#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
schema.py
topic schema
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-02'
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.topic import Topic


class TopicConnection(SQLAlchemyObjectType):
    class Meta:
        model = Topic
        interfaces = (relay.Node, )
