#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
muation.py
topic mutations
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-02'
import graphene
from app.graphql.topic.create_topic import CreateTopic


class TopicMutation(graphene.ObjectType):
    createTopic = CreateTopic.Field()
