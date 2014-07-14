#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Switch Object
        Taken from Activestate.command
        @author: Brien Beck [http://code.activestate.com/recipes/users/2425329/]
        @see: http://code.activestate.com/recipes/
                410692-readable-switch-construction-without-lambdas-or-di/
'''


class Switch(object):
    '''
        Make Switch statements possible

        Taken from Activestate.command
        @author: Brien Beck [http://code.activestate.com/recipes/users/2425329/]
        @see: http://code.activestate.com/recipes/
                410692-readable-switch-construction-without-lambdas-or-di/
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

    def get_value(self):
        '''
            return switch value
        '''
        return self.value
