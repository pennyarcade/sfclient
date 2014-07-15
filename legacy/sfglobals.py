#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html
'''


# savegame (request answer) Indices
SG = {
    "ATTR": {
        "AUSDAUER": 33,
        "AUSDAUER_BONUS": 38,
        "AUSDAUER_GEKAUFT": 43,
        "BEWEGLICHKEIT": 32,
        "BEWEGLICHKEIT_BONUS": 37,
        "BEWEGLICHKEIT_GEKAUFT": 42,
        "INTELLIGENZ": 34,
        "INTELLIGENZ_BONUS": 39,
        "INTELLIGENZ_GEKAUFT": 44,
        "STAERKE": 31,
        "STAERKE_BONUS": 36,
        "STAERKE_GEKAUFT": 41,
        "WILLENSKRAFT": 35,
        "WILLENSKRAFT_BONUS": 40,
        "WILLENSKRAFT_GEKAUFT": 45
    },
    "ACTION": {
        "ENDTIME": 48,
        "INDEX": 47,
        "STATUS": 46
    },
    "FACE": {
        "1": 18,
        "2": 19,
        "3": 20,
        "4": 21,
        "5": 22,
        "6": 23,
        "7": 24,
        "8": 25,
        "9": 26,
        "10": 27
    },
    "GUILD": {
        "FIGHT_STATUS": 509,
        "INDEX": 436,
        "JOIN_DATE": 444,
        "RANK": 437
    },
    "ITM": {
        "ATTRIBTYP1": 4,
        "ATTRIBTYP2": 5,
        "ATTRIBTYP3": 6,
        "ATTRIBVAL1": 7,
        "ATTRIBVAL2": 8,
        "ATTRIBVAL3": 9,
        "EXT_ENCHANT": 601,
        "EXT_ENCHANT_POWER": 602,
        "EXT_SOCKET": 600,
        "EXT_SOCKET_POWER": 603,
        "GOLD": 10,
        "MUSH": 11,
        "PIC": 1,
        "SCHADEN_MAX": 3,
        "SCHADEN_MIN": 2,
        "SIZE": 12,
        "TYP": 0
    },
    "LAST": {
        "ACTION_DATE": 3,
        "GUILD_FIGHT_EXP": 440,
        "LOGIN_IP": 504
    },
    "MUSH": {
        "MUSH": 15,
        "BOUGHT_SINCE_LAST_LOGIN": 446,
        "GAINED": 16,
        "SPENT": 17
    },
    "POTION": {
        "DURATION": 497,
        "GAIN": 500,
        "TYPE": 494
    },
    "QUEST": {
        "OFFER": {
            "DURATION1": 242,
            "ENEMY1": 236,
            "EXP1": 281,
            "GOLD1": 284,
            "LEVEL1": 230,
            "LOCATION1": 239,
            "REWARD_ITM1": 245,
            "TYPE1": 233
        },
        "REROLL_TIME": 229
    },
    "ACCOUNT_PROTECTION_DATE": 441,
    "ACHIEVEMENTS": 466,
    "ALBUM": 439,
    "ARMOR": 448,
    "BACKPACK_OFFS": 169,
    "BACKPACK_SIZE": 5,
    "BAR": 478,
    "BEERS": 458,
    "CLASS": 30,
    "CLASS_RANK": 13,
    "DAMAGE_MAX": 450,
    "DAMAGE_MIN": 449,
    "DUNGEON_13": 491,
    "DUNGEON_LEVEL": 481,
    "EMAIL_DATE": 465,
    "EMAIL_VALID": 464,
    "EVASION": 454,
    "EVENT_TRIGGER_COUNT": 510,
    "EXP": 9,
    "EXP_BONUS": 462,
    "EXP_FOR_NEXTLEVEL": 10,
    "FIDGET_ITEM1": 362,
    "FIDGET_REROLL_TIME": 361,
    "FIRST_PAYMENT": 480,
    "FOO": 477,
    "GENDER": 29,
    "GOLD": 14,
    "GOLD_BONUS": 463,
    "HELLO": 479,
    "HONOR": 11,
    "INVENTORY_OFFS": 49,
    "INVENTORY_SIZE": 10,
    "LEVEL": 8,
    "LIFE": 451,
    "LOCKDURATION": 476,
    "MAGICRSISTANCE": 455,
    "MOUNT": 287,
    "MOUNT_DURATION": 452,
    "MQ_REROLL_TIME": 460,
    "MQ_STATE": 459,
    "MSG_COUNT": 6,
    "MUSHROOM_BOUGHT_AMOUNT": 507,
    "MUSHROOM_BOUGHT_DATE": 508,
    "MUSHROOMS_MAY_DONATE": 438,
    "NEW_DUNGEONS": 442,
    "NEW_FLAGS": 445,
    "NEXT_BATTLE_TIME": 434,
    "PAYMENT_ID": 1,
    "PHP_SESSION": 493,
    "PLAYER_ID": 2,
    "POWER_LIFE_POTION": 503,
    "PVP_REROLL_TIME": 461,
    "RACE": 28,
    "RANK": 12,
    "REGISTRATION_DATE": 4,
    "REGISTRATION_IP": 5,
    "SERVER_TIME": 511,
    "SHAKES_ITEM1": 289,
    "SHAKES_REROLL_TIME": 288,
    "TIMEBAR": 457,
    "TIMEBAR_REROLL_TIME": 456,
    "TOILET": 492,
    "TRANSACTION_COUNT": 453,
    "UNREAD_MESSAGES": 435,
    "VALIDATION_IP": 7,
    "WE_MISS_YOU": 447,
}


# ???
BNC = {
    "CHAR": {
        "ACH": 23076,
        "PREISE": 409,
        "RIGHTPANE": 23078,
        "SECONDPROP": 408
    },
    "CHARSPECIALOVL": {
        "DARKELF_M": 351,
        "DWARF_F": 349,
        "DWARF_M": 343,
        "ELF_F": 347,
        "ELF_M": 341,
        "GNOM_M": 350,
        "GOBLIN_F": 345,
        "GOBLIN_M": 342,
        "HUMAN_F": 348,
        "HUMAN_M": 344,
        "ORC_F": 346
    },
    "CITY": {
        "CA_OVL": 264,
        "ORK": 266,
        "OVERLAYS": 267,
        "STATISTEN": 268,
        "ZWERG": 265
    },
    "GILDE": {
        "CHAT": 23449,
        "CREST": 24541,
        "CREST_CONTROLS": 24570,
        "DIALOG": {
            "INVITE": 23516,
            "KICK": 23514,
            "MASTER": 23515,
            "RAID": 23518,
            "REVOLT": 23517
        },
        "GEBAEUDE": 23486,
        "KATAPULT": 24528,
        "LISTBUTTONS": 23396,
        "SCHATZ": 23497,
        "SET": {
            "MASTER": 23402,
            "MEMBER": 23400,
            "OFFICER": 23401
        }
    },
    "HUTBECHER": {
        "1_HOVER": 23582,
        "2_HOVER": 23583,
        "3_HOVER": 23584
    },
    "HUTMANN": {
        "BECHERCHOOSE": 23585,
        "LOST": 23587,
        "PLACEBET": 23581,
        "WON": 23586
    },
    "IF": {
        "BUTTONS": 112,
        "MAIN": 9,
        "OVL": 10,
        "STATS": 33
    },
    "POST": {
        "DAWN": 23263,
        "FLUSHMSG": 24592,
        "LIST": 23291,
        "NIGHT": 23264,
        "READ": 23293,
        "WRITE": 23292
    },
    "SCREEN": {
        "ALBUM": 24438,
        "ARBEITEN": {
            "TXT": 316,
            "SUCCESS": 318,
            "WAIT": 317
        },
        "ARENA": {
            "TXT": 23304,
            "DAWN": 23307,
            "DAY": 23305,
            "NIGHT": 23306
        },
        "BUILDCHAR": 116,
        "CHAR": 23079,
        "CHAR_GOLDEN": 24531,
        "CITY": {
            "TXT": 263,
            "DAWN": 261,
            "DAY": 262,
            "NIGHT": 260
        },
        "DEALER": 23256,
        "DEALER2": 23257,
        "DEMO": 24243,
        "DISCONNECTED": 24370,
        "EMAIL_NAG": 24375,
        "FIDGET": 23103,
        "FIGHT": 24240,
        "GILDE_GRUENDEN": 23498,
        "GILDEN": 23499,
        "HALLE": 283,
        "HLMAINQUESTS": 24767,
        "HUTMANN": 23588,
        "INVITE": 22974,
        "MAINQUEST": 24366,
        "MAINQUESTS": 24353,
        "OPTION": 24308,
        "POST": 23294,
        "QUEST": 23213,
        "SHAKES": 23104,
        "STALL": 23358,
        "TAVERNE": 23532,
        "TOILET": 24598,
        "TOWER": 24716,
        "WITCH": 25635,
        "WORLDMAP": 23106
    },
    "VOLK": {
        "BTNS": {
            "ALL": 165,
            "F": 163,
            "M": 164
        }
    },
    "WINDOW": {
        "ARENA": 23302,
        "FORGOT_PASSWORD": 79,
        "LOGIN": 77,
        "SIGNUP": 78
    },
    "ALBUM_CAT_IN": 24435,
    "BEERFEST": 24481,
    "BEEROFFER": 23630,
    "BUBBLES": 281,
    "CHARIMG": 329,
    "CHARIMG2": 340,
    "DUNGEON_CONGRATS": 24356,
    "FIDGET_DAY": 23090,
    "FIDGET_NIGHT": 23091,
    "FIGHT_REWARDS": 24208,
    "FUCK": 81,
    "HERO_OF_THE_DAY": 24212,
    "INVITE_INPUTDIALOGUE": 22975,
    "INVITE_SUCCESS": 22978,
    "OPPIMG": 23844,
    "OPPIMG2": 23855,
    "OPTION_DOCHANGE": 24306,
    "OPTION_DORESEND": 24307,
    "PURCHASE_BUTTONS": 25634,
    "QUESTOFFER": 23625,
    "SCR_BUILDCHAR": 118,
    "SPECIAL_ACTION": 24496,
    "STALL_BOESE": 23342,
    "STALL_GUT": 23341,
    "TAVERNE_CAS": 23533,
    "TAVERNE_QUESTOVL": 23539,
    "TOILET_OVERLAYS": 24613,
    "TOWER_BOOSTPRICE": 25608,
    "TOWER_PIECES": 24752
}


# Configuration file indices
CFG = {
    "ALLOW_SKIP_QUEST": 34,
    "BACKGROUND_ID": 57,
    "BUFFED_URL": 19,
    "buffed_mode": 15,
    "BULLSHIT_BOX": 50,
    "BULLSHIT_CID": 51,
    "CENSORED": 40,
    "DATAPROT_URL": 13,
    "DONT_SAVE_CID": 44,
    "FLAG_NAMES": 47,
    "FLAGS": 46,
    "FORUM_URL": 10,
    "GAMESTAFF_EMAIL": 36,
    "IDLE_POLLING": 33,
    "IMAGE_TIMEOUT": 21,
    "URL": 2,
    "IMPRINT_URL": 11,
    "INSTR_URL": 14,
    "INTERNAL_PIXEL": 41,
    "LANG_CODE": 1,
    "LANG_URL": 8,
    "LEGAL_URL": 12,
    "LIGHT_MODE": 45,
    "LOWRES_URL": 48,
    "MOBILE_PAYMENT_OLD": 55,
    "MOBILE_PAYMENT_URL": 56,
    "MOBILE_VALIDATION": 54,
    "MP_PROJECT": 18,
    "NO_CROSSDOMAIN": 9,
    "NO_TUNNELING_TIME": 27,
    "PAPAYA_FILE": 31,
    "PAPAYA_PATH": 30,
    "pay_methods": 16,
    "PHP_TUNNEL_URL": 25,
    "PIXEL_CALL": 53,
    "POLL_TUNNEL_URL": 28,
    "PORT_FIREWALL": 6,
    "PORT_OFFSET": 4,
    "PORT_RANGE": 5,
    "RECONNECT": 24,
    "RELOAD_PIXEL": 42,
    "REROLL_IMG": 23,
    "RESEND_COUNT": 32,
    "RESPONSE_TIMEOUT": 20,
    "SERVER": 7,
    "SERVER_ID": 17,
    "SERVER_VERSION": 43,
    "SHOP_URL": 35,
    "SND_URL": 3,
    "SOCIAL_BUTTONS": 52,
    "SPONSOR_IMG": 22,
    "SPONSOR_URL": 49,
    "SUPPORT_EMAIL": 29,
    "TRACKING_PIXEL": 26,
    "TV_FUNCTION": 59,
    "TV_POLL_INTERVAL_LONG": 61,
    "TV_POLL_INTERVAL_NORMAL": 60,
    "WORLDS": 58,
}


# ???
CNT = {
    "ALBUM": {
        "CAT_OUT": 24430,
        "MONSTER": 24388,
        "MONSTER_FRAME": 24392,
        "WEAPON": {
            "1": 24396,
            "2": 24400,
            "3": 24404,
            "4": 24408,
            "5": 24412,
            "EPIC": 24416
        }
    },
    "CHANGE": {
        "PASSWORD": {
            "SMILEY": {
                "HAPPY": 24267,
                "NEUTRAL": 24266,
                "SAD": 24265
            }
        }
    },
    "CHAR": {
        "ACH": 23033,
        "POTION": 23073,
        "SLOT": {
            "1": 410,
            "2": 411,
            "3": 412,
            "4": 413,
            "5": 414,
            "6": 415,
            "7": 416,
            "8": 417,
            "9": 418,
            "10": 419,
            "11": 420,
            "12": 421,
            "13": 422,
            "14": 423,
            "15": 424,
            "FIDGET": {
                "1": 425,
                "2": 426,
                "3": 427,
                "4": 428,
                "5": 429,
                "6": 430
            },
            "SHAKES": {
                "1": 431,
                "2": 432,
                "3": 433,
                "4": 434,
                "5": 435,
                "6": 436
            }
        }
    },
    "FIGHT": {
        "BOX3": 24200,
        "ONO": 24220,
        "OPP_BORDER": 24185,
        "REWARDGOLD": 24202,
        "REWARDMUSH": 24206,
        "REWARDSILVER": 24204,
        "SLOT": 24201
    },
    "GILDE": {
        "ATTACK": 23389,
        "CREST": 24559,
        "CREST_COLOR": 24584,
        "DEFENCE": 23390,
        "GEBAEUDE_GOLD": 23474,
        "GEBAEUDE_MUSH": 23477,
        "GOLD": 23489,
        "GOLD2": 23495,
        "LINK": 23446,
        "LIST": 23368,
        "MUSH": 23490,
        "MUSH2": 23496,
        "RANG": 23365
    },
    "HALL": {
        "GOTO_GILDEN": 291,
        "GOTO_SPIELER": 288,
        "LIST": 294
    },
    "HLMQS": {
        "BUTTON": 24768,
        "COMPLETED": 24783,
        "DISABLED": 24778
    },
    "HUTMANN": {
        "GOLDBET": 23569,
        "GOLDBET2": 23576,
        "MUSHBET": 23570,
        "MUSHBET2": 23577
    },
    "IF": {
        "AGB": 19,
        "ANLEITUNG": 23,
        "DATENSCHUTZ": 21,
        "DRAGON": {
            "1": 86,
            "2": 87,
            "3": 88,
            "4": 89,
            "5": 90,
            "6": 91,
            "7": 92,
            "8": 93,
            "9": 94,
            "10": 95,
            "11": 96,
            "12": 97,
            "13": 98
        },
        "FORUM": 15,
        "HUTMANN": 39,
        "IMPRESSUM": 13,
        "LOGOUT": 11,
        "SHOP": 25,
        "SPONSOR": 18,
        "TOILET": 25611,
    },
    "MAINQUEST": {
        "ENEMY": 24364,
        "ENEMY_BORDER": 24363,
        "SLOT": 24362
    },
    "MQS": {
        "BUTTON": 24311,
        "COMPLETED": 24342,
        "DISABLED": 24331
    },
    "QO": {
        "CHOICE": {
            "1": 23591,
            "2": 23592,
            "3": 23593,
            "4": 23594,
            "5": 23595
        },
        "REWARDGOLD": 23609,
        "REWARDSILVER": 23611
    },
    "SCR": {
        "ARBEITEN": {
            "BAR": 313,
            "FILL": 314
        },
        "CHAR": {
            "GILDE": 22957,
            "GOLD1": 393,
            "NAME": 354,
            "SILBER1": 403
        }
    },
    "STALL": {
        "GOLD": 23354,
        "MUSH": 23356,
        "SCHATZGOLD": 23349,
        "SCHATZSILBER": 23351
    },
    "TOWER": {
        "BOOSTCOIN": 25607,
        "FACE": 0x6400,
        "SCROLLAREA": 24743,
        "SLOT": 24720,
        "WINDOW": 24753
    },
    "AGB": 69,
    "BULLET_CHAR": 24194,
    "BULLET_OPP": 24195,
    "CREATE_GOTO_LOGIN": 200,
    "DATENSCHUTZ": 72,
    "EMAIL_RESEND": 24372,
    "FORGOT_PASSWORD": 62,
    "GOTO_LOGIN": 64,
    "GOTO_SIGNUP": 66,
    "LIFEBAR_FILL_OPP": 24161,
    "LIFEBAR_OPP": 24159,
    "POST_GUILD": 23289,
    "POST_LIST": 23269,
    "PW_GOTO_LOGIN": 25615,
    "QUEST_SLOT": 23619,
    "SHIELD_CHAR": 24192,
    "SHIELD_OPP": 24193,
    "SOCIAL": 24460,
    "TIMEBAR_FILL": 23544,
    "WEAPON_CHAR": 24190,
    "WEAPON_OPP": 24191,
    "WITCH_SCROLL": 25641,
}


# ???
C = {
    "AUTO_LOGIN": True,
    "BEARD": 1,
    "BROWS": 2,
    "CHAREXT": ".png",
    "DISPLAY_ITEM_INFO": False,
    "HAIR": 4,
    "ITEMS_PER_TYPE": 110,
    "SHOW_CA": False,
    "SPECIAL2": 8,
    "TIMEOFDAY": -1
}


# ???
CA = {
    "CITY": {
        "ARENA": 227,
        "BUH": 259,
        "DEALER": 234,
        "ESEL": 237,
        "POST": 241,
        "RUHMESHALLE": 221,
        "SHAKES": 217,
        "TAVERNE": 239,
        "WACHE": 244,
        "ZAUBERLADEN": 219
    },
    "HUTBECHER": {
        "1": 23562,
        "2": 23563,
        "3": 23564
    },
    "SCR": {
        "ARBEITEN_BLOCKCITY": 295,
        "CHAR_EXPBAR": 360,
        "INVITE_BLOCKCITY": 22967
    },
    "STALL": {
        "BOX": {
            "BOESE": {
                "1": 23337,
                "2": 23338,
                "3": 23339,
                "4": 23340
            },
            "GUT": {
                "1": 23333,
                "2": 23334,
                "3": 23335,
                "4": 23336
            }
        }
    },
    "TAVERNE": {
        "BAR": 23541,
        "HUTMANN": 23524,
        "QUESTOFFER": 23531,
        "TOILETTE": 24597
    },
    "TOILET": {
        "BOWL": 24616,
        "CHAIN": 24615,
        "LID": 24619,
        "TANK": 24614
    },
    "CHALDRON": 25639,
    "DEALER_AKTION": 23254,
    "DEALER_SPONSOR": 23255,
    "GILDE_DIALOG_BLOCK": 23500,
    "GOTO_WITCH": 25640,
    "POST_BLOCK": 24595,
    "SELL_ITEM": 361,
    "TV": 25706,
    "USE_ITEM": 362,
    "WITCH": 25638,
}


# ???
CB = {
    "AGB_CHECKED": 76,
    "AGB_UNCHECKED": 75,
    "COMPARE_CHECKED": 24625,
    "COMPARE_UNCHECKED": 24624,
    "CS_CHECKED": 24483,
    "CS_UNCHECKED": 24482,
    "FUCK_CHECKED": 84,
    "FUCK_UNCHECKED": 83,
    "LM_CHECKED": 24284,
    "LM_UNCHECKED": 24283,
    "TV_CHECKED": 25704,
    "TV_UNCHECKED": 25703,
}


# Color values
CLR = {
    "ATTACK": {
        "ERROR": {
            "OFFLINE": 0xA10000,
            "OFFLINE_HALF": 0xB04000,
            "ONLINE": 0xFF2000,
            "ONLINE_HALF": 0xFF6000
        },
        "OK": 8978312
    },
    "SYSMSG": {
        "CLR": 16746564,
        "GREEN": 4521796,
        "GREEN_HIGHLIGHT": 8978312,
        "RED": 16729156,
        "RED_GRAYED": 13648964,
        "RED_HIGHLIGHT": 16746632,
        "RED_HIGHLIGHT_GRAYED": 13666440,
        "HIGHLIGHT": 16764040
    },
    "ATTRIBBONUS": 8947967,
    "BLACK": 0,
    "CHAT_WHISPER": 0xFF00FF,
    "EPICITEMQUOTE": 8947967,
    "ERROR": 0xFF0000,
    "GRAYED": 13664290,
    "GRAYED_HL": 15769634,
    "ITEMENCHANTMENT": 0xA300FF,
    "NOATTACK": 15761432,
    "OFFLINE": 15769634,
    "ONLINE": 15790146,
    "RED": 16729156,
    "SFHIGHLIGHT": 16777026,
    "SFHIGHLIGHT_WHISPER": 16746751,
    "SFORANGE": 15777858,
    "WHITE": 0xFFFFFF,
}


# ???
CPC = {
    "ARMOR": 19,
    "ATTRIBS": 4,
    "ATTRIBS_BONUS": 9,
    "ATTRIBS_BOUGHT": 14,
    "CLASS": 1,
    "DAMAGE_MAX": 21,
    "DAMAGE_MIN": 20,
    "FREE": 143,
    "GOLD_STOLEN": 2,
    "GOLD_STOLEN_NEXT": 3,
    "ITEMS": 22,
    "LEVEL": 0,
    "PRICE_NEXT_LEVEL": 142,
}


# Guild Indices
GUILD = {
    "ATTACK_TARGET": 364,
    "ATTACK_TIME": 365,
    "DEFENCE_TARGET": 366,
    "DEFENCE_TIME": 367,
    "EVENT_TRIGGER_COUNT": 368,
    "IS_RAID": 9,
    "MEMBER": {
        "GOLDSPENT": 214,
        "HONOR": 164,
        "ID": 14,
        "LEVEL": 64,
        "MUSHSPENT": 264,
        "ONLINE": 114,
        "RANK": 314
    },
    "RAID_LEVEL": 8,
}


# Sound Indices
SND = {
    "CATAPULT_HIT": 24533,
    "CATAPULT_LAUNCH": 24532,
    "CLICK": 2,
    "ERROR": 3,
    "HATCH": 24742,
    "JINGLE": 4,
    "MAINQUESTS_UNLOCK": 24310,
    "MIRROR": 24737,
    "MOUNT_1": 23325,
    "SHARD": 24736,
    "TEST": 24244,
    "TOILET_DROP": 24623,
    "TOILET_FLUSH": 24622,
    "TOILET_FLUSHTRY": 24621,
    "WEAPON": 23631,
    "WITCH_DROP": 25636,
}


# ???
TSG = {
    "COPYCATS": 3,
    "FILEOFFSET": 1,
    "FREE": 447,
    "LOOT_SACK": 477,
    "PLAYERID": 0,
    "TOWER_LEVEL": 2
}


ARROW_MAX = 22950
ARROW_OFFS = 21900
BLACK_SQUARE = 1
CLA_GILDE_CREST = 24560

DIST_DEALER_Y = 50

ITM_EMPTY = 30000
ITM_MAX = 60000
ITM_OFFS = 30001

POPUP_BEGIN_LINE = 5
POPUP_END_LINE = 0
POPUP_INFO = 41

RES_X = 0x0500
RES_Y = 800
