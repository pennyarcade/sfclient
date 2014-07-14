#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Character Object

'''

from classes.sfface import Face


class Character(object):
    '''
        Character information
    '''
    def __init__(self):
        '''
            Setup Character object
        '''
        self.face = Face()
        self.revertface = Face()

    def set_face(self, sface):
        '''
            set Face
        '''
        self.face = sface

    def set_revertface(self, sface):
        '''
            set Face backup for reverting
        '''
        self.revertface = sface
