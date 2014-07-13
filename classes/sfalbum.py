#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Album Object

'''


class Album(object):
    '''
        handle collectors album data
    '''
    def __init__(self, effect=False, category=0, page=0):
        '''
            setup collectors album
        '''
        self.effect = effect
        self.category = category
        self.page = page
