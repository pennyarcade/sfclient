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


def on_stage(actor_id):
    '''
        actor is schon on screen?
    '''
    if actor[actor_id] is DisplayObject:
        return bool(get_child_by_name(actor[actor_id].name))
    return False
