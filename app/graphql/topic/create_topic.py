#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
create_topic.py
photo mutation
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-02'
import graphene
from app.extensions import db
from app.graphql.topic.schema import TopicConnection
from app.graphql.topic.input import TopicInput
from app.models.topic import Topic


class CreateTopic(graphene.Mutation):

    topic = graphene.Field(lambda: TopicConnection)

    class Arguments:
        input = TopicInput(required=True)

    def mutate(self, info, input=None):
        topic = Topic(**input)
        db.session.add(topic)
        return CreateTopic(topic=topic)
