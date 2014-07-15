#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Mirror Object

'''

from legacy.sfglobals import ARROW_MAX
from legacy.sfglobals import ARROW_OFFS
from legacy.sfglobals import SG
from legacy.sfglobals import C
from legacy.sfglobals import IMG
from legacy.sfglobals import ITM_MAX

from legacy.sftextidx import TXT


class Item(object):
    '''
        handle Item data
    '''
    def __init__(self, pic=0, typ=0, cclass=1, gold=0,
                 maxd=0, mind=0, color=0, attr=False, slot_id=0, logger=None):
        '''
            setup Item object

            TODO: documentation
        '''
        self.log = logger

        self.slot_id = slot_id
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

    def __get_attr_offs(self, dom_attr_val):
        '''
            get attr offset
        '''
        attr_val_offs = 0

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

        return attr_val_offs

    def __get_suffix(self, texts):
        '''
            get attr suffix for item name
        '''
        txt_idx = TXT['ITMNAME']

        if self.cclass > 0:
            return ''

        dom_attr_typ = -1
        dom_attr_val = 0

        for i in range(3):
            if self.attr[i]['val'] > dom_attr_val:
                dom_attr_typ = self.attr[i]['typ']
                dom_attr_val = self.attr[i]['val']

        attr_val_code = pow(2, dom_attr_typ - 1)

        attr_val_offs = self.__get_attr_offs(dom_attr_val)

        if attr_val_code > 0:
            return texts[txt_idx['EXT'] + attr_val_code + attr_val_offs]

        return ''

    def from_sg(self, sg_index=0, save=False, logger=None):
        '''
            setup item object from savegame

            @param int sg_index
            @param list save

            @return self
        '''
        # Preset values
        pic = 0
        typ = 0
        cclass = 0
        gold = 0
        color = 0
        mush = 0
        slot_id = 0
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

            while pic >= 1000:
                pic -= 1000
                cclass += 1
            cclass -= 1

            slot_id = cclass + pic * SG['ITM']['SIZE']

        return self.__init__(
            pic, typ, cclass, gold, mush, damage['max'],
            damage['min'], color, attr, slot_id, logger
        )

    def get_name(self, texts):
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

        txt_suffix = self.__get_suffix(texts)

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
            self.log.error(' '.join([
                "Fehler: Zu wenige Indizes für Items:", item_id, ITM_MAX,
                "Typ:", self.typ,
                "Pic:", self.pic,
                "Color:", self.color,
                "Class:", self.cclass
            ]))
            return 0

        if is_sg and (self.typ == 0) and (slot_num > 0) and (slot_num <= 10):
            if slot_num <= 8:
                item_id = IMG['EMPTY']['SLOT']['1'] + slot_num - 1
            else:
                if owner_class == 1:
                    if slot_num == 9:
                        item_id = IMG['EMPTY']['SLOT']['9_1']
                    elif no_shield_flag:
                        item_id = IMG['NO_SHIELD']
                    else:
                        item_id = IMG['EMPTY']['SLOT']['10']
                elif (owner_class == 2) and (slot_num == 9):
                    item_id = IMG['EMPTY']['SLOT']['9_2']
                elif (owner_class == 3) and (slot_num == 9):
                    item_id = IMG['EMPTY']['SLOT']['9_3']

        return item_id

    def get_arrow_id(self, some_obj=False, slot_mode=False,
                     color_override=-1):
        '''
            calculate id for arrow/bolt shots
        '''
        arrow_id = ARROW_OFFS

        color = self.color

        if not slot_mode:
            color = int(some_obj)

        if color_override >= 0:
            color = color_override

        arrow_id += self.cclass * 5 * 100
        arrow_id += self.pic * 5
        arrow_id += color

        if arrow_id >= ARROW_MAX:
            self.log.error(' '.join(
                "Fehler: Zu wenige Indizes für Pfeile:",
                arrow_id,
                ">=",
                ARROW_MAX,
                "Pic:",
                self.pic,
                "Color:",
                color,
                "Class:",
                self.cclass
            ))
            return 0

        return arrow_id


def item_popup(slot_id, sg_index, save=None, hide_back_pack=False,
               no_prices=False, tower_mode=False, witch_mode=False):
    '''
    var attribLines:Array;
    var shopLines:Array;
    var i;
    var ii;
    var iii;
    var goldRaw;
    var gold;
    var silber;
    var pilze;
    var compareIndex;
    var compareVal;
    var compareFound:Boolean;
    var lossFound:Boolean;
    var hours;
    var socket;
    var socketPower;
    var enchant;
    var enchantPower;
    var itm_color:Number;
    var itm_class;
    var itm_pic;
    var attribSum;
    var itmName:String;
    var itmQuote:String;
    var quoteArray:Array;
    tower_mode = on_stage(PREV_COPYCAT);
    attribLines = list();
    shopLines = list();
    if (!(save is Array)){
        save = savegame;
    };
    if (save[(sg_index + SG_ITM_TYP)] > 0){
        ii = 0;
        iii = 0;
        goldRaw = save[(sg_index + SG_ITM_GOLD)];
        if (witch_mode){
            if (save[(sg_index + SG_ITM_TYP)] == witchDesiredType){
                goldRaw = (goldRaw * 2);
            } else {
                goldRaw = 0;
            };
        };
        gold = int((goldRaw / 100));
        silber = int((goldRaw % 100));
        pilze = int((save[(sg_index + SG_ITM_MUSH)] % 100));
        compareIndex = 0;
        compareFound = False;
        lossFound = False;
        socket = int(save[(sg_index + SG_ITM_EXT_SOCKET)]);
        socketPower = int(save[(sg_index + SG_ITM_EXT_SOCKET_POWER)]);
        enchant = int(save[(sg_index + SG_ITM_EXT_ENCHANT)]);
        enchantPower = int(save[(sg_index + SG_ITM_EXT_ENCHANT_POWER)]);
        if (((!(hide_back_pack)) and (!(no_prices)))){
            shopLines[shopLines.length] = FontFormatPopup;
            if (gold > 0){
                if (silber > 0){
                    shopLines[shopLines.length] = [POPUP_BEGIN_LINE, str(gold),
                    actor[IF_GOLD], str(silber), actor[IF_SILBER],
                    POPUP_END_LINE];
                } else {
                    shopLines[shopLines.length] = [POPUP_BEGIN_LINE, str(gold),
                    actor[IF_GOLD], POPUP_END_LINE];
                };
            } else {
                if (silber > 0){
                    shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                    str(silber), actor[IF_SILBER], POPUP_END_LINE];
                };
            };
            if (pilze > 0){
                shopLines[shopLines.length] = [POPUP_BEGIN_LINE, str(pilze),
                actor[IF_PILZE], POPUP_END_LINE];
            };
            if (witch_mode){
                if (save[(sg_index + SG_ITM_TYP)] != witchDesiredType){
                    shopLines.append([POPUP_BEGIN_LINE,
                    texts[TXT_WITCH_WRONGTYPE], POPUP_END_LINE]);
                };
            } else {
                if ((((((pilze + gold) + silber) == 0))
                    and ((save[(sg_index + SG_ITM_TYP)] <= 10)))){
                    shopLines.append([POPUP_BEGIN_LINE,
                                     texts[TXT_TOILET_ITEM], POPUP_END_LINE]);
                };
            };
        };
        itm_color = 0;
        itm_class = 0;
        itm_pic = int(save[(sg_index + SG['ITM']['PIC'])]);
        i = 0;
        while (i < 8) {
            itm_color = (itm_color + Number(save[((sg_index
                         + SG['ITM']['SCHADEN_MIN']) + i)]));
            i++;
        };
        itm_color = (itm_color % 5);
        while (itm_pic >= 1000) {
            itm_pic = (itm_pic - 1000);
            itm_class++;
        };
        if (C_DISPLAY_ITEM_INFO){
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                actorURL[GetItemID(sg_index, 0, save)], POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "Typ: ", POPUP_TAB, str(save[(sg_index + SG_ITM_TYP)]),
                POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "Pic: ", POPUP_TAB, str(itm_pic), POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "Color: ", POPUP_TAB, str((itm_color + 1)), POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "Class: ", POPUP_TAB, str((itm_class + 1)), POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "Sock: ", POPUP_TAB, str(socket), POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "SockPwr: ", POPUP_TAB, str(socketPower), POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "Enchant: ", POPUP_TAB, str(enchant), POPUP_END_LINE];
            shopLines[shopLines.length] = [POPUP_BEGIN_LINE,
                "EnchantPwr: ", POPUP_TAB, str(enchantPower), POPUP_END_LINE];
        };
        i = 0;
        while (i < 10) {
            suggestion_slot[slot_id] = 0;
            if (int(save[(sg_index + SG_ITM_TYP)]) == CorrectItemType[i]){
                if ((((slot_id >= CHAR_SLOT_11))
                        and ((slot_id <= CHAR_SLOT_SHAKES_6)))){
                    suggestion_slot[slot_id] = (i + CHAR_SLOT_1);
                    if (save[((SG_INVENTORY_OFFS + (SG['ITM']['SIZE'] * i))
                            + SG_ITM_TYP)] > 0){
                        if (((compare_items) and (!(tower_mode)))){
                            compareIndex = (SG_INVENTORY_OFFS
                                            + (SG['ITM']['SIZE'] * i));
                        };
                    };
                };
                break;
            };
            i++;
        };
        attribSum = 0;
        i = 0;
        while (i < 3) {
            if ((((int(save[((sg_index + SG_ITM_ATTRIBTYP1) + i)]) > 0))
                    and ((int(save[((sg_index + SG_ITM_ATTRIBVAL1) + i)]) > 0){
                var _temp1 = ii;
                ii = (ii + 1);
                var _local33 = _temp1;
                attribLines[_local33] = POPUP_BEGIN_LINE;
                if (int(save[((sg_index + SG_ITM_ATTRIBTYP1) + i)]) <= 6){
                    var _temp2 = ii;
                    ii = (ii + 1);
                    var _local34 = _temp2;
                    attribLines[_local34] = FontFormatPopup;
                } else {
                    var _temp3 = ii;
                    ii = (ii + 1);
                    _local34 = _temp3;
                    attribLines[_local34] = FontFormatPopup;
                };
                var _temp4 = ii;
                ii = (ii + 1);
                _local34 = _temp4;
                attribLines[_local34] = texts[(TXT_ITEM_ATTRIB_CLASSES
                           + int(save[((sg_index + SG_ITM_ATTRIBTYP1) + i)]))];
                var _temp5 = ii;
                ii = (ii + 1);
                var _local35 = _temp5;
                attribLines[_local35] = (POPUP_TAB + POPUP_TAB_ADD);
                if (int(save[((sg_index + SG_ITM_ATTRIBTYP1) + i)]) == 11){
                    hours = int(save[((sg_index + SG_ITM_ATTRIBVAL1) + i)]);
                    var _temp6 = ii;
                    ii = (ii + 1);
                    var _local36 = _temp6;
                    attribLines[_local36] = (((int((hours / 24)))>0)
                        ? (((str(int((hours / 24))) + " ")
                           + texts[(((int((hours / 24)) == 1))
                            ? TXT_DAY : TXT_DAYS)]) + ((((hours % 24) > 0))
                            ? ", " : "")) : "" + ((((hours % 24) > 0))
                            ? ((str((hours % 24)) + " ")
                           + texts[((((hours % 24) == 1))
                                    ? TXT_HOUR : TXT_HOURS)]) : ""));
                } else {
                    if (int(save[((sg_index + SG_ITM_ATTRIBTYP1) + i)]) == 12){
                        var _temp7 = ii;
                        ii = (ii + 1);
                        _local36 = _temp7;
                        attribLines[_local36] = POPUP_TAB;
                        var _temp8 = ii;
                        ii = (ii + 1);
                        var _local37 = _temp8;
                        attribLines[_local37] = (("+ " + save[((sg_index
                                 + SG_ITM_ATTRIBVAL1) + i)]) + "%");
                    } else {
                        if (save[(sg_index + SG_ITM_TYP)] == 12){
                            var _temp9 = ii;
                            ii = (ii + 1);
                            _local36 = _temp9;
                            attribLines[_local36] = POPUP_TAB;
                            if (save[((sg_index + SG_ITM_ATTRIBVAL1) + i)
                                    ] <= 25){
                                var _temp10 = ii;
                                ii = (ii + 1);
                                _local37 = _temp10;
                                attribLines[_local37] = (("+ "
                                   + save[sg_index + SG_ITM_ATTRIBVAL1 + i])
                                    + "%");
                            } else {
                                var _temp11 = ii;
                                ii = (ii + 1);
                                _local37 = _temp11;
                                attribLines[_local37] = ("+ "
                                 + save[((sg_index + SG_ITM_ATTRIBVAL1) + i)]);
                            };
                        } else {
                            var _temp12 = ii;
                            ii = (ii + 1);
                            _local36 = _temp12;
                            attribLines[_local36] =
                                save[((sg_index + SG_ITM_ATTRIBVAL1) + i)];
                        };
                    };
                };
                if (compareIndex > 0){
                    compareFound = False;
                    iii = 0;
                    while (iii < 3) {
                        if ((((((int(save[((compareIndex + SG_ITM_ATTRIBTYP1)
                                + iii)]) == int(save[((sg_index
                                 + SG_ITM_ATTRIBTYP1) + i)])))
                                and ((int(save[((compareIndex
                                     + SG_ITM_ATTRIBVAL1) + iii)]) > 0))))
                                and ((int(save[((sg_index + SG_ITM_ATTRIBVAL1)
                                     + i)]) > 0)))){
                            compareVal = (int(save[((sg_index
                                          + SG_ITM_ATTRIBVAL1) + i)])
                                    - int(save[((compareIndex +
                                     SG_ITM_ATTRIBVAL1) + iii)]));
                            if (int(save[((compareIndex + SG_ITM_ATTRIBTYP1)
                                + iii)]) == 6){
                                compareVal = (compareVal * 5);
                            };
                            attribSum = (attribSum + compareVal);
                            var _temp13 = ii;
                            ii = (ii + 1);
                            _local36 = _temp13;
                            attribLines[_local36] = (((compareVal == 0))
                                 ? FontFormatPopup : (((compareVal > 0))
                               ? FontFormatPopupCompareBetter
                               : FontFormatPopupCompareWorse));
                            var _temp14 = ii;
                            ii = (ii + 1);
                            _local37 = _temp14;
                            attribLines[_local37] = COMPARE_TAB;
                            var _temp15 = ii;
                            ii = (ii + 1);
                            var _local38 = _temp15;
                            attribLines[_local38] = (((compareVal >= 0))
                                 ? (((compareVal == 0)) ? "+-" : "+") : "-");
                            var _temp16 = ii;
                            ii = (ii + 1);
                            var _local39 = _temp16;
                            attribLines[_local39] = str(math.abs(compareVal));
                            var _temp17 = ii;
                            ii = (ii + 1);
                            var _local40 = _temp17;
                            attribLines[_local40] = FontFormatPopup;
                            compareFound = True;
                            break;
                        };
                        iii++;
                    };
                    if (!compareFound){
                        var _temp18 = ii;
                        ii = (ii + 1);
                        _local36 = _temp18;
                        attribLines[_local36] = FontFormatPopupCompareBetter;
                        var _temp19 = ii;
                        ii = (ii + 1);
                        _local37 = _temp19;
                        attribLines[_local37] = COMPARE_TAB;
                        var _temp20 = ii;
                        ii = (ii + 1);
                        _local38 = _temp20;
                        attribLines[_local38] = "+";
                        var _temp21 = ii;
                        ii = (ii + 1);
                        _local39 = _temp21;
                        attribLines[_local39] = str((save[((sg_index
                            + SG_ITM_ATTRIBVAL1) + i)]
                            * (((save[((sg_index + SG_ITM_ATTRIBTYP1) + i)]
                               == 6)) ? 5 : 1)));
                        var _temp22 = ii;
                        ii = (ii + 1);
                        _local40 = _temp22;
                        attribLines[_local40] = FontFormatPopup;
                        attribSum = (attribSum + (save[((sg_index
                             + SG_ITM_ATTRIBVAL1) + i)] * (((save[((sg_index
                             + SG_ITM_ATTRIBTYP1) + i)] == 6)) ? 5 : 1)));
                    };
                };
                var _temp23 = ii;
                ii = (ii + 1);
                _local36 = _temp23;
                attribLines[_local36] = POPUP_END_LINE;
            };
            if ((((((compareIndex > 0)) and ((int(save[((compareIndex
                + SG_ITM_ATTRIBTYP1) + i)]) > 0))))
                and ((int(save[((compareIndex + SG_ITM_ATTRIBVAL1) + i)])
                     > 0)))){
                lossFound = False;
                iii = 0;
                while (iii < 3) {
                    if ((((((int(save[compareIndex + SG_ITM_ATTRIBTYP1 + i])
                        == int(save[((sg_index + SG_ITM_ATTRIBTYP1) + iii)])))
                         and ((int(save[((compareIndex + SG_ITM_ATTRIBVAL1)
                              + i)]) > 0)))) and
                            ((int(save[((sg_index + SG_ITM_ATTRIBVAL1)
                             + iii)]) > 0)))){
                        lossFound = True;
                        break;
                    };
                    iii++;
                };
                if (!lossFound){
                    var _temp24 = ii;
                    ii = (ii + 1);
                    _local33 = _temp24;
                    attribLines[_local33] = POPUP_BEGIN_LINE;
                    var _temp25 = ii;
                    ii = (ii + 1);
                    _local34 = _temp25;
                    attribLines[_local34] = texts[(TXT_ITEM_ATTRIB_CLASSES
                       + int(save[((compareIndex + SG_ITM_ATTRIBTYP1) + i)]))];
                    var _temp26 = ii;
                    ii = (ii + 1);
                    _local35 = _temp26;
                    attribLines[_local35] = (POPUP_TAB + POPUP_TAB_ADD);
                    var _temp27 = ii;
                    ii = (ii + 1);
                    _local36 = _temp27;
                    attribLines[_local36] = "-";
                    var _temp28 = ii;
                    ii = (ii + 1);
                    _local37 = _temp28;
                    attribLines[_local37] = FontFormatPopupCompareWorse;
                    var _temp29 = ii;
                    ii = (ii + 1);
                    _local38 = _temp29;
                    attribLines[_local38] = COMPARE_TAB;
                    var _temp30 = ii;
                    ii = (ii + 1);
                    _local39 = _temp30;
                    attribLines[_local39] = "-";
                    var _temp31 = ii;
                    ii = (ii + 1);
                    _local40 = _temp31;
                    attribLines[_local40] = str((save[((compareIndex
                                                + SG_ITM_ATTRIBVAL1) + i)]
                                * (((save[((compareIndex + SG_ITM_ATTRIBTYP1)
                                   + i)] == 6)) ? 5 : 1)));
                    var _temp32 = ii;
                    ii = (ii + 1);
                    var _local41 = _temp32;
                    attribLines[_local41] = FontFormatPopup;
                    var _temp33 = ii;
                    ii = (ii + 1);
                    var _local42 = _temp33;
                    attribLines[_local42] = POPUP_END_LINE;
                    attribSum = (attribSum - (save[((compareIndex
                                 + SG_ITM_ATTRIBVAL1) + i)]
                        * (((save[((compareIndex + SG_ITM_ATTRIBTYP1) + i)]
                           == 6)) ? 5 : 1)));
                };
            };
            i++;
        };
        itmName = GetItemName(sg_index, save);
        itmQuote = "";
        quoteArray = list();
        if (itmName.find("|") > 0){
            itmQuote = itmName.split("|")[1];
            itmName = itmName.split("|")[0];
            quoteArray[0] = POPUP_BEGIN_LINE;
            quoteArray[1] = ((save[(sg_index + SG_ITM_TYP)])==14)
                ? FontFormatItemEnchantment : FontFormatEpicItemQuote;
            quoteArray[2] = itmQuote;
            quoteArray[3] = FontFormatPopup;
            quoteArray[4] = POPUP_END_LINE;
        };
        if (save[(sg_index + SG_ITM_TYP)] < 8){
            if ((itm_class + 1) != ((tower_mode)
                ? (copyCatSel + 1) : savegame[SG_CLASS])){
                quoteArray.append(POPUP_BEGIN_LINE);
                quoteArray.append(FontFormatError);
                quoteArray.append(texts[TXT_NECESSARY_CLASS].split("%1")
                      .join(texts[((TXT_NECESSARY_CLASS + itm_class) + 1)]));
                quoteArray.append(FontFormatPopup);
                quoteArray.append(POPUP_END_LINE);
            };
        };
        if (save[(sg_index + SG_ITM_EXT_ENCHANT)] > 0){
            if (save[(sg_index + SG_ITM_TYP)] == 14){
                itmName = texts[TXT_SCROLL_NAME].split("%1").join(itmName);
            } else {
                quoteArray.append(POPUP_BEGIN_LINE);
                quoteArray.append(FontFormatItemEnchantment);
                quoteArray.append(texts[TXT_ENCHANT_HINT]);
                quoteArray.append((POPUP_TAB + POPUP_TAB_ADD));
                quoteArray.append(texts[((TXT_ITMNAME_14
                 + int(save[(sg_index + SG_ITM_EXT_ENCHANT)])) - 1)]
                    .split("|")[0]);
                quoteArray.append(FontFormatPopup);
                quoteArray.append(POPUP_END_LINE);
            };
            quoteArray.append(POPUP_BEGIN_LINE);
            quoteArray.append(FontFormatItemEnchantment);
            quoteArray.append(texts[((TXT_ENCHANT_NAMES + int(save[(sg_index
                              + SG_ITM_EXT_ENCHANT)])) - 1)]);
            quoteArray.append((POPUP_TAB + POPUP_TAB_ADD));
            quoteArray.append(texts[((TXT_ENCHANT_VALUES + int(save[(sg_index
                              + SG_ITM_EXT_ENCHANT)])) - 1)].split("%1")
                    .join(str(save[(sg_index + SG_ITM_EXT_ENCHANT_POWER)])));
            quoteArray.append(FontFormatPopup);
            quoteArray.append(POPUP_END_LINE);
        };
        if (int(save[(sg_index + SG_ITM_TYP)]) == 1){
            if (compareIndex > 0){
                compareVal = (math.round(((Number(save[(sg_index
                    + SG['ITM']['SCHADEN_MIN'])])
                    + Number(save[(sg_index + SG_ITM_SCHADEN_MAX)])) / 2))
                    - math.round(((Number(save[(compareIndex
                    + SG['ITM']['SCHADEN_MIN'])]) +
                    Number(save[(compareIndex + SG_ITM_SCHADEN_MAX)])) / 2)));
                enable_popup(slot_id, itmName, quoteArray, POPUP_BEGIN_LINE,
                             texts[TXT_SCHADEN], (POPUP_TAB + POPUP_TAB_ADD),
                             (save[sg_index + SG['ITM']['SCHADEN_MIN']] + "-")
                              + save[(sg_index + SG_ITM_SCHADEN_MAX)]),
                            (("(~" + str(math.round(((Number(save[(sg_index
                             + SG['ITM']['SCHADEN_MIN'])])
                            + Number(save[(sg_index + SG_ITM_SCHADEN_MAX)]))
                            / 2)))) + ")"), (((compareVal == 0))
                            ? FontFormatPopup : (((compareVal > 0))
                            ? FontFormatPopupCompareBetter
                            : FontFormatPopupCompareWorse)), COMPARE_TAB,
                            ((((compareVal >= 0)) ? (((compareVal == 0))
                             ? "+- " : "+ ") : "- ")
                            + str(math.abs(compareVal))), FontFormatPopup,
                            POPUP_END_LINE, attribLines, shopLines);
            } else {
                enable_popup(slot_id, itmName, quoteArray, POPUP_BEGIN_LINE,
                             texts[TXT_SCHADEN], (POPUP_TAB + POPUP_TAB_ADD),
                             ((save[sg_index + SG['ITM']['SCHADEN_MIN']] + "-"
                              + save[(sg_index + SG_ITM_SCHADEN_MAX)]),
                            (("(~" + str(math.round(((Number(save[(sg_index
                             + SG['ITM']['SCHADEN_MIN'])])
                            + Number(save[(sg_index + SG_ITM_SCHADEN_MAX)]))
                            / 2)))) + ")"), POPUP_END_LINE,
                            attribLines, shopLines);
            };
        } else {
            if (int(save[(sg_index + SG_ITM_TYP)]) == 2){
                if (compareIndex > 0){
                    compareVal = int(save[sg_index
                                + SG['ITM']['SCHADEN_MIN']])
                                  - int(save[(compareIndex
                                        + SG['ITM']['SCHADEN_MIN'])]));
                    enable_popup(slot_id, itmName, quoteArray,
                                 POPUP_BEGIN_LINE, texts[TXT_BLOCKEN],
                                 (POPUP_TAB + POPUP_TAB_ADD),
                                 (save[(sg_index + SG['ITM']['SCHADEN_MIN'])]
                                  + " %"),
                                 (((compareVal == 0))
                                  ? FontFormatPopup
                                  : (((compareVal > 0))
                                     ? FontFormatPopupCompareBetter
                                     : FontFormatPopupCompareWorse)),
                                 COMPARE_TAB,
                                 ((((compareVal >= 0))
                                    ? (((compareVal == 0))
                                       ? "+- " : "+ ") : "- ")
                                    + str(math.abs(compareVal))),
                                    FontFormatPopup, POPUP_END_LINE,
                                    attribLines, shopLines);
                } else {
                    enable_popup(slot_id, itmName, quoteArray,
                                 POPUP_BEGIN_LINE, texts[TXT_BLOCKEN],
                                 (POPUP_TAB + POPUP_TAB_ADD),
                                 (save[(sg_index + SG['ITM']['SCHADEN_MIN'])]
                                  + " %"), POPUP_END_LINE, attribLines,
                                shopLines);
                };
            } else {
                if (int(save[(sg_index + SG['ITM']['SCHADEN_MIN'])]) > 0){
                    if (compareIndex > 0){
                        compareVal = (int(save[(sg_index
                                  + SG['ITM']['SCHADEN_MIN'])])
                                - int(save[(compareIndex
                                      + SG['ITM']['SCHADEN_MIN'])]));
                        enable_popup(slot_id, itmName, quoteArray,
                                     POPUP_BEGIN_LINE, texts[TXT_RUESTUNG],
                                     (POPUP_TAB + POPUP_TAB_ADD),
                                     save[sg_index
                                     + SG['ITM']['SCHADEN_MIN']],
                                     (((compareVal == 0))
                                      ? FontFormatPopup : (((compareVal > 0))
                                      ? FontFormatPopupCompareBetter
                                      : FontFormatPopupCompareWorse)),
                                    COMPARE_TAB,
                                    ((((compareVal >= 0))
                                     ? (((compareVal == 0))
                                        ? "+- " : "+ ") : "- ")
                                        + str(math.abs(compareVal))),
                                        FontFormatPopup, POPUP_END_LINE,
                                        attribLines, shopLines);
                    } else {
                        enable_popup(slot_id, itmName, quoteArray,
                                     POPUP_BEGIN_LINE, texts[TXT_RUESTUNG],
                                     (POPUP_TAB + POPUP_TAB_ADD),
                                     save[(sg_index
                                        + SG['ITM']['SCHADEN_MIN'])],
                                     POPUP_END_LINE, attribLines, shopLines);
                    };
                } else {
                    enable_popup(slot_id, itmName, quoteArray, attribLines,
                                 shopLines);
                };
            };
        };
    } else {
        enable_popup(slot_id);
    };
    '''
    print slot_id, sg_index, save, hide_back_pack, no_prices, tower_mode
    print witch_mode
