#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Mirror Object

'''

class Item(object):
    '''
        handle Item data
    '''
    def __init__(self, pic=0, typ=0, cclass=1, gold=0,
                 maxd=0, mind=0, color=0, attr=False):
        '''
            setup Item object

            TODO: documentation
        '''
        self.pic = pic
        self.typ = typ
        self.cclass = cclass
        self.gold = gold
        self.color = color
        self.damage = {
            'min': mind,
            'max': maxd
        }
        if type(attr) is list:
            self.attr = attr
        else:
            self.attr = [
                {'typ': 0, 'val': 0},
                {'typ': 0, 'val': 0},
                {'typ': 0, 'val': 0}
            ]
        while self.pic >= 1000:
            self.pic -= 1000
            self.cclass += 1

    def from_sg(self, sg_index=0, save=False):
        '''
            setup item object from savegame

            @param int sg_index
            @param list save

            @return self
        '''
        # Preset values
        pic = 0
        typ = 0
        cclass = 1
        gold = 0
        color = 0
        mush = 0
        damage = {'max': 0, 'min': 0}
        attr = [
            {'typ': 0, 'val': 0},
            {'typ': 0, 'val': 0},
            {'typ': 0, 'val': 0}
        ]

        if type(save) is list:
            pic = int(save[sg_index + SG['ITM']['PIC']])
            typ = int(save[sg_index + SG['ITM']['TYP']])

            gold = int(save[sg_index + SG['ITM']['GOLD']])
            mush = int(save[sg_index + SG['ITM']['MUSH']])
            damage['max'] = int(save[sg_index + SG['ITM']['SCHADEN_MAX']])
            damage['min'] = int(save[sg_index + SG['ITM']['SCHADEN_MIN']])

            for i in range(3):
                attr[i]['typ'] = save[sg_index + SG['ITM']['ATTRIBTYP1'] + i]
                attr[i]['val'] = save[sg_index + SG['ITM']['ATTRIBVAL1'] + i]

            for i in range(8):
                color += int(save[sg_index + SG['ITM']['SCHADEN_MIN'] + i])

            color = color % 5

        return self.__init__(
            pic, typ, cclass, gold, mush, damage['max'],
            damage['min'], color, attr
        )

    def get_name(self):
        '''
            get item name snippet

            @param int sg_index index of item in savegame
            @param list SG savegame
            @param int albumMode

            @return str

            @oldname GetItemName
        '''

        txt_idx = TXT['ITMNAME']
        txt_base = 0
        txt_suffix = ""

        if self.cclass <= 0:
            dom_attr_typ = -1
            dom_attr_val = 0
            attr_val_code = 0
            attr_val_offs = 0

            attrim_in = list()
            for i in range(10):
                attrim_in[i] = False

            for i in range(3):
                if self.attr[i]['val'] > dom_attr_val:
                    dom_attr_typ = self.attr[i]['typ']
                    dom_attr_val = self.attr[i]['val']
                if (self.attr[i]['typ'] > 0) and (self.attr[i]['val'] > 0):
                    attrim_in[self.attr[i]['typ'] - 1] = True

            attr_val_code = pow(2, dom_attr_typ - 1)

            if dom_attr_val >= 25:
                attr_val_offs = 250
            elif dom_attr_val >= 16:
                attr_val_offs = 200
            elif dom_attr_val >= 11:
                attr_val_offs = 150
            elif dom_attr_val >= 6:
                attr_val_offs = 100
            elif dom_attr_val >= 3:
                attr_val_offs = 50

            if attr_val_code > 0:
                txt_suffix = texts[
                    txt_idx['EXT'] + attr_val_code + attr_val_offs
                ]

        if self.typ >= 8:
            txt_base = txt_idx[str(self.typ)]
        else:
            txt_base = txt_idx[str(self.typ)][str(self.cclass)]

        if (self.pic >= 50) and (self.typ != 14):
            txt_base += txt_idx['1']['1']['EPIC'] - txt_idx['1']['1']
            self.pic -= 49
            txt_suffix = ""

        if texts[txt_base + self.pic - 1] is None:
            return "Unknown Item (base=%d, entry=%d)" % (
                txt_base, (txt_base + self.pic - 1)
            )

        if texts[txt_idx['EXT']] == "1":
            result = ""
            if txt_suffix != "":
                result = texts[txt_base + self.pic - 1]
            return result

        if texts[txt_idx['EXT']] == "2":
            result = txt_suffix.replace("%1", texts[txt_base + self.pic - 1])
            if txt_suffix == "":
                result = texts[txt_base + self.pic - 1]
            return result

        result = texts[txt_base + self.pic - 1] + " " + txt_suffix
        if txt_suffix == "":
            result = texts[txt_base + self.pic - 1]
        return result

    def get_file(self, itm_color):
        '''
            get item graphic relative url

            @oldname GetItemFile
            @param int itm_color
            @return str

            TODO: itm_color ???
        '''
        item_file = "itm"

        if (self.pic >= 50) and (self.typ != 14):
            itm_color = 0

        item_file += str(self.typ) + "-" + str(self.pic)

        if self.typ in range(1, 8):
            item_file = str(self.typ) + "-" + str(self.cclass + 1) + "/"
            item_file += item_file + "-" + str(itm_color + 1)
            item_file += "-" + str(self.cclass + 1)
        else:
            if self.typ in range(8, 15):
                item_file = str(self.typ) + "-1/" + item_file + "-"
                if self.typ < 10:
                    item_file += str(self.color + 1) + "-"

                item_file += "1"

        return "res/gfx/itm/" + item_file + ".png"

    def get_id(self):
        '''
            get item ID

            @return int
            @oldname GetItemID

        '''
        item_id = SG['ITM']['OFFS']
        slot_num = 0
        owner_class = 0
        is_sg = False
        no_shield_flag = False

        if self.cclass < 0:
            slot_id = self.typ + self.pic * SG['ITM']['SIZE']
            slot_num = self.pic + 1

            if self.cclass == -2:
                is_sg = True
            elif self.cclass <= -3:
                owner_class = -1 * self.cclass - 2
                no_shield_flag = True
                is_sg = True

        item_id += self.typ * C['ITEMS_PER_TYPE'] * 5 * 3
        item_id += self.pic * 5 * 3
        item_id += self.color * 3
        item_id += self.cclass

        if item_id >= SG['ITM']['MAX']:
            # FIXME
            # LOG.error("Fehler: Zu wenige Indizes für Items:", item_id,
            # ITM_MAX, "Typ:", itmTyp, "Pic:", itm_pic, "Color:",
            # itm_color, "Class:", itm_class)
            return 0

        if is_sg and (self.typ == 0) and (slot_num > 0) and (slot_num <= 10):
            if slot_num <= 8:
                item_id = IMG['EMPTY']['SLOT']['1'] + slot_num - 1
            else:
                if owner_class == 1:
                    if slot_num == 9:
                        item_id = IMG['EMPTY']['SLOT']['9_1']
                    else:
                        if no_shield_flag:
                            item_id = IMG['NO_SHIELD']
                        else:
                            item_id = IMG['EMPTY']['SLOT']['10']
                elif owner_class == 2:
                    if slot_num == 9:
                        item_id = IMG['EMPTY']['SLOT']['9_2']
                elif owner_class == 3:
                    if slot_num == 9:
                        item_id = IMG['EMPTY']['SLOT']['9_3']

        return item_id


def get_arrow_id(itm_class, itm_pic, some_obj=False, slot_mode=False,
                 color_override=-1):
    '''
        calculate id for arrow/bolt shots
    '''
    arrow_id = ARROW_OFFS
    if slot_mode:
        if not type(some_obj) is list:
            some_obj = savegame

        slot_id = itm_class + itm_pic * SG['ITM']['SIZE']
        itm_pic = some_obj[slot_id + SG['ITM']['PIC']]
        itm_color = 0

        for i in range(8):
            itm_color += int(some_obj[slot_id + SG['ITM']['SCHADEN_MIN'] + i])

        itm_color = itm_color % 5

        itm_class = 0
        while itm_pic >= 1000:
            itm_pic -= 1000
            itm_class += 1
        itm_class -= 1
    else:
        itm_color = int(some_obj)

    if color_override >= 0:
        itm_color = color_override

    arrow_id += itm_class * 5 * 100
    arrow_id += itm_pic * 5
    arrow_id += arrow_id + itm_color

    if arrow_id >= ARROW_MAX:
        LOG.error(' '.join(
            "Fehler: Zu wenige Indizes für Pfeile:",
            arrow_id,
            ">=",
            ARROW_MAX,
            "Pic:",
            itm_pic,
            "Color:",
            itm_color,
            "Class:",
            itm_class
        ))
        return 0

    return arrow_id
