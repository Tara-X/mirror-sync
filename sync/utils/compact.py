# -*- coding: utf-8 -*-

'''
    remove keys which value is None
'''
def clean_dict(dict_obj):
    items = [x for x in dict_obj.items() if x[1] is not None]
    return dict(items)
    
