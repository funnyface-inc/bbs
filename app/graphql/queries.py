#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
query.py
root query
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-01'
import graphene
#from app.graphql.comment.query import CommentQuery
from app.graphql.topic.query import TopicQuery


class Query(
    TopicQuery,
    #CommentQuery,
    graphene.ObjectType):
    pass
