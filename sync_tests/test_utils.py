# -*- coding:utf-8 -*-

import sys
import unittest

from sync.utils import config
from sync.utils import helper

class TestUtil(unittest.TestCase):

    def test_extract_args(self):
        args_tuple = ('PATH', 'test_key',)
        sys.argv = ['app.py', '--test_key=testkeytestkey']
        
        parsed_args = config.extract_args(args_tuple)
        
        assert parsed_args[args_tuple[0]] is not None
        assert parsed_args[args_tuple[1]] == 'testkeytestkey'   
       
    
    def test_qiniu_file_exists(self):

        qn = helper.QiniuBudget()

        # qn.resource_exists('index.html')
        # qn.resource_exists('dfsdfsdfsdf')
        qn.resource_exists('color_admin_v1.7.zip')

if __name__ == '__main__':
    unittest.main()
    
  
        

        