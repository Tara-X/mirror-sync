# -*- coding:utf-8 -*-

import sys
import unittest

from sync.utils import config

class TestUtil(unittest.TestCase):

    def test_extract(self):
        args_tuple = ('PATH', 'test_key',)
        sys.argv = ['app.py', '--test_key=testkeytestkey']
        
        parsed_args = config.extract_args(args_tuple)
        
        assert parsed_args[args_tuple[0]] is not None
        assert parsed_args[args_tuple[1]] == 'testkeytestkey'   
       


if __name__ == '__main__':
    unittest.main()
    
  
        

        