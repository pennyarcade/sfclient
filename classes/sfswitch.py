#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Switch Object

'''


class Switch(object):
    '''
        Make Switch statements possible
        TODO: Credits for this classs?
    '''
    def __init__(self, value):
        '''
            Constructor to Switch
        '''
        self.value = value
        self.fall = False

    def __iter__(self):
        '''
            Return the match method once, then stop
        '''
        yield self.match
        raise StopIteration

    def match(self, *args):
        '''
            Indicate whether or not to enter a case suite
        '''
        if self.fall or not args:
            return True
        # changed for v1.5, see below
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False
