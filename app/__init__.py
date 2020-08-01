#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__init__.py
create_app init script
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '2020-08-01'
from flask import Flask
from flask_migrate import Migrate
from flask_graphql import GraphQLView
from inflection import camelize
from app.healthcheck import healthcheck
from app.extensions import db, redis, cors
from app.transactions import Transaction
from app.models.topic import Topic
from app.models.comment import Comment
from app.graphql import schema


def create_app(env='development'):
    """ bss アプリケーションを作成する
    """
    app = Flask(__name__)
    if env not in ['development', 'production']:
        raise Exception('unkown environment. you should one of the development, staging or production')
    config_path = 'config.{}.{}'.format(env, camelize(env))
    app.config.from_object(config_path)

    # interviewz plugin
    transaction = Transaction()

    cors.init_app(app)
    db.init_app(app)
    redis.init_app(app)
    transaction.init_app(app)
    Migrate(app, db)

    app.register_blueprint(healthcheck, url_prefix='/')
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    return app
