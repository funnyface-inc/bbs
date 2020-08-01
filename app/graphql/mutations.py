#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
mutation object
mutation
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-06'
import graphene
from app.graphql.topic.mutation import TopicMutation
#from app.graphql.mutation import CommentMutation


class Mutation(
    TopicMutation,
    #CommentMutation,
    graphene.ObjectType):
    pass
