#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Face Object

'''

import random

from sfglobals import C


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
        self.klasse_gewaehlt = False

    def __color_offset(item_id):
        '''
            get color offset
        '''
        if self.get_char_image_bound(11) and item_id:
            return self.color * 100
        return 0

    def randomize_character(self, param_obj):
        '''
            get random character
        '''
        self.volk = int(random.random() * 8) + 1
        self.male = random.random() > 0.5

        if param_obj["playerclass"]:
            self.cclass = int(param_obj["playerclass"])
            if self.cclass < 1:
                self.cclass = 1
            if self.cclass > 3:
                self.cclass = 3
            self.klasse_gewaehlt = True
        else:
            self.cclass = int(random.random() * 3) + 1
            self.klasse_gewaehlt = False

        self.randomize_char_image()

    def randomize_char_image(self):
        '''
            get random character image
        '''
        self.color = int(random.random() * self.get_char_image_bound(10) + 1)
        self.mouth = int(random.random() * self.get_char_image_bound(1) + 1)
        self.beard = int(random.random() * self.get_char_image_bound(2) + 1
                         + ColorOffset(C['BEARD']))
        self.nose = int(random.random() * self.get_char_image_bound(3) + 1)
        self.eyes = int(random.random() * self.get_char_image_bound(4) + 1)
        self.brows = int(random.random() * get_char_image_bound(5) + 1
                         + ColorOffset(C['BROWS'])
        self.ears = int(random.random() * get_char_image_bound(6) + 1)
        self.hair = int(random.random() * get_char_image_bound(7) + 1
                        + ColorOffset(C_HAIR))
        self.special = int(random.random() * get_char_image_bound(8) + 1)
        self.special2 = int(random.random() * get_char_image_bound(9) + 1
                            + ColorOffset(C_SPECIAL2))

        # load_character_image()

    def get_char_image_bound(self, item_index):
        '''
            lookup image boundary?
        '''
        lookup = {
            True: {
                1: [None, 9, 13, 6, 7, 7, 5, 11, 17, 0, 5,
                    (C['BROWS'] + C['HAIR'] + C['BEARD'])],
                2: [None, 8, 7, 7, 8, 5, 4, 10, 13, 0, 3,
                    (C['BROWS'] + C['HAIR'] + C['BEARD'])],
                3: [None, 5, 5, 5, 8, 5, 10, 13, 0, 5,
                    (C['BROWS'] + C['HAIR'] + C['BEARD'])],
                4: [None, 10, 12, 6, 9, 6, 12, 17, 0, 5,
                    (C['BROWS'] + C['HAIR'] + C['BEARD'])],
                5: [None, 7, 5, 5, 6, 5, 5, 10, 9, 0, 5,
                    (C['HAIR'] + C['BEARD'])],
                6: [None, 6, 6, 5, 5, 5, 5, 8, 12, 0, 3,
                    (C['BROWS'] + C['HAIR'] + C['BEARD'])],
                7: [None, 6, 8, 5, 9, 6, 5, 12, 12, 0, 0, 0],
                8: [None, 9, 10, 6, 7, 5, 5, 0, 17, 11, 5,
                    (C['BEARD'] + C['SPECIAL2'])],
            },
            False: {
                1: [None, 8, 0, 6, 6, 6, 6, 8, 5, 0, 4],
                2: [None, 8, 0, 8, 7, 8, 7, 8, 5, 0, 4],
                3: [None, 9, 0, 6, 6, 8, 4, 8, 4, 0, 4],
                4: [None, 7, 0, 7, 6, 6, 6, 8, 5, 0, 4,
                    (C['HAIR'] + C['BROWS'])],
                5: [None, 7, 0, 5, 6, 5, 4, 8, 7, 0, 4, C['HAIR']],
                6: [None, 9, 0, 6, 6, 6, 3, 6, 5, 0, 3, C['HAIR']],
                7: [None, 9, 0, 5, 6, 5, 4, 8, 4, 0, 4, C['HAIR']],
                8: [None, 8, 5, 7, 6, 5, 4, 7, 6, 4, 3, C['HAIR']],
            }
        }

        try:
            if lookup[self.male][self.volk][item_index] is not None:
                return lookup[self.male][self.volk][item_index]
            else:
                return 0
        except IndexError:
            return 0
