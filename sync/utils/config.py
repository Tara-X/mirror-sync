# -*- coding: utf-8 -*-
import os
import sys
import argparse

ROOT_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
STATIC_PATH = os.path.join(ROOT_PATH, 'static')
TEMPLATE_PATH = os.path.join(ROOT_PATH, 'tmpl')
LOG_PATH = os.path.join(ROOT_PATH, 'logs')

from .compact import clean_dict

'''
    Extract arguments from command/environ/raw_input
'''
def extract_args(args_tuple):

    default_args = dict()
    for k in args_tuple:
        default_args[k] = None
    
    parser = argparse.ArgumentParser()

    for k in args_tuple:
        parser.add_argument(u'--{0}'.format(k), default=None)
    
    parser_args = parser.parse_known_args()[0].__dict__
    env_args = dict([(k, os.environ.get(k)) for k in args_tuple if os.environ.get(k) is not None])

    default_args.update(clean_dict(env_args))
    default_args.update(clean_dict(parser_args))

    
    for k, v in default_args.items():
        if v is None:
            default_args[k] = raw_input(u'input {0} > '.format(k))

    return default_args
     




