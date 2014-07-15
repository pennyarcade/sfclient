#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Quest Object

'''

from legacy.sfglobals import SG
from legacy.sfglobals import TXT
from legacy.sfglobals import LBL

from classes.sfswitch import Switch


class Quest(object):
    '''
        harndle qurest data
    '''
    def __init__(self, qtype, qid, qlevel, qmonster,
                 qexp, qgold, qtime, qlocation, qitem, texts):
        '''
            Setup Quest object
        '''

        # set members directly
        self.qtype = qtype
        self.qid = qid
        self.qlevel = qlevel
        self.qmonster = qmonster
        self.qtime = qtime
        self.qitem = qitem
        self.qexp = qexp
        self.qgold = qgold
        self.qlocation = qlocation

        self.qtitle = ''
        self.qtext = ''

        # set derived members
        self.get_title(texts)
        self.get_text(texts)

    def __get_offs(self):
        '''
            get texts offset
        '''
        qst = TXT['QUEST']
        offs = qst['SCOUT']['TITLE']

        for case in Switch(self.qtype):
            if case(1):
                offs = qst['SCOUT']['TITLE'] + self.get_random(20, 0)
                break
            if case(2):
                offs = qst['COLLECT']['TITLE'] + self.get_random(20, 0)
                break
            if case(3):
                offs = qst['FETCH']['TITLE'] + self.get_random(20, 0)
            if case(4):
                offs = qst['KILL']['TITLE'] - self.qmonster - 1
                break
            if case(5):
                offs = qst['TRANSPORT']['TITLE'] + self.get_random(21, 0)
                break
            if case(6):
                offs = qst['ESCORT']['TITLE'] + self.get_random(23, 0)
                break

        return offs

    def from_sg(self, qid, save):
        '''
            setup Quest object from savegame
        '''
        # Constants
        sg_idx = SG['QUEST']['OFFER']

        # set members directly from savegame
        qtype = int(save[sg_idx['TYPE1'] + qid])
        qlevel = int(save[sg_idx['LEVEL1'] + qid])
        qmonster = int(save[sg_idx['enemy1'] + qid])
        qexp = int(save[sg_idx['EXP1'] + qid])
        qgold = int(save[sg_idx['GOLD1'] + qid])
        qtime = int(save[sg_idx['DURATION1'] + qid])
        qlocation = int(save[sg_idx['LOCATION1'] + qid])
        qitem = int(save[sg_idx['REWARD_ITM1'] + qid])

        return self.__init__(
            qtype, qid, qlevel, qmonster, qexp,
            qgold, qtime, qlocation, qitem
        )

    def get_title(self, texts):
        '''
            gets quest title snippet

            @return string
        '''
        # check for cached value
        if not self.qtitle:
            if texts[self.__get_offs()]:
                self.qtitle = texts[self.__get_offs()]

            # Error msg if no quest title found
            # return 'ERR QID=%d QT=%d OFS=%d' % (
            #     quest_id, quest_type, self.get_offs()
            # )

        return self.qtitle

    def get_text(self, texts):
        '''
            get quest description

            @return str
        '''
        if not self.qtext:
            # Constants
            idx = TXT['QUEST']

            self.qtext = ''.join([
                '\"',
                texts[idx['OPENER'] + self.get_random(10, 3)],
                ' '
            ])

            for case in Switch(self.qid):
                if case(1):
                    self.qtext += ' '.join(
                        texts[idx['LOCATION'] + self.qlocation - 1],
                        texts[
                            idx['SCOUT']['TASK1'] + self.get_random(20, 0)
                        ],
                        texts[
                            idx['SCOUT']['TASK2'] + self.get_random(10, 1)
                        ],
                        ' '
                    )
                    break

                if case(2):
                    self.qtext += ' '.join(
                        texts[
                            idx['COLLECT']['WHAT'] + self.get_random(20, 0)
                        ],
                        texts[idx['LOCATION'] + self.qlocation - 1],
                        texts[
                            idx['COLLECT']['AMOUNT'] + self.get_random(11, 1)
                        ].replace(
                            "%",
                            str(self.get_random(10, 2) + 2)
                        ),
                        ' '
                    )
                    break

                if case(3):
                    self.qtext += ' '.join(
                        texts[
                            idx['FETCH']['WHAT'] + self.get_random(20, 0)
                        ],
                        texts[idx['LOCATION'] + self.qlocation - 1],
                        texts[
                            idx['FETCH']['FROM'] + self.get_random(15, 1)
                        ],
                        texts[
                            idx['FETCH']['PRECLOSER'] + self.get_random(20, 0)
                        ],
                        ' '
                    )
                    break

                if case(4):
                    self.qtext += ' '.join(
                        texts[idx['KILL']['LOCATION'] + self.qlocation - 1],
                        texts[
                            idx['KILL']['WHOM'] - self.qmonster - 1
                        ],
                        texts[
                            idx['KILL']['PRECLOSER'] + self.get_random(10, 1)
                        ],
                        " "
                    )
                    break

                if case(5):
                    self.qtext += ' '.join(
                        texts[
                            idx['TRANSPORT']['WHAT'] + self.get_random(21, 0)
                        ],
                        texts[
                            idx['TRANSPORT']['LOCATION'] + self.qlocation - 1
                        ],
                        texts[
                            idx['TRANSPORT']['PRECLOSER']
                            + self.get_random(10, 1)
                        ],
                        " "
                    )
                    break

                if case():
                    self.qtext += ' '.join(
                        texts[
                            idx['ESCORT']['WHOM'] + self.get_random(23, 0)
                        ],
                        texts[
                            idx['ESCORT']['LOCATION'] + self.qlocation - 1
                        ],
                        texts[
                            idx['ESCORT']['PRECLOSER'] + self.get_random(23, 0)
                        ],
                        " "
                    )

        return self.qtext

    def get_random(self, rrange, rmod):
        '''
            Get quest random number

            @param int rrange
            @param int rmod

            @return int
        '''
        checksum = 0

        if rmod != 1:
            modifier = self.qlevel
        if rmod != 2:
            modifier = self.qtype
        if rmod != 3:
            modifier = self.qmonster

        checksum += modifier
        checksum += self.qlocation
        checksum += self.qtime
        checksum += self.qexp
        checksum += self.qgold
        checksum += self.qitem.typ
        checksum += self.qitem.pic

        return checksum % rrange

    def get_bg(self):
        '''
            Get quest background index

            @return int
        '''
        return LBL['SCR']['QUEST']['BG'][str(self.qlocation)]
