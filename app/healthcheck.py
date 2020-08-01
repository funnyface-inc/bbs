#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
healthcheck.py
死活監視
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2018-06-12'
from flask import Blueprint

healthcheck = Blueprint('healthcheck', __name__)

@healthcheck.route('/healthcheck')
def get():
    """ 死活監視API
    """
    try:
        return '', 200
    except Exception:
        return '', 500
