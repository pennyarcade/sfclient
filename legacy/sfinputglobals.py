#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html

    Input element constants
'''


# Label Texts
LBL = {
    "ALBUM": {
        "COLLECTION": 24379,
        "HEADING": 24380,
        "HINT": 24384,
        "PAGENUMBER_LEFT": 24377,
        "PAGENUMBER_RIGHT": 24378
    },
    "CHAR": {
        "ALBUM": 22966,
        "DELAY": 23077,
        "MOUNT": {
            "DESCR": 22988,
            "GAIN": 22990,
            "NAME": 22987,
            "RUNTIME": 22989
        },
        "RUESTUNG": 22992
    },
    "CREATE": {
        "CLASS": 198,
        "CLASS_DESC": 199,
        "GOTO_LOGIN": 201,
        "RACE": 196,
        "RACE_DESC": 197
    },
    "DEALER": {
        "PAYICON": {
            "1": 23244,
            "2": 23245,
            "3": 23246,
            "4": 23247,
            "5": 23248,
            "6": 23249,
            "7": 23250,
            "8": 23251,
            "9": 23252
        }
    },
    "EMAIL": {
        "TXT": 52,
        "NAG": 24371,
        "RESEND": 24373
    },
    "FIGHT": {
        "CHAR": {
            "AUSDAUER": 24166,
            "AUSDAUER_CAPTION": 24176,
            "BEWEGLICHKEIT": 24165,
            "BEWEGLICHKEIT_CAPTION": 24175,
            "INTELLIGENZ": 24167,
            "INTELLIGENZ_CAPTION": 24177,
            "STAERKE": 24164,
            "STAERKE_CAPTION": 24174,
            "WILLENSKRAFT": 24168,
            "WILLENSKRAFT_CAPTION": 24178
        },
        "OPP": {
            "AUSDAUER": 24171,
            "AUSDAUER_CAPTION": 24181,
            "BEWEGLICHKEIT": 24170,
            "BEWEGLICHKEIT_CAPTION": 24180,
            "INTELLIGENZ": 24172,
            "INTELLIGENZ_CAPTION": 24182,
            "STAERKE": 24169,
            "STAERKE_CAPTION": 24179,
            "WILLENSKRAFT": 24173,
            "WILLENSKRAFT_CAPTION": 24183
        },
        "OPPGUILD": 23833,
        "PLAYERGUILD": 23832,
        "REWARDEXP": 24209,
        "REWARDGOLD": 24203,
        "REWARDMUSH": 24207,
        "REWARDSILVER": 24205,
        "SUMMARY": 24197
    },
    "GILDE": {
        "ATTACK": 0x5B5B,
        "CHAT": 23406,
        "CHAT_CAPTION": 23405,
        "CREST_ELEMENT": 24557,
        "CREST_INSCRIPTION": 24558,
        "DEFENCE": 23388,
        "DIALOG": {
            "TEXT": {
                "INVITE": 23504,
                "KICK": 23502,
                "MASTER": 23503,
                "QUIT": 23501,
                "RAID": 23506,
                "REVOLT": 23505
            }
        },
        "GEBAEUDE": {
            "KOSTEN_GOLD": 23468,
            "KOSTEN_MUSH": 23471,
            "NAME": 23453,
            "STUFE": 23465,
            "STUFE_CAPTION": 23462,
            "WERT": 23459,
            "WERT_CAPTION": 23456
        },
        "GOLD": 23487,
        "GOLD2": 23493,
        "GRUENDEN_TEXT": 23361,
        "LINK": 23447,
        "MUSH": 23488,
        "MUSH2": 23494,
        "RANG": 23366,
        "TITEL": 23364
    },
    "HALL": {
        "GOTO": {
            "GILDEN": 292,
            "GILDEN_HL": 293,
            "SPIELER": 289,
            "SPIELER_HL": 290
        }
    },
    "HUTMANN": {
        "GOLDBET": 23567,
        "GOLDBET2": 23574,
        "INSTR": 23580,
        "MUSHBET": 23568,
        "MUSHBET2": 23575,
        "TEXT": 23566
    },
    "IF": {
        "AGB": 20,
        "ANLEITUNG": 24,
        "DATENSCHUTZ": 22,
        "FORUM": 16,
        "GOLD": 30,
        "IMPRESSUM": 14,
        "LOGOUT": 12,
        "PILZE": 32,
        "SHOP": 26,
        "SILBER": 31
    },
    "INVITE": {
        "SUCCESS": 22976,
        "TEXT": {
            "1": 22968,
            "2": 22970,
            "3": 22972
        }
    },
    "LOGIN": {
        "LEGAL": {
            "0": 80,
            "LEGAL_1": 71,
            "LEGAL_2": 74
        },
        "PASSWORD": 59
    },
    "MAINQUEST": {
        "MUSHHINT": 24360,
        "TEXT": 24359,
        "TITLE": 24358,
        "TITLE1": 24309
    },
    "OPTION": {
        "CHANGE": 24250,
        "DOCHANGE": 24257,
        "FIELD": {
            "1": 24258,
            "2": 24259,
            "3": 24260
        },
        "IMAGE": 24247,
        "TITLE": 24246,
        "VER": 24282,
        "VOLUME": 24268
    },
    "POST": {
        "_FLUSH_TEXT": 24596,
        "GUILD": 23290,
        "LIMIT": 23288,
        "TITLE": {
            "INBOX": 23266,
            "READ": 23267,
            "WRITE": 23268
        }
    },
    "QO": {
        "CHOICE": {
            "1": 23596,
            "1_HL": 23601,
            "2": 23597,
            "2_HL": 23602,
            "3": 23598,
            "3_HL": 23603,
            "4": 23599,
            "4_HL": 23604,
            "5": 23600,
            "5_HL": 23605
        },
        "CHOOSE": 23590,
        "QUESTNAME": 23606,
        "QUESTSTODAY": 23618,
        "QUESTTEXT": 23607,
        "REWARD": {
            "TXT": 23608,
            "EXP": 23613,
            "GOLD": 23610,
            "ITM": 23614,
            "SILVER": 23612
        },
        "TIME": 23615
    },
    "SCR": {
        "ARBEITEN": {
            "TEXT": 296,
            "TEXT2": 297,
            "TIME": 315
        },
        "CHAR": {
            "AUSDAUER": 365,
            "AUSDAUER_CAPTION": 375,
            "BEWEGLICHKEIT": 364,
            "BEWEGLICHKEIT_CAPTION": 374,
            "EHRE": 22956,
            "EXPLABEL": 359,
            "GILDE": 22955,
            "INTELLIGENZ": 366,
            "INTELLIGENZ_CAPTION": 376,
            "KAMPFWERT": 369,
            "KAMPFWERT_CAPTION": 379,
            "LEBEN": 370,
            "LEBEN_CAPTION": 380,
            "NAME": 355,
            "PREIS1": 388,
            "RUESTUNG": 371,
            "RUESTUNG_CAPTION": 381,
            "SCHADEN": 368,
            "SCHADEN_CAPTION": 378,
            "SILBER1": 398,
            "STAERKE": 363,
            "STAERKE_CAPTION": 373,
            "WIDERSTAND": 372,
            "WIDERSTAND_CAPTION": 382,
            "WILLENSKRAFT": 367,
            "WILLENSKRAFT_CAPTION": 377
        }
    },
    "STALL": {
        "GAIN": 23347,
        "GOLD": 23353,
        "LAUFZEIT": 23346,
        "MUSH": 23355,
        "SCHATZ": 23348,
        "SCHATZGOLD": 23350,
        "SCHATZSILBER": 23352,
        "TEXT": 23345,
        "TITEL": 23344
    },
    "AGB": 70,
    "ARENA_DELAY": 23303,
    "ARENA_TEXT": 23299,
    "BEARD": 190,
    "BROWS": 188,
    "COLOR": 195,
    "COMPARE": 24626,
    "COPYCAT_NAME": 24738,
    "COUNTRY": 25617,
    "CS": 24484,
    "DAMAGE_INDICATOR": 24196,
    "DATENSCHUTZ": 73,
    "DISCONNECTED": 24368,
    "DUNGEON_CONGRATS": 24355,
    "EARS": 192,
    "ERROR": 61,
    "EYES": 189,
    "FORGOT_PASSWORD": 63,
    "FUCK": 85,
    "GOTO_LOGIN": 65,
    "GOTO_SIGNUP": 67,
    "HAIR": 187,
    "HERO_OF_THE_DAY": 24211,
    "HERO_OF_THE_DAY_TITLE": 24210,
    "HLMAINQUESTS_TITLE": 24762,
    "LIFEBAR_CHAR": 24162,
    "LIFEBAR_OPP": 24163,
    "LM": 24285,
    "MOUTH": 186,
    "NAME": 50,
    "NAMERANK_CHAR": 24156,
    "NAMERANK_OPP": 24157,
    "NOSE": 191,
    "PASSWORD": 54,
    "PW_GOTO_LOGIN": 25616,
    "QUESTBAR_TEXT": 23210,
    "SCREEN_TITLE": 113,
    "SERVER": 25620,
    "SPECIAL": 193,
    "SPECIAL2": 194,
    "TIMEBAR_TEXT": 23545,
    "TOILET_AURA": 24620,
    "TOWER_BOOSTPRICELABEL": 25604,
    "TOWER_EXPLABEL": 25603,
    "TV_CHECKBOX": 25705,
    "WINDOW_TITLE": 46,
    "WINDOW_TITLE_HIGH": 25614,
    "WORLD_TITLE": 25623
}


# Buttons
BTN = {
    "CHAR": {
        "ALBUM": 22964,
        "ATTACK": 22961,
        "GILDE": 22962,
        "INVITE": 22963,
        "MESSAGE": 22960,
        "ROB": 24741
    },
    "DEALER": {
        "BUY": {
            "1": 23223,
            "2": 23224,
            "3": 23225
        }
    },
    "GILDE": {
        "ATTACK": 23381,
        "CHAT_DOWN": 23404,
        "CHAT_UP": 23403,
        "CREST": {
            "CHANGE_NEXT": 24556,
            "CHANGE_PREV": 24555,
            "COLOR_NEXT": 24554,
            "COLOR_PREV": 24553,
            "GOTO_GEBAEUDE": 24542,
            "OK": 24589
        },
        "DEFEND": 23382,
        "DEMOTE": 23375,
        "DIALOG": {
            "CANCEL": 23508,
            "OK": {
                "INVITE": 23511,
                "KICK": 23509,
                "MASTER": 23510,
                "RAID": 23513,
                "REVOLT": 23512
            }
        },
        "GEBAEUDE_GOTO_CREST": 24540,
        "GEBAEUDE_IMPROVE": 23480,
        "GOLD": 23491,
        "GRUENDEN": 23363,
        "INVITE": 23371,
        "KATAPULT": 24507,
        "KICK": 23373,
        "MASTER": 23376,
        "MUSH": 23492,
        "PROFILE": 23372,
        "PROMOTE": 23374,
        "RAID": 23378,
        "REVOLT": 23377,
        "SCROLL_DOWN": 23370,
        "SCROLL_UP": 23369
    },
    "HALL": {
        "DOWN": 285,
        "GOTO": 286,
        "UP": 284
    },
    "HUTMANN": {
        "BACK": 23579,
        "GOLDBET": 23571,
        "MUSHBET": 23572,
        "OK": 23578
    },
    "IF": {
        "ARBEITEN": 101,
        "ARENA": 100,
        "CHARAKTER": 106,
        "EHRENHALLE": 109,
        "EXIT": 115,
        "GILDEN": 108,
        "LOGIN": 48,
        "OPTIONEN": 111,
        "PILZDEALER": 105,
        "POST": 107,
        "REQUEST_PASSWORD": 49,
        "SCHMIEDE": 102,
        "SIGNUP": 47,
        "STALL": 104,
        "TAVERNE": 99,
        "WELTKARTE": 110,
        "ZAUBERLADEN": 103
    },
    "OPTION": {
        "CHANGE_EMAIL": 24253,
        "CHANGE": {
            "NAME": 24251,
            "PASSWORD": 24254,
            "IMG": 24249
        },
        "DELETE": 24255,
        "DOCHANGE": 24264,
        "LUXURY": 24529,
        "RESEND": 24252
    },
    "POST": {
        "ACCEPT": 23285,
        "CANCEL": 23283,
        "DELETE": 23271,
        "DELETEREAD": 23272,
        "DOWN": 23276,
        "FLUSH": {
            "TXT": 24591,
            "CANCEL": 24593,
            "OK": 24594
        },
        "FORWARD": 24539,
        "PROFILE": 23273,
        "READ": {
            "TXT": 23270,
            "NEXT": 23277,
            "PREV": 23278
        },
        "REPLY": 23286,
        "RETURN": 23284,
        "SEND": 23282,
        "UP": 23275,
        "VIEWFIGHT": 23287,
        "WRITE": 23274
    },
    "SCR": {
        "ARBEITEN": {
            "CANCEL": 311,
            "CLOSE": 312,
            "OK": 310
        },
        "CHAR_STEIGERN1": 383,
        "INVITE_OK": 22973
    },
    "ALBUM_NEXT": 24437,
    "ALBUM_PREV": 24436,
    "ARENA_OK": 23301,
    "BACK": 114,
    "BATTLE_SKIP": 24188,
    "BATTLE_SKIPONE": 24189,
    "BEARD_MINUS": 168,
    "BEARD_PLUS": 169,
    "BO_BUY": 23629,
    "BROWS_MINUS": 174,
    "BROWS_PLUS": 175,
    "COLOR_MINUS": 184,
    "COLOR_PLUS": 185,
    "COUNTRY_NEXT": 25619,
    "COUNTRY_PREV": 25618,
    "CREATE_CHARACTER": 202,
    "DEMO_LOGOFF": 24242,
    "DISCONNECTED": 24369,
    "EARS_MINUS": 176,
    "EARS_PLUS": 177,
    "EMAIL_NAG": 24374,
    "EYES_MINUS": 172,
    "EYES_PLUS": 173,
    "FIGHT_OK": 24187,
    "FIGHT_SKIP": 24186,
    "HAIR_MINUS": 178,
    "HAIR_PLUS": 179,
    "INVITE_SUCCESS_OK": 22977,
    "MAINQUEST_START": 24361,
    "MODIFY_CHARACTER": 203,
    "MOUTH_MINUS": 166,
    "MOUTH_PLUS": 167,
    "NEXT_COPYCAT": 24740,
    "NEXT_PLAYER": 357,
    "NOSE_MINUS": 170,
    "NOSE_PLUS": 171,
    "OPTIONEN": 24700,
    "PLAYER_GUILD_INVITE": 24485,
    "PREV_COPYCAT": 24739,
    "PREV_PLAYER": 356,
    "PURCHASE": 25624,
    "PURCHASE_MAX": 25633,
    "QO_RETURN": 23617,
    "QO_START": 23616,
    "QUEST_CANCEL": 23211,
    "QUEST_SKIP": 23212,
    "RANDOM": 119,
    "SERVER_NEXT": 25622,
    "SERVER_PREV": 25621,
    "SHOPS_NEWWAREZ": 23102,
    "SPECIAL2_MINUS": 182,
    "SPECIAL2_PLUS": 183,
    "SPECIAL_MINUS": 180,
    "SPECIAL_PLUS": 181,
    "STALL_BUY": 23357,
    "TOWER_STEIGERN1": 24788,
    "TOWER_TRY": 24791,
}


# ???
INP = {
    "ARENA_ENEMY": 23300,
    "CHAR_INVITE": 22969,
    "CHAR_INVITE2": 22971,
    "CHARDESC": 22959,
    "EMAIL": 53,
    "GILDE": {
        "CHAT": 23448,
        "DIALOG_INVITE": 23507,
        "GRUENDEN": 23362,
        "TEXT": 23367
    },
    "HALLE_GOTO": 287,
    "LOGIN_PASSWORD": 60,
    "NAME": 51,
    "OPTION": {
        "FIELD": {
            "1": 24261,
            "2": 24262,
            "3": 24263
        }
    },
    "PASSWORD": 55,
    "POST_ADDRESS": 23280,
    "POST_SUBJECT": 23279,
    "POST_TEXT": 23281
}


# Slider Indices
SLDR = {
    "ARBEITEN": {
        "SLDR": 298,
        "BAR": 299,
        "TICK": {
            "1": 300,
            "2": 301,
            "3": 302,
            "4": 303,
            "5": 304,
            "6": 305,
            "7": 306,
            "8": 307,
            "9": 308,
            "10": 309
        }
    },
    "OPTION": {
        "BAR": 24270,
        "TICK1": 24271,
        "VOLUME": 24269
    }
}
