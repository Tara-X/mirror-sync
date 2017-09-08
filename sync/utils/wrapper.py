# -*- coding: utf-8 -*-


def max_try(f):
    @wrap
    def wrap_function():
        print 'wrap function'
        