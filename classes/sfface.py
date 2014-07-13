#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Face Object

'''


class Face(object):
    '''
        character face
    '''
    def __init__(self, beard=1, brows=1, cclass=1, color=1, eyes=1, ears=1,
                 hair=1, male=True, mouth=1, nose=1, special=1, special2=1,
                 volk=0):
        '''
            setup face object
        '''
        self.beard = beard
        self.brows = brows
        self.cclass = cclass
        self.color = color
        self.eyes = eyes
        self.ears = ears
        self.hair = hair
        self.male = male
        self.mouth = mouth
        self.nose = nose
        self.special = special
        self.special2 = special2
        self.volk = volk
