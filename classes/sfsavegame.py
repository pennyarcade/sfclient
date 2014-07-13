#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Savegame handling

'''

from sfglobals import SG
from sfglobals import IMG
from sfglobals import POS
from sfglobals import LBL
from sfglobals import TXT
from sfglobals import ACT
from sfglobals import CNT

from classes.sfmirror import Mirror
from classes.sfface import Face


class Savegame(object):
    '''
        handle savegame data
    '''
    def __init__(self, logger):
        '''
            setup savegame
        '''
        self.mirror = Mirror()
        self.has_mirror = False
        self.can_rob = False
        tower_level = 0

        self.log = logger

    def __get_face(self, savegame):
        '''
            extract face from savegame
        '''
        i = char_hair
        char_color = 0
        while i > 100:
            i -= 100
            char_color += 1

        return Face(
            savegame[SG['FACE']['5']],
            savegame[SG['FACE']['3']],
            savegame[SG['CLASS']],
            char_hair,
            savegame[SG['FACE']['4']],
            savegame[SG['FACE']['7']],
            savegame[SG['FACE']['2']],
            (savegame[SG['GENDER']] == 1),
            savegame[SG['FACE']['1']],
            savegame[SG['FACE']['6']],
            savegame[SG['FACE']['8']],
            savegame[SG['FACE']['9']],
            savegame[SG['RACE']]
        )

    def __get_mirror(self, bin_str):
        '''
            extract mirror status from savegame
        '''
        self.mirror = Mirror()

        self.mirror.pieces = list()
        for i in range(13):
            self.mirror.pieces[i] = bin_str.substr(i + 1, 1) == "1"

        self.has_mirror = bin_str.substr(23, 1) == "1"
        self.can_rob = bin_str.substr(22, 1) == "1"

    def parse(self, str_save_game, fill_face_variables=True, no_spoil=False):
        '''
            parse raw response into Savegame object
        '''
        save_obj = self.__init__()

        # parse into array of (mostly) numbers
        savegame = ("0/" + str_save_game).split("/")

        # TODO: Tower object
        # Extract tower level from mount id
        if not no_spoil:
            self.tower_level = int((savegame[SG['MOUNT']] / 65536))

        savegame[SG['MOUNT']] -= self.tower_level * 65536

        # Extract mirror pieces from gender entry
        bin_str = bin(int(savegame[SG['GENDER']]))

        bin_str.zfill(32)

        # TODO: save in character object
        if bin_str.substr(31) == "1":
            savegame[SG['GENDER']] = 1
        else:
            savegame[SG['GENDER']] = 2

        if (savegame[SG['ALBUM']] - 10000) > content_max:
            savegame[SG['ALBUM']] = content_max + 10000

        for i in range(SG['BACKPACK']['SIZE']):
            expand_item_structure(
                savegame, SG['BACKPACK']['OFFS'] + i * SG['ITM']['SIZE']
            )

        for i in range(SG['INVENTORY']['SIZE']):
            expand_item_structure(
                savegame, (SG['INVENTORY']['OFFS'] + i * SG['ITM']['SIZE'])
            )

        for i in range(6):
            expand_item_structure(
                savegame, SG['SHAKES']['ITEM1'] + i * SG['ITM']['SIZE']
            )
            expand_item_structure(
                savegame, SG['FIDGET']['ITEM1'] + i * SG['ITM']['SIZE']
            )

        for i in range(3):
            expand_item_structure(
                savegame,
                (SG['QUEST']['OFFER']['REWARD_ITM1'] + (i * SG['ITM']['SIZE']))
            )

        debug_info = ""
        for i in range(len(savegame)):
            debug_info += str(i) + "=" + savegame[i] + ", "

        if (last_level != 0) and (int(savegame[SG['LEVEL']]) > last_level):
            level_up = True
            pulse_char = True

        last_level = int(savegame[SG['LEVEL']])

        friend_link = "http://" + server + "/index.php?rec="
        friend_link += savegame[SG['PLAYER']['ID']]

        if len(old_ach) != 0:
            for i in range(8):
                if ach_level(savegame, i) > old_ach[i]:
                    old_ach[i] = -1 * ach_level(savegame, i)
                else:
                    old_ach[i] = ach_level(savegame, i)
        else:
            for i in range(8):
                old_ach[i] = ach_level(savegame, i)

        if (old_album >= 0) and (savegame[SG['ALBUM']] > old_album):
            album_effect = True
        old_album = savegame[SG['ALBUM']]

        if fill_face_variables:
            char_face = self.__get_face(savegame)

        if not no_spoil:
            ppos = POS['IF']['LBL']['GOLDPILZE_X']

            if text_dir == "right":
                actor[IMG['IF']['GOLD']].x = POS['IF']['LBL']['GOLDPILZE_X']

                label = actor[LBL['IF']['GOLD']]
                label.text = str(int(savegame[SG['GOLD']] / 100))
                label.x = ppos - label.text_width - 10
                actor[IMG['IF']['SILBER']].x = label.x - label.width - 10

                label = actor[LBL['IF']['SILBER']]
                if int(savegame[SG['GOLD']] % 100) < 10:
                    label.text = "0"
                else:
                    label.text = ""
                label.text += str(int(savegame[SG['GOLD']] % 100))
                label.x = actor[IMG['IF']['SILBER']].x - label.text_width - 10

                label = actor[LBL['IF']['PILZE']]
                label.text = savegame[SG['MUSH']]
                label.x = ppos - label.text_width - 10

                if texts[TXT['MUSHROOMS']['BOUGHT']]:
                    enable_popup(
                        LBL['IF']['PILZE'],
                        texts[TXT['MUSHROOMS']['BOUGHT']].replace(
                            "%1", savegame[SG['MUSHROOMS']['MAY']['DONATE']]
                        )
                    )
            else:
                label = actor[LBL['IF']['SILBER']]
                if int(savegame[SG['GOLD']] % 100) < 10:
                    label.text = "0"
                else:
                    label.text = ""
                label.text += str(int(savegame[SG['GOLD']] % 100))
                label.x = ppos - label.text_width - 10
                actor[IMG['IF']['GOLD']].x = label.x - 24 - 10

                label = actor[LBL['IF']['GOLD']]
                label.text = str(int(savegame[SG['GOLD']] / 100))
                label.x = actor[IMG['IF']['GOLD']].x - label.text_width - 10

                label = actor[LBL['IF']['PILZE']]
                label.text = savegame[SG['MUSH']]
                label.x = ppos - label.text_width - 10

                if texts[TXT['MUSHROOMS']['BOUGHT']]:
                    enable_popup(
                        LBL['IF']['PILZE'],
                        texts[TXT['MUSHROOMS']['BOUGHT']].replace(
                            "%1", savegame[SG['MUSHROOMS']['MAY']['DONATE']]
                        )
                    )

        add(BNC['IF']['STATS'])
        if int(savegame[SG['SERVER']['TIME']]) > 0:
            server_time.setTime(
                1000 * int(savegame[SG['SERVER']['TIME']]) - 1000 * 60 * 60
            )
            local_time = datetime.now()
            time_calc.start()

        if session_id == "":
            self.log.error(''.join([
                "Fehler: Keine Session ID für PHP-Tunneling vergeben. ",
                "PHP-Tunneling wird deaktiviert."
            ]))
            show_login_screen()
        else:
            self.log.debug("Session ID für PHP Tunneling:" + session_id)

        if int(savegame[SG['GUILD']['INDEX']]) != gilden_id:
            gilden_id = int(savegame[SG['GUILD']['INDEX']])
            if gilden_id != 0:
                send_action(
                    ACT['REQUEST']['GUILD'],
                    savegame[SG['GUILD']['INDEX']]
                )

        sg_idx = SG['UNREAD']['MESSAGES']
        if (int(savegame[sg_idx]) > 0) and (not on_stage(CNT['POST']['LIST'])):
            pulse_post = True

        if int(savegame[SG['LOCKDURATION']]) != 0:
            request_logout()

        if next_pxl < 0:
            next_pxl = abs(next_pxl)

        return save_obj


def expand_item_structure(arr, offset):
    '''
    var typeOriginal:Number;
    var picOriginal:Number;
    var mushOriginal:Number;
    var enchantment;
    var socket;
    var enchantmentPower;
    var socketPower;
    typeOriginal = arr[(offset + SG_ITM_TYP)];
    picOriginal = arr[(offset + SG['ITM']['PIC'])];
    mushOriginal = arr[(offset + SG_ITM_MUSH)];
    enchantment = int((typeOriginal / math.pow(2, 24)));
    socket = (typeOriginal - (enchantment * math.pow(2, 24)));
    socket = (socket / math.pow(2, 16));
    typeOriginal = ((typeOriginal - (enchantment * math.pow(2, 24)))
                    - (socket * math.pow(2, 16)));
    enchantmentPower = int((picOriginal / math.pow(2, 16)));
    picOriginal = (picOriginal - (enchantmentPower * math.pow(2, 16)));
    socketPower = int((mushOriginal / math.pow(2, 16)));
    mushOriginal = (mushOriginal - (socketPower * math.pow(2, 16)));
    arr[(offset + SG_ITM_TYP)] = typeOriginal;
    arr[(offset + SG['ITM']['PIC'])] = picOriginal;
    arr[(offset + SG_ITM_MUSH)] = mushOriginal;
    arr[(offset + SG_ITM_EXT_SOCKET)] = socket;
    arr[(offset + SG_ITM_EXT_ENCHANT)] = enchantment;
    arr[(offset + SG_ITM_EXT_ENCHANT_POWER)] = enchantmentPower;
    arr[(offset + SG_ITM_EXT_SOCKET_POWER)] = socketPower;
    '''
    print arr, offset
