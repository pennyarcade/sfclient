#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html
'''

# standard library
import time
from datetime import datetime
import random
import md5
import logging
import math
import types
import base64

# external dependencies
import requests
# import curses

# internal dependencies
from sfglobals import ACT
from sfglobals import ARROW_MAX
from sfglobals import ARROW_OFFS
from sfglobals import BNC
from sfglobals import BTN
from sfglobals import C
from sfglobals import CA
from sfglobals import CB
from sfglobals import CFG
from sfglobals import CLR
from sfglobals import CNT
from sfglobals import ERR
from sfglobals import GUILD
from sfglobals import IMG
from sfglobals import INP
from sfglobals import LBL
from sfglobals import POPUP_INFO
from sfglobals import POS
from sfglobals import REL
from sfglobals import RESP
from sfglobals import SG
from sfglobals import SHP
from sfglobals import SLDR
from sfglobals import SND
from sfglobals import TXT

from sflegacy import AntiAliasType
from sflegacy import ApplicationDomain
from sflegacy import Bitmap
from sflegacy import Capabilities
from sflegacy import DisplayObject
from sflegacy import Event
from sflegacy import ExternalIF
from sflegacy import Function
from sflegacy import IOErrorEvent
from sflegacy import KeyboardEvent
from sflegacy import Loader
from sflegacy import LoaderComplete
from sflegacy import LoaderContext
from sflegacy import LoaderError
from sflegacy import LoaderInfo
from sflegacy import MouseEvent
from sflegacy import MovieClip
from sflegacy import remove_event_listener
from sflegacy import SecurityDomain
from sflegacy import SecurityErrorEvent
from sflegacy import SecurityHandler
from sflegacy import SharedObject
from sflegacy import Sound
from sflegacy import SoundLoaderContext
from sflegacy import TextField
from sflegacy import TextFieldAutoSize
from sflegacy import TextFieldType
from sflegacy import TextFormat
from sflegacy import Timer
from sflegacy import TimerEvent
from sflegacy import URLLoader
from sflegacy import URLLoaderdataFormat
from sflegacy import URLRequest

from sfbuildinterface import build_interface

from sflegacyfonts import FontFormatAttackLabel
from sflegacyfonts import FontFormatAttrib
from sflegacyfonts import FontFormatAttribBonus
from sflegacyfonts import FontFormatAttribTemp
from sflegacyfonts import FontFormatBook
from sflegacyfonts import FontFormatBookHint
from sflegacyfonts import FontFormatBookLeft
from sflegacyfonts import FontFormatBullshit
from sflegacyfonts import FontFormatCatapultDamage
from sflegacyfonts import FontFormatChat
from sflegacyfonts import FontFormatChatError
from sflegacyfonts import FontFormatChatWhisper
from sflegacyfonts import FontFormatClassError
from sflegacyfonts import FontFormatCriticalDamage
from sflegacyfonts import FontFormatDamage
from sflegacyfonts import FontFormatDefault
from sflegacyfonts import FontFormatDefaultLeft
from sflegacyfonts import FontFormatEpicItemQuote
from sflegacyfonts import FontFormatError
from sflegacyfonts import FontFormatGrayed
from sflegacyfonts import FontFormatGrayedHighLight
from sflegacyfonts import FontFormatGuildBuilding
from sflegacyfonts import FontFormatGuildHallNoAttack
from sflegacyfonts import FontFormatGuildListText
from sflegacyfonts import FontFormatGuildListTextAttackError
from sflegacyfonts import FontFormatGuildListTextAttackErrorHalf
from sflegacyfonts import FontFormatGuildListTextAttackErrorOnline
from sflegacyfonts import FontFormatGuildListTextAttackErrorOnlineHalf
from sflegacyfonts import FontFormatGuildListTextAttackErrorOnlinePopup
from sflegacyfonts import FontFormatGuildListTextAttackOk
from sflegacyfonts import FontFormatGuildListTextAttackOkPopup
from sflegacyfonts import FontFormatGuildListTextOnline
from sflegacyfonts import FontFormatGuildMoney
from sflegacyfonts import FontFormatHallListHeading
from sflegacyfonts import FontFormatHallListHighLight
from sflegacyfonts import FontFormatHallListText
from sflegacyfonts import FontFormatHeading
from sflegacyfonts import FontFormatHighlight
from sflegacyfonts import FontFormatHighlightWhisper
from sflegacyfonts import FontFormatHighStakes
from sflegacyfonts import FontFormatHighStakesHighLight
from sflegacyfonts import FontFormatHighStakesHighLightGrayed
from sflegacyfonts import FontFormatItemEnchantment
from sflegacyfonts import FontFormatLifeBar
from sflegacyfonts import FontFormatLOGoutLink
from sflegacyfonts import FontFormatLOGoutLinkHighLight
from sflegacyfonts import FontFormatPayIcon
from sflegacyfonts import FontFormatPopup
from sflegacyfonts import FontFormatPopupCompare
from sflegacyfonts import FontFormatPopupCompareBetter
from sflegacyfonts import FontFormatPopupCompareBetterHL
from sflegacyfonts import FontFormatPopupCompareSum
from sflegacyfonts import FontFormatPopupCompareWorse
from sflegacyfonts import FontFormatPopupCompareWorseHL
from sflegacyfonts import FontFormatPostListHeading
from sflegacyfonts import FontFormatPostListHighLight
from sflegacyfonts import FontFormatPostListHighLightSys
from sflegacyfonts import FontFormatPostListHighLightSysGreen
from sflegacyfonts import FontFormatPostListHighLightSysRed
from sflegacyfonts import FontFormatPostListText
from sflegacyfonts import FontFormatPostListTextSys
from sflegacyfonts import FontFormatPostListTextSysGreen
from sflegacyfonts import FontFormatPostListTextSysRed
from sflegacyfonts import FontFormatQuestBar
from sflegacyfonts import FontFormatScreenTitle
from sflegacyfonts import FontFormatSpeech
from sflegacyfonts import FontFormatTimeBar
from sflegacyfonts import FontFormatToiletAura

from classes.sfsavegame import Savegame
from classes.sfswitch import Switch
from classes.sfface import Face
from classes.sfcharacter import Character

# global for logger
LOG = logging.getLogger()

# TODO: refactor into config object
param_obj = dict()
actor = dict()
texts = dict()

# TODO: should be obsolete
when_loaded_fn = list()
Security = SecurityHandler()
pending_loaders = None
SAVE = None


class RequestFailedException(Exception):
    '''
        Request to server failed
    '''
    pass


class Session(object):
    '''
        Session object to handle request stuff
    '''
    def __init__(self):
        '''
            Constructor to Session object
        '''
        # TODO: Check if needed?
        self.param_poll_tunnel_url = ""
        self.poll_lock = False
        self.send_lock = False
        self.fight_lock = False
        self.mp_api_user_id = 'notset'
        self.mp_api_user_token = 'notset'

        self.server = 's31.sfgame.de'

        self.baseuri = 'http://s31.sfgame.de/request.php'
        self.loginparams = '?req=&random=%%2&rnd=%s%s'

        self.req_format = '%s%%3B%s%%3bv1.70'
        self.rnd_format = '%s%s'

        self.session_id = '00000000000000000000000000000000'
        self.user = 'chocokiko'
        self.pwdmd5 = 'c33def595b633a53fbb6a3987ab54a05'
        random.seed()

    def login(self):
        '''
            login to server

            TODO: refactor to use sendAction()
        '''
        action = '002'

        req_string = self.req_format % (
            self.session_id + action + self.user, self.pwdmd5
        )

        random_string = '%2'
        # TODO: rework random number generation
        rnd_string = self.rnd_format % (
            random.randint(0, 9999999999),
            int(time.time() * 1000)
        )

        payload = {
            'req': req_string,
            'random': random_string,
            'rnd': rnd_string
        }

        resp = requests.get(self.baseuri, params=payload)

        return resp.text.split('/')

    def send_action(self, action, *params):
        '''
            Send formatted request to server
        '''
        if action == ACT['GET_CHAT_HISTORY']:
            if not on_stage(CNT['IF_LOGOUT']):
                return
            if self.param_poll_tunnel_url != "":
                if self.poll_lock:
                    return
            else:
                if self.poll_lock or self.send_lock or self.fight_lock:
                    return action
        else:
            if self.send_lock:
                if (action not in (
                        ACT['VALIDATE'],
                        ACT['SEND_CHAT'],
                        ACT['GUILD']['DONATE'],
                        ACT['REQUEST']['GUILD_NAMES'],
                        ACT['REQUEST']['CHAR'],
                        ACT['POST']['SEND'])):
                    LOG.warning(''.join([
                        "Aktionsbefehl wird ignoriert, weil noch auf eine ",
                        "Serverantwort gewartet wird: ",
                        str(action)
                    ]))
                    return
            else:
                if self.fight_lock:
                    LOG.warning(''.join([
                        "Aktionsbefehl wird ignoriert, weil ein wichtiges ",
                        "Ereignis stattfindet:",
                        str(action)
                    ]))
                    return

        data_str = str(action).zfill(3) + ';'.join(params)
        last_act = action

        fail_try = 1

        if self.session_id == "":
            self.session_id = "00000000000000000000000000000000"

            LOG.debug("SID: " + str(self.session_id))
            LOG.debug("Action: " + str(action))
            LOG.debug("Action+Daten: " + str(data_str))

        # TODO: This "if" switches base URL
        # self.param_poll_tunnel_url / param_php_tunnel_url
        if ((action == ACT['GET_CHAT_HISTORY'])
                and (self.param_poll_tunnel_url != "")):
            # TODO: move payload creation to method
            # self.param_poll_tunnel_url
            req_string = self.session_id + data_str
            random_string = '%2'
            rnd_string = str(round(random.random() * 0x77359400))
            rnd_string += str(int(time.time() * 1000))

            payload = {
                'req': req_string,
                'random': random_string,
                'rnd': rnd_string
            }

            self.poll_lock = True
        else:
            # self.param_php_tunnel_url
            req_string = self.session_id + data_str
            random_string = '%2'
            rnd_string = str(round(random.random() * 0x77359400))
            rnd_string += str(int(time.time() * 1000))

            payload = {
                'req': req_string,
                'random': random_string,
                'rnd': rnd_string
            }

            if action != ACT['GET_CHAT_HISTORY']:
                self.send_lock = True

        if self.mp_api_user_id != "notset":
            payload['mp_api_user_id'] = self.mp_api_user_id

        if self.mp_api_user_token != "notset":
            payload['mp_api_user_token'] = self.mp_api_user_token

        while fail_try < param_fail_tries:
            resp = requests.get(self.baseuri, params=payload)
            LOG.debug(resp.url)

            # TODO : test success of request here !!
            success = True

            if success:
                if ((action == ACT['GET_CHAT_HISTORY'])
                        and (self.param_poll_tunnel_url != "")):
                    self.poll_lock = False
                else:
                    self.send_lock = False

                data = resp.text()

                LOG.debug(str("Antwort auf %s: %s" % (action, data)))

                if data == "":
                    LOG.error(
                        "Fehler: Keine (leere) Antwort vom Tunnelskript.")
                    success = False
                else:
                    return data

            if not success:
                if fail_try < param_fail_tries:
                    LOG.warning(''.join([
                        "PHP-Request fehlgeschlagen (Versuch",
                        str(fail_try), "/",
                        str(param_fail_tries) + ").",
                        "Erneutes Senden..."
                    ]))
                    LOG.info("Erneut gesendet.")
                else:
                    LOG.warning(''.join([
                        "PHP Tunneling fehlgeschlagen. ",
                        "Versuche, neu zu verbinden."
                    ]))
                    self.session_id = ""
                    if ((action == ACT['GET_CHAT_HISTORY'])
                            and (self.param_poll_tunnel_url != "")):
                        self.poll_lock = False
                    else:
                        self.send_lock = False

                    raise RequestFailedException()
                fail_try += 1

    def load_configuration_file(self):
        '''
            configuration loader
        '''

        response = requests.get('http://' + self.server + '/client_cfg.php')

        # error handling

        return response.text


class Account(object):
    '''
        Account information
    '''
    def __init__(self):
        '''
            Setup account object
        '''
        pass


class Album(object):
    '''
        handle collectors album data
    '''
    def __init__(self, effect=False, category=0, page=0):
        '''
            setup collectors album
        '''
        self.effect = effect
        self.category = category
        self.page = page


class Guild(object):
    '''
        handle guild data
    '''
    def __init__(self):
        '''
            setup guild data with default values
        '''
        pass


class Toilet(object):
    '''
        handle toilet data
    '''
    def __init__(self):
        '''
            setup toilet object
        '''
        pass


class Witch(object):
    '''
        handle witch laboratory data
    '''
    def __init__(self):
        '''
            setup wich object
        '''
        pass


def md5hash(instr):
    '''
        Calculate MD5 Hash

        @param string in_str
        @return string MD5 hash
    '''
    return md5.new(instr).hexdigest().lower()


# -----------------------------------------------------------------------------


def setup_logging():
    '''
        Setup logging module for console and file logging
    '''

    # TODO: make configurable
    # create logger
    LOG.setLevel(logging.DEBUG)

    # Console LOGging
    # create console handler and set level to debug
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # add formatter to handler
    handler.setFormatter(formatter)

    # add handler to logger
    LOG.addHandler(handler)

    # File LOGger
    # create console handler and set level to debug
    handler = logging.FileHandler('sfclient.LOG')
    handler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # add formatter to handler
    handler.setFormatter(formatter)

    # add handler to logger
    LOG.addHandler(handler)

    return LOG


def init_vars():
    '''
        Initialize tons of Variables
        ex frame1()

        TODO: check vars if needed
    '''
    # values char_*
    defaultface = Face()

    # values revertchar_*
    global revertface
    revertface = Face()

    # values album_*
    global col_album
    col_album = Album()

    global actor, actorLoaded, actorURL
    actor = list()

    # actorBitmap = list()
    actorLoaded = list()
    # actorPersistent = list()
    # actorpopup_stamp = list()
    # actorSoundLoader = list()
    actorURL = list()

    # admin_login = ""

    # allow_smoothing = True
    # alternate_char_opp_img = False
    # arrow_hall_mode = False
    # avgLevel = 0

    # beer_fest = False

    # BlockReroll = False

    # buffed_email = ""
    # buffed_id = ""
    # buffed_link_text = ""
    # buffed_link_url = ""
    # buffed_mode = False
    # buffed_name = ""
    # buffed_reg = ""
    # buffed_req = False
    # buffed_stuff = list()

    # can_rob = False

    # canBoost = list()

    # chat_sound = False
    # ChatHist = list()

    # chosen_lang_font = "Komika Text"
    # compare_items = False
    # contentMax = 1700
    # copyCatSel = 0

    # CorrectItemType = [6, 3, 5, 4, 8, 7, 9, 10, 1, 2]

    # country_name = list()

    # crest = get_random_crest()
    # crestColor = [0, 0, 0, 0]
    # crestColorSelection = 0
    # crestMoveTimer = new Timer(25)
    # crestMoveTimer.add_event_listener(TimerEvent.TIMER, crest_move_fn)
    # crestSuggested = False
    # crestSuggestion = list()

    # CupChosen = 0
    # dataprot_url = ""
    # dealer_aktion = 0
    # dealer_menuSelect = 0
    # defined_pixel_calls = list()
    # DemoMode = False
    # destroy_guild_btn_timer = False
    # disable_tv = False
    # dragDropActive = False
    # dragDropProhibit = False
    # dragNotYet = False
    # fight_flush_mode = False
    # fight_lock = False
    # fightNumber = 0
    # fights = list()
    # Filter_Shadow = [
    # first_chat_fill = False

    global font_embedded
    font_embedded = True

    # force_adventure = False
    # force_smoothing = True
    # forum_url = ""
    # forward_text = ""
    # FrenzyMode = False
    # friend_link = ""
    # game_font = ""
    # game_time = new Date()
    # gilde = ""
    # GildeBuildingGold = list()
    # GildeBuildingPilz = list()
    # GildeChatScroll = 0
    # gilden_id = 0
    # guild_attack_time = 0
    # guild_attacked = ""
    # guild_attacking = ""
    # guild_blink_ready = False
    # guild_defense_time = 0
    # guild_fight_count = 0
    # guild_hall_mode = False
    # guildForumLink = ""
    # guildInstanceID = 0

    # had_account = False
    # has_mirror = False

    # hasFoughtGuildBattle = False
    # hasLostMQ = False

    image_timeout = 3
    global img_url, img_url_index
    img_url = list()
    img_url_index = 0

    # TODO: remove this when configuration loading works
    img_url.append('')

    # imprint_url = ""
    # indexInGuild = 0
    # indexInHall = 0
    # instr_url = ""
    # interval_multiplier_chat = 1
    # interval_multiplier_reconnect = 1
    # invitegilden_id = 0
    # io_error_count = 0
    # KlasseGewählt = False

    global lang_code, lang_url
    lang_code = "de"
    lang_url = ""

    # last_chat_hist = ""
    # last_chat_index = 0
    # last_guild_data = list()
    # last_guild_shown = ""
    # last_hall_members = list()
    # last_level = 0
    # last_message_target = ""
    # last_round_fighter_name = ""
    # last_whisper_target = ""
    # lastAct = 0
    # lastAttacked = list()
    # LastDungeonenemy = 0
    # Lastdungeon_nr = 0
    # lastguild_members = list()
    # lastPlayer = ""
    # lastRaidCost = 0
    # legal_url = ""
    # level_up = False
    # light_mode = False
    # light_mode_default = False
    # local_time = new Date()
    # login_background_id = "3"
    # mirror_ani_timer = new Timer(25)
    # mirror_ani_timer.add_event_listener(TimerEvent.TIMER, mirror_ani_fn)
    # mirror_fade_amount = 0.2
    # mirror_pieces = list()
    # mirrorAniStep = 0
    # mp_project = "sfgame2"
    # MQDelayTimer = new Timer(500)
    # MQSInstance = 0
    # mush_bought = 0
    # my_own_attack_target = -1
    # my_own_guild_money = -1
    # my_own_rank = -1
    # new_crest_suggested = ""
    next_fight_timer = Timer(10, 1)
    # next_pxl = 0
    # no_crossdomain = False
    # noMush = False
    # notFirstVolChange = True
    # notSecondVolChange = True
    global offline_guild_members, oldcreststring
    offline_guild_members = list()
    # old_album = -1
    oldcreststring = ""
    # oldSel = 0
    # option_new_data = ""
    # original_lang_code = "de"
    # param_adv = ""
    # param_allow_skip_quest = False
    # param_bullshit_cid = ""
    # param_bullshit_text = ""
    # param_censored = False
    # param_cid = ""
    # param_cid_original = False

    global param_fail_tries
    param_fail_tries = 1

    # param_forceport = 0
    # param_gamestaff_email = param_support_email
    # param_hall = ""
    # param_happy_hour = False
    # param_id = ""
    # param_idle_polling = 0
    # param_imgsvr = 0
    # param_internal_pixel = False
    # param_language_names = list()
    # param_languages = list()
    # param_lowres_url = ""
    # param_no_cid_save = False
    # param_obj = LoaderInfo(root.loader_info).parameters
    # param_papaya_cfg_file = ""
    # param_papaya_path = ""
    # param_php_tunnel_url = ""
    # param_poll_tunnel_url = ""
    # param_rec = ""
    # param_reconnect = 5000
    # param_reload_pixel = False
    # param_reroll_img = 0
    # param_server_version_act = "unknown"
    # param_server_version_cfg = "unknown"
    # param_social_buttons = list()
    # param_sponsor = ""
    # param_sponsor_url = ""
    # param_support_email = "support@sfgame.de"
    # param_valid = ""
    # pay_methods = list()

    global pending_configuration_files, pending_debug_file
    global pending_language_file, pending_loaders
    pending_configuration_files = False
    pending_debug_file = False
    pending_language_file = False
    pending_loaders = 0

    # player_desc = ""
    # playerTowerLevel = 0
    # pollLock = False
    # popup_stamp = 0
    # post_fight_mode = False
    # post_scroll = 1
    # post_scrollDown = False
    # post_sel = 0
    # postInstance = 0
    # PostMax = 1
    # PostReturnToPlayer = ""
    # PresetGold = 0
    # PresetMush = 0
    # prevent_tv = False
    # previous_login = False
    # pulse_arbeiten = False
    # pulse_char = False
    # pulse_dealer = False
    # pulse_gilde = False
    # pulse_gilde_on_history = False
    # pulse_post = False
    # pulse_taverne = False
    # reply_address = ""
    # reply_subject = ""
    # response_timeout = 10

    # RollFrenzy = new Timer(1000)
    # ruhmes_halle_such_name = True
    # ruhmes_halle_such_string = ""
    # savegame = list()
    # sel_guild = ""
    # sel_name = ""
    # SelectedDungeon = 0
    # SelectedGuild = ""
    # SelectedQuest = 1
    # selecterCrestElement = -1
    # sendLock = False

    global server
    server = "localhost"

    # server_id = 0
    # server_time = new Date()
    # session_id = ""
    # set_font(new SFGameFont().font_name)
    # shop_url = ""

    # showActivityTime = False
    # showAlbumOffset = False
    # SignupJumpRunning = False

    # size_mod = 0
    # skip_allowed = False
    # skip_guild_fights = 0
    # slm_count = 0
    # smoothing = True

    global snd_url, snd_url_index
    snd_url = list()
    snd_url_index = 0

    # TODO: remove this when configuration loading works
    snd_url.append('')

    # special_action = 0
    # special_actionHint = False
    # sso_mode = False
    # stObject = new SoundTransform()
    # ststep = 0
    # stundenlohn = 10
    # suggestion_slot = list()
    # suggestNames = list()
    global text_dir
    text_dir = "left"
    # tmp_battle_info = ""
    # tmpAmount = 0
    # to_error_count = 0

    # toiletTankAdjustTimer = new Timer(25)
    # toiletTankCurrent = 0
    # toiletTankDest = 0

    # tower_fight_mode = False
    # tower_level = 0
    # tower_levelLabelPos = (SCR_CHAR_CHARX + 127)
    # towerScroll = 0
    # towerScrollDest = 0
    # tower_scroll_grabPos = -1
    # towerScrollSpeed = 0
    # towerScrollTimer = new Timer(25)
    # towerScrollTimer.add_event_listener(TimerEvent.TIMER, tower_timer_fn)

    # trackPixels = list()
    # tv_function_name = ""
    # tv_poll_normal = 5000
    # tv_poll_long = 300000
    # tvTest = False
    # verdientes_geld = 0
    # view_player = ""

    # witchDesiredType = -1

    # worlds = list()
    #     new DropShadowFilter(3, 45, 0, 0.8),
    #     new GradientGlowFilter(
    #         0, 45, [CLR_BLACK, CLR_BLACK], [0, 0.3],
    #         [0, 32], 1, 1, 5, 15, "outer")
    # ]

    # Filter_HeavyShadow = [
    #     new DropShadowFilter(2, 45, 0, 1, 5, 5, 3, 3),
    #     new GradientGlowFilter(
    #         0, 45, [CLR_BLACK, CLR_BLACK], [0, 0.3],
    #         [0, 32], 1, 1, 5, 15, "outer")
    # ]

    # crestElementPos = [
    #     [55, 8, 130, 90, 21],
    #     [0, 50, 240, 150, 34],
    #     [65, 75, 108, 114, 23],
    #     [15, 194, 210, 45, 12],
    #     [85, 17, 73, 70, 24],
    #     [98, 176, 43, 40, 16],
    #     [85, 100, 70, 70, 68]
    # ]

    # heraldicColors = [
    #     [0, 0, 1],
    #     [1, 0, 0],
    #     [0.7, 0, 0.8],
    #     [0.1, 0.1, 0.1],
    #     [0, 0.6, 0],
    #     [1, 0.8, 0],
    #     [0.9, 0.9, 0.9],
    #     [0.7, 0.4, 0.2],
    #     [0.5, 0.5, 0.5],
    #     [0.7, 0, 0],
    #     [0.5, 0, 0.3],
    #     [1, 0.6, 0],
    #     [1, 0.8, 0.8]
    # ]

    # Filter_CrestSelected = new GradientGlowFilter(
    #     0, 0, [16777026, 16777026], [0, 0.6], [0, 127],
    #     26, 26, 1, 1, "outer"
    # )

    # toiletTankAdjustTimer.add_event_listener(
    #     TimerEvent.TIMER,
    #     toilet_tank_adjust_event
    # )

    # get buffered registration?
    if ('reg' in param_obj.keys()) and (param_obj["reg"] is not None):
        buffed_req = True
        buffed_reg = ExternalIF.call("get_base64")
        if (buffed_reg) and (buffed_reg != ""):
            buffed_stuff = buffed_reg.split("")
            if len(buffed_stuff) == 3:
                buffed_id = buffed_stuff[0]
                buffed_name = buffed_stuff[1]
                buffed_email = buffed_stuff[2]

    # pre populate text snippet list
    global texts
    texts = list()
    while len(texts) < 20000:
        texts.append("")

    # setup image loading timeout event
    global when_loaded_fn, when_loaded_active, when_loaded_timeout
    when_loaded_fn = list()
    when_loaded_active = False
    when_loaded_timeout = Timer(1000 * image_timeout, 1)
    when_loaded_timeout.add_event_listener(
        TimerEvent.TIMER,
        when_loaded_timeout_event
    )

    # timer event to generate ticks
    time_calc = Timer(50)
    time_calc.add_event_listener(TimerEvent.TIMER, time_calc_event)

    # TV Stuff
    tv_status = 0
    tv_status_dest = 0
    tv_wobble = 0
    tv_ani = 0
    tv_return_value = 0
    tv_timer = Timer(100)

    tv_timer.add_event_listener(TimerEvent.TIMER, tv_timer_event_handler)
    tv_poll_timer = Timer(5000)
    tv_poll_timer.add_event_listener(TimerEvent.TIMER, try_show_tv)

    pvp_delay_timer = Timer(500)

    # Witch Animation Timer
    witch_ani_step = 0
    witch_ani_timer = Timer(50)
    witch_ani_timer.add_event_listener(TimerEvent.TIMER,
                                       witch_timer_event_handler)

    # Fight timers
    next_fight_timer.add_event_listener(TimerEvent.TIMER, next_fight)
    guild_fight_timer = Timer(1000)
    guild_fight_timer.add_event_listener(TimerEvent.TIMER,
                                         guild_fight_timer_fn)
    guild_fight_timer.start()

    # Guild chat poll
    guild_chat_poll = Timer(1000)
    guild_chat_poll.add_event_listener(TimerEvent.TIMER, guild_chat_poll_fn)
    guild_chat_poll.start()


def configure(session):
    '''
        Load configuration from server
        Load language file from server

        TODO: check event stuff??

        @oldname Start
    '''
    global serverconfig
    serverconfig = session.load_configuration_file()

    when_loaded(do_load_language_file)


# -----------------------------------------------------------------------------
# gold stuff

def geld(amount):
    '''
        Format money amout in silver into a string

        @param int amount
        @return str formatted money string
    '''
    gold = gold_anteil(amount)
    silber = silber_anteil(amount)

    geld_str = ''

    if gold > 0:
        geld_str += '%d %s' % (gold, texts[TXT["GOLD"]])
        if silber > 0:
            geld_str += ' %s ' % (texts[TXT['UND']])
    if silber > 0:
        geld_str += '%d %s' % (texts[TXT['SILBER']])

    return geld_str


def gold_anteil(amount):
    '''
        get gold part of money value

        @param int amount
        @return int
    '''
    return int(amount / 100)


def silber_anteil(amount):
    '''
        get silver part of money value

        @param int amount
        @return int
    '''
    return int(amount % 100)

# -----------------------------------------------------------------------------
# Time and date stuff


def tageszeit():
    '''
        get time of day
        0 - night
        1 - dusk/dawn
        2 - day

        @return int
    '''
    # TODO: make this a parameter?
    hours = time.strftime('%H')

    if hours < 4:
        return 0
    elif hours < 8:
        return 1
    elif hours < 18:
        return 2
    elif hours < 21:
        return 1
    else:
        return 0


def sleep_time():
    '''
        get charakters sleeping time

        @return bool True= Time to sleep
    '''
    # TODO: make this a parameter?
    hours = time.strftime('%H')

    if C['TIMEOFDAY'] >= 0:
        return C['TIMEOFDAY']
    elif hours < 7:
        return True
    elif hours < 23:
        return False
    else:
        return True


def is_today(req_time):
    '''
        checks if timestamp is today
    '''
    req_date = datetime.fromtimestamp(req_time/1000)
    return req_date.date() == datetime.today().date()


def time_str(req_time, short=False):
    '''
        convert datetime object to formatted string

    '''

    req_date = datetime.fromtimestamp(req_time/1000)

    formats = {
        "de": {
            'short': '%d.%m. %H:%M',
            'long': '%d.%m.%Y %H:%M:%S'
        },
        "pl": {
            'short': '%d/%m/ %H:%M',
            'long': '%d/%m/%Y %H:%M:%S'
        },
        "default": {
            'short': '%d/%m/ %H:%M',
            'long': '%d/%m/%Y %H:%M:%S'
        }
    }

    code = lang_code
    if code not in formats.keys():
        code = "default"

    length = 'long'
    if short:
        length = 'short'

    return req_date.strftime(formats[code][length])


def time_calc_event():
    '''
        Time Event Callback
    '''
    current_time = datetime.now()
    if (slm_count > 23) and (ststep == 8):
        add(IMG['FILLSPACE'])
        slm_count = 0

    game_time.setTime(
        current_time.getTime() + server_time.getTime() - local_time.getTime()
    )


# -----------------------------------------------------------------------------
# Weapon stuff

def get_weapon_sound_file(wpn_class, wpn_pic, use_case):
    '''
        get weapon sound file url
    '''
    use_case_str = ""
    for case in Switch(use_case):
        if case(0):
            use_case_str = "s"
            break
        if case(1):
            use_case_str = "n"
            break
        if case(2):
            use_case_str = "b"
            break
        if case(3):
            use_case_str = "k"
            break

    file_name = 'res/sfx/wpn/wpn'
    if wpn_pic < 1:
        file_name += str(1)
    else:
        file_name += str(wpn_class)

    return file_name + "-%d-%s.mp3" % (
        get_weapon_level(wpn_class, wpn_pic) + 1, use_case_str
    )


def get_weapon_sound(wpn_class, wpn_pic, use_case):
    '''
        get sound actor
    '''
    snd_actor = SND['WEAPON']
    snd_actor += (wpn_class - 1) * 4 * 14
    snd_actor += get_weapon_level(wpn_class, wpn_pic) * 4
    snd_actor += snd_actor + use_case
    return snd_actor


def get_weapon_level(wpn_class, wpn_pic):
    '''
        calculate weapon level
    '''
    for case in Switch(wpn_class):
        result = None

        if case(1):
            if wpn_pic == -7:
                result = 7
            elif wpn_pic == -3:
                result = 6
            elif wpn_pic in (-2, -1, 54):
                result = 4
            elif wpn_pic == 0:
                result = 5
            elif wpn_pic in (-5, -4, 1, 2, 3, 4):
                result = 0
            elif wpn_pic in (5, 6, 8, 11, 15, 17, 19, 21, 22, 24, 26, 27,
                             29, 30, 50, 51, 60):
                result = 1
            elif wpn_pic in (-6, 7, 10, 13, 16, 20, 23, 25, 28, 52):
                result = 2
            elif wpn_pic in (9, 12, 14, 18):
                result = 3
            elif wpn_pic == 53:
                result = 8
            elif wpn_pic == 55:
                result = 9
            elif wpn_pic == 56:
                result = 10
            elif wpn_pic == 57:
                result = 11
            elif wpn_pic == 58:
                result = 12
            elif wpn_pic == 59:
                result = 13

            if result is not None:
                return result
            break
        if case(2):
            if wpn_pic in range(-5, 0):
                result = 4
            elif wpn_pic == 0:
                result = 5
            elif wpn_pic in (1, 60):
                result = 0
            elif wpn_pic in (2, 9):
                result = 1
            elif wpn_pic in (6, 7, 10, 52, 54):
                result = 2
            elif wpn_pic in (3, 4, 5, 8, 50, 51):
                result = 3
            elif wpn_pic == 53:
                result = 4
            elif wpn_pic == 55:
                result = 9
            elif wpn_pic == 56:
                result = 10
            elif wpn_pic == 57:
                result = 11
            elif wpn_pic == 58:
                result = 12
            elif wpn_pic == 59:
                result = 13

            if result is not None:
                return result
            break
        if case(3):
            if wpn_pic in range(-5, 0):
                result = 4
            elif wpn_pic == 0:
                result = 5
            elif wpn_pic in (1, 2):
                result = 0
            elif wpn_pic == (3, 5, 6, 7, 50, 52, 53, 54):
                result = 1
            elif wpn_pic in (4, 8, 9, 10, 59):
                result = 2
            elif wpn_pic == 51:
                result = 3
            elif wpn_pic == 55:
                result = 9
            elif wpn_pic == 56:
                result = 10
            elif wpn_pic == 57:
                result = 11
            elif wpn_pic == 58:
                result = 12
            elif wpn_pic == 60:
                result = 13

            if result is not None:
                return result
            break

    return 0

# -----------------------------------------------------------------------------
# request functions


# TODO: How to do Event stuff?
def request_signup(evt):
    '''
        TODO: Documentation
    '''
    if evt is KeyboardEvent:
        if ((KeyboardEvent(evt).keyCode != 13)
                and (KeyboardEvent(evt).keyCode != 10)
                and (KeyboardEvent(evt).keyCode != 16777230)):
            inp_text = actor[INP['NAME']].getChildAt(1).text
            if inp_text.substr(0, 7) == "xxxtest":
                actor[INP['EMAIL']].getChildAt(1).text = (
                    inp_text + "@playagames.com"
                )
                actor[INP['PASSWORD']].getChildAt(1).text = "12345"
                add(CB['AGB']['CHECKED'])
            return

    if get_child_by_name(actor[CB['AGB_CHECKED']].name):
        if (param_bullshit_text != "") and (on_stage(CB['FUCK']['CHECKED'])):
            param_cid = param_bullshit_cid
            shared_obj.data.cid = param_cid
            shared_obj.flush()

        if buffed_req:
            bufftxt = "buf" + buffed_id
        else:
            bufftxt = param_adv

        if char_male:
            genderparam = 1
        else:
            genderparam = 2

        faceparam = '/'.join(
            charface.mouth, charface.hair, charface.brows, charface.eyes,
            charface.beard, charface.nose, charface.ears, charface.special,
            charface.special2
        )

        # Create account
        send_action(
            ACT['ACCOUNT']['CREATE'],
            actor[INP['NAME']].getChildAt(1).text,
            actor[INP['PASSWORD']].getChildAt(1).text,
            actor[INP['EMAIL']].getChildAt(1).text,
            param_rec,
            bufftxt,
            charface.volk,
            genderparam,
            charface.cclass,
            faceparam,
            param_cid
        )
    else:
        error_message(texts[TXT['ERROR']['AGB']])


def request_player_screen(evt):
    '''
        request player screen
    '''
    sel_index = actor[CNT['HALL']['LIST']].getChildIndex(evt.target)
    if sel_index < 5:
        return

    sel_row = int((sel_index - 5) / 6) + 1
    sel_name = hall_list_name[sel_row]
    sel_guild = hall_list_guild[sel_row]
    if sel_name == "":
        return
    send_action(ACT['REQUEST']['CHAR'], sel_name)


def request_player_guild_screen(evt):
    '''
        setup request for guild screen
    '''
    sel_index = actor[CNT['HALL']['LIST']].getChildIndex(evt.target)
    if sel_index < 5:
        return

    sel_row = int((sel_index - 5) / 6 + 1)
    sel_name = hall_list_name[sel_row]
    sel_guild = hall_list_guild[sel_row]

    if sel_guild == texts[TXT['NOGUILD']]:
        return

    if sel_guild == "":
        return

    if sel_guild == gilde:
        send_action(ACT['SCREEN']['GILDEN'])
    else:
        send_action(ACT['SCREEN']['FREMDGILDE'], sel_guild)


def request_login(evt=None):
    '''
        setup login request
    '''
    if evt is KeyboardEvent:
        if ((KeyboardEvent(evt).keyCode != 13)
                and (KeyboardEvent(evt).keyCode != 10)
                and (KeyboardEvent(evt).keyCode != 16777230)):
            return

    tmp_pw = actor[INP['LOGIN_PASSWORD']].getChildAt(1).text
    if C['MD5']:
        if len(tmp_pw) < 32:
            tmp_pw = md5hash(tmp_pw)

    send_action(
        ACT['LOGIN'],
        actor[INP['NAME']].getChildAt(1).text,
        tmp_pw,
        "v1.70"
    )


def request_logout(keep_data=False):
    '''
        prepare logout action
    '''
    remove_all()
    next_pxl = 0
    actor[LBL['ERROR']].text = ""
    if not keep_data:
        shared_obj.data.userName = ""
        shared_obj.data.password = ""
        actor[INP['NAME']].getChildAt(1).text = ""
        actor[INP['LOGIN_PASSWORD']].getChildAt(1).text = ""
        shared_obj.flush()
        actor[INP['EMAIL']].getChildAt(1).text = ""
        actor[INP['PASSWORD']].getChildAt(1).text = ""

    send_action(ACT['LOGOUT'])
    savegame = list()
    char_volk = 0
    gilde = ""
    my_own_rank = -1
    my_own_attack_target = -1
    my_own_guild_money = -1
    guild_attack_time = 0
    guild_defense_time = 0
    guild_attacked = ""
    guild_attacking = ""
    pulse_taverne = False
    pulse_arbeiten = False
    pulse_gilde = False
    pulse_gilde_on_history = False
    pulse_post = False
    pulse_dealer = False
    guild_blink_ready = False
    session_id = ""
    fight_flush_mode = False
    if not keep_data:
        show_login_screen()


def request_cancel_arbeiten():
    '''
        cancel work
    '''
    send_action(ACT['ARBEIT']['CANCEL'])


def request_arbeiten():
    '''
        start working
    '''
    send_action(ACT['ARBEIT'], get_slider_value(SLDR['ARBEITEN']))


def request_create_character():
    '''
        TODO: obsolete?
    '''
    pass


def request_change_face():
    '''
        prepare to change profile picture
    '''
    if ((charface.volk == revertchar.volk)
            and (charface.male == revertchar.male)
            and (charface.color == revertchar.color)
            and (charface.mouth == revertchar.mouth)
            and (charface.beard == revertchar.beard)
            and (charface.nose == revertchar.nose)
            and (charface.eyes == revertchar.eyes)
            and (charface.brows == revertchar.brows)
            and (charface.ears == revertchar.ears)
            and (charface.hair == revertchar.hair)
            and (charface.special == revertchar.special)
            and (charface.special2 == revertchar.special2)):
        send_action(ACT['SCREEN']['OPTIONEN'])
    else:
        tmp_gender = 2
        if charface.male:
            tmp_gender = 1

        send_action(
            ACT['CHANGE']['FACE'],
            actor[INP['NAME']].getChildAt(1).text,
            actor[INP['LOGIN_PASSWORD']].getChildAt(1).text,
            charface.volk,
            tmp_gender,
            '/'.join(
                charface.mouth,
                charface.hair,
                charface.brows,
                charface.eyes,
                charface.beard,
                charface.nose,
                charface.ears,
                charface.special,
                charface.special2
            ) + "/"
        )


def request_char_screen():
    '''
        setup and request character screen
    '''
    arrow_hall_mode = False
    send_action(ACT['SCREEN']['CHAR'])


def request_city_screen():
    '''
        TODO: obsolete?
    '''
    pass


def request_tv():
    '''
        request tv action
    '''
    if tv_function_name != "":
        LOG.debug(''.join(['Calling TV function "',
                           tv_function_name,
                           '" with parameter "showtv"!']))

        ExternalIF.call(tv_function_name,
                        "showtv",
                        '_'.join(savegame[SG['PLAYER_ID']],
                                 savegame[SG['PAYMENT_ID']],
                                 server_id,
                                 "1"),
                        savegame[SG['GENDER']],
                        tv_return_value)
        tv_poll_timer.delay = tv_poll_long
    else:
        LOG.error("Error: No TV function set!")

    tv_status_dest = 0


# -----------------------------------------------------------------------------
# Tower stuff


def tower_btn_handler(evt):
    '''
    var i;
    Switch (get_actor_id(evt.target)){
        if case(PREV_COPYCAT:
            copyCatSel--;
            if (copyCatSel < 0){
                copyCatSel = 2;
            };
            display_inventory(towerSG, True, True, copyCatSel);
            break;
        if case(NEXT_COPYCAT:
            copyCatSel++;
            if (copyCatSel > 2){
                copyCatSel = 0;
            };
            display_inventory(towerSG, True, True, copyCatSel);
            break;
        if case(TOWER_TRY:
            show_main_quest_screen(100, (399 + tower_level));
            break;
    };
    '''
    print evt


def tower_scroll_grab():
    '''
    tower_scroll_grabPos = evt.localY;
    towerScrollSpeed = 0;
    '''
    pass


def tower_scroll_move(evt):
    '''
    if (tower_scroll_grabPos != -1){
        towerScrollSpeed = (evt.localY - tower_scroll_grabPos);
        towerScroll = (towerScroll + (towerScrollSpeed / 375));
        towerScrollDest = towerScroll;
        towerScrollTimer.start();
        tower_scroll_grabPos = evt.localY;
    };
    '''
    print evt


def tower_scroll_relase():
    '''
    if (tower_scroll_grabPos != -1){
        towerScrollDest = (towerScrollDest + (towerScrollSpeed / 40));
        towerScrollTimer.start();
        tower_scroll_grabPos = -1;
    };
    '''
    pass


def tower_scroll_release():
    '''
    if (tower_scroll_grabPos != -1){
        TODO: Something missing here
    };
    '''
    pass


def tower_scroll_curent():
    '''
    towerScrollDest = (towerSG[TSG_TOWER_LEVEL] + 1);
    towerScrollTimer.start();
    tower_scroll_grabPos = -1;
    '''
    pass


def tower_scroll_wheel():
    '''
    towerScrollSpeed = (evt.delta * 10);
    towerScroll = (towerScroll + (towerScrollSpeed / 375));
    towerScrollDest = towerScroll;
    towerScrollTimer.start();
    '''
    pass


def tower_key_event(evt):
    '''
    var evt:* = evt;
    if (on_stage(TOWER_SCROLLAREA)){
        if (evt.keyCode == Keyboard.ENTER){
            towerScrollDest = towerSG[TSG_TOWER_LEVEL];
            towerScrollTimer.start();
        } else {
            if (evt.keyCode == Keyboard.UP){
                towerScrollDest = (math.round(towerScrollDest) + 1);
                towerScrollTimer.start();
            } else {
                if (evt.keyCode == Keyboard.DOWN){
                    towerScrollDest = (math.round(towerScrollDest) - 1);
                    towerScrollTimer.start();
                };
            };
        };
    } else {
        var _local3 = actor[TOWER_SCROLLAREA];
        with (_local3) {
            remove_event_listener(KeyboardEvent.KEY_DOWN, tower_key_event);
            remove_event_listener(FocusEvent.FOCUS_OUT,
                                  tower_scroll_set_focus);
        };
    };
    '''
    print evt


def tower_scroll_set_focus():
    '''
    var evt:* = evt;
    if (on_stage(TOWER_SCROLLAREA)){
        stage.focus = actor[TOWER_SCROLLAREA];
    } else {
        var _local3 = actor[TOWER_SCROLLAREA];
        with (_local3) {
            remove_event_listener(KeyboardEvent.KEY_DOWN, tower_key_event);
            remove_event_listener(FocusEvent.FOCUS_OUT,
                                  tower_scroll_set_focus);
        };
    };
    '''
    pass


def tower_timer_fn(evt=None):
    '''
    var i;
    var towerScrollMax = "";
    var towerScrollLvl:Array;
    var thisFloor:*;
    towerScrollMax = 100;
    if (!on_stage(TOWER_SCROLLAREA)){
        towerScrollTimer.stop();
    };
    if (towerScrollDest > towerScrollMax){
        towerScrollDest = towerScrollMax;
    };
    if (towerScrollDest < 0){
        towerScrollDest = 0;
    };
    if (math.abs((towerScroll - towerScrollDest)) > 0.01){
        towerScroll = (((towerScroll * 9) + towerScrollDest) / 10);
    } else {
        towerScroll = towerScrollDest;
        towerScrollTimer.stop();
    };
    if (towerScroll > towerScrollMax){
        towerScroll = towerScrollMax;
    };
    if (towerScroll < 0){
        towerScroll = 0;
    };
    actor[TOWER_BG].y = (-700 + ((towerScroll / towerScrollMax) * 700));
    actor[TOWER_BASE].y = (towerScroll * 375);
    towerScrollLvl = list();
    i = 0;
    while (i < 3) {
        towerScrollLvl[i] = (towerScroll - 0.7);
        while (towerScrollLvl[i] > (3 - i)) {
            towerScrollLvl[i] = (towerScrollLvl[i] - 3);
        };
        i++;
    };
    towerScrollLvl[2] = (((575 - 350) + 35) + (towerScrollLvl[2] * 375));
    towerScrollLvl[1] = (((575 - 700) + 10) + (towerScrollLvl[1] * 375));
    towerScrollLvl[0] = ((575 - 1065) + (towerScrollLvl[0] * 375));
    towerScrollLvl.sort(Array.NUMERIC);
    thisFloor = 0;
    i = 0;
    while (i < 3) {
        thisFloor = math.floor((towerScroll - 0.7));
        if (thisFloor < 0){
            thisFloor = 0;
        };
        thisFloor = (thisFloor + i);
        set_cnt(
            (TOWER_WINDOW + i),
            (((thisFloor < (int(towerSG[TSG_TOWER_LEVEL]) + 1)))
                ? TOWER_WINDOW_BURNT
                : (((thisFloor == (int(towerSG[TSG_TOWER_LEVEL]) + 1)))
                    ? TOWER_WINDOW_OPEN
                    : TOWER_WINDOW_CLOSED))
        );
        set_cnt(
            (TOWER_FACE + i),
            ((OPPMONSTER + int(towerSG[TSG_TOWER_LEVEL])) + 399)
        );
        actor[(TOWER_LEVEL + i)].y = towerScrollLvl[(2 - i)];
        actor[(TOWER_WINDOW + i)].y = towerScrollLvl[(2 - i)];
        actor[(TOWER_FACE + i)].y = (towerScrollLvl[(2 - i)] + 277);
        i++;
    };
    '''
    print evt


# -----------------------------------------------------------------------------
# show functions


def do_show_screen_album():
    '''
    var i;
    i = 0;
    while (i < 4) {
        set_cnt((ALBUM_MONSTER_FRAME + i), FIGHT_CHAR_BORDER);
        i++;
    };
    showalbum_content();
    remove_all();
    add(SCREEN_ALBUM);
    '''
    pass


def show_screen_album():
    '''
    var i:* = 0;
    var do_show_screen_album:* = None;
    load(FIGHT_CHAR_BORDER);
    load(UNKNOWN_enemy);
    i = 0;
    while (i < 5) {
        load((ALBUM_CAT_OUT + i));
        i = (i + 1);
    };
    when_loaded(do_show_screen_album);
    '''
    pass


def show_tower_screen(tower_data):
    '''
    var thisCpc:* = 0;
    var DoShowTowerScreen:* = None;
    var thisSlot:* = 0;
    var tower_data:* = tower_data;
    DoShowTowerScreen = function (){
        var i:* = 0;
        var _local2 = actor[TOWER_SCROLLAREA];
        with (_local2) {
            addChild(actor[TOWER_BG]);
            addChild(actor[(TOWER_LEVEL + 2)]);
            addChild(actor[(TOWER_LEVEL + 1)]);
            addChild(actor[TOWER_LEVEL]);
            addChild(actor[TOWER_FACE]);
            addChild(actor[(TOWER_FACE + 1)]);
            addChild(actor[(TOWER_FACE + 2)]);
            addChild(actor[TOWER_WINDOW]);
            addChild(actor[(TOWER_WINDOW + 1)]);
            addChild(actor[(TOWER_WINDOW + 2)]);
            addChild(actor[TOWER_BASE]);
            add_event_listener(KeyboardEvent.KEY_DOWN, tower_key_event);
        };
        stage.focus = actor[TOWER_SCROLLAREA];
        if (!on_stage(TOWER_SCROLLAREA)){
            towerScrollDest = (int(towerSG[TSG_TOWER_LEVEL]) + 1);
            if (light_mode){
                towerScroll = towerScrollDest;
            } else {
                towerScroll = 0;
            };
            towerScrollTimer.start();
            set_alpha(CHAR_SECONDPROP, 1);
            set_alpha(CHAR_PREISE, 0);
        };
        remove_all();
        add(SCREEN_TOWER);
        if (tower_level >= 100){
            remove(TOWER_TRY);
        };
        i = 0;
        while (i < 3) {
            actor[
                (LBL_TOWER_BOOSTPRICELABEL + i)
            ].text = str(int(
                (towerSG[((TSG_COPYCATS + (i * COPYCAT))
                    + CPC_PRICE_NEXT_LEVEL)] / 100)));
            i = (i + 1);
        };
        display_inventory(towerSG, True, True, copyCatSel);
    };
    towerSG = tower_data[1].split("/");
    thisCpc = 0;
    while (thisCpc < 3) {
        thisSlot = 0;
        while (thisSlot < 10) {
            expand_item_structure(
                towerSG,
                (((TSG_COPYCATS + (thisCpc * COPYCAT)) + CPC_ITEMS)
                    + (thisSlot * SG['ITM']['SIZE'])));
            thisSlot = (thisSlot + 1);
        };
        thisCpc = (thisCpc + 1);
    };
    load(SCREEN_TOWER);
    load(TOWER_PIECES);
    if (towerSG[TSG_TOWER_LEVEL] < 100){
        load(((OPPMONSTER + int(towerSG[TSG_TOWER_LEVEL])) + 399));
    };
    when_loaded(DoShowTowerScreen);
    '''
    print tower_data


def show_demo_screen():
    '''
    var DoShowDemoScreen:* = None;
    DoShowDemoScreen = function (){
        remove_all();
        DemoMode = True;
        add(SCREEN_DEMO);
        var _local2 = actor[BG_DEMO];
        with (_local2) {
            x = (SCREEN_TITLE_X - int((width / 2)));
        };
        remove(IF_STATS, IF_LOGOUT);
    };
    load(SCREEN_DEMO);
    when_loaded(DoShowDemoScreen);
    '''
    pass


def show_option_screen(evt=None):
    '''
    var DoShowOptionScreen:* = None;
    var evt:* = evt;
    DoShowOptionScreen = function (){
        var i:* = 0;
        remove_all();
        set_cnt(CHANGE_PASSWORD_SMILEY_SAD, PASSWORD_SMILEY_SAD);
        set_cnt(CHANGE_PASSWORD_SMILEY_NEUTRAL, PASSWORD_SMILEY_NEUTRAL);
        set_cnt(CHANGE_PASSWORD_SMILEY_HAPPY, PASSWORD_SMILEY_HAPPY);
        hide(CHANGE_PASSWORD_SMILEY_SAD);
        hide(CHANGE_PASSWORD_SMILEY_NEUTRAL);
        hide(CHANGE_PASSWORD_SMILEY_HAPPY);
        add(SCREEN_OPTION);
        if (((texts[TXT_LUXURY_BUTTON]) and ((savegame[SG_MUSH] >= 1000)))){
            actor[OPTION_RESEND].y = ((OPTION_Y + OPTION_Y4) - 34);
            actor[OPTION_CHANGE_PASSWORD].y = ((OPTION_Y + OPTION_Y3) - 17);
            actor[OPTION_DELETE].y = ((OPTION_Y + OPTION_Y5) - 51);
            add(OPTION_LUXURY);
        };
        if (text_dir == "right"){
            actor[LBL_OPTION_CHANGE].x = (
                (actor[OPTION_CHANGE_NAME].x
                    + actor[OPTION_CHANGE_NAME].width)
                    - actor[LBL_OPTION_CHANGE].text_width);
            actor[LBL_OPTION_IMAGE].x = (
                (actor[OPTION_IMAGEBORDER].x
                    + actor[OPTION_IMAGEBORDER].width)
                    - actor[LBL_OPTION_IMAGE].text_width);
        };
        enable_popup(
            LBL_OPTION_VER,
            POPUP_BEGIN_LINE,
            "Player ID",
            140,
            savegame[SG['PLAYER_ID']],
            POPUP_END_LINE,
            POPUP_BEGIN_LINE,
            "Server Ver.Cfg.",
            140,
            param_server_version_cfg,
            POPUP_END_LINE,
            POPUP_BEGIN_LINE,
            "Server Ver.Act.",
            140,
            param_server_version_act,
            POPUP_END_LINE
        );
        i = 0;
        while (i < 10) {
            var _local2 = actor[(CHARBACKGROUND + i)];
            with (_local2) {
                x = ((OPTION_X + OPTION_IMAGE_X) + 4);
                y = ((OPTION_Y + OPTION_Y2) + 4);
                scaleX = 0.56;
                scaleY = 0.56;
            };
            i = (i + 1);
        };
        _local2 = actor[LBL_OPTION_TITLE];
        with (_local2) {
            x = ((OPTION_X + int((OPTION_X / 2))) - int((text_width / 2)));
        };
        load_character_image();
        set_slider_value(SLDR_OPTION_VOLUME, (shared_obj.data.volume + 1));
        if (light_mode){
            add(CB_LM_CHECKED);
        };
        if (chat_sound){
            add(CB_CS_CHECKED);
        };
        if (compare_items){
            add(CB_COMPARE_CHECKED);
        };
        if (tv_function_name != ""){
            if (disable_tv){
                add(CB_TV_CHECKED);
            };
        } else {
            remove(CB_TV_CHECKED);
            remove(CB_TV_UNCHECKED);
            remove(LBL_TV_CHECKBOX);
        };
    };
    load(SCREEN_OPTION);
    load(PASSWORD_SMILEY_SAD);
    load(PASSWORD_SMILEY_NEUTRAL);
    load(PASSWORD_SMILEY_HAPPY);
    when_loaded(DoShowOptionScreen);
    '''
    print evt


def do_skip_fight(evt=None, fight_done=False):
    '''
    var quest_id:* = 0;
    var PilzBekommen:* = False;
    var i:* = 0;
    var charWin:* = False;
    var lastHero:* = None;
    var lastHeroWins:* = 0;
    var heroCount:* = 0;
    var thisWinner:* = None;
    var evt:* = evt;
    var fight_done:Boolean = fight_done;
    quest_id = (savegame[SG_ACTION_INDEX] - 1);
    var rewardX:* = FIGHT_REWARDGOLD_X;
    PilzBekommen = get_pilz;
    var pilzX:* = FIGHT_REWARDGOLD_X;
    var rewardGoldText:* = "";
    var fightStyle:* = 5;
    fight_lock = False;
    DoStrikeTimer.stop();
    DoStrikeTimer.remove_event_listener(TimerEvent.TIMER, do_strike_event);
    actor[FIGHT_SKIP].remove_event_listener(
        MouseEvent.CLICK, do_skip_fight);
    actor[BATTLE_SKIP].remove_event_listener(
        MouseEvent.CLICK, do_skip_fight);
    actor[BATTLE_SKIPONE].remove_event_listener(
        MouseEvent.CLICK, do_skip_fight);
    fightRound = (int((fight_data.length / 6)) - 1);
    charLife = fight_data[(fightRound * 6)];
    charDamage = fight_data[((fightRound * 6) + 1)];
    charFlag = fight_data[((fightRound * 6) + 2)];
    oppLife = fight_data[((fightRound * 6) + 3)];
    oppDamage = fight_data[((fightRound * 6) + 4)];
    oppFlag = fight_data[((fightRound * 6) + 5)];
    charWin = (charLife > 0);
    set_life_bars();
    if (((!(is_guildBattle)) or (last_fight))){
        remove(FIGHT_SKIP);
        remove(BATTLE_SKIP);
        remove(BATTLE_SKIPONE);
        add(LBL_FIGHT_SUMMARY);
    };
    if (is_guildBattle){
        if (((charWin) and (last_fight))){
            play(SND_JINGLE);
        };
    } else {
        show(IF_STATS);
        add(FIGHT_OK);
        if (charWin){
            play(SND_JINGLE);
        };
    };
    if (is_guildBattle){
        last_round_fighter_name = thisCharName;
        if (charWin){
            if (winners[("name_" + thisCharName)]){
                var _local4 = winners;
                var _local5 = ("name_" + thisCharName);
                var _local6 = (_local4[_local5] + 1);
                _local4[_local5] = _local6;
            } else {
                winners[("name_" + thisCharName)] = 1;
            };
        };
        if (((tower_fight_mode) and ((guild_fight_honor >= 0)))){
            set_cnt(
                FIGHT_SLOT,
                GetItemID(
                    SG_INVENTORY_OFFS,
                    (guild_fight_honor + 10),
                     savegame
                 )
            );
            item_popup(
                FIGHT_SLOT,
                (SG_INVENTORY_OFFS
                    + ((guild_fight_honor + 10)
                        * SG['ITM']['SIZE'])
                ),
                None,
                False,
                True,
                False
            );
            guild_fight_honor = 0;
        } else {
            set_cnt(FIGHT_SLOT, C_EMPTY);
            enable_popup(FIGHT_SLOT);
        };
        if (last_fight){
            lastHero = "";
            lastHeroWins = 0;
            heroCount = 0;
            if (texts[TXT_HERO_OF_THE_DAY]){
                for (thisWinner in winners) {
                    if (winners[thisWinner] > lastHeroWins){
                        lastHeroWins = winners[thisWinner];
                        lastHero = texts[TXT_HERO_OF_THE_DAY].split(
                            "%1").join(thisWinner[5:]).split(
                            "%2").join(str(lastHeroWins));
                        heroCount = 1;
                    } else {
                        if (winners[thisWinner] == lastHeroWins){
                            lastHeroWins = winners[thisWinner];
                            lastHero = (
                                lastHero + (chr(13)
                                + texts[TXT_HERO_OF_THE_DAY].split(
                                    "%1").join(thisWinner[5:]).split(
                                    "%2").join(str(lastHeroWins))));
                            heroCount = (heroCount + 1);
                        };
                    };
                };
                if (
                    (((((lastHeroWins >= 5))
                        and (charWin)))
                        and (!(isRaid)))){
                    add(HERO_OF_THE_DAY);
                    if (heroCount == 1){
                        actor[LBL_HERO_OF_THE_DAY_TITLE].text = (
                            (texts[TXT_HERO_OF_THE_DAY_TITLE])
                            ? texts[TXT_HERO_OF_THE_DAY_TITLE]
                            : "");
                    } else {
                        actor[LBL_HERO_OF_THE_DAY_TITLE].text = (
                            (texts[TXT_HEROES_OF_THE_DAY_TITLE])
                                ? texts[TXT_HEROES_OF_THE_DAY_TITLE]
                                : "");
                    };
                    actor[LBL_HERO_OF_THE_DAY_TITLE].x = (
                        SCREEN_TITLE_X - (
                            actor[LBL_HERO_OF_THE_DAY_TITLE].width / 2
                            ));
                    actor[LBL_HERO_OF_THE_DAY].text = lastHero;
                    actor[LBL_HERO_OF_THE_DAY].x = (S
                        CREEN_TITLE_X -
                        (actor[LBL_HERO_OF_THE_DAY].width / 2)
                        );
                };
            };
            add(FIGHT_OK);
            add(FIGHT_REWARDS);
            hide(
                FIGHT_REWARDGOLD,
                LBL_FIGHT_REWARDGOLD,
                FIGHT_REWARDSILVER,
                LBL_FIGHT_REWARDSILVER,
                FIGHT_REWARDMUSH,
                LBL_FIGHT_REWARDMUSH,
                LBL_FIGHT_REWARDEXP
            );
            if ((((guild_fight_exp > 0)) and (charWin))){
                if (tower_fight_mode){
                    _local4 = actor[LBL_FIGHT_REWARDGOLD];
                    with (_local4) {
                        visible = True;
                        text = str(guild_fight_exp);
                        x = (rewardX - text_width);
                    };
                    _local4 = actor[FIGHT_REWARDGOLD];
                    with (_local4) {
                        visible = True;
                        x = (
                            (actor[LBL_FIGHT_REWARDGOLD].x - width)
                            - 8);
                    };
                } else {
                    _local4 = actor[LBL_FIGHT_REWARDEXP];
                    with (_local4) {
                        visible = True;
                        if (text_dir == "right"){
                            text = (
                                (str(math.abs(guild_fight_exp)) + " :")
                                + texts[TXT_EXP]);
                        } else {
                            text = (
                                (texts[TXT_EXP] + ": ")
                                + str(math.abs(guild_fight_exp)));
                        };
                    };
                };
            };
            if (!isRaid){
                _local4 = actor[LBL_FIGHT_REWARDGOLD];
                with (_local4) {
                    visible = True;
                    if (text_dir == "right"){
                        text = (
                            (str(math.abs(guild_fight_honor)) + " ")
                            + texts[(((guild_fight_honor > 0))
                                ? TXT_GUILD_HONOR_GAINED
                                : TXT_GUILD_HONOR_LOST)]);
                    } else {
                        text = (
                            (texts[(((guild_fight_honor > 0))
                                ? TXT_GUILD_HONOR_GAINED
                                : TXT_GUILD_HONOR_LOST)] + " ")
                            + str(math.abs(guild_fight_honor)));
                    };
                    x = (rewardX - text_width);
                };
            };
        } else {
            if ((evt is MouseEvent)){
                if (get_actor_id(evt.target) == BATTLE_SKIP){
                    skip_guild_fights = (
                        math.abs(skip_guild_fights) + 1);
                };
            };
        };
    } else {
        if (is_pvp){
            add(FIGHT_REWARDS);
            hide(
                FIGHT_REWARDGOLD,
                LBL_FIGHT_REWARDGOLD,
                FIGHT_REWARDSILVER,
                LBL_FIGHT_REWARDSILVER,
                FIGHT_REWARDMUSH,
                LBL_FIGHT_REWARDMUSH,
                LBL_FIGHT_REWARDEXP
            );
            if (honor_gain != 0){
                _local4 = actor[LBL_FIGHT_REWARDEXP];
                with (_local4) {
                    visible = True;
                    if (text_dir == "right"){
                        text = (
                            (str(math.abs(honor_gain)) + " ")
                            + texts[(((honor_gain > 0))
                                ? TXT_HONOR_GAINED
                                : TXT_HONOR_LOST)]);
                    } else {
                        text = (
                            (texts[(((honor_gain > 0))
                                ? TXT_HONOR_GAINED
                                : TXT_HONOR_LOST)] + " ")
                                + str(math.abs(honor_gain)));
                    };
                };
            };
            if (gold_gain > 0){
                if (text_dir == "right"){
                    rewardGoldText = (
                        " " + texts[TXT_GOLD_GAINED]);
                } else {
                    rewardGoldText = (texts[TXT_GOLD_GAINED] + " ");
                };
            } else {
                if (gold_gain < 0){
                    if (text_dir == "right"){
                        rewardGoldText = (" " + texts[TXT_GOLD_LOST]);
                    } else {
                        rewardGoldText = (texts[TXT_GOLD_LOST] + " ");
                    };
                };
            };
            if (silber_anteil(math.abs(gold_gain)) > 0){
                if (text_dir != "right"){
                    _local4 = actor[FIGHT_REWARDSILVER];
                    with (_local4) {
                        visible = True;
                        x = (rewardX - width);
                        rewardX = (x - 8);
                    };
                };
                _local4 = actor[LBL_FIGHT_REWARDSILVER];
                with (_local4) {
                    visible = True;
                    if (text_dir == "right"){
                        text = (
                            silber_anteil(math.abs(gold_gain))
                            + rewardGoldText);
                    } else {
                        text = (
                            (((gold_anteil(math.abs(gold_gain)) > 0))
                                ? ""
                                : rewardGoldText)
                            + silber_anteil(math.abs(gold_gain)));
                    };
                    x = (rewardX - text_width);
                    rewardX = (x - (((text_dir == "right")) ? 8 : 14));
                };
                if (text_dir == "right"){
                    _local4 = actor[FIGHT_REWARDSILVER];
                    with (_local4) {
                        visible = True;
                        x = (rewardX - width);
                        rewardX = (x - 14);
                    };
                };
            };
            if (gold_anteil(math.abs(gold_gain)) > 0){
                if (text_dir != "right"){
                    _local4 = actor[FIGHT_REWARDGOLD];
                    with (_local4) {
                        visible = True;
                        x = (rewardX - width);
                        rewardX = (x - 8);
                    };
                };
                _local4 = actor[LBL_FIGHT_REWARDGOLD];
                with (_local4) {
                    visible = True;
                    if (text_dir == "right"){
                        text = (
                            gold_anteil(math.abs(gold_gain))
                            + (((silber_anteil(math.abs(gold_gain))
                                > 0)) ? "" : rewardGoldText));
                    } else {
                        text = (
                            rewardGoldText
                            + gold_anteil(math.abs(gold_gain)));
                    };
                    x = (rewardX - text_width);
                    rewardX = (x - (((text_dir == "right")) ? 8 : 14));
                };
                if (text_dir == "right"){
                    _local4 = actor[FIGHT_REWARDGOLD];
                    with (_local4) {
                        visible = True;
                        x = (rewardX - width);
                        rewardX = (x - 14);
                    };
                };
            };
            set_cnt(FIGHT_SLOT, C_EMPTY);
            enable_popup(FIGHT_SLOT);
        } else {
            if (((is_mq) and (charWin))){
                add(FIGHT_REWARDS);
                hide(
                    FIGHT_REWARDGOLD,
                    LBL_FIGHT_REWARDGOLD,
                    FIGHT_REWARDSILVER,
                    LBL_FIGHT_REWARDSILVER,
                    FIGHT_REWARDMUSH,
                    LBL_FIGHT_REWARDMUSH,
                    LBL_FIGHT_REWARDEXP
                );
                if (honor_gain > 0){
                    _local4 = actor[LBL_FIGHT_REWARDEXP];
                    with (_local4) {
                        visible = True;
                        if (text_dir == "right"){
                            text = (
                                (str(honor_gain) + " :")
                                + texts[TXT_EXP]);
                        } else {
                            text = (
                                (texts[TXT_EXP] + ": ")
                                + str(honor_gain));
                        };
                    };
                };
                if (PilzBekommen){
                    _local4 = actor[FIGHT_REWARDMUSH];
                    with (_local4) {
                        visible = True;
                        x = (pilzX - width);
                        pilzX = (x - 8);
                    };
                    _local4 = actor[LBL_FIGHT_REWARDMUSH];
                    with (_local4) {
                        visible = True;
                        text = "1";
                        x = (pilzX - text_width);
                        pilzX = (x - 14);
                    };
                    animate_ach(
                        FIGHT_REWARDMUSH,
                        actor[FIGHT_REWARDMUSH].y);
                };
                if (silber_anteil(gold_gain) > 0){
                    _local4 = actor[FIGHT_REWARDSILVER];
                    with (_local4) {
                        visible = True;
                        x = (rewardX - width);
                        rewardX = (x - 8);
                    };
                    _local4 = actor[LBL_FIGHT_REWARDSILVER];
                    with (_local4) {
                        visible = True;
                        text = silber_anteil(gold_gain);
                        x = (rewardX - text_width);
                        rewardX = (x - 14);
                    };
                };
                if (gold_anteil(gold_gain) > 0){
                    _local4 = actor[FIGHT_REWARDGOLD];
                    with (_local4) {
                        visible = True;
                        x = (rewardX - width);
                        rewardX = (x - 8);
                    };
                    _local4 = actor[LBL_FIGHT_REWARDGOLD];
                    with (_local4) {
                        visible = True;
                        text = gold_anteil(gold_gain);
                        x = (rewardX - text_width);
                        rewardX = (x - 14);
                    };
                };
                if (back_pack_slot >= 0){
                    set_cnt(
                        FIGHT_SLOT,
                        GetItemID(SG_INVENTORY_OFFS,
                            (back_pack_slot + 10),
                            savegame));
                    item_popup(
                        FIGHT_SLOT,
                        (SG_INVENTORY_OFFS
                            + ((back_pack_slot + 10)
                                * SG['ITM']['SIZE'])),
                        None,
                        False,
                        True,
                        False
                    );
                } else {
                    set_cnt(FIGHT_SLOT, C_EMPTY);
                    enable_popup(FIGHT_SLOT);
                };
            } else {
                if (is_mq){
                    hasLostMQ = True;
                } else {
                    if (
                        ((charWin)
                        and ((savegame[SG_ACTION_STATUS] == 2)))
                    ){
                        add(FIGHT_REWARDS);
                        hide(
                            FIGHT_REWARDGOLD,
                            LBL_FIGHT_REWARDGOLD,
                            FIGHT_REWARDSILVER,
                            LBL_FIGHT_REWARDSILVER,
                            FIGHT_REWARDMUSH,
                            LBL_FIGHT_REWARDMUSH,
                            LBL_FIGHT_REWARDEXP
                        );
                        if (
                            int(savegame[
                                (SG_QUEST_OFFER_EXP1 + quest_id)
                                ]) > 0){
                            _local4 = actor[LBL_FIGHT_REWARDEXP];
                            with (_local4) {
                                visible = True;
                                if (text_dir == "right"){
                                    text = (
                                        (savegame[
                                            (SG_QUEST_OFFER_EXP1
                                                + quest_id)
                                        ] + " :")
                                        + texts[TXT_EXP]);
                                } else {
                                    text = (
                                        (texts[TXT_EXP] + ": ")
                                        + savegame[
                                        (SG_QUEST_OFFER_EXP1
                                            + quest_id)]);
                                };
                            };
                        };
                        if (PilzBekommen){
                            _local4 = actor[FIGHT_REWARDMUSH];
                            with (_local4) {
                                visible = True;
                                x = (pilzX - width);
                                pilzX = (x - 8);
                            };
                            _local4 = actor[LBL_FIGHT_REWARDMUSH];
                            with (_local4) {
                                visible = True;
                                text = "1";
                                x = (pilzX - text_width);
                                pilzX = (x - 14);
                            };
                            animate_ach(
                                FIGHT_REWARDMUSH,
                                actor[FIGHT_REWARDMUSH].y);
                        };
                        if (silber_anteil(
                            savegame[(SG_QUEST_OFFER_GOLD1
                                + quest_id)]) > 0){
                            _local4 = actor[FIGHT_REWARDSILVER];
                            with (_local4) {
                                visible = True;
                                x = (rewardX - width);
                                rewardX = (x - 8);
                            };
                            _local4 = actor[LBL_FIGHT_REWARDSILVER];
                            with (_local4) {
                                visible = True;
                                text = silber_anteil(
                                    savegame[(SG_QUEST_OFFER_GOLD1
                                        + quest_id)]);
                                x = (rewardX - text_width);
                                rewardX = (x - 14);
                            };
                        };
                        if (gold_anteil(
                            savegame[(SG_QUEST_OFFER_GOLD1
                                + quest_id)]) > 0){
                            _local4 = actor[FIGHT_REWARDGOLD];
                            with (_local4) {
                                visible = True;
                                x = (rewardX - width);
                                rewardX = (x - 8);
                            };
                            _local4 = actor[LBL_FIGHT_REWARDGOLD];
                            with (_local4) {
                                visible = True;
                                text = gold_anteil(savegame[
                                    (SG_QUEST_OFFER_GOLD1 + quest_id)]);
                                x = (rewardX - text_width);
                                rewardX = (x - 14);
                            };
                        };
                        if (int(savegame[
                            ((SG['QUEST']['OFFER']['REWARD_ITM1']
                                + (quest_id * SG['ITM']['SIZE']))
                                + SG_ITM_TYP)]) > 0){
                            set_cnt(
                                FIGHT_SLOT,
                                GetItemID(
                                    SG['QUEST']['OFFER']['REWARD_ITM1'],
                                    quest_id));
                            item_popup(
                                FIGHT_SLOT,
                                (SG['QUEST']['OFFER']['REWARD_ITM1']
                                    + (quest_id * SG['ITM']['SIZE'])),
                                None, False, True, False);
                        } else {
                            set_cnt(FIGHT_SLOT, C_EMPTY);
                            enable_popup(FIGHT_SLOT);
    if (charWin){
        if ((charLife / charFullLife) > 0.8){
            fightStyle = 0;
        } else {
            if ((charLife / charFullLife) > 0.4){
                fightStyle = 5;
            } else {
                if ((charLife / charFullLife) > 0.2){
                    fightStyle = 10;
                } else {
                    fightStyle = 15;
    } else {
        if ((oppLife / oppFullLife) > 0.8){
            fightStyle = 0;
        } else {
            if ((oppLife / oppFullLife) > 0.4){
                fightStyle = 5;
            } else {
                if ((oppLife / oppFullLife) > 0.2){
                    fightStyle = 10;
                } else {
                    fightStyle = 15;
    _local4 = actor[LBL_FIGHT_SUMMARY];
    with (_local4) {
        width = FIGHT_RESULT_TEXT_X;
        wordWrap = True;
        if (is_guildBattle){
            if (last_fight){
                if (tower_fight_mode){
                    if (charWin){
                        text = texts[
                            (TXT_TOWER_WON + int((random.random() * 5)))
                        ];
                    } else {
                        text = texts[
                            (TXT_TOWER_LOST + int((random.random() * 5)))
                        ];
                    };
                } else {
                    if (isRaid){
                        if (charWin){
                            text = texts[
                                TXT_RAID_WON + int(random.random() * 5)
                            ];
                        } else {
                            text = texts[
                                (TXT_RAID_LOST +
                                    int((random.random() * 5)))];
                        };
                    } else {
                        if (charWin){
                            text = texts[(TXT_GUILD_BATTLE_WON
                                + int((random.random() * 5)))];
                        } else {
                            text = texts[(TXT_GUILD_BATTLE_LOST
                                + int((random.random() * 5)))];
            } else {
                if (!in_strikeAni){
                    next_fight_timer.start();
                } else {
                    strikeBreak = True;
                };
                return;
            };
        } else {
            if (is_pvp){
                text = texts[
                    ((int((random.random() * 5)) + fightStyle)
                        + ((charWin)
                            ? TXT_PVP_WIN
                            : TXT_PVP_LOSE))];
            } else {
                text = texts[
                    ((int((random.random() * 5)) + fightStyle)
                        + ((charWin)
                            ? TXT_FIGHT_WIN
                            : TXT_FIGHT_LOSE))];
        x = (SCREEN_TITLE_X - int((width / 2)));
    };
    arabize(LBL_FIGHT_SUMMARY);
    '''
    print evt, fight_done


def set_life_bars(which_one=0):
    '''
    var barWidth:* = 0;
    var which_one = which_one;
    if ((((which_one == 0)) or ((which_one == 1)))){
        var _local3 = actor[LBL_LIFEBAR_CHAR];
        with (_local3) {
            if (text_dir == "right"){
                text = ((str(charFullLife) + " / ") + str(charLife));
            } else {
                text = ((str(charLife) + " / ") + str(charFullLife));
            };
            x = ((FIGHT_CHARX + 150) - int((text_width / 2)));
        };
        _local3 = actor[LIFEBAR_FILL_CHAR];
        with (_local3) {
            barWidth = (
                (Number(charLife) / Number(charFullLife)) * 279);
            if (barWidth < 0){
                barWidth = 0;
            };
            width = barWidth;
            scaleY = 1;
        };
    };
    if ((((which_one == 0)) or ((which_one == 2)))){
        _local3 = actor[LBL_LIFEBAR_OPP];
        with (_local3) {
            if (text_dir == "right"){
                text = ((str(oppFullLife) + " / ") + str(oppLife));
            } else {
                text = ((str(oppLife) + " / ") + str(oppFullLife));
            };
            x = ((OPPX + 150) - int((text_width / 2)));
        };
        _local3 = actor[LIFEBAR_FILL_OPP];
        with (_local3) {
            barWidth = (
                (Number(oppLife) / Number(oppFullLife)) * 279);
            if (barWidth < 0){
                barWidth = 0;
            };
            width = barWidth;
            scaleY = 1;
        };
    };
    '''
    print which_one


def do_strike_event(evt):
    '''
    if (((!(on_stage(FIGHT_BOX1))) or (strikeBreak))){
        DoStrikeTimer.stop();
        DoStrikeTimer.remove_event_listener(
            TimerEvent.TIMER, do_strike_event);
        return;
    };
    if ((((skip_guild_fights > 0)) and (is_guildBattle))){
        do_skip_fight();
        DoStrikeTimer.stop();
        DoStrikeTimer.remove_event_listener(
            TimerEvent.TIMER, do_strike_event);
        return;
    };
    if (fightRound > (int((fight_data.length / 6)) - 1)){
        do_skip_fight(None, True);
        return;
    };
    charLife = fight_data[(fightRound * 6)];
    charDamage = fight_data[((fightRound * 6) + 1)];
    charFlag = fight_data[((fightRound * 6) + 2)];
    oppLife = fight_data[((fightRound * 6) + 3)];
    oppDamage = fight_data[((fightRound * 6) + 4)];
    oppFlag = fight_data[((fightRound * 6) + 5)];
    if (
        (((((((fightRound == 0))
            and (!(oppStrike))))
            and ((charDamage == 0))))
            and ((charFlag == 0)))){
        oppStrike = True;
    };
    DoStrikeTimer.stop();
    weapon_strike(oppStrike);
    if (
        ((((oppStrike)
            and ((charLife <= 0))))
            or (((!(oppStrike))
            and ((oppLife <= 0)))))){
        return;
    };
    oppStrike = !(oppStrike);
    if (!oppStrike){
        fightRound++;
    };
    '''
    print evt


def weapon_strike(opponent=False):
    '''
    var StrikeAniTimer:* = None;
    var StrikeAlpha:* = NaN;
    var BulletAlpha:* = NaN;
    var ShieldAlpha:* = NaN;
    var DamageAlpha:* = NaN;
    var OnoAlpha:* = NaN;
    var strikeVal:* = NaN;
    var strikePhase:* = 0;
    var damageIndicatorActive:* = False;
    var weaponType:* = 0;
    var onoID:* = 0;
    var DoSkip:* = False;
    var catapultStrike:* = False;
    var StrikeAniTimerEvent:* = None;
    var opponent:Boolean = opponent;
    StrikeAniTimerEvent = function (evt:TimerEvent){
        var evt:* = evt;
        if (!on_stage(FIGHT_BOX1)){
            in_strikeAni = False;
            if (strikeBreak){
                next_fight_timer.start();
            };
            StrikeAniTimer.stop();
            StrikeAniTimer.remove_event_listener(
                TimerEvent.TIMER,
                StrikeAniTimerEvent);
            return;
        };
        Switch (((catapultStrike) ? 4 : weaponType)){
            if case(1:
                if (
                    (((((((opponent) ? oppWeapon : charWeapon) < 0))
                    and ((opponent) ? oppWeapon : charWeapon) > -4))
                    or ((opponent) ? oppWeapon : charWeapon) < -6)
                ){
                    Switch (strikePhase){
                        if case(0:
                            if ((strikeVal == 0)){
                                play(
                                    get_weapon_sound(((opponent)
                                        ? oppWeaponType
                                        : charWeaponType),
                                        ((opponent)
                                            ? oppWeapon
                                            : charWeapon), 0));
                            };
                            strikeVal = (strikeVal + 0.2);
                            if (
                                (((((opponent)
                                    ? oppFlag
                                    : charFlag) == 1))
                                and ((strikeVal >= 0.4)))){
                                ShieldAlpha = 1;
                            };
                            if (strikeVal >= 0.4){
                                strikePhase++;
                            };
                            break;
                        if case(1:
                            strikeVal = (strikeVal + 0.2);
                            if (strikeVal >= 1){
                                strikeVal = 1;
                                strikePhase++;
                                damageIndicatorActive = True;
                                DamageAlpha = 1;
                                set_life_bars(((opponent) ? 1 : 2));
                                var _local3 = actor[
                                    LBL_DAMAGE_INDICATOR];
                                with (_local3) {
                                    text = ("-" + str(((opponent)
                                        ? oppDamage : charDamage)));
                                    if (text == "-0"){
                                        if (((opponent)
                                            ? oppFlag
                                            : charFlag) == 1){
                                            text = texts[TXT_GEBLOCKT];
                                            play(get_weapon_sound(
                                                ((opponent)
                                                    ? oppWeaponType
                                                    : charWeaponType),
                                                ((opponent)
                                                    ? oppWeapon
                                                    : charWeapon), 2));
                                        } else {
                                            text = texts[
                                                TXT_AUSGEWICHEN];
                                        };
                                    } else {
                                        play(
                                            get_weapon_sound(
                                                ((opponent)
                                                    ? oppWeaponType
                                                    : charWeaponType),
                                                ((opponent)
                                                    ? oppWeapon
                                                    : charWeapon),
                                                ((((opponent)
                                                    ? oppFlag
                                                    : charFlag))==3)
                                                        ? 3 : 1));
                                    };
                                    x = ((SCREEN_TITLE_X
                                        + (((opponent) ? -1 : 1)
                                            * 200)) -
                                            int((text_width / 2)));
                                    y = (FIGHT_WEAPONS_Y - 100);
                                };
                                if (
                                    ((((opponent)
                                    and ((charLife <= 0))))
                                    or (((!(opponent))
                                    and ((oppLife <= 0)))))){
                                    DoSkip = True;
                                };
                            };
                            break;
                        if case(2:
                            DamageAlpha = (DamageAlpha - 0.075);
                            StrikeAlpha = (StrikeAlpha - 0.2);
                            ShieldAlpha = (ShieldAlpha - 0.2);
                            actor[LBL_DAMAGE_INDICATOR].y = (
                                actor[LBL_DAMAGE_INDICATOR].y - 2);
                            if (ShieldAlpha <= 0){
                                ShieldAlpha = 0;
                            };
                            if (StrikeAlpha <= 0){
                                StrikeAlpha = 0;
                            };
                            if (DamageAlpha <= 0){
                                DamageAlpha = 0;
                                in_strikeAni = False;
                                if (strikeBreak){
                                    next_fight_timer.start();
                                };
                                StrikeAniTimer.stop();
                                StrikeAniTimer.remove_event_listener(
                                    TimerEvent.TIMER,
                                    StrikeAniTimerEvent);
                                DoStrikeTimer.start();
                            };
                            break;
                    };
                } else {
                    Switch (strikePhase){
                        if case(0:
                            if ((strikeVal == 0)){
                                play(get_weapon_sound(
                                    ((opponent)
                                        ? oppWeaponType
                                        : charWeaponType),
                                    ((opponent)
                                        ? oppWeapon
                                        : charWeapon), 0));
                            };
                            strikeVal = (strikeVal + 0.1);
                            if (
                                (((((opponent)
                                    ? oppFlag
                                    : charFlag) == 1))
                                and ((strikeVal >= 0.5)))){
                                ShieldAlpha = 1;
                            };
                            if (strikeVal >= 0.8){
                                strikePhase++;
                            };
                            break;
                        if case(1:
                            strikeVal = (strikeVal + 0.15);
                            if (strikeVal >= 1){
                                set_cnt(
                                    FIGHT_ONO, onoID, 0, 0, True);
                                OnoAlpha = 1;
                                strikeVal = 1;
                                strikePhase++;
                                damageIndicatorActive = True;
                                DamageAlpha = 1;
                                set_life_bars(((opponent) ? 1 : 2));
                                _local3 = actor[LBL_DAMAGE_INDICATOR];
                                with (_local3) {
                                    text = (
                                        "-" + str((
                                            (opponent)
                                                ? oppDamage
                                                : charDamage)));
                                    if (text == "-0"){
                                        if (
                                            ((opponent)
                                                ? oppFlag
                                                : charFlag) == 1){
                                            text = texts[
                                            TXT_GEBLOCKT];
                                            play(get_weapon_sound(
                                                ((opponent)
                                                    ? oppWeaponType
                                                    : charWeaponType),
                                                ((opponent)
                                                    ? oppWeapon
                                                    : charWeapon),
                                                2));
                                        } else {
                                            text = texts[
                                                TXT_AUSGEWICHEN];
                                        };
                                    } else {
                                        play(get_weapon_sound(
                                            ((opponent)
                                                ? oppWeaponType
                                                : charWeaponType),
                                            ((opponent)
                                                ? oppWeapon
                                                : charWeapon),
                                            ((((opponent)
                                                ? oppFlag
                                                : charFlag))==3)
                                                    ? 3 : 1));
                                    };
                                    x = ((SCREEN_TITLE_X
                                        + (((opponent) ? -1 : 1)
                                            * 200))
                                            - int((text_width / 2)));
                                    y = (FIGHT_WEAPONS_Y - 100);
                                };
                                if (
                                    ((((opponent)
                                    and ((charLife <= 0))))
                                    or (((!(opponent))
                                    and ((oppLife <= 0)))))){
                                    DoSkip = True;
                                };
                            };
                            break;
                        if case(2:
                            DamageAlpha = (DamageAlpha - 0.075);
                            StrikeAlpha = (StrikeAlpha - 0.2);
                            ShieldAlpha = (ShieldAlpha - 0.2);
                            OnoAlpha = (OnoAlpha - 0.2);
                            actor[LBL_DAMAGE_INDICATOR].y = (
                                actor[LBL_DAMAGE_INDICATOR].y - 2);
                            if (OnoAlpha <= 0){
                                OnoAlpha = 0;
                            };
                            if (ShieldAlpha <= 0){
                                ShieldAlpha = 0;
                            };
                            if (StrikeAlpha <= 0){
                                StrikeAlpha = 0;
                            };
                            if (DamageAlpha <= 0){
                                DamageAlpha = 0;
                                in_strikeAni = False;
                                if (strikeBreak){
                                    next_fight_timer.start();
                                };
                                StrikeAniTimer.stop();
                                StrikeAniTimer.remove_event_listener(
                                    TimerEvent.TIMER,
                                    StrikeAniTimerEvent);
                                DoStrikeTimer.start();
                            };
                            break;
                    };
                };
                break;
            if case(2:
                Switch (strikePhase){
                    if case(0:
                        strikeVal = (strikeVal + 0.15);
                        if (strikeVal >= 0.4){
                            strikePhase++;
                            BulletAlpha = 1;
                            play(get_weapon_sound(
                                ((opponent)
                                    ? oppWeaponType
                                    : charWeaponType),
                                ((opponent)
                                    ? oppWeapon
                                    : charWeapon), 0));
                        };
                        break;
                    if case(1:
                        strikeVal = (strikeVal + 0.15);
                        if (
                            (((((opponent)
                                ? oppFlag
                                : charFlag) == 1))
                            and ((strikeVal >= 0.5)))){
                            ShieldAlpha = 1;
                        };
                        if (strikeVal >= 1){
                            set_cnt(FIGHT_ONO, onoID, 0, 0, True);
                            OnoAlpha = 1;
                            strikeVal = 1;
                            strikePhase++;
                            DamageAlpha = 1;
                            damageIndicatorActive = True;
                            set_life_bars(((opponent) ? 1 : 2));
                            _local3 = actor[LBL_DAMAGE_INDICATOR];
                            with (_local3) {
                                text = ("-" + str((
                                    (opponent)
                                    ? oppDamage
                                    : charDamage)));
                                if (text == "-0"){
                                    if (
                                        ((opponent)
                                            ? oppFlag
                                            : charFlag) == 1){
                                        text = texts[TXT_GEBLOCKT];
                                        play(get_weapon_sound(
                                            ((opponent)
                                                ? oppWeaponType
                                                : charWeaponType),
                                            ((opponent)
                                                ? oppWeapon
                                                : charWeapon), 2));
                                    } else {
                                        text = texts[TXT_AUSGEWICHEN];
                                    };
                                } else {
                                    play(get_weapon_sound(
                                        ((opponent)
                                            ? oppWeaponType
                                            : charWeaponType),
                                        ((opponent)
                                            ? oppWeapon
                                            : charWeapon),
                                        ((((opponent)
                                            ? oppFlag
                                            : charFlag))==3)
                                                ? 3 : 1));
                                };
                                x = ((SCREEN_TITLE_X + (
                                    ((opponent) ? -1 : 1) * 200))
                                    - int((text_width / 2)));
                                y = (FIGHT_WEAPONS_Y - 100);
                            };
                            if (
                                ((((opponent)
                                and ((charLife <= 0))))
                                or (((!(opponent))
                                and ((oppLife <= 0)))))){
                                DoSkip = True;
                            };
                        };
                        break;
                    if case(2:
                        DamageAlpha = (DamageAlpha - 0.075);
                        StrikeAlpha = (StrikeAlpha - 0.2);
                        ShieldAlpha = (ShieldAlpha - 0.2);
                        BulletAlpha = (BulletAlpha - 0.2);
                        OnoAlpha = (OnoAlpha - 0.2);
                        actor[LBL_DAMAGE_INDICATOR].y = (
                            actor[LBL_DAMAGE_INDICATOR].y - 2);
                        if (OnoAlpha <= 0){
                            OnoAlpha = 0;
                        };
                        if (ShieldAlpha <= 0){
                            ShieldAlpha = 0;
                        };
                        if (StrikeAlpha <= 0){
                            StrikeAlpha = 0;
                        };
                        if (DamageAlpha <= 0){
                            DamageAlpha = 0;
                            in_strikeAni = False;
                            if (strikeBreak){
                                next_fight_timer.start();
                            };
                            StrikeAniTimer.stop();
                            StrikeAniTimer.remove_event_listener(
                                TimerEvent.TIMER,
                                StrikeAniTimerEvent);
                            DoStrikeTimer.start();
                        };
                        break;
                };
                break;
            if case(3:
                Switch (strikePhase){
                    if case(0:
                        strikeVal = (strikeVal + 0.05);
                        BulletAlpha = 1;
                        if (strikeVal >= 0.3){
                            strikePhase++;
                            play(get_weapon_sound(
                                ((opponent)
                                    ? oppWeaponType
                                    : charWeaponType),
                                ((opponent)
                                    ? oppWeapon
                                    : charWeapon), 0));
                        };
                        break;
                    if case(1:
                        strikeVal = (strikeVal + 0.1);
                        if (
                            (((((opponent)
                                ? oppFlag
                                : charFlag) == 1))
                            and ((strikeVal >= 0.5)))){
                            ShieldAlpha = 1;
                        };
                        if (strikeVal >= 1){
                            set_cnt(FIGHT_ONO, onoID, 0, 0, True);
                            OnoAlpha = 1;
                            strikeVal = 1;
                            strikePhase++;
                            DamageAlpha = 1;
                            damageIndicatorActive = True;
                            set_life_bars(((opponent) ? 1 : 2));
                            _local3 = actor[LBL_DAMAGE_INDICATOR];
                            with (_local3) {
                                text = ("-" + str((
                                    (opponent)
                                        ? oppDamage
                                        : charDamage)));
                                if (text == "-0"){
                                    if (
                                        ((opponent)
                                            ? oppFlag
                                            : charFlag) == 1){
                                        text = texts[TXT_GEBLOCKT];
                                        play(get_weapon_sound(
                                            ((opponent)
                                                ? oppWeaponType
                                                : charWeaponType),
                                            ((opponent)
                                                ? oppWeapon
                                                : charWeapon), 2));
                                    } else {
                                        text = texts[TXT_AUSGEWICHEN];
                                    };
                                } else {
                                    play(get_weapon_sound(
                                        ((opponent)
                                            ? oppWeaponType
                                            : charWeaponType),
                                        ((opponent)
                                            ? oppWeapon
                                            : charWeapon),
                                        ((((opponent)
                                            ? oppFlag
                                            : charFlag))==3)
                                                ? 3 : 1));
                                };
                                x = ((SCREEN_TITLE_X +
                                    (((opponent) ? -1 : 1) * 200))
                                    - int((text_width / 2)));
                                y = (FIGHT_WEAPONS_Y - 100);
                            };
                            if (
                                ((((opponent)
                                and ((charLife <= 0))))
                                or (((!(opponent))
                                    and ((oppLife <= 0)))))){
                                DoSkip = True;
                            };
                        };
                        break;
                    if case(2:
                        DamageAlpha = (DamageAlpha - 0.075);
                        StrikeAlpha = (StrikeAlpha - 0.2);
                        ShieldAlpha = (ShieldAlpha - 0.2);
                        BulletAlpha = (BulletAlpha - 0.2);
                        OnoAlpha = (OnoAlpha - 0.2);
                        actor[LBL_DAMAGE_INDICATOR].y = (
                            actor[LBL_DAMAGE_INDICATOR].y - 2);
                        if (OnoAlpha <= 0){
                            OnoAlpha = 0;
                        };
                        if (ShieldAlpha <= 0){
                            ShieldAlpha = 0;
                        };
                        if (StrikeAlpha <= 0){
                            StrikeAlpha = 0;
                        };
                        if (DamageAlpha <= 0){
                            DamageAlpha = 0;
                            in_strikeAni = False;
                            if (strikeBreak){
                                next_fight_timer.start();
                            };
                            StrikeAniTimer.stop();
                            StrikeAniTimer.remove_event_listener(
                                TimerEvent.TIMER,
                                StrikeAniTimerEvent);
                            DoStrikeTimer.start();
                        };
                        break;
                };
                break;
            if case(4:
                Switch (strikePhase){
                    if case(0:
                        if (strikeVal == 0){
                            play(SND_CATAPULT_LAUNCH);
                            load(FIGHT_MUSH);
                        };
                        strikeVal = (strikeVal + 0.01);
                        if (strikeVal >= 0.3){
                            strikePhase++;
                            add(FIGHT_MUSH);
                        };
                        break;
                    if case(1:
                        strikeVal = (strikeVal + 0.1);
                        if (strikeVal >= 1){
                            strikeVal = 1;
                            strikePhase++;
                            DamageAlpha = 1;
                            damageIndicatorActive = True;
                            set_life_bars(((opponent) ? 1 : 2));
                            play(SND_CATAPULT_HIT);
                            _local3 = actor[LBL_DAMAGE_INDICATOR];
                            with (_local3) {
                                text = ("-" + str((
                                    (opponent)
                                        ? oppDamage
                                        : charDamage)));
                                x = ((SCREEN_TITLE_X + (
                                    ((opponent) ? -1 : 1) * 200))
                                    - int((text_width / 2)));
                                y = (FIGHT_WEAPONS_Y - 100);
                            };
                            if (
                                ((((opponent)
                                    and ((charLife <= 0))))
                                or (((!(opponent))
                                    and ((oppLife <= 0)))))){
                                DoSkip = True;
                            };
                        };
                        break;
                    if case(2:
                        strikeVal = (strikeVal - 0.1);
                        DamageAlpha = (DamageAlpha - 0.05);
                        actor[LBL_DAMAGE_INDICATOR].y = (
                            actor[LBL_DAMAGE_INDICATOR].y - 2);
                        if (DamageAlpha <= 0){
                            DamageAlpha = 0;
                            in_strikeAni = False;
                            if (strikeBreak){
                                next_fight_timer.start();
                            };
                            remove(FIGHT_MUSH);
                            StrikeAniTimer.stop();
                            StrikeAniTimer.remove_event_listener(
                                TimerEvent.TIMER,
                                StrikeAniTimerEvent);
                            DoStrikeTimer.start();
                        };
                        break;
                };
                break;
        };
        if (catapultStrike){
            _local3 = actor[FIGHT_MUSH];
            with (_local3) {
                x = ((SCREEN_TITLE_X - 128)
                    + ((230 + (100 * ((
                        (strikePhase > 1))
                            ? (2 - strikeVal)
                            : strikeVal)))
                    * ((opponent) ? -1 : 1)));
                y = ((0 - 265) + (strikeVal * 500));
                scaleY = (((strikeVal >= 0.7))
                    ? (1.7 - strikeVal) : 1);
            };
        } else {
            _local3 = actor[
                ((opponent) ? WEAPON_OPP : WEAPON_CHAR)];
            with (_local3) {
                if (weaponType == 1){
                    if (
                        (((((((opponent)
                            ? oppWeapon
                            : charWeapon) < 0))
                        and ((((opponent)
                            ? oppWeapon
                            : charWeapon) > -4))))
                        or ((((opponent)
                            ? oppWeapon
                            : charWeapon) < -6)))){
                        if (
                            ((opponent)
                                ? oppWeapon
                                : charWeapon) == -1){
                            set_cnt(
                                ((opponent)
                                    ? WEAPON_OPP
                                    : WEAPON_CHAR),
                                (WEAPON_CLAW + int((strikeVal * 3.9);
                        } else {
                            if (
                                ((opponent)
                                    ? oppWeapon
                                    : charWeapon) == -3){
                                set_cnt(
                                    ((opponent)
                                        ? WEAPON_OPP
                                        : WEAPON_CHAR),
                                    (WEAPON_SPLAT
                                        + int((strikeVal * 2.9))));
                            } else {
                                if (
                                    ((opponent)
                                        ? oppWeapon
                                        : charWeapon) == -7){
                                    set_cnt(
                                        ((opponent)
                                            ? WEAPON_OPP
                                            : WEAPON_CHAR),
                                        (WEAPON_FIRE
                                            + int((strikeVal * 2.9))));
                                } else {
                                    set_cnt(
                                        ((opponent)
                                            ? WEAPON_OPP
                                            : WEAPON_CHAR),
                                        (WEAPON_SWOOSH
                                            + int((strikeVal * 2.9))));
                        scaleX = (((opponent) ? 1 : -1) * 1);
                        scaleY = 1;
                        y = (FIGHT_WEAPONS_Y - 240);
                        x = (((SCREEN_TITLE_X
                            + ((opponent) ? 231 : 0)) - 115)
                            + ((((opponent) ? -1 : 1) * 560)
                            * ((((opponent)
                                ? oppFlag
                                : charFlag))==1) ? 0.7 : 1));
                        rotation = (0 * ((opponent) ? -1 : 1));
                        alpha = StrikeAlpha;
                        visible = True;
                    } else {
                        scaleX = (((opponent) ? 1 : -1)
                            * SPRITE_SCALE);
                        scaleY = SPRITE_SCALE;
                        y = (FIGHT_WEAPONS_Y
                            - (math.cos((strikeVal * (TWOPI / 4)))
                                * (75 + ((((opponent) ? oppFlag
                                    : charFlag))==3) ? 75 : 0)));
                        x = (((SCREEN_TITLE_X
                            + ((opponent) ? 231 : 0)) - 115)
                            + (((((opponent) ? -1 : 1) * 230)
                            * strikeVal) * ((((opponent)
                                ? oppFlag : charFlag))==1)
                                    ? 0.7 : 1));
                        rotation = ((280 + (100 * strikeVal))
                            * ((opponent) ? -1 : 1));
                        alpha = StrikeAlpha;
                        visible = True;
                    };
                } else {
                    if (weaponType == 2){
                        scaleX = (((opponent) ? -1 : 1)
                            * SPRITE_SCALE);
                        scaleY = SPRITE_SCALE;
                        y = FIGHT_WEAPONS_Y;
                        x = (SCREEN_TITLE_X
                            + (((opponent) ? 1 : -1) * 170));
                        rotation = (((opponent) ? -1 : 1)
                            * (-30 + (70 * strikeVal)));
                        alpha = StrikeAlpha;
                        visible = True;
                    } else {
                        if (weaponType == 3){
                            scaleX = (((opponent) ? -1 : 1)
                                * SPRITE_SCALE);
                            scaleY = SPRITE_SCALE;
                            y = (FIGHT_WEAPONS_Y - 140);
                            if (strikeVal <= 0.3){
                                x = ((SCREEN_TITLE_X
                                    + (((opponent) ? 1 : -1) * 200))
                                    + (((opponent) ? -1 : 1)
                                        * ((0.3 / strikeVal) * 10)));
                            } else {
                                x = ((SCREEN_TITLE_X
                                    + (((opponent) ? 1 : -1) * 200))
                                    + (((1 - strikeVal)
                                        * math.sin(((strikeVal * 4)
                                            * TWOPI))) * -10));
                            };
                            rotation = ((opponent) ? -42 : 42);
                            alpha = StrikeAlpha;
                            visible = True;

            if (weaponType == 2){
                set_cnt(((opponent) ? BULLET_OPP : BULLET_CHAR),
                    get_arrow_id(0, ((opponent) ? 1 : 0),
                    weapon_data, True, int((random.random() * 3))));
            };
            _local3 = actor[
                ((opponent) ? BULLET_OPP : BULLET_CHAR)];
            with (_local3) {
                if (weaponType == 2){
                    scaleX = ((((opponent) ? -1 : 1)
                        * strikeVal) * 2);
                    scaleY = (strikeVal * 2);
                    y = ((FIGHT_WEAPONS_Y - 70) - (height / 2));
                    x = ((SCREEN_TITLE_X
                        + (((opponent) ? 1 : -1) * 200))
                        + ((((opponent) ? -1 : 1) * 300)
                            * strikeVal));
                    rotation = 0;
                } else {
                    if (weaponType == 3){
                        scaleX = ((opponent) ? -1 : 1);
                        scaleY = 1;
                        y = (FIGHT_WEAPONS_Y - 110);
                        if (strikeVal <= 0.3){
                            x = ((SCREEN_TITLE_X
                                + (((opponent) ? 1 : -1) * 200))
                                + (((opponent) ? -1 : 1)
                                    * ((0.3 / strikeVal) * 10)));
                        } else {
                            x = ((SCREEN_TITLE_X
                                + (((opponent) ? 1 : -1) * 200))
                                + (((((opponent) ? -1 : 1) * 400)
                                    * strikeVal)
                                * ((((opponent)
                                    ? oppFlag : charFlag))==1)
                                        ? 0.7 : 1));
                        };
                        rotation = (
                            ((opponent) ? -1 : 1)
                            * (42 + ((strikeVal - 0.3) * 6)));
                    };
                };
                alpha = BulletAlpha;
                visible = (weaponType >= 2);
            };
            _local3 = actor[
                ((opponent) ? SHIELD_CHAR : SHIELD_OPP)];
            with (_local3) {
                scaleX = (((opponent) ? 1 : -1) * SPRITE_SCALE);
                scaleY = SPRITE_SCALE;
                y = ((FIGHT_WEAPONS_Y
                    - (math.cos((strikeVal * TWOPI)) * 20)) - 20);
                x = (((SCREEN_TITLE_X
                    + ((opponent) ? 0 : 231)) - 115)
                    + ((((opponent) ? -1 : 1) * 50)
                        * (((((strikeVal > 0.9))
                            and ((weaponType == 1))))
                                ? (strikeVal + 0.2) : 1)));
                alpha = ShieldAlpha;
                visible = (
                    ((opponent) ? oppFlag : charFlag) == 1);
            };
        };
        if (damageIndicatorActive){
            _local3 = actor[LBL_DAMAGE_INDICATOR];
            with (_local3) {
                visible = True;
                alpha = DamageAlpha;
                if (((opponent) ? oppFlag : charFlag) == 4){
                    default_text_format = FontFormatCatapultDamage;
                } else {
                    if (((opponent) ? oppFlag : charFlag) == 3){
                        default_text_format =
                             FontFormatCriticalDamage;
                    } else {
                        default_text_format = FontFormatDamage;
                    };
                };
                text = text;
            };
            _local3 = actor[FIGHT_ONO];
            with (_local3) {
                visible = (
                    ((((opponent) ? oppFlag : charFlag) == 0))
                    or ((((opponent) ? oppFlag : charFlag) == 3)));
                Switch (weaponType){
                    if case(1:
                        x = (SCREEN_TITLE_X
                            + (((opponent) ? -1 : 1) * 200));
                        y = (FIGHT_WEAPONS_Y - 20);
                        if (OnoAlpha == 1){
                            scaleX = 0.6;
                            scaleY = 0.6;
                        } else {
                            if (OnoAlpha > 0){
                                scaleX = (scaleX + 0.2);
                                scaleY = (scaleY + 0.2);
                            };
                        };
                        break;
                    if case(2:
                        x = (SCREEN_TITLE_X
                            + (((opponent) ? -1 : 1) * 230));
                        y = (FIGHT_WEAPONS_Y - 40);
                        if (OnoAlpha == 1){
                            scaleX = 0.3;
                            scaleY = 0.3;
                        } else {
                            if (OnoAlpha > 0){
                                scaleX = (scaleX + 0.1);
                                scaleY = (scaleY + 0.1);
                            };
                        };
                        break;
                    if case(3:
                        x = (SCREEN_TITLE_X
                            + (((opponent) ? -1 : 1) * 235));
                        y = (FIGHT_WEAPONS_Y - 42);
                        if (OnoAlpha == 1){
                            scaleX = (0.4 * ((opponent) ? -1 : 1));
                            scaleY = 0.4;
                        } else {
                            if (OnoAlpha > 0){
                                scaleX = (scaleX
                                    + (0.05 * (
                                        (opponent) ? -1 : 1)));
                                scaleY = (scaleY + 0.05);
                            };
                        };
                        break;
                };
                alpha = OnoAlpha;
            };
            if (DoSkip){
                do_skip_fight();
                DoSkip = False;
            };
        };
    };
    StrikeAniTimer = new Timer(40);
    StrikeAlpha = 1;
    BulletAlpha = 0;
    ShieldAlpha = 0;
    DamageAlpha = 0;
    OnoAlpha = 0;
    const SPRITE_SCALE:Number = 1.5;
    const TWOPI:Number = (math.pi * 2);
    strikeVal = 0;
    strikePhase = 0;
    damageIndicatorActive = False;
    weaponType = ((opponent) ? oppWeaponType : charWeaponType);
    onoID = (int((random.random() * 6)) + FIGHT_ONO);
    DoSkip = False;
    catapultStrike = False;
    if (((opponent) ? oppFlag : charFlag) == 4){
        catapultStrike = True;
    } else {
        if (weaponType == 2){
            onoID = get_arrow_id(
                0, ((opponent) ? 1 : 0),
                weapon_data, True, 3);
        } else {
            if (weaponType == 3){
                onoID = FIGHT_ARROW_SMASH;
            };
        };
    };
    StrikeAniTimer.add_event_listener(
        TimerEvent.TIMER, StrikeAniTimerEvent);
    StrikeAniTimer.start();
    in_strikeAni = True;
    '''
    print opponent


def do_show_fight_screen(evt=None):
    '''
    var i:* = 0;
    var DoStrikeTimer:* = None;
    var do_skip_fight:* = None;
    var strikeBreak:* = False;
    var do_strike_event:* = None;
    var evt:* = evt;
    DoStrikeTimer = new Timer(200);
    if (((((is_pvp) and (!(is_replay)))) and (!(is_guildBattle)))){
        if (!waiting_for(savegame[SG_PVP_REROLL_TIME])){
            savegame[SG_PVP_REROLL_TIME] = (
                int((game_time.getTime() / 1000)) + (70 * 60));
        };
    };
    if (is_guildBattle){
        remove_all();
        if (tower_fight_mode){
            add(SCR_TOWER_BG);
        } else {
            if (isRaid){
                add(GUILD_RAID_BG);
            } else {
                add(GUILD_BATTLE_BG);
            };
        };
        if (tower_fight_mode){
            add(LBL_HERO_OF_THE_DAY_TITLE);
            actor[LBL_HERO_OF_THE_DAY_TITLE].text = texts[
                TXT_TOWER_LEVEL].split(
                    "%1").join(str((tower_level + 1)));
            actor[LBL_HERO_OF_THE_DAY_TITLE].x = (
                SCREEN_TITLE_X -
                (actor[LBL_HERO_OF_THE_DAY_TITLE].width / 2));
        } else {
            if (((isRaid) and (texts[TXT_DUNGEON_NAMES]))){
                add(LBL_HERO_OF_THE_DAY_TITLE);
                actor[LBL_HERO_OF_THE_DAY_TITLE].text = texts[
                    ((TXT_DUNGEON_NAMES + raid_level) - 1)];
                actor[LBL_HERO_OF_THE_DAY_TITLE].x = (
                    SCREEN_TITLE_X
                    - (actor[LBL_HERO_OF_THE_DAY_TITLE].width / 2));
            } else {
                if (((!(isRaid)) and (texts[TXT_FIGHTS_COUNTER]))){
                    add(LBL_HERO_OF_THE_DAY_TITLE);
                    actor[LBL_HERO_OF_THE_DAY_TITLE].text = texts[
                        TXT_FIGHTS_COUNTER].split(
                            "%1").join(str(fightNumber)).split(
                            "%2").join(str(guild_fight_count));
                    actor[LBL_HERO_OF_THE_DAY_TITLE].x = (
                        SCREEN_TITLE_X - (
                            actor[LBL_HERO_OF_THE_DAY_TITLE].width / 2));
                };
            };
        };
    } else {
        if (on_stage(QUESTBAR_BG)){
            remove(
                QUESTBAR_BG,
                QUESTBAR_FILL,
                QUESTBAR_LIGHT,
                LBL_QUESTBAR_TEXT,
                QUEST_CANCEL,
                QUEST_SKIP,
                LBL_SCREEN_TITLE
            );
        } else {
            if (is_pvp){
                remove_all();
                Switch (tz){
                    if case(0:
                        add(SCREEN_ARENA_NIGHT);
                        break;
                    if case(1:
                        add(SCREEN_ARENA_DAWN);
                        break;
                    if case(2:
                        add(SCREEN_ARENA_DAY);
                        break;
                };
            } else {
                remove_all();
                if (is_mq){
                    if (SelectedDungeon == 100){
                        add(SCR_TOWER_BG);
                    } else {
                        add(((SCR_QUEST_BG_1 + 50) + SelectedDungeon));
                    };
                } else {
                    if (int(savegame[SG_ACTION_STATUS]) == 2){
                        add(get_quest_bg());

    set_cnt(LIFEBAR_OPP, LIFEBAR_CHAR);
    set_cnt(LIFEBAR_FILL_OPP, LIFEBAR_FILL_CHAR);
    set_cnt(FIGHT_OPP_BORDER, FIGHT_CHAR_BORDER);
    set_cnt(FIGHT_BOX3, FIGHT_BOX1);
    set_cnt(FIGHT_REWARDGOLD, IF_GOLD);
    set_cnt(FIGHT_REWARDSILVER, IF_SILBER);
    set_cnt(FIGHT_REWARDMUSH, IF_PILZE);
    var _local3 = actor[LBL_NAMERANK_CHAR];
    with (_local3) {
        if (text_dir == "right"){
            text = ((((("(" + str(charLevel)) + " ")
                + texts[TXT_HALL_LIST_COLUMN_4]) + ") ")
                + thisCharName);
        } else {
            text = (((((thisCharName + " (")
                + texts[TXT_HALL_LIST_COLUMN_4]) + " ")
                + str(charLevel)) + ")");
        };
        x = ((FIGHT_CHARX + 150) - int((text_width / 2)));
        y = ((OPPY + 290) - textHeight);
    };
    _local3 = actor[LBL_NAMERANK_OPP];
    with (_local3) {
        if (text_dir == "right"){
            text = ((((("(" + str(oppLevel)) + " ")
                + texts[TXT_HALL_LIST_COLUMN_4]) + ") ") + opp_name);
        } else {
            text = (((((opp_name + " (")
                + texts[TXT_HALL_LIST_COLUMN_4]) + " ")
                + str(oppLevel)) + ")");
        };
        x = ((OPPX + 150) - int((text_width / 2)));
        y = ((OPPY + 290) - textHeight);
    };
    i = 0;
    while (i < 10) {
        _local3 = actor[(CHARBACKGROUND + i)];
        with (_local3) {
            x = (FIGHT_CHARX + 300);
            y = OPPY;
            scaleX = -1;
            scaleY = 1;
        };
        _local3 = actor[(CHARBACKGROUND2 + i)];
        with (_local3) {
            x = (FIGHT_CHARX + 300);
            y = OPPY;
            scaleX = -1;
            scaleY = 1;
        };
        i = (i + 1);
    };
    add(SCREEN_FIGHT);
    if (oppMonster > 0){
        add(((OPPMONSTER + oppMonster) - 1));
    } else {
        load_character_image(
            ((alternate_char_opp_img)
                ? OPPBACKGROUND2
                : OPPBACKGROUND),
                 False, oppVolk, oppMann,
                 oppKaste, oppMouth, oppBeard,
                 oppNose, oppEyes, oppBrows,
                 oppEars, oppHair, oppSpecial,
                 oppSpecial2);
    };
    if ((((thisCharMonster >= 391)) and ((thisCharMonster <= 393)))){
        add(((FIGHT_COPYCAT + thisCharMonster) - 391));
    } else {
        load_character_image(
            ((alternate_char_opp_img)
                ? CHARBACKGROUND2
                : CHARBACKGROUND),
                False, thischar_volk, thischar_male, thischar_class,
                thischar_mouth, thischar_beard, thischar_nose,
                thischar_eyes, thischar_brows, thischar_ears,
                thischar_hair, thischar_special, thischar_special2);
    };
    if (is_guildBattle){
        alternate_char_opp_img = !(alternate_char_opp_img);
    };
    add_some(LBL_NAMERANK_CHAR, LBL_NAMERANK_OPP);
    add_some(
        SHIELD_CHAR, SHIELD_OPP, WEAPON_CHAR,
        WEAPON_OPP, BULLET_CHAR, BULLET_OPP);
    hide(
        SHIELD_CHAR, SHIELD_OPP, WEAPON_CHAR,
        WEAPON_OPP, BULLET_CHAR, BULLET_OPP);
    add_some(LBL_DAMAGE_INDICATOR, FIGHT_ONO);
    hide(LBL_DAMAGE_INDICATOR, FIGHT_ONO);
    actor[FIGHT_SKIP].add_event_listener(MouseEvent.CLICK, do_skip_fight);
    actor[BATTLE_SKIP].add_event_listener(MouseEvent.CLICK, do_skip_fight);
    actor[BATTLE_SKIPONE].add_event_listener(MouseEvent.CLICK, do_skip_fight);
    if (is_guildBattle){
        add(BATTLE_SKIP);
        add(BATTLE_SKIPONE);
        remove(FIGHT_SKIP);
        if (!tower_fight_mode){
            add(LBL_FIGHT_PLAYERGUILD);
            add(LBL_FIGHT_OPPGUILD);
        };
        _local3 = actor[LBL_FIGHT_PLAYERGUILD];
        with (_local3) {
            if (tower_fight_mode){
                text = texts[TXT_TOWER_GUYS];
            } else {
                text = own_guild;
            };
            x = ((FIGHT_CHARX + 150) - (text_width / 2));
        };
        _local3 = actor[LBL_FIGHT_OPPGUILD];
        with (_local3) {
            if (tower_fight_mode){
                text = texts[TXT_TOWER_LEVEL].split(
                    "%1").join(str((tower_level + 1)));
            } else {
                text = opp_guild;
            };
            x = ((OPPX + 150) - (text_width / 2));
        };
    };
    set_life_bars();
    i = 0;
    while (i < 5) {
        if (is_guildBattle){
            actor[(LBL_FIGHT_CHAR_STAERKE + i)].text = "";
            actor[(LBL_FIGHT_OPP_STAERKE + i)].text = "";
            if (((tower_fight_mode)
                and (!((int(guild_battle_data[(i + 1)]) == 0))))){
                actor[(LBL_FIGHT_CHAR_STAERKE_CAPTION + i)].text = texts[
                    ((TXT_COPYCAT_NAME
                        + int(guild_battle_data[(i + 1)])) - 1)];
            } else {
                actor[(LBL_FIGHT_CHAR_STAERKE_CAPTION + i)].text = str(
                    guild_battle_data[(i + 1)]);
            };
            if (tower_fight_mode){
                actor[(LBL_FIGHT_OPP_STAERKE + i)].text = str(
                    fighter_data[(i + 7)]);
                actor[(LBL_FIGHT_OPP_STAERKE_CAPTION + i)].text = texts[
                    (TXT_CHAR_STAERKE + i)];
            } else {
                if (int(guild_battle_data[(i + 7)]) != 0){
                    if (-(int(guild_battle_data[(i + 7)])) >= 400){
                        actor[
                            (LBL_FIGHT_OPP_STAERKE_CAPTION + i)
                        ].text = texts[
                            ((TXT_TOWER_enemy_NAMES +
                            -(int(guild_battle_data[(i + 7)]))) - 400)
                        ].split("|")[0];
                    } else {
                        if (-(int(guild_battle_data[(i + 7)])) > 220){
                            actor[
                                (LBL_FIGHT_OPP_STAERKE_CAPTION + i)
                            ].text = texts[
                                ((TXT_NEW_MONSTER_NAMES
                                    + -(int(guild_battle_data[(
                                        i + 7)]))) - 221)];
                        } else {
                            actor[
                                (LBL_FIGHT_OPP_STAERKE_CAPTION + i)
                            ].text = texts[
                                ((TXT_MONSTER_NAME
                                    + -(int(guild_battle_data[(i + 7)])))
                                    - 1)];
                        };
                    };
                } else {
                    actor[(LBL_FIGHT_OPP_STAERKE_CAPTION + i)].text = str(
                        guild_battle_data[(i + 7)]);
                };
            };
        } else {
            actor[(LBL_FIGHT_CHAR_STAERKE + i)].text = str(
                fighter_data[(i + 1)]);
            actor[(LBL_FIGHT_OPP_STAERKE + i)].text = str(
                fighter_data[(i + 7)]);
            actor[(LBL_FIGHT_CHAR_STAERKE_CAPTION + i)].text = texts[
                (TXT_CHAR_STAERKE + i)];
            actor[(LBL_FIGHT_OPP_STAERKE_CAPTION + i)].text = texts[
                (TXT_CHAR_STAERKE + i)];
        };
        i = (i + 1);
    };
    if (text_dir == "right"){
        i = 0;
        while (i < 5) {
            actor[(LBL_FIGHT_CHAR_STAERKE_CAPTION + i)].x = (
                (FIGHT_CHAR_PROP_COLUMN_2_X + 30)
                - actor[(LBL_FIGHT_CHAR_STAERKE_CAPTION + i)].text_width);
            actor[(LBL_FIGHT_OPP_STAERKE_CAPTION + i)].x = (
                (FIGHT_CHAR_PROP_COLUMN_4_X + 30)
                - actor[(LBL_FIGHT_OPP_STAERKE_CAPTION + i)].text_width);
            actor[(LBL_FIGHT_CHAR_STAERKE + i)].x = (
                (FIGHT_CHAR_PROP_COLUMN_1_X + 40)
                - actor[(LBL_FIGHT_CHAR_STAERKE + i)].text_width);
            actor[(LBL_FIGHT_OPP_STAERKE + i)].x = (
                (FIGHT_CHAR_PROP_COLUMN_3_X + 40)
                - actor[(LBL_FIGHT_OPP_STAERKE + i)].text_width);
            i = (i + 1);
        };
    };
    strikeBreak = False;
    var in_strikeAni:* = False;
    DoStrikeTimer.add_event_listener(TimerEvent.TIMER, do_strike_event);
    DoStrikeTimer.start();
    '''
    print evt


def show_fight_screen(fighter_data, fight_data, get_pilz, face_data, is_pvp,
                      weapon_data, honor_gain, gold_gain, is_mq,
                      is_replay=False, back_pack_slot=-1,
                      guild_battle_data=None, last_fight=False,
                      guild_fight_exp=0, guild_fight_honor=0, own_guild="",
                      opp_guild="", raid_level=0):
    '''
    var is_guildBattle:* = False;
    var charWeapon:* = 0;
    var oppWeapon:* = 0;
    var charHasWeapon:* = False;
    var oppHasWeapon:* = False;
    var charWeaponType:* = 0;
    var oppWeaponType:* = 0;
    var tz:* = 0;
    var charShield:* = 0;
    var oppShield:* = 0;
    var i:* = 0;
    var oppVolk:* = 0;
    var oppMann:* = False;
    var oppKaste:* = 0;
    var thischar_volk:* = 0;
    var thischar_male:* = False;
    var thischar_class:* = 0;
    var thischar_mouth:* = None;
    var thischar_beard:* = None;
    var thischar_nose:* = None;
    var thischar_eyes:* = None;
    var thischar_brows:* = None;
    var thischar_ears:* = None;
    var thischar_hair:* = None;
    var thischar_special:* = None;
    var thischar_special2:* = None;
    var thisCharMonster:* = 0;
    var oppMouth:* = 0;
    var oppBeard:* = 0;
    var oppNose:* = 0;
    var oppEyes:* = 0;
    var oppBrows:* = 0;
    var oppEars:* = 0;
    var oppHair:* = 0;
    var oppSpecial:* = 0;
    var oppSpecial2:* = 0;
    var oppMonster:* = 0;
    var opp_name:* = None;
    var thisCharName:* = None;
    var charFullLife:* = 0;
    var oppFullLife:* = 0;
    var charLife:* = 0;
    var charDamage:* = 0;
    var oppLife:* = 0;
    var charFlag:* = 0;
    var oppFlag:* = 0;
    var fightRound:* = 0;
    var oppStrike:* = False;
    var isRaid:* = False;
    var do_show_fight_screen:* = None;
    var fighter_data:* = fighter_data;
    var fight_data:* = fight_data;
    var get_pilz:* = get_pilz;
    var face_data:* = face_data;
    var is_pvp:* = is_pvp;
    var weapon_data:* = weapon_data;
    var honor_gain:* = honor_gain;
    var gold_gain:* = gold_gain;
    var is_mq:* = is_mq;
    var is_replay:Boolean = is_replay;
    var back_pack_slot = back_pack_slot;
    var guild_battle_data:* = guild_battle_data;
    var last_fight:Boolean = last_fight;
    var guild_fight_exp = guild_fight_exp;
    var guild_fight_honor = guild_fight_honor;
    var own_guild:String = own_guild;
    var opp_guild:String = opp_guild;
    var raid_level = raid_level;

    is_guildBattle = False;
    if (guild_battle_data){
        is_guildBattle = True;
    };
    hasFoughtGuildBattle = is_guildBattle;
    charWeapon = weapon_data[SG['ITM']['PIC']];
    oppWeapon = weapon_data[(SG['ITM']['SIZE'] + SG['ITM']['PIC'])];
    charHasWeapon = (
        ((int(weapon_data[SG_ITM_TYP]) > 0))
        and ((int(weapon_data[SG['ITM']['PIC']]) > 0)));
    oppHasWeapon = (
        ((int(weapon_data[(SG['ITM']['SIZE'] + SG_ITM_TYP)]) > 0))
        and ((int(weapon_data[(SG['ITM']['SIZE'] + SG['ITM']['PIC'])]) > 0)));
    charWeaponType = 1;
    oppWeaponType = 1;
    tz = tageszeit();
    hasLostMQ = False;
    actor[LBL['ERROR']].text = "";
    if (is_guildBattle){
        remove(GILDE_CHAT);
    };
    Switch (tz){
        if case(0:
            load(SCREEN_ARENA_NIGHT);
            break;
        if case(1:
            load(SCREEN_ARENA_DAWN);
            break;
        if case(2:
            load(SCREEN_ARENA_DAY);
            break;
    };
    while (charWeapon > 1000) {
        charWeapon = (charWeapon - 1000);
        charWeaponType = (charWeaponType + 1);
    };
    while (oppWeapon > 1000) {
        oppWeapon = (oppWeapon - 1000);
        oppWeaponType = (oppWeaponType + 1);
    };
    charShield = (int(weapon_data[((SG['ITM']['SIZE'] * 2)
                  + SG['ITM']['PIC'])])
        * (((int(weapon_data[((SG['ITM']['SIZE'] * 2)
            + SG_ITM_TYP)]) == 0)) ? 0 : 1));
    oppShield = (weapon_data[((SG['ITM']['SIZE'] * 3) + SG['ITM']['PIC'])]
        * (((int(weapon_data[((SG['ITM']['SIZE'] * 3)
            + SG_ITM_TYP)]) == 0)) ? 0 : 1));
    if (charHasWeapon){
        load(get_weapon_sound(charWeaponType, charWeapon, 0));
        load(get_weapon_sound(charWeaponType, charWeapon, 1));
        if (((!((charWeaponType == 2))) and (!((oppShield == 0))))){
            load(get_weapon_sound(charWeaponType, charWeapon, 2));
        };
        load(get_weapon_sound(charWeaponType, charWeapon, 3));
    };
    if (oppHasWeapon){
        load(get_weapon_sound(oppWeaponType, oppWeapon, 0));
        load(get_weapon_sound(oppWeaponType, oppWeapon, 1));
        if (((!((oppWeaponType == 2))) and (!((charShield == 0))))){
            load(get_weapon_sound(oppWeaponType, oppWeapon, 2));
        };
        load(get_weapon_sound(oppWeaponType, oppWeapon, 3));
    } else {
        if (oppWeapon == -1){
            load(WEAPON_CLAW, WEAPON_CLAW2, WEAPON_CLAW3, WEAPON_CLAW4);
        } else {
            if (oppWeapon == -3){
                load(WEAPON_SPLAT, WEAPON_SPLAT2, WEAPON_SPLAT3);
            } else {
                if (oppWeapon == -4){
                    load(WEAPON_STICK);
                } else {
                    if (oppWeapon == -5){
                        load(WEAPON_BONE);
                    } else {
                        if (oppWeapon == -6){
                            load(WEAPON_STONEFIST);
                        } else {
                            if (oppWeapon == -7){
                                load(
                                    WEAPON_FIRE,
                                    WEAPON_FIRE2,
                                    WEAPON_FIRE3
                                );
                            } else {
                                if (oppWeapon == -2){
                                    load(
                                        WEAPON_SWOOSH,
                                        WEAPON_SWOOSH2,
                                        WEAPON_SWOOSH3
                                    );
    };
    i = 0;
    while (i < 6) {
        load((FIGHT_ONO + i));
        i = (i + 1);
    };
    if ((((charWeaponType == 3)) or ((oppWeaponType == 3)))){
        load(FIGHT_ARROW_SMASH);
    };
    load(SCREEN_FIGHT);
    if (int(savegame[SG_ACTION_STATUS]) == 2){
        load(get_quest_bg());
    };
    if (!charHasWeapon){
        charWeapon = int(weapon_data[SG_ITM_TYP]);
        load(get_weapon_sound(charWeaponType, charWeapon, 0));
        load(get_weapon_sound(charWeaponType, charWeapon, 1));
        if (((!((charWeaponType == 2))) and (!((oppShield == 0))))){
            load(get_weapon_sound(charWeaponType, charWeapon, 2));
        };
        load(get_weapon_sound(charWeaponType, charWeapon, 3));
        set_cnt(
            WEAPON_CHAR,
            (((charWeapon == 0))
                ? WEAPON_FIST
                : (((charWeapon == -1))
                    ? WEAPON_CLAW
                    : WEAPON_SWOOSH)), -30, -30, True);
        set_cnt(BULLET_CHAR, C_EMPTY);
        charWeaponType = 1;
    } else {
        if (charWeaponType == 1){
            set_cnt(
                WEAPON_CHAR,
                GetItemID(0, 0, weapon_data),
                -30, -30, True);
            set_cnt(BULLET_CHAR, C_EMPTY);
        } else {
            if (charWeaponType == 2){
                set_cnt(
                    WEAPON_CHAR,
                    GetItemID(0, 0, weapon_data),
                    30, -30, True);
                set_cnt(
                    BULLET_CHAR, get_arrow_id(
                        0, 0, weapon_data, True, 0));
                load(get_arrow_id(
                    0, 0, weapon_data, True, 1),
                    get_arrow_id(
                        0, 0, weapon_data, True, 2),
                    get_arrow_id(0, 0, weapon_data, True, 3));
            } else {
                if (charWeaponType == 3){
                    set_cnt(
                        WEAPON_CHAR,
                        GetItemID(0, 0, weapon_data));
                    set_cnt(
                        BULLET_CHAR,
                        get_arrow_id(0, 0, weapon_data, True));
                };
            };
        };
    };
    if (!oppHasWeapon){
        oppWeapon = int(weapon_data[(SG['ITM']['SIZE'] + SG_ITM_TYP)]);
        load(get_weapon_sound(oppWeaponType, oppWeapon, 0));
        load(get_weapon_sound(oppWeaponType, oppWeapon, 1));
        if (((!((oppWeaponType == 2))) and (!((charShield == 0))))){
            load(get_weapon_sound(oppWeaponType, oppWeapon, 2));
        };
        load(get_weapon_sound(oppWeaponType, oppWeapon, 3));
        if (oppWeapon == -4){
            set_cnt(WEAPON_OPP, WEAPON_STICK, -30, -30, True);
        } else {
            if (oppWeapon == -5){
                set_cnt(WEAPON_OPP, WEAPON_BONE, -30, -30, True);
            } else {
                if (oppWeapon == -6){
                    set_cnt(WEAPON_OPP, WEAPON_STONEFIST, -30, -30, True);
                } else {
                    set_cnt(
                        WEAPON_OPP,
                        (((oppWeapon == 0)) ? WEAPON_FIST : C_EMPTY),
                         -30, -30, True);
                };
            };
        };
        set_cnt(BULLET_OPP, C_EMPTY);
        oppWeaponType = 1;
    } else {
        if (oppWeaponType == 1){
            set_cnt(WEAPON_OPP, GetItemID(0, 1, weapon_data), -30, -30, True);
            set_cnt(BULLET_OPP, C_EMPTY);
        } else {
            if (oppWeaponType == 2){
                set_cnt(WEAPON_OPP,
                       GetItemID(0, 1, weapon_data),
                       30, -30, True)
                set_cnt(BULLET_OPP, get_arrow_id(0, 1, weapon_data, True, 0));
                load(
                    get_arrow_id(0, 1, weapon_data, True, 1),
                    get_arrow_id(0, 1, weapon_data, True, 2),
                    get_arrow_id(0, 1, weapon_data, True, 3));
            } else {
                if (oppWeaponType == 3){
                    set_cnt(WEAPON_OPP, GetItemID(0, 1, weapon_data));
                    set_cnt(BULLET_OPP, get_arrow_id(0, 1, weapon_data, True));
                };
            };
        };
    };
    if (charShield > 0){
        set_cnt(SHIELD_CHAR, GetItemID(0, 2, weapon_data), 0, 0, True);
    } else {
        set_cnt(SHIELD_CHAR, C_EMPTY);
    };
    if (oppShield > 0){
        set_cnt(SHIELD_OPP, GetItemID(0, 3, weapon_data), 0, 0, True);
    } else {
        set_cnt(SHIELD_OPP, C_EMPTY);
    };
    oppVolk = int(face_data[17]);
    oppMann = (int(face_data[18]) == 1);
    oppKaste = int(face_data[19]);
    thischar_volk = int(face_data[2]);
    thischar_male = (int(face_data[3]) == 1);
    thischar_class = int(face_data[4]);
    thischar_mouth = int(face_data[5]);
    thischar_beard = int(face_data[9]);
    thischar_nose = int(face_data[10]);
    thischar_eyes = int(face_data[8]);
    thischar_brows = int(face_data[7]);
    thischar_ears = int(face_data[11]);
    thischar_hair = int(face_data[6]);
    thischar_special = int(face_data[12]);
    thischar_special2 = int(face_data[13]);
    thisCharMonster = ((int(face_data[5]))<0) ? -(int(face_data[5])) : 0;
    oppMouth = int(face_data[20]);
    oppBeard = int(face_data[24]);
    oppNose = int(face_data[25]);
    oppEyes = int(face_data[23]);
    oppBrows = int(face_data[22]);
    oppEars = int(face_data[26]);
    oppHair = int(face_data[21]);
    oppSpecial = int(face_data[27]);
    oppSpecial2 = int(face_data[28]);
    var oppLevel:* = int(face_data[16]);
    oppMonster = ((int(face_data[20]))<0) ? -(int(face_data[20])) : 0;
    opp_name = "";
    if (oppMonster > 0){
        if (oppMonster >= 400){
            opp_name = texts[
                ((TXT_TOWER_enemy_NAMES + oppMonster) - 400)
            ].split("|")[0];
        } else {
            if (oppMonster > 220){
                opp_name = texts[
                    ((TXT_NEW_MONSTER_NAMES + oppMonster) - 221)];
            } else {
                opp_name = texts[((TXT_MONSTER_NAME + oppMonster) - 1)];
            };
        };
    } else {
        opp_name = face_data[15];
        if (!is_guildBattle){
            add_suggest_names(opp_name);
        };
    };
    thisCharName = (
        ((face_data[0] == ""))
            ? actor[INP['NAME']].getChildAt(1).text
            : face_data[0]);
    if (((is_guildBattle) and (tower_fight_mode))){
        if (thisCharMonster >= 391){
            thisCharName = texts[
                ((TXT_COPYCAT_NAME + thisCharMonster) - 391)];
        };
    };
    charFullLife = fighter_data[0];
    oppFullLife = fighter_data[6];
    charLife = (
        (is_guildBattle)
            ? (((int(guild_battle_data[0]) < 0))
                ? (charFullLife / -(int(guild_battle_data[0])))
                : int(guild_battle_data[0]))
            : charFullLife);
    charDamage = 0;
    oppLife = (
        (is_guildBattle)
            ? (((int(guild_battle_data[6]) < 0))
                ? (oppFullLife / -(int(guild_battle_data[6])))
                : int(guild_battle_data[6]))
            : oppFullLife);
    var oppDamage:* = 0;
    charFlag = 0;
    oppFlag = 0;
    fightRound = 0;
    oppStrike = False;
    var charLevel:* = int(face_data[(16 - 15)]);
    isRaid = False;
    if (!is_guildBattle){
        alternate_char_opp_img = False;
    };
    if (((is_guildBattle) and ((own_guild == "")))){
        isRaid = True;
    };
    if (oppMonster > 0){
        load(((OPPMONSTER + oppMonster) - 1));
    } else {
        load_character_image(
            ((alternate_char_opp_img)
                ? OPPBACKGROUND2
                : OPPBACKGROUND),
            True, oppVolk, oppMann, oppKaste, oppMouth,
            oppBeard, oppNose, oppEyes, oppBrows, oppEars,
            oppHair, oppSpecial, oppSpecial2);
    };
    if ((((thisCharMonster >= 391)) and ((thisCharMonster <= 393)))){
        load(((FIGHT_COPYCAT + thisCharMonster) - 391));
    } else {
        load_character_image(
            ((alternate_char_opp_img)
                ? CHARBACKGROUND2
                : CHARBACKGROUND), True,
            thischar_volk, thischar_male, thischar_class, thischar_mouth,
            thischar_beard, thischar_nose, thischar_eyes, thischar_brows,
            thischar_ears, thischar_hair, thischar_special, thischar_special2);
    };
    if (is_guildBattle){
        if (tower_fight_mode){
            load(SCR_TOWER_BG);
        } else {
            if (isRaid){
                load(GUILD_RAID_BG);
            } else {
                load(GUILD_BATTLE_BG);
            };
        };
    };
    when_loaded(do_show_fight_screen);
    '''
    print fighter_data, fight_data, get_pilz, face_data, is_pvp, weapon_data
    print honor_gain, gold_gain, is_mq, is_replay, back_pack_slot,
    print guild_battle_data, last_fight, guild_fight_exp, guild_fight_honor,
    print own_guild, opp_guild, raid_level


def show_email_nag_screen(val_mode=-1):
    '''
    var doShowEmailNagScreen:* = None;
    var val_mode = val_mode;
    doShowEmailNagScreen = function (){
        remove_all();
        actor[LBL_EMAIL_RESEND].htmlText = texts[TXT_EMAIL_RESEND];
        arabize(LBL_EMAIL_RESEND);
        var _local2 = actor[LBL_WINDOW_TITLE];
        with (_local2) {
            text = texts[
                (((val_mode == 1))
                    ? TXT_VALIDATE_OK_TITLE
                    : (((val_mode == 2))
                        ? TXT_VALIDATE_ERR_TITLE
                        : (((val_mode == 3))
                            ? TXT_VALIDATE_UNN_TITLE
                            : TXT_EMAIL_NAG_TITLE)))];
            x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((text_width / 2)));
        };
        _local2 = actor[LBL_EMAIL_NAG];
        with (_local2) {
            htmlText = texts[
                (((val_mode == 1))
                    ? TXT_VALIDATE_OK
                    : (((val_mode == 2))
                        ? TXT_VALIDATE_ERR
                        : (((val_mode == 3))
                            ? TXT_VALIDATE_UNN
                            : TXT_EMAIL_NAG)))];
        };
        arabize(LBL_EMAIL_NAG);
        add(SCREEN_EMAIL_NAG);
        if (val_mode == -1){
            add(EMAIL_RESEND);
        };
    };
    load(SCREEN_EMAIL_NAG);
    when_loaded(doShowEmailNagScreen);
    '''
    print val_mode


def show_disconnect_screen():
    '''
    var ReconnectTimer:* = None;
    var TryReconnect:* = None;
    TryReconnect = function (evt:TimerEvent){
        ReconnectTimer.delay = (
            param_reconnect * interval_multiplier_reconnect);
        if (on_stage(LBL_DISCONNECTED)){
            request_login();
        } else {
            ReconnectTimer.remove_event_listener(
                TimerEvent.TIMER, TryReconnect);
        };
    };
    if (on_stage(LBL_DISCONNECTED)){
        return;
    };
    remove_all();
    remove(IF_LOGOUT);
    add(SCREEN_DISCONNECTED);
    session_id = "";
    ReconnectTimer = new Timer(param_reconnect);
    ReconnectTimer.add_event_listener(TimerEvent.TIMER, TryReconnect);
    ReconnectTimer.start();
    '''
    pass


def show_quest_screen(evt=None):
    '''
    var DoShowQuestScreen:* = None;
    var evt:* = evt;
    DoShowQuestScreen = function (evt:Event=None){
        var questBarTimer:* = None;
        var QuestBarUpdate:* = None;
        var evt:* = evt;
        QuestBarUpdate = function (evt:TimerEvent=None){
            var evt:* = evt;
            if (!on_stage(QUESTBAR_BG)){
                questBarTimer.stop();
                questBarTimer.remove_event_listener(
                    TimerEvent.TIMER, QuestBarUpdate);
                set_title_bar(waiting_time(savegame[SG_ACTION_ENDTIME]));
                return;
            };
            if (waiting_for(savegame[SG_ACTION_ENDTIME])){
                var _local3 = actor[QUESTBAR_FILL];
                with (_local3) {
                    width = (waiting_progress(
                        (savegame[SG_ACTION_ENDTIME]
                            - savegame[(SG_QUEST_OFFER_DURATION1
                                + (savegame[SG_ACTION_INDEX] - 1))]),
                            savegame[SG_ACTION_ENDTIME]) * 555);
                    actor[QUESTBAR_LIGHT].x = ((x + width) - 5);
                };
                _local3 = actor[LBL_QUESTBAR_TEXT];
                with (_local3) {
                    text = waiting_time(savegame[SG_ACTION_ENDTIME]);
                    set_title_bar(text);
                    x = int((QUESTBAR_LABEL_X - (text_width / 2)));
                };
            } else {
                questBarTimer.stop();
                questBarTimer.remove_event_listener(
                    TimerEvent.TIMER, QuestBarUpdate);
                send_action(ACT_SCREEN_TAVERNE);
            };
        };
        questBarTimer = new Timer(200);
        remove_all();
        add(get_quest_bg());
        add(SCREEN_QUEST);
        var _local3 = actor[LBL_SCREEN_TITLE];
        with (_local3) {
            text = get_quest_title((int(savegame[SG_ACTION_INDEX]) - 1));
            x = (SCREEN_TITLE_X - int((text_width / 2)));
            y = SCREEN_TITLE_Y_QUEST;
        };
        actor[QUESTBAR_FILL].width = 0;
        actor[QUESTBAR_LIGHT].x = (actor[QUESTBAR_FILL].x - 5);
        questBarTimer.add_event_listener(TimerEvent.TIMER, QuestBarUpdate);
        questBarTimer.start();
        QuestBarUpdate();
        if (skip_allowed){
            actor[QUEST_CANCEL].x = int((QUEST_CANCEL_X + 5));
            show(QUEST_SKIP);
        } else {
            actor[QUEST_CANCEL].x = int(
                (QUEST_CANCEL_X - (actor[QUEST_CANCEL].width / 2)));
            hide(QUEST_SKIP);
        };
        check_wrong_page(ACT_SCREEN_TAVERNE);
        try_show_tv();
    };
    load(SCREEN_QUEST);
    load(get_quest_bg());
    if (text_dir == "right"){
        set_btn_text(QUEST_SKIP, ("~P " + texts[TXT_SKIP_FIGHT]));
    };
    when_loaded(DoShowQuestScreen);
    '''
    print evt


def show_taverne_screen(evt=None):
    '''
    var DoShowTaverneScreen:* = None;
    var evt:* = evt;
    DoShowTaverneScreen = function (evt:Event=None){
        var i:* = 0;
        var quest_type:* = 0;
        var HutBlinzelTimer:* = None;
        var HutBlinzelStep:* = 0;
        var BarkeeperStep:* = 0;
        var HutBlinzelTimerEvent:* = None;
        var evt:* = evt;
        HutBlinzelTimerEvent = function (evt:TimerEvent){
            if (on_stage(TAVERNE_BG)){
                HutBlinzelStep++;
                if (HutBlinzelStep > 70){
                    hide(TAVERNE_HUTMANN_BLINZELN);
                    HutBlinzelStep = int((random.random() * 30));
                } else {
                    if (HutBlinzelStep > 68){
                        show(TAVERNE_HUTMANN_BLINZELN);
                    };
                };
                BarkeeperStep++;
                if (BarkeeperStep >= 12){
                    hide(TAVERNE_BARKEEPER1);
                    hide(TAVERNE_BARKEEPER2);
                    BarkeeperStep = 0;
                } else {
                    if (BarkeeperStep >= 9){
                        show(TAVERNE_BARKEEPER1);
                        hide(TAVERNE_BARKEEPER2);
                    } else {
                        if (BarkeeperStep >= 6){
                            hide(TAVERNE_BARKEEPER1);
                            show(TAVERNE_BARKEEPER2);
                        } else {
                            if (BarkeeperStep >= 3){
                                show(TAVERNE_BARKEEPER1);
                                hide(TAVERNE_BARKEEPER2);
                            } else {
                                hide(TAVERNE_BARKEEPER1);
                                hide(TAVERNE_BARKEEPER2);
                            };
                        };
                    };
                };
                actor[TAVERNE_KERZEN].visible = (random.random() >= 0.5);
            } else {
                HutBlinzelTimer.stop();
                HutBlinzelTimer.remove_event_listener(
                    TimerEvent.TIMER, HutBlinzelTimerEvent);
            };
        };
        quest_type = get_quest_random(0, 5);
        HutBlinzelTimer = new Timer(50);
        HutBlinzelStep = 0;
        BarkeeperStep = 0;
        set_cnt(TIMEBAR_FILL, TIMEBAR_FILL);
        set_cnt(QO_REWARDGOLD, IF_GOLD);
        set_cnt(QO_REWARDSILVER, IF_SILBER);
        remove_all();
        add(SCREEN_TAVERNE);
        if (get_advent() != 0){
            add(((TAVERN_ADVENT + get_advent()) - 1));
        };
        if (beer_fest){
            add(BEERFEST);
            i = 0;
            while (i < 4) {
                add((TV + i));
                i = (i + 1);
            };
            add(CA_TV);
        };
        if (special_action > 0){
            add(((SPECIAL_ACTION + special_action) - 1));
            actor[
                ((SPECIAL_ACTION + special_action) - 1)
            ].mouse_enabled = False;
            if (!special_actionHint){
                add(TAVERNE_BARKEEPER_HINT);
                actor[TAVERNE_BARKEEPER_HINT].mouse_enabled = False;
                animate_ach(
                    TAVERNE_BARKEEPER_HINT,
                    ((100 + TAVERNE_BARKEEPER_Y) - 215));
            };
            i = 0;
            while (i < 4) {
                add((TV + i));
                i = (i + 1);
            };
            add(CA_TV);
        };
        refresh_time_bar();
        check_wrong_page(ACT_SCREEN_TAVERNE);
        hide(TAVERNE_HUTMANN_BLINZELN);
        hide(TAVERNE_BARKEEPER1);
        hide(TAVERNE_BARKEEPER2);
        i = 0;
        while (i < 5) {
            actor[(TAVERNE_QUEST1 + i)].visible = (quest_type == i);
            i = (i + 1);
        };
        define_bunch(TAVERNE_QUESTOVL, (TAVERNE_QUESTOVL1 + quest_type));
        HutBlinzelTimer.add_event_listener(
            TimerEvent.TIMER, HutBlinzelTimerEvent);
        try_show_tv();
        if (!light_mode){
            HutBlinzelTimer.start();
        } else {
            HutBlinzelTimer.stop();
        };
    };
    if (int(savegame[SG_ACTION_STATUS]) == 2){
        show_quest_screen();
        return;
    };
    force_adventure = False;
    actor[QUEST_SLOT].alpha = 1;
    if (on_stage(TAVERNE_BG)){
        remove(QUESTOFFER);
        remove(BEEROFFER);
        add(TAVERNE_CAS);
        refresh_time_bar();
        return;
    };
    load(SCREEN_TAVERNE);
    load(QUESTOFFER);
    load(BEEROFFER);
    if (beer_fest){
        load(BEERFEST);
    };
    if (special_action > 0){
        load(((SPECIAL_ACTION + special_action) - 1));
        load(TAVERNE_BARKEEPER_HINT);
    };
    if (get_advent() != 0){
        load(((TAVERN_ADVENT + get_advent()) - 1));
    };
    when_loaded(DoShowTaverneScreen);
    '''
    print evt


def show_stall_screen(evt=None):
    '''
    var i:* = 0;
    var DoShowStall:* = None;
    var evt:* = evt;
    DoShowStall = function (){
        var HandTimer:* = None;
        var BauerHandEvent:* = None;
        BauerHandEvent = function (evt:TimerEvent){
            var iHand;
            var i;
            iHand = int((random.random() * 5));
            if (
                ((!(on_stage(STALL_BG_GUT)))
                    and (!(on_stage(STALL_BG_BOESE))))){
                HandTimer.stop();
                HandTimer.remove_event_listener(
                    TimerEvent.TIMER, BauerHandEvent);
            };
            i = 0;
            while (i < 5) {
                actor[(STALL_ARME1 + i)].visible = Boolean((i == iHand));
                i++;
            };
        };
        HandTimer = new Timer(200);
        remove_all();
        actor[LBL_STALL_TITEL].text = texts[TXT_STALL_TITEL];
        if (text_dir == "right"){
            actor[LBL_STALL_TITEL].x = (
                (actor[LBL_STALL_TEXT].x + actor[LBL_STALL_TEXT].width)
                - actor[LBL_STALL_TITEL].text_width);
        };
        actor[LBL_STALL_TEXT].text = texts[TXT_STALL_TEXT];
        arabize(LBL_STALL_TEXT);
        actor[LBL_STALL_GAIN].text = "";
        if ((((char_volk >= 5)) and (!(param_censored)))){
            add(STALL_BOESE);
        } else {
            add(STALL_GUT);
        };
        add(SCREEN_STALL);
        if (tageszeit() == 1){
            remove(STALL_NIGHT);
        } else {
            if (tageszeit() == 2){
                remove(STALL_NIGHT, STALL_DAWN);
            };
        };
        HandTimer.add_event_listener(TimerEvent.TIMER, BauerHandEvent);
        HandTimer.start();
    };
    if (((on_stage(STALL_BG_GUT)) or (on_stage(STALL_BG_BOESE)))){
        return;
    };
    load(SCREEN_STALL);
    if ((((char_volk >= 5)) and (!(param_censored)))){
        load(STALL_BOESE);
        load(
            STALL_OVL_BOESE1,
            STALL_OVL_BOESE2,
            STALL_OVL_BOESE3,
            STALL_OVL_BOESE4
        );
        i = 0;
        while (i < 4) {
            load(((SND_MOUNT_1 + i) + 4));
            i = (i + 1);
        };
    } else {
        load(STALL_GUT);
        load(
            STALL_OVL_GUT1,
            STALL_OVL_GUT2,
            STALL_OVL_GUT3,
            STALL_OVL_GUT4
        );
        i = 0;
        while (i < 4) {
            load((SND_MOUNT_1 + i));
            i = (i + 1);
        };
    };
    when_loaded(DoShowStall);
    '''
    print evt


def show_arena_screen(opp_name, opp_gilde, opp_stufe):
    '''
    var tz:* = 0;
    var DoShowArenaScreen:* = None;
    var PvPDelayCheck:* = None;
    var opp_name:* = opp_name;
    var opp_gilde:* = opp_gilde;
    var opp_stufe:* = opp_stufe;
    DoShowArenaScreen = function (evt:Event=None){
        var evt:* = evt;
        remove_all();
        Switch (tz){
            if case(0:
                add(SCREEN_ARENA_NIGHT);
                break;
            if case(1:
                add(SCREEN_ARENA_DAWN);
                break;
            if case(2:
                add(SCREEN_ARENA_DAY);
                break;
        };
        if (opp_name != ""){
            var _local3 = actor[LBL_WINDOW_TITLE];
            with (_local3) {
                text = texts[TXT_ARENA_TITLE];
                x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((text_width / 2)));
            };
            add(SCREEN_ARENA);
            if (Capabilities.version[0: 3] != "IOS"){
                if (light_mode){
                    remove(ARENA_FEUER);
                };
            };
            pvp_delay_timer.add_event_listener(TimerEvent.TIMER,
                                               PvPDelayCheck);
            pvp_delay_timer.start();
            PvPDelayCheck();
            actor[INP_ARENA_enemy].getChildAt(1).text = opp_name;
        };
    };
    PvPDelayCheck = function (evt:TimerEvent=None){
        if (!on_stage(INP_ARENA_enemy)){
            pvp_delay_timer.remove_event_listener(TimerEvent.TIMER,
                                                PvPDelayCheck);
            pvp_delay_timer.stop();
            return;
        };
        if (waiting_for(savegame[SG_PVP_REROLL_TIME])){
            if (text_dir == "right"){
                actor[LBL_ARENA_TEXT].text = (
                    ((((((((texts[TXT_ARENA_4] + " (")
                        + str(opp_stufe)) + " ")
                        + texts[TXT_HALL_LIST_COLUMN_4]) + ") ")
                        + (((opp_gilde == ""))
                            ? ""
                            : (("[" + opp_gilde) + "] ")))
                        + opp_name) + " ") + texts[TXT_ARENA_3]);
            } else {
                actor[LBL_ARENA_TEXT].text = (
                    ((((((((texts[TXT_ARENA_3] + " ") + opp_name)
                    + (((opp_gilde == "")) ? "" : ((" [" + opp_gilde) + "]")))
                    + " (") + texts[TXT_HALL_LIST_COLUMN_4]) + " ")
                    + str(opp_stufe)) + ") ") + texts[TXT_ARENA_4]);
            };
            actor[LBL_ARENA_DELAY].text = waiting_time(
                savegame[SG_PVP_REROLL_TIME]);
            set_title_bar(waiting_time(savegame[SG_PVP_REROLL_TIME]));
            if (text_dir == "right"){
                set_btn_text(ARENA_OK, ("(~P1) " + texts[TXT_OK]));
            } else {
                set_btn_text(ARENA_OK, (texts[TXT_OK] + " (1~P)"));
            };
            show(LBL_ARENA_DELAY);
        } else {
            if (text_dir == "right"){
                actor[LBL_ARENA_TEXT].text = (
                    ((((((((texts[TXT_ARENA_2] + " (")
                        + str(opp_stufe)) + " ")
                    + texts[TXT_HALL_LIST_COLUMN_4]) + ") ")
                    + (((opp_gilde == "")) ? "" : (("[" + opp_gilde) + "] ")))
                    + opp_name) + " ") + texts[TXT_ARENA_1]);
            } else {
                actor[LBL_ARENA_TEXT].text = (
                    ((((((((texts[TXT_ARENA_1] + " ") + opp_name)
                    + (((opp_gilde == "")) ? "" : ((" [" + opp_gilde) + "]")))
                    + " (") + texts[TXT_HALL_LIST_COLUMN_4]) + " ")
                    + str(opp_stufe)) + ") ") + texts[TXT_ARENA_2]);
            };
            arabize(LBL_ARENA_TEXT);
            set_btn_text(ARENA_OK, texts[TXT_OK]);
            hide(LBL_ARENA_DELAY);
            set_title_bar();
            pvp_delay_timer.remove_event_listener(
                TimerEvent.TIMER, PvPDelayCheck);
            pvp_delay_timer.stop();
        };
    };
    tz = tageszeit();
    if ((((int(savegame[SG_ACTION_STATUS]) == 1)) and (!(has_mirror)))){
        show_work_screen();
        return;
    };
    if ((((int(savegame[SG_ACTION_STATUS]) == 2)) and (!(has_mirror)))){
        show_quest_screen();
        return;
    };
    load(SCREEN_ARENA);
    Switch (tz){
        if case(0:
            load(SCREEN_ARENA_NIGHT);
            break;
        if case(1:
            load(SCREEN_ARENA_DAWN);
            break;
        if case(2:
            load(SCREEN_ARENA_DAY);
            break;
    };
    when_loaded(DoShowArenaScreen);
    '''
    print opp_name, opp_gilde, opp_stufe


def show_hall_screen(evt=None):
    '''
    var DoShowHallScreen:* = None;
    var evt:* = evt;
    DoShowHallScreen = function (){
        remove_all();
        if (guild_hall_mode){
            ruhmes_halle_such_string = gilde;
            ruhmes_halle_such_name = True;
        } else {
            ruhmes_halle_such_string = actor[INP['NAME']].getChildAt(1).text;
            ruhmes_halle_such_name = True;
        };
        actor[INP_HALLE_GOTO].getChildAt(1).text = texts[
            TXT_HALLE_SUCHFELD_TEXT];
        add(SCREEN_HALLE);
    };
    load(SCREEN_HALLE);
    when_loaded(DoShowHallScreen);
    '''
    print evt


def show_dealer_screen(evt=None, load_only=False):
    '''
    var papaya_firebug:* = None;
    var url:* = None;
    var DoShowDealerScreen:* = None;
    var evt:* = evt;
    var load_only:Boolean = load_only;
    DoShowDealerScreen = function (par:Object=None){
        remove_all();
        add(SCREEN_DEALER);
    };
    papaya_firebug = "0";
    if (param_obj["firebug"]){
        if (param_obj["firebug"] != ""){
            papaya_firebug = "1";
        };
    };
    url = (
        (((((((((((((((((((((param_papaya_path + "?playerid=")
            + savegame[SG['PLAYER_ID']]) + "&paymentid=")
            + savegame[SG_PAYMENT_ID]) + "&server_id=") + server_id)
            + "&serverdomain=") + server) + "&session_id=") + session_id)
            + "&special=") + dealer_aktion) + "&langcode=") + lang_code)
            + "&volume=") + str(shared_obj.data.volume / 10)) + "&mp_project=")
            + mp_project) + "&cfgfile=") + param_papaya_cfg_file)
            + "&firebug=") + papaya_firebug);
    if (actorURL[SCR_DEALER_BG] != url){
        actorURL[SCR_DEALER_BG] = url;
        actorLoaded[SCR_DEALER_BG] = 0;
    };
    actor[SCR_DEALER_BG].mouseChildren = True;
    actor[SCR_DEALER_BG].mouse_enabled = True;
    load(SCREEN_DEALER);
    if (!load_only){
        when_loaded(DoShowDealerScreen);
    };
    '''
    print evt, load_only


def show_screen_gilde_gruenden(evt=None):
    '''
    var DoShowScreenGilden:* = None;
    var evt:* = evt;
    DoShowScreenGilden = function (evt:Event=None){
        var evt:* = evt;
        remove_all();
        gilde = "";
        my_own_rank = -1;
        my_own_attack_target = -1;
        my_own_guild_money = -1;
        var _local3 = actor[LBL_WINDOW_TITLE];
        with (_local3) {
            text = texts[TXT_GILDE_GRUENDEN_TITLE];
            x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((text_width / 2)));
        };
        add(SCREEN_GILDE_GRUENDEN);
    };
    load(SCREEN_GILDE_GRUENDEN);
    when_loaded(DoShowScreenGilden);
    '''
    print evt


def show_city_screen(evt=None):
    '''
    var StatistenBleiben:* = False;
    var doShowCityScreen:* = None;
    var evt:* = evt;
    doShowCityScreen = function (){
        if (
            ((((on_stage(SCR_CITY_BACKG_NIGHT))
            or (on_stage(SCR_CITY_BACKG_DAWN))))
            or (on_stage(SCR_CITY_BACKG_DAY)))
        ){
            make_persistent(CITY_STATISTEN, BUBBLES);
            StatistenBleiben = True;
        };
        remove_all();
        Switch (tageszeit()){
            if case(0:
                add(SCREEN_CITY_NIGHT);
                break;
            if case(1:
                add(SCREEN_CITY_DAWN);
                break;
            if case(2:
                add(SCREEN_CITY_DAY);
                break;
        };
        add(SCREEN_CITY);
        if (StatistenBleiben){
            make_temporary(CITY_STATISTEN, BUBBLES);
            visible_to_front(CITY_STATISTEN, BUBBLES);
        } else {
            if (int((random.random() * 3)) == 0){
                add(CITY_MAGIER1);
            };
            if (int((random.random() * 3)) == 0){
                add(CITY_ORK1);
                define_bunch(CITY_ORK, CITY_ORK1);
            };
            if (int((random.random() * 3)) == 0){
                add(CITY_SANDWICH1);
            };
            if (int((random.random() * 3)) == 0){
                add(CITY_ZWERG1);
                define_bunch(CITY_ZWERG, CITY_ZWERG1);
            };
            if (int((random.random() * 3)) == 0){
                add(CITY_ELF1);
            };
        };
        if (Capabilities.version[0: 3] != "IOS"){
            actor[SCR_CITY_CLOUDS_NIGHT].scrollRect = new Rectangle(
                0, 0, 1000, 265);
            actor[SCR_CITY_CLOUDS_DAWN].scrollRect = new Rectangle(
                0, 0, 1000, 265);
            actor[SCR_CITY_CLOUDS_DAY].scrollRect = new Rectangle(
                0, 0, 1000, 265);
            if (light_mode){
                remove(SCR_CITY_CLOUDS_NIGHT);
                remove(SCR_CITY_CLOUDS_DAWN);
                remove(SCR_CITY_CLOUDS_DAY);
            };
        };
        show_dealer_screen(None, True);
    };
    StatistenBleiben = False;
    load(BUBBLES);
    Switch (tageszeit()){
        if case(0:
            load(SCREEN_CITY_NIGHT);
            break;
        if case(1:
            load(SCREEN_CITY_DAWN);
            break;
        if case(2:
            load(SCREEN_CITY_DAY);
            break;
    };
    load(SCREEN_CITY);
    load(CITY_ESEL2);
    load(CITY_SANDWICH1);
    load(CITY_SANDWICH2);
    when_loaded(doShowCityScreen);
    '''
    print evt


def show_post_screen(par=None):
    '''
    var DoShowPost:* = None;
    var BuildPostList:* = None;
    var par:* = par;
    DoShowPost = function (evt:Event=None){
        var thisInstance:* = 0;
        var postSchonDa:* = False;
        var evt:* = evt;
        var PostSetFocus:* = function (evt:Event=None){
            var evt:* = evt;
            if (!on_stage(POST_BG)){
                return;
            };
            if (thisInstance != postInstance){
                var _local3 = actor[POST_LIST];
                with (_local3) {
                    remove_event_listener(KeyboardEvent.KEY_DOWN,
                                          PostKeyEvent);
                    remove_event_listener(FocusEvent.FOCUS_OUT, PostSetFocus);
                };
            } else {
                stage.stageFocusRect = False;
                stage.focus = actor[POST_LIST];
            };
        };
        var PostKeyEvent:* = function (evt:KeyboardEvent){
            var evt:* = evt;
            if (((!(on_stage(POST_LIST))) or (on_stage(POST_FLUSH_OK)))){
                return;
            };
            if (thisInstance != postInstance){
                var _local3 = actor[POST_LIST];
                with (_local3) {
                    remove_event_listener(KeyboardEvent.KEY_DOWN,
                                          PostKeyEvent);
                    remove_event_listener(FocusEvent.FOCUS_OUT, PostSetFocus);
                };
                return;
            };
            if (on_stage(POST_LIST)){
                if (
                    (((evt.keyCode == Keyboard.DELETE))
                        or ((evt.keyCode == Keyboard.BACKSPACE)))
                ){
                    post_btn_handler(None, POST_DELETE);
                } else {
                    if (evt.keyCode == Keyboard.ENTER){
                        post_btn_handler(None, POST_READ);
                    } else {
                        if (
                            (((evt.keyCode == Keyboard.UP))
                            or ((evt.keyCode == Keyboard.DOWN)))
                        ){
                            BuildPostList(evt);

        postInstance++;
        if (postInstance > 20000){
            postInstance = 0;
        };
        thisInstance = postInstance;
        postSchonDa = on_stage(SHP_POST_BLACK_SQUARE);
        remove_all();
        if ((par is Array)){
            PostReturnToPlayer = "";
            BuildPostList();
        };
        add(SCREEN_POST);
        var _local3 = actor[POST_LIST];
        with (_local3) {
            add_event_listener(KeyboardEvent.KEY_DOWN, PostKeyEvent);
            add_event_listener(FocusEvent.FOCUS_OUT, PostSetFocus);
        };
        PostSetFocus();
        if (!(par is Array)){
            PostReturnToPlayer = sel_name;
            actor[INP_POST_ADDRESS].getChildAt(1).type = TextFieldType.INPUT;
            actor[INP_POST_SUBJECT].getChildAt(1).type = TextFieldType.INPUT;
            actor[INP_POST_TEXT].getChildAt(1).type = TextFieldType.INPUT;
            remove(POST_LIST);
            add(POST_WRITE);
            hide(POST_GUILD);
            actor[INP_POST_ADDRESS].getChildAt(1).text = sel_name;
            actor[INP_POST_SUBJECT].getChildAt(1).text = texts[TXT_BETREFF];
            actor[INP_POST_TEXT].getChildAt(1).text = texts[TXT_NACHRICHT];
        };
        if (tageszeit() != 0){
            remove(POST_NIGHT);
        };
        if (tageszeit() != 1){
            remove(POST_DAWN);
        };
        if (
            ((((!(postSchonDa))
            and ((par is Array))))
            and (!(light_mode)))
        ){
            set_alpha(POST_LIST, 0);
            set_alpha(SHP_POST_BLACK_SQUARE, 0);
            fade_in(POST_LIST);
            fade_in(SHP_POST_BLACK_SQUARE, 20, 0.05, 0.6);
        };
    };
    BuildPostList = function (evt:Event=None){
        var tmp_array:* = None;
        var sel_row:* = 0;
        var tmpBalken:* = None;
        var line:* = None;
        var i:* = 0;
        var tmp_fmt:* = None;
        var evt:* = evt;
        tmp_array = par[1].split("/");
        if (par[2]){
            savegame[SG_MSG_COUNT] = par[2];
        };
        sel_row = (((tmp_array[0] == "")) ? 0 : 1);
        var _local3 = actor[LBL_POST_LIMIT];
        with (_local3) {
            if (int(savegame[SG_MSG_COUNT]) >= 100){
                default_text_format = FontFormatError;
            } else {
                default_text_format = FontFormatDefault;
            };
            text = (savegame[SG_MSG_COUNT] + " / 100");
            x = (((POST_SQUARE_X + POST_SQUARE_X) - width) + POST_LIMIT_X);
        };
        if ((evt is MouseEvent)){
            sel_row = (int(((
                actor[POST_LIST].getChildIndex(evt.target) - 3) / 4)) + 1);
        };
        if ((evt is KeyboardEvent)){
            sel_row = (o
                ldSel + ((KeyboardEvent(evt).keyCode)==Keyboard.UP)
                    ? -1 : 1);
            if (sel_row < 1){
                post_btn_handler(None, POST_UP);
                return;
            };
            if (sel_row > 15){
                post_btn_handler(None, POST_DOWN);
                return;
            };
            if (tmp_array[((sel_row - 1) * 3)] == ""){
                return;
            };
        };
        if (oldSel == -1){
            sel_row = 15;
        };
        while (tmp_array[((sel_row - 1) * 3)] == "") {
            sel_row = (sel_row - 1);
        };
        oldSel = sel_row;
        _local3 = actor[POST_LIST];
        with (_local3) {
            while (numChildren > 0) {
                removeChildAt(0);
            };
            mouse_enabled = True;
            doubleClickEnabled = True;
            mouseChildren = True;
        };
        if (text_dir == "right"){
            PostListAddField(
                (POST_LIST_COLUMN_1_X + 180),
                POST_LIST_LINES_Y,
                texts[TXT_POST_LIST_COLUMN_1],
                FontFormatPostListHeading
            );
            PostListAddField(
                (POST_LIST_COLUMN_2_X + 470),
                POST_LIST_LINES_Y,
                texts[TXT_POST_LIST_COLUMN_2],
                FontFormatPostListHeading
            );
            PostListAddField(
                (POST_LIST_COLUMN_3_X + 180),
                POST_LIST_LINES_Y,
                texts[TXT_POST_LIST_COLUMN_3],
                FontFormatPostListHeading
            );
        } else {
            PostListAddField(
                POST_LIST_COLUMN_1_X,
                POST_LIST_LINES_Y,
                texts[TXT_POST_LIST_COLUMN_1],
                FontFormatPostListHeading
            );
            PostListAddField(
                POST_LIST_COLUMN_2_X,
                POST_LIST_LINES_Y,
                texts[TXT_POST_LIST_COLUMN_2],
                FontFormatPostListHeading
            );
            PostListAddField(
                POST_LIST_COLUMN_3_X,
                POST_LIST_LINES_Y,
                texts[TXT_POST_LIST_COLUMN_3],
                FontFormatPostListHeading
            );
        };
        post_sel = sel_row;
        post_scrollDown = !((tmp_array[(tmp_array.length - 3)] == ""));
        line = 1;
        i = 0;
        while (i < ((tmp_array.length - 1) - 3)) {
            if (sel_row == line){
                tmp_fmt = FontFormatPostListHighLightSys;
            } else {
                tmp_fmt = FontFormatPostListTextSys;
            };
            tmpBalken = new MovieClip();
            _local3 = tmpBalken.graphics;
            with (_local3) {
                beginFill(CLR_SFORANGE, 0.5);
                lineStyle(0, 0, 0);
                drawRect(
                    0, 0,
                    ((POST_SQUARE_X - (POST_LIST_COLUMN_1_X * 2)) - 10),
                    (POST_LIST_LINE_Y + 3));
            };
            _local3 = tmpBalken;
            with (_local3) {
                x = (POST_LIST_COLUMN_1_X - 5);
                y = ((POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)) - 3);
                mouse_enabled = True;
                doubleClickEnabled = True;
                mouseChildren = False;
                alpha = (((sel_row == line)) ? 1 : 0);
            };
            double_click_handler(tmpBalken, BuildPostList, post_btn_handler);
            if (tmp_array[i] == ""){
                fight_flush_mode = False;
                return;
            };
            Switch (tmp_array[(i + 1)]){
                if case("1":
                    tmp_array[(i + 1)] = texts[TXT_SUBJECT_GUILD_DELETED];
                    break;
                if case("2":
                    tmp_array[(i + 1)] = texts[
                        TXT_SUBJECT_GUILD_DELETED_BY_ADMIN];
                    break;
                if case("3":
                    tmp_array[(i + 1)] = texts[TXT_SUBJECT_GUILD_EXPELLED];
                    break;
                if case("4":
                    tmp_array[(i + 1)] = texts[
                        TXT_SUBJECT_GUILD_EXPELLED_BY_ADMIN];
                    break;
                if case("5":
                    tmp_array[(i + 1)] = texts[TXT_SUBJECT_GUILD_INVITE];
                    break;
                if case("6":
                    if (fight_flush_mode){
                        send_action(
                            ACT_POST_DELETE, ((line + post_scroll) - 1));
                        return;
                    };
                    tmp_array[(i + 1)] = texts[TXT_SUBJECT_PVP].replace(
                        "%1", tmp_array[i]);
                    if (sel_row == line){
                        tmp_fmt = FontFormatPostListHighLightSysRed;
                    } else {
                        tmp_fmt = FontFormatPostListTextSysRed;
                    };
                    break;
                if case("7":
                    if (fight_flush_mode){
                        send_action(
                            ACT_POST_DELETE,
                            ((line + post_scroll) - 1));
                        return;
                    };
                    tmp_array[(i + 1)] = texts[TXT_SUBJECT_PVP].replace(
                        "%1", tmp_array[i]);
                    if (sel_row == line){
                        tmp_fmt = FontFormatPostListHighLightSysGreen;
                    } else {
                        tmp_fmt = FontFormatPostListTextSysGreen;
                    };
                    break;
                if case("8":
                    if (texts[TXT_INV_ACC_TITLE] != ""){
                        tmp_array[(i + 1)] = texts[TXT_INV_ACC_TITLE];
                    } else {
                        tmp_array[(i + 1)] = "FRIEND_INVITE_ACCEPTED";
                    };
                    break;
                if case("9":
                    if (texts[TXT_INV_VAL_TITLE] != ""){
                        tmp_array[(i + 1)] = texts[TXT_INV_VAL_TITLE];
                    } else {
                        tmp_array[(i + 1)] = "FRIEND_EMAIL_VERIFIED";
                    };
                    break;
                if case("1  ":
                if case("2  ":
                if case("3  ":
                if case("4  ":
                if case("5  ":
                if case("6  ":
                if case("7  ":
                if case("8  ":
                if case("9  ":
                    tmp_array[(i + 1)] = "Moo!";
                default:
                    if (sel_row == line){
                        tmp_fmt = FontFormatPostListHighLight;
                    } else {
                        tmp_fmt = FontFormatPostListText;
                    };
            };
            actor[POST_LIST].addChild(tmpBalken);
            add_suggest_names(tmp_array[i]);
            if (text_dir == "right"){
                i = (i + 1);
                PostListAddField(
                    (POST_LIST_COLUMN_1_X + 180),
                    (POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)),
                    tmp_array[i], tmp_fmt
                );
                i = (i + 1);
                PostListAddField(
                    (POST_LIST_COLUMN_2_X + 470),
                    (POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)),
                    tmp_array[i],
                    tmp_fmt
                );
                PostListAddField(
                    (POST_LIST_COLUMN_3_X + 180),
                    (POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)),
                    (((int(tmp_array[i]) == 0))
                        ? ""
                        : time_str(tmp_array[i])),
                    tmp_fmt
                );
            } else {
                i = (i + 1);
                PostListAddField(
                    POST_LIST_COLUMN_1_X,
                    (POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)),
                    tmp_array[i],
                    tmp_fmt
                );
                i = (i + 1);
                PostListAddField(
                    POST_LIST_COLUMN_2_X,
                    (POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)),
                    tmp_array[i],
                    tmp_fmt
                );
                PostListAddField(
                    POST_LIST_COLUMN_3_X,
                    (POST_LIST_LINES_Y + (line * POST_LIST_LINE_Y)),
                    (((int(tmp_array[i]) == 0))
                        ? ""
                        : time_str(tmp_array[i])),
                    tmp_fmt
                );
            };
            line = (line + 1);
            i = (i + 1);
        };
        fight_flush_mode = False;
    };
    var PostListAddField:* = function (
        pos_x, pos_y, txt:String, fmt:TextFormat
    ):
        var tmpLbl:* = None;
        var pos_x:* = pos_x;
        var pos_y:* = pos_y;
        var txt:* = txt;
        var fmt:* = fmt;
        tmpLbl = new TextField();
        var _local6 = tmpLbl;
        with (_local6) {
            default_text_format = fmt;
            auto_size = TextFieldAutoSize.LEFT;
            background = False;
            selectable = False;
            embed_fonts = font_embedded;
            anti_alias_type = AntiAliasType.ADVANCED;
            mouse_enabled = True;
            doubleClickEnabled = True;
            text = txt;
            if (text_dir == "right"){
                x = (pos_x - (((tmpLbl is TextField)) ? text_width : width));
            } else {
                x = pos_x;
            };
            y = pos_y;
            visible = True;
            filters = Filter_Shadow;
        };
        double_click_handler(tmpLbl, BuildPostList, post_btn_handler);
        actor[POST_LIST].addChild(tmpLbl);
    };
    load(SCREEN_POST);
    when_loaded(DoShowPost);
    '''
    print par


def show_build_character_screen(evt=None):
    '''
    var RebuildMode:* = False;
    var i:* = 0;
    var evt:* = evt;
    RebuildMode = False;
    if (
        (((evt is MouseEvent))
        and ((get_actor_id(evt.target) == OPTION_CHANGEIMG)))
    ){
        RebuildMode = True;
    };
    if (
        (((evt is MouseEvent))
        and ((((get_actor_id(evt.target) == GOTO_LOGIN))
        or ((get_actor_id(evt.target) == GOTO_SIGNUP)))))
    ){
        shared_obj.data.skipAutoLOGin = True;
    };
    if (
        ((((shared_obj.data.HasAccount)
        and (!(shared_obj.data.skipAutoLOGin))))
        and (!(RebuildMode)))
    ){
        if (shared_obj.data.userName){
            actor[INP['NAME']].getChildAt(1).text = str(
                shared_obj.data.userName)
        };
        if (shared_obj.data.password){
            actor[INP['LOGIN_PASSWORD']].getChildAt(1).text = str(
                shared_obj.data.password);
        };
        add(BLACK_SQUARE);
        request_login();
        return;
    };
    if (((((buffed_mode) and (!(buffed_req)))) and (!(RebuildMode)))){
        show_login_screen();
        return;
    };
    remove_all();
    i = 0;
    while (i < 10) {
        var _local3 = actor[(CHARBACKGROUND + i)];
        with (_local3) {
            x = ((SCREEN_TITLE_X - 150) + CHARX);
            y = (SCREEN_TITLE_Y + CHARY);
            scaleX = 1;
            scaleY = 1;
        };
        i = (i + 1);
    };
    _local3 = actor[LBL_SCREEN_TITLE];
    with (_local3) {
        text = texts[TXT_CREATE_CHARACTER];
        x = (SCREEN_TITLE_X - int((text_width / 2)));
        y = SCREEN_TITLE_Y;
    };
    add(SCREEN_BUILDCHAR);
    if (DemoMode){
        remove(CREATE_GOTO_LOGIN, IF_LOGOUT);
    };
    if (charface.volk == 0){
        randomize_character();
    };
    if (RebuildMode){
        remove(CREATE_CHARACTER);
        revertchar.volk = charface.volk;
        revertchar.male = charface.male;
        revertchar.color = charface.color;
        revertchar.mouth = charface.mouth;
        revertchar.beard = charface.beard;
        revertchar.nose = charface.nose;
        revertchar.eyes = charface.eyes;
        revertchar.brows = charface.brows;
        revertchar.ears = charface.ears;
        revertchar.hair = charface.hair;
        revertchar.special = charface.special;
        revertchar.special2 = charface.special2;
        KlasseGewählt = True;
    };
    load_character_image();
    '''
    print evt


def show_character_screen(evt=None, no_prices=False):
    '''
    var DoShowCharacterScreen:* = None;
    var evt:* = evt;
    var no_prices:Boolean = no_prices;
    DoShowCharacterScreen = function (){
        var i:* = 0;
        var OneUp:* = False;
        var level_upTimer:* = None;
        var MountTimeTimer:* = None;
        var MountTimeEvent:* = None;
        var vanityRandom:* = NaN;
        var findIndex:* = 0;
        var level_upAniStep:* = 0;
        var kickIn:* = NaN;
        var level_upAniEvent:* = None;
        MountTimeEvent = function (evt:TimerEvent=None){
            if (
                ((!(on_stage(LBL_CHAR_MOUNT_RUNTIME)))
                    or ((savegame[SG_MOUNT] == 0)))
            ){
                MountTimeTimer.stop();
                MountTimeTimer.remove_event_listener(
                    TimerEvent.TIMER, MountTimeEvent);
                return;
            };
            if (
                ((texts[TXT_MOUNT_FOREVER])
                    and ((savegame[SG_MOUNT_DURATION] == 0x7D2B7500)))
            ){
                actor[LBL_CHAR_MOUNT_RUNTIME].text = texts[
                    TXT_MOUNT_FOREVER];
            } else {
                if (text_dir == "right"){
                    actor[LBL_CHAR_MOUNT_RUNTIME].text = (
                        (waiting_time(savegame[SG_MOUNT_DURATION]) + " ")
                        + texts[TXT_MOUNT_DURATION]
                    );
                } else {
                    actor[LBL_CHAR_MOUNT_RUNTIME].text = (
                        (texts[TXT_MOUNT_DURATION] + " ")
                        + waiting_time(savegame[SG_MOUNT_DURATION])
                    );
                };
            };
        };
        level_upTimer = new Timer(20);
        error_message(" ");
        if (!on_stage(SCR_CHAR_BG)){
            set_alpha(CHAR_SECONDPROP, 1);
            set_alpha(CHAR_PREISE, 0);
        };
        remove_all();
        i = 0;
        while (i < 10) {
            var _local2 = actor[(CHARBACKGROUND + i)];
            with (_local2) {
                x = SCR_CHAR_CHARX;
                y = SCR_CHAR_CHARY;
                scaleX = 0.86;
                scaleY = 0.86;
            };
            i = (i + 1);
        };
        i = 0;
        while (i < 5) {
            set_cnt((SCR_CHAR_GOLD1 + i), IF_GOLD);
            set_cnt((SCR_CHAR_SILBER1 + i), IF_SILBER);
            i = (i + 1);
        };
        if (text_dir == "right"){
            actor[LBL_CHAR_MOUNT_NAME].text = (
                (texts[TXT_NOMOUNT] + " ") + texts[TXT_MOUNT]);
        } else {
            actor[LBL_CHAR_MOUNT_NAME].text = (
                (texts[TXT_MOUNT] + " ") + texts[TXT_NOMOUNT]);
        };
        actor[LBL_CHAR_MOUNT_RUNTIME].text = "";
        actor[LBL_CHAR_MOUNT_DESCR].text = "";
        actor[LBL_CHAR_MOUNT_GAIN].text = "";
        if (savegame[SG_MOUNT] > 0){
            add(LBL_CHAR_MOUNT_RUNTIME);
        } else {
            remove(LBL_CHAR_MOUNT_RUNTIME);
        };
        MountTimeTimer = new Timer(500);
        MountTimeTimer.add_event_listener(TimerEvent.TIMER, MountTimeEvent);
        MountTimeTimer.start();
        i = 0;
        while (i < 8) {
            if (
                (((int(savegame[SG_MOUNT]) > 0))
                and (((i + 1) == (int(savegame[SG_MOUNT])
                + (((((savegame[SG_RACE] >= 5))
                and (!(param_censored)))) ? 4 : 0)))))
            ){
                show((CHAR_MOUNT_1 + i));
                if (text_dir == "right"){
                    actor[LBL_CHAR_MOUNT_NAME].text = (
                        (texts[(TXT_STALL_MOUNTTITEL + i)] + " ")
                        + texts[TXT_MOUNT]
                    );
                    actor[LBL_CHAR_MOUNT_DESCR].text = texts[
                        (TXT_STALL_MOUNTTEXT + i)
                    ];
                    actor[LBL_CHAR_MOUNT_GAIN].text = texts[
                        (TXT_MOUNT_GAIN1 + i)
                    ].split("|")[0];
                } else {
                    actor[LBL_CHAR_MOUNT_NAME].text = (
                        (texts[TXT_MOUNT] + " ")
                        + texts[(TXT_STALL_MOUNTTITEL + i)]
                    );
                    actor[LBL_CHAR_MOUNT_DESCR].text = texts[
                        (TXT_STALL_MOUNTTEXT + i)];
                    actor[LBL_CHAR_MOUNT_GAIN].text = texts[
                        (TXT_MOUNT_GAIN1 + i)].split("|")[0];
                };
                MountTimeEvent();
            } else {
                hide((CHAR_MOUNT_1 + i));
            };
            i = (i + 1);
        };
        if (text_dir == "right"){
            actor[LBL_SCR_CHAR_NAME].text = (
                ((gilde) ? (("[" + gilde) + "] ") : "")
                + actor[INP['NAME']].getChildAt(1).text
            );
        } else {
            actor[LBL_SCR_CHAR_NAME].text = (
                actor[INP['NAME']].getChildAt(1).text
                + ((gilde) ? ((" [" + gilde) + "]") : "")
            );
        };
        lastPlayer = actor[INP['NAME']].getChildAt(1).text;
        if (gilde){
            SelectedGuild = gilde;
            actor[SCR_CHAR_NAME].useHandCursor = True;
        } else {
            SelectedGuild = "";
            actor[SCR_CHAR_NAME].useHandCursor = False;
        };
        trim_too_long(LBL_SCR_CHAR_NAME, 260);
        i = 0;
        while (i < 3) {
            if ((int(savegame[SG_CLASS]) - 1) == i){
                show((SCR_CHAR_KLASSE_1 + i));
            } else {
                hide((SCR_CHAR_KLASSE_1 + i));
            };
            i = (i + 1);
        };
        if (text_dir == "right"){
            actor[LBL_SCR_CHAR_GILDE].text = (
                (((((savegame[SG_HONOR] + " :")
                + texts[TXT_HALL_LIST_COLUMN_5]) + "     ")
                + savegame[SG_RANK]) + " :")
                + texts[TXT_HALL_LIST_COLUMN_1]
            );
        } else {
            actor[LBL_SCR_CHAR_GILDE].text = (
                (((((texts[TXT_HALL_LIST_COLUMN_1] + ": ")
                    + savegame[SG_RANK]) + "     ")
                    + texts[TXT_HALL_LIST_COLUMN_5]) + ": ")
                    + savegame[SG_HONOR]);
        };
        actor[LBL_SCR_CHAR_EHRE].text = "";
        _local2 = actor[INP_CHARDESC];
        with (_local2) {
            getChildAt(0).text = (
                (player_desc)=="") ? texts[TXT_ENTERDESC] : player_desc;
            getChildAt(0).type = TextFieldType.INPUT;
            if (text_dir == "right"){
                getChildAt(0).wordWrap = False;
            };
        };
        actor[SCR_CHAR_NAME].x = (
            (SCR_CHAR_CHARX + 128)
            - int((actor[LBL_SCR_CHAR_NAME].text_width / 2)));
        actor[LBL_SCR_CHAR_EHRE].x = (
            (actor[LBL_SCR_CHAR_GILDE].x
            + actor[LBL_SCR_CHAR_GILDE].text_width) + CHAR_EHRE_X);
        _local2 = actor[SCR_CHAR_EXPBAR];
        with (_local2) {
            width = int(((Number(savegame[SG_EXP])
                / Number(savegame[SG_EXP_FOR_NEXTLEVEL])) * 254));
        };
        _local2 = actor[LBL_SCR_CHAR_EXPLABEL];
        with (_local2) {
            if (text_dir == "right"){
                text = ((savegame[SG_LEVEL] + " ")
                    + texts[TXT_HALL_LIST_COLUMN_4]);
            } else {
                text = ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                    + savegame[SG_LEVEL]);
            };
            x = ((EXPERIENCE_BAR_X + 127) - int((text_width / 2)));
        };
        if (text_dir == "right"){
            enable_popup(
                CA_SCR_CHAR_EXPBAR,
                POPUP_BEGIN_LINE,
                (":" + texts[TXT_EXP]),
                (POPUP_TAB + POPUP_TAB_ADD),
                savegame[SG_EXP],
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                (":" + texts[TXT_EXPNEXTLEVEL]),
                (POPUP_TAB + POPUP_TAB_ADD),
                savegame[SG_EXP_FOR_NEXTLEVEL],
                POPUP_END_LINE
            );
        } else {
            enable_popup(
                CA_SCR_CHAR_EXPBAR,
                POPUP_BEGIN_LINE,
                (texts[TXT_EXP] + ":"),
                (POPUP_TAB + POPUP_TAB_ADD),
                savegame[SG_EXP],
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                (texts[TXT_EXPNEXTLEVEL] + ":"),
                (POPUP_TAB + POPUP_TAB_ADD),
                savegame[SG_EXP_FOR_NEXTLEVEL],
                POPUP_END_LINE
            );
        };
        display_inventory(None, no_prices);
        vanityRandom = random.random();
        if (
            (((((((uint(savegame[SG_NEW_FLAGS]) & 32))
            and ((int(shared_obj.data.vanityMode) == 0))))
            or ((int(shared_obj.data.vanityMode) == 2))))
            or ((((int(shared_obj.data.vanityMode) == 3))
            and ((vanityRandom < 0.5)))))
        ){
            add(SCREEN_CHAR_GOLDEN);
        } else {
            add(SCREEN_CHAR);
        };
        load_character_image();
        add_some(SCR_CHAR_NAME, SCR_CHAR_GILDE);
        mirror_ani_timer.stop();
        i = 0;
        while (i < 13) {
            if (mirror_pieces[i]){
                add((MIRROR_PIECE + i));
                mirror_ani_timer.start();
            };
            i = (i + 1);
        };
        if (
            (((((((uint(savegame[SG_NEW_FLAGS]) & 32))
                and ((int(shared_obj.data.vanityMode) == 0))))
                or ((int(shared_obj.data.vanityMode) == 2))))
                or ((((int(shared_obj.data.vanityMode) == 3))
                and ((vanityRandom < 0.5)))))
            ){
            add_some(GOLDEN_FRAME, SCR_CHAR_NAME);
            actor[SCR_CHAR_NAME].y = (CHAR_NAME_Y + 8);
            add_filter(LBL_SCR_CHAR_NAME, Filter_HeavyShadow);
        } else {
            actor[SCR_CHAR_NAME].y = CHAR_NAME_Y;
            add_filter(LBL_SCR_CHAR_NAME, Filter_Shadow);
        };
        if (texts[(TXT_ACH_4 + 4)]){
            if (int(savegame[SG_EMAIL_VALID]) == 1){
                add_some(CHAR_INVITE);
            };
        };
        if (texts[TXT_ALBUM]){
            if (Number(savegame[SG_ALBUM]) >= 10000){
                add(CHAR_ALBUM);
                enable_popup(
                    CHAR_ALBUM,
                    POPUP_BEGIN_LINE,
                    texts[TXT_ITMNAME_13],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[TXT_COLLECTION].split(
                        "%1").join(str((savegame[SG_ALBUM] - 10000))).split(
                        "%2").join(str(contentMax)).split(
                        "%3").join(str((math.round((((
                            savegame[SG_ALBUM] - 10000)
                            / contentMax) * 10000)) / 100))).split(
                        "#").join(chr(13)),
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_COLLECTION + 7)],
                    POPUP_END_LINE
                );
                if (album_effect){
                    animate_ach(CHAR_ALBUM, CHAR_PLAYERY);
                    album_effect = False;
                };
            };
        };
        OneUp = do_achievements(savegame);
        if (level_up){
            level_upAniEvent = function (evt:Event){
                var evt:* = evt;
                level_upAniStep++;
                if (level_upAniStep > 125){
                    level_upTimer.stop();
                    level_upTimer.remove_event_listener(
                        TimerEvent.TIMER, level_upAniEvent);
                    var _local3 = actor[LBL_SCR_CHAR_EXPLABEL];
                    with (_local3) {
                        scaleX = 1;
                        scaleY = 1;
                        x = ((EXPERIENCE_BAR_X + 127)
                            - int((text_width / 2)));
                        y = (EXPERIENCE_BAR_Y + 2);
                    };
                    return;
                };
                if (level_upAniStep > 115){
                    if (kickIn > 0){
                        kickIn = (kickIn - 0.1);
                    };
                } else {
                    if (kickIn < 1){
                        kickIn = (kickIn + 0.1);
                    };
                };
                _local3 = actor[LBL_SCR_CHAR_EXPLABEL];
                with (_local3) {
                    scaleX = (
                        ((math.cos((((level_upAniStep / 50) * 2)
                            * math.pi)) + 1) * kickIn) + 1);
                    scaleY = (
                        ((math.sin((((level_upAniStep / 50) * 2)
                            * math.pi)) + 1) * kickIn) + 1);
                    x = ((EXPERIENCE_BAR_X + 128) - int((width / 2)));
                    y = (((EXPERIENCE_BAR_Y + 17)
                        - int((height / 2)))
                        - (((math.sin((((level_upAniStep / 50) * 2)
                            * math.pi)) + 1) * kickIn) * 20));
                };
            };
            level_upAniStep = 25;
            kickIn = 0;
            add(LBL_SCR_CHAR_EXPLABEL);
            OneUp = True;
            level_up = False;
            _local2 = level_upTimer;
            with (_local2) {
                add_event_listener(TimerEvent.TIMER, level_upAniEvent);
                start();
            };
        };
        if (OneUp){
            play(SND_JINGLE);
        };
        if (arrow_hall_mode){
            enable_popup(PREV_PLAYER, texts[TXT_EHRENHALLE]);
            enable_popup(NEXT_PLAYER, texts[TXT_EHRENHALLE]);
            indexInHall = -1;
            findIndex = 0;
            while (findIndex < last_hall_members.length) {
                if (last_hall_members[findIndex].lower() == actor[
                    INP['NAME']
                ].getChildAt(1).text.lower()
                ){
                    indexInHall = (findIndex - 1);
                    break;
                };
                findIndex = (findIndex + 1);
            };
            if (indexInHall < 0){
                indexInHall = -1;
            };
            if (indexInHall != -1){
                if (indexInHall > 0){
                    add(PREV_PLAYER);
                };
                if (indexInHall < 14){
                    add(NEXT_PLAYER);
                };
            };
        } else {
            enable_popup(PREV_PLAYER, texts[TXT_GILDEN]);
            enable_popup(NEXT_PLAYER, texts[TXT_GILDEN]);
            indexInGuild = -1;
            findIndex = 0;
            while (findIndex < lastguild_members.length) {
                if (lastguild_members[
                    findIndex
                ].lower() == actor[INP['NAME']].getChildAt(1).text.lower()
                ){
                    indexInGuild = (findIndex - 1);
                    break;
                };
                findIndex = (findIndex + 1);
            };
            if (indexInGuild < 0){
                indexInGuild = -1;
            };
            if (indexInGuild != -1){
                if (indexInGuild > 0){
                    add(PREV_PLAYER);
                };
                if (indexInGuild < (int(last_guild_data[3]) - 1)){
                    add(NEXT_PLAYER);
                };
            };
        };
    };
    if (
        (((((uint(savegame[SG_NEW_FLAGS]) & 32))
        and ((int(shared_obj.data.vanityMode) == 0))))
        or ((int(shared_obj.data.vanityMode) > 1)))
    ){
        load(SCR_CHAR_BG_GOLDEN, GOLDEN_FRAME);
    };
    load(SCR_CHAR_BG, SCR_CHAR_EXPBAR, SCR_CHAR_BG_RIGHT);
    when_loaded(DoShowCharacterScreen);
    '''
    print evt, no_prices


def show_player_screen(player_sg, player_name, player_gilde, player_comment):
    '''
    var i:* = 0;
    var bin_str:* = None;
    var Playermirror_pieces:* = None;
    var Doshow_player_screen:* = None;
    var player_sg:* = player_sg;
    var player_name:* = player_name;
    var player_gilde:* = player_gilde;
    var player_comment:* = player_comment;
    Doshow_player_screen = function (){
        var i:* = 0;
        var vanityRandom:* = NaN;
        var PvPDelayCheck:* = None;
        var findIndex:* = 0;
        PvPDelayCheck = function (evt:TimerEvent=None){
            var evt:* = evt;
            if (!on_stage(CHAR_ATTACK)){
                pvp_delay_timer.remove_event_listener(
                    TimerEvent.TIMER, PvPDelayCheck);
                pvp_delay_timer.stop();
                return;
            };
            if (waiting_for(savegame[SG_PVP_REROLL_TIME])){
                set_title_bar(waiting_time(savegame[SG_PVP_REROLL_TIME]));
                if (text_dir == "right"){
                    set_btn_text(
                        CHAR_ATTACK, ("(~P1) " + texts[TXT_ATTACK])
                    );
                } else {
                    set_btn_text(
                        CHAR_ATTACK, (texts[TXT_ATTACK] + " (1~P)")
                    );
                };
                show(LBL_CHAR_DELAY);
                var _local3 = actor[LBL_CHAR_DELAY];
                with (_local3) {
                    text = waiting_time(savegame[SG_PVP_REROLL_TIME]);
                    x = (((280 + 500) + CHAR_DELAY_X) - (text_width / 2));
                };
            } else {
                set_title_bar();
                set_btn_text(CHAR_ATTACK, texts[TXT_ATTACK]);
                hide(LBL_CHAR_DELAY);
                pvp_delay_timer.remove_event_listener(
                    TimerEvent.TIMER, PvPDelayCheck
                );
                pvp_delay_timer.stop();
            };
        };
        remove_all();
        dragDropProhibit = True;
        i = 0;
        while (i < 15) {
            actor[(CHAR_SLOT_1 + i)].mouse_enabled = False;
            i = (i + 1);
        };
        i = 0;
        while (i < 10) {
            var _local2 = actor[(CHARBACKGROUND + i)];
            with (_local2) {
                x = SCR_CHAR_CHARX;
                y = SCR_CHAR_CHARY;
                scaleX = 0.86;
                scaleY = 0.86;
            };
            i = (i + 1);
        };
        i = 0;
        while (i < 5) {
            set_cnt((SCR_CHAR_GOLD1 + i), IF_GOLD);
            set_cnt((SCR_CHAR_SILBER1 + i), IF_SILBER);
            i = (i + 1);
        };
        if (text_dir == "right"){
            actor[LBL_CHAR_MOUNT_NAME].text = (
                (texts[TXT_NOMOUNT] + " ") + texts[TXT_MOUNT]
            );
        } else {
            actor[LBL_CHAR_MOUNT_NAME].text = (
                (texts[TXT_MOUNT] + " ") + texts[TXT_NOMOUNT]
            );
        };
        actor[LBL_CHAR_MOUNT_RUNTIME].text = "";
        actor[LBL_CHAR_MOUNT_DESCR].text = "";
        actor[LBL_CHAR_MOUNT_GAIN].text = "";
        i = 0;
        while (i < 8) {
            if (
                (((int(player_sg[SG_MOUNT]) > 0))
                and (((i + 1) == (int(player_sg[SG_MOUNT])
                + (((((player_sg[SG_RACE] >= 5))
                and (!(param_censored)))) ? 4 : 0)))))
            ){
                show((CHAR_MOUNT_1 + i));
                if (text_dir == "right"){
                    actor[LBL_CHAR_MOUNT_NAME].text = (
                        (texts[(TXT_STALL_MOUNTTITEL + i)] + " ")
                        + texts[TXT_MOUNT]);
                    actor[LBL_CHAR_MOUNT_DESCR].text = texts[
                        (TXT_STALL_MOUNTTEXT + i)];
                    actor[LBL_CHAR_MOUNT_GAIN].text = texts[
                        (TXT_MOUNT_GAIN1 + i)].split("|")[0];
                } else {
                    actor[LBL_CHAR_MOUNT_NAME].text = (
                        (texts[TXT_MOUNT] + " ")
                        + texts[(TXT_STALL_MOUNTTITEL + i)]);
                    actor[LBL_CHAR_MOUNT_DESCR].text = texts[
                        (TXT_STALL_MOUNTTEXT + i)];
                    actor[LBL_CHAR_MOUNT_GAIN].text = texts[
                        (TXT_MOUNT_GAIN1 + i)].split("|")[0];
                };
            } else {
                hide((CHAR_MOUNT_1 + i));
            };
            i = (i + 1);
        };
        if (text_dir == "right"){
            actor[LBL_SCR_CHAR_NAME].text = (
                ((player_gilde == "")) ? "" : ((("[" + player_gilde) + "] ")
                    + player_name));
        } else {
            actor[LBL_SCR_CHAR_NAME].text = (
                player_name + (((player_gilde == ""))
                    ? "" : ((" [" + player_gilde) + "]")));
        };
        trim_too_long(LBL_SCR_CHAR_NAME, 260);
        lastPlayer = player_name;
        if (player_gilde){
            SelectedGuild = player_gilde;
            actor[SCR_CHAR_NAME].useHandCursor = True;
        } else {
            SelectedGuild = "";
            actor[SCR_CHAR_NAME].useHandCursor = False;
        };
        i = 0;
        while (i < 3) {
            if ((int(player_sg[SG_CLASS]) - 1) == i){
                show((SCR_CHAR_KLASSE_1 + i));
            } else {
                hide((SCR_CHAR_KLASSE_1 + i));
            };
            i = (i + 1);
        };
        if (text_dir == "right"){
            actor[LBL_SCR_CHAR_GILDE].text = (
                (((((player_sg[SG_HONOR] + " :")
                + texts[TXT_HALL_LIST_COLUMN_5]) + "     ")
                + player_sg[SG_RANK]) + " :")
                + texts[TXT_HALL_LIST_COLUMN_1]
            );
        } else {
            actor[LBL_SCR_CHAR_GILDE].text = (
                (((((texts[TXT_HALL_LIST_COLUMN_1] + ": ")
                + player_sg[SG_RANK]) + "     ")
                + texts[TXT_HALL_LIST_COLUMN_5]) + ": ")
                + player_sg[SG_HONOR]
            );
        };
        actor[LBL_SCR_CHAR_EHRE].text = "";
        _local2 = actor[INP_CHARDESC];
        with (_local2) {
            getChildAt(0).text = (
                (player_comment)=="")
                    ? texts[TXT_NODESC]
                    : player_comment;
            getChildAt(0).type = TextFieldType.DYNAMIC;
        };
        actor[SCR_CHAR_NAME].x = (
            (SCR_CHAR_CHARX + 128)
            - int((actor[LBL_SCR_CHAR_NAME].text_width / 2)));
        actor[LBL_SCR_CHAR_EHRE].x = (
            (actor[LBL_SCR_CHAR_GILDE].x
                + actor[LBL_SCR_CHAR_GILDE].text_width) + CHAR_EHRE_X);
        _local2 = actor[SCR_CHAR_EXPBAR];
        with (_local2) {
            width = int(
                ((Number(player_sg[SG_EXP])
                    / Number(player_sg[SG_EXP_FOR_NEXTLEVEL])) * 254));
        };
        _local2 = actor[LBL_SCR_CHAR_EXPLABEL];
        with (_local2) {
            if (text_dir == "right"){
                text = (
                    (player_sg[SG_LEVEL] + " ")
                    + texts[TXT_HALL_LIST_COLUMN_4]);
            } else {
                text = (
                    (texts[TXT_HALL_LIST_COLUMN_4] + " ")
                    + player_sg[SG_LEVEL]);
            };
            x = ((EXPERIENCE_BAR_X + 127) - int((text_width / 2)));
        };
        enable_popup(CA_SCR_CHAR_EXPBAR);
        set_alpha(CHAR_SECONDPROP, 1);
        set_alpha(CHAR_PREISE, 0);
        display_inventory(player_sg);
        vanityRandom = random.random();
        if (
            (((((((uint(player_sg[SG_NEW_FLAGS]) & 32))
            and ((int(shared_obj.data.vanityMode) == 0))))
            or ((int(shared_obj.data.vanityMode) == 2))))
            or ((((int(shared_obj.data.vanityMode) == 3))
            and ((vanityRandom < 0.5)))))
        ){
            add(SCREEN_CHAR_GOLDEN);
        } else {
            add(SCREEN_CHAR);
        };
        if (((!((player_gilde == gilde))) and (!((gilde == ""))))){
            add(PLAYER_GUILD_INVITE);
        };
        if (texts[TXT_ALBUM]){
            if (Number(player_sg[SG_ALBUM]) >= 10000){
                add(CHAR_ALBUM);
                enable_popup(
                    CHAR_ALBUM,
                    POPUP_BEGIN_LINE,
                    texts[TXT_ITMNAME_13],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[TXT_COLLECTION].split(
                        "%1").join(str((player_sg[SG_ALBUM] - 10000))).split(
                        "%2").join(str(contentMax)).split(
                        "%3").join(str((math.round(
                            (((player_sg[SG_ALBUM] - 10000) / contentMax)
                                * 10000)) / 100))).split(
                        "#").join(chr(13)),
                        POPUP_END_LINE
                    );
            };
        };
        if ((((player_gilde == gilde)) and (!((gilde == ""))))){
            add_some(CHAR_MESSAGE, CHAR_GILDE);
        } else {
            add_some(CHAR_MESSAGE);
            if (
                (((savegame[SG_ACTION_STATUS] == 0))
                or ((((savegame[SG_ACTION_STATUS] >= 1))
                and (has_mirror))))
            ){
                if (can_rob){
                    add_some(CHAR_ATTACK, LBL_CHAR_DELAY);
                } else {
                    add_some(CHAR_ATTACK, LBL_CHAR_DELAY);
                };
            };
        };
        do_achievements(player_sg);
        pvp_delay_timer.add_event_listener(TimerEvent.TIMER, PvPDelayCheck);
        pvp_delay_timer.start();
        PvPDelayCheck();
        i = 0;
        while (i < 5) {
            remove((SCR_CHAR_STEIGERN1 + i));
            i = (i + 1);
        };
        remove(LBL_CHAR_MOUNT_RUNTIME);
        load_character_image(
            CHARBACKGROUND,
            False,
            player_sg[SG_RACE],
            (int(player_sg[SG_GENDER]) == 1),
            player_sg[SG_CLASS],
            player_sg[SG_FACE_1],
            player_sg[SG_FACE_5],
            player_sg[SG_FACE_6],
            player_sg[SG_FACE_4],
            player_sg[SG_FACE_3],
            player_sg[SG_FACE_7],
            player_sg[SG_FACE_2],
            player_sg[SG_FACE_8],
            player_sg[SG_FACE_9]
        );
        add_some(SCR_CHAR_NAME, SCR_CHAR_GILDE);
        if (
            (((((((uint(player_sg[SG_NEW_FLAGS]) & 32))
            and ((int(shared_obj.data.vanityMode) == 0))))
            or ((int(shared_obj.data.vanityMode) == 2))))
            or ((((int(shared_obj.data.vanityMode) == 3))
            and ((vanityRandom < 0.5)))))
        ){
            add_some(GOLDEN_FRAME, SCR_CHAR_NAME);
            actor[SCR_CHAR_NAME].y = (CHAR_NAME_Y + 8);
            add_filter(LBL_SCR_CHAR_NAME, Filter_HeavyShadow);
        } else {
            actor[SCR_CHAR_NAME].y = CHAR_NAME_Y;
            add_filter(LBL_SCR_CHAR_NAME, Filter_Shadow);
        };
        if (arrow_hall_mode){
            enable_popup(PREV_PLAYER, texts[TXT_EHRENHALLE]);
            enable_popup(NEXT_PLAYER, texts[TXT_EHRENHALLE]);
            indexInHall = -1;
            findIndex = 0;
            while (findIndex < last_hall_members.length) {
                if (
                    last_hall_members[
                        findIndex
                    ].lower() == player_name.lower()
                ){
                    indexInHall = (findIndex - 1);
                    break;
                };
                findIndex = (findIndex + 1);
            };
            if (indexInHall < 0){
                indexInHall = -1;
            };
            if (indexInHall != -1){
                if (indexInHall > 0){
                    add(PREV_PLAYER);
                };
                if (indexInHall < 14){
                    add(NEXT_PLAYER);
                };
            };
        } else {
            enable_popup(PREV_PLAYER, texts[TXT_GILDEN]);
            enable_popup(NEXT_PLAYER, texts[TXT_GILDEN]);
            indexInGuild = -1;
            findIndex = 0;
            while (findIndex < lastguild_members.length) {
                if (
                    lastguild_members[findIndex].lower() == player_name.lower()
                ){
                    indexInGuild = (findIndex - 1);
                    break;
                };
                findIndex = (findIndex + 1);
            };
            if (indexInGuild < 0){
                indexInGuild = -1;
            };
            if (indexInGuild != -1){
                if (indexInGuild > 0){
                    add(PREV_PLAYER);
                };
                if (indexInGuild < (int(last_guild_data[3]) - 1)){
                    add(NEXT_PLAYER);
                };
            };
        };
    };
    playerTowerLevel = int((player_sg[SG_MOUNT] / 65536));
    player_sg[SG_MOUNT] = (player_sg[SG_MOUNT] - (playerTowerLevel * 65536));
    bin_str = Number(player_sg[SG_GENDER]).tostr(2);
    while (bin_str.length < 32) {
        bin_str = ("0" + bin_str);
    };
    Playermirror_pieces = list();
    i = 0;
    while (i < 13) {
        Playermirror_pieces[i] = (bin_str[(i + 1): 1] == "1");
        i = (i + 1);
    };
    var playerHasMirror:* = (bin_str[23: 1] == "1");
    if (bin_str[31:] == "1"){
        player_sg[SG_GENDER] = 1;
    } else {
        player_sg[SG_GENDER] = 2;
    };
    i = 0;
    while (i < SG_BACKPACK_SIZE) {
        expand_item_structure(
            player_sg,
            (SG_BACKPACK_OFFS + (i * SG['ITM']['SIZE']))
        );
        i = (i + 1);
    };
    i = 0;
    while (i < SG_INVENTORY_SIZE) {
        expand_item_structure(
            player_sg,
            (SG_INVENTORY_OFFS + (i * SG['ITM']['SIZE']))
        );
        i = (i + 1);
    };
    i = 0;
    while (i < 6) {
        expand_item_structure(
            player_sg,
            (SG_SHAKES_ITEM1 + (i * SG['ITM']['SIZE']))
        );
        expand_item_structure(
            player_sg,
            (SG_FIDGET_ITEM1 + (i * SG['ITM']['SIZE']))
        );
        i = (i + 1);
    };
    i = 0;
    while (i < 3) {
        expand_item_structure(
            player_sg,
            (SG['QUEST']['OFFER']['REWARD_ITM1'] + (i * SG['ITM']['SIZE']))
        );
        i = (i + 1);
    };
    if (
        (((((uint(player_sg[SG_NEW_FLAGS]) & 32))
        and ((int(shared_obj.data.vanityMode) == 0))))
        or ((int(shared_obj.data.vanityMode) > 1)))
    ){
        load(SCR_CHAR_BG_GOLDEN, GOLDEN_FRAME);
    };
    load(SCR_CHAR_BG, SCR_CHAR_EXPBAR, SCR_CHAR_BG_RIGHT);
    when_loaded(Doshow_player_screen);
    '''
    print player_sg, player_name, player_gilde, player_comment


def show_screen_gilden(
        guild_data, guild_descr, guild_members,
        this_gilde, is_mine=True, gilden_rang=0,
        gilden_ehre=0, attack_cost=0
):
    '''
    var DoShowScreenGilden:* = None;
    var guild_data:* = guild_data;
    var guild_descr:* = guild_descr;
    var guild_members:* = guild_members;
    var this_gilde:* = this_gilde;
    var is_mine:Boolean = is_mine;
    var gilden_rang = gilden_rang;
    var gilden_ehre = gilden_ehre;
    var attack_cost = attack_cost;
    DoShowScreenGilden = function (evt:Event=None){
        var i:* = 0;
        var myRank:* = 0;
        var myAttackStatus:* = 0;
        var scrollLevel:* = 0;
        var selectLevel:* = 0;
        var GoldToDonate:* = 0;
        var MushToDonate:* = 0;
        var DonateTimeout:* = None;
        var thisInstanceID:* = 0;
        var removeListenersTimer:* = None;
        var GoldKosten:* = 0;
        var PilzKosten:* = 0;
        var Nutzen:* = None;
        var Ausbaustufe:* = 0;
        var AusbaustufeEx:* = 0;
        var GoldKostenAvg:* = 0;
        var PilzKostenAvg:* = 0;
        var cheapest:* = 0;
        var countCompleted:* = 0;
        var LeftBoxWidth:* = 0;
        var RightBoxWidth:* = 0;
        var crestView:* = False;
        var startWithCrest:* = False;
        var GuildBtnRepeatTimer:* = None;
        var raidCost:* = NaN;
        var isRaid:* = False;
        var GuildBtnHandler:* = None;
        var DoDonate:* = None;
        var RequestPlayerScreen:* = None;
        var BuildGuildList:* = None;
        var evt:* = evt;
        var removeListeners:* = function (evt:TimerEvent){
            var evt:* = evt;
            if (
                ((!((guildInstanceID == thisInstanceID)))
                or (!(on_stage(GILDE_RAHMEN))))
            ){
                removeListenersTimer.stop();
                var _local3 = removeListenersTimer;
                with (_local3) {
                    remove_event_listener(TimerEvent.TIMER, removeListeners);
                };
                actor[GILDE_SCROLL_UP].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_SCROLL_DOWN].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DIALOG_CANCEL].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DIALOG_OK_KICK].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DIALOG_OK_MASTER].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DIALOG_OK_INVITE].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DIALOG_OK_REVOLT].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DIALOG_OK_RAID].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_INVITE].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_PROFILE].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_KICK].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_PROMOTE].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_DEMOTE].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_MASTER].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_REVOLT].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_GEBAEUDE_IMPROVE].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[(GILDE_GEBAEUDE_IMPROVE + 1)].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[(GILDE_GEBAEUDE_IMPROVE + 2)].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_KATAPULT].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[(GILDE_KATAPULT + 1)].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[(GILDE_KATAPULT + 2)].remove_event_listener(
                    MouseEvent.CLICK, GuildBtnHandler);
                actor[GILDE_GOLD].remove_event_listener(
                    MouseEvent.MOUSE_DOWN, GuildBtnHandler);
                actor[GILDE_MUSH].remove_event_listener(
                    MouseEvent.MOUSE_DOWN, GuildBtnHandler);
                actor[GILDE_GOLD].remove_event_listener(
                    MouseEvent.MOUSE_OUT, DoDonate);
                actor[GILDE_MUSH].remove_event_listener(
                    MouseEvent.MOUSE_OUT, DoDonate);
                _local3 = actor[GILDE_GOLD];
                with (_local3) {
                    remove_event_listener(
                        MouseEvent.MOUSE_DOWN, GuildBtnDownHandler);
                    remove_event_listener(
                        MouseEvent.MOUSE_UP, GuildBtnUpHandler);
                    remove_event_listener(
                        MouseEvent.MOUSE_OUT, GuildBtnUpHandler);
                };
                _local3 = actor[GILDE_MUSH];
                with (_local3) {
                    remove_event_listener(
                        MouseEvent.MOUSE_DOWN, GuildBtnDownHandler);
                    remove_event_listener(
                        MouseEvent.MOUSE_UP, GuildBtnUpHandler);
                    remove_event_listener(
                        MouseEvent.MOUSE_OUT, GuildBtnUpHandler);
                };
                _local3 = actor[INP_GILDE_TEXT];
                with (_local3) {
                    remove_event_listener(FocusEvent.FOCUS_IN, EnterGuildDesc);
                    remove_event_listener(FocusEvent.FOCUS_OUT,
                                          LeaveGuildDesc);
                };
            };
        };
        var DonateVal:* = function (avg, localMax):String{
            var dval;
            dval = 1;
            if (avg >= 10000){
                dval = 10;
            } else {
                if (avg >= 5000){
                    dval = 10;
                } else {
                    if (avg >= 1000){
                        dval = 10;
                    } else {
                        if (avg >= 500){
                            dval = 5;
                        } else {
                            if (avg >= 100){
                                dval = 5;
                            } else {
                                if (avg >= 50){
                                    dval = 2;
                                } else {
                                    if (avg >= 10){
                                        dval = 1;
                                    } else {
                                        dval = 1;

            if (((!((cheapest == -1))) and ((dval > cheapest)))){
                dval = cheapest;
            };
            if (dval > localMax){
                dval = localMax;
            };
            if (dval < 1){
                dval = 1;
            };
            return (str(dval));
        };
        var GuildBtnDownHandler:* = function (evt:Event){
            var ClickCount:* = 0;
            var evt:* = evt;
            var DoPushGuildBtn:* = function (timerevt:Event){
                var timerevt:* = timerevt;
                if (destroy_guild_btn_timer){
                    destroy_guild_btn_timer = False;
                    var _local3 = GuildBtnRepeatTimer;
                    with (_local3) {
                        stop();
                        delay = 1000;
                        remove_event_listener(
                            TimerEvent.TIMER, DoPushGuildBtn);
                    };
                } else {
                    ClickCount++;
                    Switch (ClickCount){
                        if case(1:
                            GuildBtnRepeatTimer.delay = 500;
                            break;
                        if case(3:
                            GuildBtnRepeatTimer.delay = 250;
                            break;
                        if case(10:
                            GuildBtnRepeatTimer.delay = 125;
                            break;
                        if case(20:
                            GuildBtnRepeatTimer.delay = 62;
                            break;
                    };
                    if (GuildBtnHandler(evt, True)){
                        play(SND['CLICK']);
                    } else {
                        if (GuildBtnRepeatTimer.running){
                            destroy_guild_btn_timer = True;

            ClickCount = 0;
            if (GuildBtnRepeatTimer.running){
                return;
            };
            destroy_guild_btn_timer = False;
            var _local3 = GuildBtnRepeatTimer;
            with (_local3) {
                delay = 1000;
                add_event_listener(TimerEvent.TIMER, DoPushGuildBtn);
                start();
            };
        };
        var GuildBtnUpHandler:* = function (evt:Event){
            if (GuildBtnRepeatTimer.running){
                destroy_guild_btn_timer = True;
            };
        };
        var EnterGuildDesc:* = function (evt:FocusEvent){
            var evt:* = evt;
            var _local3 = actor[INP_GILDE_TEXT].getChildAt(0);
            with (_local3) {
                if (type == TextFieldType.INPUT){
                    if (text == texts[TXT_ENTERGUILDDESC]){
                        text = "";

        var LeaveGuildDesc:* = function (evt:FocusEvent){
            var evt:* = evt;
            var _local3 = actor[INP_GILDE_TEXT].getChildAt(0);
            with (_local3) {
                if (type == TextFieldType.INPUT){
                    if (text != resolve_breaks(guild_descr)){
                        guild_descr = semi_strip(text);
                        send_action(
                            ACT_GUILD_SET_DESC,
                            actor[INP['NAME']].getChildAt(1).text,
                            gilde,
                            ((oldcreststring + "§") + remove_illegal_chars(
                                semi_strip(text))),
                            MD5(actor[INP['LOGIN_PASSWORD']]
                                .getChildAt(1).text)
                        );
                    };
                    if (text == ""){
                        text = texts[TXT_ENTERGUILDDESC];

        var PlaceButtonSet:* = function (){
            var selRank;
            Switch (myRank){
                if case(1:
                    add(GILDE_SET_MASTER);
                    if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                        show(PLAYER_GUILD_INVITE);
                    };
                    break;
                if case(2:
                    add(GILDE_SET_OFFICER);
                    if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                        show(PLAYER_GUILD_INVITE);
                    };
                    break;
                if case(3:
                if case(0:
                    if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                        hide(PLAYER_GUILD_INVITE);
                    };
                    add(GILDE_SET_MEMBER);
                    break;
            };
            selRank = guild_data[
                ((GUILD_MEMBERRANK + selectLevel) + scrollLevel)];
            if (
                (((int(guild_data[((GUILD_MEMBERID + selectLevel)
                    + scrollLevel)]) == int(savegame[SG['PLAYER_ID']])))
                and (is_mine))
            ){
                add(GILDE_KICK);
                remove(GILDE_KICK_GRAY);
                remove(GILDE_PROMOTE);
                remove(GILDE_MASTER);
                add_some(GILDE_PROMOTE_GRAY, GILDE_MASTER_GRAY);
            } else {
                if ((((selRank <= 2)) and ((myRank == 2)))){
                    remove(GILDE_KICK);
                    add(GILDE_KICK_GRAY);
                };
            };
            if (selRank == 4){
                remove(GILDE_PROMOTE);
                remove(GILDE_MASTER);
                add_some(GILDE_PROMOTE_GRAY, GILDE_MASTER_GRAY);
            };
            if (int(guild_data[3]) >= int(guild_data[5])){
                remove(GILDE_INVITE);
                if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                    hide(PLAYER_GUILD_INVITE);
                };
                add_some(GILDE_INVITE_GRAY);
            };
            if ((((selRank == 2)) and ((myRank == 1)))){
                remove(GILDE_PROMOTE);
                add(GILDE_DEMOTE);
            };
            if (
                (((((((selRank == 1))
                and ((int(guild_data[12]) < 0))))
                and ((myRank <= 3))))
                and ((myRank > 0)))
            ){
                remove(GILDE_MASTER_GRAY);
                add(GILDE_REVOLT);
            };
        };
        GuildBtnHandler = function (
            evt:Event, typematic=False
        ):
            var actor_id:* = 0;
            var selRank:* = 0;
            var evt:* = evt;
            var typematic:Boolean = typematic;
            actor_id = get_actor_id(evt.target);
            selRank = guild_data[
                ((GUILD_MEMBERRANK + selectLevel) + scrollLevel)
            ];
            Switch (actor_id){
                if case(GILDE_SCROLL_UP:
                    scrollLevel = (scrollLevel - 15);
                    if (scrollLevel < 0){
                        scrollLevel = 0;
                    };
                    BuildGuildList();
                    break;
                if case(GILDE_SCROLL_DOWN:
                    scrollLevel = (scrollLevel + 15);
                    if (scrollLevel > (int(guild_data[3]) - 15)){
                        scrollLevel = (int(guild_data[3]) - 15);
                    };
                    if (scrollLevel < 0){
                        scrollLevel = 0;
                    };
                    BuildGuildList();
                    break;
                if case(GILDE_INVITE:
                    add(GILDE_DIALOG_INVITE);
                    actor[INP_GILDE_DIALOG_INVITE].getChildAt(1).text = "";
                    var _local4 = actor[LBL_WINDOW_TITLE];
                    with (_local4) {
                        text = texts[TXT_GILDE_INVITE_TITLE];
                        x = (
                            (IF_WIN_X + IF_WIN_WELCOME_X)
                            - int((text_width / 2)));
                    };
                    break;
                if case(GILDE_PROFILE:
                    request_player_screen();
                    break;
                if case(GILDE_REVOLT:
                    add(GILDE_DIALOG_REVOLT);
                    _local4 = actor[LBL_WINDOW_TITLE];
                    with (_local4) {
                        text = texts[TXT_REVOLT_WARNING_TITLE];
                        x = (
                            (IF_WIN_X + IF_WIN_WELCOME_X)
                            - int((text_width / 2)));
                    };
                    break;
                if case(GILDE_KICK:
                    if (selRank == 4){
                        KickMember();
                    } else {
                        add(GILDE_DIALOG_KICK);
                        if (int(guild_data[
                            ((GUILD_MEMBERID + selectLevel) + scrollLevel)
                            ]) == int(savegame[SG['PLAYER_ID']])
                        ){
                            remove(LBL_GILDE_DIALOG_TEXT_KICK);
                            add(LBL_GILDE_DIALOG_TEXT_QUIT);
                            _local4 = actor[LBL_WINDOW_TITLE];
                            with (_local4) {
                                text = texts[TXT_GILDE_QUIT_TITLE];
                                x = (
                                    (IF_WIN_X + IF_WIN_WELCOME_X)
                                    - int((text_width / 2)));
                            };
                        } else {
                            _local4 = actor[LBL_WINDOW_TITLE];
                            with (_local4) {
                                text = texts[TXT_GILDE_KICK_TITLE];
                                x = (
                                    (IF_WIN_X + IF_WIN_WELCOME_X)
                                    - int((text_width / 2)));
                            };
                        };
                    };
                    break;
                if case(GILDE_PROMOTE:
                if case(GILDE_DEMOTE:
                    ToggleOfficer();
                    break;
                if case(GILDE_MASTER:
                    add(GILDE_DIALOG_MASTER);
                    _local4 = actor[LBL_WINDOW_TITLE];
                    with (_local4) {
                        text = texts[TXT_GILDE_MASTER_TITLE];
                        x = (
                            (IF_WIN_X + IF_WIN_WELCOME_X)
                            - int((text_width / 2)));
                    };
                    break;
                if case(GILDE_DIALOG_OK_KICK:
                    KickMember();
                    break;
                if case(GILDE_DIALOG_OK_MASTER:
                    MakeMaster();
                    break;
                if case(GILDE_DIALOG_OK_INVITE:
                    InvitePlayer();
                    break;
                if case(GILDE_DIALOG_OK_REVOLT:
                    Revolt();
                    break;
                if case(GILDE_DIALOG_OK_RAID:
                    send_action(ACT_GUILD_COMMENCE_ATTACK, -1);
                    break;
                if case(GILDE_DIALOG_CANCEL:
                    remove(GILDE_DIALOG_INVITE);
                    remove(GILDE_DIALOG_KICK);
                    remove(GILDE_DIALOG_REVOLT);
                    remove(GILDE_DIALOG_MASTER);
                    remove(LBL_GILDE_DIALOG_TEXT_QUIT);
                    remove(GILDE_DIALOG_RAID);
                    break;
                if case(GILDE_KATAPULT:
                if case((GILDE_KATAPULT + 1):
                if case((GILDE_KATAPULT + 2):
                    send_action(
                        ACT_GUILD_IMPROVE,
                        actor[INP['NAME']].getChildAt(1).text,
                        gilde,
                        MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text),
                        0
                    );
                    break;
                if case(GILDE_GEBAEUDE_IMPROVE:
                if case((GILDE_GEBAEUDE_IMPROVE + 1):
                if case((GILDE_GEBAEUDE_IMPROVE + 2):
                    send_action(
                        ACT_GUILD_IMPROVE,
                        actor[INP['NAME']].getChildAt(1).text,
                        gilde,
                        MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text),
                        ((actor_id - GILDE_GEBAEUDE_IMPROVE) + 1)
                    );
                    break;
                if case(GILDE_GOLD:
                    if (int(savegame[SG_EMAIL_VALID]) == 1){
                        if ((((int(
                            actor[LBL_IF_GOLD].text
                            ) >= int(actor[LBL_GILDE_GOLD2].text)))
                            and (((int(actor[LBL_GILDE_GOLD].text)
                                + int(actor[LBL_GILDE_GOLD2].text)
                                ) <= 10000000)))
                        ){
                            GoldToDonate = (
                                GoldToDonate
                                + int(actor[LBL_GILDE_GOLD2].text));
                            actor[LBL_IF_GOLD].text = str(
                                (int(actor[LBL_IF_GOLD].text)
                                    - int(actor[LBL_GILDE_GOLD2].text)));
                            actor[LBL_GILDE_GOLD].text = str(
                                (int(actor[LBL_GILDE_GOLD].text)
                                    + int(actor[LBL_GILDE_GOLD2].text)));
                            DonateTimeout.stop();
                            DonateTimeout.start();
                        } else {
                            DoDonate();
                            if (int(
                                actor[LBL_IF_GOLD].text) >= int(
                                actor[LBL_GILDE_GOLD2].text)
                            ){
                                error_message(
                                    texts[TXT_ERROR_GUILD_CASH_FULL]);
                            } else {
                                if (!typematic){
                                    error_message(
                                        texts[TXT_ERROR_GUILD_TOO_EXPENSIVE]);
                                };
                            };
                            return (False);
                        };
                    } else {
                        error_message(
                            texts[TXT_ERROR_GUILD_EMAIL_VALIDATE]);
                        return (False);
                    };
                    break;
                if case(GILDE_MUSH:
                    if (int(savegame[SG_EMAIL_VALID]) == 1){
                        if (int(savegame[SG_FIRST_PAYMENT]) != 0){
                            if (int(
                                actor[LBL_IF_PILZE].text
                                ) >= int(actor[LBL_GILDE_MUSH2].text)
                            ){
                                MushToDonate = (
                                    MushToDonate
                                    + int(actor[LBL_GILDE_MUSH2].text));
                                actor[LBL_IF_PILZE].text = str(
                                    (int(actor[LBL_IF_PILZE].text)
                                        - int(actor[LBL_GILDE_MUSH2].text)));
                                actor[LBL_GILDE_MUSH].text = str(
                                    (int(actor[LBL_GILDE_MUSH].text)
                                        + int(actor[LBL_GILDE_MUSH2].text)));
                                enable_popup(LBL_IF_PILZE);
                                DonateTimeout.stop();
                                DonateTimeout.start();
                            } else {
                                DoDonate();
                                if (!typematic){
                                    error_message(
                                        texts[TXT_ERROR_GUILD_TOO_EXPENSIVE]);
                                };
                                return (False);
                            };
                        } else {
                            error_message(
                                texts[TXT_ERROR_GUILD_MUSH_FREE]);
                            return (False);
                        };
                    } else {
                        error_message(
                            texts[TXT_ERROR_GUILD_EMAIL_VALIDATE]);
                        return (False);
                    };
                    break;
            };
            return (True);
        };
        DoDonate = function (evt:Event=None){
            DonateTimeout.stop();
            if (GoldToDonate > 0){
                send_action(ACT_GUILD_DONATE, 1, str((GoldToDonate * 100)));
            } else {
                if (MushToDonate > 0){
                    send_action(ACT_GUILD_DONATE, 2, str(MushToDonate));
                };
            };
            GoldToDonate = 0;
            MushToDonate = 0;
        };
        RequestPlayerScreen = function (){
            var player_name:String;
            var selRank;
            player_name = guild_members[((selectLevel + scrollLevel) + 1)];
            if (player_name == ""){
                return;
            };
            sel_name = player_name;
            selRank = guild_data[
                ((GUILD_MEMBERRANK + selectLevel) + scrollLevel)
            ];
            sel_guild = (((selRank == 4)) ? "" : gilde);
            send_action(ACT['REQUEST']['CHAR'], player_name);
        };
        var InvitePlayer:* = function (){
            var sel_name:String;
            sel_name = guild_members[((selectLevel + scrollLevel) + 1)];
            if (sel_name == ""){
                return;
            };
            send_action(
                ACT_GUILD_INVITE,
                actor[INP['NAME']].getChildAt(1).text,
                gilde,
                actor[INP_GILDE_DIALOG_INVITE].getChildAt(1).text,
                MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text),
                ""
            );
        };
        var MakeMaster:* = function (){
            var sel_name:String;
            sel_name = guild_members[((selectLevel + scrollLevel) + 1)];
            if (sel_name == ""){
                return;
            };
            send_action(
                ACT_GUILD_SET_MASTER,
                actor[INP['NAME']].getChildAt(1).text,
                gilde,
                sel_name,
                MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text)
            );
        };
        var KickMember:* = function (){
            var sel_name:String;
            sel_name = guild_members[((selectLevel + scrollLevel) + 1)];
            if (sel_name == ""){
                return;
            };
            send_action(
                ACT_GUILD_EXPEL,
                actor[INP['NAME']].getChildAt(1).text,
                gilde,
                sel_name,
                MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text)
            );
        };
        var ToggleOfficer:* = function (){
            var sel_name:String;
            var selRank;
            sel_name = guild_members[((selectLevel + scrollLevel) + 1)];
            selRank = guild_data[
                ((GUILD_MEMBERRANK + selectLevel) + scrollLevel)
            ];
            if (sel_name == ""){
                return;
            };
            if (selRank == 2){
                send_action(
                    ACT_GUILD_SET_OFFICER,
                    actor[INP['NAME']].getChildAt(1).text,
                    gilde,
                    sel_name,
                    MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text),
                    0
                );
            } else {
                if (selRank == 3){
                    send_action(
                        ACT_GUILD_SET_OFFICER,
                        actor[INP['NAME']].getChildAt(1).text,
                        gilde,
                        sel_name,
                        MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text),
                        1
                    );
                };
            };
        };
        var Revolt:* = function (){
            send_action(ACT_REVOLT);
        };
        BuildGuildList = function (evt:Event=None){
            var i:* = 0;
            var j:* = 0;
            var tmpBalken:* = None;
            var isOnline:* = False;
            var attackError:* = False;
            var lvl:* = 0;
            var attackStatus:* = 0;
            var avgCount:* = None;
            var evt:* = evt;
            var AddGuildImage:* = function (rank, line){
                var tmp_obj:* = None;
                var rank:* = rank;
                var line:* = line;
                if (rank == 0){
                    rank = 4;
                };
                tmp_obj = new Bitmap(
                    actor[
                        ((GILDE_RANK + (((rank < 4)) ? rank : 3)) - 1)
                    ].content.bitmapData.clone()
                );
                var _local4 = tmp_obj;
                with (_local4) {
                    allow_smoothing = True;
                    force_smoothing = True;
                    smoothing = True;
                    mouse_enabled = True;
                    if (text_dir == "right"){
                        x = 180;
                    } else {
                        x = 2;
                    };
                    y = ((line * GILDE_LIST_Y) + 4);
                    alpha = (((rank == 4)) ? 0.5 : 1);
                };
                actor[GILDE_LIST].addChild(tmp_obj);
            };
            var BuildGuildPopup:* = function (evt:MouseEvent){
                var hoverLevel;
                var lvl;
                var attackStatus;
                var attackError:Boolean;
                var attackHint:String;
                hoverLevel = int(
                    ((actor[GILDE_LIST].getChildIndex(evt.target) - 1) / 2));
                lvl = int(guild_data[
                    ((GUILD_MEMBERLEVEL + hoverLevel) + scrollLevel)
                ]);
                attackStatus = 0;
                attackError = False;
                attackHint = "";
                while (lvl > 1000) {
                    lvl = (lvl - 1000);
                    attackStatus++;
                };
                if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                    if (
                        (((int(guild_data[GUILD_ATTACK_TARGET]) > 0))
                        and (!((attackStatus & 1))))
                    ){
                        attackError = True;
                    };
                    if (
                        (((int(guild_data[GUILD_DEFENCE_TARGET]) > 0))
                        and (!((attackStatus & 2))))
                    ){
                        attackError = True;
                    };
                } else {
                    if (
                        (((int(guild_data[GUILD_ATTACK_TARGET]) == int(
                            savegame[SG_GUILD_INDEX])))
                        and ((attackStatus & 1)))
                    ){
                        attackError = True;
                    };
                    if (
                        (((int(guild_data[GUILD_DEFENCE_TARGET]) == int(
                            savegame[SG_GUILD_INDEX])))
                        and ((attackStatus & 2)))
                    ){
                        attackError = True;
                    };
                };
                if (((showActivityTime) and (is_mine))){
                    if (Number(guild_data[
                        ((GUILD_MEMBERONLINE + hoverLevel) + scrollLevel)
                        ]) > 0
                    ){
                        enable_popup(
                            GILDE_LIST,
                            time_str(guild_data[
                                ((GUILD_MEMBERONLINE + hoverLevel)
                                    + scrollLevel)]));
                    } else {
                        enable_popup(GILDE_LIST, ":-(");
                    };
                    return;
                };
                if (attackError){
                    if (guild_data[0] != savegame[SG_GUILD_INDEX]){
                        if (
                            (((int(guild_data[GUILD_ATTACK_TARGET]) == int(
                                savegame[SG_GUILD_INDEX])))
                            and ((attackStatus & 1)))
                        ){
                            attackHint = (
                                attackHint + (chr(13) + texts[
                                    (TXT_ATTACK_STATUS + 3)]));
                        };
                        if (
                            (((int(guild_data[GUILD_DEFENCE_TARGET]) == int(
                                savegame[SG_GUILD_INDEX])))
                            and ((attackStatus & 2)))
                        ){
                            attackHint = (
                                attackHint + (chr(13) + texts[
                                    (TXT_ATTACK_STATUS + 4)]));
                        };
                        if (attackHint.length > 0){
                            attackHint = attackHint[1:]
                            if (text_dir == "right"){
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    ((("(" + texts[((TXT_RANKNAME
                                        + int(guild_data[
                                            ((GUILD_MEMBERRANK + hoverLevel)
                                            + scrollLevel)])) - 1)]) + ") ")
                                        + guild_members[((hoverLevel
                                            + scrollLevel) + 1)]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((str(lvl) + " ") +
                                        texts[TXT_HALL_LIST_COLUMN_4]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                FontFormatGuildListTextAttackErrorOnlinePopup,
                                    attackHint,
                                    POPUP_END_LINE
                                );
                            } else {
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    (((guild_members[((hoverLevel
                                        + scrollLevel) + 1)] + " (")
                                        + texts[((TXT_RANKNAME
                                            + int(guild_data[
                                                ((GUILD_MEMBERRANK
                                                + hoverLevel)
                                                + scrollLevel)])) - 1)
                                        ]) + ")"),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                                        + str(lvl)),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                            FontFormatGuildListTextAttackErrorOnlinePopup,
                                    attackHint,
                                    POPUP_END_LINE
                                );
                            };
                        } else {
                            if (text_dir == "right"){
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    ((("(" + texts[((TXT_RANKNAME
                                        + int(guild_data[((GUILD_MEMBERRANK
                                            + hoverLevel) + scrollLevel)]))
                                            - 1)]) + ") ") + guild_members[
                                        ((hoverLevel + scrollLevel) + 1)]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((str(lvl) + " ") + texts[
                                        TXT_HALL_LIST_COLUMN_4]),
                                    POPUP_END_LINE
                                );
                            } else {
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    (((guild_members[((hoverLevel
                                        + scrollLevel) + 1)] + " (")
                                        + texts[((TXT_RANKNAME
                                        + int(guild_data[((GUILD_MEMBERRANK
                                        + hoverLevel) + scrollLevel)]))
                                        - 1)]) + ")"),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                                        + str(lvl)),
                                    POPUP_END_LINE
                                );
                            };
                        };
                    } else {
                        if (text_dir == "right"){
                            enable_popup(
                                GILDE_LIST,
                                POPUP_BEGIN_LINE,
                                ((("(" + texts[((TXT_RANKNAME
                                    + int(guild_data[((GUILD_MEMBERRANK
                                    + hoverLevel) + scrollLevel)])) - 1)])
                                    + ") ") + guild_members[((hoverLevel
                                    + scrollLevel) + 1)]),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                ((str(lvl) + " ")
                                    + texts[TXT_HALL_LIST_COLUMN_4]),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                texts[TXT_GOLD_SPENT],
                                170,
                                str(int((guild_data[((GUILD_MEMBERGOLDSPENT
                                    + hoverLevel) + scrollLevel)] / 100))),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                texts[TXT_MUSH_SPENT],
                                170,
                                str(guild_data[((GUILD_MEMBERMUSHSPENT
                                    + hoverLevel) + scrollLevel)]),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                    FontFormatGuildListTextAttackErrorOnlinePopup,
                                texts[(TXT_ATTACK_STATUS + attackStatus)],
                                POPUP_END_LINE
                            );
                        } else {
                            enable_popup(
                                GILDE_LIST,
                                POPUP_BEGIN_LINE,
                                (((guild_members[((hoverLevel + scrollLevel)
                                    + 1)] + " (") + texts[((TXT_RANKNAME
                                    + int(guild_data[((GUILD_MEMBERRANK
                                    + hoverLevel) + scrollLevel)])) - 1)])
                                    + ")"),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                                    + str(lvl)),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                texts[TXT_GOLD_SPENT],
                                170,
                                str(int((guild_data[((GUILD_MEMBERGOLDSPENT
                                    + hoverLevel) + scrollLevel)] / 100))),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                texts[TXT_MUSH_SPENT],
                                170,
                                str(guild_data[((GUILD_MEMBERMUSHSPENT
                                    + hoverLevel) + scrollLevel)]),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                        FontFormatGuildListTextAttackErrorOnlinePopup,
                                texts[(TXT_ATTACK_STATUS + attackStatus)],
                                POPUP_END_LINE
                            );
                        };
                    };
                } else {
                    if (guild_data[0] != savegame[SG_GUILD_INDEX]){
                        if (text_dir == "right"){
                            enable_popup(
                                GILDE_LIST,
                                POPUP_BEGIN_LINE,
                                ((("(" + texts[((TXT_RANKNAME +
                                    int(guild_data[((GUILD_MEMBERRANK
                                    + hoverLevel) + scrollLevel)])) - 1)])
                                    + ") ") + guild_members[((hoverLevel
                                    + scrollLevel) + 1)]),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                ((str(lvl) + " ") + texts[
                                    TXT_HALL_LIST_COLUMN_4]),
                                POPUP_END_LINE
                            );
                        } else {
                            enable_popup(
                                GILDE_LIST,
                                POPUP_BEGIN_LINE,
                                (((guild_members[((hoverLevel + scrollLevel)
                                    + 1)] + " (") + texts[((TXT_RANKNAME
                                    + int(guild_data[((GUILD_MEMBERRANK
                                    + hoverLevel) + scrollLevel)])) - 1)])
                                    + ")"),
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                                    + str(lvl)),
                                POPUP_END_LINE
                            );
                        };
                    } else {
                        if (text_dir == "right"){
                            if (attackStatus == 0){
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    ((("(" + texts[((TXT_RANKNAME
                                        + int(guild_data[((GUILD_MEMBERRANK
                                        + hoverLevel) + scrollLevel)])) - 1)])
                                        + ") ") + guild_members[((hoverLevel
                                        + scrollLevel) + 1)]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((str(lvl) + " ") + texts[
                                        TXT_HALL_LIST_COLUMN_4]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_GOLD_SPENT],
                                    170,
                                    str(int((guild_data[
                                        ((GUILD_MEMBERGOLDSPENT
                                        + hoverLevel) + scrollLevel)]
                                        / 100))),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_MUSH_SPENT],
                                    170,
                                    str(guild_data[((GUILD_MEMBERMUSHSPENT
                                        + hoverLevel) + scrollLevel)]),
                                    POPUP_END_LINE
                                );
                            } else {
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    ((("(" + texts[((TXT_RANKNAME
                                        + int(guild_data[((GUILD_MEMBERRANK
                                        + hoverLevel)
                                        + scrollLevel)])) - 1)])
                                        + ") ") + guild_members[((hoverLevel
                                        + scrollLevel) + 1)]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((str(lvl) + " ") +
                                        texts[TXT_HALL_LIST_COLUMN_4]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_GOLD_SPENT],
                                    170,
                                    str(int((guild_data[((
                                        GUILD_MEMBERGOLDSPENT + hoverLevel)
                                        + scrollLevel)] / 100))),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_MUSH_SPENT],
                                    170,
                                    str(guild_data[((GUILD_MEMBERMUSHSPENT
                                        + hoverLevel) + scrollLevel)]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    FontFormatGuildListTextAttackOkPopup,
                                    texts[(TXT_ATTACK_OK_STATUS +
                                        attackStatus)],
                                    POPUP_END_LINE
                                );
                            };
                        } else {
                            if (attackStatus == 0){
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    (((guild_members[((hoverLevel
                                        + scrollLevel) + 1)] + " (")
                                        + texts[((TXT_RANKNAME
                                        + int(guild_data[((GUILD_MEMBERRANK
                                        + hoverLevel) + scrollLevel)])) - 1)])
                                        + ")"),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                        ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                                            + str(lvl)),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_GOLD_SPENT],
                                    170,
                                    str(int((guild_data[((GUILD_MEMBERGOLDSPENT
                                        + hoverLevel) + scrollLevel)] / 100))),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_MUSH_SPENT],
                                    170,
                                    str(guild_data[((GUILD_MEMBERMUSHSPENT
                                        + hoverLevel) + scrollLevel)]),
                                    POPUP_END_LINE
                                );
                            } else {
                                enable_popup(
                                    GILDE_LIST,
                                    POPUP_BEGIN_LINE,
                                    (((guild_members[
                                        ((hoverLevel + scrollLevel)
                                        + 1)] + " (") + texts[((TXT_RANKNAME
                                        + int(guild_data[((GUILD_MEMBERRANK
                                        + hoverLevel) + scrollLevel)])) - 1)])
                                        + ")"),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                                        + str(lvl)),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_GOLD_SPENT],
                                    170,
                                    str(int((guild_data[((GUILD_MEMBERGOLDSPENT
                                        + hoverLevel) + scrollLevel)] / 100))),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[TXT_MUSH_SPENT],
                                    170,
                                    str(guild_data[((GUILD_MEMBERMUSHSPENT
                                        + hoverLevel) + scrollLevel)]),
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    FontFormatGuildListTextAttackOkPopup,
                                    texts[TXT_ATTACK_OK_STATUS + attackStatus],
                                    POPUP_END_LINE
                                );

            var RemoveGuildPopup:* = function (evt:MouseEvent){
                enable_popup(GILDE_LIST);
            };

            var AddGuildPlayer:* = function (
                memberName:String, rank, line, onlineStatus:Boolean,
                thisAttackError:Boolean, thisAttackStatus
            ){
                var tmp_obj:* = None;
                var memberName:* = memberName;
                var rank:* = rank;
                var line:* = line;
                var onlineStatus:* = onlineStatus;
                var thisAttackError:* = thisAttackError;
                var thisAttackStatus:* = thisAttackStatus;
                tmp_obj = new TextField();
                double_click_handler(
                    tmp_obj, BuildGuildList, RequestPlayerScreen
                );
                var _local8 = tmp_obj;
                with (_local8) {
                    add_event_listener(MouseEvent.MOUSE_OVER, BuildGuildPopup);
                    add_event_listener(MouseEvent.MOUSE_OUT, RemoveGuildPopup);
                    if (thisAttackError){
                        if (is_mine){
                            if (
                                (((thisAttackStatus & 1))
                                 or ((thisAttackStatus & 2)))
                            ){
                                tmp_obj.default_text_format = (
                                    (onlineStatus)
                                ? FontFormatGuildListTextAttackErrorOnlineHalf
                                : FontFormatGuildListTextAttackErrorHalf
                                );
                            } else {
                                tmp_obj.default_text_format = (
                                    (onlineStatus)
                                    ? FontFormatGuildListTextAttackErrorOnline
                                    : FontFormatGuildListTextAttackError
                                );
                            };
                        } else {
                            if (
                                !(((thisAttackStatus & 1))
                                and ((thisAttackStatus & 2)))
                            ){
                                tmp_obj.default_text_format =
                                    FontFormatGuildListTextAttackErrorHalf;
                            } else {
                                tmp_obj.default_text_format =
                                    FontFormatGuildListTextAttackError;
                            };
                        };
                    } else {
                        tmp_obj.default_text_format = (
                            (((onlineStatus) and (is_mine)))
                                ? FontFormatGuildListTextOnline
                                : FontFormatGuildListText
                            );
                    };
                    auto_size = TextFieldAutoSize.LEFT;
                    background = False;
                    selectable = False;
                    embed_fonts = font_embedded;
                    anti_alias_type = AntiAliasType.ADVANCED;
                    mouse_enabled = True;
                    filters = Filter_Shadow;
                    text = memberName;
                    if (text_dir == "right"){
                        x = (172 - text_width);
                    } else {
                        x = GILDE_LIST_C1;
                    };
                    y = ((line * GILDE_LIST_Y) + 0);
                    alpha = (((rank == 4)) ? 0.5 : 1);
                };
                actor[GILDE_LIST].addChild(tmp_obj);
            };
            i = 0;
            j = 0;
            isOnline = False;
            attackError = False;
            lvl = 0;
            attackStatus = 0;
            if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                offline_guild_members = list();
            };
            if ((evt is MouseEvent)){
                selectLevel = int(((
                    actor[GILDE_LIST].getChildIndex(evt.target) - 1) / 2));
            };
            var _local3 = actor[GILDE_LIST];
            with (_local3) {
                while (numChildren > 0) {
                    removeChildAt(0);
                };
                mouse_enabled = True;
                doubleClickEnabled = True;
                mouseChildren = True;
            };
            tmpBalken = new MovieClip();
            _local3 = tmpBalken.graphics;
            with (_local3) {
                beginFill(CLR_SFORANGE, 0.5);
                lineStyle(0, 0, 0);
                drawRect(0, 0, GILDE_LIST_X, GILDE_LIST_Y);
            };
            _local3 = tmpBalken;
            with (_local3) {
                x = 0;
                y = (selectLevel * GILDE_LIST_Y);
                mouse_enabled = True;
                doubleClickEnabled = True;
            };
            actor[GILDE_LIST].addChild(tmpBalken);
            j = 0;
            avgLevel = 0;
            avgCount = 0;
            if (scrollLevel == -1){
                i = 0;
                while (i < int(guild_data[3])) {
                    if (int(guild_data[(GUILD_MEMBERID + i)]) == int(
                        savegame[SG['PLAYER_ID']])
                    ){
                        scrollLevel = (i - 7);
                    };
                    i = (i + 1);
                };
                if (scrollLevel > (int(guild_data[3]) - 15)){
                    scrollLevel = (int(guild_data[3]) - 15);
                };
                if (scrollLevel < 0){
                    scrollLevel = 0;
                };
            };
            i = 0;
            while (i < int(guild_data[3])) {
                isOnline = waiting_for((Number(
                    guild_data[(GUILD_MEMBERONLINE + i)]) + (60 * 5)));
                lvl = int(guild_data[(GUILD_MEMBERLEVEL + i)]);
                attackStatus = 0;
                attackError = False;
                while (lvl > 1000) {
                    lvl = (lvl - 1000);
                    attackStatus = (attackStatus + 1);
                };
                if (int(guild_data[(GUILD_MEMBERID + i)]) == int(
                    savegame[SG['PLAYER_ID']])
                ){
                    myRank = int(guild_data[(GUILD_MEMBERRANK + i)]);
                    myAttackStatus = int(
                        (Number(guild_data[(GUILD_MEMBERLEVEL + i)]) / 1000)
                    );
                };
                if (
                    (((int(guild_data[(GUILD_MEMBERRANK + i)]) > 0))
                    and ((int(guild_data[(GUILD_MEMBERRANK + i)]) < 4)))
                ){
                    avgLevel = (avgLevel + lvl);
                    avgCount = (avgCount + 1);
                };
                if (guild_data[0] == savegame[SG_GUILD_INDEX]){
                    if (!isOnline){
                        offline_guild_members.append(guild_members[(i + 1)]);
                    };
                    if (
                        (((int(guild_data[GUILD_ATTACK_TARGET]) > 0))
                        and (!((attackStatus & 1))))
                    ){
                        attackError = True;
                    };
                    if (
                        (((int(guild_data[GUILD_DEFENCE_TARGET]) > 0))
                        and (!((attackStatus & 2))))
                    ){
                        attackError = True;
                    };
                } else {
                    if (
                        (((int(guild_data[GUILD_ATTACK_TARGET]) == int(
                        savegame[SG_GUILD_INDEX]))) and ((attackStatus & 1)))
                    ){
                        attackError = True;
                    };
                    if ((((int(guild_data[GUILD_DEFENCE_TARGET]) == int(
                        savegame[SG_GUILD_INDEX]))) and ((attackStatus & 2)))
                    ){
                        attackError = True;
                    };
                };
                if ((((i >= scrollLevel)) and ((i < (scrollLevel + 15))))){
                    AddGuildImage(int(guild_data[(GUILD_MEMBERRANK + i)]), j);
                    j = (j + 1);
                    AddGuildPlayer(
                        guild_members[(i + 1)],
                        int(guild_data[(GUILD_MEMBERRANK + i)]),
                        j,
                        isOnline,
                        attackError,
                        attackStatus
                    );
                };
                i = (i + 1);
            };
            avgLevel = (avgLevel / avgCount);
            PlaceButtonSet();
            if (text_dir == "right"){
                actor[GILDE_SCROLL_UP].x = GILDE_LIST_X;
                actor[GILDE_SCROLL_DOWN].x = GILDE_LIST_X;
                actor[GILDE_CHAT_UP].x = (GILDE_GEBAEUDE_X - 2);
                actor[GILDE_CHAT_DOWN].x = (GILDE_GEBAEUDE_X - 2);
                actor[GILDE_LIST].x = (
                    (actor[GILDE_SCROLL_UP].x
                    + actor[GILDE_SCROLL_UP].width) + 5
                );
                actor[INP_GILDE_CHAT].x = (
                    (actor[GILDE_CHAT_UP].x + actor[GILDE_CHAT_UP].width) + 5
                );
                i = 0;
                while (i < 40) {
                    actor[(LBL['GILDE']['CHAT'] + i)].x = (
                        (actor[INP_GILDE_CHAT].x + actor[INP_GILDE_CHAT].width)
                        - actor[(LBL['GILDE']['CHAT'] + i)].text_width
                    );
                    actor[(LBL['GILDE']['CHAT'] + i)].auto_size = "right";
                    i = (i + 1);

        i = 0;
        myRank = 0;
        myAttackStatus = 0;
        scrollLevel = -1;
        selectLevel = 0;
        GoldToDonate = 0;
        MushToDonate = 0;
        DonateTimeout = new Timer(2000, 1);
        DonateTimeout.add_event_listener(TimerEvent.TIMER, DoDonate);
        guildInstanceID++;
        if (guildInstanceID > 10000){
            guildInstanceID = 0;
        };
        thisInstanceID = guildInstanceID;
        removeListenersTimer = new Timer(20);
        var _local3 = removeListenersTimer;
        with (_local3) {
            add_event_listener(TimerEvent.TIMER, removeListeners);
            start();
        };
        GoldKosten = 10;
        PilzKosten = 10;
        Nutzen = "";
        Ausbaustufe = 1;
        AusbaustufeEx = 1;
        GoldKostenAvg = 0;
        PilzKostenAvg = 0;
        cheapest = -1;
        countCompleted = 0;
        i = 0;
        while (i < 3) {
            Ausbaustufe = guild_data[(i + 5)];
            AusbaustufeEx = (
                Ausbaustufe + ((i)==0)
                    ? 0
                    : int(guild_data[GUILD_RAID_LEVEL])
            );
            GoldKosten = int((GildeBuildingGold[(Ausbaustufe + 1)] / 100));
            PilzKosten = GildeBuildingPilz[(Ausbaustufe + 1)];
            Switch (i){
                if case(0:
                    if (AusbaustufeEx > 50){
                        Nutzen = "50";
                    } else {
                        Nutzen = str(AusbaustufeEx);
                    };
                    break;
                if case(1:
                    Nutzen = (str((AusbaustufeEx * 2)) + "%");
                    break;
                if case(2:
                    Nutzen = (str((AusbaustufeEx * 2)) + "%");
                    break;
            };
            actor[(LBL_GILDE_GEBAEUDE_WERT + i)].text = Nutzen;
            actor[(LBL_GILDE_GEBAEUDE_STUFE + i)].text = str(AusbaustufeEx);
            if (text_dir == "right"){
                actor[(LBL_GILDE_GEBAEUDE_NAME + i)].x = (
                    ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                    - actor[(LBL_GILDE_GEBAEUDE_NAME + i)].text_width
                );
                actor[(LBL_GILDE_GEBAEUDE_WERT_CAPTION + i)].x = (
                    ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                    - actor[(LBL_GILDE_GEBAEUDE_WERT_CAPTION + i)].text_width
                );
                actor[(LBL_GILDE_GEBAEUDE_WERT + i)].x = (
                    ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                    - actor[(LBL_GILDE_GEBAEUDE_WERT + i)].text_width
                );
                actor[(LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i)].x = (
                    ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                    - actor[(LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i)].text_width
                );
                actor[(LBL_GILDE_GEBAEUDE_STUFE + i)].x = (
                    (actor[(LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i)].x
                    - actor[(LBL_GILDE_GEBAEUDE_STUFE + i)].text_width) - 5
                );
                actor[(GILDE_GEBAEUDE_IMPROVE + i)].y = actor[
                    (LBL_GILDE_GEBAEUDE_NAME + i)
                ].y;
                actor[(GILDE_GEBAEUDE_IMPROVE_GRAY + i)].y = actor[
                    (LBL_GILDE_GEBAEUDE_NAME + i)
                ].y;
            };
            set_cnt((GILDE_GEBAEUDE_GOLD + i), IF_GOLD);
            set_cnt((GILDE_GEBAEUDE_MUSH + i), IF_PILZE);
            hide(
                (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i),
                (GILDE_GEBAEUDE_GOLD + i)
            );
            hide(
                (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i),
                (GILDE_GEBAEUDE_MUSH + i)
            );
            if (Ausbaustufe >= 50){
                countCompleted = (countCompleted + 1);
                show((LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i));
                actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].text = texts[
                    TXT_BUILDING_COMPLETE
                ];
                if (text_dir == "right"){
                    actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].x = (
                        ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                        - actor[LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i].text_width
                    );
                } else {
                    actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].x = (
                        GILDE_GEBAEUDE_X + GILDE_TEXT_X
                    );
                };
            } else {
                if (GoldKosten > 0){
                    show(
                        (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i),
                        (GILDE_GEBAEUDE_GOLD + i)
                    );
                    actor[
                        (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)
                    ].text = str(GoldKosten);
                    if (text_dir == "right"){
                        actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].x = (
                            ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                            - actor[
                                (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)
                            ].text_width);
                        actor[(GILDE_GEBAEUDE_GOLD + i)].x = (
                            (actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].x
                            - actor[
                                (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)
                            ].text_width) - 7);
                    } else {
                        actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].x = (
                            GILDE_GEBAEUDE_X + GILDE_TEXT_X
                        );
                        actor[(GILDE_GEBAEUDE_GOLD + i)].x = (
                            (actor[(LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)].x
                            + actor[
                                (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i)
                            ].text_width) + 7);
                    };
                    if ((((cheapest == -1)) or ((GoldKosten < cheapest)))){
                        cheapest = GoldKosten;
                    };
                };
                if (PilzKosten > 0){
                    show(
                        (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i),
                        (GILDE_GEBAEUDE_MUSH + i)
                    );
                    actor[
                        (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)
                    ].text = str(PilzKosten);
                    if (text_dir == "right"){
                        if (GoldKosten > 0){
                            actor[(LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)].x = (
                                (actor[(GILDE_GEBAEUDE_GOLD + i)].x
                                - actor[
                                    (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)
                                ].text_width) - 10);
                        } else {
                            actor[(LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)].x = (
                                ((GILDE_GEBAEUDE_X + GILDE_TEXT_X) + 130)
                                - actor[
                                    (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)
                                ].text_width);
                        };
                        actor[(GILDE_GEBAEUDE_MUSH + i)].x = (
                            (actor[(LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)].x
                            - actor[(GILDE_GEBAEUDE_MUSH + i)].width) - 7
                        );
                    } else {
                        if (GoldKosten > 0){
                            actor[(LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)].x = (
                                (actor[(GILDE_GEBAEUDE_GOLD + i)].x
                                + actor[(GILDE_GEBAEUDE_GOLD + i)].width) + 10
                            );
                        } else {
                            actor[(LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)].x = (
                                GILDE_GEBAEUDE_X + GILDE_TEXT_X
                            );
                        };
                        actor[(GILDE_GEBAEUDE_MUSH + i)].x = (
                            (actor[(LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)].x
                            + actor[
                                (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i)
                            ].text_width) + 7);
                    };
                };
            };
            GoldKostenAvg = (GoldKostenAvg + GoldKosten);
            PilzKostenAvg = (PilzKostenAvg + PilzKosten);
            i = (i + 1);
        };
        GoldKostenAvg = (GoldKostenAvg / 3);
        PilzKostenAvg = (PilzKostenAvg / 3);
        actor[LBL_GILDE_GOLD2].text = get_spend_amount();
        actor[LBL_GILDE_MUSH2].text = "1";
        actor[GILDE_GOLD2].x = (
            (actor[LBL_GILDE_GOLD2].x
            + actor[LBL_GILDE_GOLD2].text_width) + 15
        );
        actor[GILDE_MUSH2].x = (
            (actor[LBL_GILDE_GOLD2].x + actor[LBL_GILDE_GOLD2].text_width) + 15
        );
        set_cnt(GILDE_GOLD, IF_GOLD);
        set_cnt(GILDE_GOLD2, IF_GOLD);
        set_cnt(GILDE_MUSH, IF_PILZE);
        set_cnt(GILDE_MUSH2, IF_PILZE);
        RightBoxWidth = (((
            (actor[GILDE_GOLD].width + GILDE_GOLDMUSH_C1)
            + actor[LBL_GILDE_GOLD2].text_width)
            + GILDE_GOLDMUSH_C1)
            + actor[GILDE_GOLD2].width
        );
        if (
            ((((actor[GILDE_MUSH].width + GILDE_GOLDMUSH_C1)
            + actor[LBL_GILDE_MUSH2].text_width)
            + GILDE_GOLDMUSH_C1)
            + actor[GILDE_MUSH2].width) > RightBoxWidth
        ){
            RightBoxWidth = (
                (((actor[GILDE_MUSH].width + GILDE_GOLDMUSH_C1)
                + actor[LBL_GILDE_MUSH2].text_width)
                + GILDE_GOLDMUSH_C1)
                + actor[GILDE_MUSH2].width
            );
        };
        if (text_dir == "right"){
            actor[GILDE_GOLD].x = (
                ((GILDE_GOLDMUSH_X + GILDE_GOLDMUSH_C2)
                + int((RightBoxWidth / 2))) - actor[GILDE_GOLD].width
            );
            actor[GILDE_MUSH].x = actor[GILDE_GOLD].x;
            actor[LBL_GILDE_GOLD2].x = (
                (actor[GILDE_GOLD].x - actor[LBL_GILDE_GOLD2].text_width)
                - GILDE_GOLDMUSH_C1
            );
            actor[LBL_GILDE_MUSH2].x = (
                (actor[GILDE_MUSH].x - actor[LBL_GILDE_MUSH2].text_width)
                - GILDE_GOLDMUSH_C1
            );
            actor[GILDE_GOLD2].x = (
                (actor[LBL_GILDE_GOLD2].x - actor[GILDE_GOLD2].width)
                - GILDE_GOLDMUSH_C1
            );
            actor[GILDE_MUSH2].x = (
                (actor[LBL_GILDE_MUSH2].x - actor[GILDE_MUSH2].width)
                - GILDE_GOLDMUSH_C1
            );
        } else {
            actor[GILDE_GOLD].x = (
                (GILDE_GOLDMUSH_X + GILDE_GOLDMUSH_C2)
                - int((RightBoxWidth / 2))
            );
            actor[GILDE_MUSH].x = actor[GILDE_GOLD].x;
            actor[LBL_GILDE_GOLD2].x = (
                (actor[GILDE_GOLD].x + actor[GILDE_GOLD].width)
                + GILDE_GOLDMUSH_C1
            );
            actor[LBL_GILDE_MUSH2].x = (
                (actor[GILDE_MUSH].x + actor[GILDE_MUSH].width)
                + GILDE_GOLDMUSH_C1
            );
            actor[GILDE_GOLD2].x = (
                (actor[LBL_GILDE_GOLD2].x + actor[LBL_GILDE_GOLD2].text_width)
                + GILDE_GOLDMUSH_C1
            );
            actor[GILDE_MUSH2].x = (
                (actor[LBL_GILDE_MUSH2].x + actor[LBL_GILDE_MUSH2].text_width)
                + GILDE_GOLDMUSH_C1
            );
        };
        _local3 = actor[LBL_GILDE_GOLD];
        with (_local3) {
            text = str(int((guild_data[1] / 100)));
            LeftBoxWidth = (
                (text_width + GILDE_GOLDMUSH_C1) + actor[GILDE_GOLD].width
            );
        };
        _local3 = actor[LBL_GILDE_MUSH];
        with (_local3) {
            text = guild_data[2];
            if (
                ((text_width + GILDE_GOLDMUSH_C1) + actor[GILDE_MUSH].width)
                > LeftBoxWidth
            ){
                LeftBoxWidth = (
                    (text_width + GILDE_GOLDMUSH_C1) + actor[GILDE_MUSH].width)
            };
            if (text_dir == "right"){
                actor[GILDE_MUSH].x = (
                    (GILDE_GOLDMUSH_X + int((LeftBoxWidth / 2)))
                    - actor[GILDE_MUSH].width
                );
                actor[GILDE_GOLD].x = actor[GILDE_MUSH].x;
                actor[LBL_GILDE_GOLD].x = (
                    (actor[GILDE_GOLD].x - actor[LBL_GILDE_GOLD].text_width)
                    - GILDE_GOLDMUSH_C1
                );
                x = ((actor[GILDE_MUSH].x - actor[LBL_GILDE_MUSH].text_width)
                    - GILDE_GOLDMUSH_C1);
            } else {
                actor[GILDE_MUSH].x = (
                   GILDE_GOLDMUSH_X - int((LeftBoxWidth / 2))
                );
                actor[GILDE_GOLD].x = actor[GILDE_MUSH].x;
                actor[LBL_GILDE_GOLD].x = (
                    (actor[GILDE_GOLD].x + actor[GILDE_GOLD].width)
                    + GILDE_GOLDMUSH_C1);
                x = (
                    (actor[GILDE_MUSH].x + actor[GILDE_MUSH].width)
                    + GILDE_GOLDMUSH_C1);
            };
        };
        crestView = on_stage(GILDE_CREST);
        startWithCrest = (
            (((((((((is_mine)
            or ((guild_data[0] == savegame[SG_GUILD_INDEX]))))
            and ((guild_data[5] >= 50))))
            and ((guild_data[6] >= 50))))
            and ((guild_data[7] >= 50))))
            and (!(on_stage(GILDE_SCROLL_UP)))
        );
        if (guild_data[0] != last_guild_crest_id){
            crestView = False;
        };
        last_guild_crest_id = guild_data[0];
        remove_all();
        add(SCREEN_GILDEN);
        if (crestView){
            if (actor[GILDE_CREST].y == GILDE_GEBAEUDE_Y){
                set_alpha(GILDE_CREST_CONTROLS, 1);
                add(GILDE_CREST_CONTROLS);
            };
            remove(GILDE_GEBAEUDE);
        } else {
            actor[GILDE_CREST].y = (GILDE_GEBAEUDE_Y + 60);
            selecterCrestElement = -1;
            if (((is_mine) or ((guild_data[0] == savegame[SG_GUILD_INDEX])))){
                if (startWithCrest){
                    remove(GILDE_GEBAEUDE);
                } else {
                    remove(GILDE_CREST);
                };
                actor[GILDE_CREST].mouseChildren = True;
            } else {
                remove(GILDE_CREST_GOTO_GEBAEUDE);
                actor[GILDE_CREST].mouseChildren = False;
            };
            load_crest();
        };
        if (!((is_mine) or ((guild_data[0] == savegame[SG_GUILD_INDEX])))){
            remove(GILDE_CREST_GOTO_GEBAEUDE);
            actor[GILDE_CREST].mouseChildren = False;
        };
        if (text_dir == "right"){
            actor[LBL['GILDE']['CHAT']_CAPTION].x = (
                (actor[GILDE_RAID].x -
                 actor[LBL['GILDE']['CHAT']_CAPTION].text_width)
                - 5);
            actor[GILDE_LINK].x = (
                (actor[GILDE_RAID].x - actor[LBL_GILDE_LINK].text_width) - 5
            );
            actor[INP_GILDE_TEXT].x = (GILDE_TEXT_X - 5);
            make_right_text_area(INP_GILDE_TEXT, 0);
            make_right_text_area(INP_GILDE_CHAT, 0);
        };
        i = 0;
        while (i < 3) {
            Ausbaustufe = guild_data[(i + 5)];
            if (Ausbaustufe >= 50){
                hide((GILDE_GEBAEUDE_IMPROVE + i));
                show((GILDE_GEBAEUDE_IMPROVE_GRAY + i));
            };
            i = (i + 1);
        };
        GuildBtnRepeatTimer = new Timer(1000);
        actor[GILDE_SCROLL_UP].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_SCROLL_DOWN].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DIALOG_CANCEL].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DIALOG_OK_KICK].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DIALOG_OK_MASTER].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DIALOG_OK_INVITE].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DIALOG_OK_REVOLT].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DIALOG_OK_RAID].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_INVITE].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_PROFILE].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_KICK].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_PROMOTE].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_DEMOTE].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_MASTER].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_REVOLT].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_GEBAEUDE_IMPROVE].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[(GILDE_GEBAEUDE_IMPROVE + 1)].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[(GILDE_GEBAEUDE_IMPROVE + 2)].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_KATAPULT].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[(GILDE_KATAPULT + 1)].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[(GILDE_KATAPULT + 2)].add_event_listener(
            MouseEvent.CLICK, GuildBtnHandler
        );
        actor[GILDE_GOLD].add_event_listener(
            MouseEvent.MOUSE_DOWN, GuildBtnHandler
        );
        actor[GILDE_MUSH].add_event_listener(
            MouseEvent.MOUSE_DOWN, GuildBtnHandler
        );
        actor[GILDE_GOLD].add_event_listener(
            MouseEvent.MOUSE_OUT, DoDonate
        );
        actor[GILDE_MUSH].add_event_listener(
            MouseEvent.MOUSE_OUT, DoDonate
        );

        with (actor[GILDE_GOLD]) {
            add_event_listener(MouseEvent.MOUSE_DOWN, GuildBtnDownHandler);
            add_event_listener(MouseEvent.MOUSE_UP, GuildBtnUpHandler);
            add_event_listener(MouseEvent.MOUSE_OUT, GuildBtnUpHandler);
        };
        _local3 = actor[GILDE_MUSH];
        with (_local3) {
            add_event_listener(MouseEvent.MOUSE_DOWN, GuildBtnDownHandler);
            add_event_listener(MouseEvent.MOUSE_UP, GuildBtnUpHandler);
            add_event_listener(MouseEvent.MOUSE_OUT, GuildBtnUpHandler);
        };
        BuildGuildList();
        if (myRank > 2){
            hide(
                GILDE_GEBAEUDE_IMPROVE,
                (GILDE_GEBAEUDE_IMPROVE + 1),
                (GILDE_GEBAEUDE_IMPROVE + 2)
            );
            show(
                GILDE_GEBAEUDE_IMPROVE_GRAY,
                (GILDE_GEBAEUDE_IMPROVE_GRAY + 1),
                (GILDE_GEBAEUDE_IMPROVE_GRAY + 2)
            );
        };
        _local3 = actor[LBL_SCREEN_TITLE];
        with (_local3) {
            text = this_gilde;
            x = (SCREEN_TITLE_X - int((text_width / 2)));
            y = SCREEN_TITLE_Y_GUILD;
        };
        _local3 = actor[LBL_GILDE_CREST_INSCRIPTION];
        with (_local3) {
            text = this_gilde;
            x = (120 - int((text_width / 2)));
        };
        _local3 = actor[LBL_GILDE_RANG];
        with (_local3) {
            if (
                (((int(guild_data[GUILD_RAID_LEVEL]) > 0))
                and (texts[(TXT_RAID_TEXT + 18)]))
            ){
                if (text_dir == "right"){
                    text = (
                        (((((((((("50/" + guild_data[GUILD_RAID_LEVEL]) + " :")
                        + texts[(TXT_RAID_TEXT + 18)]) + "  ")
                        + str(((gilden_ehre)==1) ? 0 : gilden_ehre)) + " :")
                        + texts[TXT_HALL_LIST_COLUMN_5]) + "  ")
                        + str(gilden_rang)) + " :")
                        + texts[TXT_HALL_LIST_COLUMN_1]
                    );
                } else {
                    text = (
                        ((((((((((texts[TXT_HALL_LIST_COLUMN_1] + ": ")
                        + str(gilden_rang)) + "  ")
                        + texts[TXT_HALL_LIST_COLUMN_5])
                        + ": ") + str(((gilden_ehre)==1) ? 0 : gilden_ehre))
                        + "  ") + texts[(TXT_RAID_TEXT + 18)]) + ": ")
                        + guild_data[GUILD_RAID_LEVEL]) + "/50"
                    );
                };
            } else {
                if (text_dir == "right"){
                    text = (
                        (((((str(((gilden_ehre)==1) ? 0 : gilden_ehre) + " :")
                        + texts[TXT_HALL_LIST_COLUMN_5]) + "     ")
                        + str(gilden_rang)) + " :")
                        + texts[TXT_HALL_LIST_COLUMN_1]
                    );
                } else {
                    text = (
                        (((((texts[TXT_HALL_LIST_COLUMN_1] + ": ")
                        + str(gilden_rang)) + "     ")
                        + texts[TXT_HALL_LIST_COLUMN_5]) + ": ")
                        + str(((gilden_ehre)==1) ? 0 : gilden_ehre)
                    );
                };
            };
        };
        if (text_dir == "right"){
            actor[GILDE_RANG].x = (1175 - actor[LBL_GILDE_RANG].text_width);
        };
        if (guild_descr.find("http://") != -1){
            guildForumLink = guild_descr[guild_descr.find("http://"):]
            guildForumLink = guildForumLink.split(
                ")").join(" ").split(
                "#").join(" ").split(
                chr(13)).join(" ").split(
                chr(10)).join(" ").split(" ")[0];
            add(GILDE_LINK);
            if (guildForumLink[guildForumLink.length: 1] == "."){
                guildForumLink = guildForumLink[0: (guildForumLink.length - 1)]
            };
            enable_popup(GILDE_LINK, guildForumLink);
        } else {
            if (guild_descr.find("www.") != -1){
                guildForumLink = (
                    "http://" + guild_descr[guild_descr.find("www."):]
                )
                guildForumLink = guildForumLink.split(
                    ")").join(" ").split("#").join(
                    " ").split(chr(13)).join(" ").split(
                    chr(10)).join(" ").split(" ")[0];
                add(GILDE_LINK);
                if (guildForumLink[guildForumLink.length: 1] == "."){
                    guildForumLink = guildForumLink[
                        0: (guildForumLink.length - 1)
                    ]
                };
                enable_popup(GILDE_LINK, guildForumLink);
            };
        };
        _local3 = actor[INP_GILDE_TEXT];
        with (_local3) {
            getChildAt(0).text = (
                (guild_descr)=="")
                    ? (((myRank == 1))
                        ? texts[TXT_ENTERGUILDDESC]
                        : texts[TXT_GUILDNOTEXT])
                    : resolve_breaks(guild_descr);
            getChildAt(0).type = (
                ((((myRank == 1)) and (is_mine)))
                    ? TextFieldType.INPUT
                    : TextFieldType.DYNAMIC
            );
            mouse_enabled = True;
            add_event_listener(FocusEvent.FOCUS_IN, EnterGuildDesc);
            add_event_listener(FocusEvent.FOCUS_OUT, LeaveGuildDesc);
            if (text_dir == "right"){
                getChildAt(0).wordWrap = False;
            };
        };
        add(GILDE_RAID_GRAY);
        add(GILDE_ATTACK_GRAY);
        add(GILDE_DEFEND_GRAY);
        if (
            (((guild_data[5] >= 20))
            and ((guild_data[0] == savegame[SG_GUILD_INDEX])))
        ){
            if (myRank <= 2){
                if (guild_data[4] == 0){
                    add(GILDE_KATAPULT);
                } else {
                    if (guild_data[4] == 1){
                        add((GILDE_KATAPULT + 1));
                    } else {
                        if (guild_data[4] == 2){
                            add((GILDE_KATAPULT + 2));
                        } else {
                            if (guild_data[4] == 3){
                                add((GILDE_KATAPULT_OK + 2));
                            };
                        };
                    };
                };
            } else {
                if (guild_data[4] == 0){
                    add(GILDE_KATAPULT_GRAY);
                } else {
                    if (guild_data[4] == 1){
                        add(GILDE_KATAPULT_OK);
                    } else {
                        if (guild_data[4] == 2){
                            add((GILDE_KATAPULT_OK + 1));
                        } else {
                            if (guild_data[4] == 3){
                                add((GILDE_KATAPULT_OK + 2));
                            };
                        };
                    };
                };
            };
            i = 0;
            while (i < 3) {
                enable_popup(
                    (GILDE_KATAPULT + i),
                    POPUP_BEGIN_LINE,
                    texts[TXT_CATAPULT],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_CATAPULT + 1)].split(
                        "%1").join("3").split("#").join(chr(13)),
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_CATAPULT + 2)],
                    200,
                    texts[(TXT_CATAPULT + 3)].split(
                        "%1").join(str(guild_data[4])).split(
                        "%2").join("3"),
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_CATAPULT + 4)],
                    200,
                    texts[(TXT_CATAPULT + 5)].split("%1").join("5"),
                    actor[IF_PILZE],
                    POPUP_END_LINE
                );
                i = (i + 1);
            };
            enable_popup(
                GILDE_KATAPULT_GRAY,
                POPUP_BEGIN_LINE,
                texts[TXT_CATAPULT],
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                texts[(TXT_CATAPULT + 1)].split(
                    "%1").join("3").split("#").join(chr(13)),
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                texts[(TXT_CATAPULT + 2)],
                200,
                texts[(TXT_CATAPULT + 3)].split(
                    "%1").join(str(guild_data[4])).split("%2").join("3"),
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                texts[(TXT_CATAPULT + 6)],
                POPUP_END_LINE
            );
            i = 0;
            while (i < 2) {
                enable_popup(
                    (GILDE_KATAPULT_OK + i),
                    POPUP_BEGIN_LINE,
                    texts[TXT_CATAPULT],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_CATAPULT + 1)].split(
                        "%1").join("3").split("#").join(chr(13)),
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_CATAPULT + 2)],
                    200,
                    texts[(TXT_CATAPULT + 3)].split(
                        "%1").join(str(guild_data[4])).split("%2").join("3"),
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_CATAPULT + 6)],
                    POPUP_END_LINE
                );
                i = (i + 1);
            };
            enable_popup(
                (GILDE_KATAPULT_OK + 2),
                POPUP_BEGIN_LINE,
                texts[TXT_CATAPULT],
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                texts[(TXT_CATAPULT + 1)].split(
                    "%1").join("3").split("#").join(chr(13)),
                POPUP_END_LINE,
                POPUP_BEGIN_LINE,
                texts[(TXT_CATAPULT + 2)],
                200,
                texts[(TXT_CATAPULT + 3)].split(
                    "%1").join(str(guild_data[4])).split("%2").join("3"),
                POPUP_END_LINE
            );
        };
        raidCost = GildeBuildingGold[(int(guild_data[GUILD_RAID_LEVEL]) + 51)];
        if (int(guild_data[GUILD_RAID_LEVEL]) == 0){
            raidCost = (raidCost * 0.2);
        };
        if (int(guild_data[GUILD_RAID_LEVEL]) == 1){
            raidCost = (raidCost * 0.4);
        };
        if (int(guild_data[GUILD_RAID_LEVEL]) == 2){
            raidCost = (raidCost * 0.6);
        };
        if (int(guild_data[GUILD_RAID_LEVEL]) == 3){
            raidCost = (raidCost * 0.8);
        };
        raidCost = Number(int((raidCost / 100)));
        lastRaidCost = raidCost;
        if (texts[TXT_RAID_TEXT]){
            if (guild_data[GUILD_RAID_LEVEL] >= 50){
                enable_popup(GILDE_RAID_GRAY, texts[(TXT_RAID_TEXT + 17)]);
            } else {
                enable_popup(
                    GILDE_RAID_GRAY,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_RAID_TEXT + 4)],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_RAID_TEXT + 15)],
                    (POPUP_TAB + POPUP_TAB_ADD),
                    texts[TXT_DUNGEON_NAMES
                            + int(guild_data[GUILD_RAID_LEVEL])],
                    "(" + str((int(guild_data[
                        GUILD_RAID_LEVEL]) + 1)) + "/50)",
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_RAID_TEXT + 16)],
                    (POPUP_TAB + POPUP_TAB_ADD),
                    str(raidCost),
                    actor[IF_GOLD],
                    POPUP_END_LINE
                );
            };
        };
        enable_popup(GILDE_ATTACK_GRAY, texts[(TXT_GUILD_BATTLE_POPUP + 7)]);
        enable_popup(GILDE_DEFEND_GRAY, texts[(TXT_GUILD_BATTLE_POPUP + 6)]);
        actor[LBL_GILDE_ATTACK].text = "";
        actor[LBL_GILDE_DEFENCE].text = "";
        last_guild_data = guild_data;
        isRaid = !((guild_data[GUILD_IS_RAID] == 0));
        send_action(
            ACT_REQUEST_GUILD_NAMES,
            guild_data[GUILD_ATTACK_TARGET],
            guild_data[GUILD_DEFENCE_TARGET],
            ((is_mine) ? 0 : 1)
        );
        if (guild_data[0] == savegame[SG_GUILD_INDEX]){
            my_own_rank = myRank;
            my_own_attack_target = int(guild_data[GUILD_ATTACK_TARGET]);
            my_own_guild_money = int(guild_data[1]);
            if (
                (int(savegame[SG_SERVER_TIME])
                - int(savegame[SG_GUILD_JOIN_DATE])) > ((60 * 60) * 24)
            ){
                if ((((myRank == 1)) or ((myRank == 2)))){
                    if (int(guild_data[GUILD_ATTACK_TARGET]) == 0){
                        add(GILDE_ATTACK);
                        enable_popup(
                            GILDE_ATTACK,
                            texts[(TXT_GUILD_BATTLE_POPUP + 0)]
                        );
                        if (guild_data[GUILD_RAID_LEVEL] >= 50){
                            if (texts[TXT_RAID_TEXT]){
                                enable_popup(
                                    GILDE_RAID_GRAY,
                                    texts[(TXT_RAID_TEXT + 17)]
                                );
                            };
                        } else {
                            add(GILDE_RAID);
                            if (texts[TXT_RAID_TEXT]){
                                enable_popup(
                                    GILDE_RAID,
                                    POPUP_BEGIN_LINE,
                                    texts[(TXT_RAID_TEXT + 0)],
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[(TXT_RAID_TEXT + 15)],
                                    (POPUP_TAB + POPUP_TAB_ADD),
                                    texts[(TXT_DUNGEON_NAMES
                                        + int(guild_data[GUILD_RAID_LEVEL]))],
                                    ("(" + str(int(guild_data[
                                        GUILD_RAID_LEVEL])
                                        + 1)) + "/50)",
                                    POPUP_END_LINE,
                                    POPUP_BEGIN_LINE,
                                    texts[(TXT_RAID_TEXT + 16)],
                                    (POPUP_TAB + POPUP_TAB_ADD),
                                    str(raidCost),
                                    actor[IF_GOLD],
                                    POPUP_END_LINE
                                );
                            };
                        };
                    } else {
                        if (int(guild_data[GUILD_ATTACK_TARGET]) < 0){
                            enable_popup(
                                GILDE_ATTACK_GRAY,
                                texts[(TXT_GUILD_BATTLE_POPUP + 5)].split(
                                    "%1").join(time_str(
                                        last_guild_data[GUILD_ATTACK_TIME])));
                            if (texts[TXT_RAID_TEXT]){
                                enable_popup(
                                    GILDE_RAID_GRAY,
                                    texts[(TXT_RAID_TEXT + 3)].split(
                                        "%1").join(time_str(
                                        last_guild_data[GUILD_ATTACK_TIME]))
                                    );
                            };
                        } else {
                            if ((myAttackStatus & 1)){
                                if (isRaid){
                                    add(GILDE_RAID_OK);
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID_OK,
                                            texts[(TXT_RAID_TEXT + 2)]
                                        );
                                    };
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_ATTACK_GRAY,
                                            texts[(TXT_RAID_TEXT + 10)]
                                        );
                                    };
                                } else {
                                    add(GILDE_ATTACK_OK);
                                    enable_popup(
                                        GILDE_ATTACK_OK,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 3)]
                                    );
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID_GRAY,
                                            texts[(TXT_RAID_TEXT + 11)]
                                        );
                                    };
                                };
                            } else {
                                if (isRaid){
                                    add(GILDE_RAID);
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID,
                                            texts[(TXT_RAID_TEXT + 1)]
                                        );
                                    };
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_ATTACK_GRAY,
                                            texts[(TXT_RAID_TEXT + 10)]
                                        );
                                    };
                                } else {
                                    add(GILDE_ATTACK);
                                    enable_popup(
                                        GILDE_ATTACK,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 1)]
                                    );
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID_GRAY,
                                            texts[(TXT_RAID_TEXT + 11)]
                                        );

                } else {
                    if (int(guild_data[GUILD_ATTACK_TARGET]) == 0){
                    } else {
                        if (int(guild_data[GUILD_ATTACK_TARGET]) < 0){
                            enable_popup(
                                GILDE_ATTACK_GRAY,
                                texts[(TXT_GUILD_BATTLE_POPUP + 5)].split(
                                    "%1").join(time_str(last_guild_data[
                                        GUILD_ATTACK_TIME])));
                            if (texts[TXT_RAID_TEXT]){
                                enable_popup(
                                    GILDE_RAID_GRAY,
                                    texts[(TXT_RAID_TEXT + 3)].split(
                                        "%1").join(time_str(last_guild_data[
                                            GUILD_ATTACK_TIME]))
                                    );
                            };
                        } else {
                            if (isRaid){
                                if (int(savegame[SG_GUILD_FIGHT_STATUS]) & 1):
                                    add(GILDE_RAID_OK);
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID_OK,
                                            texts[(TXT_RAID_TEXT + 2)]
                                        );
                                    };
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_ATTACK_GRAY,
                                            texts[(TXT_RAID_TEXT + 10)]
                                        );
                                    };
                                } else {
                                    add(GILDE_RAID);
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID,
                                            texts[(TXT_RAID_TEXT + 1)]
                                        );
                                    };
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_ATTACK_GRAY,
                                            texts[(TXT_RAID_TEXT + 10)]
                                        );
                                    };
                                };
                            } else {
                                if (int(savegame[SG_GUILD_FIGHT_STATUS]) & 1):
                                    add(GILDE_ATTACK_OK);
                                    enable_popup(
                                        GILDE_ATTACK_OK,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 3)]
                                    );
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID_GRAY,
                                            texts[(TXT_RAID_TEXT + 11)]
                                        );
                                    };
                                } else {
                                    add(GILDE_ATTACK);
                                    enable_popup(
                                        GILDE_ATTACK,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 1)]
                                    );
                                    if (texts[TXT_RAID_TEXT]){
                                        enable_popup(
                                            GILDE_RAID_GRAY,
                                            texts[(TXT_RAID_TEXT + 11)]
                                        );

                if (int(guild_data[GUILD_DEFENCE_TARGET]) <= 0){
                    enable_popup(
                        GILDE_DEFEND_GRAY,
                        texts[(TXT_GUILD_BATTLE_POPUP + 6)]
                    );
                } else {
                    if ((int(savegame[SG_GUILD_FIGHT_STATUS]) & 2)){
                        add(GILDE_DEFEND_OK);
                        enable_popup(
                            GILDE_DEFEND_OK,
                            texts[(TXT_GUILD_BATTLE_POPUP + 4)]
                        );
                    } else {
                        add(GILDE_DEFEND);
                        enable_popup(
                            GILDE_DEFEND,
                            texts[(TXT_GUILD_BATTLE_POPUP + 2)]
                        );
                    };
                };
            } else {
                enable_popup(
                    GILDE_RAID_GRAY,
                    texts[TXT_GUILD_JOINED_TOO_RECENTLY].split(
                        "%1").join(time_str((Number(
                            savegame[SG_GUILD_JOIN_DATE]) + ((60 * 60) * 24)),
                            True))
                    );
                enable_popup(
                    GILDE_ATTACK_GRAY,
                    texts[TXT_GUILD_JOINED_TOO_RECENTLY].split(
                        "%1").join(time_str((Number(
                            savegame[SG_GUILD_JOIN_DATE]) + ((60 * 60) * 24)),
                            True))
                    );
                enable_popup(
                    GILDE_DEFEND_GRAY,
                    texts[TXT_GUILD_JOINED_TOO_RECENTLY].split(
                        "%1").join(time_str((Number(
                            savegame[SG_GUILD_JOIN_DATE]) + ((60 * 60) * 24)),
                        True))
                    );
            };
        } else {
            remove(GILDE_RAID);
            remove(GILDE_RAID_GRAY);
            remove(GILDE_RAID_OK);
            if (
                (int(savegame[SG_SERVER_TIME])
                 - int(savegame[SG_GUILD_JOIN_DATE])) > ((60 * 60) * 24)
            ){
                if (my_own_rank == -1){
                    remove(GILDE_ATTACK_GRAY);
                    remove(GILDE_DEFEND_GRAY);
                } else {
                    if ((((my_own_rank == 1)) or ((my_own_rank == 2)))){
                        if (int(guild_data[GUILD_DEFENCE_TARGET]) == 0){
                            if (my_own_attack_target == 0){
                                if (my_own_guild_money >= attack_cost){
                                    add(GILDE_ATTACK);
                                    enable_popup(
                                        GILDE_ATTACK,
                                        POPUP_BEGIN_LINE,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 8)],
                                        POPUP_END_LINE,
                                        POPUP_BEGIN_LINE,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 17)],
                                        str(int((attack_cost / 100))),
                                        actor[IF_GOLD],
                                        POPUP_END_LINE
                                    );
                                } else {
                                    enable_popup(
                                        GILDE_ATTACK_GRAY,
                                        POPUP_BEGIN_LINE,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 18)],
                                        POPUP_END_LINE,
                                        POPUP_BEGIN_LINE,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 17)],
                                        str(int((attack_cost / 100))),
                                        actor[IF_GOLD],
                                        POPUP_END_LINE
                                    );
                                };
                            } else {
                                if (my_own_attack_target < 0){
                                    enable_popup(
                                        GILDE_ATTACK_GRAY,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 11)]
                                    );
                                } else {
                                    enable_popup(
                                        GILDE_ATTACK_GRAY,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 16)]
                                    );
                                };
                            };
                        } else {
                            if (
                                int(guild_data[GUILD_DEFENCE_TARGET]) == int(
                                    savegame[SG_GUILD_INDEX])
                                ){
                                add(GILDE_ATTACK_OK);
                                enable_popup(
                                    GILDE_ATTACK_OK,
                                    texts[(TXT_GUILD_BATTLE_POPUP + 12)]
                                );
                            } else {
                                if (int(guild_data[GUILD_DEFENCE_TARGET]) < 0){
                                    enable_popup(
                                        GILDE_ATTACK_GRAY,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 11)]
                                    );
                                } else {
                                    enable_popup(
                                        GILDE_ATTACK_GRAY,
                                        texts[(TXT_GUILD_BATTLE_POPUP + 13)]
                                    );
                                };
                            };
                        };
                    } else {
                        if (
                            int(guild_data[GUILD_DEFENCE_TARGET]) == int(
                                savegame[SG_GUILD_INDEX])
                            ){
                            add(GILDE_ATTACK_OK);
                            enable_popup(
                                GILDE_ATTACK_OK,
                                texts[(TXT_GUILD_BATTLE_POPUP + 12)]
                            );
                        } else {
                            enable_popup(
                                GILDE_ATTACK_GRAY,
                                texts[(TXT_GUILD_BATTLE_POPUP + 14)]
                            );
                        };
                        if (
                            int(guild_data[GUILD_ATTACK_TARGET]) == int(
                               savegame[SG_GUILD_INDEX])
                            ){
                            if ((int(savegame[SG_GUILD_FIGHT_STATUS]) & 2)){
                                add(GILDE_DEFEND_OK);
                                enable_popup(
                                    GILDE_DEFEND_OK,
                                    texts[(TXT_GUILD_BATTLE_POPUP + 4)]
                                );
                            } else {
                                add(GILDE_DEFEND);
                                enable_popup(
                                    GILDE_DEFEND,
                                    texts[(TXT_GUILD_BATTLE_POPUP + 9)]
                                );
                            };
                        } else {
                            enable_popup(
                                GILDE_DEFEND_GRAY,
                                texts[(TXT_GUILD_BATTLE_POPUP + 15)]
                            );
                        };
                    };
                };
            } else {
                if (my_own_rank == -1){
                    remove(GILDE_ATTACK_GRAY);
                    remove(GILDE_DEFEND_GRAY);
                } else {
                    enable_popup(
                        GILDE_ATTACK_GRAY,
                        texts[TXT_GUILD_JOINED_TOO_RECENTLY].split(
                           "%1").join(time_str((Number(
                            savegame[SG_GUILD_JOIN_DATE]) + ((60 * 60) * 24)),
                        True))
                    );
                    enable_popup(
                        GILDE_DEFEND_GRAY,
                        texts[TXT_GUILD_JOINED_TOO_RECENTLY].split(
                            "%1").join(time_str((Number(
                                savegame[SG_GUILD_JOIN_DATE])
                                + ((60 * 60) * 24)),
                        True))
                    );
                };
            };
        };
        if (
            ((((int(guild_data[GUILD_MEMBERLEVEL]) % 1000) < 50))
            or (!(texts[TXT_RAID_TEXT])))
        ){
            remove(GILDE_RAID);
            remove(GILDE_RAID_GRAY);
            remove(GILDE_RAID_OK);
        };
        if (countCompleted >= 3){
        };
        if (guild_data[0] != savegame[SG_GUILD_INDEX]){
            remove(GILDE_GEBAEUDE);
            remove(GILDE_CHAT);
            remove(
                GILDE_GEBAEUDE_IMPROVE_GRAY,
                (GILDE_GEBAEUDE_IMPROVE_GRAY + 1),
                (GILDE_GEBAEUDE_IMPROVE_GRAY + 2)
            );
            remove(GILDE_SCHATZ);
        };
    };
    arrow_hall_mode = False;
    if (is_mine){
        if (int(guild_data[0]) != gilden_id){
            gilden_id = int(guild_data[0]);
            send_action(ACT_REQUEST_GUILD, guild_data[0]);
        };
    };
    last_guild_shown = this_gilde;
    lastguild_members = guild_members.join("#").split("#");
    add_suggest_names(lastguild_members);
    load(SCREEN_GILDEN);
    load(GILDE_SET_MEMBER);
    load(GILDE_SET_MASTER);
    load(GILDE_RANK, (GILDE_RANK + 1), (GILDE_RANK + 2));
    load(GILDE_DIALOG_INVITE, GILDE_DIALOG_KICK, GILDE_DIALOG_MASTER);
    when_loaded(DoShowScreenGilden);
    '''
    print guild_data, guild_descr, guild_members, this_gilde, is_mine,
    print gilden_rang, gilden_ehre, attack_cost


def show_work_success_screen():
    '''
    show_city_screen();
    add(SCREEN_ARBEITEN_SUCCESS);
    actor[LBL_WINDOW_TITLE].text = texts[TXT_TITLE_WORK];
    actor[LBL_WINDOW_TITLE].x = (
        (IF_WIN_X + IF_WIN_WELCOME_X)
        - int((actor[LBL_WINDOW_TITLE].text_width / 2))
    );
    actor[LBL_SCR_ARBEITEN_TEXT].text = texts[TXT_ARBEIT_TEXT5];
    actor[LBL_SCR_ARBEITEN_TEXT2].text = (
        (((texts[TXT_ARBEIT_TEXT6] + " ")
        + geld(verdientes_geld)) + " ")
        + texts[TXT_ARBEIT_TEXT7]
    );
    play(SND_JINGLE);
    check_wrong_page(ACT_SCREEN_ARBEITEN);
    '''
    pass


def show_work_screen(evt=None):
    '''
    var ArbeitCountdown:* = None;
    var DoShowWorking:* = None;
    var evt:* = evt;
    ArbeitCountdown = new Timer(100);
    show_city_screen();
    if (savegame[SG_ACTION_STATUS] == 1){
        DoShowWorking = function (){
            var ArbeitCountdownEvent:* = None;
            ArbeitCountdownEvent = function (evt:Event):
                var evt:* = evt;
                var _local3 = actor[LBL_SCR_ARBEITEN_TIME];
                with (_local3) {
                    if (waiting_for(savegame[SG_ACTION_ENDTIME])){
                        if (texts[TXT_WORK_FINISH]){
                            text = texts[TXT_WORK_FINISH].split(
                                "%1").join(waiting_time(
                                   savegame[SG_ACTION_ENDTIME])).split(
                                "%2").join(time_str(
                                    savegame[SG_ACTION_ENDTIME],
                            True));
                        } else {
                            text = waiting_time(savegame[SG_ACTION_ENDTIME]);
                        };
                        if (on_stage(LBL_SCR_ARBEITEN_TIME)){
                            set_title_bar(text);
                        };
                        actor[SCR_ARBEITEN_FILL].width = (
                            waiting_progress((savegame[SG_ACTION_ENDTIME]
                            - ((savegame[SG_ACTION_INDEX] * 60) * 60)),
                            savegame[SG_ACTION_ENDTIME]) * 278
                        );
                    } else {
                        ArbeitCountdown.stop();
                        ArbeitCountdown.remove_event_listener(
                            TimerEvent.TIMER, ArbeitCountdownEvent
                        );
                        if (on_stage(LBL_SCR_ARBEITEN_TIME)){
                            send_action(ACT_SCREEN_ARBEITEN);
                        };
                    };
                    x = (
                         (IF_WIN_X + IF_WIN_WELCOME_X)
                         - int((actor[LBL_SCR_ARBEITEN_TIME].text_width / 2))
                    );
                };
            };
            var _local2 = actor[SCR_ARBEITEN_BAR];
            with (_local2) {
                scaleX = 0.5;
                scaleY = 0.5;
            };
            _local2 = actor[SCR_ARBEITEN_FILL];
            with (_local2) {
                width = 0;
                scaleY = 0.5;
            };
            actor[LBL_WINDOW_TITLE].text = texts[TXT_TITLE_WORK];
            actor[LBL_WINDOW_TITLE].x = (
                (IF_WIN_X + IF_WIN_WELCOME_X)
                - int((actor[LBL_WINDOW_TITLE].text_width / 2))
            );
            actor[LBL_SCR_ARBEITEN_TEXT].text = texts[TXT_ARBEIT_TEXT4];
            ArbeitCountdown.add_event_listener(
                TimerEvent.TIMER, ArbeitCountdownEvent
            );
            ArbeitCountdown.start();
            check_wrong_page(ACT_SCREEN_ARBEITEN);
        };
        add(SCREEN_ARBEITEN_WAIT);
        set_cnt(SCR_ARBEITEN_BAR, QUESTBAR_BG);
        set_cnt(SCR_ARBEITEN_FILL, QUESTBAR_FILL);
        when_loaded(DoShowWorking);
    } else {
        if (savegame[SG_ACTION_STATUS] == 0){
            add(SCREEN_ARBEITEN);
            actor[LBL_WINDOW_TITLE].text = texts[TXT_TITLE_WORK];
            actor[LBL_WINDOW_TITLE].x = (
                (IF_WIN_X + IF_WIN_WELCOME_X)
                - int((actor[LBL_WINDOW_TITLE].text_width / 2))
            );
            actor[LBL_SCR_ARBEITEN_TEXT].text = texts[TXT_ARBEIT_TEXT];
            set_slider_value(SLDR['ARBEITEN'], 1);
            arbeiten_slider_change(1);
        };
    };
    '''
    print evt


def show_main_quests_screen(next_enemies):
    '''
    var i:* = 0;
    var countDone:* = 0;
    var Background:* = 0;
    var DoShowMainQuestsScreen:* = None;
    var next_enemies:* = next_enemies;
    var doShowCongrats:* = function (){
        remove_all();
        add(DUNGEON_CONGRATS);
    };
    DoShowMainQuestsScreen = function (){
        var this_mqSInstance:* = 0;
        var DungeonLevel:* = None;
        var Nextenemy:* = None;
        var PlayUnlockSound:* = False;
        var i:* = None;
        var MainQuestsClick:* = function (evt:MouseEvent){
            var evt:* = evt;
            if (this_mqSInstance != MQSInstance){
                i = 0;
                while (i < 9) {
                    var _local3 = actor[(MQS_BUTTON + i)].content;
                    with (_local3) {
                        remove_event_listener(
                                MouseEvent.CLICK, MainQuestsClick)
                    };
                    i++;
                };
                return;
            };
            if (get_actor_id(evt.target) == (HLMQS_BUTTON + 4)){
                send_action(ACT_SCREEN_TOWER);
            } else {
                if (countDone == 9){
                    show_main_quest_screen(9, (int(next_enemies[9]) - 1));
                } else {
                    if (countDone == 10){
                        show_main_quest_screen(10,
                            (int(next_enemies[10]) - 1));
                    } else {
                        if (countDone == 11){
                            show_main_quest_screen(11,
                                int(next_enemies[11] - 1))
                        } else {
                            if (countDone == 12){
                                show_main_quest_screen(
                                    12, (int(next_enemies[12]) - 1)
                                );
                            } else {
                                show_main_quest_screen(
                                    (get_actor_id(evt.target) - MQS_BUTTON),
                                    (int(next_enemies[(get_actor_id(evt.target)
                                        - MQS_BUTTON)]) - 1)
                                );

        MQSInstance++;
        if (MQSInstance > 1000){
            MQSInstance = 0;
        };
        this_mqSInstance = MQSInstance;
        DungeonLevel = "";
        Nextenemy = "";
        PlayUnlockSound = False;
        remove_all();
        add(Background);
        add((((countDone >= 9)) ? SCREEN_HLMAINQUESTS : SCREEN_MAINQUESTS));
        var _local2 = actor[LBL_MAINQUESTS_TITLE];
        with (_local2) {
            x = (SCREEN_TITLE_X - int((text_width / 2)));
        };
        _local2 = actor[LBL_HLMAINQUESTS_TITLE];
        with (_local2) {
            x = (SCREEN_TITLE_X - int((text_width / 2)));
        };
        if (countDone < 9){
            i = 0;
            while (i < 9) {
                if (int(next_enemies[i]) >= 500){
                    Nextenemy = texts[
                        ((TXT_COPYCAT_NAME + int(next_enemies[i])) - 500)
                    ];
                } else {
                    if (int(next_enemies[i]) > 220){
                        Nextenemy = texts[
                            TXT_NEW_MONSTER_NAMES + int(next_enemies[i]) - 221
                        ];
                    } else {
                        Nextenemy = texts[
                            ((int(next_enemies[i]))==-1)
                                ? TXT_enemy_SELF
                                : (TXT_MONSTER_NAME + int(next_enemies[i]) - 1)
                            ];
                    };
                };
                set_cnt((MQS_DISABLED + i), MQS_DISABLED);
                set_cnt((MQS_COMPLETED + i), MQS_COMPLETED);
                _local2 = actor[(MQS_DISABLED + i)];
                with (_local2) {
                    visible = (int(savegame[(SG_DUNGEON_LEVEL + i)]) <= 1);
                    alpha = 1;
                };
                actor[(MQS_COMPLETED + i)].visible = (
                    int(savegame[(SG_DUNGEON_LEVEL + i)]) >= 12
                );
                set_cnt((MQS_BUTTON + i), (MQS_BUTTON + i));
                DungeonLevel = str((int(savegame[(SG_DUNGEON_LEVEL + i)]) - 1))
                if (DungeonLevel == "0"){
                    PlayUnlockSound = True;
                    fade_out((MQS_DISABLED + i), 20, 0.05, 0, True);
                    DungeonLevel = "1";
                };
                enable_popup(
                    (MQS_BUTTON + i),
                    POPUP_BEGIN_LINE,
                    texts[(TXT_DUNGEON_NAME + i)].split("|")[0],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    FontFormatEpicItemQuote,
                    texts[(TXT_DUNGEON_NAME + i)].split("|")[1],
                    FontFormatPopup,
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[TXT_DUNGEON_INFO].split(
                        "%1").join(DungeonLevel).split(
                        "%2").join(Nextenemy),
                    POPUP_END_LINE
                );
                _local2 = actor[(MQS_BUTTON + i)];
                with (_local2) {
                    add_event_listener(MouseEvent.CLICK, MainQuestsClick);
                    buttonMode = True;
                    useHandCursor = True;
                    mouseChildren = False;
                };
                i = (i + 1);
            };
        } else {
            i = 0;
            while (i < 5) {
                if (i < 4){
                    set_cnt((HLMQS_DISABLED + i), MQS_DISABLED);
                    set_cnt((HLMQS_COMPLETED + i), MQS_COMPLETED);
                    if (i == 0){
                        DungeonLevel = savegame[(SG_DUNGEON_LEVEL + 9)];
                        if (countDone > 9){
                            actor[(HLMQS_DISABLED + i)].visible = False;
                            actor[(HLMQS_COMPLETED + i)].visible = True;
                        } else {
                            actor[(HLMQS_COMPLETED + i)].visible = False;
                            actor[(HLMQS_DISABLED + i)].alpha = 1;
                            if (DungeonLevel == "0"){
                                actor[(HLMQS_DISABLED + i)].visible = True;
                                PlayUnlockSound = True;
                                fade_out(
                                    (HLMQS_DISABLED + i), 20, 0.05, 0, True
                                );
                                DungeonLevel = "1";
                            } else {
                                DungeonLevel = str((int(DungeonLevel) - 1));
                                actor[(HLMQS_DISABLED + i)].visible = False;
                            };
                        };
                        Switch (DungeonLevel){
                            if case("1":
                                Nextenemy = texts[2300];
                                break;
                            if case("2":
                                Nextenemy = texts[2314];
                                break;
                            if case("3":
                                Nextenemy = texts[2358];
                                break;
                            if case("4":
                                Nextenemy = texts[2220];
                                break;
                            if case("5":
                                Nextenemy = texts[2260];
                                break;
                            if case("6":
                                Nextenemy = texts[2362];
                                break;
                            if case("7":
                                Nextenemy = texts[2360];
                                break;
                            if case("8":
                                Nextenemy = texts[2358];
                                break;
                            if case("9":
                                Nextenemy = texts[2357];
                                break;
                            if case("10":
                                Nextenemy = texts[2364];
                                break;
                        };
                    } else {
                        if (i == 1){
                            if (countDone > 10){
                                actor[(HLMQS_DISABLED + i)].visible = False;
                                actor[(HLMQS_COMPLETED + i)].visible = True;
                            } else {
                                if (countDone == 10){
                                    actor[HLMQS_COMPLETED + i].visible = False
                                    actor[(HLMQS_DISABLED + i)].alpha = 1;
                                    DungeonLevel = savegame[
                                            SG_NEW_DUNGEONS + 0]
                                    if (DungeonLevel == "0"){
                                        actor[
                                            HLMQS_DISABLED + i].visible = True
                                        PlayUnlockSound = True;
                                        fade_out(
                                            (HLMQS_DISABLED + i),
                                            20, 0.05, 0, True
                                        );
                                        DungeonLevel = "1";
                                    } else {
                                        DungeonLevel = str(
                                            (int(DungeonLevel) - 1)
                                        );
                                        actor[
                                            HLMQS_DISABLED + i
                                        ].visible = False
                                    };
                                } else {
                                    actor[HLMQS_COMPLETED + i].visible = False
                                    actor[(HLMQS_DISABLED + i)].alpha = 1;
                                    actor[(HLMQS_DISABLED + i)].visible = True;
                                };
                            };
                            Nextenemy = texts[(2372 + int(DungeonLevel)) - 1]
                        } else {
                            if (i == 2){
                                if (countDone > 11){
                                    actor[(HLMQS_DISABLED + i)].visible = False
                                    actor[(HLMQS_COMPLETED + i)].visible = True
                                } else {
                                    if (countDone == 11){
                                        actor[
                                            HLMQS_COMPLETED + i
                                        ].visible = False
                                        actor[(HLMQS_DISABLED + i)].alpha = 1;
                                        DungeonLevel = savegame[
                                            SG_NEW_DUNGEONS + 1
                                        ]
                                        if (DungeonLevel == "0"){
                                            actor[
                                                HLMQS_DISABLED + i
                                            ].visible = True;
                                            PlayUnlockSound = True;
                                            fade_out(
                                                (HLMQS_DISABLED + i),
                                                20, 0.05, 0, True
                                            );
                                            DungeonLevel = "1";
                                        } else {
                                            DungeonLevel = str(
                                                (int(DungeonLevel) - 1)
                                            );
                                            actor[
                                                (HLMQS_DISABLED + i)
                                            ].visible = False;
                                        };
                                    } else {
                                        actor[
                                            (HLMQS_COMPLETED + i)
                                        ].visible = False;
                                        actor[(HLMQS_DISABLED + i)].alpha = 1;
                                        actor[
                                            (HLMQS_DISABLED + i)
                                        ].visible = True;
                                    };
                                };
                                Nextenemy = texts[2382 + int(DungeonLevel) - 1]
                            } else {
                                if (i == 3){
                                    if (countDone > 12){
                                        actor[
                                            HLMQS_DISABLED + i
                                        ].visible = False
                                        actor[
                                            (HLMQS_COMPLETED + i)
                                        ].visible = True;
                                    } else {
                                        if (countDone == 12){
                                            actor[
                                                (HLMQS_COMPLETED + i)
                                            ].visible = False;
                                            actor[HLMQS_DISABLED + i].alpha = 1
                                            DungeonLevel = str((int(savegame[
                                                SG_DUNGEON_13]) - 120));
                                            if (DungeonLevel == "0"){
                                                actor[
                                                    HLMQS_DISABLED + i
                                                ].visible = True;
                                                PlayUnlockSound = True;
                                                fade_out(
                                                    (HLMQS_DISABLED + i),
                                                    20, 0.05, 0, True
                                                );
                                                DungeonLevel = "1";
                                            } else {
                                                DungeonLevel = str(
                                                    (int(DungeonLevel) - 1));
                                                actor[
                                                    (HLMQS_DISABLED + i)
                                                ].visible = False;
                                            };
                                        } else {
                                            actor[
                                                (HLMQS_COMPLETED + i)
                                            ].visible = False;
                                            actor[
                                                (HLMQS_DISABLED + i)
                                            ].alpha = 1;
                                            actor[
                                                (HLMQS_DISABLED + i)
                                            ].visible = True;
                                        };
                                    };
                                    Nextenemy = texts[
                                        ((9032 + int(DungeonLevel)) - 1)
                                    ];
                                };
                            };
                        };
                    };
                } else {
                    set_cnt((HLMQS_COMPLETED + i), HLMQS_TOWER_DISABLED);
                    Nextenemy = texts[
                        (TXT_TOWER_enemy_NAMES + tower_level)
                    ].split("|")[0];
                    DungeonLevel = str((tower_level + 1));
                    if (tower_level >= 100){
                        actor[(HLMQS_COMPLETED + i)].visible = True;
                    } else {
                        actor[(HLMQS_COMPLETED + i)].visible = False;
                    };
                };
                set_cnt((HLMQS_BUTTON + i), (HLMQS_BUTTON + i));
                enable_popup(
                    (HLMQS_BUTTON + i),
                    POPUP_BEGIN_LINE,
                    texts[(TXT_HL_MAINQUESTS_NAME + i)].split("|")[0],
                    POPUP_END_LINE, POPUP_BEGIN_LINE,
                    FontFormatEpicItemQuote,
                    texts[(TXT_HL_MAINQUESTS_NAME + i)].split("|")[1],
                    FontFormatPopup,
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(((i == 4))
                           ? TXT_TOWER_INFO
                           : TXT_DUNGEON_INFO)].split(
                        "%1").join(DungeonLevel).split(
                        "%2").join(Nextenemy).split(
                        "%3").join(str(tower_level)),
                    POPUP_END_LINE
                );
                _local2 = actor[(HLMQS_BUTTON + i)];
                with (_local2) {
                    add_event_listener(MouseEvent.CLICK, MainQuestsClick);
                    buttonMode = True;
                    useHandCursor = True;
                    mouseChildren = False;
                };
                i = (i + 1);
            };
        };
        if (PlayUnlockSound){
            play(SND_MAINQUESTS_UNLOCK);
        };
    };
    countDone = 0;
    i = 0;
    while (i < 10) {
        if (int(savegame[(SG_DUNGEON_LEVEL + i)]) >= 12){
            countDone = (countDone + 1);
        };
        i = (i + 1);
    };
    i = 0;
    while (i < 2) {
        if (int(savegame[(SG_NEW_DUNGEONS + i)]) >= 12){
            countDone = (countDone + 1);
        };
        i = (i + 1);
    };
    if (int(savegame[SG_DUNGEON_13]) >= (120 + 12)){
        countDone = (countDone + 1);
    };
    Background = (SCR_QUEST_BG_1 + 50);
    load(Background);
    load((((countDone >= 9)) ? SCREEN_HLMAINQUESTS : SCREEN_MAINQUESTS));
    load(MQS_DISABLED);
    load(MQS_COMPLETED);
    if (countDone >= 9){
        load(HLMQS_TOWER_DISABLED);
        load(HLMQS_TOWER_COMPLETED);
    };
    i = 0;
    while (i < 9) {
        load((MQS_BUTTON + i));
        i = (i + 1);
    };
    when_loaded(DoShowMainQuestsScreen);
    '''
    print next_enemies


def show_main_quest_screen(dungeon_nr=0, enemy=0):
    '''
    var Doshow_main_quest_screen:* = None;
    var MQDelayCheck:* = None;
    var dungeon_nr = dungeon_nr;
    var enemy = enemy;
    Doshow_main_quest_screen = function (){
        var DungeonLevel:* = None;
        var i:* = 0;
        DungeonLevel = "";
        if (dungeon_nr == 100){
            DungeonLevel = str((tower_level + 1));
        } else {
            if (dungeon_nr == 12){
                DungeonLevel = str((int(savegame[SG_DUNGEON_13]) - 121));
            } else {
                if (dungeon_nr >= 10){
                    DungeonLevel = str(
                       (int(savegame[(SG_NEW_DUNGEONS + dungeon_nr - 10)]) - 1)
                    );
                } else {
                    DungeonLevel = str(
                        (int(savegame[(SG_DUNGEON_LEVEL + dungeon_nr)]) - 1)
                    );
                };
            };
        };
        remove_all();
        if (dungeon_nr != 100){
            if (DungeonLevel == "0"){
                DungeonLevel = "1";
            };
            if (int(DungeonLevel) >= 120){
                DungeonLevel = "1";
            };
            var _local2 = actor[LBL_MAINQUEST_TITLE];
            with (_local2) {
                text = texts[(TXT_DUNGEON_INFO + 3)].split(
                    "%1").join(texts[(TXT_DUNGEON_NAME + dungeon_nr)].split(
                    "|")[0]).split(
                    "%2").join(DungeonLevel
                );
                x = (SCREEN_TITLE_X - (text_width / 2));
            };
        } else {
            _local2 = actor[LBL_MAINQUEST_TITLE];
            with (_local2) {
                text = (
                    (texts[TXT_TOWER_LEVEL].split(
                        "%1").join(DungeonLevel) + " - ")
                    + texts[((TXT_TOWER_enemy_NAMES + enemy) - 399)].split(
                        "|")[0]);
                x = (SCREEN_TITLE_X - (text_width / 2));
            };
        };
        _local2 = actor[LBL_MAINQUEST_TEXT];
        with (_local2) {
            text = questText.split("#").join(chr(13));
        };
        arabize(LBL_MAINQUEST_TEXT);
        if (text_dir == "right"){
            set_btn_text(
                MAINQUEST_START,
                (((waiting_for(savegame[SG_MQ_REROLL_TIME])) ? "(~P1) " : "")
                    + texts[TXT_OK]));
        } else {
            set_btn_text(
                MAINQUEST_START,
                (texts[TXT_OK] + ((waiting_for(savegame[SG_MQ_REROLL_TIME]))
                    ? " (1~P)" : ""))
                );
        };
        if (waiting_for(savegame[SG_MQ_REROLL_TIME])){
            show(LBL_MAINQUEST_MUSHHINT);
            actor[LBL_MAINQUEST_MUSHHINT].text =
                texts[TXT_MQ_MUSHHINT].split(
                    "%1").join(waiting_time(savegame[SG_MQ_REROLL_TIME]));
            arabize(LBL_MAINQUEST_MUSHHINT);
            MQDelayTimer.add_event_listener(TimerEvent.TIMER, MQDelayCheck);
            MQDelayTimer.start();
        } else {
            hide(LBL_MAINQUEST_MUSHHINT);
        };
        if (dungeon_nr == 100){
            add(SCR_TOWER_BG);
        } else {
            add(((SCR_QUEST_BG_1 + 50) + dungeon_nr));
        };
        set_cnt(MAINQUEST_enemy_BORDER, FIGHT_CHAR_BORDER);
        add(SCREEN_MAINQUEST);
        if (enemy < 0){
            i = 0;
            while (i < 10) {
                _local2 = actor[(CHARBACKGROUND + i)];
                with (_local2) {
                    x = actor[MAINQUEST_enemy].x;
                    y = actor[MAINQUEST_enemy].y;
                    scaleX = 1;
                    scaleY = 1;
                };
                i = (i + 1);
            };
            load_character_image();
        } else {
            set_cnt(MAINQUEST_enemy, (OPPMONSTER + enemy));
        };
        SelectedDungeon = dungeon_nr;
    };
    MQDelayCheck = function (evt:TimerEvent=None){
        if (!on_stage(SHP_MAINQUEST)){
            MQDelayTimer.remove_event_listener(TimerEvent.TIMER, MQDelayCheck);
            MQDelayTimer.stop();
            return;
        };
        if (waiting_for(savegame[SG_MQ_REROLL_TIME])){
            show(LBL_MAINQUEST_MUSHHINT);
            actor[LBL_MAINQUEST_MUSHHINT].text = texts[TXT_MQ_MUSHHINT].split(
                "%1").join(waiting_time(savegame[SG_MQ_REROLL_TIME]));
            set_title_bar(waiting_time(savegame[SG_MQ_REROLL_TIME]));
        } else {
            hide(LBL_MAINQUEST_MUSHHINT);
            set_title_bar();
            MQDelayTimer.remove_event_listener(TimerEvent.TIMER, MQDelayCheck);
            MQDelayTimer.stop();
        };
        if (text_dir == "right"){
            set_btn_text(
                MAINQUEST_START,
                (((waiting_for(savegame[SG_MQ_REROLL_TIME])) ? "(~P1) " : "")
                + texts[TXT_OK])
            );
        } else {
            set_btn_text(
                MAINQUEST_START,
                (texts[TXT_OK] + ((waiting_for(savegame[SG_MQ_REROLL_TIME]))
                    ? " (1~P)" : "")));
        };
    };
    var questText:* = "";
    if (savegame[SG_DUNGEON_13] < 122){
        savegame[SG_DUNGEON_13] = 122;
    };
    if (dungeon_nr == 100){
        questText = texts[(TXT_TOWER_enemy_NAMES + tower_level)].split("|")[1];
    } else {
        if (dungeon_nr == 12){
            questText = texts[
                ((TXT_QUEST_TEXT + (dungeon_nr * 10))
                + ((((int(savegame[SG_DUNGEON_13]) - 2) < 120))
                   ? 0 : ((int(savegame[SG_DUNGEON_13]) - 2) - 120)))];
        } else {
            if (dungeon_nr >= 10){
                questText = texts[
                    ((TXT_QUEST_TEXT + (dungeon_nr * 10))
                    + ((((int(savegame[((SG_NEW_DUNGEONS + dungeon_nr) - 10)])
                    - 2) < 0)) ? 0 : (int(savegame[((SG_NEW_DUNGEONS
                    + dungeon_nr) - 10)]) - 2)))];
            } else {
                questText = texts[
                    ((TXT_QUEST_TEXT + (dungeon_nr * 10))
                    + ((((int(savegame[(SG_DUNGEON_LEVEL + dungeon_nr)])
                    - 2) < 0)) ? 0 : (int(savegame[(SG_DUNGEON_LEVEL
                    + dungeon_nr)]) - 2)))];
            };
        };
    };
    hasLostMQ = False;
    Lastdungeon_nr = dungeon_nr;
    LastDungeonenemy = enemy;
    load(SCREEN_MAINQUEST);
    if (dungeon_nr == 100){
        load(SCR_TOWER_BG);
    } else {
        load(((SCR_QUEST_BG_1 + 50) + dungeon_nr));
    };
    load(FIGHT_CHAR_BORDER);
    if (enemy >= 0){
        load((OPPMONSTER + enemy));
    };
    when_loaded(Doshow_main_quest_screen);
    '''
    print dungeon_nr, enemy


def show_toilet(
        is_full, toilet_level, toilet_exp, toilet_max_exp, item_added=-1
):
    '''
    var doShowToilet:* = None;
    var is_full:* = is_full;
    var toilet_level:* = toilet_level;
    var toilet_exp:* = toilet_exp;
    var toilet_max_exp:* = toilet_max_exp;
    var item_added = item_added;
    doShowToilet = function (buildScreen=True){
        var i:* = 0;
        var toiletItemAddFrame:* = 0;
        var toiletItemAddTimer:* = None;
        var gatheredItemId:* = 0;
        var itemDestX:* = NaN;
        var itemDestY:* = NaN;
        var toiletItemAddFrameEvent:* = None;
        var buildScreen:Boolean = buildScreen;
        toiletTankDest = (toilet_exp / toilet_max_exp);
        toiletTankAdjustTimer.stop();
        if (buildScreen){
            toiletTankCurrent = toiletTankDest;
            remove(CHAR_RIGHTPANE);
            add(SCREEN_TOILET);
            hide(TOILET_OVERLAYS);
            show(TOILET_CHAIN);
        };
        display_inventory(None, True);
        enable_popup(
            CA_TOILET_TANK,
            texts[TXT_TOILET_HINT].split(
                "%1").join(str(int((toiletTankDest * 100)))).split(
                "%2").join(str(toilet_exp)).split(
                "%3").join(str(toilet_max_exp))
        );
        if (is_full == 0){
            hide(TOILET_IDLE);
        } else {
            show(TOILET_IDLE);
        };
        hide(TOILET_DROP);
        actor[LBL_TOILET_AURA].text = texts[(TXT_TOILET_HINT + 4)].split(
            "#").join(chr(13)).split("%1").join(str(toilet_level));
        actor[LBL_TOILET_AURA].x = (
            (SCR_SHOP_BG_X + 248) - (actor[LBL_TOILET_AURA].text_width / 2));
        toilet_tank_adjust_event();
        if (toiletTankDest != toiletTankCurrent){
            toiletTankAdjustTimer.start();
        };
        if (item_added >= 0){
            toiletItemAddFrameEvent = function (evt:TimerEvent){
                if ((((toiletItemAddFrame >= 50)) or (!(on_stage(TOILET))))){
                    actor[gatheredItemId].x = itemDestX;
                    actor[gatheredItemId].y = itemDestY;
                    actor[gatheredItemId].alpha = 1;
                    toiletItemAddTimer.stop();
                    toiletItemAddTimer.remove_event_listener(
                       TimerEvent.TIMER, toiletItemAddFrameEvent
                    );
                } else {
                    if (toiletItemAddFrame >= 35){
                        actor[gatheredItemId].alpha = 1;
                        actor[gatheredItemId].x = (
                            (actor[gatheredItemId].x + itemDestX) / 2);
                        actor[gatheredItemId].y = (
                            (actor[gatheredItemId].y + itemDestY) / 2);
                    } else {
                        actor[gatheredItemId].alpha = (toiletItemAddFrame / 35)
                        actor[gatheredItemId].y = (actor[gatheredItemId].y - 5)
                    };
                };
                i = 0;
                while (i < 7) {
                    hide((TOILET_FLUSH + i));
                    i++;
                };
                show((TOILET_FLUSH + int(((toiletItemAddFrame / 50) * 7))));
                toiletItemAddFrame++;
            };
            toiletItemAddFrame = 0;
            toiletItemAddTimer = new Timer(25);
            play(SND_TOILET_FLUSH);
            toiletItemAddTimer.add_event_listener(
                TimerEvent.TIMER, toiletItemAddFrameEvent
            );
            toiletItemAddTimer.start();
            gatheredItemId = (CHAR_SLOT_11 + item_added);
            Switch (item_added){
                if case(0:
                    itemDestX = CHAR_SLOTS_LEFT_X;
                    itemDestY = CHAR_SLOTS_ROW5_Y;
                    break;
                if case(1:
                    itemDestX = CHAR_SLOTS_R5C2_X;
                    itemDestY = CHAR_SLOTS_ROW5_Y;
                    break;
                if case(2:
                    itemDestX = CHAR_SLOTS_R5C3_X;
                    itemDestY = CHAR_SLOTS_ROW5_Y;
                    break;
                if case(3:
                    itemDestX = CHAR_SLOTS_R5C4_X;
                    itemDestY = CHAR_SLOTS_ROW5_Y;
                    break;
                if case(4:
                    itemDestX = CHAR_SLOTS_RIGHT_X;
                    itemDestY = CHAR_SLOTS_ROW5_Y;
                    break;
            };
            actor[gatheredItemId].alpha = 0;
            actor[gatheredItemId].x = (SCR_SHOP_BG_X + 205);
            actor[gatheredItemId].y = 590;
        };
    };
    if (on_stage(TOILET)){
        doshow_toilet(False);
        return;
    };
    load(SCREEN_TOILET);
    show_character_screen();
    when_loaded(doShowToilet);
    '''
    print is_full, toilet_level, toilet_exp, toilet_max_exp, item_added


def show_witch(witch_data, chaldron_bubble=False, enchant_cost=0):
    '''
    var doShowWitch:* = None;
    var witch_data:* = witch_data;
    var chaldron_bubble:Boolean = chaldron_bubble;
    var enchant_cost = enchant_cost;
    doShowWitch = function (buildScreen=True){
        var i;
        if (buildScreen){
            remove(CHAR_RIGHTPANE);
            add(SCREEN_WITCH);
        };
        if (!light_mode){
            witch_ani_timer.start();
        };
        witchDesiredType = witch_data[3];
        display_inventory(None, False, False, 0, True);
        i = 0;
        while (i < int(witch_data[7])) {
            load(GetItemID(14, int(witch_data[(9 + (3 * i))]), None, 0));
            set_cnt(
                (WITCH_SCROLL + i),
                GetItemID(14, int(witch_data[(9 + (3 * i))]),
                None,
                0)
            );
            suggestion_slot[(WITCH_SCROLL + i)] = (
                CHAR_SLOT_1 + CorrectItemType.find(math.floor(
                   (int(witch_data[(9 + (3 * i))]) / 10))));
            trace(
                i,
                savegame[((SG_INVENTORY_OFFS + (CorrectItemType.find(
                    math.floor((int(witch_data[(9 + (3 * i))]) / 10))
                ) * SG['ITM']['SIZE'])) + SG_ITM_EXT_ENCHANT)]);
            if (
                savegame[((SG_INVENTORY_OFFS + (CorrectItemType.find(
                    math.floor((int(witch_data[(9 + (3 * i))]) / 10))
                    ) * SG['ITM']['SIZE'])) + SG_ITM_EXT_ENCHANT)] != 0
                ){
                actor[(WITCH_SCROLL + i)].alpha = 0.5;
                enable_popup(
                    (WITCH_SCROLL + i),
                    POPUP_BEGIN_LINE,
                    texts[
                        ((TXT_ITMNAME_14 + int(witch_data[(9 + (3 * i))])) - 1)
                    ].split("|")[0],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[
                        (TXT_ITMNAME_14 + int(witch_data[(9 + (3 * i))])) - 1
                    ].split("|")[1],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[TXT_SCROLL_DATE].split(
                        "%1").join(time_str(Number(
                            witch_data[(10 + (3 * i))]), True)),
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[TXT_SCROLL_BOUGHT],
                    POPUP_END_LINE
                );
            } else {
                if (enchant_cost){
                    actor[(WITCH_SCROLL + i)].alpha = 1;
                    enable_popup(
                        (WITCH_SCROLL + i),
                        POPUP_BEGIN_LINE,
                        texts[((TXT_ITMNAME_14 + int(
                            witch_data[(9 + (3 * i))])) - 1)].split("|")[0],
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        texts[((TXT_ITMNAME_14 + int(
                           witch_data[(9 + (3 * i))])) - 1)].split("|")[1],
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        texts[TXT_SCROLL_DATE].split(
                            "%1").join(time_str(Number(witch_data[
                                (10 + (3 * i))]), True)),
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        texts[TXT_SCROLL_BUYNOW],
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        actor[IF_GOLD],
                        str(math.floor((enchant_cost / 100))),
                        POPUP_END_LINE
                    );
                } else {
                    actor[(WITCH_SCROLL + i)].alpha = 1;
                    enable_popup(
                        (WITCH_SCROLL + i),
                        POPUP_BEGIN_LINE,
                        texts[((TXT_ITMNAME_14 + int(
                            witch_data[(9 + (3 * i))])) - 1)].split("|")[0],
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        texts[((TXT_ITMNAME_14 + int(witch_data[
                            (9 + (3 * i))])) - 1)].split("|")[1],
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        texts[TXT_SCROLL_DATE].split(
                            "%1").join(time_str(Number(
                                witch_data[(10 + (3 * i))]), True)),
                        POPUP_END_LINE,
                        POPUP_BEGIN_LINE,
                        texts[TXT_SCROLL_BUYHINT],
                        POPUP_END_LINE
                    );
                };
            };
            actor[(WITCH_SCROLL + i)].scaleX = 0.8;
            actor[(WITCH_SCROLL + i)].scaleY = 0.8;
            add((WITCH_SCROLL + i));
            i++;
        };
        if (witch_data[2] == -1){
            enable_popup(CA_WITCH, texts[(TXT_WITCH_HINT + 6)]);
            enable_popup(CA_CHALDRON, texts[(TXT_WITCH_HINT + 7)]);
        } else {
            if (witch_data[5] == 0){
                enable_popup(
                    CA_WITCH,
                    texts[TXT_WITCH_HINT].split(
                        "%1").join(texts[((TXT_WITCH_HINT + 12) + int(
                            witch_data[3]))])
                    );
                enable_popup(
                    CA_CHALDRON,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_WITCH_HINT + 2)],
                    (POPUP_TAB + 100),
                    texts[((TXT_WITCH_HINT + 12) + int(witch_data[3]))],
                    POPUP_END_LINE,
                    POPUP_BEGIN_LINE,
                    texts[(TXT_WITCH_HINT + 3)],
                    (POPUP_TAB + 100),
                    texts[(TXT_WITCH_HINT + 4)].split(
                        "%1").join(str((math.round((
                            (witch_data[1] / witch_data[2]) * 100000)) / 1000))
                            ).split(
                        "%2").join(str(witch_data[2])),
                    POPUP_END_LINE
                );
            } else {
                enable_popup(CA_WITCH, texts[(TXT_WITCH_HINT + 1)]);
                enable_popup(CA_CHALDRON, texts[(TXT_WITCH_HINT + 5)]);
            };
        };
    };
    if (chaldron_bubble){
        play(SND_TOILET_DROP);
    };
    if (on_stage(WITCH)){
        doshow_witch(False);
        return;
    };
    load(SCREEN_WITCH);
    show_character_screen(None, True);
    when_loaded(doShowWitch);
    '''
    print witch_data, chaldron_bubble, enchant_cost


def showalbum_content(evt=None):
    '''
    var i:* = 0;
    var entryText:* = None;
    var hintText:* = None;
    var hunterOffs:* = 0;
    var actor_id:* = 0;
    var contentCount:* = 0;
    var catMax:* = None;
    var catCount:* = None;
    var evt:* = evt;
    var SetAlbumItems:* = function (
        aOffs, itmTyp, itm_pic, itm_class
    ){
        var itemSet:Array;
        var anyItem:Boolean;
        var j;
        itemSet = list();
        anyItem = False;
        j = 0;
        while (j < 5) {
            itemSet[j] = album_content[(aOffs + j)];
            if (itemSet[j] == 1){
                anyItem = True;
            };
            j++;
        };
        if (anyItem){
            entryText = GetItemName(itmTyp, itm_pic, itm_class);
            if (itm_class > 0){
                itm_class--;
            };
            set_cnt(
               (ALBUM_WEAPON_1 + i),
               GetItemID(itmTyp, itm_pic, 0, itm_class)
            );
            set_cnt(
               (ALBUM_WEAPON_2 + i),
               GetItemID(itmTyp, itm_pic, 1, itm_class)
            );
            set_cnt(
               (ALBUM_WEAPON_3 + i),
               GetItemID(itmTyp, itm_pic, 2, itm_class)
            );
            set_cnt(
                (ALBUM_WEAPON_4 + i),
                GetItemID(itmTyp, itm_pic, 3, itm_class)
            );
            set_cnt(
               (ALBUM_WEAPON_5 + i),
               GetItemID(itmTyp, itm_pic, 4, itm_class)
            );
            actor[(ALBUM_WEAPON_1 + i)].alpha = ((itemSet[0]) ? 1 : 0.3);
            actor[(ALBUM_WEAPON_2 + i)].alpha = ((itemSet[1]) ? 1 : 0.3);
            actor[(ALBUM_WEAPON_3 + i)].alpha = ((itemSet[2]) ? 1 : 0.3);
            actor[(ALBUM_WEAPON_4 + i)].alpha = ((itemSet[3]) ? 1 : 0.3);
            actor[(ALBUM_WEAPON_5 + i)].alpha = ((itemSet[4]) ? 1 : 0.3);
            if (showAlbumOffset){
                enable_popup((ALBUM_WEAPON_1 + i), str((aOffs + 0)));
                enable_popup((ALBUM_WEAPON_2 + i), str((aOffs + 1)));
                enable_popup((ALBUM_WEAPON_3 + i), str((aOffs + 2)));
                enable_popup((ALBUM_WEAPON_4 + i), str((aOffs + 3)));
                enable_popup((ALBUM_WEAPON_5 + i), str((aOffs + 4)));
            } else {
                enable_popup((ALBUM_WEAPON_1 + i));
                enable_popup((ALBUM_WEAPON_2 + i));
                enable_popup((ALBUM_WEAPON_3 + i));
                enable_popup((ALBUM_WEAPON_4 + i));
                enable_popup((ALBUM_WEAPON_5 + i));
                if ((((itmTyp == 1)) and ((itm_class > 1)))){
                };
            };
        };
        if (showAlbumOffset){
            enable_popup(
                (LBL_ALBUM_HEADING + i),
                ((str(aOffs) + " - ") + str((aOffs + 4)))
            );
        };
    };
    var SetAlbumEpic:* = function (
        aOffs, itmTyp, itm_pic, itm_class
    ){
        if (album_content[aOffs] == 1){
            entryText = GetItemName(itmTyp, itm_pic, itm_class);
            if (entryText.find("|") != -1){
                hintText = entryText.split("|")[1].split("#").join(chr(13));
                entryText = entryText.split("|")[0];
            };
            if (itm_class > 0){
                itm_class--;
            };
            set_cnt(
               (ALBUM_WEAPON_EPIC + i),
               GetItemID(itmTyp, itm_pic, 0, itm_class));
            if (showAlbumOffset){
                enable_popup((ALBUM_WEAPON_EPIC + i), str(aOffs));
            } else {
                enable_popup((ALBUM_WEAPON_EPIC + i));
            };
        };
        if (showAlbumOffset){
            enable_popup((LBL_ALBUM_HEADING + i), str(aOffs));
        };
    };
    entryText = "";
    hintText = "";
    hunterOffs = 0;
    album_clear();
    actor_id = 0;
    if (evt){
        actor_id = get_actor_id(evt.target);
    };
    if (actor_id == ALBUM_PREV){
        albumPage--;
    };
    if (actor_id == ALBUM_NEXT){
        albumPage++;
    };
    if (
        (((actor_id >= ALBUM_CAT_OUT))
        and ((actor_id <= (ALBUM_CAT_OUT + 4))))
    ){
        albumCat = (actor_id - ALBUM_CAT_OUT);
        albumPage = 0;
    };
    hide(ALBUM_CAT_IN);
    show((ALBUM_CAT_IN + albumCat));
    contentCount = 0;
    catMax = [252, 246, 506, 348, 348];
    catCount = [0, 0, 0, 0, 0];
    i = 0;
    while (i < album_content.length) {
        if (album_content[i] == 1){
            if (i < 300){
                var _local3 = catCount;
                var _local4;
                var _local5 = (_local3[_local4] + 1);
                _local3[_local4] = _local5;
            } else {
                if (i < 792){
                    _local3 = catCount;
                    _local4 = 1;
                    _local5 = (_local3[_local4] + 1);
                    _local3[_local4] = _local5;
                } else {
                    if (i < 1804){
                        _local3 = catCount;
                        _local4 = 2;
                        _local5 = (_local3[_local4] + 1);
                        _local3[_local4] = _local5;
                    } else {
                        if (i < 2500){
                            _local3 = catCount;
                            _local4 = 3;
                            _local5 = (_local3[_local4] + 1);
                            _local3[_local4] = _local5;
                        } else {
                            _local3 = catCount;
                            _local4 = 4;
                            _local5 = (_local3[_local4] + 1);
                            _local3[_local4] = _local5;
                        };
                    };
                };
            };
            contentCount = (contentCount + 1);
        };
        i = (i + 1);
    };
    if (contentCount > contentMax){
        contentCount = contentMax;
    };
    i = 0;
    while (i < 5) {
        if (catCount[i] > catMax[i]){
            catCount[i] = catMax[i];
        };
        i = (i + 1);
    };
    actor[LBL_ALBUM_COLLECTION].text = texts[TXT_COLLECTION].split(
        "%1").join(str(contentCount)).split(
        "%2").join(str(contentMax)).split(
        "%3").join(str((math.round((
            (contentCount / contentMax) * 10000)) / 100))).split(
        "#").join(chr(13)
    );
    i = 0;
    while (i < 5) {
        enable_popup(
            (ALBUM_CAT_IN + i),
            (((((((texts[((TXT_COLLECTION + 2) + i)] + chr(13))
                + catCount[i]) + " / ") + catMax[i]) + " = ")
                + str((math.round(((catCount[i] / catMax[i]) * 10000)) / 100)))
                + "%"));
        enable_popup(
            (ALBUM_CAT_OUT + i),
            (((((((texts[((TXT_COLLECTION + 2) + i)] + chr(13)) + catCount[i])
                + " / ") + catMax[i]) + " = ")
                + str((math.round(((catCount[i] / catMax[i]) * 10000)) / 100)))
                + "%"));
        i = (i + 1);
    };
    enable_popup(LBL_ALBUM_COLLECTION, texts[(TXT_COLLECTION + 7)]);
    i = 0;
    while (i < 4) {
        hintText = "";
        enable_popup((LBL_ALBUM_HEADING + i));
        enable_popup((ALBUM_MONSTER_FRAME + i));
        if (albumCat == 0){
            show((ALBUM_MONSTER_FRAME + i));
            if (albumPage > 62){
                albumPage = 0;
            };
            if (albumPage < 0){
                albumPage = 62;
            };
            if (album_content[((albumPage * 4) + i)] == 1){
                set_cnt(
                   (ALBUM_MONSTER + i),
                   ((OPPMONSTER + (albumPage * 4)) + i)
                );
                if (((albumPage * 4) + i) >= 220){
                    entryText = texts[
                        (((TXT_NEW_MONSTER_NAMES + (albumPage * 4)) + i) - 220)
                    ];
                } else {
                    entryText = texts[
                        ((TXT_MONSTER_NAME + (albumPage * 4)) + i)
                    ];
                };
            } else {
                set_cnt((ALBUM_MONSTER + i), UNKNOWN_enemy);
                entryText = texts[TXT_UNKNOWN];
            };
            if (showAlbumOffset){
                enable_popup(
                    (ALBUM_MONSTER_FRAME + i), str(((albumPage * 4) + i))
                );
            };
            if (showAlbumOffset){
                enable_popup(
                    (LBL_ALBUM_HEADING + i), str(((albumPage * 4) + i))
                );
            };
        } else {
            if (albumCat == 1){
                entryText = texts[TXT_UNKNOWN];
                if (albumPage > 25){
                    albumPage = 0;
                };
                if (albumPage < 0){
                    albumPage = 25;
                };
                if (albumPage <= 5){
                    if ((((albumPage < 5)) or ((i <= 0)))){
                        SetAlbumItems(
                            ((300 + (albumPage * 20)) + (i * 5)), 8,
                            ((1 + (albumPage * 4)) + i), 0
                        );
                    } else {
                        entryText = "";
                    };
                } elif (albumPage <= 7){
                    SetAlbumEpic(
                        ((510 + ((albumPage - 6) * 4)) + i), 8,
                        ((50 + ((albumPage - 6) * 4)) + i), 0
                    );
                } elif (albumPage <= 11){
                    SetAlbumItems(
                        ((526 + ((albumPage - 8) * 20))
                        + (i * 5)), 9, ((1 + ((albumPage - 8) * 4))
                        + i), 0
                    );
                } elif (albumPage <= 13){
                    SetAlbumEpic(
                        ((686 + ((albumPage - 12) * 4)) + i), 9,
                        ((50 + ((albumPage - 12) * 4)) + i), 0
                    );
                } elif (albumPage <= 23){
                    if ((((albumPage < 23)) or ((i <= 0)))){
                        SetAlbumEpic(
                            (702 + ((albumPage - 14) * 4) + i),
                            10,
                            ((1 + ((albumPage - 14) * 4)) + i),
                            0
                        );
                    } else {
                        entryText = "";
                    };
                } elif (albumPage <= 25){
                    SetAlbumEpic(
                        ((760 + 16 + (albumPage
                         - 24) * 4) + i),
                        10,
                        ((50 + ((albumPage - 24) * 4)) + i),
                        0
                    );

            } else {
                if (albumCat == 2){
                    entryText = texts[TXT_UNKNOWN];
                    if (albumPage > 39){
                        albumPage = 0;
                    };
                    if (albumPage < 0){
                        albumPage = 39;
                    };
                    if (albumPage <= 7){
                        if ((((albumPage < 7)) or ((i <= 1)))){
                            SetAlbumItems(
                                (((776 + 16) + (albumPage * 20)) + (i * 5)),
                                1,
                                ((1 + (albumPage * 4)) + i),
                                1
                            );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 9){
                        SetAlbumEpic(
                            (((1076 + 16) + ((albumPage - 8) * 4)) + i),
                            1,
                            ((50 + ((albumPage - 8) * 4)) + i),
                            1
                        );
                    } elif (albumPage <= 12){
                        if ((((albumPage < 12)) or ((i <= 1)))){
                            SetAlbumItems(
                                ((1092 + 16 + ((albumPage - 10) * 20))
                                    + (i * 5)),
                                2,
                                ((1 + ((albumPage - 10) * 4)) + i),
                                1
                            );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 14){
                        SetAlbumEpic(
                            ((1192 + 16)
                                + ((albumPage - 13) * 4)) + i,
                            2,
                            ((50 + ((albumPage - 13) * 4)) + i),
                            1
                        );
                    } elif (albumPage <= 17){
                        if ((((albumPage < 17)) or ((i <= 1)))){
                            SetAlbumItems(
                                (((1208 + 16)
                                    + ((albumPage - 15) * 20))
                                    + (i * 5)),
                                3,
                                (1 + ((albumPage - 15) * 4))
                                    + i,
                                1
                            );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 19){
                        SetAlbumEpic(
                            (((1308 + 16)
                                + ((albumPage - 18) * 4))
                                + i),
                            3,
                            ((50 + ((albumPage - 18) * 4))
                                + i),
                            1
                        );
                    } elif (albumPage <= 22){
                        if (
                            (((albumPage < 22))
                            or ((i <= 1)))
                        ){
                            SetAlbumItems(
                                (((1324 + 16)
                                 + ((albumPage - 20)
                                 * 20)) + (i * 5)),
                            4,
                            ((1 + ((albumPage - 20)
                                * 4)) + i),
                            1
                        );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 24){
                        SetAlbumEpic(
                            (((1424 + 16)
                              + ((albumPage - 23)
                              * 4)) + i),
                        4,
                        ((50 + ((albumPage - 23)
                             * 4)) + i),
                        1
                    );
                    } elif (albumPage <= 27){
                        if (
                            (((albumPage < 27))
                            or ((i <= 1)))
                        ){
                            SetAlbumItems(
                                (((1440 + 16)
                                 + ((albumPage
                                 - 25) * 20))
                                 + (i * 5)),
                                5,
                                ((1 +
                                  ((albumPage
                                   - 25) * 4))
                                   + i),
                                1
                            );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 29){
                        SetAlbumEpic(
                            (((1540 + 16)
                              + ((albumPage
                              - 28) * 4))
                              + i),
                            5,
                            ((50 +
                              ((albumPage
                               - 28) * 4))
                               + i),
                            1
                        );
                    } elif (albumPage <= 32){
                        if ((((albumPage < 32)) or ((i <= 1)))){
                            SetAlbumItems(
                                (1556 + 16 + (albumPage - 30) * 20) + (i * 5),
                                6,
                                ((1 + ((albumPage - 30) * 4)) + i),
                                1
                            );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 34){
                        SetAlbumEpic(
                            (((1656 + 16) + ((albumPage - 33) * 4)) + i),
                            6,
                            ((50 + ((albumPage - 33) * 4)) + i),
                            1
                        );
                    } elif (albumPage <= 37){
                        if ((((albumPage < 37)) or ((i <= 1)))){
                            SetAlbumItems(
                                (1672 + 16 + (albumPage - 35) * 20) + (i * 5),
                                7,
                                ((1 + ((albumPage - 35) * 4)) + i),
                                1
                            );
                        } else {
                            entryText = "";
                        };
                    } elif (albumPage <= 39){
                        SetAlbumEpic(
                            (((1772 + 16) + ((albumPage - 38) * 4)) + i),
                            7,
                            ((50 + ((albumPage - 38) * 4)) + i),
                            1
                        );


                } else {
                    if ((((albumCat == 3)) or ((albumCat == 4)))){
                        entryText = texts[TXT_UNKNOWN];
                        if (albumPage > 29){
                            albumPage = 0;
                        };
                        if (albumPage < 0){
                            albumPage = 29;
                        };
                        hunterOffs = (((albumCat)==3) ? 0 : 696 + 16);
                        if (albumPage <= 2){
                            if ((((albumPage < 2)) or ((i <= 1)))){
                                SetAlbumItems(
                                    (((1788 + hunterOffs)
                                     + (albumPage * 20)) + (i * 5)),
                                    1,
                                    ((1 + (albumPage * 4)) + i),
                                    (albumCat - 1)
                                );
                            } else {
                                entryText = "";
                            };
                        } elif (albumPage <= 4){
                            SetAlbumEpic(
                                (((1888 + hunterOffs)
                                  + ((albumPage - 3) * 4)) + i),
                                1,
                                ((50 + ((albumPage - 3) * 4)) + i),
                                (albumCat - 1)
                            );
                        } elif (albumPage <= 7){
                            if ((((albumPage < 7)) or ((i <= 1)))){
                                SetAlbumItems(
                                    (((1904 + hunterOffs)
                                     + ((albumPage - 5) * 20))
                                     + (i * 5)),
                                    3,
                                    ((1 + ((albumPage - 5) * 4)) + i),
                                    (albumCat - 1)
                                );
                            } else {
                                entryText = "";
                            };
                        } elif (albumPage <= 9){
                            SetAlbumEpic(
                                (((2004 + hunterOffs)
                                 + ((albumPage - 8) * 4)) + i),
                                3,
                                ((50 + ((albumPage - 8) * 4)) + i),
                                (albumCat - 1)
                            );
                        } elif (albumPage <= 12){
                            if (
                                (((albumPage < 12))
                                or ((i <= 1)))
                            ){
                                SetAlbumItems(
                                    (((2020 + hunterOffs)
                                     + ((albumPage - 10) * 20))
                                     + (i * 5)),
                                    4,
                                    ((1 + ((albumPage
                                        - 10) * 4)) + i),
                                    (albumCat - 1)
                                );
                            } else {
                                entryText = "";
                            };
                        } elif (albumPage <= 14){
                            SetAlbumEpic(
                                (((2120 + hunterOffs)
                                    + ((albumPage - 13)
                                    * 4)) + i),
                                4,
                                ((50 + ((albumPage
                                    - 13) * 4)) + i),
                                (albumCat - 1)
                            );
                        } elif (albumPage <= 17){
                            if ((((albumPage < 17)) or ((i <= 1)))){
                                SetAlbumItems(
                                    (((2136 + hunterOffs)
                                     + ((albumPage - 15) * 20)) + (i * 5)),
                                    5,
                                    ((1 + ((albumPage - 15) * 4)) + i),
                                    (albumCat - 1)
                                );
                            } else {
                                entryText = "";
                            };
                        } elif (albumPage <= 19){
                            SetAlbumEpic(
                                (2236 + hunterOffs + (albumPage - 18) * 4) + i,
                                5,
                                (50 + ((albumPage - 18) * 4)) + i,
                                (albumCat - 1)
                            );
                        } elif (albumPage <= 22){
                            if ((((albumPage < 22)) or ((i <= 1)))){
                                SetAlbumItems(
                                    (((2252 + hunterOffs)
                                     + ((albumPage - 20) * 20)) + (i * 5)),
                                    6,
                                    ((1 + ((albumPage - 20) * 4)) + i),
                                    (albumCat - 1)
                                );
                            } else {
                                entryText = "";
                            };
                        } elif (albumPage <= 24){
                            SetAlbumEpic(
                                (((2352 + hunterOffs)
                                  + ((albumPage - 23) * 4)) + i),
                                6, ((50 + ((albumPage - 23) * 4)) + i),
                                (albumCat - 1)
                            );
                        } elif (albumPage <= 27){
                            if ((((albumPage < 27)) or ((i <= 1)))){
                                SetAlbumItems(
                                    (((2368 + hunterOffs)
                                        + ((albumPage - 25) * 20)) + (i * 5)),
                                    7,
                                    ((1 + ((albumPage - 25) * 4)) + i),
                                    (albumCat - 1)
                                );
                            } else {
                                entryText = "";
                            };
                        } elif (albumPage <= 29){
                            SetAlbumEpic(
                                (((2468 + hunterOffs)
                                    + ((albumPage - 28) * 4)) + i),
                                7,
                                ((50 + ((albumPage - 28) * 4)) + i),
                                (albumCat - 1)
                            );


        actor[LBL_ALBUM_PAGENUMBER_LEFT].text = str(((albumPage * 2) + 1));
        actor[LBL_ALBUM_PAGENUMBER_RIGHT].text = str(((albumPage * 2) + 2));
        actor[LBL_ALBUM_PAGENUMBER_RIGHT].x = (
            1205 - actor[LBL_ALBUM_PAGENUMBER_RIGHT].text_width
        );
        actor[(LBL_ALBUM_HEADING + i)].text = entryText;
        actor[(LBL_ALBUM_HEADING + i)].x = (
            ((i)<=1)
                ? 535
                : 1005 - (actor[(LBL_ALBUM_HEADING + i)].text_width / 2));
        actor[(LBL_ALBUM_HINT + i)].text = hintText;
        actor[(LBL_ALBUM_HINT + i)].x = (
            ((i)<=1)
                ? 535
                : 1005 - (actor[(LBL_ALBUM_HINT + i)].text_width / 2));
        i = (i + 1);
    };
    if (
        ((!((hintText == "")))
        and (((actor[LBL_ALBUM_COLLECTION].x
             + actor[LBL_ALBUM_COLLECTION].text_width) > (
             actor[LBL_ALBUM_HINT].x - 5))))
    ){
        actor[LBL_ALBUM_COLLECTION].y = (
            (actor[LBL_ALBUM_HINT].y + actor[LBL_ALBUM_HINT].textHeight) + 5
        );
    } else {
        if (
            (actor[LBL_ALBUM_COLLECTION].x
             + actor[LBL_ALBUM_COLLECTION].text_width) > (
             actor[LBL_ALBUM_HEADING].x - 5)
        ){
            actor[LBL_ALBUM_COLLECTION].y = (
                (actor[LBL_ALBUM_HEADING].y
                 + actor[LBL_ALBUM_HEADING].textHeight) + 5);
        } else {
            actor[LBL_ALBUM_COLLECTION].y = 135;
        };
    };
    '''
    print evt


def show_login_screen(evt=None, no_bc=False, no_cookie=False):
    '''
    var player_name:String;
    if (
        ((((((((!(shared_obj.data.HasAccount))
        and (!((evt is MouseEvent)))))
        and (!(no_bc))))
        and (!(buffed_mode))))
        and (!(sso_mode)))
    ){
        show_build_character_screen();
        return;
    };
    remove_all();
    actor[INP['LOGIN_PASSWORD']].getChildAt(1).visible = True;
    actor[LBL_WINDOW_TITLE].text = texts[TXT_WELCOME];
    actor[LBL_WINDOW_TITLE].x = (
        (IF_WIN_X + IF_WIN_WELCOME_X) - int(
        (actor[LBL_WINDOW_TITLE].text_width / 2)));
    actor[INP['NAME']].add_event_listener(KeyboardEvent.KEY_DOWN, RequestLOGin)
    actor[INP['LOGIN_PASSWORD']].add_event_listener(
        KeyboardEvent.KEY_DOWN, RequestLOGin
    );
    if (!no_cookie){
        if (shared_obj.data.userName){
            actor[INP['NAME']].getChildAt(1).text = str(
                shared_obj.data.userName);
        };
        if (shared_obj.data.password){
            actor[INP['LOGIN_PASSWORD']].getChildAt(1).text = str(
                shared_obj.data.password
            );
        };
    };
    add(WINDOW_LOGIN);
    log_on_rtl();
    if (buffed_mode){
        actor[LBL_GOTO_SIGNUP].htmlText = buffed_link_text;
        actor[GOTO_SIGNUP].x = (
            (IF_WIN_X + IF_WIN_WELCOME_X)
            - int((actor[LBL_GOTO_SIGNUP].text_width / 2)));
    };
    if (sso_mode){
        actor[INP['NAME']].getChildAt(1).type = TextFieldType.DYNAMIC;
        actor[INP['LOGIN_PASSWORD']].getChildAt(1).type = TextFieldType.DYNAMIC
        player_name = ExternalIF.call("sso_get_uid");
        actor[INP['NAME']].getChildAt(1).text = player_name;
        actor[INP['LOGIN_PASSWORD']].getChildAt(1).text = mp_api_user_token;
    };
    '''
    print evt, no_bc, no_cookie


def show_bet_result(won):
    '''
    var doShowBetResults:* = None;
    var won:* = won;
    doShowBetResults = function (){
        var BallX:* = 0;
        add(((won) ? HUTMANN_WON : HUTMANN_LOST));
        set_btn_text(
            HUTMANN_OK,
            texts[((won) ? TXT_HUTMANN_YEAH : TXT_HUTMANN_DAMN)]
        );
        add(HUTMANN_OK);
        var _local2 = actor[LBL_HUTMANN_TEXT];
        with (_local2) {
            text = texts[((won) ? TXT_HUTMANN_WIN : TXT_HUTMANN_LOSE)];
            x = (SCREEN_TITLE_X - (text_width / 2));
        };
        Switch (CupChosen){
            if case(0:
                add(HUTBECHER_1_CLICK);
                remove(HUTBECHER_1_IDLE);
                if (won){
                    BallX = HUTMANN_KUGEL_X1;
                } else {
                    BallX = (
                        (random.random())<0.5)
                            ? HUTMANN_KUGEL_X2
                            : HUTMANN_KUGEL_X3;
                };
                break;
            if case(1:
                add(HUTBECHER_2_CLICK);
                remove(HUTBECHER_2_IDLE);
                if (won){
                    BallX = HUTMANN_KUGEL_X2;
                } else {
                    BallX = (
                        (random.random())<0.5)
                        ? HUTMANN_KUGEL_X1
                        : HUTMANN_KUGEL_X3;
                };
                break;
            if case(2:
                add(HUTBECHER_3_CLICK);
                remove(HUTBECHER_3_IDLE);
                if (won){
                    BallX = HUTMANN_KUGEL_X3;
                } else {
                    BallX = (
                        (random.random())<0.5)
                        ? HUTMANN_KUGEL_X1
                        : HUTMANN_KUGEL_X2;
                };
                break;
        };
        actor[HUTKUGEL].x = BallX;
        if (won){
            play(SND_JINGLE);
            add(HUTKUGEL);
            actor[LBL_HUTMANN_GOLDBET].text = str(
                (int(actor[LBL_HUTMANN_GOLDBET].text) * 2));
            actor[LBL_HUTMANN_MUSHBET].text = str(
                (int(actor[LBL_HUTMANN_MUSHBET].text) * 2));
        } else {
            actor[LBL_HUTMANN_GOLDBET].text = "0";
            actor[LBL_HUTMANN_MUSHBET].text = "0";
        };
    };
    load(((won) ? HUTMANN_WON : HUTMANN_LOST));
    Switch (CupChosen){
        if case(0:
            load(HUTBECHER_1_CLICK);
            break;
        if case(1:
            load(HUTBECHER_2_CLICK);
            break;
        if case(2:
            load(HUTBECHER_3_CLICK);
            break;
    };
    if (won){
        load(HUTKUGEL);
    };
    when_loaded(doShowBetResults);
    '''
    print won


def show_signup_screen(evt=None):
    '''
    var i:* = 0;
    var j:* = 0;
    var jumpTimer:* = None;
    var player_name:* = None;
    var email:* = None;
    var DoJump:* = None;
    var evt:* = evt;
    jumpTimer = new Timer(200, 20);
    if (KlasseGewählt){
        remove_all();
        actor[INP['PASSWORD']].getChildAt(1).visible = True;
        actor[LBL_WINDOW_TITLE].text = texts[TXT_TITLE_SIGNUP];
        actor[LBL_WINDOW_TITLE].x = (
            (IF_WIN_X + IF_WIN_WELCOME_X)
            - int((actor[LBL_WINDOW_TITLE].text_width / 2)));
        actor[INP['NAME']].add_event_listener(
            KeyboardEvent.KEY_UP, request_signup);
        actor[INP['PASSWORD']].add_event_listener(
            KeyboardEvent.KEY_DOWN, request_signup);
        actor[INP['EMAIL']].add_event_listener(
            KeyboardEvent.KEY_DOWN, request_signup);
        if (buffed_req){
            actor[INP['NAME']].getChildAt(1).text = buffed_name;
            actor[INP['EMAIL']].getChildAt(1).text = buffed_email;
        };
        if (sso_mode){
            actor[INP['EMAIL']].getChildAt(1).type = TextFieldType.DYNAMIC;
            actor[INP['PASSWORD']].getChildAt(1).type = TextFieldType.DYNAMIC;
            player_name = ExternalIF.call("sso_get_uid");
            actor[INP['NAME']].getChildAt(1).text = player_name;
            email = ExternalIF.call("sso_get_email");
            actor[INP['EMAIL']].getChildAt(1).text = email;
            actor[INP['PASSWORD']].getChildAt(1).text = mp_api_user_token;
        };
        log_on_rtl();
        hide(
            PASSWORD_SMILEY_SAD,
            PASSWORD_SMILEY_NEUTRAL,
            PASSWORD_SMILEY_HAPPY
        );
        add(WINDOW_SIGNUP);
        if (param_bullshit_text != ""){
            add(FUCK);
        };
    } else {
        error_message(texts[TXT_ERROR_SELECTCLASS]);
        if (!SignupJumpRunning){
            DoJump = function (evt:TimerEvent){
                if (j <= 2){
                    i = 0;
                    while (i < 2) {
                        animate_ach(
                            ((KASTE_1_IDLE + i) + (j * 2)),
                            actor[((KASTE_1_IDLE + i) + (j * 2))].y
                        );
                        i++;
                    };
                };
                j++;
                if (j > 10){
                    jumpTimer.stop();
                    jumpTimer.remove_event_listener(TimerEvent.TIMER, DoJump);
                    SignupJumpRunning = False;
                };
            };
            SignupJumpRunning = True;
            jumpTimer.add_event_listener(TimerEvent.TIMER, DoJump);
            j = 0;
            jumpTimer.start();
        };
    };
    '''
    print evt


# -----------------------------------------------------------------------------
# low level graphic stuff


def remove(*actor_ids):
    '''
        remove actor
    '''
    for actor_id in actor_ids:
        if actor[actor_id]:
            if actor[actor_id] is list:
                for i_bunch in actor[actor_id]:
                    remove(i_bunch)
                return

            if actor[actor_id] is Sound:
                return

            with actor[actor_id]:
                if parent:
                    parent.removeChild(actor[actor_id])


def show(*actor_ids):
    '''
        show actor
    '''
    for actor_id in actor_ids:
        if actor[actor_id]:
            if actor[actor_id] is list:
                for i_bunch in actor[actor_id]:
                    show(i_bunch)
                return

            actor[actor_id].visible = True


def hide(*actor_ids):
    '''
        hide actor(s)
    '''
    for actor_id in actor_ids:
        if actor[actor_id]:
            if actor[actor_id] is list:
                for i_bunch in actor[actor_id]:
                    hide(i_bunch)
                return

            actor[actor_id].visible = False


def add(actor_id, pos_x=None, pos_y=None, scale_x=None,
        scale_y=None, vis=None, container_id=-1):
    '''
        add actor to global list
    '''
    if actor[actor_id] is Sound:
        return

    if actor[actor_id] is list:
        for i_bunch in actor[actor_id]:
            if i_bunch == actor_id:
                return

            add(i_bunch, pos_x, pos_y, scale_x, scale_y, vis, container_id)
        return

    if actor[actor_id] is Loader:
        if actorLoaded[actor_id] == 0:
            load(actor_id)

    if pos_x:
        actor[actor_id].x = pos_x

    if pos_y:
        actor[actor_id].y = pos_y

    if scale_x:
        actor[actor_id].scaleX = size_x

    if scale_y:
        actor[actor_id].scaleY = size_y

    if vis is not None:
        actor[actor_id].visible = bool(vis)

    if container_id == -1:
        addChild(actor[actor_id])
    else:
        actor[container_id].addChild(actor[actor_id])


def visible_to_front(*actor_ids):
    '''
        is visible from front of screen
    '''
    for actor_id in actor_ids:
        if actor[actor_id]:
            if actor[actor_id] is list:
                for i_bunch in actor[actor_id]:
                    visible_to_front(i_bunch)
                return

            with actor[actor_id]:
                if on_stage(actor_id):
                    actor[actor_id].add(actor_id)


def move(actor_id, pos_x, pos_y):
    '''
        move actor to coords x/y
    '''
    if actor[actor_id] is list:
        for current in actor[actor_id]:
            move(current, pos_x, pos_y)
    else:
        actor[actor_id].x_pos = pos_x
        actor[actor_id].y_pos = pos_y


def add_some(*args):
    '''
        add multiple actors
    '''
    for arg in args:
        if actor[arg]:
            if actor[arg] is list:
                for i_bunch in actor[arg]:
                    add(i_bunch)
                return

            add(arg)


def remove_all(also_persistent=False):
    '''
        remove all actors
    '''
    for i in range(len(actor)):
        if actor[i]:
            if actor[i] is not list:
                if (not actorPersistent[i]) or also_persistent:
                    remove(i)

    ExternalIF.call("hideSocial")


def visible(actor_id):
    '''
        actor is visible?
    '''
    if actor[actor_id] is DisplayObject:
        return bool(get_child_by_name(actor[actor_id].name)
                    and actor[actor_id].visible)
    return False


def set_alpha(actor_id, alpha_value):
    '''
        set alpha value for actor(s)
    '''
    if actor[actor_id] is list:
        for act in actor[actor_id]:
            set_alpha(act, alpha_value)
    elif getattr(actor[actor_id], 'alpha', None) is not None:
        actor[actor_id].alpha = alpha_value


def get_alpha(actor_id):
    '''
        get highest alpha value from actor(s)
    '''
    tmp_alpha = 0
    if actor[actor_id] is list:
        for act in actor[actor_id]:
            if get_alpha(act) > tmp_alpha:
                tmp_alpha = get_alpha(act)
        return tmp_alpha

    if getattr(actor[actor_id], 'alpha', None) is not None:
        return actor[actor_id].alpha

    return 0


def fade_in_event():
    '''
        update alpha for fade in
    '''
    current_alpha += alpha_step
    if current_alpha >= alpha_max:
        current_alpha = alpha_max
        fade_timer.stop()
        fade_timer.remove_event_listener(TimerEvent.TIMER, fade_in_event)
    set_alpha(actor_id, current_alpha)


def fade_in(actor_id, timer_interval=20, alpha_step=0.05, alpha_max=1):
    '''
        perform fade in animation on actor
    '''
    fade_timer = Timer(timer_interval)
    current_alpha = get_alpha(actor_id)
    if alpha_step <= 0:
        return

    fade_timer.add_event_listener(TimerEvent.TIMER, fade_in_event)
    fade_timer.start()
    set_alpha(actor_id, current_alpha)


def fade_out_event():
    '''
        update alpha for fade out
    '''
    current_alpha -= alpha_step
    if current_alpha <= alpha_min:
        current_alpha = alpha_min
        fade_timer.stop()
        fade_timer.remove_event_listener(TimerEvent.TIMER, fade_out_event)
        if hide_then:
            hide(actor_id)
    set_alpha(actor_id, current_alpha)


def fade_out(actor_id, timer_interval=20, alpha_step=0.05,
             alpha_min=0, hide_then=False):
    '''
        perform fade out animation on actor
    '''
    fade_timer = Timer(timer_interval)
    current_alpha = get_alpha(actor_id)
    if alpha_step <= 0:
        return

    fade_timer.add_event_listener(TimerEvent.TIMER, fade_out_event)
    fade_timer.start()
    set_alpha(actor_id, current_alpha)


def add_filter(actor_id, filter_obj):
    '''
        add filter to actor
    '''
    actor[actor_id].filters = filter_obj


def set_font(font_name):
    '''
        set up fonts by name
    '''
    game_font = font_name
    font_embedded = True
    if font_name in ("Verdana", "Arial Narrow", "Geeza Pro"):
        font_embedded = False
        size_mod = -6

    LOG.info("Font chosen: " + font_name)

    fmt = FontFormatToiletAura
    fmt.font = font_name
    fmt.size = size_mod + 35
    fmt.color = CLR['BLACK']
    fmt.align = "center"
    fmt.left_margin = 0
    fmt.kerning = True

    fmt = FontFormatGuildListTextAttackErrorHalf
    fmt.font = font_name
    fmt.size = size_mod + 24
    fmt.color = CLR['ATTACK']['ERROR']['OFFLINE_HALF']
    fmt.align = text_dir
    fmt.left_margin = 0
    fmt.kerning = True

    with FontFormatGuildListTextAttackErrorOnlineHalf:
        font = font_name
        size = size_mod + 24
        color = CLR['ATTACK']['ERROR']['ONLINE_HALF']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatError:
        font = font_name
        size = size_mod + 24
        color = CLR['ERROR']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatDefault:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatHighStakes:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['RED']
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatHighStakesHighLight:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['RED_HIGHLIGHT']
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatHighStakesHighLight:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['RED_GRAYED']
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatHighStakesHighLightGrayed:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['RED_HIGHLIGHT_GRAYED']
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatBook:
        font = font_name
        size = size_mod + 20
        color = 0
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatBookHint:
        font = font_name
        size = size_mod + 18
        color = 136
        align = "center"
        left_margin = 0
        kerning = True

    with FontFormatBookLeft:
        font = font_name
        size = size_mod + 16
        color = 0
        align = "left"
        left_margin = 0
        kerning = True

    with FontFormatBullshit:
        font = font_name
        size = 14
        color = CLR['SFORANGE']
        align = "left"
        left_margin = 0
        kerning = True

    with FontFormatAttackLabel:
        font = font_name
        size = size_mod + 19
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatSpeech:
        font = font_name
        size = size_mod + 20
        color = CLR['WHITE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGrayed:
        font = font_name
        size = size_mod + 20
        color = CLR['GRAYED']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGrayedHighLight:
        font = font_name
        size = size_mod + 20
        color = CLR['GRAYED_HL']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatClassError:
        font = font_name
        size = size_mod + 20
        color = CLR['ERROR']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatChat:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatChatWhisper:
        font = font_name
        size = size_mod + 20
        color = CLR['CHAT_WHISPER']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatChatError:
        font = font_name
        size = size_mod + 20
        color = CLR['ERROR']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildBuilding:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildMoney:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatDefaultLeft:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatHighlight:
        font = font_name
        size = size_mod + 20
        color = CLR['SFHIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatHighlightWhisper:
        font = font_name
        size = size_mod + 20
        color = CLR['SFHIGHLIGHT_WHISPER']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatHeading:
        font = font_name
        size = (size_mod + 30)
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatScreenTitle:
        font = font_name
        size = size_mod + 34
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopup:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopupCompare:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopupCompareSum:
        font = font_name
        size = size_mod + 20
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopupCompareBetter:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG_GREEN']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopupCompareWorse:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['RED']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopupCompareBetterHL:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['GREEN_HIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPopupCompareWorseHL:
        font = font_name
        size = size_mod + 20
        color = CLR['SYSMSG']['RED_HIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatEpicItemQuote:
        font = font_name
        size = size_mod + 20
        color = CLR['EPICITEMQUOTE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatItemEnchantment:
        font = font_name
        size = size_mod + 20
        color = CLR['ITEMENCHANTMENT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatLOGoutLink:
        font = font_name
        size = (size_mod + 22)
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatLOGoutLinkHighLight:
        font = font_name
        size = (size_mod + 22)
        color = CLR['SFHIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatHallListHeading:
        font = font_name
        size = (size_mod + 19)
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatHallListText:
        font = font_name
        size = (size_mod + 19)
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildHallNoAttack:
        font = font_name
        size = (size_mod + 19)
        color = CLR['NOATTACK']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatHallListHighLight:
        font = font_name
        size = (size_mod + 19)
        color = CLR['SFHIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatAttribBonus:
        font = font_name
        size = (size_mod + 19)
        color = CLR['ATTRIBBONUS']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatAttribTemp:
        font = font_name
        size = (size_mod + 19)
        color = CLR['SYSMSG']['GREEN']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatAttrib:
        font = font_name
        size = (size_mod + 19)
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPayIcon:
        font = font_name
        size = (size_mod + 19)
        color = CLR['WHITE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListHeading:
        font = font_name
        size = (size_mod + 26)
        color = CLR['SFORANGE']
        align = text_dir
        bold = True
        left_margin = 0
        kerning = True

    with FontFormatPostListText:
        font = font_name
        size = size_mod + 24
        color = CLR['SFORANGE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListTextSys:
        font = font_name
        size = size_mod + 24
        color = CLR['SYSMSG']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListText:
        font = font_name
        size = size_mod + 24
        color = CLR['OFFLINE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListTextOnline:
        font = font_name
        size = size_mod + 24
        color = CLR['ONLINE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListTextAttackError:
        font = font_name
        size = size_mod + 24
        color = CLR['ATTACK']['ERROR']['OFFLINE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListTextAttackErrorOnline:
        font = font_name
        size = size_mod + 24
        color = CLR['ATTACK']['ERROR']['ONLINE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListTextAttackErrorOnlinePopup:
        font = font_name
        size = size_mod + 20
        color = CLR['ATTACK']['ERROR']['ONLINE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListTextAttackOk:
        font = font_name
        size = size_mod + 24
        color = CLR['ATTACK']['OK']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatGuildListTextAttackOkPopup:
        font = font_name
        size = size_mod + 20
        color = CLR['ATTACK']['OK']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListHighLight:
        font = font_name
        size = size_mod + 24
        color = CLR['SFHIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListHighLightSys:
        font = font_name
        size = size_mod + 24
        color = CLR['SYSMSG']['HIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListTextSysRed:
        font = font_name
        size = size_mod + 24
        color = CLR['SYSMSG']['RED']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListHighLightSysRed:
        font = font_name
        size = size_mod + 24
        color = CLR['SYSMSG']['RED_HIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListTextSysGreen:
        font = font_name
        size = size_mod + 24
        color = CLR['SYSMSG']['GREEN']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatPostListHighLightSysGreen:
        font = font_name
        size = size_mod + 24
        color = CLR['SYSMSG']['GREEN_HIGHLIGHT']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatQuestBar:
        font = font_name
        size = size_mod + 24
        color = CLR['WHITE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatTimeBar:
        font = font_name
        size = size_mod + 24
        color = CLR['WHITE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatLifeBar:
        font = font_name
        size = size_mod + 20
        color = CLR['WHITE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatDamage:
        font = font_name
        size = (size_mod + 30)
        color = CLR['WHITE']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatCriticalDamage:
        font = font_name
        size = size_mod + 34
        color = CLR['RED']
        align = text_dir
        left_margin = 0
        kerning = True

    with FontFormatCatapultDamage:
        font = font_name
        size = size_mod + 38
        color = CLR['ATTACK']['ERROR']['ONLINE_HALF']
        align = text_dir
        left_margin = 0
        kerning = True


# -----------------------------------------------------------------------------
# unsorted stuff


def do_act_zauberladen():
    '''
        setup magic shop actors
    '''
    error_message(" ")
    remove(BNC['CHAR']['RIGHTPANE'])
    remove(IMG['FIDGET']['EPCIOVL'])
    remove(IMG['SHAKES']['EPCIOVL'])
    add(BNC['SCREEN']['FIDGET'])
    if savegame[SG['LEVEL']] >= 66:
        add(CA['GOTO']['WITCH'])
    if (special_action == 2) or (special_action == 5):
        add(IMG['FIDGET']['EPCIOVL'])
        actor[IMG['FIDGET']['EPCIOVL']].mouse_enabled = False
    if not sleep_time():
        remove(BNC['FIDGET']['NIGHT'])
    else:
        remove(BNC['FIDGET']['DAY'])
    if Capabilities.version.substr(0, 3) != "IOS":
        if light_mode:
            remove(IMG['FIDGET']['TAGKERZE'])
            remove(IMG['FIDGET']['NACHTKERZE'])
    remove(IMG['FIDGET']['BLINZELN'])


def do_act_schmiede():
    '''
        setup weapon shop actors
    '''
    error_message(" ")
    remove(BNC['CHAR']['RIGHTPANE'])
    remove(IMG['FIDGET']['EPCIOVL'])
    remove(IMG['SHAKES']['EPCIOVL'])
    add(BNC['SCREEN']['SHAKES'])
    if (special_action == 2) or (special_action == 5):
        add(IMG['SHAKES']['EPCIOVL'])
        actor[IMG['SHAKES']['EPCIOVL']].mouse_enabled = False
    remove(IMG['SHAKES']['IDLE'],
           IMG['SHAKES']['IDLE1'],
           IMG['SHAKES']['IDLE2'],
           IMG['SHAKES']['IDLE3'])
    if not sleep_time():
        remove(IMG['SHAKES']['NIGHT'],
               IMG['SHAKES']['BLINZELN1'],
               IMG['SHAKES']['BLINZELN2'])
    else:
        remove(IMG['SHAKES']['DAY'])


def install_hall_popup():
    '''
        setup popup object for hall
    '''
    if this_field_popup != "":
        enable_popup(CNT['HALL']['LIST'], this_field_popup)
    else:
        enable_popup(CNT['HALL']['LIST'])


def hall_list_add_field(pos_x, pos_y, txt, fmt, max_width=0, is_guild=False):
    '''
        add field to hall table
    '''
    tmp_obj = None
    this_field_popup = ""

    if txt == "[K]":
        tmp_obj = Bitmap(
            actor[IMG['IF']['KRIEGER']].content.bitmapData.clone())
        tmp_obj.allow_smoothing = True
        tmp_obj.force_smoothing = True
        tmp_obj.smoothing = True
        tmp_obj.mouse_enabled = True
    elif txt == "[M]":
        tmp_obj = Bitmap(actor[IMG['IF']['MAGIER']].content.bitmapData.clone())
        tmp_obj.allow_smoothing = True
        tmp_obj.force_smoothing = True
        tmp_obj.smoothing = True
        tmp_obj.mouse_enabled = True
    elif txt == "[J]":
        tmp_obj = Bitmap(actor[IMG['IF']['JAEGER']].content.bitmapData.clone())
        tmp_obj.allow_smoothing = True
        tmp_obj.force_smoothing = True
        tmp_obj.smoothing = True
        tmp_obj.mouse_enabled = True
    else:
        tmp_obj = TextField()
        tmp_obj.default_text_format = fmt
        tmp_obj.auto_size = TextFieldAutoSize.LEFT
        tmp_obj.background = False
        tmp_obj.selectable = False
        tmp_obj.embed_fonts = font_embedded
        tmp_obj.anti_alias_type = AntiAliasType.ADVANCED
        tmp_obj.text = txt

        if max_width > 0:
            this_field_popup = trim_too_long(tmp_obj, max_width)

    if is_guild:
        tmp_obj.add_event_listener(MouseEvent.CLICK,
                                   request_player_guild_screen)
    else:
        tmp_obj.add_event_listener(MouseEvent.CLICK, request_player_screen)

    tmp_obj.add_event_listener(MouseEvent.MOUSE_OVER, install_hall_popup)
    if text_dir == "right":
        tmp_obj.x_pos = pos_x - tmp_obj.width
    else:
        tmp_obj.x_pos = pos_x

    tmp_obj.y_pos = pos_y
    tmp_obj.visible = True

    actor[CNT['HALL']['LIST']].addChild(tmp_obj)


def action_handler(event):
    '''
        handle server reply
    '''
    global oldcreststring
    global SAVE

    SAVE = Savegame(LOG)

    data_str = str(event.data)
    is_mine = False
    log_in_after_pixel = False

    if data_str[0] == "+":
        data_str = data_str[1:]
        if guild_blink_ready:
            send_action(ACT['GET']['CHAT_HISTORY'])
            pulse_gilde_on_history = True

    if data_str[0] == "E":
        act = -1 * int(data_str[1, 4])
        par_str = data_str[4:]
    else:
        act = int(data_str[0: 3])
        par_str = data_str[3:]

    par = par_str.split("")
    if on_stage(BTN['FIGHT_SKIP']):
        return

    set_title_bar()
    if act != ERR['SERVER']['DOWN']:
        interval_multiplier_reconnect = 1

    skip_allowed = False

    for case in Switch(act):
        if case(ERR['TOWER']['CLOSED']):
            break

        if case(RESP['TOWER']['SAVE']):
            SAVE.parse(par[0])
            show_tower_screen(par)
            break

        if case(RESP['TOILET']['LOCKED']):
            remove(IMG['TAVERNE']['BARKEEPER']['HINT'])
            remove(BNC['TAVERNE']['CAS'])
            add(BNC['BEEROFFER'])
            enable_popup(CNT['QO']['REWARDGOLD'])
            enable_popup(CNT['QO']['REWARDSILVER'])
            enable_popup(LBL['QO']['REWARDGOLD'])
            enable_popup(LBL['QO']['REWARDSILVER'])
            enable_popup(LBL['QO']['REWARDEXP'])

            current = actor[LBL['QO']['QUESTNAME']]
            current.text = texts[(TXT['TOILET']['HINT'] + 5)]
            current.x_pos = (POS['QO']['BLACK']['SQUARE_X']
                             + REL['QO']['QUESTNAME_X']
                             - current.text_width / 2)

            current = actor[LBL['QO']['QUESTTEXT']]
            current.text = texts[TXT['TOILET']['HINT'] + 6].replace(
                "#", chr(13)
            )

            arabize(LBL['QO']['QUESTTEXT'])
            actor[LBL['QO']['TIME']].text = ""
            actor[LBL['QO']['REWARDEXP']].text = ""
            remove(BTN['BO']['BUY'])
            add(IMG['BO']['PORTRAIT']['TH'])
            break

        if case(RESP['TOILET']['UNLOCKED']):
            play(SND['MAINQUESTS']['UNLOCK'])
        if case(RESP['TOILET']['DROPPED']):
            pass
        if case(RESP['TOILET']['FULL']):
            pass
        if case(RESP['TOILET']['FLUSHED']):
            pass
        if case(ACT['SCREEN']['TOILET']):
            pass
        if case(RESP['TOILET']['TANKFULL']):
            pass
        if case(RESP['TOILET']['DROPTWICE']):
            if act == RESP['TOILET']['DROPPED']:
                play(SND['TOILET']['DROP'])

            SAVE.parse(par[0])
            if len(par) > 1:
                if act == RESP['TOILET']['FLUSHED']:
                    show_toilet(par[1], par[2], par[3], par[4], par[5])
                else:
                    show_toilet(par[1], par[2], par[3], par[4])

            if act == RESP['TOILET']['FULL']:
                error_message(texts[TXT['TOILET']['FULL']])
            elif act == RESP['TOILET']['TANKFULL']:
                error_message(texts[TXT['TOILET']['TANKFULL']])
            elif act == RESP['TOILET']['DROPTWICE']:
                error_message(texts[TXT['TOILET']['DROPTWICE']])
            else:
                error_message("")
            break

        if case(RESP['SCREEN']['WITCH']):
            SAVE.parse(par[0])
            show_witch(
                par[1].split("/"),
                (par[2].split("/")[0] == "1"),
                par[2].split("/")[1])
            break

        if case(ERR['NO_SLOT_FOR_FLUSHING']):
            error_message(texts[TXT['ERR']['NO_SLOT_FOR_FLUSHING']])
            break

        if case(ERR['TOILET']['EMPTY']):
            error_message(texts[TXT['ERR']['TOILET']['EMPTY']])
            break

        if case(ERR['GUILD']['DESCR_TOO_LONG']):
            error_message(texts[TXT['ERR']['GUILD']['DESCR_TOO_LONG']])
            break

        if case(ERR['NO_CHAT_INFO']):
            break

        if case(ERR['NO_CHAT_OVERFLOW']):
            break

        if case(ERR['GUILD']['RANK_WRONG']):
            error_message(texts[TXT['ERROR']['GUILD']['RANK_WRONG']])
            break

        if case(RESP['ALBUM']):
            tmp_byte_array = base64.b64decode(par.join("/"))
            bit_array = list()

            for i in range(len(tmp_byte_array)):
                bit_array.append((tmp_byte_array[i] & 128) / 128)
                bit_array.append((tmp_byte_array[i] & 64) / 64)
                bit_array.append((tmp_byte_array[i] & 32) / 32)
                bit_array.append((tmp_byte_array[i] & 16) / 16)
                bit_array.append((tmp_byte_array[i] & 8) / 8)
                bit_array.append((tmp_byte_array[i] & 4) / 4)
                bit_array.append((tmp_byte_array[i] & 2) / 2)
                bit_array.append(tmp_byte_array[i] & 1)

            album_content = bit_array
            show_screen_album()
            break

        if case(RESP['INVITE']['SUCCESS']):
            show(BNC['INVITE_SUCCESS'])
            hide(BNC['INVITE_INPUTDIALOGUE'])
            break

        if case(ERR['INVITE']['NOT_VALIDATED']):
            pass
        if case(ERR['INVITE']['TOO_MANY']):
            pass
        if case(ERR['INVITE']['EMAIL_REJECTED']):
            txtid = TXT['ERROR']['INVITE']['NOT_VALIDATED']
            error_message(texts[
                txtid - act + ERR['INVITE']['NOT_VALIDATED']
            ])
            break

        if case(RESP['LOGOUT_SUCCESS']):
            break

        if case(ERR['SERVER_DOWN']):
            show_disconnect_screen()
            if (param_reconnect * interval_multiplier_reconnect) < (120000):
                interval_multiplier_reconnect += 0.1
            break

        if case(ERR['JOINED_TOO_RECENTLY']):
            SAVE.parse(par[0])
            error_message(texts[TXT['GUILD']['JOINED_TOO_RECENTLY']].replace(
                "%1", time_str(
                    int(savegame[SG['GUILD']['JOIN_DATE']]) + 60 * 60 * 24,
                    True
                )
            ))
            break

        if case(RESP['ATTACK']['NOT_EXIST']):
            error_message(texts[TXT['ERROR']['PLAYER_NOT_FOUND']])
            break

        if case(ERR['GUILD']['FIGHT_TOO_EXPENSIVE']):
            pass
        if case(ERR['GUILD']['ALREADY_UNDER_ATTACK']):
            pass
        if case(ERR['GUILD']['ATTACK_DELAY']):
            pass
        if case(ERR['GUILD']['ALREADY_ATTACKING']):
            pass
        if case(ERR['GUILD']['ATTACK_STATUS']):
            txtid = TXT['ERROR']['GUILD']['FIGHT_TOO_EXPENSIVE']
            error_message(texts[
                txtid - act + ERR['GUILD']['FIGHT_TOO_EXPENSIVE']
            ])
            break

        if case(RESP['GUILD']['NAMES']):
            last_attack = last_guild_data[GUILD['ATTACK_TIME']]
            if par[0] == "":
                if last_guild_data[GUILD['IS_RAID']] != 0:
                    if texts[TXT['RAID']['TEXT']]:
                        if is_today(last_attack):
                            offset = 13
                        else:
                            offset = 12

                        last_raid = int(last_guild_data[GUILD['RAID_LEVEL']])

                        actor[LBL['GILDE']['ATTACK']].text = texts[
                            TXT['RAID']['TEXT'] + offset
                        ].replace(
                            "%1", texts[TXT['DUNGEON']['NAMES'] + last_raid]
                        ).replace(
                            "%2", time_str(last_attack, True)
                        )
                    else:
                        actor[LBL['GILDE']['ATTACK']].text = ""
                else:
                    actor[LBL['GILDE']['ATTACK']].text = ""
            else:
                if is_today(last_attack):
                    offset = 2
                else:
                    offset = 0

                actor[LBL['GILDE']['ATTACK']].text = texts[
                    TXT['GUILD']['BATTLE_MSG'] + offset
                ].replace(
                    "%1", par[0]
                ).replace(
                    "%2", time_str(last_attack, True)
                )

            if par[1] == "":
                snippet = ''
            else:
                last_defense = last_guild_data[GUILD['DEFENCE']['TIME']]

                if is_today(last_defense):
                    offset = 2
                else:
                    offset = 0

                snippet = texts[
                    TXT['GUILD']['BATTLE']['MSG'] + 1 + offense
                ].replace(
                    "%1", par[1]
                ).replace(
                    "%2", time_str(last_defense, True)
                )

            actor[LBL['GILDE']['DEFENCE']].text = snippet

            if par[2]:
                if last_guild_data[GUILD['IS_RAID']] != 0:
                    if texts[TXT['RAID']['TEXT']]:
                        enable_popup(
                            CNT['GILDE']['ATTACK'],
                            texts[TXT['RAID']['TEXT'] + 14]
                        ).replace("%1", par[2])
                elif (par[0] == "") or (par[2] == ""):
                    enable_popup(CNT['GILDE']['ATTACK'])
                elif texts[TXT['GUILD']['ATTACK']['PLAYER']]:
                    enable_popup(
                        CNT['GILDE']['ATTACK'],
                        texts[TXT['GUILD']['ATTACK']['PLAYER']].replace(
                            "%1", par[2]
                        )
                    )
                else:
                    enable_popup(CNT['GILDE']['ATTACK'], par[2])
            else:
                enable_popup(CNT['GILDE']['ATTACK'])

            guild_attack_time = last_guild_data[GUILD['ATTACK_TIME']]
            guild_defense_time = last_guild_data[GUILD['DEFENCE_TIME']]
            guild_attacked = par[0]
            guild_attacking = par[1]
            break

        if case(ERR['SESSION_ID_EXPIRED']):
            LOG.warning("Achtung, session_id ist abgelaufen.")
            session_id = ""
            fight_flush_mode = False
            show_login_screen()
            break

        if case(ERR['MSG']['LEVEL_TOO_LOW']):
            if texts[TXT['ERROR']['MSG']['LEVEL_TOO_LOW']]:
                error_message(texts[TXT['ERROR']['MSG']['LEVEL_TOO_LOW']])
            else:
                error_message(''.join([
                    "Error: You need to reach at least level 10 to ",
                    "send messages."
                ]))
            break

        if case(ERR['MSG']['NOT_VALIDATED']):
            if texts[TXT['ERROR']['MSG']['NOT_VALIDATED']]:
                error_message(texts[TXT['ERROR']['MSG']['NOT_VALIDATED']])
            else:
                error_message(' '.join("Error: Your email address has to be",
                                       "validated in order to send messages."))
            break

        if case(ERR['INVENTORY_FULL']):
            error_message(texts[TXT['ERROR']['INVENTORY_FULL']])
            break

        if case(ERR['INVENTORY_FULL_ADV']):
            if texts[TXT['ERROR']['INVENTORY_FULL_ADV']]:
                error_message(texts[TXT['ERROR']['INVENTORY_FULL_ADV']])
            else:
                error_message(texts[TXT['ERROR']['INVENTORY_FULL']])

            fade_out(CNT['QUEST_SLOT'], 20, 0.04, 0.3)
            force_adventure = True
            break

        if case(ERR['PLACE_BET']):
            break

        if case(RESP['BET_WON']):
            SAVE.parse(par[0])
            show_bet_result(True)
            break

        if case(RESP['BET_LOST']):
            SAVE.parse(par[0])
            show_bet_result(False)
            break

        if case(ERR['ACCOUNTS_PER_IP']):
            error_message(texts[TXT['ERRROR']['ACCOUNTS_PER_IP']])
            break

        if case(ERR['TOO_SOON']):
            break

        if case(ERR['LOCKED_PAYMENT']):
            error_message(
                texts[TXT['ERRROR']['LOCKED_PAYMENT']].replace(
                    "%supportemail%", param_support_email
                ).replace(
                    "%gamestaffemail%", param_gamestaff_email
                )
            )
            break

        if case(ERR['LOCKED_ADMIN']):
            if par[2]:
                if texts[TXT['LOCK_REASON'] + int(par[1]) - 1]:
                    error_message(
                        texts[TXT['LOCK_REASON'] + int(par[1]) - 1].replace(
                            "%1", str(1 + int(par[2] / (60 * 60 * 24)))
                        )
                    )
                else:
                    error_message(texts[TXT['ERRROR']['LOCKED_ADMIN']])
            else:
                error_message(texts[TXT['ERRROR']['LOCKED_ADMIN']])
            break

        if case(RESP['REQUEST']['GUILD_QUIET']):
            destroy_guild_btn_timer = True
            if on_stage(LBL['GILDE']['CHAT_CAPTION']):
                send_action(ACT['SCREEN']['GILDEN'])
            break

        if case(RESP['REQUEST']['GUILD']):
            destroy_guild_btn_timer = True
            if on_stage(LBL['GILDE']['CHAT_CAPTION']):
                send_action(ACT['SCREEN']['GILDEN'])
            else:
                pulse_gilde = True
            break

        if case(ERR['GUILD']['DONATE_FRA']):
            error_message(texts[TXT['ERROR']['GUILD']['DONATE_FRA']])
            break

        if case(ERR['GUILD']['DONATE_NEG']):
            error_message(texts[TXT['ERROR']['GUILD']['DONATE_NEG']])
            break

        if case(ERR['MAIL']['EXISTS']):
            error_message(texts[TXT['ERROR']['MAIL_EXISTS']])
            break

        if case(RESP['VALIDATE_OK']):
            if par[0]:
                param_cid = par[0]
                LOG.debug("cid set by server: " + param_cid)
            show_email_nag_screen(1)
            break

        if case(ERR['VALIDATE']):
            show_email_nag_screen(2)
            break

        if case(RESP['PASSWORD_SENT']):
            show_login_screen()
            break

        if case(ERR['REQUEST_PW']):
            error_message(texts[TXT['ERROR']['REQUEST_PW']])
            break

        if case(RESP['TRANS_COUNT']):
            sep = '.'
            if lang_code:
                sep = ','

            permanent_link = (''.join([
                "http://www.payment.playa-games.com/legal/wiretransfer_",
                lang_code,
                ".php?amount=",
                str(int((tmpAmount / 100))),
                sep,
                str(tmpAmount % 100),
                "&use=",
                par[0]
            ]))
            navigate_to_url(URLRequest(permanent_link), "_blank")
            break

        if case(RESP['DEALER']['AKTION']):
            pass
        if case(RESP['DEALER']['SPONSOR']):
            pass
        if case(RESP['EMAIL_RESENT']):
            actor[LBL['EMAIL_RESEND']].htmlText = texts[TXT['EMAIL']['RESENT']]
            arabize(LBL['EMAIL_RESEND'])
            actor[LBL['OPTION']['FIELD1']].htmlText = texts[
                TXT['EMAIL']['RESENT']
            ]
            arabize(LBL['OPTION']['FIELD1'])
            remove(BTN['OPTION']['DOCHANGE'])
            break

        if case(RESP['CHAT_HISTORY']):
            if par[0] != last_chat_hist:
                last_chat_hist = par[0]
                interval_multiplier_chat = 1
            elif interval_multiplier_chat < 5:
                interval_multiplier_chat = (interval_multiplier_chat + 0.1)
            elif interval_multiplier_chat < 30:
                interval_multiplier_chat = (interval_multiplier_chat + 1)

            if par[0] == "":
                tmp_array = []
            else:
                tmp_array = par[0].split("/")

            first_chat_fill = False
            if last_chat_index == 0:
                first_chat_fill = True

                for i in range(40):
                    with actor[(LBL['GILDE']['CHAT'] + i)]:
                        default_text_format = font_format_chat
                        text = ""

            if len(tmp_array) > 0:
                for i in range(len(tmp_array)-1, 0, -1):
                    if not par[3]:
                        if ((last_chat_index != 0)
                                and (decode_chat(tmp_array[i],
                                                 False, True) == "1")):
                            remove(BNC['GILDE']['CHAT'])

                        chat_line(decode_chat(tmp_array[i]),
                                  False,
                                  get_hl_index(tmp_array[i]))

                        if (((tmp_array[i].find("§") != -1)
                             or (not shared_obj.data.noPulseOnSysMsg))
                                and pulse_gilde_on_history):
                            pulse_gilde = True

                        if last_chat_index != 0:
                            for j in range(len(offline_guild_members)):
                                tmp_str = offline_guild_members[j].lower()
                                tmp_str += ":§"
                                if tmp_array[i].lower().find(tmp_str) != -1:
                                    if on_stage(INP['GILDE_CHAT']):
                                        send_action(ACT['SCREEN']['GILDEN'])
                                    break
                    else:
                        if par[3].split("/")[i] > last_chat_index:
                            if not first_chat_fill and chat_sound:
                                play(SND['ERROR'])

                            last_chat_index = par[3].split("/")[i]
                            if ((not last_chat_index == 0)
                                    and (decode_chat(
                                        tmp_array[i], False, True) == "1")):
                                remove(BNC['GILDE']['CHAT'])

                            chat_line(
                                decode_chat(tmp_array[i]),
                                False,
                                get_hl_index(tmp_array[i])
                            )

                            if (((tmp_array[i].find("§") != -1)
                                 or (not shared_obj.data.noPulseOnSysMsg))
                                    and (pulse_gilde_on_history)):
                                pulse_gilde = True

                            for j in range(len(offline_guild_members)):
                                tmp_str = offline_guild_members[j].lower()
                                tmp_str += ":§"
                                if tmp_array[i].lower().find(tmp_str) != -1:
                                    if on_stage(INP['GILDE_CHAT']):
                                        send_action(ACT['SCREEN']['GILDEN'])
                                    break

                pulse_gilde_on_history = False

            if (par[1]) and (not par[3]):
                last_chat_index = int(par[1])

            if par[2]:
                tmp_array = par[2].split("/")
            else:
                tmp_array = []

            if len(tmp_array) > 0:
                if chat_sound:
                    play(SND['ERROR'])

                for i in range(len(tmp_array)-1, 0, -1):
                    pulse_gilde = True
                    external_whisperer = tmp_array[i][6:]
                    external_whisperer = external_whisperer[
                        0: external_whisperer.find(":§")
                    ]
                    chat_line(decode_chat(tmp_array[i]),
                              False,
                              get_hl_index(tmp_array[i]),
                              True)

                    add_suggest_names(external_whisperer)

                    if last_chat_index != 0:
                        for j in range(len(offline_guild_members)):
                            tmp_str = offline_guild_members[j].lower()
                            tmp_str += ":§"
                            if tmp_array[i].lower().find(tmp_str) != -1:
                                if on_stage(INP['GILDE_CHAT']):
                                    send_action(ACT['SCREEN']['GILDEN'])
                                break

            guild_blink_ready = True

            if ((new_crest_suggested != "")
                    and (not first_chat_fill)
                    and (on_stage(INP['GILDE_CHAT']))):
                clickchat_line(new_crest_suggested)

            new_crest_suggested = ""
            break

        if case(RESP['WHISPER_SUCCESS']):
            add_suggest_names(last_whisper_target)
            chat_line(decode_chat(par[0]), False, get_hl_index(par[0]), True)
            break

        if case(ERR['GUILD']['NAME']['REJECTED']):
            error_message(texts[TXT['ERROR']['GUILD']['NAME_REJECTED']])
            break

        if case(ERR['GUILD']['NAME']['LENGTH']):
            error_message(texts[TXT['ERROR']['GUILD']['NAME_LENGTH']])
            break

        if case(ERR['GUILD']['NAME']['CHARACTERS']):
            error_message(texts[TXT['ERROR']['GUILD']['NAME']['CHARACTERS']])
            break

        if case(ERR['GUILD']['EMAIL']['VALIDATE']):
            error_message(texts[TXT['ERROR']['GUILD']['EMAIL_VALIDATE']])
            break

        if case(ERR['GUILD']['MUSH_FREE']):
            error_message(texts[TXT['ERROR']['GUILD']['MUSH_FREE']])
            break

        if case(RESP['CHAT_LINE']):
            if decode_chat(par[0], False, True) == "1":
                remove(BNC['GILDE']['CHAT'])

            chat_line(decode_chat(par[0]), False, get_hl_index(par[0]))

            if not on_stage(INP['GILDE_CHAT']):
                pulse_gilde = True
            break

        if case(RESP['GUILD']['DONATE_SUCCESS']):
            SAVE.parse(par[0])
            send_action(ACT['SCREEN']['GILDEN'])
            break

        if case(RESP['NO_LOGIN']):
            request_logout(True)
            show_login_screen()
            break

        if case(RESP['DELETE_ACCOUNT']['OK']):
            request_logout()
            break

        if case(RESP['CHANGE']['PASS_OK']):
            shared_obj.data.password = option_new_data
            shared_obj.flush()
            actor[INP['LOGIN_PASSWORD']].getChildAt(1).text = option_new_data
            show_option_screen()
            error_message(texts[TXT['PASSWORD_CHANGED']])
            break

        if case(RESP['CHANGE']['NAME_OK']):
            shared_obj.data.userName = option_new_data
            shared_obj.flush()
            actor[INP['NAME']].getChildAt(1).text = option_new_data
            SAVE.parse(par[0])
            show_option_screen()
            error_message(texts[TXT['NAME_CHANGED']])
            break

        if case(RESP['CHANGE']['MAIL_OK']):
            show_option_screen()
            error_message(texts[TXT['EMAIL']['CHANGED']])
            break

        if case(RESP['CHANGE']['FACE_OK']):
            SAVE.parse(par[0])

        if case(ACT['SCREEN']['OPTIONEN']):
            show_option_screen()
            break

        if case(RESP['DEMO_SCREEN']):
            show_demo_screen()
            break

        if case(RESP['PLAYER_SCREEN']):
            show_demo_screen(
                ("0/" + par[0]).split("/"),
                sel_name, par[2], resolve_breaks(par[1])
            )
            break

        if case(RESP['PLAYER_DESC']['SUCCESS']):
            player_desc = actor[INP['CHARDESC']].getChildAt(0).text
            break

        if case(RESP['GUILD']['CHANGE_DESC']['SUCCESS']):
            break

        if case(RESP['GUILD_DATA']):
            if par[1] == savegame[SG['GUILD']['INDEX']]:
                gilde = par[0]

            last_chat_index = 0
            send_action(ACT['GET_CHAT_HISTORY'])
            break

        if case(RESP['MAINQUEST']):
            hide(BNC['IF']['STATS'])
            SAVE.parse(par[10])
            pulse_char = False
        if case(RESP['QUEST']['DONE']):
            pass
        if case(RESP['QUEST']['DONE_PIXEL']):
            pass
        if case(RESP['QUEST']['DONE_PIXEL_2']):
            fight_lock = True
            post_fight_mode = False
            show_fight_screen(
                par[0].split("/"),
                par[1].split("/"),
                (par[6] == "1"),
                par[2].split("/"),
                (par[5] == "2"),
                (par[3] + "/" + par[4]).split("/"),
                int(par[7]),
                int(par[8]),
                (par[5] == "3"),
                False,
                int(par[9])
            )
            break

        if case(RESP['GUILD_FIGHT']):
            tower_fight_mode = False
            alternate_char_opp_img = True
            fight_lock = True
            winners = list()
            last_round_fighter_name = ""
            fights = par_str.split("§")
            guild_fight_count = int((len(fights) - 1) / 2)
            skip_guild_fights = 0
            next_fight_timer.start()
            break

        if case(RESP['TOWER_FIGHT']):
            tower_fight_mode = True
            alternate_char_opp_img = True
            fight_lock = True
            winners = list()
            last_round_fighter_name = ""
            fights = par_str.split("§")
            SAVE.parse(fights.pop(), True, True)
            guild_fight_count = int(((len(fights) - 1) / 2))
            skip_guild_fights = 0
            next_fight_timer.start()
            break

        if case(RESP['QUEST']['SKIP_ALLOWED_START']):
            skip_allowed = True
        if case(RESP['QUEST']['START']):
            SAVE.parse(par[0])
            show_quest_screen()
            break

        if case(RESP['QUEST']['SKIP_ALLOWED']):
            skip_allowed = True
        if case(ACT['SCREEN']['TAVERNE']):
            pass
        if case(RESP['QUEST']['STOP']):
            SAVE.parse(par[0])
            if par[1]:
                special_action = par[1]
            else:
                if act != RESP['QUEST']['STOP']:
                    special_action = 0
                else:
                    LOG.info(
                        "Quest cancelled, preserving special action flag!")
            LOG.info("Tavern says special action is " + special_action)
            if par[2] is not None:
                prevent_tv = (par[2] == 1)

            show_taverne_screen()
            break

        if case(ACT['SCREEN']['GILDE_GRUENDEN']):
            show_screen_gilde_gruenden()
            break

        if case(RESP['GUILD']['FOUND_SUCCESS']):
            actor[LBL['IF']['GOLD']].text = str(
                (int(actor[LBL['IF']['GOLD']].text) - 10)
            )
            actor[LBL['IF']['GOLD']].x = (
                actor[IMG['IF']['GOLD']].x
                - actor[LBL['IF']['GOLD']].text_width - 10
            )
        if case(RESP['GUILD']['RENAME_SUCCESS']):
            pass
        if case(RESP['GUILD']['IMPROVE_SUCCESS']):
            pass
        if case(RESP['GUILD']['OFFICER_SUCCESS']):
            pass
        if case(RESP['GUILD']['EXPEL_SUCCESS']):
            pass
        if case(RESP['GUILD']['INVITE_SUCCESS']):
            pass
        if case(RESP['GUILD']['MASTER_SUCCESS']):
            pass
        if case(RESP['GUILD']['JOIN_SUCCESS']):
            send_action(ACT['SCREEN']['GILDEN'])
            break

        if case(RESP['GUILD']['DELETE_SUCCESS']):
            gilde = ""
            my_own_rank = -1
            my_own_attack_target = -1
            my_own_guild_money = -1
            show_city_screen()
            break

        if case(RESP['GUILD']['COMMENCE_ATTACK_OK']):
            pass
        if case(RESP['GUILD']['JOIN_ATTACK_OK']):
            pass
        if case(RESP['GUILD']['JOIN_DEFENSE_OK']):
            SAVE.parse(par[0])
            send_action(ACT['SCREEN']['GILDEN'])
            break

        if case(ACT['SCREEN']['GILDEN']):
            savegame[SG['GUILD']['INDEX']] = par[0].split("/")[0]
            gilde = par[3]
            is_mine = True
            interval_multiplier_chat = 1

        if case(RESP['OTHER_GUILD']):
            destroy_guild_btn_timer = True

            if (not on_stage(BNC['GILDE']['CREST'])
                    or (act == RESP['OTHER_GUILD'])
                    or (last_guild_crest_id != par[0].split("/")[0])
                    or (is_mine and (oldcreststring == old_crest_str()))):
                if par[1].find("§") != -1:
                    set_crest_str(par[1].split("§")[0])
                    par[1] = par[1][(par[1].find("§") + 1):]
                else:
                    last_guild_data = par[0].split("/")
                    set_default_crest()

                oldcreststring = old_crest_str()
            else:
                if par[1].find("§") != -1:
                    par[1] = par[1][(par[1].find("§") + 1):]

            if last_guild_crest_id != par[0].split("/")[0]:
                oldcreststring = old_crest_str()

            if (not is_mine) and par[1].find("///") > -1:
                par[1] = par[1] .split("///")[1]

            if not par[6]:
                par[6] = 0

            show_screen_gilden(
                par[0].split("/"),
                tmp_str,
                par[2].split("/"),
                par[3],
                is_mine,
                int(par[5]),
                int(par[4]),
                par[6]
            )
            break

        if case(ACT['SCREEN']['STALL']):
            stundenlohn = int(par[0])
            show_stall_screen()
            break

        if case(ERR['ATTACK']['AGAIN']):
            error_message(texts[TXT['ERROR']['ATTACK']['AGAIN']])
            break

        if case(ACT['SCREEN']['ARENA']):
            show_arena_screen(par[0], par[2], par[1])
            break

        if case(ERR['INBOX_FULL']):
            error_message(texts[TXT['ERROR']['INBOX_FULL']])
            break

        if case(ERR['RECIPIENT_NOT_FOUND']):
            error_message(texts[TXT['ERROR']['RECIPIENT_NOT_FOUND']])
            break

        if case(ERR['RECIPIENT_SELF']):
            error_message(texts[TXT['ERROR']['RECIPIENT_SELF']])
            break

        if case(RESP['MESSAGE_SENT']):
            add_suggest_names(last_message_target)
            remove(BNC['POST']['WRITE'])
            remove(BNC['POST']['READ'])
            add(BNC['POST']['LIST'])
            break

        if case(RESP['READ_MESSAGE']):
            remove_all()
            add(BNC['SCREEN']['POST'])
            if tageszeit() != 0:
                remove(BNC['POST']['NIGHT'])

            if tageszeit() != 1:
                remove(BNC['POST']['DAWN'])

            remove(BNC['POST']['LIST'])
            add(BNC['POST']['READ'])

            if (post_sel + post_scroll - 1) == 1:
                remove(BTN['POST']['READ_PREV'])

            if (post_sel + post_scroll - 1) == savegame[SG['MSG']['COUNT']]:
                remove(BTN['POST']['READ_NEXT'])

            if int(par[4]) > 0:
                invitegilden_id = int(par[4])
                add(BTN['POST']['ACCEPT'])

            current = actor[INP['POST']['ADDRESS']].getChildAt(1)
            current.type = TextFieldType.DYNAMIC
            current.text = (' '.join(
                texts[TXT['POST']['FROM']],
                par[0],
                texts[TXT['POST']['TIME']],
                time_str(par[2])
            ))

            current = actor[INP['POST']['SUBJECT']].getChildAt(1)
            current.type = TextFieldType.DYNAMIC
            current.reply_address = par[0]
            for case in switch(par[1]):
                if case("1  ", "2  ", "3  ", "4  ", "5  ",
                        "6  ", "7  ", "8  ", "9  "):
                    par[1] = "Moo!"
                    par[3] = "Holy Cow!"
                    break

                if case("1"):
                    par[1] = texts[TXT['SUBJECT']['GUILD_DELETED']]
                    par[3] = texts[TXT['BODY']['GUILD_DELETED']].replace(
                        "%1", par[0]
                    ).replace(
                        "%2", par[3]
                    )
                    break

                if case("2"):
                    par[1] = texts[
                        TXT['SUBJECT']['GUILD']['DELETED_BY_ADMIN']
                    ]
                    par[3] = texts[
                        TXT['BODY']['GUILD']['DELETED_BY_ADMIN']
                    ].replace("%1", par[0]).replace("%2", par[3])
                    break

                if case("3"):
                    par[1] = texts[TXT['SUBJECT']['GUILD_EXPELLED']]
                    par[3] = texts[
                        TXT['BODY']['GUILD_EXPELLED']
                    ].replace(
                        "%1", par[0]
                    ).replace(
                        "%2", par[3]
                    )
                    break

                if case("4"):
                    par[1] = texts[
                        TXT['SUBJECT']['GUILD_EXPELLED_BY_ADMIN']
                    ]
                    par[3] = texts[
                        TXT['BODY']['GUILD_EXPELLED_BY_ADMIN']
                    ].replace(
                        "%1", par[0]
                    ).replace(
                        "%2", par[3]
                    )
                    break

                if case("5"):
                    par[1] = texts[TXT['SUBJECT']['GUILD_INVITE']]
                    par[3] = texts[TXT['BODY']['GUILD_INVITE']].replace(
                        "%1", par[0]
                    ).replace(
                        "%2", par[3]
                    )
                    break

                if case("6", "7"):
                    par[1] = texts[TXT['SUBJECT']['PVP']].replace(
                        "%1", par[0]
                    )
                    tmp_battle_info = par[3]
                    tmp_fighter_array = tmp_battle_info.split(
                        "#"
                    )[0].split("/")
                    ich_anfg = tmp_fighter_array[0]
                    er_anfg = tmp_fighter_array[6]

                    tmp_fight_array = tmp_battle_info.split(
                        "#"
                    )[1].split("/")
                    ich_ende = tmp_fight_array[len(tmp_fight_array) - 7]
                    er_ende = tmp_fight_array[len(tmp_fight_array) - 4]
                    runden_zahl = int(len(tmp_fight_array) / 6)
                    tmp_honor = abs(tmp_battle_info.split("#")[7])
                    tmp_gold = abs(int(
                        tmp_battle_info.split("#")[8] / 100))
                    tmp_silver = abs(
                        int(tmp_battle_info.split("#")[8] % 100)
                    )

                    outcome = TXT['DU_VERLOREN']
                    if ich_ende > er_ende:
                        outcome = TXT['DU_GEWONNEN']
                    plural = texts[TXT['ROUNDS_PLURAL']]
                    if runden_zahl == 1:
                        plural = ""
                    wonlost = TXT['DU']['WAS_VERLOREN']
                    if ich_ende > er_ende:
                        wonlost = TXT['DU']['WAS_GEWONNEN']

                    par[3] = texts[TXT['BODY']['PVP']].replace(
                        "%1", par[0]
                    ).replace(
                        "%2", par[3]
                    ).replace(
                        "%3", str(ich_anfg)
                    ).replace(
                        "%4", str(er_anfg)
                    ).replace(
                        "%5", str(ich_ende)
                    ).replace(
                        "%6", str(er_ende)
                    ).replace(
                        "%7", str(runden_zahl)
                    ).replace(
                        "%8", texts[outcome]
                    ).replace(
                        "%9", plural
                    ).replace(
                        "%10", str(tmp_honor)
                    ).replace(
                        "%11", str(tmp_gold)
                    ).replace(
                        "%12", str(tmp_silver)
                    ).replace(
                        "%13", texts[wonlost]
                    ).replace(
                        "#", chr(13)
                    )
                    add(BTN['POST']['VIEWFIGHT'])
                    break

                if case("8"):
                    if texts[TXT['INV']['ACC_TITLE']] != "":
                        par[1] = texts[TXT['INV']['ACC_TITLE']]
                        par[3] = texts[TXT['INV']['ACC_TEXT']].replace(
                            "%1", par[0]
                        )
                    else:
                        par[1] = "FRIEND_LINK_ACCEPTED"
                        par[3] = (''.join([
                            "You are seeing this message in",
                            "english because it has not been translated",
                            "for your location yet. ",
                            par[0],
                            " has accepted your invitation to the game."
                            "Please wait for ",
                            par[0],
                            " to verify"
                            "email address in order to get your bonus."
                        ]))
                    add(BTN['POST']['REPLY'])
                    break

                if case("9"):
                    if texts[TXT['INV']['VAL_TITLE']] != "":
                        par[1] = texts[TXT['INV']['VAL_TITLE']]
                        par[3] = texts[TXT['INV']['VAL_TEXT']].replace(
                            "%1", par[0]
                        )
                    else:
                        par[1] = "FRIEND_EMAIL_VERIFIED"
                        par[3] = ''.join([
                            par[0],
                            " has verified his/her email address."
                        ])
                    add(BTN['POST']['REPLY'])
                    break

                if case():
                    add(BTN['POST']['REPLY'])

            current.reply_subject = par[1]
            current.text = par[1].replace("%u20AC", "€")

            post_read_text = par[3]
            if texts[TXT['ALERT_WORDS']]:
                alert_words = texts[TXT['ALERT_WORDS']].split(" ")

                for i in range(len(alert_words)):
                    if (post_read_text.lower().find(
                            alert_words[i].lower()) != -1):
                        post_read_text = texts[TXT['ALERT_TEXT']].replace(
                            "%1", post_read_text
                        )
                        break

            current = (actor[INP['POST_TEXT']].getChildAt(1))
            current.type = TextFieldType.DYNAMIC
            current.text = swap_words(post_read_text).replace(
                "#", chr(13)
            ).replace(
                "%u20AC", "€"
            )

            forward_text = post_read_text
            break

        if case(ACT['SCREEN']['POST']):
            show_post_screen(par)
            break

        if case(ACT['SCREEN']['PILZDEALER']):
            if par[0]:
                dealer_aktion = int(par[0])
            else:
                dealer_aktion = 0
            pulse_dealer = False
            show_dealer_screen()
            break

        if case(ACT['SCREEN']['WELTKARTE']):
            SAVE.parse(par[0])
            show_main_quests_screen(par[1].split("/"))
            break

        if case(ACT['SCREEN']['EHRENHALLE']):
            last_guild_shown = ""

        if case(RESP['SCREEN']['GILDENHALLE']):
            guild_hall_mode = (act == RESP['SCREEN']['GILDENHALLE'])
            if guild_hall_mode:
                hide(
                    LBL['HALL'][['GOTO_SPIELER_HL']],
                    LBL['HALL']['GOTO_GILDEN']
                )
                show(
                    LBL['HALL']['GOTO_SPIELER'],
                    LBL['HALL']['GOTO_GILDEN_HL']
                )
            else:
                last_hall_members = list()
                last_hall_members.append("")
                show(LBL['HALL'][['GOTO_SPIELER_HL']],
                     LBL['HALL']['GOTO_GILDEN'])
                hide(LBL['HALL']['GOTO_SPIELER'],
                     LBL['HALL']['GOTO_GILDEN_HL'])

            if par[1]:
                ruhmes_halle_such_string = par[1]
                ruhmes_halle_such_name = True

            if not on_stage(IMG['SCR']['HALLE']['BG']):
                show_hall_screen()

            current = actor[CNT['HALL_LIST']]
            while current.numChildren > 0:
                current.removeChildAt(0)

            if text_dir == "right":
                hall_list_add_field(
                    col_idx['6_X'] + 40,
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[TXT['HALL']['LIST']['COLUMN']['1']],
                    FontFormatHallListHeading
                )

                modetxt = TXT['HALL']['LIST']['COLUMN']['2']
                if guild_hall_mode:
                    modetxt = TXT['HALL']['LIST']['COLUMN']['3']
                hall_list_add_field(
                    col_idx['6_X'] - 10,
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[modetxt],
                    FontFormatHallListHeading
                )
                hall_list_add_field(
                    col_idx['2_X'] - 10,
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[TXT['HALL']['LIST']['COLUMN']['5']],
                    FontFormatHallListHeading
                )

                modetxt = TXT['GUILDHALL']['LEADER']
                if guild_hall_mode:
                    modetxt = TXT['HALL']['LIST']['COLUMN']['3']
                hall_list_add_field(
                    col_idx['4_X'] + 20,
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[modetxt],
                    FontFormatHallListHeading
                )

                modetxt = TXT['GUILDHALL']['MEMBERS']
                if guild_hall_mode:
                    modetxt = TXT['HALL']['LIST']['COLUMN']['4']
                hall_list_add_field(
                    col_idx['3_X'] + 25,
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[modetxt],
                    FontFormatHallListHeading
                )
            else:
                hall_list_add_field(
                    col_idx['1_X'],
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[TXT['HALL']['LIST']['COLUMN']['1']],
                    FontFormatHallListHeading
                )

                modetxt = TXT['HALL']['LIST']['COLUMN']['2']
                if guild_hall_mode:
                    modetxt = TXT['HALL']['LIST']['COLUMN']['3']
                hall_list_add_field(
                    col_idx['2_X'],
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[modetxt],
                    FontFormatHallListHeading
                )

                hall_list_add_field(
                    col_idx['6_X'],
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[TXT['HALL']['LIST']['COLUMN']['5']],
                    FontFormatHallListHeading
                )

                modetxt = TXT['GUILDHALL']['LEADER']
                if guild_hall_mode:
                    modetxt = TXT['HALL']['LIST']['COLUMN']['3']
                hall_list_add_field(
                    col_idx['4_X'],
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[modetxt],
                    FontFormatHallListHeading
                )

                modetxt = TXT['GUILDHALL']['MEMBERS']
                if guild_hall_mode:
                    modetxt = TXT['HALL']['LIST']['COLUMN']['4']
                hall_list_add_field(
                    col_idx['5_X'],
                    REL['HALL']['LIST']['LINES']['Y'],
                    texts[modetxt],
                    FontFormatHallListHeading
                )

            hall_list_name = list()
            hall_list_guild = list()
            tmp_array = par[0].split("/")
            line = 1

            for i in range(len(tmp_array) - 1):
                tmp_str = ''
                if tmp_array[i] < 0:
                    tmp_str += '-'
                tmp_str += ruhmes_halle_such_string.lower()

                tmpidx = i
                if ruhmes_halle_such_name:
                    if guild_hall_mode:
                        tmpidx += 2
                    else:
                        tmpidx += 1

                if ((not guild_hall_mode)
                        and (not ruhmes_halle_such_name)
                        and (tmp_str == tmp_array[tmpidx].lower())):
                    tmp_fmt = FontFormatHallListHighLight
                elif guild_hall_mode and (int(tmp_array[i + 3]) < 0):
                    tmp_fmt = FontFormatGuildHallNoAttack
                elif ((not guild_hall_mode)
                      and (not lastAttacked.find(
                          tmp_array[i + 1].lower()) == -1)):
                    tmp_fmt = FontFormatGuildHallNoAttack
                else:
                    tmp_fmt = FontFormatHallListText

                last_hall_members.append(tmp_array[i + 1])
                arrow_hall_mode = True

                col_idx = col_idx
                lines_idx = REL['HALL']['LIST']['LINES']['Y']
                lines_idx += line * REL['HALL']['LIST']['LINE']['Y']

                if text_dir == "right":
                    hall_list_add_field(
                        col_idx['6_X'] + 40,
                        lines_idx,
                        abs(tmp_array[i]),
                        tmp_fmt,
                        0,
                        guild_hall_mode
                    )

                    if guild_hall_mode:
                        modetxt = ''
                    elif tmp_array[i] < 0:
                        modetxt = '[J]'
                    elif tmp_array[i + 3] < 0:
                        modetxt = '[M]'
                    else:
                        modetxt = "[K]"

                    hall_list_add_field(
                        col_idx['6_X'] - 10,
                        lines_idx + 5,
                        modetxt,
                        tmp_fmt
                    )
                    i += 1

                    hall_list_name[line] = tmp_array[i]
                    i += 1

                    tmpidx = col_idx['6_X'] - 30
                    tmpidx2 = col_idx['5_X'] - col_idx['4_X'] - 10
                    if guild_hall_mode:
                        tmpidx = col_idx['4_X'] + 20
                        tmpidx2 = (col_idx['4_X'] - col_idx['3_X'] - 10)
                    hall_list_add_field(
                        tmpidx,
                        lines_idx,
                        tmp_array[i],
                        tmp_fmt,
                        tmpidx2
                    )

                    hall_list_guild[line] = tmp_array[i]
                    i += 1

                    tmpidx = col_idx['4_X'] - 20
                    tmpidx2 = col_idx['5_X'] - col_idx['4_X'] - 10
                    if guild_hall_mode:
                        tmpidx = col_idx['6_X'] + 10
                        tmpidx2 = (col_idx['4_X'] - col_idx['2_X'] - 10)
                    tmp_str = tmp_array[i - 1]
                    if tmp_array[i] == "":
                        tmp_str = texts[TXT['NOGUILD']]
                    hall_list_add_field(
                        tmpidx,
                        lines_idx,
                        tmp_str,
                        tmp_fmt,
                        tmpidx2,
                        True
                    )
                    i += 1

                    hall_list_add_field(
                        col_idx['3_X'] + 25,
                        lines_idx,
                        abs(tmp_array[i]),
                        tmp_fmt,
                        0,
                        guild_hall_mode
                    )

                    tmpidx = tmp_array[i]
                    if tmp_array[i] == 1:
                        tmpidx = 0
                    hall_list_add_field(
                        col_idx['2_X'] - 10,
                        lines_idx,
                        tmpidx,
                        tmp_fmt,
                        0,
                        guild_hall_mode
                    )
                else:
                    hall_list_add_field(
                        col_idx['1_X'],
                        lines_idx,
                        abs(tmp_array[i]),
                        tmp_fmt,
                        0,
                        guild_hall_mode
                    )

                    if guild_hall_mode:
                        modetxt = ''
                    elif tmp_array[i] < 0:
                        modetxt = '[J]'
                    elif tmp_array[i + 3] < 0:
                        modetxt = '[M]'
                    else:
                        modetxt = "[K]"

                    hall_list_add_field(
                        col_idx['2_X'],
                        lines_idx + 5,
                        modetxt,
                        tmp_fmt
                    )
                    i += 1

                    hall_list_name[line] = tmp_array[i]
                    i += 1

                    tmpidx = col_idx['3_X']
                    tmpidx2 = col_idx['4_X'] - col_idx['3_X'] - 10
                    if guild_hall_mode:
                        tmpidx = col_idx['4_X']
                        tmpidx2 = (col_idx['5_X'] - col_idx['4_X'] - 10)
                    hall_list_add_field(
                        tmpidx,
                        lines_idx,
                        tmp_array[i],
                        tmp_fmt,
                        tmpidx2
                    )

                    hall_list_guild[line] = tmp_array[i]
                    i += 1

                    tmpidx = col_idx['4_X']
                    tmpidx2 = col_idx['5_X'] - col_idx['4_X'] - 10
                    if guild_hall_mode:
                        tmpidx = col_idx['2_X']
                        tmpidx2 = (col_idx['4_X'] - col_idx['2_X'] - 10)
                    tmp_str = tmp_array[i - 1]
                    if tmp_array[i] == "":
                        tmp_str = texts[TXT['NOGUILD']]
                    hall_list_add_field(
                        tmpidx,
                        lines_idx,
                        tmp_str,
                        tmp_fmt,
                        tmpidx2,
                        True
                    )
                    i += 1

                    hall_list_add_field(
                        col_idx['5_X'],
                        lines_idx,
                        abs(tmp_array[i]),
                        tmp_fmt,
                        0,
                        guild_hall_mode
                    )

                    tmpidx = tmp_array[i]
                    if tmp_array[i] == 1:
                        tmpidx = 0
                    hall_list_add_field(
                        col_idx['6_X'],
                        lines_idx,
                        tmpidx,
                        tmp_fmt,
                        0,
                        guild_hall_mode
                    )

                line += 1
            break

        if case(RESP['ARBEIT']['START'], RESP['ARBEIT']['STOP']):
            SAVE.parse(par[0])
            show_work_screen()
            break

        if case(RESP['ARBEIT']['ERLEDIGT']):
            SAVE.parse(par[0])
            verdientes_geld = par[1]
            show_work_success_screen()
            break

        if case(ACT['SCREEN']['ARBEITEN']):
            stundenlohn = int(par[0])
            show_work_screen()
            break

        if case(RESP['SAVEGAME']['STAY_ERROR']):
            error_message(texts[TXT['ERROR']['SELL_ITEM']])

        if case(RESP['SAVEGAME']['STAY'],
                RESP['SAVEGAME']['SHARD'],
                RESP['SAVEGAME']['MIRROR'],
                RESP['MOVE']['TOWER_ITEM']):
            SAVE.parse(par[0])
            if on_stage(IMG['SCR']['CHAR_BG']):
                if act == RESP['MOVE']['TOWER_ITEM']:
                    show_tower_screen(par)
                else:
                    if act == RESP['SAVEGAME']['SHARD']:
                        play(SND['SHARD'])
                        mirror_fade_amount = 0.2
                        mirror_ani_timer.start()

                    if act == RESP['SAVEGAME']['MIRROR']:
                        play(SND['MIRROR'])

                    display_inventory(
                        None, on_stage(IMG['SCR']['CHAR_BG_RIGHT'])
                    )

                    for i in range(13):
                        if mirror_pieces[i]:
                            add(IMG['MIRROR']['PIECE'] + i)
                        else:
                            remove(IMG['MIRROR']['PIECE'] + i)
            break

        if case(ACT['SCREEN']['CHAR']):
            SAVE.parse(par[0])
            player_desc = resolve_breaks(par[1])
            if savegame[SG['FACE']['1']] == 0:
                show_build_character_screen()
            else:
                show_character_screen(None, True)
            break

        if case(ACT['SCREEN']['ZAUBERLADEN']):
            SAVE.parse(par[0])
            if par[1]:
                special_action = par[1]
            else:
                special_action = 0

            LOG.info("Magic shop says special action is" + special_action)
            if on_stage(IMG['SCR']['FIDGET_BG']):
                display_inventory()
            else:
                load(IMG['SCR']['FIDGET_BG'])
                show_character_screen()
                when_loaded(do_act_zauberladen)
            break

        if case(ACT['SCREEN']['SCHMIEDE']):
            SAVE.parse(par[0])
            if par[1]:
                special_action = par[1]
            else:
                special_action = 0
            LOG.info("Weapon shop says special action is" + special_action)
            if on_stage(IMG['SCR']['SHAKES_BG']):
                display_inventory()
            else:
                load(IMG['SCR']['SHAKES_BG'])
                show_character_screen()
                when_loaded(do_act_schmiede)
            break

        if case(RESP['UPDATE']['CHECK']):
            ExternalIF.call("refresh")
            break

        if case(RESP['LOGIN']['SUCCESS']['BOUGHT'],
                RESP['LOGIN']['SUCCESS']):
            mirror_fade_amount = 0.2
            admin_login = ""

            mush_bought = 0
            if act == RESP['LOGIN']['SUCCESS_BOUGHT']:
                mush_bought = int(par[3])

            beer_fest = False
            if par[5]:
                beer_fest = not int(par[5]) == 0

            if par[4]:
                param_server_version_act = par[4]

            session_id = ""
            if par[2]:
                session_id = par[2]

            level_up = False
            last_level = 0
            global old_ach
            old_ach = list()
            old_album = -1
            album_effect = False
            previous_login = True
            gilden_id = 0
            SAVE.parse(par[0], False)

            dealer_aktion = 0
            if par[1]:
                dealer_aktion = int(par[1])

            pulse_dealer = False
            if dealer_aktion > 0:
                pulse_dealer = True

            shared_obj.data.skipAutoLOGin = False
            if not shared_obj.data.HasAccount:
                shared_obj.data.PaymentMethod = 4

            shared_obj.data.HasAccount = True
            shared_obj.data.userName = actor[INP['NAME']].getChildAt(1).text
            shared_obj.data.password = actor[
                INP['LOGIN_PASSWORD']
            ].getChildAt(1).text
            shared_obj.flush()
            add(CNT['IF']['LOGOUT'])

            if savegame[SG['FACE']['1']] == 0:
                LOG.error("Fehler): Charakter nicht initialisiert.")
                request_logout()
            else:
                SAVE.parse(par[0])
                server_time = int(savegame[SG['SERVER']['TIME']])
                email_date = int(savegame[SG['EMAIL']['DATE']])

                if view_player != "":
                    sel_name = view_player
                    send_action(ACT['REQUEST']['CHAR'], view_player)
                elif param_hall != "":
                    send_action(ACT['SCREEN']['EHRENHALLE'], param_hall, "-2")
                    param_valid = ""
                elif ((int(savegame[SG['EMAIL']['VALID']]) < 1)
                      and (server_time > (email_date + 2 * 60 * 24 * 60))):
                    if param_valid != "":
                        send_action(ACT['VALIDATE'], param_valid)
                        param_valid = ""
                    else:
                        show_email_nag_screen()
                elif int(savegame[SG['EMAIL']['VALID']]) == 1:
                    if param_valid != "":
                        show_email_nag_screen(3)
                    else:
                        show_city_screen()
                elif param_valid != "":
                    send_action(ACT['VALIDATE'], param_valid)
                    param_valid = ""
                else:
                    show_city_screen()
            break

        if case(ERR['ALREADY_IN_GUILD'],
                ERR['NO_INDEX_FREE'],
                ERR['FIGHT_SELF'],
                ERR['GUILD']['NOT_FOUND'],
                ERR['GUILD']['NOT_ALLOWED'],
                ERR['GUILD']['LACK_MUSH'],
                ERR['GUILD']['LACK_GOLD'],
                ERR['GUILD']['BUILDING_NOT_FOUND'],
                ERR['GUILD']['BUILDING_MAX'],
                ERR['GUILD']['NOT_MEMBER'],
                ERR['GUILD']['MASTER_CANT_BE_OFFICER'],
                ERR['GUILD']['IS_FULL'],
                ERR['GUILD']['ALREADY_YOU_OTHER'],
                ERR['GUILD']['NOT_REAL_MEMBER'],
                ERR['GUILD']['ALREADY_YOU_THIS'],
                ERR['GUILD']['PLAYER_NOT_FOUND'],
                ERR['SUBJECT']['TOO_SHORT'],
                ERR['GUILD']['TOO_EXPENSIVE'],
                ERR['GUILD']['CHAT']['NOT_MEMBER'],
                ERR['GUILD']['CHAT']['HISTORY'],
                ERR['GUILD']['CHAT']['TEXT_ERROR'],
                ERR['BEER'],
                ERR['NO_MUSH_BAR'],
                ERR['NO_ENDURANCE'],
                ERR['WORSE_MOUNT'],
                ERR['GUILD']['ALREADY_MEMBER'],
                ERR['NOT_INVITED'],
                ERR['NO_MUSH_PVP'],
                ERR['NO_MUSH_MQ']):
            error_message(
                texts[
                    TXT['ERROR']['ALREADY_IN_GUILD']
                    - ERR['ALREADY_IN_GUILD'] + act
                ]
            )
            break

        if case(ERR['BOOST']):
            break

        if case(RESP['ACCOUNT']['SUCCESS']):
            actor[
                INP['LOGIN_PASSWORD']
            ].getChildAt(1).text = actor[INP['PASSWORD']].getChildAt(1).text
            shared_obj.data.skipAutoLOGin = False
            shared_obj.data.HasAccount = True
            shared_obj.data.had_account = True
            shared_obj.data.userName = actor[INP['NAME']].getChildAt(1).text
            shared_obj.data.password = actor[
                INP['LOGIN_PASSWORD']
            ].getChildAt(1).text
            shared_obj.data.advpar = param_obj
            shared_obj.flush()
            log_in_after_pixel = True
            break

        if case(ERR['NAME_EXISTS']):
            error_message(texts[TXT['ERROR']['NAME_EXISTS']])
            break

        if case(ERR['NAME_TOO_SHORT']):
            error_message(texts[TXT['ERROR']['NAME_TOO_SHORT']])
            break

        if case(ERR['PASSWORD_TOO_SHORT']):
            error_message(texts[TXT['ERROR']['PASSWORD_TOO_SHORT']])
            break

        if case(ERR['EMAIL_REJECTED']):
            error_message(texts[TXT['ERROR']['EMAIL_REJECTED']])
            break

        if case(ERR['NAME_REJECTED']):
            error_message(texts[TXT['ERROR']['NAME_REJECTED']])
            break

        if case(ERR['LOGIN_FAILED']):
            shared_obj.data.skipAutoLlogin = True
            shared_obj.data.password = ""
            shared_obj.flush()
            actor[INP['EMAIL']].getChildAt(1).text = ""
            actor[INP['PASSWORD']].getChildAt(1).text = ""
            charface.volk = 0
            show_login_screen(None, True, True)
            error_message(texts[TXT['ERROR']['LOGIN_FAILED']])
            break

        if case(ERR['TOO_EXPENSIVE']):
            if on_stage(BTN['MODIFY_CHARACTER']):
                charface = revertface
                show_option_screen()

            error_message(texts[TXT['ERROR']['TOO_EXPENSIVE']])
            break

        if case(ERR['WRONG']['PASSWORD']):
            error_message(texts[TXT['ERROR']['WRONG_PASSWORD']])
            break

        if case(ERR['FACE']['DATA_INCORRECT']):
            error_message(texts[TXT['ERROR']['FACE_DATA_INCORRECT']])
            break

        if case(ERR['EMAIL_WRONG']):
            error_message(texts[TXT['ERROR']['EMAIL']['WRONG']])
            break

        if case(RESP['PLAYER_NOT_FOUND']):
            error_message(texts[TXT['ERROR']['PLAYER_NOT_FOUND']])
            break

        if case(act < 0):
            error_message(
                texts[TXT['ERROR']['UNKNOWN']] + " (#" + str(act) + ")"
            )
            break
        if case():
            LOG.warning("Warning: Action unknown: " + act + ". Ignored!")

    playerid = savegame[SG['PLAYER_ID']]
    if act == RESP['ACCOUNT']['SUCCESS']:
        playerid = par[0]

    if defined_pixel_calls[act]:
        ExternalIF.call(
            defined_pixel_calls[act],
            str(act),
            param_cid,
            playerid,
            param_obj,
            shared_obj.data.advpar
        )

    pas = list()
    pxl_str = ""
    in_var = False

    for pixel in trackPixels:
        if (((int(pixel[0]) == act) or (next_pxl > 0))
                and (next_pxl == int(pixel[0]))):
            pas = list()

            for pxa in pixel[1].split(","):
                if pxa.find("-") != -1:
                    parange = pxa.split("-")
                    for i in range(int(parange[0]), int(parange[1])+1):
                        pas.append(int(i))
                else:
                    pas.append(int(pxa))

            if (pixel[1] == "") or (not pas.index(int(param_adv)) != -1):
                pxl_str = pixel[2].replace(
                    "%playerid%", savegame[SG['PLAYER_ID']]
                ).replace(
                    "%cid%", param_cid
                ).replace(
                    "%mushbought%", str(mush_bought / 100)
                )

                if shared_obj.data.advpar:
                    pxl_arr = pxl_str.replace("<", ">").split(">")
                    pxl_str = ""
                    in_var = False

                    for pxl_itm in pxl_arr:
                        if in_var:
                            if shared_obj.data.advpar[pxl_itm]:
                                pxl_str += str(shared_obj.data.advpar[pxl_itm])
                            else:
                                LOG.warning(''.join([
                                    "Warning: Constructing tracking pixel ",
                                    "url: Variable",
                                    pxl_itm,
                                    "was not within the stored parameters."
                                ]))
                        else:
                            pxl_str = pxl_str + pxl_itm

                        in_var = not in_var

                if int(savegame[SG['PLAYER_ID']]) == 0:
                    next_pxl = -(act)
                else:
                    load_tracking_pixel(pxl_str)

    if next_pxl > 0:
        next_pxl = 0

    if log_in_after_pixel:
        request_login(event)


def io_error_handler(event):
    '''
        log IO errors

        TODO: better use exceptions??
    '''
    LOG.error(event)


def get_file_version():
    '''
        get file version

        TODO: hor does this work anyways?
    '''
    tmp_str = get_my_path(1)
    num_str = ""
    result = ""
    tmp_str = tmp_str.split(".")[0]

    for i in range(len(tmp_str), 0, -1):
        num_str = tmp_str[i: 1]
        if num_str == str(int(num_str)):
            result += num_str

    return int(result)


def get_my_path(mode=0):
    '''
        get url/path of current file
    '''
    full_path = loader_info.url
    sections = full_path.split("/")
    file_name = sections[(sections.length - 1)]
    folder_name = full_path[0: len(full_path) - len(file_name)]
    for case in Switch(mode):
        if case(0):
            return folder_name
        if case(1):
            return file_name
        if case(2):
            return full_path

    return ""


def get_ip():
    '''
        return fake own ip
    '''
    return "127.0.0.1"


def set_title_bar(msg=""):
    '''
        set browser window title
    '''
    tmp_str = ""
    if msg == "":
        tmp_str = " - "

    msg += ''.join([
        tmp_str,
        texts[TXT['GAMETITLE']],
        " (",
        server.split(".")[0],
        ")"
    ])

    ExternalIF.call("set_title", msg)


def swap_words(tmp_str):
    '''
        some oscure string manipulation

        TODO: hat does this do?
    '''
    if text_dir == "right":
        tmp_arr = list()
        tmp_str2 = ""
        tmp_char = ""
        tmp_arr = tmp_str.split(" ").reverse()

        for k in range(len(tmp_arr)):
            if len(tmp_arr[k]) >= 2:
                punct1 = tmp_arr[k][-3: 3]
                if punct1 != "...":
                    punct1 = tmp_arr[k][-1: 1]

                punct2 = tmp_arr[k][0: 1]
                if ((punct1 != "!")
                        and (punct1 != ".")
                        and (punct1 != ":")
                        and (punct1 != "،")
                        and (punct1 != "x؟")
                        and ((punct1 != "\"")
                             or (len(tmp_arr[k].split("\"")) > 2))):
                    punct1 = ""

                if ((punct2 != "\"")
                        or (len(tmp_arr[k].split("\"")) > 2)):
                    punct2 = ""

                if punct1 == "...":
                    punct2 += "..."
                    punct1 = ""

                tmpidx = 0
                if punct2 != "":
                    tmpidx = 1

                tmpidx2 = len(tmp_arr[k]) - len(punct1 + punct2) + punct2

                tmp_arr[k] = punct1 + tmp_arr[k][tmpidx: tmpidx2]

        tmp_str = tmp_arr.join(" ")
        tmp_str = tmp_str.replace(
            "(", "#PARENTHESIS#"
        ).replace(
            ")", "("
        ).replace(
            "#PARENTHESIS#", ")"
        )

        tmp_str = tmp_str.replace(
            "[", "#SBRACKET#"
        ).replace(
            "]", "["
        ).replace(
            "#SBRACKET#", "]"
        )

    return tmp_str


def superior_font(font1, font2):
    '''
        get higher rated font from hardcoded ranking
    '''
    font_ranking = [
        "Gorilla Milkshake", "Komika Text", "Verdana", "Arial Narrow"
    ]
    rank1 = font_ranking.index(font1)
    rank2 = font_ranking.index(font2)

    if rank1 < 0:
        LOG.warning(' '.join(
            "Warning: Font",
            font1,
            "was unknown and could not be ranked."
        ))
        rank1 = len(font_ranking)

    if rank2 < 0:
        LOG.warning(' '.join(
            "Warning: Font",
            font2,
            "was unknown and could not be ranked."
        ))
        rank2 = len(font_ranking)

    if rank1 > rank2:
        return font1
    else:
        return font2


def define_bunch(bunch_id, *args):
    '''
        define group of actors
    '''
    actor[bunch_id] = list()

    for arg in args:
        actor[bunch_id].append(arg)


def add_bunch(bunch_id, *args):
    '''
        add actors to goup
    '''
    for arg in args:
        actor[bunch_id].append(arg)


def define_snd(actor_id, url, pre_load=False):
    '''
        define sound actor
    '''
    if url.lower()[0: 4] == "http:":
        full_url = url
    else:
        full_url = snd_url[snd_url_index] + url

    actor[actor_id] = Sound()
    actorSoundLoader[actor_id] = SoundLoaderContext()
    actorURL[actor_id] = full_url
    actorLoaded[actor_id] = 0
    if pre_load:
        load(actor_id)


def define_btn(actor_id, caption, handler, btn_class,
               pos_x=0, pos_y=0, scale_x=1, scale_y=1, vis=True):
    '''
        define button actor
    '''
    def play_click_sound():
        '''
            button click sound
        '''
        play(SND['CLICK'])

    actor[i] = btn_class()

    current = actor[actor_id]
    current.add_event_listener(MouseEvent.MOUSE_DOWN, play_click_sound)
    if btn_class == btn_classPlus:
        current.add_event_listener(MouseEvent.MOUSE_DOWN, handler)
    else:
        current.add_event_listener(MouseEvent.CLICK, handler)

    current.x = pos_x
    current.y = pos_y
    current.scaleX = scale_x
    current.scaleY = scale_y
    current.visible = bool(vis)
    current.tab_enabled = False
    current.allow_smoothing = True
    current.force_smoothing = True
    current.smoothing = True

    if caption != "":
        set_btn_text(actor_id, caption)


def error_message(msg=""):
    '''
        Display error message
    '''
    if msg != "":
        LOG.error("Error message: " + msg)

        if on_stage(SHP['FUCK']['BLACK_SQUARE']):
            label = actor[LBL['ERROR']]
            label.text = msg
            label.scaleX = 1
            label.scaleY = 1
            label.x = POS['IF']['ERROR_X'] - int(label.text_width / 2)
            label.y = POS['IF']['ERROR_Y'] + 60

            add(LBL['ERROR'])
        else:
            if on_stage(CNT['GILDE']['LIST']):
                if msg.replace(" ", "") != "":
                    chat_line(msg, True)
            else:
                if ((on_stage(BTN['CREATE_CHARACTER'])
                     and (not on_stage(IMG['IF']['WINDOW'])))):
                    label = actor[LBL['CREATE']['RACE_DESC']]
                    label.default_text_format = FontFormatClassError
                    label.text = msg
                    label.default_text_format = FontFormatDefaultLeft

                    actor[LBL['CREATE']['CLASS']].text = ""
                    actor[LBL['CREATE']['CLASS_DESC']].text = ""

                else:
                    label = actor[LBL['ERROR']]
                    label.text = msg
                    label.scaleX = 1
                    label.scaleY = 1
                    if on_stage(BTN['SHOPS_NEWWAREZ']):
                        label.x = (POS['SHOP']['ERROR_X']
                                   - int(label.text_width / 2))
                        label.y = POS['SHOP']['ERROR_Y']
                    elif on_stage(IMG['TOILET']):
                        label.x = (POS['SHOP']['ERROR_X'] - 15
                                   - int(label.text_width / 2))
                        label.y = 720
                    elif on_stage(BTN['QUEST']['CANCEL']):
                        label.x = (POS['IF']['ERROR_X']
                                   - int(label.text_width / 2))
                        label.y = POS['QUEST']['ERROR_Y']
                    elif on_stage(IMG['POST_BG']):
                        label.x = (POS['IF']['ERROR_X']
                                   - int(label.text_width / 2))
                        label.y = POS['QUEST']['ERROR_Y']
                    elif on_stage(LBL['STALL_TITEL']):
                        label.x = (POS['IF']['ERROR_X']
                                   - int(label.text_width / 2))
                        label.y = POS['QUEST']['ERROR_Y']
                    elif on_stage(BTN['CHAR_ATTACK']):
                        label.scaleX = 0.7
                        label.scaleY = 0.7
                        label.x = 280 + 500 + 235 - label.width / 2
                        label.y = 100 + 657
                    elif on_stage(SHP['MAINQUEST']):
                        label.x = (POS['IF']['ERROR_X']
                                   - int(label.text_width / 2))
                        label.y = POS['MQ']['ERROR_Y']
                    else:
                        label.x = (POS['IF']['ERROR_X']
                                   - int(label.text_width / 2))
                        label.y = POS['IF']['ERROR_Y']

                    add(LBL['ERROR'])


def enable_popup(actor_id, *args):
    '''
        enable popup actor
    '''
    popup_width = 0
    text_y = 0
    text_x = 0
    my_stamp = 0

    my_stamp, popup_stamp = popup_stamp + 1
    if popup_stamp > 10000:
        popup_stamp = 0

    if len(args) > 0:
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_OVER, show_popup)
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_MOVE,
                                           position_popup)
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_OUT, hide_popup)
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_DOWN, hide_popup)
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_UP, hide_popup)

    actorpopup_stamp[actor_id] = my_stamp


def on_stage(actor_id):
    '''
        actor is schon on screen?
    '''
    if actor[actor_id] is DisplayObject:
        return bool(get_child_by_name(actor[actor_id].name))
    return False


def tv_timer_event_handler():
    '''
        handle tev timer event
    '''
    tv_wobble += 0.1
    while tv_wobble > (2 * math.pi):
        tv_wobble -= 2 * math.pi
    if (tv_status_dest - tv_status) >= 0.1:
        tv_status += 0.1
    elif (tv_status - tv_status_dest) >= 0.1:
        tv_status -= 0.1
    else:
        tv_status = tv_status_dest

    tv_ani += 1
    if tv_ani >= 4:
        tv_ani = 0

    if tv_status == 1:
        show(CA['TV'])
    if tv_status == 0:
        hide(CA['TV'])

    for i in range(4):
        actor[IMG['TV'] + i].scaleX = tv_status
        actor[IMG['TV'] + i].scaleY = tv_status
        actor[IMG['TV'] + i].rotation = math.sin(tv_wobble) * 5
        actor[IMG['TV'] + i].alpha = tv_status
        if (i == tv_ani) and (tv_status > 0):
            show(IMG['TV'] + i)
        else:
            hide(IMG['TV'] + i)

    if not on_stage(IMG['TV']):
        tv_timer.stop()

        for i in range(4):
            hide(IMG['TV'] + i)

        tv_status = 0
        tv_status_dest = 0


def witch_timer_event_handler():
    '''
        handle itch time event
    '''
    witch_ani_step += 1

    if witch_ani_step >= 15:
        witch_ani_step = 0

    for i in range(15):
        if i == witch_ani_step:
            show(IMG['WITCH_ANI'] + i)
        else:
            hide(IMG['WITCH_ANI'] + i)

    if not on_stage(IMG['WITCH']):
        witch_ani_timer.stop()


def sound_loaded(duration):
    '''
        load sound success callback
    '''
    LOG.debug("Sound " + actor_id + " geladen.")
    actor[actor_id].play(0, duration, stObject)


def play(actor_id, endless=False):
    '''
        play a sound
    '''
    if actorLoaded[actor_id] == 2:
        duration = 0
        if endless:
            duration = 30000
        actor[actor_id].play(0, duration, stObject)
    else:
        LOG.warning(' '.join("Warnung: Sound",
                             actor_id,
                             "nicht geladen! Wird geladen..."))
        actor[actor_id].add_event_listener(Event.COMPLETE, sound_loaded)
        load(actor_id)


def process_arg(arg):
    '''
        process popup argument
    '''
    i_array = 0
    tmp_do = None
    if arg is list:
        for i_array in arg:
            process_arg(i_array)

    elif arg is int:
        if arg < 0:
            popup_width = -arg
        elif arg == 0:
            text_x = 0
            if text_dir == "right":
                text_x = popup_width

            text_y += last_text_height + 10
        elif text_dir == "right":
            text_x = popup_width - arg
        else:
            text_x = arg

    elif arg is TextFormat:
        tmp_text_format = arg

    elif arg is DisplayObject:
        tmp_do = Bitmap(arg.content.bitmapData.clone())
        if text_dir == "right":
            if text_x < popup_width:
                tmp_do.x_pos = text_x - tmp_do.width
                text_x = text_x - tmp_do.width + 5
                tmp_do.y_pos = text_y
            else:
                tmp_do.x_pos = popup_width - 5 - tmp_do.width
                tmp_do.y_pos = text_y
                text_y = text_y + tmp_do.text_height + 10
        else:
            if text_x > 0:
                tmp_do.x_pos = text_x
                text_x = text_x + tmp_do.width + 5
                tmp_do.y_pos = text_y
            else:
                tmp_do.x_pos = 5
                tmp_do.y_pos = text_y
                text_y = text_y + tmp_do.text_height + 10
        actor[POPUP_INFO].addChild(tmp_do)

    elif arg is str:
        arg = arg.replace("#", chr(13))

        tmp_tf = TextField()
        tmp_tf.auto_size = TextFieldAutoSize.LEFT
        tmp_tf.background = False
        tmp_tf.selectable = False
        tmp_tf.embed_fonts = font_embedded
        tmp_tf.default_text_format = tmp_text_format
        tmp_tf.html_text = arg
        last_text_height = tmp_tf.text_height
        if text_dir == "right":
            tmp_tf.auto_size = TextFieldAutoSize.RIGHT
            if text_x < popup_width:
                tmp_tf.x_pos = text_x - tmp_tf.text_width
                text_x -= tmp_tf.text_width + 5
                tmp_tf.y_pos = text_y
            else:
                tmp_tf.x_pos = popup_width - 5 - tmp_tf.text_width
                tmp_tf.y_pos = text_y
                text_y += tmp_tf.text_height + 10
        else:
            if text_x > 0:
                tmp_tf.x_pos = text_x
                text_x += tmp_tf.text_width + 5
                tmp_tf.y_pos = text_y
            else:
                tmp_tf.x_pos = 5
                tmp_tf.y_pos = text_y
                text_y += tmp_tf.text_height + 10

            if (tmp_tf.x_pos + tmp_tf.text_width + 10) > popup_width:
                popup_width = tmp_tf.x_pos + tmp_tf.text_width + 10

        actor[POPUP_INFO].addChild(tmp_tf)


def show_popup(evt, *args):
    '''
        Show popup window
    '''
    if evt.buttonDown:
        return

    if actorpopup_stamp[actor_id] != my_stamp:
        remove_event_listener(MouseEvent.MOUSE_OVER, show_popup)
        remove_event_listener(MouseEvent.MOUSE_MOVE, position_popup)
        remove_event_listener(MouseEvent.MOUSE_OUT, hide_popup)
        remove_event_listener(MouseEvent.MOUSE_DOWN, hide_popup)
        remove_event_listener(MouseEvent.MOUSE_UP, hide_popup)
        return

    if on_stage(POPUP_INFO):
        remove(POPUP_INFO)

    actor[POPUP_INFO] = MovieClip()
    if suggestion_slot[actor_id]:
        actor[IMG['SLOT_SUGGESTION']].x = actor[suggestion_slot[actor_id]].x
        actor[IMG['SLOT_SUGGESTION']].y = actor[suggestion_slot[actor_id]].y
        if not on_stage(IMG['SLOT_SUGGESTION']):
            add_some(IMG['SLOT_SUGGESTION'], suggestion_slot[actor_id])
            actor[IMG['SLOT_SUGGESTION']].alpha = 0
            fade_in(IMG['SLOT_SUGGESTION'])

    tmp_text_format = FontFormatPopup
    last_text_height = 0

    popup_width = 0
    if text_dir == "right":
        popup_width = 50
        text_x = popup_width

    text_y = 10

    for arg in args:
        process_arg(arg)

    current = actor[POPUP_INFO]
    for i in range(numChildren):
        if current.getChildAt(i).x < 5:
            dist = 5 - current.getChildAt(i).x

            for cur_child in current.numChildren:
                cur_child.x += dist
                if (cur_child.x + cur_child.width + 5) > popup_width:
                    popup_width = cur_child.x + cur_child.width + 5

    current.mouse_enabled = False
    current.mouseChildren = False
    current.allow_smoothing = True
    current.force_smoothing = True
    current.smoothing = True

    current = actor[POPUP_INFO].graphics
    current.beginFill(0, 0)
    current.lineStyle(0, 0, 0)
    current.drawRect(0, 0, popup_width, text_y)
    current.beginFill(CLR['BLACK'], 0.8)
    current.lineStyle(1, CLR['SFORANGE'], 1)
    current.drawRect(1, 1, (popup_width - 1), (text_y - 1))

    position_popup(evt)
    add(POPUP_INFO)


def try_show_tv():
    '''
    var evt:* = evt;
    if (tvTest){
        tv_status_dest = 1;
        tv_timer.start();
        tvTest = False;
    } else {
        if (((((!((tv_function_name == ""))) and (!(disable_tv))))
                and (!(prevent_tv)))){
            if (!evt){
                tv_poll_timer.start();
                tv_poll_timer.delay = tv_poll_normal;
            } else {
                if (((!(on_stage(TAVERNE_BG)))
                        and (!(on_stage(QUESTBAR_BG))))){
                    tv_poll_timer.stop();
                    return;
                };
            };
            trc((("Calling TV function \"" + tv_function_name)
                + "\" with parameter \"requesttv\"!"));
            try {
                tv_return_value = ExternalIF.call(tv_function_name,
                     "requesttv", (((((savegame[SG['PLAYER_ID']] + "_")
                   + savegame[SG_PAYMENT_ID]) + "_") + server_id) + "_1"),
                    savegame[SG_GENDER], 0);
            } catch(e:Error) {
                trc(("There was an error: " + e.message));
                tv_poll_timer.delay = tv_poll_long;
            };
            trc(("Return value is " + str(tv_return_value)));
            if (tv_return_value > 0){
                tv_status_dest = 1;
                tv_poll_timer.delay = tv_poll_long;
            } else {
                tv_status_dest = 0;
                if (tv_return_value == -2){
                    tv_poll_timer.stop();
                } else {
                    if (tv_return_value == -1){
                        tv_poll_timer.delay = tv_poll_long;
                    } else {
                        tv_poll_timer.delay = tv_poll_normal;
                    };
                };
            };
            if (tv_status_dest != tv_status){
                tv_timer.start();
            };
        } else {
            if (((!(disable_tv)) and (!(prevent_tv)))){
                trc("Notice: No TV function set!");
            };
        };
    };

    '''
    pass


def next_fight():
    '''
    var guild_fight_exp;
    var guild_fight_honor;
    var par:Array;
    var thisRoundFighterName:String;
    var guild_battle_data:Array;
    var tmp_str:*;
    guild_fight_exp = 0;
    guild_fight_honor = 0;
    if (fights.length < 2){
        fights = list();
        return;
    };
    thisRoundFighterName = "";
    var nextRoundFighterName:String = "";
    var thisRoundopp_name:String = "";
    if (skip_guild_fights > 0){
        while (fights.length > 3) {
            if (thisRoundFighterName != ""){
                last_round_fighter_name = thisRoundFighterName;
            };
            if (fights[0].split(";")[2].split("/")[5] > 0){
                thisRoundFighterName = fights[0].split(";")[2].split("/")[0];
            } else {
                thisRoundFighterName = "?";
            };
            thisRoundopp_name = fights[0].split(";")[2].split("/")[15];
            if (thisRoundFighterName.lower() == actor[INP['NAME'
                ]].getChildAt(1).text.lower()){
                if (skip_guild_fights == 1){
                    skip_guild_fights = -1;
                    break;
                };
            };
            if (fights[2]){
                nextRoundFighterName = fights[2].split(";")[2].split("/")[0];
                if (last_round_fighter_name == thisRoundFighterName){
                    if (winners[("name_" + thisRoundFighterName)]){
                        var _local10 = winners;
                        var _local11 = ("name_" + thisRoundFighterName);
                        var _local12 = (_local10[_local11] + 1);
                        _local10[_local11] = _local12;
                    } else {
                        winners[("name_" + thisRoundFighterName)] = 1;
                    };
                };
            };
            fights.shift();
            fights.shift();
        };
    };
    thisRoundFighterName = fights[0].split(";")[2].split("/")[0];
    if (thisRoundFighterName.lower() == actor[INP['NAME'
        ]].getChildAt(1).text.lower()){
        if (skip_guild_fights == 1){
            skip_guild_fights = -1;
        };
    };
    par = fights.shift().split(";");
    guild_battle_data = fights.shift().split("/");
    if (fights.length == 1){
        tmp_str = fights.pop();
        guild_fight_exp = tmp_str.split(";")[1];
        guild_fight_honor = tmp_str.split(";")[2];
    };
    post_fight_mode = False;
    fightNumber = ((guild_fight_count - int(((fights.length + 1) / 2)))
     (((guild_fight_count % 2))==0) ? 1 : 0);
    if (fightNumber > guild_fight_count){
        fightNumber = 1;
    };
    show_fight_screen(par[0].split("/"), par[1].split("/"), (par[6] == "1"),
                      par[2].split("/"), (par[5] == "2"), ((par[3] + "/")
                                                       + par[4]).split("/"),
                        int(par[7]), int(par[8]), (par[5] == "3"), False,
                        int(par[9]), guild_battle_data, (fights.length <= 1),
                        guild_fight_exp, guild_fight_honor, par[10], par[11],
                        par[12]);
    '''
    pass


def guild_fight_timer_fn():
    '''
    if (guild_attack_time != 0){
        if (!waiting_for(guild_attack_time)){
            if (on_stage(LBL['GILDE']['CHAT']_CAPTION)){
                send_action(ACT_SCREEN_GILDEN);
            } else {
                pulse_gilde = True;
            };
            guild_attack_time = 0;
        };
    };
    if (guild_defense_time != 0){
        if (!waiting_for(guild_defense_time)){
            if (on_stage(LBL['GILDE']['CHAT']_CAPTION)){
                send_action(ACT_SCREEN_GILDEN);
            } else {
                pulse_gilde = True;
            };
            guild_defense_time = 0;
    '''
    pass


def guild_chat_poll_fn():
    '''
    if (param_poll_tunnel_url == ""){
        if (gilde == ""){
            guild_chat_poll.delay = 1000;
            return;
        };
        if (on_stage(INP_GILDE_CHAT)){
            guild_chat_poll.delay = (1000 * interval_multiplier_chat);
        } else {
            if (param_idle_polling > 0){
                guild_chat_poll.delay = (1000 * param_idle_polling);
            } else {
                guild_chat_poll.delay = (1000 * 60);
            };
        };
    } else {
        guild_chat_poll.delay = 1000;
        if (gilde == ""){
            return;
        };
    };
    send_action(ACT_GET_CHAT_HISTORY, last_chat_index);
    '''
    pass


def position_popup(evt):
    '''
    var evt:* = evt
    var _local3 = actor[POPUP_INFO]
    with (_local3) {
        x = (evt.stageX - int((popup_width / 2)))
        y = ((evt.stageY - 20) - text_y)
        if (x < 0){
            x = 0
        }
        if (y < 0){
            y = 0
        }
        if (x > (RES_X - popup_width)){
            x = (RES_X - popup_width);
        };
        if (y > (RES_Y - text_y)){
            y = (RES_Y - text_y);
        };
        if ((((((((evt.stageX > (x - 20)))
            and ((evt.stageX < ((x + popup_width) + 15)))))
            and ((evt.stageY > (y - 20)))))
            and ((evt.stageY < ((y + text_y) + 15))))){
            if (evt.stageY < (text_y + 20)){
                y = (evt.stageY + 40);
            };
            if ((((((((evt.stageX > (x - 20)))
                and ((evt.stageX < ((x + popup_width) + 15)))))
                and ((evt.stageY > (y - 20)))))
                and ((evt.stageY < ((y + text_y) + 15))))){
                if (evt.stageX > ((RES_X - popup_width) - 20)){
                    x = ((evt.stageX - popup_width) - 20);
                };
            };
        };
    };
    '''
    print evt


def hide_popup():
    '''
    remove(SLOT_SUGGESTION);
    remove(POPUP_INFO);
    '''
    pass


def do_add_btn_image():
    '''
    var _local2 = obj.getChildAt(1);
    with (_local2) {
        tmpImage = new Bitmap(actor[imgActor].content.bitmapData.clone());
        tmpImage.x = ((getCharBoundaries(imgIndex).x + x) + 4);
        tmpImage.y = (((getCharBoundaries(imgIndex).y + y) - 3)
                      + (((text_dir == "right")) ? 7 : 0));
        obj.addChild(tmpImage);
    };
    '''
    pass


def center_text_field(obj, aoffsx=0, aoffsy=0):
    '''
    var btnText:* = None;
    var char:* = None;
    var i:* = 0;
    var imgActor:* = 0;
    var tmpImage:* = None;
    var obj:* = obj;
    var aoffsx = aoffsx;
    var aoffsy = aoffsy;
    btnText = "";
    var imgIndex:* = -1;
    while (obj.numChildren > 2) {
        Sprite(obj).removeChildAt(2);
    };
    i = 0;
    while (i < caption.length) {
        char = caption[i];
        if (char == "~"){
            imgIndex = i;
            i = (i + 1);
            if (caption[i] == "P"){
                btnText = (btnText + "     ");
                load(IF_PILZE);
                imgActor = IF_PILZE;
            } else {
                if (caption[i] == "G"){
                    btnText = (btnText + "     ");
                    load(IF_GOLD);
                    imgActor = IF_GOLD;
                } else {
                    if (caption[i] == "S"){
                        btnText = (btnText + "     ");
                        load(IF_SILBER);
                        imgActor = IF_SILBER;
                    };
                };
            };
        } else {
            btnText = (btnText + char);
        };
        i = (i + 1);
    };
    var _local5 = obj.getChildAt(1);
    with (_local5) {
        auto_size = TextFieldAutoSize.LEFT;
        embed_fonts = font_embedded;
        default_text_format = new TextFormat(game_font,
                                             (((specialFontSize == 0))
                                              ? default_text_format.size
                                              : specialFontSize),
                                             default_text_format.color);
        text = btnText;
        x = int(((((obj.getChildAt(0).width / 2)
                - (text_width / 2)) + offs) + aoffsx));
        y = int(((((obj.getChildAt(0).height / 2)
                - (textHeight / 2)) + offsy) + aoffsy));
        if (imgIndex != -1){
            when_loaded(do_add_btn_image);
        };
    };
    '''
    print obj, aoffsx, aoffsy


def set_btn_text(actor_id, caption):
    '''
    var i:* = 0;
    var offsy:* = 0;
    var actor_id:* = actor_id;
    var caption:* = caption;
    i = actor_id;
    var offs:* = 0;
    offsy = 0;
    var specialFontSize:* = 0;
    if ((actor[i] is btn_classBasic)){
        offs = -2;
    };
    if ((actor[i] is btn_classBasic)){
        offsy = 1;
    };
    if ((actor[i] is btn_classInterface)){
        offs = 5;
    };
    if ((actor[i] is btn_classInterface)){
        offsy = 0;
    };
    if ((actor[i] is btn_classLOGin)){
        offs = -2;
    };
    if ((actor[i] is btn_classLOGin)){
        offsy = 1;
    };
    if ((actor[i] is btn_classBack)){
        offsy = 50;
    };
    if (game_font == "Verdana"){
        offsy = (offsy - 6);
    };
    if (game_font == "Arial Narrow"){
        specialFontSize = 16;
        offsy = (offsy - 4);
    };
    center_text_field(actor[i].upState);
    center_text_field(actor[i].downState, 1, 2);
    center_text_field(actor[i].overState);
    center_text_field(actor[i].hitTestState);
    '''
    print actor_id, caption


def define_lbl(actor_id, caption, pos_x=0, pos_y=0, fmt=None, vis=True):
    '''
    var i:* = 0;
    var fmtUL:* = None;
    var actor_id:* = actor_id;
    var caption:* = caption;
    var pos_x = pos_x;
    var pos_y = pos_y;
    var fmt:* = fmt;
    var vis:Boolean = vis;
    i = actor_id;
    actor[i] = new TextField();
    if (!fmt){
        fmt = FontFormatDefault;
    };
    var _local8 = actor[i];
    with (_local8) {
        default_text_format = fmt;
        auto_size = TextFieldAutoSize.LEFT;
        background = False;
        selectable = False;
        embed_fonts = font_embedded;
        anti_alias_type = AntiAliasType.ADVANCED;
        if (caption){
            htmlText = caption;
        };
        x = pos_x;
        y = pos_y;
        visible = Boolean(vis);
    };
    '''
    print actor_id, caption, pos_x, pos_y, fmt, vis


# -----------------------------------------------------------------------------
# (File) Loaders


def language_file_error():
    '''
        error handling for I18N file loader
    '''
    global lang_code, text_dir
    LOG.error("Chosen language " + lang_code + " not available!")
    if lang_code == original_lang_code:
        lang_code = original_lang_code

    if lang_code == "ar":
        text_dir = "right"

    loader.load(
        URLRequest(lang_url + "lang/sfgame_" + lang_code + ".txt")
    )


def language_file_loaded(evt):
    '''
        success handler for I18N file loader
    '''
    str_data = loader.data
    in_value = False
    tmp_str = ""
    last_index = 0

    for i in range(len(str_data) - 1):
        char = str_data.charCodeAt(i)
        for case in Switch(char):
            if case(10, 13):
                in_value = False
                if len(tmp_str) > 0:
                    texts[last_index] = swap_words(tmp_str)
                    tmp_str = ""
                else:
                    if not texts[last_index]:
                        texts[last_index] = ""
                break

            if case(9, 20):
                if not in_value:
                    last_index = int(tmp_str)
                    tmp_str = ""
                    in_value = True
                else:
                    tmp_str += str_data[i]
                break

            if case(136):
                tmp_str += chr(13) + chr(10)

            if case():
                tmp_str += str_data[i]

    global pending_language_file
    pending_language_file = False
    if lang_code == original_lang_code:
        if texts[TXT['FONT_NAME']] != "":
            set_font(texts[TXT['FONT_NAME']])
        else:
            set_font("Komika Text")
    else:
        chosen_lang_font = "Komika Text"
        if texts[TXT['FONT_NAME']]:
            chosen_lang_font = texts[TXT['FONT_NAME']]
        load_original_language_file()

    for i in range(TXT['COUNTRY_NAMES'], TXT['COUNTRY_NAMES'] + 100):
        if texts[i]:
            country_name[texts[i].split("=")[0]] = texts[i].split("=")[1]
        else:
            break

    loader_complete(evt)


def load_language_file():
    '''
        I18N file loader
    '''
    global text_dir, pending_language_file

    loader = URLLoader()
    loader.data_format = URLLoaderdataFormat.TEXT
    loader.add_event_listener(Event.COMPLETE, language_file_loaded)
    loader.add_event_listener(IOErrorEvent.IO_ERROR, language_file_error)
    loader.add_event_listener(SecurityErrorEvent.SECURITY_ERROR,
                              language_file_error)
    if lang_code == "ar":
        text_dir = "right"

    loader.load(URLRequest(''.join([
        lang_url,
        "lang/sfgame_",
        lang_code,
        ".txt?rnd=",
        str(random.random())
    ])))

    global pending_loaders
    pending_loaders += 1
    pending_language_file = True


def original_language_file_loaded(evt):
    '''
        success on loading original I18N file
    '''
    str_data = loader.data
    in_value = False
    tmp_str = ""
    last_index = 0
    original_font = "Komika Text"

    for i in range(len(str_data) - 1):
        char = str_data.charCodeAt(i)
        for case in Switch(char):
            if case(10, 13):
                in_value = False
                if len(tmp_str) > 0:
                    old_str = tmp_str
                    if last_index == TXT['FONT_NAME']:
                        original_font = tmp_str
                    tmp_str = ""

                break
            if case(9, 20):
                if not in_value:
                    last_index = int(tmp_str)
                    tmp_str = ""
                    in_value = True
                else:
                    tmp_str += str_data[i]
                break
            if case(136):
                tmp_str += chr(13) + chr(10)

            if case():
                tmp_str += str_data[i]

    global pending_language_file
    pending_language_file = False
    set_font(superior_font(chosen_lang_font, original_font))
    loader_complete(evt)


def load_original_language_file():
    '''
        I18N file loader
    '''
    loader = URLLoader()
    loader.data_format = URLLoaderdataFormat.TEXT
    loader.add_event_listener(Event.COMPLETE, Originallanguage_file_loaded)
    loader.load(URLRequest(
        lang_url + "lang/sfgame_" + original_lang_code + ".txt"
    ))

    global pending_language_file, pending_loaders
    pending_loaders += 1
    pending_language_file = True


def configuration_file_loaded(evt):
    '''
        parse configuration file
    '''
    str_data = evt.target.data
    in_value = False
    tmp_str = ""
    last_index = 0

    for i in range(len(str_data) - 1):
        char = str_data.charCodeAt(i)
        for case in Switch(char):
            if case(13, 10):
                in_value = False
                if len(tmp_str) > 0:
                    for case in Switch(last_index):
                        if case(CFG['LANG_CODE']):
                            global lang_code
                            lang_code = tmp_str
                            original_lang_code = lang_code
                            break

                        if case(CFG['URL']):
                            img_url.append(tmp_str)
                            break

                        if case(CFG['SND_URL']):
                            snd_url[len(snd_url)] = tmp_str
                            break

                        if case(CFG['LIGHT_MODE']):
                            light_mode_default = (int(tmp_str) != 0)
                            break

                        if case(CFG['SERVER']):
                            global server
                            server = tmp_str
                            break

                        if case(CFG['LANG_URL']):
                            global lang_url
                            lang_url = tmp_str
                            break

                        if case(CFG['NO_CROSSDOMAIN']):
                            no_crossdomain = (int(tmp_str) != 0)
                            break

                        if case(CFG['FORUM_URL']):
                            forum_url = tmp_str
                            break

                        if case(CFG['SHOP_URL']):
                            shop_url = tmp_str
                            break

                        if case(CFG['IMPRINT_URL']):
                            imprint_url = tmp_str
                            break

                        if case(CFG['LEGAL_URL']):
                            legal_url = tmp_str
                            break

                        if case(CFG['DATAPROT_URL']):
                            dataprot_url = tmp_str
                            break

                        if case(CFG['INSTR_URL']):
                            instr_url = tmp_str
                            break

                        if case(CFG['BUFFEDMODE']):
                            buffed_mode = (tmp_str != "")
                            buffed_link_text = tmp_str
                            break

                        if case(CFG['PAYMETHODS']):
                            pay_methods = tmp_str.split("/")

                            for j in range(len(pay_methods)):
                                pay_methods[j] = int(pay_methods[j])
                            break

                        if case(CFG['SERVER_ID']):
                            server_id = int(tmp_str)
                            break

                        if case(CFG['MP_PROJECT']):
                            mp_project = tmp_str
                            break

                        if case(CFG['BUFFED_URL']):
                            buffed_link_url = tmp_str
                            break

                        if case(CFG['RESPONSE_TIMEOUT']):
                            response_timeout = int(tmp_str)
                            break

                        if case(CFG['IMAGE_TIMEOUT']):
                            image_timeout = int(tmp_str)
                            break

                        if case(CFG['SPONSOR_IMG']):
                            param_sponsor = tmp_str
                            break

                        if case(CFG['REROLL_IMG']):
                            param_reroll_img = int(tmp_str)
                            break

                        if case(CFG['RECONNECT']):
                            param_reconnect = int(tmp_str)
                            break

                        if case(CFG['PHP_TUNNEL_URL']):
                            param_php_tunnel_url = tmp_str
                            break

                        if case(CFG['TRACKING_PIXEL']):
                            trackPixels.append(tmp_str.split(";"))
                            LOG.debug(
                                ("Tracking pixel definition old " + tmp_str)
                            )
                            break

                        if case(CFG['POLL_TUNNEL_URL']):
                            param_poll_tunnel_url = tmp_str
                            break

                        if case(CFG['SUPPORT_EMAIL']):
                            param_support_email = tmp_str
                            break

                        if case(CFG['GAMESTAFF_EMAIL']):
                            param_gamestaff_email = tmp_str
                            break

                        if case(CFG['PAPAYA_PATH']):
                            param_papaya_path = tmp_str
                            break

                        if case(CFG['PAPAYA_FILE']):
                            param_papaya_cfg_file = tmp_str
                            break

                        if case(CFG['RESEND_COUNT']):
                            global param_fail_tries
                            param_fail_tries = int(tmp_str)
                            break

                        if case(CFG['IDLE_POLLING']):
                            param_idle_polling = int(tmp_str)
                            break

                        if case(CFG['ALLOW_SKIP_QUEST']):
                            param_allow_skip_quest = (int(tmp_str) == 1)
                            param_happy_hour = (int(tmp_str) == 2)
                            break

                        if case(CFG['CENSORED']):
                            param_censored = (int(tmp_str) != 0)
                            break

                        if case(CFG['INTERNAL_PIXEL']):
                            param_internal_pixel = (int(tmp_str) != 0)
                            break

                        if case(CFG['RELOAD_PIXEL']):
                            param_reload_pixel = (int(tmp_str) != 0)
                            break

                        if case(CFG['SERVER_VERSION']):
                            param_server_version_cfg = tmp_str
                            break

                        if case(CFG['DONT_SAVE_CID']):
                            param_no_cid_save = (int(tmp_str) != 0)
                            break

                        if case(CFG['FLAGS']):
                            param_languages = tmp_str.split("/")
                            break

                        if case(CFG['FLAG_NAMES']):
                            param_language_names = tmp_str.split("/")
                            break

                        if case(CFG['LOWRES_URL']):
                            break

                        if case(CFG['SPONSOR_URL']):
                            param_sponsor_url = tmp_str
                            break

                        if case(CFG['BULLSHIT_BOX']):
                            param_bullshit_text = tmp_str
                            break

                        if case(CFG['BULLSHIT_CID']):
                            param_bullshit_cid = tmp_str
                            break

                        if case(CFG['SOCIAL_BUTTONS']):
                            param_social_buttons = tmp_str.split("/")
                            break

                        if case(CFG['PIXEL_CALL']):
                            defined_pixel_calls[
                                tmp_str.split(":")[0]
                            ] = tmp_str.split(":")[1]
                            break

                        if case(CFG['BACKGROUND_ID']):
                            login_background_id = tmp_str
                            break

                        if case(CFG['WORLDS']):
                            worlds = list()
                            tmp_worlds = tmp_str.split(";")

                            for j in range(len(tmp_worlds)):
                                tmp_world = list()
                                tmp_world[0] = tmp_worlds[j].split(":")[0]
                                tmp_world[1] = tmp_worlds[
                                    j
                                ].split(":")[1].split("/")
                                worlds.append(tmp_world)
                            break

                        if case(CFG['TV_FUNCTION']):
                            tv_function_name = tmp_str
                            break

                        if case(CFG['TV_POLL_INTERVAL_NORMAL']):
                            tv_poll_normal = int(tmp_str) * 1000
                            break

                        if case(CFG['TV_POLL_INTERVAL_LONG']):
                            tv_poll_long = int(tmp_str) * 1000
                            break
                tmp_str = ""
                break

            if case(20, 9):
                if not in_value:
                    last_index = int(tmp_str)
                    tmp_str = ""
                    in_value = True
                else:
                    tmp_str += str_data[i]
                break

            if case(136):
                tmp_str += chr(13) + chr(10)
            if case():
                tmp_str += str_data[i]

    global pending_configuration_files
    pending_configuration_files -= 1
    if pending_configuration_files == 1:
        loader2.load(URLRequest("config_txt"))
    else:
        pending_configuration_files = False
        global shared_obj
        shared_obj = SharedObject.get_local(
            "SFGame/" + server.replace(".", "/"), "/")
        if shared_obj.data.lang_code:
            lang_code = shared_obj.data.lang_code

        light_mode = light_mode_default
        chat_sound = False
        compare_items = False
        disable_tv = False

        if shared_obj.data.light_mode is False:
            light_mode = False
        if shared_obj.data.light_mode is True:
            light_mode = True
        if shared_obj.data.chat_sound is False:
            chat_sound = False
        if shared_obj.data.chat_sound is True:
            chat_sound = True
        if shared_obj.data.compare_items is False:
            compare_items = False
        if shared_obj.data.compare_items is True:
            compare_items = True
        if shared_obj.data.disable_tv is False:
            disable_tv = False
        if shared_obj.data.disable_tv is True:
            disable_tv = True
        if param_obj["lang"] is not None:
            lang_code = param_obj["lang"]
        if param_obj["id"] is not None:
            param_id = str(param_obj["id"])

        if param_obj["rec"] is not None:
            param_rec = str(param_obj["rec"])
            if shared_obj.data.had_account:
                param_rec = ""

        if param_obj["viewplayer"] is not None:
            view_player = str(param_obj["viewplayer"])

        if param_obj["adminlogin"] is not None:
            admin_login = str(param_obj["adminlogin"])

        if param_obj["mp_api_user_id"] is not None:
            mp_api_user_id = str(param_obj["mp_api_user_id"])

        if param_obj["mp_api_user_token"] is not None:
            mp_api_user_token = str(param_obj["mp_api_user_token"])

        if ((param_obj["mp_api_user_id"] is not None)
                and (param_obj["mp_api_user_token"] is not None)):
            sso_mode = True

        if param_obj["cid"] is not None:
            param_cid = str(param_obj["cid"])
            param_cid_original = True
            shared_obj.data.cid = param_cid
            shared_obj.flush()
        elif param_obj["CID"] is not None:
            param_cid = str(param_obj["CID"])
            param_cid_original = True
            shared_obj.data.cid = param_cid
            shared_obj.flush()
        elif param_obj["Cid"] is not None:
            param_cid = str(param_obj["Cid"])
            param_cid_original = True
            shared_obj.data.cid = param_cid
            shared_obj.flush()
        elif shared_obj.data.cid:
            if ((shared_obj.data.cid.find("_") == -1)
                    and (len(shared_obj.data.cid) == 15)):
                param_cid = shared_obj.data.cid + "_r"
        elif not param_no_cid_save:
            param_cid = shared_obj.data.cid

        had_account = shared_obj.data.had_account
        if param_obj["adv"] is not None:
            param_adv = str(param_obj["adv"])
            shared_obj.data.adv = param_adv
            shared_obj.data.advpar = param_obj
            shared_obj.flush()
        elif param_obj["cid"] is not None:
            shared_obj.data.advpar = param_obj
            shared_obj.flush()
        elif shared_obj.data.adv:
            param_adv = shared_obj.data.adv

        if param_obj["valid"] is not None:
            param_valid = str(param_obj["valid"])

        if param_obj["val"] is not None:
            param_valid = str(param_obj["val"])

        if param_obj["hall"] is not None:
            param_hall = str(param_obj["hall"])

        if param_obj["imgsvr"] is not None:
            param_imgsvr = int(param_obj["imgsvr"])

        if param_obj["port"] is not None:
            param_forceport = int(param_obj["port"])

        force_reroll = (param_reroll_img > int(shared_obj.data.force_reroll))

        if force_reroll:
            shared_obj.data.force_reroll = param_reroll_img
            shared_obj.flush()

        if len(img_url) == 0:
            img_url[0] = ""

        if len(snd_url) == 0:
            snd_url[0] = ""

        global img_url_index, snd_url_index
        if shared_obj.data.img_url_index:
            if param_imgsvr > 0:
                img_url_index = param_imgsvr - 1
            elif ((shared_obj.data.img_url_index <= len(img_url))
                  and not force_reroll):
                img_url_index = shared_obj.data.img_url_index - 1
            else:
                img_url_index = int(random.random() * len(img_url))
        else:
            img_url_index = int((random.random() * len(img_url)))

        if shared_obj.data.snd_url_index:
            if param_imgsvr > 0:
                snd_url_index = param_imgsvr - 1
            elif ((shared_obj.data.snd_url_index <= len(snd_url))
                  and (not force_reroll)):
                snd_url_index = shared_obj.data.snd_url_index - 1
            else:
                snd_url_index = int(random.random() * len(snd_url))
        else:
            snd_url_index = int(random.random() * len(snd_url))

        if len(img_url) == len(snd_url):
            snd_url_index = img_url_index

        shared_obj.data.img_url_index = img_url_index + 1
        shared_obj.data.snd_url_index = snd_url_index + 1
        shared_obj.flush()

        if light_mode:
            if param_lowres_url != "":
                img_url[img_url_index] = param_lowres_url
                snd_url[snd_url_index] = param_lowres_url

    loader_complete(evt)


def strip_slashes(source):
    '''
        strip slashes from url
    '''
    return source.replace("http://", "").replace("/", "")


def do_load_language_file():
    '''
        load language file
    '''
    Security.load_policy_file(img_url[img_url_index] + "crossdomain.xml")
    Security.load_policy_file(snd_url[snd_url_index] + "crossdomain.xml")
    Security.load_policy_file(lang_url + "crossdomain.xml")
    Security.load_policy_file("http://" + server + "/crossdomain.xml")
    Security.allow_domain(
        strip_slashes(img_url[img_url_index]),
        strip_slashes(snd_url[snd_url_index]),
        strip_slashes(lang_url),
        server
    )
    load_language_file()
    when_loaded(build_interface)


def do_load(actor_id):
    '''
        load stuff for actor
    '''
    if actorLoaded[actor_id] == 0:
        if actor[actor_id] is Sound:
            Security.allow_domain(actorURL[actor_id])
            req = URLRequest(actorURL[actor_id])
            actor[actor_id].load(req, actorSoundLoader[actor_id])
            actorLoaded[actor_id] = 2
        else:
            actor[actor_id].contentLoaderInfo.add_event_listener(
                IOErrorEvent.IO_ERROR, LoaderError
            )
            actor[actor_id].contentLoaderInfo.add_event_listener(
                Event.COMPLETE, LoaderComplete
            )
            Security.allow_domain(actorURL[actor_id])
            req = URLRequest(actorURL[actor_id])
            if ((actorURL[actor_id][-4:] == ".png")
                    and (not no_crossdomain)):
                actor[actor_id].load(
                    req,
                    LoaderContext(
                        True,
                        ApplicationDomain(None),
                        SecurityDomain.currentDomain
                    )
                )
            else:
                actor[actor_id].load(req)

            actorLoaded[actor_id] = 1


def load(*actor_ids):
    '''
        load stuff for actor
        (wrapper for do_load)
    '''
    for actid in actor_ids:
        if actor[actid] is list:
            for i_bunch in actor[actid]:
                load(i_bunch)
            return
        do_load(actid)


def when_loaded(function=None):
    '''
        async loading finished
    '''
    pending = False
    global when_loaded_fn

    if isinstance(function, types.FunctionType):
        when_loaded_fn.append(function)
        global when_loaded_active
        when_loaded_active = True
        when_loaded_timeout.stop()
        when_loaded_timeout.start()

    for i in range(len(actor)):
        if actorLoaded[i] == 1:
            pending = True
            break

    if pending_language_file:
        pending = True

    if pending_debug_file:
        pending = True

    if pending_configuration_files:
        pending = True

    if not pending:
        if when_loaded_active:
            when_loaded_timeout.stop()
            when_loaded_active = False
            when_loaded_fn_temp = when_loaded_fn
            when_loaded_fn = list()

            for i in range(len(when_loaded_fn_temp)):
                tmp_fn = when_loaded_fn_temp[i]
                when_loaded_fn_temp[i] = Function()
                tmp_fn()


def when_loaded_timeout_event():
    '''
        loading stuff timeout
    '''
    global snd_url_index, img_url_index

    when_loaded_timeout.stop()

    for i in range(len(actor)):
        if actor[i] is Loader:
            if actorLoaded[i] == 1:
                LOG.error(
                    ''.join([
                        "Fehler: Timeout beim Laden. Ladezustand wird",
                        "zurückgesetzt für Aktor"
                    ]),
                    i,
                    actorURL[i]
                )
                actorLoaded[i] = 0

    when_loaded()
    to_error_count += 1

    if to_error_count == 10:
        old_img_url_index = img_url_index
        if len(img_url) > 1:
            img_url_index = int(random.random() * len(img_url))
            while img_url_index == old_img_url_index:
                img_url_index = int(random.random() * len(img_url))

        old_snd_url_index = snd_url_index
        if len(snd_url) > 1:
            snd_url_index = int(random.random() * len(snd_url))
            while snd_url_index == old_snd_url_index:
                snd_url_index = int(random.random() * len(snd_url))

        if len(img_url) == len(snd_url):
            snd_url_index = img_url_index

        shared_obj.data.img_url_index = img_url_index + 1
        shared_obj.data.snd_url_index = snd_url_index + 1
        shared_obj.flush()


def loader_complete(evt):
    '''
        loading success
    '''
    if evt.target is LoaderInfo:
        actorLoaded[get_actor_id(evt.target.loader)] = 2
        Security.allow_domain(evt.target.loaderURL)

        content = actor[get_actor_id(evt.target.loader)].content
        content.force_smoothing = True
        content.allow_smoothing = True
        content.smoothing = True
    when_loaded()


def loader_error(evt):
    '''
        loading failed
    '''
    global snd_url_index, img_url_index

    if evt.target is LoaderInfo:
        for i in range(len(actor)):
            if actor[i] is Loader:
                if actorLoaded[i] == 1:
                    LOG.error(
                        ''.join([
                            "Fehler: IO-Fehler beim Laden. Ladezustand wird",
                            "zurückgesetzt für Aktor"
                        ]),
                        i,
                        actorURL[i]
                    )
                    actorLoaded[i] = 0

    when_loaded()
    io_error_count += 1

    if io_error_count == 10:
        old_img_url_index = img_url_index
        if len(img_url) > 1:
            img_url_index = int(random.random() * len(img_url))
            while img_url_index == old_img_url_index:
                img_url_index = int(random.random() * len(img_url))

        old_snd_url_index = snd_url_index
        if len(snd_url) > 1:
            snd_url_index = int(random.random() * len(snd_url))
            while snd_url_index == old_snd_url_index:
                snd_url_index = int(random.random() * len(snd_url))

        if len(img_url) == len(snd_url):
            snd_url_index = img_url_index

        shared_obj.data.img_url_index = img_url_index + 1
        shared_obj.data.snd_url_index = snd_url_index + 1
        shared_obj.flush()


def pixel_success():
    '''
        TODO: What does this do?
    '''
    pixel_data = pixel_loader.data
    if ((pixel_data.lower().substr(0, 7) == "http://")
            or (pixel_data.lower().substr(0, 8) == "https://")):
        ExternalIF.call("loadpixel", pixel_data)

    # pixel_loader.remove_event_listener(Event.COMPLETE, pixel_success)
    # pixel_loader.remove_event_listener(IOErrorEvent.IO_ERROR, pixel_failed)
    # pixel_loader.remove_event_listener(
    #     SecurityErrorEvent.SECURITY_ERROR, pixel_failed
    # )


def pixel_failed():
    '''
        TODO: Obsolete?
    '''
    # pixel_loader.remove_event_listener(Event.COMPLETE, pixel_success)
    # pixel_loader.remove_event_listener(IOErrorEvent.IO_ERROR, pixel_failed)
    # pixel_loader.remove_event_listener(
    #     SecurityErrorEvent.SECURITY_ERROR, pixel_failed
    # )
    pass


def load_tracking_pixel(url=''):
    '''
        load tracking pixel
    '''
    # req = None
    # variables = None
    # pixel_loader = None

    LOG.debug("Tracking Pixel Load:" + url)

    # TODO: set via requests params
    if url.find("?") == -1:
        url = url + "?random="
    else:
        url = url + "&random="

    url += str(int((random.random() * 100000)))
    url += ("&had_account=") + int(had_account)

    if param_reload_pixel:
        LOG.debug("Tracking Pixel Reload Mode for: " + url)
        LOG.debug("CID userd " + param_cid)
        LOG.debug("Action " + act)

        # req = new URLRequest("index.php")
        # req.method = URLRequestMethod.POST

        # variables = new URLVariables()
        # variables.pixel_url = url
        # variables.pixel_cid = param_cid
        # variables.pixel_player_id = savegame[SG['PLAYER_ID']]
        # variables.pixel_action = (((next_pxl == 0)) ? act : abs(next_pxl)

        # req.data = variables

        log_in_after_pixel = False
        navigate_to_url(req, "_self")
    else:
        if param_internal_pixel:
            # pixel_loader = new URLLoader()
            # pixel_loader.add_event_listener(Event.COMPLETE, pixel_success)
            # pixel_loader.add_event_listener(
            #    IOErrorEvent.IO_ERROR, pixel_failed)
            # pixel_loader.add_event_listener(
            #   SecurityErrorEvent.SECURITY_ERROR, pixel_failed
            # )
            # pixel_loader.load(new URLRequest(url))
            pass
        else:
            ExternalIF.call("loadpixel", url)


# -----------------------------------------------------------------------------

def main():
    '''
        main function
         - program starting point
    '''
    global LOG

    LOG = setup_logging()

    init_vars()

    game_session = Session()
    configure(game_session)

    # response = s.login()


if __name__ == "__main__":
    main()


def define_img(actor_id, url, pre_load=True, pos_x=0, pos_y=0,
               scale_x=1, scale_y=1, vis=True):
    '''
    var i:* = 0;
    var full_url:* = None;
    var LoaderCompleteLocal:* = None;
    var actor_id:* = actor_id;
    var url:* = url;
    var pre_load:Boolean = pre_load;
    var pos_x = pos_x;
    var pos_y = pos_y;
    var scale_x = scale_x;
    var scale_y = scale_y;
    var vis:Boolean = vis;
    LoaderCompleteLocal = function (evt:Event){
        actor[i].cacheAsBitmap = True;
    };
    i = actor_id;
    if (url.lower()[0: 4] == "http:"){
        full_url = url;
    } else {
        full_url = (img_url[img_url_index] + url);
    };
    actor[i] = new Loader();
    actor[i].contentLoaderInfo.add_event_listener(IOErrorEvent.IO_ERROR,
                                                  LoaderError);
    actor[i].contentLoaderInfo.add_event_listener(Event.COMPLETE,
                                                  LoaderComplete);
    actor[i].contentLoaderInfo.add_event_listener(Event.COMPLETE,
                                                  LoaderCompleteLocal);
    actorLoaded[i] = 0;
    actorURL[i] = full_url;
    var _local10 = actor[i];
    with (_local10) {
        tab_enabled = False;
        x = pos_x;
        y = pos_y;
        force_smoothing = True;
        allow_smoothing = True;
        smoothing = True;
        scaleX = scale_x;
        scaleY = scale_y;
        visible = Boolean(vis);
    };
    if (pre_load){
        load(i);
    };
    '''
    print actor_id, url, pre_load, pos_x, pos_y, scale_x, scale_y, vis


def define_click_area(actor_id, img_actor_id, function, pos_x, pos_y, size_x,
                      size_y, ovl_actor_id=0, hover_fn=None,
                      out_fn=None, stay_put=False):
    '''
    var actor_id:* = actor_id;
    var img_actor_id:* = img_actor_id;
    var function:* = function;
    var pos_x:* = pos_x;
    var pos_y:* = pos_y;
    var size_x:* = size_x;
    var size_y:* = size_y;
    var ovl_actor_id = ovl_actor_id;
    var hover_fn:* = hover_fn;
    var out_fn:* = out_fn;
    var stay_put:Boolean = stay_put;
    var ClickAreaHover:* = function (evt:MouseEvent):
        if (img_actor_id != C_EMPTY){
            add(img_actor_id);
        };
        if (ovl_actor_id != C_EMPTY){
            visible_to_front(ovl_actor_id);
        };
        if (!stay_put){
            add(actor_id);
        };
        if ((hover_fn is Function)){
            hover_fn();
        };
    };
    var ClickAreaOut:* = function (evt:MouseEvent):
        remove(img_actor_id);
        if ((out_fn is Function)){
            out_fn();
        };
    };
    actor[actor_id] = new MovieClip();
    var _local13 = actor[actor_id];
    with (_local13) {
        tab_enabled = False;
        x = pos_x;
        y = pos_y;
        graphics.beginFill(0xFF0000);
        graphics.drawRect(0, 0, size_x, size_y);
        alpha = ((C_SHOW_CA) ? 0.3 : 0);
        mouseChildren = False;
        mouse_enabled = True;
        if ((function is Function)){
            add_event_listener(MouseEvent.MOUSE_OVER, ClickAreaHover);
            add_event_listener(MouseEvent.MOUSE_OUT, ClickAreaOut);
            add_event_listener(MouseEvent.CLICK, function);
            useHandCursor = True;
            buttonMode = True;
        };
    };
    '''
    print actor_id, img_actor_id, function, pos_x, pos_y, size_x, size_y
    print ovl_actor_id, hover_fn, out_fn, stay_put


def define_from_class(actor_id, img_class, pos_x=0, pos_y=0, txt_manip=0,
                      txt_type=""):
    '''
    var i:* = 0;
    var actor_id:* = actor_id;
    var img_class:* = img_class;
    var pos_x = pos_x;
    var pos_y = pos_y;
    var txt_manip = txt_manip;
    var txt_type:String = txt_type;
    var ManipTextField:* = function (field){
        var field:* = field;
        var _local3 = field;
        with (_local3) {
            embed_fonts = font_embedded;
            default_text_format = new TextFormat(game_font,
                     (default_text_format.size + size_mod),
                     default_text_format.color);
        };
    };
    i = actor_id;
    actor[i] = new (img_class)();
    actorLoaded[i] = 2;
    var _local8 = actor[i];
    with (_local8) {
        x = pos_x;
        y = pos_y;
        allow_smoothing = True;
        force_smoothing = True;
        smoothing = True;
        visible = True;
    };
    if (txt_manip == 1){
        ManipTextField(actor[i].getChildAt(0));
    } else {
        if (txt_manip == 2){
            ManipTextField(actor[i].getChildAt(1));
        };
    };
    '''
    print actor_id, img_class, pos_x, pos_y, txt_manip, txt_type


def define_cnt(actor_id, pos_x=0, pos_y=0, vis=True):
    '''
    var i:* = 0;
    var actor_id:* = actor_id;
    var pos_x = pos_x;
    var pos_y = pos_y;
    var vis:Boolean = vis;
    i = actor_id;
    actor[i] = new MovieClip();
    var _local6 = actor[i];
    with (_local6) {
        tab_enabled = False;
        x = pos_x;
        y = pos_y;
        visible = Boolean(vis);
        force_smoothing = True;
        allow_smoothing = True;
        smoothing = True;
    };
    '''
    print actor_id, pos_x, pos_y, vis


def text_link_make_clickable(obj):
    '''
        does nothing?
    '''
    print obj


def define_slider(actor_id, ticks, pos_x, pos_y, function):
    '''
    var i:* = 0;
    var oldSliderVal:* = 0;
    var actor_id:* = actor_id;
    var ticks:* = ticks;
    var pos_x:* = pos_x;
    var pos_y:* = pos_y;
    var function:* = function;
    var SliderMove:* = function (evt:MouseEvent):
        var tmpX;
        var sliderVal;
        if (evt.buttonDown){
            if ((((evt.localX > 35)) and ((evt.localX < (45 + 198))))){
                tmpX = evt.localX;
                sliderVal = (int(((((tmpX - 40) / 198)
                             * (ticks - 1)) + 0.5)) + 1);
                tmpX = (int((((sliderVal - 1) / (ticks - 1)) * 198)) + 40);
                evt.target.getChildAt(1).x = (tmpX - 7);
                if (oldSliderVal != sliderVal){
                    function(sliderVal);
                };
                oldSliderVal = sliderVal;
            };
        };
    };
    var ClickTick:* = function (evt:MouseEvent):
        var tmpX;
        var sliderVal;
        tmpX = (evt.stageX - actor[(actor_id + 1)].x);
        sliderVal = (int(((((tmpX - 40) / 198) * (ticks - 1)) + 0.5)) + 1);
        tmpX = (int((((sliderVal - 1) / (ticks - 1)) * 198)) + 40);
        actor[(actor_id + 1)].getChildAt(1).x = (tmpX - 7);
        if (oldSliderVal != sliderVal){
            function(sliderVal);
        };
        oldSliderVal = sliderVal;
    };
    actorBitmap[actor_id] = ticks;
    actorBitmap[(actor_id + 1)] = [function];
    define_from_class((actor_id + 1), DragonSlider, pos_x, pos_y);
    define_bunch(actor_id, (actor_id + 1));
    var _local7 = actor[(actor_id + 1)];
    with (_local7) {
        add_event_listener(MouseEvent.MOUSE_DOWN, SliderMove);
        add_event_listener(MouseEvent.MOUSE_MOVE, SliderMove);
        buttonMode = True;
        useHandCursor = True;
    };
    i = 1;
    while (i <= ticks) {
        define_from_class(((actor_id + 1) + i), SliderTick,
                        (((pos_x + 40) + int((198 * ((i - 1)
                         / (ticks - 1))))) - 5), (pos_y - 10));
        _local7 = actor[((actor_id + 1) + i)];
        with (_local7) {
            add_event_listener(MouseEvent.MOUSE_DOWN, ClickTick);
            buttonMode = True;
            useHandCursor = True;
        };
        add_bunch(actor_id, ((actor_id + 1) + i));
        i = (i + 1);
    };
    function(get_slider_value(actor_id));
    '''
    print actor_id, ticks, pos_x, pos_y, function


def get_slider_value(actor_id):
    '''
    var tmpX;
    tmpX = (actor[(actor_id + 1)].getChildAt(1).x + 5);
    return ((int(((((tmpX - 40) / 198) * (actorBitmap[actor_id] - 1))
            + 0.5)) + 1));
    '''
    print actor_id


def set_slider_value(actor_id, value):
    '''
    var tmpX;
    var oldVal;
    oldVal = get_slider_value(actor_id);
    tmpX = (int((((value - 1) / (actorBitmap[actor_id] - 1)) * 198)) + 40);
    actor[(actor_id + 1)].getChildAt(1).x = (tmpX - 7);
    if (oldVal != value){
        var _local5 = actorBitmap[(actor_id + 1)];
        _local5[0](value);
    };
    '''
    print actor_id, value


def make_persistent(*args):
    '''
    var i;
    var i_bunch;
    i = 0;
    while (i < _args.length) {
        if ((actor[_args[i]] is Array)){
            i_bunch = 0;
            while (i_bunch < actor[_args[i]].length) {
                make_persistent(actor[_args[i]][i_bunch]);
                i_bunch++;
            };
            return;
        };
        actorPersistent[_args[i]] = True;
        i++;
    };
    '''
    print args


def make_temporary(*args):
    '''
    var i;
    var i_bunch;
    i = 0;
    while (i < _args.length) {
        if ((actor[_args[i]] is Array)){
            i_bunch = 0;
            while (i_bunch < actor[_args[i]].length) {
                make_temporary(actor[_args[i]][i_bunch]);
                i_bunch++;
            };
            return;
        };
        actorPersistent[_args[i]] = False;
        i++;
    };
    '''
    print args


def enable_drag_drop(actor_id, handler, *args):
    '''
    var old_x:* = 0;
    var old_y:* = 0;
    var i:* = 0;
    var i_bunch:* = 0;
    var MouseBtnDown:* = None;
    var dragResetTimer:* = None;
    var dragReset:* = None;
    var MouseBtnUp:* = None;
    var actor_id:* = actor_id;
    var handler:* = handler;
    var Targets:* = _args;
    MouseBtnDown = function (evt:MouseEvent):
        var topPosition;
        if (((dragDropProhibit) or (dragNotYet))){
            return;
        };
        topPosition = (evt.target.parent.numChildren - 1);
        evt.target.parent.setChildIndex(evt.target, topPosition);
        evt.target.startDrag();
        dragDropActive = True;
    };
    dragReset = function (evt:Event){
        dragNotYet = False;
        dragResetTimer.stop();
    };
    MouseBtnUp = function (evt:MouseEvent):
        var dropped:Boolean;
        var droppedOn;
        var i_bunch;
        if (!dragDropActive){
            return;
        };
        dropped = False;
        dragDropActive = False;
        dragNotYet = True;
        dragResetTimer.start();
        evt.target.stopDrag();
        if (evt.target.dropTarget is not None){
            i = 0;
            while (i < Targets.length) {
                if ((actor[Targets[i]] is Array)){
                    i_bunch = 0;
                    while (i_bunch < actor[Targets[i]].length) {
                        if (actor[actor[Targets[i]][i_bunch]] == evt.target
                                    .dropTarget.parent){
                            dropped = True;
                            droppedOn = actor[Targets[i]][i_bunch];
                            break;
                        };
                        i_bunch++;
                    };
                } else {
                    if (actor[Targets[i]] == evt.target.dropTarget.parent){
                        dropped = True;
                        droppedOn = Targets[i];
                        break;
                    };
                };
                i++;
            };
            if (Targets.length == 0){
                i = 0;
                while (i < actor.length) {
                    if ((actor[i] is DisplayObject)){
                        if ((((actor[i] == evt.target.dropTarget.parent))
                            or ((actor[i] == evt.target.dropTarget)))){
                            dropped = True;
                            droppedOn = i;
                            break;
                        };
                    };
                    i++;
                };
            };
            if (dropped){
                if (!handler(actor_id, droppedOn)){
                    evt.target.x = old_x;
                    evt.target.y = old_y;
                };
            } else {
                evt.target.x = old_x;
                evt.target.y = old_y;
            };
        } else {
            evt.target.x = old_x;
            evt.target.y = old_y;
        };
    };
    old_x = actor[actor_id].x;
    old_y = actor[actor_id].y;
    if ((actor[actor_id] is Array)){
        i_bunch = 0;
        while (i_bunch < actor[actor_id].length) {
            if ((((actor[actor[actor_id][i_bunch]] is MovieClip))
                or ((actor[actor[actor_id][i_bunch]] is Sprite)))){
                actor[actor[actor_id][i_bunch]].add_event_listener(
                                       MouseEvent.MOUSE_DOWN, MouseBtnDown);
                actor[actor[actor_id][i_bunch]].add_event_listener(
                                        MouseEvent.MOUSE_UP, MouseBtnUp);
            } else {
                trc(("Fehler: Drag & Drop nicht unterstützt für Actor "
                    + actor[actor_id][i_bunch]));
            };
            i_bunch = (i_bunch + 1);
        };
        return;
    };
    if ((((actor[actor_id] is MovieClip)) or ((actor[actor_id] is Sprite)))){
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_DOWN, MouseBtnDown)
        actor[actor_id].add_event_listener(MouseEvent.MOUSE_UP, MouseBtnUp);
    } else {
        trc(("Fehler: Drag & Drop nicht unterstützt für Actor " + actor_id));
    };
    dragResetTimer = new Timer(500);
    dragResetTimer.add_event_listener(TimerEvent.TIMER, dragReset);
    '''
    print actor_id, handler, args


def set_cnt(cnt_id, img_id=0, pos_x=0, pos_y=0, center=False):
    '''
    var i_bunch:* = 0;
    var CntImgLoaded:* = None;
    var cnt_id:* = cnt_id;
    var img_id = img_id;
    var pos_x = pos_x;
    var pos_y = pos_y;
    var center:Boolean = center;
    if (!(actor[img_id] is Loader)){
        if (actorBitmap[cnt_id]){
            actor[cnt_id].removeChild(actorBitmap[cnt_id]);
            actorBitmap[cnt_id] = None;
        };
        return;
    };
    if ((actor[cnt_id] is Array)){
        i_bunch = 0;
        while (i_bunch < actor[cnt_id].length) {
            set_cnt(actor[cnt_id][i_bunch], img_id);
            i_bunch = (i_bunch + 1);
        };
        return;
    };
    if (actorBitmap[cnt_id]){
        actor[cnt_id].removeChild(actorBitmap[cnt_id]);
        actorBitmap[cnt_id] = None;
    };
    if (img_id != 0){
        if (actorLoaded[img_id] == 2){
            if ((((((img_id == ITM_EMPTY)) or ((img_id == ITM_OFFS))))
                and ((actor[cnt_id].width == 0)))){
                var _local7 = actor[cnt_id];
                with (_local7) {
                    graphics.beginFill(0, 0);
                    graphics.drawRect(0, 0, 90, 90);
                };
            };
            if ((actor[img_id].content is Bitmap)){
                actorBitmap[cnt_id] = new Bitmap();
                actorBitmap[cnt_id].bitmapData =
                    actor[img_id].content.bitmapData
                _local7 = actorBitmap[cnt_id];
                with (_local7) {
                    allow_smoothing = True;
                    force_smoothing = True;
                    smoothing = True;
                    x = (pos_x - ((center) ? (width / 2) : 0));
                    y = (pos_y - ((center) ? (height / 2) : 0));
                };
                actor[cnt_id].addChild(actorBitmap[cnt_id]);
            } else {
                actorBitmap[cnt_id] = new Bitmap();
                actorBitmap[cnt_id].bitmapData =
                                BitmapData(actor[img_id].width,
                                           actor[img_id].height,
                                           True, 0);
                actorBitmap[cnt_id].bitmapData.draw(
                                           (actor[img_id] as IBitmapDrawable));
                _local7 = actorBitmap[cnt_id];
                with (_local7) {
                    allow_smoothing = True;
                    force_smoothing = True;
                    smoothing = True;
                    x = (pos_x - ((center) ? (width / 2) : 0));
                    y = (pos_y - ((center) ? (height / 2) : 0));
                };
                actor[cnt_id].addChild(actorBitmap[cnt_id]);
            };
        } else {
            CntImgLoaded = function (evt:Event):
                actorLoaded[img_id] = 2;
                set_cnt(cnt_id, img_id, pos_x, pos_y, center);
            };
            actor[img_id].contentLoaderInfo.add_event_listener(
                                              Event.COMPLETE, CntImgLoaded);
            if (actorLoaded[img_id] == 0){
                load(img_id);
            };
        };
    };
    '''
    print cnt_id, img_id, pos_x, pos_y, center


def add_bmo(bunch_id, offset):
    '''
    var i;
    i = 0;
    while (i < actor[bunch_id].length) {
        if ((actor[actor[bunch_id][i]] is Array)){
            add_bmo(actor[bunch_id][i], offset);
        } else {
            add((actor[bunch_id][i] + offset));
        };
        i++;
    };
    '''
    print bunch_id, offset


def remove_illegal_chars(in_str):
    '''
    var LegalChars:String;
    var i;
    var j;
    var thisChar:String;
    var outStr:String;
    var pass:Boolean;
    if (texts[TXT_LEGALCHARS] == ""){
        return (in_str);
    };
    LegalChars = texts[TXT_LEGALCHARS];
    thisChar = "";
    outStr = "";
    pass = False;
    i = 0;
    while (i < in_str.length) {
        thisChar = in_str[i: 1]
        pass = False;
        j = 0;
        while (j < LegalChars.length) {
            if ((((thisChar.charCodeAt() == 13))
                or ((thisChar.charCodeAt() == 10)))){
                pass = True;
                break;
            };
            if (thisChar == LegalChars[j: 1]){
                pass = True;
                break;
            };
            j++;
        };
        if (pass){
            outStr = (outStr + thisChar);
        };
        i++;
    };
    return (outStr);
    '''
    print in_str


def semi_strip(in_str):
    '''
    var i;
    var outStr:String;
    outStr = "";
    i = 0;
    while (i < in_str.length) {
        if (in_str[i] == chr(13)){
            outStr = (outStr + "#");
        } else {
            if (in_str[i] == ";"){
                outStr = (outStr + ",");
            } else {
                if (in_str[i] == "§"){
                    outStr = (outStr + "$");
                } else {
                    outStr = (outStr + in_str[i]);
                };
            };
        };
        i++;
    };
    return (outStr);
    '''
    print in_str


def resolve_breaks(in_str):
    '''
    var i;
    var outStr:String;
    outStr = "";
    i = 0;
    while (i < in_str.length) {
        if (in_str[i] == "#"){
            outStr = (outStr + chr(13));
        } else {
            outStr = (outStr + in_str[i]);
        };
        i++;
    };
    return (outStr);
    '''
    return in_str


def post_btn_handler(evt=None, actor_id=0):
    '''
    var par:* = None;
    var GuildMsg:* = False;
    var thisRecipient:* = None;
    var recipients:* = None;
    var evt:* = evt;
    var actor_id = actor_id;
    remove(LBL['ERROR']);
    GuildMsg = False;
    if (evt){
        actor_id = get_actor_id(evt.target);
    };
    thisRecipient = "";
    recipients = list();
    Switch (actor_id){
        if case(POST_SEND:
            last_message_target = "";
            if (!on_stage(INP_POST_ADDRESS)){
                GuildMsg = True;
            } else {
                last_message_target = actor[INP_POST_ADDRESS]
                    .getChildAt(1).text;
            };
            if (actor[INP_POST_TEXT].getChildAt(1).text.find(
                    actor[INP['LOGIN_PASSWORD']].getChildAt(1).text) != -1){
                error_message(((texts[TXT_ERROR_COMPROMISED_ACCOUNT])
                              ? texts[TXT_ERROR_COMPROMISED_ACCOUNT]
                              : "You should never give your password away."));
            } else {
                if (actor[INP_POST_ADDRESS].getChildAt(1).text == texts[
                    TXT_EMPFAENGER]){
                    error_message(texts[TXT_ERROR_RECIPIENT_NOT_FOUND]);
                } else {
                    thisRecipient = actor[INP_POST_ADDRESS].getChildAt(1).text;
                    if (thisRecipient.find(",") != -1){
                        recipients = thisRecipient.split(",");
                    } else {
                        recipients = [thisRecipient];
                    };
                    while (recipients.length > 0) {
                        thisRecipient = recipients.shift();
                        while (thisRecipient[0: 1] == " ") {
                            thisRecipient = thisRecipient[1:]
                        };
                        while (thisRecipient[
                               (thisRecipient.length - 1): 1] == " ") {
                            thisRecipient = thisRecipient[
                                0: (thisRecipient.length - 1)]
                        };
                        send_action(((GuildMsg)
                                    ? ACT_POST_SEND_GUILD
                                    : ACT_POST_SEND),
                            remove_illegal_chars(semi_strip(thisRecipient)),
                            remove_illegal_chars(semi_strip(
                               actor[INP_POST_SUBJECT].getChildAt(1).text
                               .split("/").join(""))),
                            remove_illegal_chars(
                                             semi_strip(actor[INP_POST_TEXT]
                                               .getChildAt(1).text)));
                    };
                };
            };
            break;
        if case(POST_UP:
            if (post_scroll > 1){
                oldSel = -1;
                post_scroll = (post_scroll - 15);
                if (post_scroll < 1){
                    post_scroll = 1;
                };
                send_action(ACT_SCREEN_POST, post_scroll);
            };
            break;
        if case(POST_DOWN:
            if (post_scrollDown){
                post_scroll = (post_scroll + 15);
                post_scrollDown = False;
                if (post_scroll > 86){
                    post_scroll = 86;
                };
                if (post_scroll < 1){
                    post_scroll = 1;
                };
                send_action(ACT_SCREEN_POST, post_scroll);
            };
            break;
        if case(POST_READ:
            if (text_dir == "right"){
                make_right_text_area(INP_POST_ADDRESS, 1);
                make_right_text_area(INP_POST_SUBJECT, 1);
                make_right_text_area(INP_POST_TEXT, 1);
            };
            if (post_sel > 0){
                send_action(ACT_POST_READ, ((post_sel + post_scroll) - 1));
            };
            break;
        if case(POST_READ_NEXT:
            post_sel++;
            if (post_sel > 15){
                post_scroll = (post_scroll + 1);
                post_sel = 15;
            };
            send_action(ACT_POST_READ, ((post_sel + post_scroll) - 1));
            break;
        if case(POST_READ_PREV:
            post_sel--;
            if (post_sel < 1){
                post_scroll = (post_scroll - 1);
                post_sel = 1;
            };
            send_action(ACT_POST_READ, ((post_sel + post_scroll) - 1));
            break;
        if case(POST_DELETE:
        if case(POST_DELETEREAD:
            if (post_sel > 0){
                send_action(ACT_POST_DELETE, ((post_sel + post_scroll) - 1));
                if (int(savegame[SG_MSG_COUNT]) > 0){
                    savegame[SG_MSG_COUNT] = str((int(
                                                 savegame[SG_MSG_COUNT]) - 1));
                };
            };
            break;
        if case(POST_FLUSH:
            var _local4 = actor[LBL_WINDOW_TITLE];
            with (_local4) {
                text = texts[TXT_POST_FLUSH_TEXT];
                x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((text_width / 2)));
            };
            add(POST_FLUSHMSG);
            break;
        if case(POST_FLUSH_CANCEL:
            remove(POST_FLUSHMSG);
            add(IF_EXIT);
            break;
        if case(POST_FLUSH_OK:
            remove(POST_FLUSHMSG);
            send_action(ACT_POST_DELETE, -1);
            break;
        if case(POST_PROFILE:
            if (reply_address != ""){
                sel_name = reply_address;
                send_action(ACT['REQUEST']['CHAR'], reply_address);
            };
            break;
        if case(POST_WRITE:
            actor[INP_POST_ADDRESS].getChildAt(1).type = TextFieldType.INPUT;
            actor[INP_POST_SUBJECT].getChildAt(1).type = TextFieldType.INPUT;
            actor[INP_POST_TEXT].getChildAt(1).type = TextFieldType.INPUT;
            remove(POST_LIST);
            add(POST_WRITE);
            if (gilde != ""){
                if (text_dir == "right"){
                    actor[POST_GUILD].x = (POST_INP_X + 5);
                } else {
                    actor[POST_GUILD].x = (((POST_INP_X
                        + actor[INP_POST_ADDRESS].width)
                            - actor[POST_GUILD].width) - 5);
                };
                show(POST_GUILD);
            } else {
                hide(POST_GUILD);
            };
            actor[INP_POST_ADDRESS].getChildAt(1).text = texts[TXT_EMPFAENGER];
            actor[INP_POST_SUBJECT].getChildAt(1).text = texts[TXT_BETREFF];
            actor[INP_POST_TEXT].getChildAt(1).text = texts[TXT_NACHRICHT];
            if (text_dir == "right"){
                make_right_text_area(INP_POST_ADDRESS, 1);
                make_right_text_area(INP_POST_SUBJECT, 1);
                make_right_text_area(INP_POST_TEXT, 1);
            };
            break;
        if case(POST_CANCEL:
        if case(POST_RETURN:
            if (PostReturnToPlayer != ""){
                send_action(ACT['REQUEST']['CHAR'], PostReturnToPlayer);
            } else {
                remove(POST_WRITE);
                remove(POST_READ);
                remove(POST_ACCEPT);
                remove(POST_REPLY);
                add(POST_LIST);
            };
            break;
        if case(POST_ACCEPT:
            if (invitegilden_id > 0){
                send_action(ACT_GUILD_JOIN,
                            actor[INP['NAME']].getChildAt(1).text,
                            invitegilden_id,
                            MD5(actor[INP['LOGIN_PASSWORD']]
                                .getChildAt(1).text));
            };
            break;
        if case(POST_REPLY:
            if (reply_address != ""){
                actor[INP_POST_ADDRESS]
                    .getChildAt(1).type = TextFieldType.INPUT;
                actor[INP_POST_SUBJECT]
                    .getChildAt(1).type = TextFieldType.INPUT;
                actor[INP_POST_TEXT].getChildAt(1).type = TextFieldType.INPUT;
                remove(POST_READ);
                remove(POST_REPLY);
                remove(POST_FORWARD);
                if (gilde != ""){
                    if (text_dir == "right"){
                        actor[POST_GUILD].x = (POST_INP_X + 5);
                    } else {
                        actor[POST_GUILD].x = (((POST_INP_X
                                   + actor[INP_POST_ADDRESS].width)
                                    - actor[POST_GUILD].width) - 5);
                    };
                    show(POST_GUILD);
                } else {
                    hide(POST_GUILD);
                };
                add(POST_WRITE);
                show(POST_GUILD);
                actor[INP_POST_ADDRESS].getChildAt(1).text = reply_address;
                actor[INP_POST_TEXT].getChildAt(1).text = texts[TXT_NACHRICHT];
                if (text_dir == "right"){
                    if (actor[INP_POST_SUBJECT].getChildAt(
                            1).text.find(texts[TXT_RE]) == -1){
                        actor[INP_POST_SUBJECT].getChildAt(
                           1).text = ((reply_subject + " ") + texts[TXT_RE]);
                    };
                    make_right_text_area(INP_POST_ADDRESS, 1);
                    make_right_text_area(INP_POST_SUBJECT, 1);
                    make_right_text_area(INP_POST_TEXT, 1);
                } else {
                    if (actor[INP_POST_SUBJECT].getChildAt(
                            1).text.find(texts[TXT_RE]) == -1){
                        actor[INP_POST_SUBJECT].getChildAt(1)
                        .text = ((texts[TXT_RE] + " ") + reply_subject);
                    };
                };
            };
            break;
        if case(POST_FORWARD:
            if (forward_text != ""){
                actor[INP_POST_ADDRESS].getChildAt(1)
                    .type = TextFieldType.INPUT;
                actor[INP_POST_SUBJECT].getChildAt(1)
                    .type = TextFieldType.INPUT;
                actor[INP_POST_TEXT].getChildAt(1).type = TextFieldType.INPUT;
                remove(POST_READ);
                remove(POST_REPLY);
                remove(POST_FORWARD);
                if (gilde != ""){
                    if (text_dir == "right"){
                        actor[POST_GUILD].x = (POST_INP_X + 5);
                    } else {
                        actor[POST_GUILD].x = (((POST_INP_X
                                   + actor[INP_POST_ADDRESS].width)
                                    - actor[POST_GUILD].width) - 5);
                    };
                    show(POST_GUILD);
                } else {
                    hide(POST_GUILD);
                };
                add(POST_WRITE);
                show(POST_GUILD);
                stage.focus = actor[INP_POST_ADDRESS].getChildAt(1);
                actor[INP_POST_ADDRESS].getChildAt(1).text = "";
                actor[INP_POST_TEXT].getChildAt(1)
                    .text = texts[(TXT_POST_FORWARD + 2)].split("%1")
                    .join(reply_address).split("%2").join(forward_text)
                    .split("#").join(chr(13));
                if (text_dir == "right"){
                    if (actor[INP_POST_SUBJECT].getChildAt(1).text
                            .find(texts[(TXT_POST_FORWARD + 1)]) == -1){
                        actor[INP_POST_SUBJECT].getChildAt(1)
                            .text = ((reply_subject + " ")
                                     + texts[(TXT_POST_FORWARD + 1)]);
                    };
                    make_right_text_area(INP_POST_ADDRESS, 1);
                    make_right_text_area(INP_POST_SUBJECT, 1);
                    make_right_text_area(INP_POST_TEXT, 1);
                } else {
                    if (actor[INP_POST_SUBJECT].getChildAt(1).text
                            .find(texts[(TXT_POST_FORWARD + 1)]) == -1){
                        actor[INP_POST_SUBJECT].getChildAt(1)
                            .text = ((texts[(TXT_POST_FORWARD + 1)] + " ")
                                     + reply_subject);
                    };
                };
            };
            break;
        if case(POST_VIEWFIGHT:
            par = tmp_battle_info.split("#");
            post_fight_mode = True;
            show_fight_screen(par[0].split("/"), par[1].split("/"),
                              (par[6] == "1"), par[2].split("/"),
                              (par[5] == "2"),
                              ((par[3] + "/") + par[4]).split("/"),
                              int(par[7]), int(par[8]), (par[5] == "3"), True);
            break;
        default:
            if (post_sel > 0){
                send_action(ACT_POST_READ, ((post_sel + post_scroll) - 1));
            };
    };
    '''
    print evt, actor_id


def album_clear():
    '''
    var i;
    i = 0;
    while (i < 4) {
        hide((ALBUM_MONSTER_FRAME + i));
        set_cnt((ALBUM_MONSTER + i), C_EMPTY);
        set_cnt((ALBUM_WEAPON_1 + i), C_EMPTY);
        set_cnt((ALBUM_WEAPON_2 + i), C_EMPTY);
        set_cnt((ALBUM_WEAPON_3 + i), C_EMPTY);
        set_cnt((ALBUM_WEAPON_4 + i), C_EMPTY);
        set_cnt((ALBUM_WEAPON_5 + i), C_EMPTY);
        actor[(ALBUM_WEAPON_1 + i)].alpha = 1;
        actor[(ALBUM_WEAPON_2 + i)].alpha = 1;
        actor[(ALBUM_WEAPON_3 + i)].alpha = 1;
        actor[(ALBUM_WEAPON_4 + i)].alpha = 1;
        actor[(ALBUM_WEAPON_5 + i)].alpha = 1;
        set_cnt((ALBUM_WEAPON_EPIC + i), C_EMPTY);
        actor[(LBL_ALBUM_HEADING + i)].text = "";
        actor[(LBL_ALBUM_HINT + i)].text = "";
        i++;
    };
    '''
    pass


def get_advent():
    '''
    var tmpNow:Date;
    var tmpAdventEnd:Date;
    var tmpDate:Date;
    var advent;
    Switch (lang_code){
        if case("de":
            break;
        default:
            return (0);
    };
    tmpNow = new Date();
    tmpAdventEnd = new Date(tmpNow.getFullYear(), 11, 27);
    tmpDate = new Date(tmpNow.getFullYear(), 11, 24);
    while (tmpDate.getDay() != 0) {
        tmpDate.setDate((tmpDate.getDate() - 1));
    };
    if (tmpNow.getTime() < tmpAdventEnd.getTime()){
        advent = 4;
        while (advent >= 1) {
            trace("Advent", advent, tmpNow.tostr());
            if (tmpNow.getTime() >= tmpDate.getTime()){
                return (advent);
            };
            tmpDate.setDate((tmpDate.getDate() - 7));
            advent--;
        };
    };
    return (0);
    '''
    pass


def refresh_time_bar(offer_time=0):
    '''
    var tmpTime:* = NaN;
    var tmpText:* = None;
    var offer_time = offer_time;
    var tmpX:* = 0;
    if (offer_time < 0){
        if ((Number(savegame[SG_TIMEBAR]) + offer_time) < 0){
            offer_time = 0;
        };
    };
    var _local3 = actor[TIMEBAR_FILL];
    with (_local3) {
        if (offer_time < 0){
            tmpX = (((Number(savegame[SG_TIMEBAR]) + offer_time) / 6000) * 555)
        } else {
            tmpX = ((Number(savegame[SG_TIMEBAR]) / 6000) * 555);
        };
        width = int(tmpX);
        tmpX = int((x + width));
    };
    _local3 = actor[TIMEBAR_FILL];
    with (_local3) {
        if (offer_time < 0){
            width = int(((-(offer_time) / 6000) * 555));
            x = tmpX;
        } else {
            width = int(((offer_time / 6000) * 555));
            x = tmpX;
        };
    };
    tmpTime = int(savegame[SG_TIMEBAR]);
    tmpText = "";
    if (tmpTime > (60 * 60)){
        tmpText = (tmpText + (str(int((tmpTime / (60 * 60)))) + ":"));
        tmpTime = (tmpTime % (60 * 60));
        if ((tmpTime / 60) < 10){
            tmpText = (tmpText + "0");
        };
    };
    tmpText = (tmpText + (str(int((tmpTime / 60))) + ":"));
    tmpTime = (tmpTime % 60);
    if (tmpTime < 10){
        tmpText = (tmpText + "0");
    };
    tmpText = (tmpText + str(int(tmpTime)));
    if (text_dir == "right"){
        tmpText = ((tmpText + " :") + texts[TXT_AUSDAUER]);
    } else {
        tmpText = ((texts[TXT_AUSDAUER] + ": ") + tmpText);
    };
    if (offer_time != 0){
        tmpText = (tmpText + (" (" + (((offer_time > 0)) ? "+" : "-")));
        tmpText = (tmpText + (str(int((math.abs(offer_time) / 60))) + ":"));
        if ((math.abs(offer_time) % 60) < 10){
            tmpText = (tmpText + "0");
        };
        tmpText = (tmpText + (str(int((math.abs(offer_time) % 60))) + ")"));
    };
    tmpTime = Number(savegame[SG_TIMEBAR]);
    if (text_dir == "right"){
        tmpText = (" :" + texts[TXT_AUSDAUER]);
        tmpText = (str(Number((tmpTime / 60)).toFixed(1))
                   .split(".0")[0] + tmpText);
    } else {
        tmpText = (texts[TXT_AUSDAUER] + ": ");
        tmpText = (tmpText + str(Number((tmpTime / 60)).toFixed(1))
                   .split(".0")[0]);
    };
    if (offer_time != 0){
        if (text_dir == "right"){
            tmpText = (((((offer_time > 0)) ? "+" : "-") + ") ") + tmpText);
            tmpText = (("(" + str(Number((math.abs(offer_time) / 60))
                       .toFixed(1)).split(".0")[0]) + tmpText);
        } else {
            tmpText = (tmpText + (" (" + (((offer_time > 0)) ? "+" : "-")));
            tmpText = (tmpText + (str(Number((math.abs(offer_time) / 60))
                       .toFixed(1)).split(".0")[0] + ")"));
        };
    };
    _local3 = actor[LBL_TIMEBAR_TEXT];
    with (_local3) {
        text = tmpText;
        x = int((TIMEBAR_LABEL_X - (text_width / 2)));
    };
    '''
    print offer_time


def arabize(actor_id):
    '''
    var i;
    var ii;
    var lines:Array;
    var thisStr:String;
    var nextStr:String;
    var dontCrash;
    lines = list();
    dontCrash = 0;
    if (text_dir != "right"){
        return;
    };
    actor[actor_id].width = (actor[actor_id].width - 5);
    i = 0;
    while (i < actor[actor_id].numLines) {
        lines.append(actor[actor_id].getLineText(i));
        i++;
    };
    actor[actor_id].width = (actor[actor_id].width + 5);
    dontCrash = 0;
    i = 0;
    while (i < lines.length) {
        while (((!((lines[i][-1:] == " "))) and ((lines[i].length > 0)))) {
            if (lines[i].length <= 1){
                break;
            };
            if ((((i == (lines.length - 1))) and ((lines[i].length > 0)))){
                lines.append(" ");
            };
            lines[(i + 1)] = (lines[i][-1:] + lines[(i + 1)]);
            lines[i] = lines[i][0: (lines[i].length - 1)]
            dontCrash++;
            if (dontCrash > 3000){
                break;
            };
        };
        i++;
    };
    actor[actor_id].text = "";
    i = 0;
    while (i < lines.length) {
        actor[actor_id].text = ((lines[i] + chr(13)) + actor[actor_id].text);
        i++;
    };
    '''
    print actor_id


def get_spend_amount():
    '''
    var amount;
    amount = 1;
    if (int(savegame[SG_LEVEL]) >= 120){
        amount = 100;
    } else {
        if (int(savegame[SG_LEVEL]) >= 100){
            amount = 50;
        } else {
            if (int(savegame[SG_LEVEL]) >= 50){
                amount = 10;
            } else {
                if (int(savegame[SG_LEVEL]) >= 25){
                    amount = 5;
                };
            };
        };
    };
    return (str(amount));
    '''
    pass


def add_suggest_names(add_array):
    '''
    var i;
    if (!(add_array is Array)){
        add_array = [add_array];
    };
    i = 0;
    while (i < add_array.length) {
        if (suggestNames.find(add_array[i]) == -1){
            suggestNames.append(add_array[i]);
        };
        i++;
    };
    i = 0;
    while (i < suggestNames.length) {
        if (suggestNames[i].lower() == actor[INP['NAME']].getChildAt(1)
                .text.lower()){
            suggestNames.splice(i, 1);
            i--;
        };
        i++;
    };
    '''
    print add_array


def get_actor_id(actor_obj, i_start=0, i_ende=-1):
    '''
    var i;
    var res;
    res = C_EMPTY;
    i = i_start;
    while (i <= ((i_ende)==-1) ? (actor.length - 1) : i_ende) {
        if (actor_obj == actor[i]){
            res = i;
            break;
        };
        i++;
    };
    return (res);
    '''
    print actor_obj, i_start, i_ende


def get_actor_name(actor_id=0):
    '''
    var loader:* = None;
    var actor_id = actor_id;
    loader = new URLLoader();
    if (!(actorName is Array)){
        var ConstFileLoaded:* = function (evt:Event):
            var str_data:String;
            var constName:String;
            var i;
            var c;
            var tmp_str:String;
            str_data = loader.data;
            constName = "";
            var equals:Boolean;
            tmp_str = "";
            var last_index;
            i = 0;
            while (i < (str_data.length - 1)) {
                c = str_data.charCodeAt(i);
                Switch (c){
                    if case(10:
                    if case(13:
                        if (constName != ""){
                            actorName[int(tmp_str[1:])] = constName;
                        };
                        constName = "";
                        tmp_str = "";
                        break;
                    if case(61:
                        if (tmp_str[0: 14].lower() == "_global const "){
                            constName = tmp_str[14] (tmp_str.length - 15)]
                            tmp_str = "";
                        };
                        break;
                    default:
                        tmp_str = (tmp_str + str_data[i]);
                };
                i++;
            };
            pending_debug_file = False;
            loader_complete(evt);
        };
        actorName = list();
        var _local3 = loader;
        with (_local3) {
            data_format = URLLoaderdataFormat.TEXT;
            add_event_listener(Event.COMPLETE, ConstFileLoaded);
            load(new URLRequest("constants.as"));
        };
        pending_loaders = (pending_loaders + 1);
        pending_debug_file = True;
    };
    return (actorName[actor_id]);
    '''
    print actor_id


def crest_move_fn():
    '''
    if (actor[GILDE_CREST].y > crestMoveDest){
        actor[GILDE_CREST].y = (actor[GILDE_CREST].y - 5);
    } else {
        if (actor[GILDE_CREST].y < crestMoveDest){
            actor[GILDE_CREST].y = (actor[GILDE_CREST].y + 5);
        } else {
            crestMoveTimer.stop();
        };
    };
    '''
    pass


def get_random_crest():
    '''
    var i;
    var result:Array;
    var guildChecksum:* = 0;
    result = list();
    i = 0;
    while (i < crestElementPos.length) {
        result.append(int((random.random() * crestElementPos[i][4])));
        i++;
    };
    return (result);
    '''
    pass


def set_default_crest():
    '''
    var i:* = 0;
    var lastResult:* = 0;
    var GuildRandom:* = function (val){
        var result;
        result = math.abs(((last_guild_data[0] + lastResult) % val));
        lastResult = result;
        return (result);
    };
    lastResult = 0;
    crest = list();
    i = 0;
    while (i < crestElementPos.length) {
        crest.append(int(GuildRandom(crestElementPos[i][4])));
        i = (i + 1);
    };
    i = 0;
    while (i < crestColor.length) {
        crestColor[i] = GuildRandom(heraldicColors.length);
        i = (i + 1);
    };
    load_crest();
    '''
    pass


def old_crest_str():
    '''
    var result:* = None;
    var i:* = 0;
    var dec2hex:* = function (d):String{
        var c:Array;
        var l;
        var r;
        c = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
            "D", "E", "F"];
        if (d > 0xFF){
            d = 0xFF;
        };
        l = (d / 16);
        r = (d % 16);
        return ((c[l] + c[r]));
    };
    result = "";
    i = 0;
    while (i < crest.length) {
        result = (result + dec2hex(crest[i]));
        i = (i + 1);
    };
    i = 0;
    while (i < crestColor.length) {
        result = (result + dec2hex(crestColor[i]));
        i = (i + 1);
    };
    return (result);
    '''
    return ''


def set_crest_str(in_str):
    '''
    var i;
    var hex:String;
    var val;
    i = 0;
    while (i < crest.length) {
        hex = in_str[0: 2]
        in_str = in_str[2: 0]
        val = int(("0x" + hex));
        if (val < 0){
            val = 0;
        };
        if (val >= crestElementPos[i][4]){
            val = 0;
        };
        crest[i] = val;
        i++;
    };
    i = 0;
    while (i < crestColor.length) {
        hex = in_str[0: 2]
        in_str = in_str[2:]
        val = int(("0x" + hex));
        if (val < 0){
            val = 0;
        };
        if (val >= heraldicColors.length){
            val = 0;
        };
        crestColor[i] = val;
        i++;
    };
    load_crest();
    '''
    print in_str


def load_crest():
    '''
    var i:* = 0;
    var newLoad:* = False;
    var url:* = None;
    var localActorID:* = 0;
    var tmpFltFigure:* = None;
    var tmpFltShield:* = None;
    var tmpFlt:* = None;
    tmpFltFigure = new ColorMatrixFilter([heraldicColors[crestColor[3]][0], 0,
                                         0, 0, 0,
                                         heraldicColors[crestColor[3]][1], 0,
                                         0, 0, 0,
                                         heraldicColors[crestColor[3]][2],
                                         0, 0, 0, 0, 0, 0, 0, 1, 0]);
    tmpFltShield = new ColorMatrixFilter([0, heraldicColors[crestColor[1]][0],
                                         heraldicColors[crestColor[2]][0],
                                         0, 0, 0,
                                         heraldicColors[crestColor[1]][1],
                                         heraldicColors[crestColor[2]][1],
                                         0, 0, 0,
                                         heraldicColors[crestColor[1]][2],
                                         heraldicColors[crestColor[2]][2],
                                         0, 0, 0, 0, 0, 1, 0]);
    i = 1;
    while (i < 4) {
        tmpFlt = new ColorMatrixFilter([0, heraldicColors[crestColor[i]][0],
                                       0, 0, 0, 0,
                                       heraldicColors[crestColor[i]][1], 0, 0,
                                       0, 0, heraldicColors[crestColor[i]][2],
                                       0, 0, 0, 0, 0, 0, 1, 0]);
        actor[(GILDE_CREST_COLOR_FILLIN + i)].filters = [tmpFlt];
        enable_popup((GILDE_CREST_COLOR + i),
                     texts[(TXT_CREST_TINCTUREBOXES + i)].split("%1")
                     .join(texts[(TXT_CREST_TINCTURES + crestColor[i])]));
        i = (i + 1);
    };
    i = 0;
    while (i < crestElementPos.length) {
        localActorID = (GILDE_CREST + i);
        url = (((((img_url[img_url_index]
               + "res/gfx/scr/gilde/crest/tiles/crest_") + str((i + 1))) + "_")
                + str((crest[i] + 1))) + ".png");
        newLoad = !((actorURL[localActorID] == url));
        actorURL[localActorID] = url;
        if (newLoad){
            actorLoaded[localActorID] = 0;
            load(localActorID);
        };
        if (i == 2){
            url = (((((img_url[img_url_index]
                   + "res/gfx/scr/gilde/crest/tiles/crest_")
                    + str((i + 1))) + "_") + str((crest[i] + 1)))
                        + "_color.png");
            newLoad = !((actorURL[GILDE_CREST_SHIELDCOLOR] == url));
            actorURL[GILDE_CREST_SHIELDCOLOR] = url;
            if (newLoad){
                actorLoaded[GILDE_CREST_SHIELDCOLOR] = 0;
                load(GILDE_CREST_SHIELDCOLOR);
            };
            actor[GILDE_CREST_SHIELDCOLOR].filters = [tmpFltShield];
        };
        if (i == 3){
            var _local2 = actor[LBL_GILDE_CREST_INSCRIPTION];
            with (_local2) {
                y = 210;
                Switch ((crest[i] + 1)){
                    if case(7:
                    if case(1:
                    if case(4:
                    if case(5:
                    if case(8:
                    if case(9:
                        y = (y - 2);
                        break;
                    if case(3:
                    if case(6:
                        y = (y - 1);
                        break;
                    if case(2:
                    if case(10:
                    if case(11:
                    if case(12:
                        break;
                };
            };
        };
        if (i == 6){
            if (selecterCrestElement == i){
                actor[(GILDE_CREST + i)].filters = [tmpFltFigure,
                    Filter_CrestSelected];
            } else {
                actor[(GILDE_CREST + i)].filters = [tmpFltFigure];
            };
        } else {
            if (selecterCrestElement == i){
                actor[(GILDE_CREST + i)].filters = [Filter_CrestSelected];
            } else {
                actor[(GILDE_CREST + i)].filters = [];
            };
        };
        i = (i + 1);
    };
    if (selecterCrestElement >= 0){
        actor[LBL_GILDE_CREST_ELEMENT].text = texts[(TXT_CREST_ELEMENT
                 + selecterCrestElement)].split("%1")
                .join(str((crest[selecterCrestElement] + 1)))
                .split("%2")
                .join(str(crestElementPos[selecterCrestElement][4]));
        actor[LBL_GILDE_CREST_ELEMENT].x = ((GILDE_GEBAEUDE_X + 120)
                        - (actor[LBL_GILDE_CREST_ELEMENT].text_width / 2));
    };
    '''
    pass


def clickchat_line(evt):
    '''
    var lineText:String;
    var chatAuthor:*;
    if ((evt is MouseEvent)){
        lineText = evt.target.text;
    } else {
        lineText = evt;
    };
    if (crestSuggestion[lineText]){
        remove(GILDE_GEBAEUDE);
        add(GILDE_CREST);
        if (actor[GILDE_CREST].y == GILDE_GEBAEUDE_Y){
            set_alpha(GILDE_CREST_CONTROLS, 1);
            add(GILDE_CREST_CONTROLS);
        } else {
            selecterCrestElement = -1;
        };
        if (my_own_rank == 1){
            crestSuggested = True;
            set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_APPLY]);
        } else {
            crestSuggested = False;
            set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST]);
        };
        set_crest_str(crestSuggestion[lineText]);
        return;
    };
    chatAuthor = lineText[6:]
    if (chatAuthor.find(":") != -1){
        chatAuthor = chatAuthor[0: chatAuthor.find(":")]
        if (chatAuthor.length <= 20){
            if (chatAuthor.find(" > ") == -1){
                if (actor[INP_GILDE_CHAT].getChildAt(0).text == ""){
                    actor[INP_GILDE_CHAT].getChildAt(0).text = (("/w "
                                + chatAuthor.split(" ").join("#")) + " ");
                };
                actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                     actor[INP_GILDE_CHAT].getChildAt(0).text.length,
                     actor[INP_GILDE_CHAT].getChildAt(0).text.length);
            };
        };
    };
    stage.focus = actor[INP_GILDE_CHAT].getChildAt(0);
    '''
    print evt


def arbeiten_slider_change(value):
    '''
    var txtWorkDur:String;
    if (texts[TXT_ARBEIT_TEXT3] == ""){
        txtWorkDur = texts[TXT_ARBEIT_TEXT2].split("%hours")
            .join(str(value)).split("%reward")
            .join(Geld((value * stundenlohn)));
        if (texts[TXT_WORK_FINISH]){
            actor[LBL_SCR_ARBEITEN_TEXT2].text = texts[TXT_WORK_FINISH]
            .split("%1").join(txtWorkDur).split("%2")
            .join(time_str((int((game_time.getTime() / 1000))
                  + (((value + 1) * 60) * 60)), True));
        } else {
            actor[LBL_SCR_ARBEITEN_TEXT2].text = txtWorkDur;
        };
    } else {
        actor[LBL_SCR_ARBEITEN_TEXT2].text = ((((((value + " ")
          + texts[TXT_ARBEIT_TEXT2]) + " ") + Geld((value * stundenlohn)))
            + " ") + texts[TXT_ARBEIT_TEXT3]);
    };
    '''
    print value


def double_click_handler(disp_obj, fn_click, fn_double_click):
    '''
    var dblClickTimer:* = None;
    var waiting:* = False;
    var tmpEvt:* = None;
    var dblClickTimerEvent:* = None;
    var disp_obj:* = disp_obj;
    var fn_click:* = fn_click;
    var fn_double_click:* = fn_double_click;
    var dblClickEvent:* = function (evt:MouseEvent){
        if (waiting){
            fn_click(tmpEvt);
            fn_double_click(evt);
            dblClickTimer.stop();
            dblClickTimer.remove_event_listener(TimerEvent.TIMER,
                                                dblClickTimerEvent);
            waiting = False;
        } else {
            tmpEvt = evt;
            dblClickTimer.add_event_listener(TimerEvent.TIMER,
                                             dblClickTimerEvent);
            dblClickTimer.start();
            waiting = True;
        };
    };
    dblClickTimerEvent = function (evt:TimerEvent){
        waiting = False;
        dblClickTimer.remove_event_listener(TimerEvent.TIMER,
                                            dblClickTimerEvent);
        fn_click(tmpEvt);
    };
    dblClickTimer = new Timer(300, 1);
    waiting = False;
    var _local5 = disp_obj;
    with (_local5) {
        mouse_enabled = True;
        add_event_listener(MouseEvent.MOUSE_DOWN,
                           dblClickEvent);
    };
    '''
    print disp_obj, fn_click, fn_double_click


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


def sing_plur(inp_text, amount, sep="*"):
    '''
    var tmp_array:Array;
    tmp_array = inp_text.split(sep);
    if (tmp_array.length == 4){
        return (((tmp_array[0] +
                tmp_array[(((amount == 1)) ? 1 : 2)]) + tmp_array[3]));
    };
    if (tmp_array.length == 5){
        return (((tmp_array[0]
                + tmp_array[(((amount == 1))
                         ? 1 : (((amount == 2)) ? 2 : 3))]) + tmp_array[4]));
    };
    if (tmp_array.length == 6){
        return (((tmp_array[0]
                + tmp_array[(((amount == 1))
                             ? 1 : (((amount == 2))
                                    ? 2 : (((amount <= 10)) ? 3 : 4)))])
                                        + tmp_array[4]));
    };
    return (tmp_array.join(""));
    '''
    print inp_text, amount, sep


def animate_ach(actor_id, y_level=635, ach_ani_pow=-10):
    '''
    var AchAniTimer:* = None;
    var actor_id:* = actor_id;
    var y_level:Number = y_level;
    var ach_ani_pow = ach_ani_pow;
    var AchAniEvent:* = function (evt:Event){
        var evt:* = evt;
        var _local3 = actor[actor_id];
        with (_local3) {
            y = (y + ach_ani_pow);
            ach_ani_pow = (ach_ani_pow + 2);
            if (y >= y_level){
                y = y_level;
                ach_ani_pow = (ach_ani_pow * -0.5);
                if (math.abs(ach_ani_pow) <= 3){
                    y = y_level;
                    AchAniTimer.remove_event_listener(TimerEvent.TIMER,
                                                      AchAniEvent);
                    AchAniTimer.stop();
                    return;
                };
            };
        };
    };
    AchAniTimer = new Timer(50);
    var AchAniStep:* = 0;
    var _local5 = AchAniTimer;
    with (_local5) {
        add_event_listener(TimerEvent.TIMER, AchAniEvent);
        start();
    };
    '''
    print actor_id, y_level, ach_ani_pow


def do_achievements(save):
    '''
    var i;
    var achPop:Array;
    var achAusfM:String;
    var achAusfF:String;
    var achAusf;
    var achCurrentGrade:String;
    var OneUp:Boolean;
    remove(CHAR_ACH);
    achAusfM = "";
    achAusfF = "";
    achAusf = 0;
    achCurrentGrade = "";
    OneUp = False;
    i = 0;
    while (i < ((buffed_mode) ? 7 : 8)) {
        achAusf = ach_level(save, (i % 8), 1);
        add(((CHAR_ACH + i) + (achAusf * 8)));
        if (old_ach[(i % 8)] < 0){
            old_ach[(i % 8)] = -(old_ach[(i % 8)]);
            animate_ach(((CHAR_ACH + i) + (achAusf * 8)));
            OneUp = True;
        };
        Switch (achAusf){
            if case(0:
                achAusfM = "";
                achAusfF = "";
                achCurrentGrade = texts[TXT_ACH_5];
                break;
            default:
                achAusfM = (texts[((TXT_ACH_5 + (achAusf * 2)) - 1)] + " ");
                achAusfF = (texts[(TXT_ACH_5 + (achAusf * 2))] + " ");
                achCurrentGrade = texts[(TXT_ACH_2 + (i % 8))].split("%1")
                    .join(str(ach_level(save, (i % 8), 0))).split("%2")
                    .join(str(ach_level(save, (i % 8), 4)));
                if (i == 6){
                    achCurrentGrade = texts[TXT_NEW_HONOR_ACH]
                        .split("%1").join(str(ach_level(save, (i % 8), 0)))
                        .split("%2").join(str(ach_level(save, (i % 8), 4)));
                };
        };
        achPop = list();
        if (texts[(TXT_ACH_4 + 4)]){
            achPop[achPop.length] = texts[(TXT_ACH_1 + (i % 8))]
                .split("%1").join(achAusfM).split("%2")
                .join(achAusfF).split("%3").join("");
        } else {
            achPop[achPop.length] = texts[(TXT_ACH_1 + (i % 8))]
                .split("%1").join(achAusfM).split("%2")
                .join(achAusfF).split("%3").join(texts[(TXT_ACH_4 + 3)]
                     .split("%1").join(friend_link));
        };
        achPop[achPop.length] = sing_plur(achCurrentGrade,
                                         ach_level(save, (i % 8), 4));
        if (i == 1){
            if (save[SG['PLAYER_ID']] == savegame[SG['PLAYER_ID']]){
                if (tower_level > 0){
                    achPop[achPop.length] = sing_plur(texts[(TXT_ACH_2 + 8)].
                                                     split("%1")
                                                     .join(str(tower_level)),
                                                     tower_level);
                };
            } else {
                if (playerTowerLevel > 0){
                    achPop[achPop.length] = sing_plur(texts[(TXT_ACH_2 + 8)].
                                                     split("%1")
                                                 .join(str(playerTowerLevel)),
                                                 playerTowerLevel);
                };
            };
        };
        if (ach_level(save, (i % 8), 2) > 0){
            if (i == 6){
                achPop[achPop.length] = sing_plur(texts[TXT_NEW_HONOR_ACH2]
                                                 .split("%1")
                                                 .join(str(ach_level(
                                                       save, (i % 8), 2)))
            .split("%2").join(texts[(TXT_ACH_4 + (((achAusf == 0)) ? 1 : 2))]),
            ach_level(save, (i % 8), 2));
            } else {
                achPop[achPop.length] = sing_plur(texts[(TXT_ACH_3 + (i % 8))]
                                                 .split("%1")
                .join(str(ach_level(save, (i % 8), 2))).split("%2")
                .join(texts[(TXT_ACH_4 + (((achAusf == 0)) ? 1 : 2))]),
                ach_level(save, (i % 8), 2));
            };
        };
        if (ach_level(save, (i % 8), 3) > 0){
            achPop[achPop.length] = texts[TXT_ACH_4]
                .split("%1").join(str(ach_level(save, (i % 8), 3)));
        };
        enable_popup((CHAR_ACH + i + (ach_level(save, (i % 8), 1) * 8)),
                     achPop);
        i++;
    };
    return (OneUp);
    '''
    print save


def mirror_ani_fn():
    '''
    var i;
    mirror_fade_amount = (mirror_fade_amount - 0.002);
    if (mirror_fade_amount <= 0){
        mirror_fade_amount = 0;
        mirror_ani_timer.stop();
    };
    mirrorAniStep = (mirrorAniStep + 0.1);
    i = 0;
    while (i < 13) {
        actor[(MIRROR_PIECE + i)].alpha = (0.3 + (math.sin((mirrorAniStep
                                           + (((i / 13) * 2) * math.pi)))
                                        * mirror_fade_amount));
        i++;
    };
    '''
    pass


def trim_too_long(actor_id_obj, max_width):
    '''
    var tmp_str:* = None;
    var remainLength:* = 0;
    var actor_id:* = 0;
    var Shortened:* = False;
    var actor_id_obj:* = actor_id_obj;
    var max_width:* = max_width;
    Shortened = False;
    var _local4 = (((actor_id_obj is int))
                   ? actor[actor_id_obj] : actor_id_obj);
    with (_local4) {
        tmp_str = text;
        remainLength = tmp_str.length;
        while (text_width > max_width) {
            remainLength--;
            Shortened = True;
            if (text_dir == "right"){
                text = ("..." + tmp_str[-(remainLength): remainLength]);
                if (tmp_str.find("]") >= 0){
                    text = ("[" + text);
                };
            } else {
                text = (tmp_str[0: remainLength] + "...");
                if (tmp_str.find("[") >= 0){
                    text = (text + "]");
                };
            };
        };
    };
    if ((actor_id_obj is int)){
        if (Shortened){
            enable_popup(int(actor_id_obj), tmp_str);
        } else {
            enable_popup(int(actor_id_obj));
        };
    };
    return (((Shortened) ? tmp_str : ""));
    '''
    print actor_id_obj, max_width
    return ''


def check_wrong_page(correct_act):
    '''
    if (correct_act != lastAct){
        if (correct_act == ACT_SCREEN_TAVERNE){
            Switch (lastAct){
                if case(ACT_SCREEN_ARENA:
                    if (!has_mirror){
                        error_message(texts[TXT_ERROR_TAVERNE_ARENA]);
                    };
                    break;
                if case(ACT_SCREEN_ARBEITEN:
                    error_message(texts[TXT_ERROR_TAVERNE_ARBEITEN]);
                    break;
                if case(ACT_SCREEN_WELTKARTE:
                    if (!has_mirror){
                        error_message(texts[TXT_ERROR_TAVERNE_MAINQUEST]);
                    };
                    break;
            };
        } else {
            if (correct_act == ACT_SCREEN_ARBEITEN){
                Switch (lastAct){
                    if case(ACT_SCREEN_ARENA:
                        error_message(texts[TXT_ERROR_ARBEITEN_ARENA]);
                        break;
                    if case(ACT_SCREEN_TAVERNE:
                        error_message(texts[TXT_ERROR_ARBEITEN_TAVERNE]);
                        break;
                    if case(ACT_SCREEN_WELTKARTE:
                        error_message(texts[TXT_ERROR_ARBEITEN_MAINQUEST]);
                        break;
                };
            };
        };
    };
    '''
    print correct_act


def make_right_text_area(actor_id, child=0, create_handler=True):
    '''
    var tmp_text_format:* = None;
    var actor_id:* = actor_id;
    var child = child;
    var create_handler:Boolean = create_handler;
    var makeRightHandler:* = function (evt:Event){
        make_right_text_area(actor_id, child, False);
    };
    if (text_dir != "right"){
        return;
    };
    tmp_text_format = actor[actor_id].getChildAt(child).default_text_format;
    tmp_text_format.align = "right";
    if (!actor[actor_id].hasHandler){
        if (create_handler){
            actor[actor_id].hasHandler = True;
        };
    };
    actor[actor_id].getChildAt(child).default_text_format = tmp_text_format;
    actor[actor_id].getChildAt(child).setTextFormat(tmp_text_format);
    '''
    print actor_id, child, create_handler


def display_inventory(save=None, no_prices=False, tower_mode=False,
                      copy_cat_id_raw=0, witch_mode=False):
    '''
    var i:* = 0;
    var ii:* = 0;
    var hide_back_pack:* = False;
    var boostPrice:* = 0;
    var boostGold:* = 0;
    var boostSilver:* = 0;
    var preisX:* = 0;
    var popupLines:* = None;
    var tempBonus:* = 0;
    var tmpHealth:* = 0;
    var potionDuration:* = None;
    var copyCatId:* = None;
    var popupLinesCpc:* = None;
    var DamageReductionCpc:* = 0;
    var DamageReductionMaxCpc:* = 0;
    var tmpKritische:* = NaN;
    var tmpDamageMin:* = 0;
    var tmpDamageMax:* = 0;
    var tmpDamageFactor:* = NaN;
    var tmpLifeFactor:* = NaN;
    var SchadenLblID:* = 0;
    var SchadenID:* = 0;
    var tmpItmClass:* = 0;
    var tmpItmPic:* = 0;
    var hasEpic:* = False;
    var DamageReduction:* = 0;
    var DamageReductionMax:* = 0;
    var save:* = save;
    var no_prices:Boolean = no_prices;
    var tower_mode:Boolean = tower_mode;
    var copy_cat_id_raw = copy_cat_id_raw;
    var witch_mode:Boolean = witch_mode;
    var GetBoostPrice:* = function (boostCount):
        return (int(TrueAttPreis[boostCount]));
    };
    hide_back_pack = False;
    tempBonus = 0;
    tmpHealth = 0;
    var hours:* = 0;
    potionDuration = "";
    copyCatId = 0;
    if (tower_mode){
        copyCatId = (TSG_COPYCATS + (COPYCAT * copy_cat_id_raw));
        i = 0;
        while (i < 3) {
            if (i == copy_cat_id_raw){
                if (int(save[(copyCatId + CPC_LEVEL)])
                        >= int(savegame[SG_LEVEL])){
                    hide((TOWER_STEIGERN1 + i));
                    hide((LBL_TOWER_BOOSTPRICELABEL + i));
                } else {
                    show((TOWER_STEIGERN1 + i));
                    show((LBL_TOWER_BOOSTPRICELABEL + i));
                };
            } else {
                hide((TOWER_STEIGERN1 + i));
                hide((LBL_TOWER_BOOSTPRICELABEL + i));
            };
            i = (i + 1);
        };
        i = 0;
        while (i < 5) {
            ii = 0;
            while (ii < 12) {
                save[((TSG_LOOT_SACK + (i * 12)) + ii)] = savegame[
                    ((SG_BACKPACK_OFFS + (i * 12)) + ii)];
                ii = (ii + 1);
            };
            i = (i + 1);
        };
        if (save[(copyCatId + CPC_LEVEL)] != 0){
            actor[LBL_SCR_CHAR_NAME].text = texts[
                (TXT_COPYCAT_NAME + copy_cat_id_raw)];
        } else {
            actor[LBL_SCR_CHAR_NAME].text = "";
        };
        actor[SCR_CHAR_NAME].x = ((SCR_CHAR_CHARX + 128)
                      - int((actor[LBL_SCR_CHAR_NAME].text_width / 2)));
        var _local7 = actor[SCR_CHAR_EXPBAR];
        with (_local7) {
            width = int(((Number(save[(copyCatId + CPC_GOLD_STOLEN)])
                        / Number(save[(copyCatId + CPC_GOLD_STOLEN_NEXT)]))
                            * 254));
        };
        i = 0;
        while (i < 3) {
            hide((TOWER_NO_PORTRAIT + i));
            hide((TOWER_PORTRAIT + i));
            _local7 = actor[(TOWER_NO_PORTRAIT + i)];
            with (_local7) {
                scaleX = 0.86;
                scaleY = 0.86;
            };
            _local7 = actor[(TOWER_PORTRAIT + i)];
            with (_local7) {
                scaleX = 0.86;
                scaleY = 0.86;
            };
            i = (i + 1);
        };
        _local7 = actor[LBL_TOWER_EXPLABEL];
        with (_local7) {
            if (save[(copyCatId + CPC_LEVEL)] != 0){
                show((TOWER_PORTRAIT + copy_cat_id_raw));
                if (text_dir == "right"){
                    text = ((save[(copyCatId + CPC_LEVEL)] + " ")
                            + texts[TXT_HALL_LIST_COLUMN_4]);
                } else {
                    text = ((texts[TXT_HALL_LIST_COLUMN_4] + " ")
                            + save[(copyCatId + CPC_LEVEL)]);
                };
            } else {
                show((TOWER_NO_PORTRAIT + copy_cat_id_raw));
                text = "";
            };
            if (tower_levelLabelPos > (SCR_CHAR_CHARX + 3)){
                x = ((SCR_CHAR_CHARX + 127)
                     - int((actor[LBL_TOWER_EXPLABEL].text_width / 2)));
            } else {
                x = (SCR_CHAR_CHARX + 3);
            };
        };
        popupLinesCpc = list();
        popupLinesCpc.append([POPUP_BEGIN_LINE, ((texts[163] + ": ")
                             + save[(copyCatId + CPC_ARMOR)]), POPUP_END_LINE])
        DamageReductionCpc = int((Number(save[(copyCatId + CPC_ARMOR)])
                                 / Number(save[(copyCatId + CPC_LEVEL)])));
        DamageReductionMaxCpc = 50;
        Switch (int(save[(copyCatId + CPC_CLASS)])){
            if case(2:
                DamageReductionMaxCpc = 10;
                break;
            if case(3:
                DamageReductionMaxCpc = 25;
                break;
        };
        if (DamageReductionCpc > DamageReductionMaxCpc){
            DamageReductionCpc = DamageReductionMaxCpc;
        };
        if (text_dir == "right"){
            popupLinesCpc[popupLinesCpc.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib, ((((((((("(" + texts[TXT_MAX]) + " -")
                                    + str(DamageReductionMaxCpc)) + "%) ")
                + str(DamageReductionCpc)) + "% :")
                + save[(copyCatId + CPC_LEVEL)]) + " ")
                + texts[TXT_RUESTUNG_SUM_HINT]), POPUP_END_LINE];
        } else {
            popupLinesCpc[popupLinesCpc.length] = [POPUP_BEGIN_LINE,
            FontFormatAttrib, (((((((((texts[TXT_RUESTUNG_SUM_HINT] + " ")
                                + save[(copyCatId + CPC_LEVEL)]) + ": -")
                                + str(DamageReductionCpc))
                                + "% (") + texts[TXT_MAX]) + " -")
                                + str(DamageReductionMaxCpc)) + "%)"),
                    POPUP_END_LINE];
        };
        if (texts[TXT_SHIELD_FORMULA]){
            popupLinesCpc[popupLinesCpc.length] = [
                POPUP_BEGIN_LINE, FontFormatAttrib,
                texts[TXT_SHIELD_FORMULA], POPUP_END_LINE];
        };
        enable_popup(LBL_TOWER_EXPLABEL, popupLinesCpc);
        i = 0;
        while (i < 3) {
            _local7 = actor[(LBL_TOWER_BOOSTPRICELABEL + i)];
            with (_local7) {
                x = ((EXPERIENCE_BAR_X + 196) - text_width);
            };
            i = (i + 1);
        };
        set_cnt(TOWER_BOOSTCOIN, IF_GOLD);
    } else {
        if (!(save is Array)){
            save = savegame;
        } else {
            hide_back_pack = True;
        };
    };
    i = 0;
    while (i < 5) {
        if (int(save[(((tower_mode)
                ? (copyCatId + CPC_ATTRIBS_BONUS)
                : SG_ATTR_STAERKE_BONUS) + i)]) > 0){
            actor[(LBL_SCR_CHAR_STAERKE + i)]
                .default_text_format = FontFormatAttribBonus;
        } else {
            actor[(LBL_SCR_CHAR_STAERKE + i)]
                .default_text_format = FontFormatAttrib;
        };
        actor[(LBL_SCR_CHAR_STAERKE + i)].text = str((int(save[(((tower_mode)
                                ? (copyCatId + CPC_ATTRIBS)
                            : SG_ATTR_STAERKE) + i)]) + int(save[(((tower_mode)
                                ? (copyCatId + CPC_ATTRIBS_BONUS)
                                : SG_ATTR_STAERKE_BONUS) + i)])));
        popupLines = list();
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
            FontFormatAttrib, texts[(TXT_CHAR_SCHADEN + i)], POPUP_END_LINE];
        if (text_dir == "right"){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib,
                (actor[(LBL_SCR_CHAR_STAERKE_CAPTION + i)].text + " ÷ 2 ="),
                POPUP_END_LINE];
        } else {
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
            FontFormatAttrib,
            (("= " + actor[(LBL_SCR_CHAR_STAERKE_CAPTION + i)].text) + " / 2"),
            POPUP_END_LINE];
        };
        enable_popup((LBL_SCR_CHAR_SCHADEN + i), popupLines);
        enable_popup((LBL_SCR_CHAR_SCHADEN_CAPTION + i), popupLines);
        popupLines = list();
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            actor[(LBL_SCR_CHAR_STAERKE_CAPTION + i)].text, POPUP_END_LINE];
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
            FontFormatAttrib, texts[(TXT_ATTRIBHELP + i)], POPUP_END_LINE];
        if ((((((tower_mode)
            ? (copy_cat_id_raw + 1) : int(save[SG_CLASS])) == 1))
                and ((i == 0)))){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
            FontFormatAttrib, texts[TXT_ATTRIBHELP_WARRIOR], POPUP_END_LINE];
        } else {
        if ((((((tower_mode)
            ? (copy_cat_id_raw + 1) : int(save[SG_CLASS])) == 3))
                and ((i == 1)))){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib, texts[TXT_ATTRIBHELP_HUNTER],
                POPUP_END_LINE];
        } else {
        if ((((((tower_mode) ? (copy_cat_id_raw + 1)
            : int(save[SG_CLASS])) == 2))
                and ((i == 2)))){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib, texts[TXT_ATTRIBHELP_MAGE], POPUP_END_LINE];
        } else {
        if (i <= 2){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib, texts[(TXT_ATTRIBHELP_EXT + i)],
                POPUP_END_LINE];

        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            texts[TXT_BASIS], POPUP_TAB,
            str(int(save[(((tower_mode)
                ? (copyCatId + CPC_ATTRIBS)
                : SG_ATTR_STAERKE) + i)])), POPUP_END_LINE];
        tempBonus = 0;
        tempBonus = int(save[(((tower_mode)
                        ? (copyCatId + CPC_ATTRIBS_BONUS)
                        : SG_ATTR_STAERKE_BONUS) + i)]);
        if (!tower_mode){
            ii = 0;
            while (ii < 3) {
                if (int(save[(SG_POTION_TYPE + ii)]) == 16){
                    tmpHealth = int(save[(SG_POTION_GAIN + ii)]);
                } else {
                    if (((int(save[(SG_POTION_TYPE + ii)]) - 1) % 5) == i){
                        potionDuration = time_str(
                                      save[(SG_POTION_DURATION + ii)], True);
                        if (int(save[(SG_POTION_GAIN + ii)]) <= 25){
                            tempBonus = ((int(save[(SG_ATTR_STAERKE + i)])
                                 + int(save[(SG_ATTR_STAERKE_BONUS + i)]))
                            / ((100 + int(save[(SG_POTION_GAIN + ii)])) / 100))

                            if (hide_back_pack){
                                popupLines[popupLines.length] = [
                                    POPUP_BEGIN_LINE, FontFormatAttribTemp,
                                    texts[TXT_TEMPORARY], POPUP_TAB,
                                    str(math.round(
                                        ((int(save[(SG_POTION_GAIN + ii)])
                                         / 100) * tempBonus))),
                                    POPUP_END_LINE];
                            } else {
                                if (text_dir == "right"){
                                    popupLines[popupLines.length] =
                                        [POPUP_BEGIN_LINE,
                                        FontFormatAttribTemp,
                                        texts[TXT_TEMPORARY],
                                        POPUP_TAB,
                                        ((((("(" + potionDuration) + " ")
                                         + texts[TXT_UNTIL]) + ") ")
                                        + str(math.round(((int(save[(
                                          SG_POTION_GAIN + ii)]) / 100)
                                        * tempBonus)))), POPUP_END_LINE];
                                } else {
                                    popupLines[popupLines.length] = [
                                        POPUP_BEGIN_LINE,
                                        FontFormatAttribTemp,
                                        texts[TXT_TEMPORARY],
                                        POPUP_TAB,
                                        (((((str(math.round(((int(save[
                                         (SG_POTION_GAIN + ii)]) / 100)
                                        * tempBonus))) + " (")
                                        + texts[TXT_UNTIL]) + " ")
                                        + potionDuration) + ")"),
                                        POPUP_END_LINE];
                                };
                            };
                            tempBonus = (tempBonus
                                         - int(save[(SG_ATTR_STAERKE + i)]));
                        } else {
                            if (hide_back_pack){
                                popupLines[popupLines.length] = [
                                    POPUP_BEGIN_LINE,
                                    FontFormatAttribTemp,
                                    texts[TXT_TEMPORARY], POPUP_TAB,
                                    str(int(save[(SG_POTION_GAIN + ii)])),
                                    POPUP_END_LINE];
                            } else {
                                if (text_dir == "right"){
                                    popupLines[popupLines.length] =
                                        [POPUP_BEGIN_LINE,
                                        FontFormatAttribTemp,
                                        texts[TXT_TEMPORARY],
                                        POPUP_TAB,
                                        ((((("(" + potionDuration) + " ")
                                         + texts[TXT_UNTIL]) + ") ")
                                        + str(int(save[
                                              (SG_POTION_GAIN + ii)]))),
                                        POPUP_END_LINE];
                                } else {
                                    popupLines[popupLines.length] = [
                                        POPUP_BEGIN_LINE,
                                        FontFormatAttribTemp,
                                        texts[TXT_TEMPORARY],
                                        POPUP_TAB,
                                        ((((str(int(save[
                                         (SG_POTION_GAIN + ii)]))
                                         + " (") + texts[TXT_UNTIL]) + " ")
                                            + potionDuration) + ")"),
                                        POPUP_END_LINE];
                                };
                            };
                            tempBonus = (int(save[(SG_ATTR_STAERKE_BONUS + i)])
                                         - int(save[(SG_POTION_GAIN + ii)]));
                        };
                        break;
                    };
                };
                ii = (ii + 1);
            };
        };
        if (tempBonus > 0){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttribBonus, texts[TXT_BONUS],
                POPUP_TAB, str(tempBonus), POPUP_END_LINE];
        };
        enable_popup((LBL_SCR_CHAR_STAERKE + i), popupLines);
        enable_popup((LBL_SCR_CHAR_STAERKE_CAPTION + i), popupLines);
        if (!tower_mode){
            boostPrice = GetBoostPrice(save[(SG_ATTR_STAERKE_GEKAUFT + i)]);
            if (boostPrice > 9999){
                boostPrice = (int((boostPrice / 100)) * 100);
            };
            if (boostPrice > 0x3B9ACA00){
                boostPrice = 0x3B9ACA00;
            };
            canBoost[i] = Boolean((boostPrice <= Number(save[SG_GOLD])));
            boostGold = int((boostPrice / 100));
            boostSilver = (boostPrice % 100);
            hide((LBL_SCR_CHAR_PREIS1 + i), (SCR_CHAR_GOLD1 + i),
                 (LBL_SCR_CHAR_SILBER1 + i), (SCR_CHAR_SILBER1 + i));
            preisX = (CHAR_PROP_COLUMN_4_X + (
                      ((text_dir == "right")) ? 240 : 0));
            if (boostGold > 0){
                _local7 = actor[(LBL_SCR_CHAR_PREIS1 + i)];
                with (_local7) {
                    text = str(boostGold);
                    if (text_dir == "right"){
                        x = (preisX - text_width);
                        preisX = (x - 8);
                    } else {
                        x = preisX;
                        preisX = ((x + text_width) + 8);
                    };
                };
                _local7 = actor[(SCR_CHAR_GOLD1 + i)];
                with (_local7) {
                    if (text_dir == "right"){
                        x = (preisX - width);
                        preisX = (x - 10);
                    } else {
                        x = preisX;
                        preisX = ((x + width) + 10);
                    };
                };
                show((LBL_SCR_CHAR_PREIS1 + i), (SCR_CHAR_GOLD1 + i));
            };
            if (boostSilver > 0){
                _local7 = actor[(LBL_SCR_CHAR_SILBER1 + i)];
                with (_local7) {
                    text = str(boostSilver);
                    if (text_dir == "right"){
                        x = (preisX - text_width);
                        preisX = (x - 8);
                    } else {
                        x = preisX;
                        preisX = ((x + text_width) + 8);
                    };
                };
                _local7 = actor[(SCR_CHAR_SILBER1 + i)];
                with (_local7) {
                    if (text_dir == "right"){
                        x = (preisX - width);
                        preisX = (x - 10);
                    } else {
                        x = preisX;
                        preisX = ((x + width) + 10);
                    };
                };
                show((LBL_SCR_CHAR_SILBER1 + i), (SCR_CHAR_SILBER1 + i));
            };
        };
        i = (i + 1);
    };
    tmpKritische = (math.round(((((int(save[((tower_mode)
                    ? ((copyCatId + CPC_ATTRIBS) + 4)
                    : SG_ATTR_WILLENSKRAFT)]) + int(save[((tower_mode)
                    ? ((copyCatId + CPC_ATTRIBS_BONUS) + 4)
                    : SG_ATTR_WILLENSKRAFT_BONUS)])) * 25)
                    / (Number(save[((tower_mode)
                       ? (copyCatId + CPC_LEVEL) : SG_LEVEL)]) * 10))
                    * 100)) / 100);
    if (tmpKritische < 0){
        tmpKritische = 0;
    };
    if (tmpKritische > 50){
        tmpKritische = 50;
    };
    tmpDamageMin = save[((tower_mode)
                       ? (copyCatId + CPC_DAMAGE_MIN)
                       : SG_DAMAGE_MIN)];
    tmpDamageMax = save[((tower_mode)
                       ? (copyCatId + CPC_DAMAGE_MAX)
                       : SG_DAMAGE_MAX)];
    tmpDamageFactor = 0;
    tmpLifeFactor = 5;
    SchadenLblID = 0;
    Switch (int(((tower_mode)
            ? (copy_cat_id_raw + 1)
            : save[SG_CLASS]))){
        if case(1:
            SchadenLblID = LBL_SCR_CHAR_SCHADEN_CAPTION;
            SchadenID = LBL_SCR_CHAR_SCHADEN;
            tmpDamageFactor = (1 + ((Number(save[((tower_mode)
                               ? (copyCatId + CPC_ATTRIBS)
                               : SG_ATTR_STAERKE)]) + Number(save[((tower_mode)
                               ? (copyCatId + CPC_ATTRIBS_BONUS)
                               : SG_ATTR_STAERKE_BONUS)])) / 10));
            tmpLifeFactor = 5;
            break;
        if case(2:
            SchadenLblID = LBL_SCR_CHAR_LEBEN_CAPTION;
            SchadenID = LBL_SCR_CHAR_LEBEN;
            tmpDamageFactor = (1 + ((Number(save[((tower_mode)
                               ? ((copyCatId + CPC_ATTRIBS) + 2)
                               : SG_ATTR_AUSDAUER)])
                                + Number(save[((tower_mode)
                               ? ((copyCatId + CPC_ATTRIBS_BONUS) + 2)
                               : SG_ATTR_AUSDAUER_BONUS)])) / 10));
            tmpLifeFactor = 2;
            break;
        if case(3:
            SchadenLblID = LBL_SCR_CHAR_KAMPFWERT_CAPTION;
            SchadenID = LBL_SCR_CHAR_KAMPFWERT;
            tmpDamageFactor = (1 + ((Number(save[((tower_mode)
                               ? ((copyCatId + CPC_ATTRIBS) + 1)
                               : SG_ATTR_BEWEGLICHKEIT)])
                                + Number(save[((tower_mode)
                                     ? ((copyCatId + CPC_ATTRIBS_BONUS) + 1)
                                     : SG_ATTR_BEWEGLICHKEIT_BONUS)])) / 10));
            tmpLifeFactor = 4;
            break;
    };
    tmpDamageMin = math.round((tmpDamageMin * tmpDamageFactor));
    tmpDamageMax = math.round((tmpDamageMax * tmpDamageFactor));
    actor[LBL_SCR_CHAR_SCHADEN].text = int(((Number(save[((tower_mode)
                                       ? (copyCatId + CPC_ATTRIBS)
                                       : SG_ATTR_STAERKE)])
                            + Number(save[((tower_mode)
                                     ? (copyCatId + CPC_ATTRIBS_BONUS)
                                     : SG_ATTR_STAERKE_BONUS)])) / 2));
    actor[LBL_SCR_CHAR_KAMPFWERT].text = int(((Number(save[((tower_mode)
                         ? ((copyCatId + CPC_ATTRIBS) + 1)
                         : SG_ATTR_BEWEGLICHKEIT)]) + Number(save[((tower_mode)
                         ? ((copyCatId + CPC_ATTRIBS_BONUS) + 1)
                         : SG_ATTR_BEWEGLICHKEIT_BONUS)])) / 2));
    actor[LBL_SCR_CHAR_LEBEN].text = int(((Number(save[((tower_mode)
                                 ? ((copyCatId + CPC_ATTRIBS) + 2)
                                 : SG_ATTR_AUSDAUER)])
                                    + Number(save[((tower_mode)
                                 ? ((copyCatId + CPC_ATTRIBS_BONUS) + 2)
                                 : SG_ATTR_AUSDAUER_BONUS)])) / 2));
    actor[LBL_SCR_CHAR_RUESTUNG].default_text_format = (((tmpHealth > 0))
                            ? FontFormatAttribBonus : FontFormatAttrib);
    actor[LBL_SCR_CHAR_RUESTUNG].text = int(((((Number(save[((tower_mode)
            ? ((copyCatId + CPC_ATTRIBS) + 3)
            : SG_ATTR_INTELLIGENZ)]) + Number(save[((tower_mode)
            ? ((copyCatId + CPC_ATTRIBS_BONUS) + 3)
            : SG_ATTR_INTELLIGENZ_BONUS)])) * (tmpLifeFactor * 2))
            * (((tmpHealth > 0)) ? (Number((tmpHealth + 100)) / 100) : 1))
            * (0.5 + (save[((tower_mode) ? (copyCatId + CPC_LEVEL)
               : SG_LEVEL)] / 2))));
    actor[LBL_SCR_CHAR_WIDERSTAND].text = (str(tmpKritische) + str("%"));
    popupLines = list();
    popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
        FontFormatAttrib, texts[TXT_SCHADEN], POPUP_END_LINE];
    if (text_dir == "right"){
        popupLines[popupLines.length] = [
            POPUP_BEGIN_LINE, FontFormatAttrib,
            (((texts[TXT_WAFFENSCHADEN] + " × (1 + ") +
             actor[((LBL_SCR_CHAR_STAERKE_CAPTION + SchadenID) -
              LBL_SCR_CHAR_SCHADEN)].text) + " ÷ 10) ="), POPUP_END_LINE];
    } else {
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            (((("= " + texts[TXT_WAFFENSCHADEN]) + " * (1 + ")
             + actor[((LBL_SCR_CHAR_STAERKE_CAPTION + SchadenID)
                  - LBL_SCR_CHAR_SCHADEN)].text) + " / 10)"), POPUP_END_LINE];
    };
    enable_popup(SchadenID, popupLines);
    enable_popup(SchadenLblID, popupLines);
    popupLines = list();
    popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
        actor[LBL_SCR_CHAR_RUESTUNG_CAPTION].text, POPUP_END_LINE];
    if (text_dir == "right"){
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            (((((((((((tmpHealth > 0)) ? "(" : "")
             + actor[(LBL_SCR_CHAR_STAERKE_CAPTION + 3)].text) + " × ")
            + str(tmpLifeFactor)) + " × (") + texts[TXT_HALL_LIST_COLUMN_4])
            + " + 1)") + (((tmpHealth > 0)) ? ((") + " + str(tmpHealth))
            + "%") : "")) + " ="), POPUP_END_LINE];
    } else {
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            (((((((("= " + (((tmpHealth > 0)) ? "(" : ""))
             + actor[(LBL_SCR_CHAR_STAERKE_CAPTION + 3)].text) + " * ")
            + str(tmpLifeFactor)) + " * (") + texts[TXT_HALL_LIST_COLUMN_4])
            + " + 1)") + (((tmpHealth > 0)) ? ((") + " + str(tmpHealth)) + "%")
            : "")), POPUP_END_LINE];
    };
    enable_popup((LBL_SCR_CHAR_SCHADEN + 3), popupLines);
    enable_popup((LBL_SCR_CHAR_SCHADEN_CAPTION + 3), popupLines);
    popupLines = list();
    popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
                actor[LBL_SCR_CHAR_WIDERSTAND_CAPTION].text, POPUP_END_LINE];
    if (text_dir == "right"){
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
                (((actor[(LBL_SCR_CHAR_STAERKE_CAPTION + 4)].text + " × 5 ÷ (")
                 + texts[TXT_GEGNERSTUFE]) + " × 2) ="), POPUP_END_LINE];
    } else {
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
                (((("= " + actor[(LBL_SCR_CHAR_STAERKE_CAPTION + 4)].text)
                 + " * 5 / (") + texts[TXT_GEGNERSTUFE]) + " * 2)"),
                POPUP_END_LINE];
    };
    popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            texts[TXT_KRITISCHMINMAX], POPUP_END_LINE];
    enable_popup((LBL_SCR_CHAR_SCHADEN + 4), popupLines);
    enable_popup((LBL_SCR_CHAR_SCHADEN_CAPTION + 4), popupLines);
    actor[LBL_SCR_CHAR_SCHADEN_CAPTION].text = texts[TXT_CHAR_SCHADEN];
    actor[LBL_SCR_CHAR_LEBEN_CAPTION].text = texts[TXT_CHAR_LEBEN];
    actor[LBL_SCR_CHAR_KAMPFWERT_CAPTION].text = texts[TXT_CHAR_KAMPFWERT];
    if (SchadenLblID > 0){
        actor[SchadenLblID].text = texts[TXT_SCHADEN];
        actor[SchadenID].text = ((tmpDamageMin
                     + (((str(tmpDamageMin).length >= 6)) ? "-" : " - "))
                    + tmpDamageMax);
    };
    if (text_dir == "right"){
        actor[LBL_SCR_CHAR_SCHADEN].x = ((CHAR_PROP_COLUMN_6_X - 15)
                                     - actor[LBL_SCR_CHAR_SCHADEN].text_width);
        actor[LBL_SCR_CHAR_KAMPFWERT].x = ((CHAR_PROP_COLUMN_6_X - 15)
                                   - actor[LBL_SCR_CHAR_KAMPFWERT].text_width);
        actor[LBL_SCR_CHAR_LEBEN].x = ((CHAR_PROP_COLUMN_6_X - 15)
                                   - actor[LBL_SCR_CHAR_LEBEN].text_width);
        actor[LBL_SCR_CHAR_RUESTUNG].x = ((CHAR_PROP_COLUMN_6_X - 15)
                                  - actor[LBL_SCR_CHAR_RUESTUNG].text_width);
        actor[LBL_SCR_CHAR_WIDERSTAND].x = ((CHAR_PROP_COLUMN_6_X - 15)
                                - actor[LBL_SCR_CHAR_WIDERSTAND].text_width);
        actor[LBL_SCR_CHAR_SCHADEN_CAPTION].x = ((CHAR_PROP_COLUMN_6_X + 110)
                             - actor[LBL_SCR_CHAR_SCHADEN_CAPTION].text_width);
        actor[LBL_SCR_CHAR_KAMPFWERT_CAPTION].x = ((CHAR_PROP_COLUMN_6_X + 110)
                           - actor[LBL_SCR_CHAR_KAMPFWERT_CAPTION].text_width);
        actor[LBL_SCR_CHAR_LEBEN_CAPTION].x = ((CHAR_PROP_COLUMN_6_X + 110)
                               - actor[LBL_SCR_CHAR_LEBEN_CAPTION].text_width);
        actor[LBL_SCR_CHAR_RUESTUNG_CAPTION].x = ((CHAR_PROP_COLUMN_6_X + 110)
                          - actor[LBL_SCR_CHAR_RUESTUNG_CAPTION].text_width);
        actor[LBL_SCR_CHAR_WIDERSTAND_CAPTION].x = (
                            (CHAR_PROP_COLUMN_6_X + 110)
                        - actor[LBL_SCR_CHAR_WIDERSTAND_CAPTION].text_width);
        i = 0;
        while (i < 5) {
            actor[(LBL_SCR_CHAR_STAERKE + i)].x = (
                       (CHAR_PROP_COLUMN_1_X + 50)
                       - actor[(LBL_SCR_CHAR_STAERKE + i)].text_width);
            actor[(LBL_SCR_CHAR_STAERKE_CAPTION + i)].x =
                        ((CHAR_PROP_COLUMN_1_X + 150)
                         - actor[(LBL_SCR_CHAR_STAERKE_CAPTION + i)]
                         .text_width);
            i = (i + 1);
        };
        if (!tower_mode){
            actor[LBL_CHAR_MOUNT_NAME].x =
                (((CHAR_MOUNT_X + CHAR_MOUNT_X) - 20)
                 - actor[LBL_CHAR_MOUNT_NAME].text_width);
            actor[LBL_CHAR_MOUNT_DESCR].width = (CHAR_MOUNT_X - 20);
            actor[LBL_CHAR_MOUNT_RUNTIME].x = (((CHAR_MOUNT_X + CHAR_MOUNT_X)
                           - 20) - actor[LBL_CHAR_MOUNT_RUNTIME].text_width);
            actor[LBL_CHAR_MOUNT_GAIN].x = (((CHAR_MOUNT_X + CHAR_MOUNT_X)
                                - 20) - actor[LBL_CHAR_MOUNT_GAIN].text_width);
            make_right_text_area(INP_CHARDESC);
            actor[SCR_CHAR_GILDE].x = ((((GILDEEHRE_X + GILDEEHRE_X) + 40)
                               + 280) - actor[LBL_SCR_CHAR_GILDE].text_width);
        };
    };
    if (!tower_mode){
        i = 0;
        while (i < 3) {
            set_cnt((CHAR_POTION + i),
                   ((int(save[(SG_POTION_TYPE + i)]))==0)
                   ? C_EMPTY
                   : GetItemID(12, int(save[(SG_POTION_TYPE + i)]), 0, 0));
            if (int(save[(SG_POTION_TYPE + i)]) == 0){
                enable_popup((CHAR_POTION + i));
            } else {
                if (hide_back_pack){
                    enable_popup((CHAR_POTION + i),
                                 POPUP_BEGIN_LINE,
                                 texts[((TXT_ITMNAME_12
                                    + int(save[(SG_POTION_TYPE + i)])) - 1)],
                                POPUP_END_LINE, POPUP_BEGIN_LINE,
                                texts[(((int(save[
                                       (SG_POTION_TYPE + i)]) == 16))
                               ? TXT_ITEM_ATTRIB_CLASS_12
                               : (TXT_ITEM_ATTRIB_CLASS_1
                                  + ((int(save[(SG_POTION_TYPE + i)])
                                     - 1) % 5)))], POPUP_TAB,
                                (("+ " + save[(SG_POTION_GAIN + i)])
                                 + (((((int(save[(SG_POTION_TYPE + i)]) == 16))
                                    or ((save[(save_POTION_GAIN + i)] <= 25))))
                                ? "%" : "")), POPUP_END_LINE);
                } else {
                    enable_popup((CHAR_POTION + i),
                                 POPUP_BEGIN_LINE,
                                 texts[((TXT_ITMNAME_12
                                    + int(save[(SG_POTION_TYPE + i)])) - 1)],
                                POPUP_END_LINE,
                                POPUP_BEGIN_LINE,
                                texts[(((int(save[
                                       (SG_POTION_TYPE + i)]) == 16))
                                       ? TXT_ITEM_ATTRIB_CLASS_12
                                       : (TXT_ITEM_ATTRIB_CLASS_1
                              + ((int(save[(SG_POTION_TYPE + i)]) - 1) % 5)))],
                            POPUP_TAB, (("+ " + save[(SG_POTION_GAIN + i)])
                            + (((((int(save[(SG_POTION_TYPE + i)]) == 16))
                       or ((save[(SG_POTION_GAIN + i)] <= 25)))) ? "%" : "")),
                        POPUP_END_LINE, POPUP_BEGIN_LINE, texts[TXT_REMAINING],
                        POPUP_TAB, time_str(save[(SG_POTION_DURATION + i)],
                            True), POPUP_END_LINE, POPUP_BEGIN_LINE,
                        texts[TXT_POTION_KILL_INSTRUCTIONS], POPUP_END_LINE);
                };
            };
            i = (i + 1);
        };
    };
    move(CHAR_SLOT_1, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_TOP_Y);
    move(CHAR_SLOT_2, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW2_Y);
    move(CHAR_SLOT_3, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW3_Y);
    move(CHAR_SLOT_4, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW4_Y);
    move(CHAR_SLOT_5, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_TOP_Y);
    move(CHAR_SLOT_6, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW2_Y);
    move(CHAR_SLOT_7, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW3_Y);
    move(CHAR_SLOT_8, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW4_Y);
    move(CHAR_SLOT_9, CHAR_SLOTS_R4C2_X, CHAR_SLOTS_ROW4_Y);
    move(CHAR_SLOT_10, CHAR_SLOTS_R4C3_X, CHAR_SLOTS_ROW4_Y);
    move(CHAR_SLOT_11, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW5_Y);
    move(CHAR_SLOT_12, CHAR_SLOTS_R5C2_X, CHAR_SLOTS_ROW5_Y);
    move(CHAR_SLOT_13, CHAR_SLOTS_R5C3_X, CHAR_SLOTS_ROW5_Y);
    move(CHAR_SLOT_14, CHAR_SLOTS_R5C4_X, CHAR_SLOTS_ROW5_Y);
    move(CHAR_SLOT_15, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW5_Y);
    move(CHAR_SLOT_FIDGET_1, SHOP_SLOTS_C1_X, SHOP_SLOTS_R1_Y);
    move(CHAR_SLOT_FIDGET_2, SHOP_SLOTS_C2_X, SHOP_SLOTS_R1_Y);
    move(CHAR_SLOT_FIDGET_3, SHOP_SLOTS_C3_X, SHOP_SLOTS_R1_Y);
    move(CHAR_SLOT_FIDGET_4, SHOP_SLOTS_C1_X, SHOP_SLOTS_R2_Y);
    move(CHAR_SLOT_FIDGET_5, SHOP_SLOTS_C2_X, SHOP_SLOTS_R2_Y);
    move(CHAR_SLOT_FIDGET_6, SHOP_SLOTS_C3_X, SHOP_SLOTS_R2_Y);
    move(CHAR_SLOT_SHAKES_1, SHOP_SLOTS_C1_X, SHOP_SLOTS_R1_Y);
    move(CHAR_SLOT_SHAKES_2, SHOP_SLOTS_C2_X, SHOP_SLOTS_R1_Y);
    move(CHAR_SLOT_SHAKES_3, SHOP_SLOTS_C3_X, SHOP_SLOTS_R1_Y);
    move(CHAR_SLOT_SHAKES_4, SHOP_SLOTS_C1_X, SHOP_SLOTS_R2_Y);
    move(CHAR_SLOT_SHAKES_5, SHOP_SLOTS_C2_X, SHOP_SLOTS_R2_Y);
    move(CHAR_SLOT_SHAKES_6, SHOP_SLOTS_C3_X, SHOP_SLOTS_R2_Y);
    tmpItmClass = 0;
    tmpItmPic = 0;
    tmpItmPic = int(save[((((tower_mode)
                    ? (copyCatId + CPC_ITEMS)
                    : SG_INVENTORY_OFFS) + (8 * SG['ITM']['SIZE']))
                    + SG['ITM']['PIC'])]);
    tmpItmClass = 0;
    while (tmpItmPic >= 1000) {
        tmpItmPic = (tmpItmPic - 1000);
        tmpItmClass = (tmpItmClass + 1);
    };
    i = 0;
    while (i < 15) {
        if ((((i < 10)) or (!(tower_mode)))){
            if (int(save[((((tower_mode)
                ? (copyCatId + CPC_ITEMS)
                : SG_INVENTORY_OFFS) + (i * SG['ITM']['SIZE']))
                + SG_ITM_TYP)]) == 0){
                save[((((tower_mode)
                    ? (copyCatId + CPC_ITEMS)
                    : SG_INVENTORY_OFFS) +
                    (i * SG['ITM']['SIZE'])) + SG['ITM']['PIC'])] = 0;
            };
        };
        if ((((i > 9)) and (hide_back_pack))){
            set_cnt((CHAR_SLOT_1 + i), C_EMPTY);
            enable_popup((CHAR_SLOT_1 + i));
        } else {
            if ((((i == 9)) and ((tmpItmClass >= 1)))){
                set_cnt((CHAR_SLOT_1 + i), get_arrow_id(((tower_mode) ?
                       (copyCatId + CPC_ITEMS) : SG_INVENTORY_OFFS), 8, save,
                        True, ((tmpItmClass)==1) ? 1 : -1));
                actor[(CHAR_SLOT_1 + i)].mouse_enabled = False;
            } else {
                set_cnt((CHAR_SLOT_1 + i),
                       GetItemID(((tower_mode) ? (((i > 9))
                                 ? TSG_LOOT_SACK : (copyCatId + CPC_ITEMS))
                        : SG_INVENTORY_OFFS), ((((tower_mode) and ((i > 9))))
                        ? (i - 10) : i), save, ((tower_mode) ? (((i > 9)) ? -1
                                         : (-(copyCatSel) - 3)) : -2)));
                item_popup((CHAR_SLOT_1 + i), (((tower_mode) ? (((i > 9))
                          ? TSG_LOOT_SACK : (copyCatId + CPC_ITEMS))
                    : SG_INVENTORY_OFFS) + (((((tower_mode) and ((i > 9))))
                         ? (i - 10) : i) * SG['ITM']['SIZE'])), save,
                        hide_back_pack, no_prices, tower_mode, witch_mode);
                actor[(CHAR_SLOT_1 + i)]
                    .mouse_enabled = !((int(save[((((tower_mode)
                    ? (((i > 9)) ? TSG_LOOT_SACK : (copyCatId + CPC_ITEMS))
                    : SG_INVENTORY_OFFS) + (((((tower_mode) and ((i > 9))))
                  ? (i - 10) : i) * SG['ITM']['SIZE'])) + SG_ITM_TYP)]) == 0));
            };
        };
        if (hide_back_pack){
            dragDropProhibit = True;
        } else {
            dragDropProhibit = False;
        };
        i = (i + 1);
    };
    if (!tower_mode){
        var IsEpic:* = function (pic):
            while (pic > 1000) {
                pic = (pic - 1000);
            };
            return ((pic >= 50));
        };
        hasEpic = False;
        i = 0;
        while (i < 6) {
            if (int(save[((SG_FIDGET_ITEM1 + (i * SG['ITM']['SIZE']))
                + SG_ITM_TYP)]) == 0){
                save[((SG_FIDGET_ITEM1 + (i * SG['ITM']['SIZE']))
                    + SG['ITM']['PIC'])] = 0;
            };
            set_cnt((CHAR_SLOT_FIDGET_1 + i),
                   GetItemID(SG_FIDGET_ITEM1, i, save))
            item_popup((CHAR_SLOT_FIDGET_1 + i),
                      (SG_FIDGET_ITEM1 + (i * SG['ITM']['SIZE'])),
                      save, hide_back_pack);
            if (((IsEpic(save[((SG_FIDGET_ITEM1 + (i * SG['ITM']['SIZE']))
                    + SG['ITM']['PIC'])])) and (on_stage(SCR_FIDGET_BG)))){
                hasEpic = True;
            };
            if (int(save[((SG_SHAKES_ITEM1 + (i * SG['ITM']['SIZE']))
                    + SG_ITM_TYP)]) == 0){
                save[((SG_SHAKES_ITEM1 + (i * SG['ITM']['SIZE']))
                    + SG['ITM']['PIC'])] = 0;
            };
            set_cnt((CHAR_SLOT_SHAKES_1 + i),
                   GetItemID(SG_SHAKES_ITEM1, i, save))
            item_popup((CHAR_SLOT_SHAKES_1 + i),
                      (SG_SHAKES_ITEM1 + (i * SG['ITM']['SIZE'])),
                      save, hide_back_pack);
            if (((IsEpic(save[((SG_SHAKES_ITEM1 + (i * SG['ITM']['SIZE']))
                    + SG['ITM']['PIC'])])) and (on_stage(SCR_SHAKES_BG)))){
                hasEpic = True;
            };
            i = (i + 1);
        };
        if (!hasEpic){
            BlockReroll = False;
        } else {
            if (RollFrenzy.running){
                error_message("Yay!");
                play(SND_JINGLE);
                RollFrenzy.stop();
            };
        };
        if (text_dir == "right"){
            actor[LBL_CHAR_RUESTUNG]
                .text = ((save[SG_ARMOR] + " :") + texts[TXT_RUESTUNG_SUM]);
        } else {
            actor[LBL_CHAR_RUESTUNG]
                .text = ((texts[TXT_RUESTUNG_SUM] + ": ") + save[SG_ARMOR]);
        };
        DamageReduction = int((Number(save[SG_ARMOR])
                              / Number(save[SG_LEVEL])));
        DamageReductionMax = 50;
        Switch (int(save[SG_CLASS])){
            if case(2:
                DamageReductionMax = 10;
                break;
            if case(3:
                DamageReductionMax = 25;
                break;
        };
        if (DamageReduction > DamageReductionMax){
            DamageReduction = DamageReductionMax;
        };
        popupLines = list();
        popupLines[popupLines.length] = [POPUP_BEGIN_LINE, FontFormatAttrib,
            texts[TXT_RUESTUNG_SUM], POPUP_END_LINE];
        if (text_dir == "right"){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib,
                ((((((((("(" + texts[TXT_MAX]) + " -")
                 + str(DamageReductionMax)) + "%) ")
                    + str(DamageReduction)) + "% :") + save[SG_LEVEL]) + " ")
                + texts[TXT_RUESTUNG_SUM_HINT]), POPUP_END_LINE];
        } else {
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
            FontFormatAttrib, (((((((((texts[TXT_RUESTUNG_SUM_HINT] + " ")
                + save[SG_LEVEL]) + ": -") + str(DamageReduction)) + "% (")
                + texts[TXT_MAX]) + " -") + str(DamageReductionMax)) + "%)"),
            POPUP_END_LINE];
        };
        if (texts[TXT_SHIELD_FORMULA]){
            popupLines[popupLines.length] = [POPUP_BEGIN_LINE,
                FontFormatAttrib, texts[TXT_SHIELD_FORMULA], POPUP_END_LINE];
        };
        enable_popup(LBL_CHAR_RUESTUNG, popupLines);
        enable_popup(CHAR_RUESTUNG, popupLines);
    };
    '''
    print save, no_prices, tower_mode, copy_cat_id_raw, witch_mode


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


def get_hl_index(in_str):
    '''
    return (int(decode_chat(in_str, True)));
    '''
    print in_str


def decode_chat(in_str, get_hl_mode=False, get_gb_mode=False):
    '''
    var namePart:String;
    var timePart:String;
    var crestStr:String;
    var authorStr:String;
    var dateStr:String;
    if (text_dir == "right"){
        if (in_str.find("§") != -1){
            namePart = in_str.split("§")[0];
            if (namePart[-1: 1] == ":"){
                namePart = namePart[0: (namePart.length - 1)]
            };
            timePart = namePart[0: namePart.find(" ")]
            namePart = namePart[(namePart.find(" ") + 1):]
            in_str = ((((in_str.split("§")[1] + " §:")
                     + namePart) + " ") + timePart);
        };
    };
    in_str = in_str.split("§").join(((get_hl_mode) ? "§" : ""));
    if (((!((in_str.find("#?") == -1))) and ((in_str.find("##") == -1)))){
        crestStr = in_str.split("#?")[1];
        authorStr = in_str.split("#?")[0];
        dateStr = in_str[0: 5]
        authorStr = authorStr[6:]
        authorStr = authorStr[0: (authorStr.length - 3)]
        in_str = ((dateStr + " ") + texts[TXT_CREST_SUGGESTION]
                 .split("%1").join(authorStr));
        if (!crestSuggestion[in_str]){
            new_crest_suggested = in_str;
        };
        crestSuggestion[in_str] = crestStr;
    };
    in_str = in_str.split("#{").join("/");
    in_str = in_str.split("#}").join(";");
    in_str = in_str.split("##").join("#");
    in_str = in_str.split("%u20AC").join("€");
    if (in_str[0: 1] == "#"){
        if (text_dir == "right"){
            if (in_str[0: 4] == "#dg#"){
                in_str = ((((((((texts[TXT_DONATE_GOLD_2] + " ")
                         + str((Number(in_str.split("#")[3]) / 100))) + " ")
                        + texts[TXT_DONATE_GOLD_1]) + " ") + in_str
                        .split("#")[2].split(" ")[1]) + " ")
                        + in_str.split("#")[2].split(" ")[0]);
            } else {
                if (in_str[0: 4] == "#dm#"){
                    in_str = ((((((((texts[TXT_DONATE_MUSH_2] + " ")
                             + in_str.split("#")[3]) + " ")
                            + texts[TXT_DONATE_MUSH_1]) + " ")
                            + in_str.split("#")[2].split(" ")[1]) + " ")
                            + in_str.split("#")[2].split(" ")[0]);
            } else {
                if (in_str[0: 4] == "#sr#"){
                    if (texts[TXT_SERVER_STARTED]){
                        in_str = texts[TXT_SERVER_STARTED].split("%1")
                        .join(time_str(int(in_str.split("#")[2])));
                    } else {
                        in_str = "Server restarted at %1".split("%1")
                        .join(time_str(int(in_str.split("#")[2])));
                    };
            } else {
                if (in_str[0: 4] == "#bd#"){
                    if (int(in_str.split("#")[3]) == 0){
                        in_str = texts[(TXT_CATAPULT + 7)];
                    } else {
                        in_str = ((((texts[TXT_BUILDING_1].split("%1")
                                 .join(texts[((TXT_GILDE_GEBAEUDE_NAME1
                                       + int(in_str.split("#")[3])) - 1)])
                                + " ") + in_str.split("#")[2].split(" ")[1])
                                + " ") + in_str.split("#")[2].split(" ")[0]);
                    };
            } else {
                if (in_str[0: 4] == "#ra#"){
                    in_str = ((((((((texts[(TXT_RANKMSG_6
                             + int(in_str.split("#")[3]))] + " ")
                            + in_str.split("#")[4]) + " ")
                            + texts[(TXT_RANKMSG_1
                            + int(in_str.split("#")[3]))]) + " ")
                            + in_str.split("#")[2].split(" ")[1]) + " ")
                            + in_str.split("#")[2].split(" ")[0]);
            } else {
                if (in_str[0: 4] == "#in#"){
                    in_str = ((((texts[TXT_GUILD_JOINED] + " ")
                        + in_str.split("#")[2].split(" ")[1]) + " ")
                        + in_str.split("#")[2].split(" ")[0]);
            } else {
                if (in_str[0: 4] == "#ou#"){
                    in_str = ((((texts[TXT_GUILD_QUIT] + " ") + in_str
                             .split("#")[2].split(" ")[1]) + " ")
                            + in_str.split("#")[2].split(" ")[0]);
            } else {
                if (in_str[0: 4] == "#rv#"){
                    in_str = texts[TXT_REVOLT_CHAT_MSG].split("%1")
                        .join(in_str.split("#")[2]).split("%2")
                        .join(in_str.split("#")[3]).split("%3")
                        .join(in_str.split("#")[4]);
            } else {
                if (in_str[0: 4] == "#a+#"){
                    in_str = texts[TXT_GUILD_ATTACK_SUCCESS].split("%1")
                        .join(((in_str.split("#")[2].split(" ")[1] + " ")
                          + in_str.split("#")[2].split(" ")[0])).split("%2")
                            .join(in_str.split("#")[3]);
                    if (get_gb_mode){
                        return ("1");
                    };
            } else {
                if (in_str[0: 4] == "#a-#"){
                    in_str = texts[TXT_GUILD_ATTACK_FAIL].split("%1")
                        .join(((in_str.split("#")[2].split(" ")[1] + " ")
                              + in_str.split("#")[2]
                              .split(" ")[0])).split("%2")
                            .join(in_str.split("#")[3]);
                    if (get_gb_mode){
                        return ("1");
                    };
            } else {
                if (in_str[0: 4] == "#d+#"){
                    in_str = texts[TXT_GUILD_DEFENSE_SUCCESS].split("%1")
                        .join(((in_str.split("#")[2].split(" ")[1] + " ")
                          + in_str.split("#")[2].split(" ")[0])).split("%2")
                            .join(in_str.split("#")[3]);
                    if (get_gb_mode){
                        return ("1");
                    };
            } else {
                if (in_str[0: 4] == "#d-#"){
                    in_str = texts[TXT_GUILD_DEFENSE_FAIL]
                        .split("%1").join(((in_str.split("#")[2].split(" ")[1]
                          + " ") + in_str.split("#")[2].split(" ")[0]))
                            .split("%2").join(in_str.split("#")[3]);
                    if (get_gb_mode){
                        return ("1");
                    };
            } else {
                if (in_str[0: 4] == "#r+#"){
                    in_str = texts[TXT_GUILD_RAID_SUCCESS]
                        .split("%1").join(((("(50/" + in_str.split("#")[2])
                          + ") ") + texts[((TXT_DUNGEON_NAMES
                          + int(in_str.split("#")[2])) - 1)]));
                    if (get_gb_mode){
                        return ("1");
                    };
            } else {
                if (in_str[0: 4] == "#r-#"){
                    in_str = texts[TXT_GUILD_RAID_FAIL].split("%1")
                        .join(((("(50/" + in_str.split("#")[2]) + ") ")
                              + texts[((TXT_DUNGEON_NAMES
                                       + int(in_str.split("#")[2])) - 1)]));
                    if (get_gb_mode){
                        return ("1");
                    };
            } else {
                if (in_str[0: 4] == "#lu#"){
                    in_str = texts[TXT_GUILD_LEVEL_UP].split("%1")
                        .join(in_str.split("#")[2]).split("%2")
                        .join(in_str.split("#")[3]);
            } else {
                if (in_str[0: 4] == "#du#"){
                    in_str = texts[TXT_GUILD_DUNGEON_COMPLETED].split("%1")
                        .join(in_str.split("#")[2]).split("%2")
                        .join(texts[(((in_str.split("#")[3] == 100)) ? 9538
                              : ((TXT_DUNGEON_NAME
                                + (1 * in_str.split("#")[3]))
                                 - 1))].split("|")[0]).split("%3")
                                    .join(in_str.split("#")[4]);
            } else {
                if (in_str[0: 4] == "#ep#"){
                    in_str = texts[TXT_GUILD_EPICITEM].split("%1")
                        .join(in_str.split("#")[2]).split("%2")
                        .join(GetItemName(0, in_str.split("#")[3].split("/")));
                };
        } else {
            if (in_str[0: 4] == "#dg#"){
                in_str = ((((((in_str.split("#")[2] + " ")
                         + texts[TXT_DONATE_GOLD_1]) + " ")
                        + str((Number(in_str.split("#")[3]) / 100))) + " ")
                        + texts[TXT_DONATE_GOLD_2]);
        } else {
            if (in_str[0: 4] == "#dm#"){
                in_str = ((((((in_str.split("#")[2] + " ")
                         + texts[TXT_DONATE_MUSH_1]) + " ")
                            + in_str.split("#")[3]) + " ")
                            + texts[TXT_DONATE_MUSH_2]);
        } else {
            if (in_str[0: 4] == "#sr#"){
                if (texts[TXT_SERVER_STARTED]){
                    in_str = texts[TXT_SERVER_STARTED].split("%1")
                        .join(time_str(int(in_str.split("#")[2])));
                } else {
                    in_str = "Server restarted at %1".split("%1")
                        .join(time_str(int(in_str.split("#")[2])));
                };
        } else {
            if (in_str[0: 4] == "#bd#"){
                if (int(in_str.split("#")[3]) == 0){
                    in_str = ((in_str.split("#")[2] + " ")
                             + texts[(TXT_CATAPULT + 7)]);
                } else {
                    in_str = ((in_str.split("#")[2] + " ")
                             + texts[TXT_BUILDING_1].split("%1")
                             .join(texts[((TXT_GILDE_GEBAEUDE_NAME1
                                   + int(in_str.split("#")[3])) - 1)]));
                };
        } else {
            if (in_str[0: 4] == "#ra#"){
                in_str = ((((((in_str.split("#")[2] + " ") + texts[
                         (TXT_RANKMSG_1 + int(in_str.split("#")[3]))]) + " ")
                            + in_str.split("#")[4]) + " ")
                        + texts[(TXT_RANKMSG_6 + int(in_str.split("#")[3]))]);
        } else {
            if (in_str[0: 4] == "#in#"){
                in_str = ((in_str.split("#")[2] + " ")
                    + texts[TXT_GUILD_JOINED])
        } else {
            if (in_str[0: 4] == "#ou#"){
                in_str = ((in_str.split("#")[2] + " ")
                    + texts[TXT_GUILD_QUIT]);
        } else {
            if (in_str[0: 4] == "#rv#"){
                in_str = texts[TXT_REVOLT_CHAT_MSG].split("%1")
                    .join(in_str.split("#")[2]).split("%2")
                    .join(in_str.split("#")[3]).split("%3")
                    .join(in_str.split("#")[4]);
        } else {
            if (in_str[0: 4] == "#a+#"){
                in_str = texts[TXT_GUILD_ATTACK_SUCCESS].split("%1")
                    .join(in_str.split("#")[2]).split("%2")
                    .join(in_str.split("#")[3]);
                if (get_gb_mode){
                    return ("1");
                };
        } else {
            if (in_str[0: 4] == "#a-#"){
                in_str = texts[TXT_GUILD_ATTACK_FAIL].split("%1")
                    .join(in_str.split("#")[2]).split("%2")
                    .join(in_str.split("#")[3]);
                if (get_gb_mode){
                    return ("1");
                };
        } else {
            if (in_str[0: 4] == "#d+#"){
                in_str = texts[TXT_GUILD_DEFENSE_SUCCESS].split("%1")
                    .join(in_str.split("#")[2]).split("%2")
                    .join(in_str.split("#")[3]);
                if (get_gb_mode){
                    return ("1");
                };
        } else {
            if (in_str[0: 4] == "#d-#"){
                in_str = texts[TXT_GUILD_DEFENSE_FAIL].split("%1")
                    .join(in_str.split("#")[2]).split("%2")
                    .join(in_str.split("#")[3]);
                if (get_gb_mode){
                    return ("1");
                };
        } else {
            if (in_str[0: 4] == "#r+#"){
                in_str = texts[TXT_GUILD_RAID_SUCCESS].split("%1")
                    .join((((texts[((TXT_DUNGEON_NAMES + int(in_str
                          .split("#")[2])) - 1)] + " (") + in_str
                            .split("#")[2]) + "/50)"));
                if (get_gb_mode){
                    return ("1");
                };
        } else {
            if (in_str[0:4] == "#r-#"){
                in_str = texts[TXT_GUILD_RAID_FAIL]
                    .split("%1").join((((texts[
                        ((TXT_DUNGEON_NAMES + int(in_str.split("#")[2])) - 1)]
                        + " (") + in_str.split("#")[2]) + "/50)"));
                if (get_gb_mode){
                    return ("1");
                };
        } else {
            if (in_str[0:4] == "#lu#"){
                in_str = texts[TXT_GUILD_LEVEL_UP].split("%1")
                    .join(in_str.split("#")[2])
                    .split("%2").join(in_str.split("#")[3]);
        } else {
            if (in_str[0:4] == "#du#"){
                in_str = texts[TXT_GUILD_DUNGEON_COMPLETED]
                    .split("%1").join(in_str.split("#")[2])
                    .split("%2").join(texts[(((in_str.split("#")[3] == 100))
                        ? 9538 : (TXT_DUNGEON_NAME
                            + (1 * in_str.split("#")[3]))
                        - 1)].split("|")[0])
                        .split("%3").join(in_str.split("#")[4]);
        } else {
            if (in_str[0:4] == "#ep#"){
                in_str = texts[TXT_GUILD_EPICITEM]
                    .split("%1").join(in_str.split("#")[2])
                    .split("%2").join(
                          GetItemName(0, in_str.split("#")[3].split("/")));
            };
        if (on_stage(LBL_GILDE_TITEL)){
            send_action(ACT_SCREEN_GILDEN);
        };
        if (get_gb_mode){
            return ("0");
        };
        if (get_hl_mode){
            return (str(in_str.length));
        };
    };
    if (get_hl_mode){
        return (str(in_str.find("§")));
    };
    return (in_str);
    '''
    print in_str, get_hl_mode, get_gb_mode


def chat_line(line, is_error=False, hl_index=-1, is_whisper=False):
    '''
    var i:* = 0;
    var nextLine:* = None;
    var line:* = line;
    var is_error:Boolean = is_error;
    var hl_index = hl_index;
    var is_whisper:Boolean = is_whisper;
    nextLine = "";
    var seekSpace:* = False;
    var noSpace:* = False;
    var indent:* = 0;
    if (GildeChatScroll > 0){
        GildeChatScroll++;
    };
    if (GildeChatScroll > 35){
        GildeChatScroll = 35;
    };
    line = swap_words(line);
    while (line.split("  ").length > 1) {
        line = line.split("  ").join(" ");
    };
    i = 0;
    while (i < 39) {
        var _local6 = actor[(LBL['GILDE']['CHAT'] + i)];
        with (_local6) {
            default_text_format = actor[((LBL['GILDE']['CHAT']
                                         + i) + 1)].default_text_format;
            htmlText = actor[((LBL['GILDE']['CHAT'] + i) + 1)].htmlText;
            y = (GILDE_CHAT_Y + (((i + GildeChatScroll) - 35) * GILDE_CHAT_Y));
            visible = ((((i + GildeChatScroll) >= 35)) and
                       (((i + GildeChatScroll) < 40)));
        };
        i = (i + 1);
    };
    _local6 = actor[(LBL['GILDE']['CHAT'] + 39)];
    with (_local6) {
        default_text_format = ((is_error)
                               ? font_format_chatError : font_format_chat);
        if (is_whisper){
            default_text_format = font_format_chatWhisper;
        };
        do  {
            text = line;
            if ((((text_width > GILDE_TEXT_X)) or (seekSpace))){
                if (!noSpace){
                    seekSpace = True;
                };
                if ((((text_width <= GILDE_TEXT_X)) and (
                    (line[(line.length - 1):] == " ")))){
                    seekSpace = False;
                } else {
                    nextLine = (line[(line.length - 1):] + nextLine);
                };
                line = line[0: (line.length - 1)]
                if (line == ""){
                    line = nextLine;
                    nextLine = "";
                    noSpace = True;
                    seekSpace = False;
                    text = line;
                };
            };
        } while ((((text_width > GILDE_TEXT_X)) or (seekSpace)));
        if (hl_index > -1){
            if (hl_index > text.length){
                hl_index = text.length;
            };
            if (is_whisper){
                if (text_dir == "right"){
                    setTextFormat(FontFormatHighlightWhisper,
                                  hl_index, length)
                } else {
                    setTextFormat(FontFormatHighlightWhisper, 0, hl_index);
                };
            } else {
                if (text_dir == "right"){
                    setTextFormat(FontFormatHighlight, hl_index, length);
                } else {
                    setTextFormat(FontFormatHighlight, 0, hl_index);
                };
            };
        };
        if (GildeChatScroll == 0){
            y = (GILDE_CHAT_Y + ((39 - 35) * GILDE_CHAT_Y));
            visible = True;
        };
    };
    if (nextLine != ""){
        chat_line(nextLine, is_error, -1, is_whisper);
    };
    '''
    print line, is_error, hl_index, is_whisper


def pay_method(dealer_menu):
    '''
    if (dealer_menu > (pay_methods.length - 1)){
        return (0);
    };
    return (pay_methods[dealer_menu]);
    '''
    print dealer_menu


def toilet_tank_adjust_event():
    '''
    actor[(TOILET + 1)].y = ((190 + 122) - (toiletTankCurrent * 118));
    if (toiletTankCurrent > (toiletTankDest + 0.01)){
        toiletTankCurrent = (toiletTankCurrent - 0.01);
    } else {
        if (toiletTankCurrent < (toiletTankDest - 0.01)){
            toiletTankCurrent = (toiletTankCurrent + 0.01);
        } else {
            toiletTankCurrent = toiletTankDest;
            toiletTankAdjustTimer.stop();
        };
    };
    '''
    pass


def waiting_for(target_time):
    '''
    var tmpTime:Date;
    tmpTime = new Date();
    tmpTime.setTime(((target_time * 1000) - ((1000 * 60) * 60)));
    return ((game_time.getTime() < tmpTime.getTime()));
    '''
    print target_time


def waiting_time(target_time):
    '''
    var tmpTime:* = None;
    var timeDiff:* = None;
    var target_time:* = target_time;
    tmpTime = new Date();
    timeDiff = new Date();
    var diffDays:* = 0;
    tmpTime.setTime(((target_time * 1000) - ((1000 * 60) * 60)));
    timeDiff.setTime((tmpTime.getTime() - game_time.getTime()));
    var _local3 = timeDiff;
    diffDays = ((((timeDiff.getTime() / 1000) / 60) / 60) / 24);
    return ((((diffDays > 0)) ? ((str((diffDays + 1)) + " ")
            + texts[(((diffDays == 0))
                     ? TXT_TAG : TXT_TAGE)])
                    : ((((((getUTCHours())>0)
                       ? (str((getUTCHours() - 0)) + ":")
                       : "" + ((getUTCMinutes())<10) ? "0" : "")
                        + str(getUTCMinutes())) + ((getUTCSeconds())<10)
                    ? ":0" : ":") + str(getUTCSeconds()))));
    '''
    print target_time


def waiting_progress(start_time, target_time):
    '''
    var tmpTime:Date;
    var tmpTime2:Date;
    tmpTime = new Date();
    tmpTime2 = new Date();
    tmpTime.setTime(((target_time * 1000) - ((1000 * 60) * 60)));
    tmpTime2.setTime(((start_time * 1000) - ((1000 * 60) * 60)));
    return (((game_time.getTime() - tmpTime2.getTime())
            / (tmpTime.getTime() - tmpTime2.getTime())));
    '''
    print start_time, target_time


def log_on_rtl():
    '''
    if (text_dir == "right"){
        actor[LBL_NAME].x = (((IF_WIN_X + IF_GOTO_LOGIN_X) - 15)
                             - actor[LBL_NAME].text_width);
        actor[LBL_LOGIN_PASSWORD].x = (((IF_WIN_X + IF_GOTO_LOGIN_X) - 15)
                                       - actor[LBL_LOGIN_PASSWORD].text_width);
        actor[LBL_EMAIL].x = (((IF_WIN_X + IF_GOTO_LOGIN_X) - 15)
                              - actor[LBL_EMAIL].text_width);
        actor[LBL_PASSWORD].x = (((IF_WIN_X + IF_GOTO_LOGIN_X) - 15)
                                 - actor[LBL_PASSWORD].text_width);
        actor[INP['NAME']].x = (IF_WIN_X + IF_WIN_INPUTS_X);
        actor[INP['LOGIN_PASSWORD']].x = (IF_WIN_X + IF_WIN_INPUTS_X);
        actor[INP['EMAIL']].x = (IF_WIN_X + IF_WIN_INPUTS_X);
        actor[INP['PASSWORD']].x = (IF_WIN_X + IF_WIN_INPUTS_X);
    };
    '''
    pass


def modify_character(evt):
    '''
    var actor_id:* = 0;
    var evt:* = evt;
    var RemoveColorOffset:* = function (val, type){
        if ((get_char_image_bound(charface.volk, charface.male, 11) & type)){
            while (val >= 100) {
                val = (val - 100);
            };
        };
        return (val);
    };
    var AddColorOffset:* = function (val, type){
        if ((get_char_image_bound(charface.volk, charface.male, 11) & type)){
            val = (val + (100 * charface.color));
        };
        return (val);
    };
    actor_id = get_actor_id(evt.target);
    charface.hair = RemoveColorOffset(charface.hair, C_HAIR);
    charface.brows = RemoveColorOffset(charface.brows, C_BROWS);
    charface.beard = RemoveColorOffset(charface.beard, C_BEARD);
    charface.special2 = RemoveColorOffset(charface.special2, C_SPECIAL2);
    Switch (actor_id){
        if case(MOUTH_MINUS:
            charface.mouth--;
            if (charface.mouth < 1){
                charface.mouth = get_char_image_bound(charface.volk,
                                                      charface.male, 1);
            };
            break;
        if case(MOUTH_PLUS:
            charface.mouth++;
            if (charface.mouth > get_char_image_bound(charface.volk,
                charface.male, 1)){
                charface.mouth = 1;
            };
            break;
        if case(HAIR_MINUS:
            charface.hair--;
            if (charface.hair < 1){
                charface.hair = get_char_image_bound(charface.volk,
                                                     charface.male, 7);
            };
            break;
        if case(HAIR_PLUS:
            charface.hair++;
            if (charface.hair > get_char_image_bound(charface.volk,
                charface.male, 7)){
                charface.hair = 1;
            };
            break;
        if case(BROWS_MINUS:
            charface.brows--;
            if (charface.brows < 1){
                charface.brows = get_char_image_bound(charface.volk,
                                                      charface.male, 5);
            };
            break;
        if case(BROWS_PLUS:
            charface.brows++;
            if (charface.brows > get_char_image_bound(charface.volk,
                charface.male, 5)){
                charface.brows = 1;
            };
            break;
        if case(EYES_MINUS:
            charface.eyes--;
            if (charface.eyes < 1){
                charface.eyes = get_char_image_bound(charface.volk,
                                                     charface.male, 4);
            };
            break;
        if case(EYES_PLUS:
            charface.eyes++;
            if (charface.eyes > get_char_image_bound(charface.volk,
                                                     charface.male, 4)){
                charface.eyes = 1;
            };
            break;
        if case(BEARD_MINUS:
            charface.beard--;
            if (charface.beard < 1){
                charface.beard = get_char_image_bound(charface.volk,
                                                      charface.male, 2);
            };
            break;
        if case(BEARD_PLUS:
            charface.beard++;
            if (charface.beard > get_char_image_bound(charface.volk,
                charface.male, 2)){
                charface.beard = 1;
            };
            break;
        if case(NOSE_MINUS:
            charface.nose--;
            if (charface.nose < 1){
                charface.nose = get_char_image_bound(charface.volk,
                                                     charface.male, 3);
            };
            break;
        if case(NOSE_PLUS:
            charface.nose++;
            if (charface.nose > get_char_image_bound(charface.volk,
                charface.male, 3)){
                charface.nose = 1;
            };
            break;
        if case(EARS_MINUS:
            charface.ears--;
            if (charface.ears < 1){
                charface.ears = get_char_image_bound(charface.volk,
                                                     charface.male, 6);
            };
            break;
        if case(EARS_PLUS:
            charface.ears++;
            if (charface.ears > get_char_image_bound(charface.volk,
                charface.male, 6)){
                charface.ears = 1;
            };
            break;
        if case(SPECIAL_MINUS:
            charface.special--;
            if (charface.special < 1){
                charface.special = get_char_image_bound(charface.volk,
                                                        charface.male, 8);
            };
            break;
        if case(SPECIAL_PLUS:
            charface.special++;
            if (charface.special > get_char_image_bound(charface.volk,
                charface.male, 8)){
                charface.special = 1;
            };
            break;
        if case(SPECIAL2_MINUS:
            charface.special2--;
            if (charface.special2 < 1){
                charface.special2 = get_char_image_bound(charface.volk,
                                                         charface.male, 9);
            };
            break;
        if case(SPECIAL2_PLUS:
            charface.special2++;
            if (charface.special2 > get_char_image_bound(charface.volk,
                charface.male, 9)){
                charface.special2 = 1;
            };
            break;
        if case(COLOR_PLUS:
            charface.color++;
            if (charface.color > get_char_image_bound(charface.volk,
                charface.male, 10)){
                charface.color = 1;
            };
            break;
        if case(COLOR_MINUS:
            charface.color--;
            if (charface.color < 1){
                charface.color = get_char_image_bound(charface.volk,
                                                      charface.male, 10);
            };
            break;
    };
    charface.hair = AddColorOffset(charface.hair, C_HAIR);
    charface.brows = AddColorOffset(charface.brows, C_BROWS);
    charface.beard = AddColorOffset(charface.beard, C_BEARD);
    charface.special2 = AddColorOffset(charface.special2, C_SPECIAL2);
    load_character_image();
    '''
    print evt


def load_character_image(actor_id=0, load_only=False, is_volk=0,
                         is_mann=False, is_kaste=0, is_mouth=0,
                         is_beard=0, is_nose=0, is_eyes=0, is_brows=0,
                         is_ears=0, is_hair=0, is_special=0,
                         is_special2=0):
    '''
    var charPrefix:* = None;
    var i:* = 0;
    var actorOffset:* = 0;
    var actor_id = actor_id;
    var load_only:Boolean = load_only;
    var is_volk = is_volk;
    var is_mann:Boolean = is_mann;
    var is_kaste = is_kaste;
    var is_mouth = is_mouth;
    var is_beard = is_beard;
    var is_nose = is_nose;
    var is_eyes = is_eyes;
    var is_brows = is_brows;
    var is_ears = is_ears;
    var is_hair = is_hair;
    var is_special = is_special;
    var is_special2 = is_special2;
    var LoadCharacterItemImage:* = function (localActorID,
                                             parURL:String, item_index):
        var newLoad:Boolean;
        var url:String;
        url = (img_url[img_url_index] + parURL);
        if ((((item_index > 0)) and ((get_char_image_bound(is_volk,
            is_mann, item_index) == 0)))){
            url = (img_url[img_url_index] + "res/gfx/empty.png");
        };
        newLoad = !((actorURL[localActorID] == url));
        actorURL[localActorID] = url;
        if (newLoad){
            actorLoaded[localActorID] = 0;
            load(localActorID);
        };
    };
    charPrefix = get_char_prefix(False, is_volk, is_mann, is_kaste);
    if (actor_id == C_EMPTY){
        if (on_stage(SCR_BUILDCHAR_BACKGROUND)){
            var _local16 = actor[LBL_CREATE_RACE];
            with (_local16) {
                text = texts[((TXT_RACENAME + charface.volk) - 1)];
                if (text_dir == "right"){
                    x = ((actor[LBL_CREATE_RACE_DESC].x
                         + actor[LBL_CREATE_RACE_DESC].width) - text_width);
                };
            };
            _local16 = actor[LBL_CREATE_RACE_DESC];
            with (_local16) {
                text = texts[((TXT_RACEDESC + charface.volk) - 1)];
                y = ((actor[LBL_CREATE_RACE].y
                     + actor[LBL_CREATE_RACE].textHeight) + BUILDCHAR_LINES_Y);
            };
            arabize(LBL_CREATE_RACE_DESC);
            _local16 = actor[LBL_CREATE_CLASS];
            with (_local16) {
                text = texts[((KlasseGewählt)
                              ? ((TXT_CLASSNAME + charface.class) - 1)
                              : TXT_NOCLASS)];
                y = ((actor[LBL_CREATE_RACE_DESC].y
                     + actor[LBL_CREATE_RACE_DESC].textHeight)
                     + BUILDCHAR_LINES_Y);
                if (text_dir == "right"){
                    x = ((actor[LBL_CREATE_RACE_DESC].x
                         + actor[LBL_CREATE_RACE_DESC].width) - text_width);
                };
            };
            _local16 = actor[LBL_CREATE_CLASS_DESC];
            with (_local16) {
                text = texts[((KlasseGewählt)
                              ? ((TXT_CLASSDESC + charface.class) - 1)
                              : TXT_NOCLASS_DESC)];
                y = ((actor[LBL_CREATE_CLASS].y +
                     actor[LBL_CREATE_CLASS].textHeight)
                    + BUILDCHAR_LINES_Y);
            };
            arabize(LBL_CREATE_CLASS_DESC);
        };
        load_character_image(CHARBACKGROUND, load_only, charface.volk,
                             charface.male,
                           charface.class, charface.mouth, charface.beard,
                           charface.nose,
                           charface.eyes, charface.brows, charface.ears,
                           charface.hair,
                           charface.special, charface.special2);
        if (on_stage(SCR_BUILDCHAR_BACKGROUND)){
            remove(VOLK_BTNS_ALL);
            add(F_IDLE);
            add(M_IDLE);
            if (charface.male){
                add(VOLK_BTNS_M);
                add(((VOLK_1_M_ACT + charface.volk) - 1));
                add(M_ACT);
            } else {
                add(VOLK_BTNS_F);
                add(((VOLK_1_F_ACT + charface.volk) - 1));
                add(F_ACT);
            };
            add(KASTE_1_IDLE);
            add(KASTE_2_IDLE);
            add(KASTE_3_IDLE);
            if (KlasseGewählt){
                add((KASTE_1_ACT + ((charface.class - 1) * 2)));
            };
            i = 1;
            while (i < 11) {
                if (get_char_image_bound(char_volk, char_male, i) == 0){
                    remove((MOUTH_MINUS + ((i - 1) * 2)));
                    remove((MOUTH_PLUS + ((i - 1) * 2)));
                    remove((LBL_MOUTH + (i - 1)));
                } else {
                    add((MOUTH_MINUS + ((i - 1) * 2)));
                    add((MOUTH_PLUS + ((i - 1) * 2)));
                    add((LBL_MOUTH + (i - 1)));
                };
                i = (i + 1);
            };
            pos_modify_char_buttons();
            if (!on_stage(CREATE_CHARACTER)){
                remove(CREATE_GOTO_LOGIN, KASTE_1_IDLE, KASTE_2_IDLE,
                       KASTE_3_IDLE, KASTE_1_ACT, KASTE_2_ACT, KASTE_3_ACT,
                       CREATE_CHARACTER, BLACK_SQUARE);
                add_some(MODIFY_CHARACTER, IF_EXIT);
            };
        };
        return;
    };
    LoadCharacterItemImage(actor_id,
                           (charPrefix + get_char_suffix(0, is_kaste)), 0);
    LoadCharacterItemImage((actor_id + 1),
                           (charPrefix + get_char_suffix(1, is_mouth)), 1);
    LoadCharacterItemImage((actor_id + 2),
                           (charPrefix + get_char_suffix(2, is_beard)), 2);
    LoadCharacterItemImage((actor_id + 3),
                           (charPrefix + get_char_suffix(3, is_nose)), 3);
    LoadCharacterItemImage((actor_id + 4),
                           (charPrefix + get_char_suffix(4, is_eyes)), 4);
    LoadCharacterItemImage((actor_id + 5),
                           (charPrefix + get_char_suffix(5, is_brows)), 5);
    LoadCharacterItemImage((actor_id + 6),
                           (charPrefix + get_char_suffix(6, is_ears)), 6);
    LoadCharacterItemImage((actor_id + 7),
                           (charPrefix + get_char_suffix(7, is_hair)), 7);
    LoadCharacterItemImage((actor_id + 8),
                           (charPrefix + get_char_suffix(8, is_special)), 8);
    LoadCharacterItemImage((actor_id + 9),
                           (charPrefix + get_char_suffix(9, is_special2)), 9);
    actorOffset = (actor_id - CHARBACKGROUND);
    if (!load_only){
        add((CHARIMG + actorOffset));
        if ((((is_volk == 2)) and (is_mann))){
            add_bmo(CHARSPECIALOVL_ELF_M, actorOffset);
        };
        if ((((is_volk == 7)) and (is_mann))){
            add_bmo(CHARSPECIALOVL_GOBLIN_M, actorOffset);
        };
        if ((((is_volk == 6)) and (is_mann))){
            add_bmo(CHARSPECIALOVL_DARKELF_M, actorOffset);
        };
        if ((((is_volk == 3)) and (is_mann))){
            add_bmo(CHARSPECIALOVL_DWARF_M, actorOffset);
        };
        if ((((is_volk == 1)) and (is_mann))){
            add_bmo(CHARSPECIALOVL_HUMAN_M, actorOffset);
        };
        if ((((is_volk == 4)) and (is_mann))){
            add_bmo(CHARSPECIALOVL_GNOM_M, actorOffset);
        };
        if ((((is_volk == 7)) and (!(is_mann)))){
            add_bmo(CHARSPECIALOVL_GOBLIN_F, actorOffset);
        };
        if ((((is_volk == 5)) and (!(is_mann)))){
            add_bmo(CHARSPECIALOVL_ORC_F, actorOffset);
        };
        if ((((is_volk == 2)) and (!(is_mann)))){
            add_bmo(CHARSPECIALOVL_ELF_F, actorOffset);
        };
        if ((((is_volk == 1)) and (!(is_mann)))){
            add_bmo(CHARSPECIALOVL_HUMAN_F, actorOffset);
        };
        if ((((is_volk == 3)) and (!(is_mann)))){
            add_bmo(CHARSPECIALOVL_DWARF_F, actorOffset);
        };
    };
    '''
    print actor_id, load_only, is_volk, is_mann, is_kaste, is_mouth, is_beard,
    print is_nose, is_eyes, is_brows, is_ears, is_hair, is_special, is_special2


def pos_modify_char_buttons():
    '''
    var i:* = 0;
    var positionmodify_characterBtn:* = function (actor_id):
        if (on_stage(actor_id)){
            actor[actor_id].y = (MODIFY_CHARACTER_BUTTONS_Y
                                 + (iPosi++ * MODIFY_CHARACTER_BUTTONS_1));
        };
    };
    var iPosi:* = 0;
    positionmodify_characterBtn(EYES_PLUS);
    positionmodify_characterBtn(BROWS_PLUS);
    positionmodify_characterBtn(MOUTH_PLUS);
    positionmodify_characterBtn(NOSE_PLUS);
    positionmodify_characterBtn(EARS_PLUS);
    positionmodify_characterBtn(HAIR_PLUS);
    positionmodify_characterBtn(COLOR_PLUS);
    positionmodify_characterBtn(BEARD_PLUS);
    positionmodify_characterBtn(SPECIAL_PLUS);
    positionmodify_characterBtn(SPECIAL2_PLUS);
    i = 0;
    while (i < 10) {
        if (text_dir == "right"){
            actor[(LBL_MOUTH + i)].x = ((MODIFY_CHARACTER_BUTTONS_X
                                - actor[(LBL_MOUTH + i)].text_width) + 20);
            actor[(MOUTH_MINUS + (i * 2))].x = (MODIFY_CHARACTER_BUTTONS_X
                                                + MODIFY_CHARACTER_LABEL_X);
            actor[(MOUTH_PLUS + (i * 2))].x = (actor[(MOUTH_MINUS + (i * 2))].x
                                               + MODIFY_CHARACTER_BUTTONS_2);
            actor[(MOUTH_MINUS + (i * 2))].y = actor[(MOUTH_PLUS + (i * 2))].y;
            actor[(LBL_MOUTH + i)].y = (actor[(MOUTH_PLUS + (i * 2))].y
                                        + MODIFY_CHARACTER_LABEL_Y);
        } else {
            actor[(MOUTH_MINUS + (i * 2))].x = MODIFY_CHARACTER_BUTTONS_X;
            actor[(MOUTH_PLUS + (i * 2))].x = (actor[(MOUTH_MINUS + (i * 2))].x
                                               + MODIFY_CHARACTER_BUTTONS_2);
            actor[(MOUTH_MINUS + (i * 2))].y = actor[(MOUTH_PLUS + (i * 2))].y;
            actor[(LBL_MOUTH + i)].x = (actor[(MOUTH_PLUS + (i * 2))].x
                                        + MODIFY_CHARACTER_LABEL_X);
            actor[(LBL_MOUTH + i)].y = (actor[(MOUTH_PLUS + (i * 2))].y
                                        + MODIFY_CHARACTER_LABEL_Y);
        };
        i = (i + 1);
    };
    '''
    pass


def get_char_suffix(item_index, item_value):
    '''
    var strItem:String;
    var strExt:String;
    var colorIndex;
    var colorString:String;
    strExt = C_CHAREXT;
    colorIndex = 0;
    colorString = "";
    while (item_value > 100) {
        item_value = (item_value - 100);
        colorIndex++;
    };
    if (colorIndex > 0){
        colorString = (("_" + str(colorIndex)) + "_");
    };
    Switch (item_index){
        if case(0:
            strExt = ".jpg";
            Switch (item_value){
                if case(1:
                    strItem = "body_hunter";
                    break;
                if case(2:
                    strItem = "body_mage";
                    break;
                if case(3:
                    strItem = "body_warrior";
                    break;
            };
            break;
        if case(1:
            strItem = ("mund" + str(item_value));
            break;
        if case(2:
            strItem = (("bart" + colorString) + str(item_value));
            break;
        if case(-2:
            strItem = ("tattoo" + str(item_value));
            break;
        if case(3:
            strItem = ("nase" + str(item_value));
            break;
        if case(4:
            strItem = ("augen" + str(item_value));
            break;
        if case(5:
            strItem = (("brauen" + colorString) + str(item_value));
            break;
        if case(6:
            strItem = ("ohren" + str(item_value));
            break;
        if case(7:
            strItem = (("haare" + colorString) + str(item_value));
            break;
        if case(8:
            strItem = ("special" + str(item_value));
            break;
        if case(9:
            strItem = (("special2" + colorString) + str(item_value));
            break;
    };
    return ((strItem + strExt));
    '''
    print item_index, item_value


def randomize_character():
    '''
    char_volk = (int((random.random() * 8)) + 1);
    char_male = (random.random() > 0.5);
    if (param_obj["playerclass"]){
        char_class = int(param_obj["playerclass"]);
        if (char_class < 1){
            char_class = 1;
        };
        if (char_class > 3){
            char_class = 3;
        };
        KlasseGewählt = True;
    } else {
        char_class = (int((random.random() * 3)) + 1);
        KlasseGewählt = False;
    };
    randomize_char_image();
    '''
    pass


def randomize_char_image(evt=None):
    '''
    var evt:* = evt;
    var ColorOffset:* = function (ItemID){
        if ((get_char_image_bound(char_volk, char_male, 11) & ItemID)){
            return ((char_color * 100));
        };
        return (0);
    };
    char_color = int(((random.random() * get_char_image_bound(char_volk,
                     char_male, 10)) + 1));
    char_mouth = int(((random.random() * get_char_image_bound(char_volk,
                     char_male, 1)) + 1));
    char_beard = (int(((random.random() * get_char_image_bound(char_volk,
                  char_male, 2)) + 1)) + ColorOffset(C_BEARD));
    char_nose = int(((random.random() * get_char_image_bound(char_volk,
                    char_male, 3)) + 1));
    char_eyes = int(((random.random() * get_char_image_bound(char_volk,
                    char_male, 4)) + 1));
    char_brows = (int(((random.random() * get_char_image_bound(char_volk,
                  char_male, 5)) + 1)) + ColorOffset(C_BROWS));
    char_ears = int(((random.random() * get_char_image_bound(char_volk,
                    char_male, 6)) + 1));
    char_hair = (int(((random.random() * get_char_image_bound(char_volk,
                 char_male, 7)) + 1)) + ColorOffset(C_HAIR));
    char_special = int(((random.random() * get_char_image_bound(char_volk,
                       char_male, 8)) + 1));
    char_special2 = (int(((random.random() * get_char_image_bound(char_volk,
                     char_male, 9)) + 1)) + ColorOffset(C_SPECIAL2));
    load_character_image();
    '''
    print evt


def get_char_image_bound(is_volk, is_mann, item_index):
    '''
    if (is_mann){
        Switch (is_volk){
            if case(1:
                Switch (item_index){
                    if case(1:
                        return (9);
                    if case(2:
                        return (13);
                    if case(3:
                        return (6);
                    if case(4:
                        return (7);
                    if case(5:
                        return (7);
                    if case(6:
                        return (5);
                    if case(7:
                        return (11);
                    if case(8:
                        return (17);
                    if case(9:
                        return (0);
                    if case(10:
                        return (5);
                    if case(11:
                        return (((C_BROWS + C_HAIR) + C_BEARD));
                };
            if case(2:
                Switch (item_index){
                    if case(1:
                        return (8);
                    if case(2:
                        return (7);
                    if case(3:
                        return (7);
                    if case(4:
                        return (8);
                    if case(5:
                        return (5);
                    if case(6:
                        return (4);
                    if case(7:
                        return (10);
                    if case(8:
                        return (13);
                    if case(9:
                        return (0);
                    if case(10:
                        return (3);
                    if case(11:
                        return (((C_HAIR + C_BROWS) + C_BEARD));
                };
            if case(3:
                Switch (item_index){
                    if case(1:
                        return (5);
                    if case(2:
                        return (5);
                    if case(3:
                        return (5);
                    if case(4:
                        return (8);
                    if case(5:
                        return (5);
                    if case(6:
                        return (5);
                    if case(7:
                        return (10);
                    if case(8:
                        return (13);
                    if case(9:
                        return (0);
                    if case(10:
                        return (5);
                    if case(11:
                        return (((C_BROWS + C_HAIR) + C_BEARD));
                };
            if case(4:
                Switch (item_index){
                    if case(1:
                        return (10);
                    if case(2:
                        return (12);
                    if case(3:
                        return (6);
                    if case(4:
                        return (9);
                    if case(5:
                        return (9);
                    if case(6:
                        return (6);
                    if case(7:
                        return (12);
                    if case(8:
                        return (17);
                    if case(9:
                        return (0);
                    if case(10:
                        return (5);
                    if case(11:
                        return (((C_HAIR + C_BEARD) + C_BROWS));
                };
            if case(5:
                Switch (item_index){
                    if case(1:
                        return (7);
                    if case(2:
                        return (5);
                    if case(3:
                        return (5);
                    if case(4:
                        return (6);
                    if case(5:
                        return (5);
                    if case(6:
                        return (5);
                    if case(7:
                        return (10);
                    if case(8:
                        return (9);
                    if case(9:
                        return (0);
                    if case(10:
                        return (5);
                    if case(11:
                        return ((C_HAIR + C_BEARD));
                };
            if case(6:
                Switch (item_index){
                    if case(1:
                        return (6);
                    if case(2:
                        return (6);
                    if case(3:
                        return (5);
                    if case(4:
                        return (5);
                    if case(5:
                        return (5);
                    if case(6:
                        return (5);
                    if case(7:
                        return (8);
                    if case(8:
                        return (12);
                    if case(9:
                        return (0);
                    if case(10:
                        return (3);
                    if case(11:
                        return (((C_HAIR + C_BEARD) + C_BROWS));
                };
            if case(7:
                Switch (item_index){
                    if case(1:
                        return (6);
                    if case(2:
                        return (8);
                    if case(3:
                        return (5);
                    if case(4:
                        return (9);
                    if case(5:
                        return (6);
                    if case(6:
                        return (5);
                    if case(7:
                        return (12);
                    if case(8:
                        return (12);
                    if case(9:
                        return (0);
                    if case(10:
                        return (0);
                    if case(11:
                        return (0);
                };
            if case(8:
                Switch (item_index){
                    if case(1:
                        return (9);
                    if case(2:
                        return (10);
                    if case(3:
                        return (6);
                    if case(4:
                        return (7);
                    if case(5:
                        return (5);
                    if case(6:
                        return (5);
                    if case(7:
                        return (0);
                    if case(8:
                        return (17);
                    if case(9:
                        return (11);
                    if case(10:
                        return (5);
                    if case(11:
                        return ((C_BEARD + C_SPECIAL2));
                };
        };
    } else {
        Switch (is_volk){
            if case(1:
                Switch (item_index){
                    if case(1:
                        return (8);
                    if case(2:
                        return (0);
                    if case(3:
                        return (6);
                    if case(4:
                        return (6);
                    if case(5:
                        return (6);
                    if case(6:
                        return (6);
                    if case(7:
                        return (8);
                    if case(8:
                        return (5);
                    if case(9:
                        return (0);
                    if case(10:
                        return (4);
                    if case(11:
                        return ((C_BROWS + C_HAIR));
                };
            if case(2:
                Switch (item_index){
                    if case(1:
                        return (8);
                    if case(2:
                        return (0);
                    if case(3:
                        return (8);
                    if case(4:
                        return (7);
                    if case(5:
                        return (8);
                    if case(6:
                        return (7);
                    if case(7:
                        return (8);
                    if case(8:
                        return (5);
                    if case(9:
                        return (0);
                    if case(10:
                        return (4);
                    if case(11:
                        return ((C_HAIR + C_BROWS));
                };
            if case(3:
                Switch (item_index){
                    if case(1:
                        return (9);
                    if case(2:
                        return (0);
                    if case(3:
                        return (6);
                    if case(4:
                        return (6);
                    if case(5:
                        return (8);
                    if case(6:
                        return (4);
                    if case(7:
                        return (8);
                    if case(8:
                        return (4);
                    if case(9:
                        return (0);
                    if case(10:
                        return (4);
                    if case(11:
                        return ((C_HAIR + C_BROWS));
                };
            if case(4:
                Switch (item_index){
                    if case(1:
                        return (7);
                    if case(2:
                        return (0);
                    if case(3:
                        return (7);
                    if case(4:
                        return (6);
                    if case(5:
                        return (6);
                    if case(6:
                        return (6);
                    if case(7:
                        return (8);
                    if case(8:
                        return (5);
                    if case(9:
                        return (0);
                    if case(10:
                        return (4);
                    if case(11:
                        return ((C_HAIR + C_BROWS));
                };
            if case(5:
                Switch (item_index){
                    if case(1:
                        return (7);
                    if case(2:
                        return (0);
                    if case(3:
                        return (5);
                    if case(4:
                        return (6);
                    if case(5:
                        return (5);
                    if case(6:
                        return (4);
                    if case(7:
                        return (8);
                    if case(8:
                        return (7);
                    if case(9:
                        return (0);
                    if case(10:
                        return (4);
                    if case(11:
                        return (C_HAIR);
                };
            if case(6:
                Switch (item_index){
                    if case(1:
                        return (9);
                    if case(2:
                        return (0);
                    if case(3:
                        return (6);
                    if case(4:
                        return (6);
                    if case(5:
                        return (6);
                    if case(6:
                        return (3);
                    if case(7:
                        return (6);
                    if case(8:
                        return (5);
                    if case(9:
                        return (0);
                    if case(10:
                        return (3);
                    if case(11:
                        return (C_HAIR);
                };
            if case(7:
                Switch (item_index){
                    if case(1:
                        return (9);
                    if case(2:
                        return (0);
                    if case(3:
                        return (5);
                    if case(4:
                        return (6);
                    if case(5:
                        return (5);
                    if case(6:
                        return (4);
                    if case(7:
                        return (8);
                    if case(8:
                        return (4);
                    if case(9:
                        return (0);
                    if case(10:
                        return (4);
                    if case(11:
                        return (C_HAIR);
                };
            if case(8:
                Switch (item_index){
                    if case(1:
                        return (8);
                    if case(2:
                        return (5);
                    if case(3:
                        return (7);
                    if case(4:
                        return (6);
                    if case(5:
                        return (5);
                    if case(6:
                        return (4);
                    if case(7:
                        return (7);
                    if case(8:
                        return (6);
                    if case(9:
                        return (4);
                    if case(10:
                        return (3);
                    if case(11:
                        return (C_HAIR);
                };
        };
    };
    return (0);
    '''
    print is_volk, is_mann, item_index


def get_char_prefix(is_gut, isinstance_volk, is_mann, is_kaste):
    '''
    var strTemp:String;
    var strRace:String;
    strTemp = "res/gfx/char/";
    strRace = "";
    Switch (is_volk){
        if case(1:
            strRace = "human";
            break;
        if case(2:
            strRace = "elf";
            break;
        if case(3:
            strRace = "dwarf";
            break;
        if case(4:
            strRace = "gnome";
            break;
        if case(5:
            strRace = "orc";
            break;
        if case(6:
            strRace = "dunkelelf";
            break;
        if case(7:
            strRace = "goblin";
            break;
        if case(8:
            strRace = "demon";
            break;
    };
    strTemp = (strTemp + (strRace + " "));
    strTemp = (strTemp + ((is_mann) ? "m" : "f"));
    strTemp = (strTemp + (("/" + strRace) + "_"));
    if (!is_mann){
        strTemp = (strTemp + "female_");
    };
    return (strTemp);
    '''
    print is_gut, isinstance_volk, is_mann, is_kaste


def drachen_setzen():
    '''
    var i;
    var d;
    var x;
    var y;
    i = IF_DRAGON_1;
    while (i <= IF_DRAGON_13) {
        x = actor[i].x;
        y = actor[i].y;
        delete actor[i];
        d = (random.random() * 5);
        actorBitmap[i] = d;
        Switch (d){
            if case(0:
                actor[i] = new interface_dragon1_png();
                break;
            if case(1:
                actor[i] = new interface_dragon2_png();
                break;
            if case(2:
                actor[i] = new interface_dragon3_png();
                break;
            if case(3:
                actor[i] = new interface_dragon4_png();
                break;
            if case(4:
            if case(5:
                actor[i] = new interface_dragon6_png();
                break;
        };
        actor[i].x = x;
        actor[i].y = y;
        addChild(actor[i]);
        i++;
    };
    '''
    pass


def interface_btn_handler(evt):
    '''
    var tmpAction;
    tmpAction = 0;
    Switch (get_actor_id(evt.target)){
        if case(CA_CITY_SHAKES:
        if case(IF_SCHMIEDE:
            tmpAction = ACT_SCREEN_SCHMIEDE;
            break;
        if case(CA_CITY_RUHMESHALLE:
        if case(IF_EHRENHALLE:
            ruhmes_halle_such_string = actor[INP['NAME']].getChildAt(1).text;
            send_action(ACT_SCREEN_EHRENHALLE,
                        actor[INP['NAME']].getChildAt(1).text, -1);
            break;
        if case(CA_CITY_ARENA:
        if case(IF_ARENA:
            tmpAction = ACT_SCREEN_ARENA;
            break;
        if case(CA_CITY_ESEL:
        if case(IF_STALL:
            tmpAction = ACT_SCREEN_STALL;
            break;
        if case(CA_CITY_POST:
        if case(IF_POST:
            post_scroll = 1;
            send_action(ACT_SCREEN_POST, 1);
            break;
        if case(CA_CITY_WACHE:
        if case(IF_ARBEITEN:
            tmpAction = ACT_SCREEN_ARBEITEN;
            break;
        if case(IF_TAVERNE:
        if case(CA_CITY_TAVERNE:
        if case(HUTMANN_BACK:
            tmpAction = ACT_SCREEN_TAVERNE;
            break;
        if case(CA_CITY_ZAUBERLADEN:
        if case(IF_ZAUBERLADEN:
            tmpAction = ACT_SCREEN_ZAUBERLADEN;
            break;
        if case(IF_PILZDEALER:
        if case(CA_CITY_DEALER:
            tmpAction = ACT_SCREEN_PILZDEALER;
            break;
        if case(FIGHT_OK:
            tmpAction = ((post_fight_mode)
                         ? ACT_SCREEN_POST
                         : ACT['SCREEN']['CHAR']);
            if (hasFoughtGuildBattle){
                if (tower_fight_mode){
                    tmpAction = ACT_SCREEN_TOWER;
                } else {
                    tmpAction = ACT_SCREEN_GILDEN;
                };
            };
            if (hasLostMQ){
                hasLostMQ = False;
                tmpAction = 0;
                show_main_quest_screen(Lastdungeon_nr, LastDungeonenemy);
            };
            break;
        if case(IF_CHARAKTER:
            arrow_hall_mode = False;
            tmpAction = ACT['SCREEN']['CHAR'];
            break;
        if case(IF_GILDEN:
            pulse_gilde = False;
            pulse_gilde_on_history = False;
            tmpAction = ACT_SCREEN_GILDEN;
            break;
        if case(IF_WELTKARTE:
            tmpAction = ACT_SCREEN_WELTKARTE;
            break;
        if case(IF_OPTIONEN:
            tmpAction = ACT['SCREEN']['OPTIONEN'];
            break;
        if case(CA_CITY_BUH:
            slm_count++;
            break;
    };
    if (tmpAction > 0){
        send_action(tmpAction);
    };
    '''
    print evt


def chat_poll_interval_reset():
    '''
    if (param_poll_tunnel_url != ""){
        guild_chat_poll.stop();
        guild_chat_poll.start();
    };
    '''
    pass
