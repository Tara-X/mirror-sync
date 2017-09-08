# -*- coding:utf-8 -*-

import os
import sys

from utils import config

def main():
    print sys.argv
    args_tuple = ('PATH', 'test_key',)
    parsed_args = config.extract_args(args_tuple)
    print parsed_args
    
if __name__ == '__main__':
    main()

