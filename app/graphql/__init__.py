#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
schema object
schema
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
import graphene
from app.graphql.queries import Query
from app.graphql.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
