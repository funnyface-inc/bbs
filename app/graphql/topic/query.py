#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
query.py
topic query
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-02'
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from app.graphql.topic.schema import TopicConnection


class TopicQuery(graphene.ObjectType):

    topics = SQLAlchemyConnectionField(TopicConnection)
    topic = graphene.Field(TopicConnection, id=graphene.Int())

    def resolve_topic(self, info, id):
        query = TopicConnection.get_query(info)
        return query.filter_by(id=id).first()

    def resolve_users(self, info):
        query = TopicConnection.get_query(info)
        return query.all()
