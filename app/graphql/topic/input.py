#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
topic input
topic_input.py
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2020-08-02'
import graphene


class TopicInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=False)
