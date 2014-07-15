#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Module for obsolete legacy stuff
'''

# from sfglobals import SG


class BaseClass(object):
    '''
        Use to fix unnessessary pylint warnings for legacy stuff
    '''
    def __init__(self, *args):
        '''
            obsolete with cli?
        '''
        self.param1 = 'Foo'
        self.param2 = 'Bar'
        print args

    def getfoo(self):
        '''
          return Foo
        '''
        return self.param1

    def getbar(self):
        '''
          return Bar
        '''
        return self.param2

    def add_event_listener(self, *args):
        '''
            obsolete
        '''
        print args, self.param1


class Actor(BaseClass):
    '''
        Use to fix unnessessary pylint warnings for legacy stuff
    '''
    def __init__(self, *args):
        '''
            obsolete with cli?
        '''
        self.allow_smoothing = None
        self.anti_alias_type = None
        self.auto_size = None
        self.background = None
        self.default_text_format = None
        self.embed_fonts = None
        self.force_smoothing = None
        self.html_text = None
        self.mouse_enabled = None
        self.selectable = None
        self.smoothing = None
        self.text = None
        self.text_height = None
        self.text_width = None
        self.visible = None
        self.width = None
        self.x_pos = None
        self.y_pos = None

        super(Actor, self).__init__(args)


class AntiAliasType(BaseClass):
    '''
        obsolete with cli?
    '''
    ADVANCED = None


class MovieClip(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class TextField(Actor):
    '''
        obsolete with cli?
    '''
    pass


class TextFormat(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class TextFieldAutoSize(Actor):
    '''
        obsolete with cli?
    '''
    RIGHT = None
    LEFT = None


class URLLoader(BaseClass):
    '''
        obsolete with cli?
    '''
    data_format = None

    def __exit__(self, *args):
        '''
            support with statement
        '''
        pass

    def __enter__(self, *args):
        '''
            support with statement
        '''
        pass

    def load(self, *args):
        '''
            obsolete
        '''
        pass


class URLLoaderdataFormat(BaseClass):
    '''
        obsolete with cli?
    '''
    TEXT = None


class URLRequest(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class TextFieldType(BaseClass):
    '''
        obsolete with cli?
    '''
    DYNAMIC = None


class DisplayObject(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class Sound(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class Loader(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class Bitmap(Actor):
    '''
        obsolete with cli?
    '''
    pass


class Timer(BaseClass):
    '''
        obsolete with cli?
    '''
    TIMER = None

    def start(self, *args):
        '''
            obsolete
        '''
        pass

    def stop(self, *args):
        '''
            obsolete
        '''
        pass


class Event(BaseClass):
    '''
        obsolete with cli?
    '''
    COMPLETE = None


class TimerEvent(Event):
    '''
        obsolete with cli?
    '''
    TIMER = None


class MouseEvent(Event):
    '''
        obsolete with cli?
    '''
    MOUSE_UP = None
    MOUSE_DOWN = None
    MOUSE_OVER = None
    MOUSE_MOVE = None
    MOUSE_OUT = None
    CLICK = None


class IOErrorEvent(Event):
    '''
        obsolete with cli?
    '''
    IO_ERROR = None


class KeyboardEvent(Event):
    '''
        obsolete with cli?
    '''
    keyCode = None


class SecurityErrorEvent(Event):
    '''
        obsolete with cli?
    '''
    SECURITY_ERROR = None


class ExternalIF(BaseClass):
    '''
        obsolete with cli?
    '''
    def call(self, *args):
        '''
            obsolete
        '''
        pass


class SecurityHandler(BaseClass):
    '''
        obsolete with cli?
    '''
    def load_policy_file(self, *args):
        '''
            obsolete
        '''
        pass

    def allow_domain(self, *args):
        '''
            obsolete
        '''
        pass


class Function(BaseClass):
    '''
        obsolete with cli?
    '''
    def call(self, *args):
        '''
            obsolete
        '''
        pass


class SharedObject(BaseClass):
    '''
        obsolete with cli?
    '''
    def get_local(self, *args):
        '''
            obsolete
        '''
        pass


class SoundLoaderContext(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class Capabilities(BaseClass):
    '''
        obsolete with cli?
    '''
    version = None


class LoaderError(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class LoaderComplete(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class LoaderContext(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class LoaderInfo(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class ApplicationDomain(BaseClass):
    '''
        obsolete with cli?
    '''
    pass


class SecurityDomain(BaseClass):
    '''
        obsolete with cli?
    '''
    currentDomain = None


def get_child_by_name(*args):
    '''
        obsolete?
    '''
    print args


def get_quest_bg():
    '''
        Get quest background index

        @return int

        obsolete
    '''
    # action = savegame[SG['ACTION']['INDEX']]
    # location = savegame[SG['QUEST']['OFFER']['LOCATION1'] + action - 1]
    # return LBL['SCR']['QUEST']['BG'][str(location)]
    pass


def get_quest_title(quest_id):
    '''
        gets quest title snippet

        @param int quest_id
        @return string

        obsolete
    '''
    # quest = Quest.from_sg(quest_id, savegame)
    # return quest.get_title()
    print quest_id


def get_quest_text(quest_id):
    '''
        get quest description

        @param int quest_id
        @return str

        obsolete
    '''
    # quest = Quest.from_sg(quest_id, savegame)
    # quest.get_text()
    print quest_id


def get_quest_random(quest_id, random_range, random_mod):
    '''
        Get quest random number

        @param int quest_id
        @param int random_range
        @param int random_mod
        @return int

        obsolete
    '''
    # quest = Quest.from_sg(quest_id, savegame)
    # return quest.get_random(random_range, random_mod)
    print quest_id, random_range, random_mod


def load_configuration_file():
    '''
        configuration loader
    '''
    # loader = URLLoader()
    # loader2 = URLLoader()

    # with loader:
    #     data_format = URLLoaderdataFormat.TEXT
    #     add_event_listener(Event.COMPLETE, configuration_file_loaded)
    #     load(URLRequest("client_cfg.php"))

    # with loader2:
    #     data_format = URLLoaderdataFormat.TEXT
    #     add_event_listener(Event.COMPLETE, configuration_file_loaded)

    # pending_loaders += 2
    # # TODO WTF?
    # pending_configuration_files = 1
    # pending_configuration_files = True
    pass


def parse_savegame(str_save_game, fill_face_variables=True, no_spoil=False):
    '''
        parse savegame string
    # '''
    # # parse into array of (mostly) numbers
    # savegame = ("0/" + str_save_game).split("/")

    # # Extract tower level from mount id
    # if not no_spoil:
    #     tower_level = int((savegame[SG['MOUNT']] / 65536))

    # savegame[SG['MOUNT']] -= tower_level * 65536

    # # Extract mirror pieces from gender entry
    # bin_str = int(savegame[SG['GENDER']]).tostr(2)
    # bin_str.zfill(32)

    # mirror_pieces = list()
    # for i in range(13):
    #     mirror_pieces[i] = bin_str.substr(i + 1, 1) == "1"

    # has_mirror = bin_str.substr(23, 1) == "1"
    # can_rob = bin_str.substr(22, 1) == "1"

    # if bin_str.substr(31) == "1":
    #     savegame[SG['GENDER']] = 1
    # else:
    #     savegame[SG['GENDER']] = 2

    # if (savegame[SG['ALBUM']] - 10000) > content_max:
    #     savegame[SG['ALBUM']] = content_max + 10000

    # for i in range(SG['BACKPACK']['SIZE']):
    #     expand_item_structure(
    #         savegame, SG['BACKPACK']['OFFS'] + i * SG['ITM']['SIZE']
    #     )

    # for i in range(SG['INVENTORY']['SIZE']):
    #     expand_item_structure(
    #         savegame, (SG['INVENTORY']['OFFS'] + i * SG['ITM']['SIZE'])
    #     )

    # for i in range(6):
    #     expand_item_structure(
    #         savegame, SG['SHAKES']['ITEM1'] + i * SG['ITM']['SIZE']
    #     )
    #     expand_item_structure(
    #         savegame, SG['FIDGET']['ITEM1'] + i * SG['ITM']['SIZE']
    #     )

    # for i in range(3):
    #     expand_item_structure(
    #         savegame,
    #         (SG['QUEST']['OFFER']['REWARD_ITM1'] + (i * SG['ITM']['SIZE']))
    #     )

    # debug_info = ""
    # for i in range(len(savegame)):
    #     debug_info += str(i) + "=" + savegame[i] + ", "

    # if (last_level != 0) and (int(savegame[SG['LEVEL']]) > last_level):
    #     level_up = True
    #     pulse_char = True

    # last_level = int(savegame[SG['LEVEL']])

    # friend_link = "http://" + server + "/index.php?rec="
    # friend_link += savegame[SG['PLAYER']['ID']]

    # if len(old_ach) != 0:
    #     for i in range(8):
    #         if ach_level(savegame, i) > old_ach[i]:
    #             old_ach[i] = -1 * ach_level(savegame, i)
    #         else:
    #             old_ach[i] = ach_level(savegame, i)
    # else:
    #     for i in range(8):
    #         old_ach[i] = ach_level(savegame, i)

    # if (old_album >= 0) and (savegame[SG['ALBUM']] > old_album):
    #     album_effect = True
    # old_album = savegame[SG['ALBUM']]

    # if fill_face_variables:
    #     char_volk = savegame[SG['RACE']]
    #     char_male = (savegame[SG['GENDER']] == 1)
    #     char_class = savegame[SG['CLASS']]
    #     char_mouth = savegame[SG['FACE']['1']]
    #     char_beard = savegame[SG['FACE']['5']]
    #     char_nose = savegame[SG['FACE']['6']]
    #     char_eyes = savegame[SG['FACE']['4']]
    #     char_brows = savegame[SG['FACE']['3']]
    #     char_ears = savegame[SG['FACE']['7']]
    #     char_hair = savegame[SG['FACE']['2']]
    #     char_special = savegame[SG['FACE']['8']]
    #     char_special2 = savegame[SG['FACE']['9']]

    #     i = char_hair

    #     char_color = 0
    #     while i > 100:
    #         i -= 100
    #         char_color += 1

    # if not no_spoil:
    #     if text_dir == "right":
    #         actor[IF['GOLD']].x = IF['LBL']['GOLDPILZE_X']

    #         with actor[LBL['IF']['GOLD']]:
    #             text = str(int(savegame[SG['GOLD']] / 100))
    #             x = IF['LBL']['GOLDPILZE_X'] - textWidth - 10
    #         actor[IF['SILBER']].x = actor[LBL['IF']['GOLD']].x - width - 10

    #         with (actor[LBL['IF']['SILBER']]):
    #             if int(savegame[SG_GOLD] % 100) < 10:
    #                 text = "0"
    #             else:
    #                 text = ""
    #             text += str(int(savegame[SG['GOLD']] % 100))
    #             x = actor[IF['SILBER']].x - textWidth - 10

    #         with actor[LBL['IF']['PILZE']]:
    #             text = savegame[SG['MUSH']]
    #             x = IF['LBL']['GOLDPILZE']['X'] - textWidth - 10

    #         if texts[TXT['MUSHROOMS']['BOUGHT']]:
    #             enable_popup(
    #                 LBL['IF']['PILZE'],
    #                 texts[TXT['MUSHROOMS']['BOUGHT']].replace(
    #                     "%1", savegame[SG['MUSHROOMS']['MAY']['DONATE']]
    #                 )
    #             )
    #     else:
    #         with (actor[LBL['IF']['SILBER']]):
    #             if int(savegame[SG_GOLD] % 100) < 10:
    #                 text = "0"
    #             else:
    #                 text = ""
    #             text += str(int(savegame[SG['GOLD']] % 100))
    #             x = actor[IF['SILBER']].x - textWidth - 10

    #         actor[IF['GOLD']].x = actor[LBL['IF']['SILBER']].x - 24 - 10

    #         with actor[LBL['IF']['GOLD']]:
    #             text = str(int(savegame[SG['GOLD']] / 100))
    #             x = actor[IF['GOLD']].x - textWidth - 10

    #         with actor[LBL['IF']['PILZE']]:
    #             text = savegame[SG['MUSH']]
    #             x = IF['LBL']['GOLDPILZE']['X'] - textWidth - 10

    #         if texts[TXT['MUSHROOMS']['BOUGHT']]:
    #             enable_popup(
    #                 LBL['IF']['PILZE'],
    #                 texts[TXT['MUSHROOMS']['BOUGHT']].replace(
    #                     "%1", savegame[SG['MUSHROOMS']['MAY']['DONATE']]
    #                 )
    #             )

    # add(IF['STATS'])
    # if int(savegame[SG['SERVER']['TIME']]) > 0:
    #     server_time.setTime(
    #         1000 * int(savegame[SG['SERVER']['TIME']]) - 1000 * 60 * 60
    #     )
    #     local_time = datetime.now()
    #     time_calc.start()

    # if session_id == "":
    #     log.error(''.join(
    #         "Fehler: Keine Session ID für PHP-Tunneling vergeben. ",
    #         "PHP-Tunneling wird deaktiviert."
    #     ))
    #     show_login_screen()
    # else:
    #     log.debug("Session ID für PHP Tunneling:", session_id)

    # if int(savegame[SG['GUILD']['INDEX']]) != gilden_id:
    #     gilden_id = int(savegame[SG['GUILD']['INDEX']])
    #     if gilden_id != 0:
    #         send_action(
    #             ACT['REQUEST']['GUILD'],
    #             savegame[SG['GUILD']['INDEX']]
    #         )

    # sg_idx = SG['UNREAD']['MESSAGES']
    # if (int(savegame[sg_idx]) > 0) and (not on_stage(POST['LIST'])):
    #     pulse_post = True

    # if int(savegame[SG['LOCKDURATION']]) != 0:
    #     request_logout()

    # if next_pxl < 0:
    #     next_pxl = abs(next_pxl)
    print str_save_game, fill_face_variables, no_spoil


def set_volume(vol):
    '''
        set volume

        Obsolete
    '''
    # with (stObject):
    #     stObject.volume = vol
    print vol


def remove_event_listener(*args):
    '''
        obsolete
    '''
    print args


def on_stage(actor_id, actor):
    '''
        actor is schon on screen?
    '''
    if actor[actor_id] is DisplayObject:
        return bool(get_child_by_name(actor[actor_id].name))
    return False


def ach_level(save, ach_index, almode=0):
    '''
    var alresult;
    var alnext;
    alresult = 0;
    alnext = 0;
    Switch (ach_index){
        if case(0:
            alnext = 2;
            if (int(save[SG_ACHIEVEMENTS]) >= 2){
                alresult = 1;
                alnext = 5;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 5){
                alresult = 2;
                alnext = 10;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 10){
                alresult = 3;
                alnext = 20;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 20){
                alresult = 4;
                alnext = 30;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 30){
                alresult = 5;
                alnext = 40;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 40){
                alresult = 6;
                alnext = 50;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 50){
                alresult = 7;
                alnext = 60;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 60){
                alresult = 8;
                alnext = 70;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 70){
                alresult = 9;
                alnext = 80;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 80){
                alresult = 10;
                alnext = 90;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 90){
                alresult = 11;
                alnext = 100;
            };
            if (int(save[SG_ACHIEVEMENTS]) >= 100){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(1:
            alnext = 1;
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 1){
                alresult = 1;
                alnext = 5;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 5){
                alresult = 2;
                alnext = 10;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 10){
                alresult = 3;
                alnext = 20;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 20){
                alresult = 4;
                alnext = 30;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 30){
                alresult = 5;
                alnext = 40;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 40){
                alresult = 6;
                alnext = 50;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 50){
                alresult = 7;
                alnext = 60;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 60){
                alresult = 8;
                alnext = 70;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 70){
                alresult = 9;
                alnext = 80;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 80){
                alresult = 10;
                alnext = 90;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 90){
                alresult = 11;
                alnext = 100;
            };
            if (int(save[(SG_ACHIEVEMENTS + 1)]) >= 100){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(2:
            alnext = 1;
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 1){
                alresult = 1;
                alnext = 5;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 5){
                alresult = 2;
                alnext = 10;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 10){
                alresult = 3;
                alnext = 25;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 25){
                alresult = 4;
                alnext = 50;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 50){
                alresult = 5;
                alnext = 100;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 100){
                alresult = 6;
                alnext = 250;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 250){
                alresult = 7;
                alnext = 500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 500){
                alresult = 8;
                alnext = 1000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 1000){
                alresult = 9;
                alnext = 2500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 2500){
                alresult = 10;
                alnext = 5000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 5000){
                alresult = 11;
                alnext = 10000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 2)]) >= 10000){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(3:
            alnext = 1;
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 1){
                alresult = 1;
                alnext = 5;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 5){
                alresult = 2;
                alnext = 10;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 10){
                alresult = 3;
                alnext = 25;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 25){
                alresult = 4;
                alnext = 50;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 50){
                alresult = 5;
                alnext = 100;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 100){
                alresult = 6;
                alnext = 250;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 250){
                alresult = 7;
                alnext = 500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 500){
                alresult = 8;
                alnext = 1000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 1000){
                alresult = 9;
                alnext = 2500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 2500){
                alresult = 10;
                alnext = 5000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 5000){
                alresult = 11;
                alnext = 10000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 3)]) >= 10000){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(4:
            alnext = 1;
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 1){
                alresult = 1;
                alnext = 5;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 5){
                alresult = 2;
                alnext = 10;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 10){
                alresult = 3;
                alnext = 25;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 25){
                alresult = 4;
                alnext = 50;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 50){
                alresult = 5;
                alnext = 100;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 100){
                alresult = 6;
                alnext = 250;
            };
            if (int(save[(save_ACHIEVEMENTS + 4)]) >= 250){
                alresult = 7;
                alnext = 500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 500){
                alresult = 8;
                alnext = 1000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 1000){
                alresult = 9;
                alnext = 2500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 2500){
                alresult = 10;
                alnext = 5000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 5000){
                alresult = 11;
                alnext = 10000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 4)]) >= 10000){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(5:
            alnext = 1;
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 100){
                alresult = 1;
                alnext = 5;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 500){
                alresult = 2;
                alnext = 10;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 1000){
                alresult = 3;
                alnext = 25;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 2500){
                alresult = 4;
                alnext = 50;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 5000){
                alresult = 5;
                alnext = 100;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 10000){
                alresult = 6;
                alnext = 250;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 25000){
                alresult = 7;
                alnext = 500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 50000){
                alresult = 8;
                alnext = 1000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 100000){
                alresult = 9;
                alnext = 2500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 250000){
                alresult = 10;
                alnext = 5000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 500000){
                alresult = 11;
                alnext = 10000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 5)]) >= 1000000){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(6:
            alnext = 1000;
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 1000){
                alresult = 1;
                alnext = 1500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 1500){
                alresult = 2;
                alnext = 2500;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 2500){
                alresult = 3;
                alnext = 5000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 5000){
                alresult = 4;
                alnext = 10000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 10000){
                alresult = 5;
                alnext = 15000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 15000){
                alresult = 6;
                alnext = 20000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 20000){
                alresult = 7;
                alnext = 25000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 25000){
                alresult = 8;
                alnext = 30000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 30000){
                alresult = 9;
                alnext = 35000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 35000){
                alresult = 10;
                alnext = 40000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 40000){
                alresult = 11;
                alnext = 50000;
            };
            if (int(save[(SG_ACHIEVEMENTS + 6)]) >= 50000){
                alresult = 12;
                alnext = 0;
            };
            break;
        if case(7:
            alresult = int(save[(SG_ACHIEVEMENTS + 7)]);
            alnext = (alresult + 1);
            if (alresult >= 12){
                alresult = 12;
                alnext = 0;
            };
    };
    if (almode == 1){
        if (alresult >= 10){
            return (4);
        };
        if (alresult >= 7){
            return (3);
        };
        if (alresult >= 4){
            return (2);
        };
        if (alresult >= 1){
            return (1);
        };
        return (0);
    };
    if (almode == 2){
        return (alnext);
    };
    if (almode == 3){
        return (alresult);
    };
    if (almode == 4){
        if (ach_index == 1){
            return ((((int(save[(SG_ACHIEVEMENTS + ach_index)])
                    + (((int(save[SG_NEW_DUNGEONS]) >= 2))
                       ? (int(save[save_NEW_DUNGEONS]) - 2) : 0))
                    + (((int(save[(SG_NEW_DUNGEONS + 1)]) >= 2))
                       ? (int(save[(SG_NEW_DUNGEONS + 1)]) - 2) : 0))
                    + (((int(save[save_DUNGEON_13]) >= 122))
                       ? (int(save[SG_DUNGEON_13]) - 122) : 0)));
        };
        return ((int(save[(SG_ACHIEVEMENTS + ach_index)]) / (((ach_index == 5))
                ? 100 : 1)));
    };
    return (alresult);
    '''
    print save, ach_index, almode
    return ''


def enable_popup(actor_id, *args):
    '''
        enable popup actor
    '''
    # popup_width = 0
    # text_y = 0
    # text_x = 0
    # my_stamp = 0

    # my_stamp, popup_stamp = popup_stamp + 1
    # if popup_stamp > 10000:
    #     popup_stamp = 0

    # if len(args) > 0:
    #     actor[actor_id].add_event_listener(MouseEvent.MOUSE_OVER, show_popup)
    #     actor[actor_id].add_event_listener(MouseEvent.MOUSE_MOVE,
    #                                        position_popup)
    #     actor[actor_id].add_event_listener(MouseEvent.MOUSE_OUT, hide_popup)
    #     actor[actor_id].add_event_listener(MouseEvent.MOUSE_DOWN, hide_popup)
    #     actor[actor_id].add_event_listener(MouseEvent.MOUSE_UP, hide_popup)

    # actorpopup_stamp[actor_id] = my_stamp
    print actor_id, args
