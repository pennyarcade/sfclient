#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html
'''


# player action codes
ACT = {
    "BUY": {
        "ATTRIB": 21,
        "BEER": 518,
        "LUXURY": 195,
        "MOUNT": 20
    },
    "CHANGE": {
        "FACE": 801,
        "MAIL": 804,
        "NAME": 803,
        "PASS": 805
    },
    "GUILD": {
        "COMMENCE_ATTACK": 114,
        "DELETE": 102,
        "DONATE": 111,
        "EXPEL": 104,
        "FOUND": 101,
        "IMPROVE": 107,
        "INVITE": 103,
        "JOIN": 110,
        "JOIN_ATTACK": 112,
        "JOIN_DEFENSE": 113,
        "RENAME": 109,
        "SET_DESC": 108,
        "SET_MASTER": 105,
        "SET_OFFICER": 106
    },
    "POST": {
        "DELETE": 508,
        "READ": 507,
        "SEND": 509,
        "SEND_GUILD": 536
    },
    "QUEST": {
        "BEGIN": 510,
        "CANCEL": 511,
        "SKIP": 189
    },
    "REQUEST": {
        "CHAR": 513,
        "GUILD": 503,
        "GUILD_NAMES": 533,
        "NEWWAREZ": 506,
        "TRANS_COUNT": 530
    },
    "SCREEN": {
        "ARBEITEN": 12,
        "ARENA": 11,
        "CHAR": 4,
        "EHRENHALLE": 7,
        "FREMDGILDE": 23,
        "GILDE_GRUENDEN": 17,
        "GILDEN": 6,
        "GILDENHALLE": 24,
        "OPTIONEN": 9,
        "PILZDEALER": 16,
        "POST": 5,
        "SCHMIEDE": 13,
        "STALL": 15,
        "TAVERNE": 10,
        "TOILET": 303,
        "TOWER": 312,
        "WELTKARTE": 8,
        "WITCH": 322,
        "ZAUBERLADEN": 14
    },
    "ACCOUNT_CREATE": 1,
    "ALBUM": 116,
    "ARBEIT": 502,
    "ARBEIT_CANCEL": 505,
    "CHAR_CREATE": 501,
    "COPYCAT_BOOST": 314,
    "DEALER_AKTION": 25,
    "DEALER_SPONSOR": 26,
    "DELETE_ACCOUNT": 802,
    "FORGOT_PASSWORD": 3,
    "GET_CHAT_HISTORY": 517,
    "INVENTORY_CHANGE": 504,
    "INVITE_PLAYER": 115,
    "KILL_POTION": 27,
    "LOAD_CATAPULT": 196,
    "LOGIN": 2,
    "LOGOUT": 535,
    "MAINQUEST": 519,
    "MOVE_COPYCAT_ITEM": 318,
    "PLACE_BET": 22,
    "RE_LOGIN": 515,
    "RESEND_EMAIL": 531,
    "REVOLT": 534,
    "ROB_PLAYER": 313,
    "SEND_CHAT": 516,
    "SET_PLAYER_DESC": 514,
    "START_FIGHT": 512,
    "TOILET_FLUSH": 302,
    "TOWER_TRY": 313,
    "VALIDATE": 532,
    "WHISPER": 537,
    "WITCH_DONATE": 323,
    "WITCH_ENCHANT": 325,
}


# Response codes
RESP = {
    "ARBEIT": {
        "ERLEDIGT": 103,
        "START": 104,
        "STOP": 105
    },
    "CHANGE": {
        "FACE_OK": 115,
        "MAIL_OK": 118,
        "NAME_OK": 117,
        "PASS_OK": 116
    },
    "GUILD": {
        "CHANGE_DESC_SUCCESS": 153,
        "COMMENCE_ATTACK_OK": 181,
        "DATA": 101,
        "DELETE_SUCCESS": 151,
        "DONATE_SUCCESS": 160,
        "EXPEL_SUCCESS": 156,
        "FIGHT": 178,
        "FOUND_SUCCESS": 150,
        "IMPROVE_SUCCESS": 154,
        "INVITE_SUCCESS": 157,
        "JOIN_ATTACK_OK": 179,
        "JOIN_DEFENSE_OK": 180,
        "JOIN_SUCCESS": 158,
        "MASTER_SUCCESS": 159,
        "NAMES": 183,
        "OFFICER_SUCCESS": 155,
        "RENAME_SUCCESS": 152
    },
    "PLAYER": {
        "DESC_SUCCESS": 109,
        "NOT_FOUND": 112,
        "SCREEN": 111
    },
    "QUEST": {
        "DONE": 106,
        "DONE_PIXEL": 188,
        "DONE_PIXEL_2": 197,
        "SKIP_ALLOWED": 193,
        "SKIP_ALLOWED_START": 194,
        "START": 107,
        "STOP": 108
    },
    "SAVEGAME": {
        "MIRROR": 317,
        "SHARD": 316,
        "STAY": 102,
        "STAY_ERROR": 173
    },
    "SCREEN": {
        "BUILDCHAR": 4,
        "GILDENHALLE": 170,
        "WITCH": 324
    },
    "TOILET": {
        "DROPPED": 305,
        "DROPTWICE": 357,
        "FLUSHED": 308,
        "FULL": 306,
        "LOCKED": 304,
        "TANKFULL": 311,
        "UNLOCKED": 309
    },
    "ACCOUNT_SUCCESS": 1,
    "ALBUM": 192,
    "ATTACK_NOT_EXIST": 114,
    "BET_LOST": 169,
    "BET_WON": 168,
    "CHAT_HISTORY": 161,
    "CHAT_LINE": 162,
    "DEALER_AKTION": 174,
    "DEALER_SPONSOR": 176,
    "DELETE_ACCOUNT_OK": 119,
    "DEMO_SCREEN": 113,
    "EMAIL_RESENT": 164,
    "FAME_LIST": 3,
    "INVITE_SUCCESS": 191,
    "LOGIN_SUCCESS": 2,
    "LOGIN_SUCCESS_BOUGHT": 184,
    "LOGOUT_SUCCESS": 187,
    "MAINQUEST": 122,
    "MESSAGE_SENT": 202,
    "MOVE_TOWER_ITEM": 319,
    "NO_LOGIN": 120,
    "OTHER_GUILD": 172,
    "PASSWORD_SENT": 165,
    "READ_MESSAGE": 201,
    "REQUEST_GUILD": 121,
    "REQUEST_GUILD_QUIET": 186,
    "TOWER_FIGHT": 321,
    "TOWER_SAVE": 315,
    "TRANS_COUNT": 163,
    "UPDATE_CHECK": 167,
    "VALIDATE_OK": 166,
    "WHISPER_SUCCESS": 190
}


# Error codes
ERR = {
    "GUILD": {
        "ALREADY_ATTACKING": -63,
        "ALREADY_MEMBER": -38,
        "ALREADY_UNDER_ATTACK": -61,
        "ALREADY_YOU_OTHER": -25,
        "ALREADY_YOU_THIS": -27,
        "ATTACK_DELAY": -62,
        "ATTACK_STATUS": -64,
        "BUILDING_MAX": -21,
        "BUILDING_NOT_FOUND": -20,
        "CHAT_HISTORY": -32,
        "CHAT_NOT_MEMBER": -31,
        "CHAT_TEXT_ERROR": -33,
        "DESCR_TOO_LONG": -102,
        "DONATE_FRA": -52,
        "DONATE_NEG": -51,
        "EMAIL_VALIDATE": -46,
        "FIGHT_TOO_EXPENSIVE": -60,
        "IS_FULL": -24,
        "LACK_GOLD": -19,
        "LACK_MUSH": -18,
        "MASTER_CANT_BE_OFFICER": -23,
        "MUSH_FREE": -47,
        "NAME_CHARACTERS": -45,
        "NAME_LENGTH": -44,
        "NAME_REJECTED": -43,
        "NOT_ALLOWED": -17,
        "NOT_FOUND": -16,
        "NOT_MEMBER": -22,
        "NOT_REAL_MEMBER": -26,
        "PLAYER_NOT_FOUND": -28,
        "RANK_WRONG": -95,
        "TOO_EXPENSIVE": -30
    },
    "INVITE": {
        "EMAIL_REJECTED": -92,
        "NOT_VALIDATED": -90,
        "TOO_MANY": -91
    },
    "NAME": {
        "EXISTS": -1,
        "REJECTED": -5,
        "TOO_SHORT": -2
    },
    "NO": {
        "ALBUM": -93,
        "CHAT_INFO": -96,
        "CHAT_OVERFLOW": -97,
        "ENDURANCE": -36,
        "INDEX_FREE": -14,
        "MUSH_BAR": -35,
        "MUSH_MQ": -41,
        "MUSH_PVP": -40
    },
    "ACCOUNTS_PER_IP": -56,
    "ALREADY_IN_GUILD": -13,
    "ATTACK_AGAIN": -48,
    "BEER": -34,
    "BOOST": -42,
    "DEALER_AKTION": 175,
    "DEALER_SPONSOR": 177,
    "EMAIL_REJECTED": -4,
    "EMAIL_WRONG": -10,
    "FACE_DATA_INCORRECT": -9,
    "FIGHT_SELF": -15,
    "GENDER_OR_RACE": -11,
    "INBOX_FULL": 203,
    "INVENTORY_FULL": -58,
    "INVENTORY_FULL_ADV": -86,
    "JOINED_TOO_RECENTLY": -68,
    "LOCKED_ADMIN": -54,
    "LOCKED_PAYMENT": -53,
    "LOGIN_FAILED": -6,
    "LUXURY_ALREADY": -94,
    "MAIL_EXISTS": -12,
    "MSG_LEVEL_TOO_LOW": -84,
    "MSG_NOT_VALIDATED": -85,
    "NO_SLOT_FOR_FLUSHING": -307,
    "NOT_INVITED": -39,
    "PASSWORD_TOO_SHORT": -3,
    "PLACE_BET": -57,
    "RECIPIENT_NOT_FOUND": 204,
    "RECIPIENT_SELF": 205,
    "REQUEST_PW": -49,
    "REVOLT_FAILED": -67,
    "SERVER_DOWN": -69,
    "SESSION_ID_EXPIRED": -65,
    "STOP_TUNNELING": -66,
    "SUBJECT_TOO_SHORT": -29,
    "TOILET_EMPTY": -310,
    "TOO_EXPENSIVE": -7,
    "TOO_SOON": -55,
    "TOWER_CLOSED": -98,
    "TOWER_ITEMMOVE": -100,
    "TOWER_NO_COPYCATS": -101,
    "VALIDATE": -50,
    "WORSE_MOUNT": -37,
    "WRONG_PASSWORD": -8,
}


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


# Text Snippet IDs
TXT = {
    "ACH": {
        "1": 6300,
        "2": 6310,
        "3": 6320,
        "4": 6330,
        "5": 6340
    },
    "ARBEIT_TEXT": {
        "1": 41,
        "2": 42,
        "3": 43,
        "4": 70,
        "5": 72,
        "6": 73,
        "7": 74
    },
    "ARENA": {
        "0": 2,
        "1": 113,
        "2": 114,
        "3": 211,
        "4": 212
    },
    "ATTACK": {
        "TXT": 166,
        "OK_STATUS": 8410,
        "STATUS": 8401
    },
    "ATTRIB": {
        "SUM": 9467,
        "HELP": {
            "TXT": 4530,
            "EXT": 4535,
            "HUNTER": 4541,
            "MAGE": 4542,
            "WARRIOR": 4540
        },
    },
    "BEERFEST": {
        "TEXT_OK": 9203,
        "TEXT_TOOHEALTHY": 9202,
        "TITLE_OK": 9201,
        "TITLE_TOOHEALTHY": 9200
    },
    "BO": {
        "BOUGHT": 190,
        "BUY": 184,
        "BUY_FREE": 9532,
        "TEXT_NO": 189,
        "TEXT_OK": 188,
        "TEXT_TOOHEALTHY": 192,
        "TIME": 185,
        "TITLE_NO": 187,
        "TITLE_OK": 186,
        "TITLE_TOOHEALTHY": 191
    },
    "BODY": {
        "GUILD": {
            "DELETED": 4405,
            "DELETED_BY_ADMIN": 4406,
            "EXPELLED": 4407,
            "EXPELLED_BY_ADMIN": 4408,
            "INVITE": 4409
        },
        "BODY_PVP": 4411
    },
    "BUILDING": {
        "1": 258,
        "2": 259,
        "COMPLETE": 306,
        "S_GOTO_CREST": 9447
    },
    "BUY": {
        "1": {
            "1": 1100,
            "1_AKTION": 1140,
            "2": 1101,
            "2_AKTION": 1141,
            "3": 1102,
            "3_AKTION": 1142
        },
        "2": {
            "1": 1103,
            "1_AKTION": 1143,
            "2": 1104,
            "2_AKTION": 1144,
            "3": 1105,
            "3_AKTION": 1145
        },
        "3": {
            "1": 1106,
            "1_AKTION": 1146,
            "2": 1107,
            "2_AKTION": 1147,
            "3": 1108,
            "3_AKTION": 1148
        },
        "4": {
            "1": 1109,
            "1_AKTION": 1149,
            "2": 1110,
            "2_AKTION": 1150,
            "3": 1111,
            "3_AKTION": 1151
        },
        "5": {
            "1": 1112,
            "1_AKTION": 1152,
            "2": 1113,
            "2_AKTION": 1153,
            "3": 1114,
            "3_AKTION": 1154
        },
        "6": {
            "1": 1115,
            "1_AKTION": 1155,
            "2": 1116,
            "2_AKTION": 1156,
            "3": 1117,
            "3_AKTION": 1157
        },
        "7": {
            "1": 1118,
            "1_AKTION": 1158,
            "2": 1119,
            "2_AKTION": 1159,
            "3": 1120,
            "3_AKTION": 1150
        }
    },
    "CHANGE": {
        "TXT": 127,
        "EMAIL": 129,
        "NAME": 128,
        "PASSWORD": 130,
        "IMG": 126
    },
    "CHAR": {
        "AUSDAUER": 62,
        "BEWEGLICHKEIT": 61,
        "INTELLIGENZ": 63,
        "KAMPFWERT": 66,
        "LEBEN": 67,
        "RUESTUNG": 68,
        "SCHADEN": 65,
        "STAERKE": 60,
        "WIDERSTAND": 69,
        "WILLENSKRAFT": 64,
        "IMG": 125
    },
    "CREATE": {
        "ACCOUNT": 21,
        "CHAR": 18,
        "CHARACTER": 36,
        "GOTO_LOGIN": 117
    },
    "CREST": {
        "APPLY": 9417,
        "ELEMENT": 9405,
        "GOTO_BUILDINGS": 9446,
        "INFO": 9445,
        "SUGGEST": 9416,
        "SUGGESTION": 9418,
        "TINCTUREBOXES": 9440,
        "TINCTURES": 9420
    },
    "DELETE": {
        "ACCOUNT": {
            "TXT": 131,
            "FIELD": {
                "1": 146,
                "2": 147,
                "3": 148
            },
            "TITLE": 145
        }
    },
    "DOCHANGE": {
        "TXT": 132,
        "EMAIL": {
            "FIELD": {
                "1": 138,
                "2": 139,
                "3": 140
            },
            "TITLE": 137
        },
        "NAME": {
            "NAME": 156,
            "FIELD": {
                "1": 134,
                "2": 135,
                "3": 136
            },
            "TITLE": 133
        },
        "PASSWORD": {
            "FIELD": {
                "1": 142,
                "2": 143,
                "3": 144
            },
            "TITLE": 141
        },
    },
    "DONATE": {
        "GOLD": {
            "1": 250,
            "2": 251
        },
        "MUSH": {
            "1": 252,
            "2": 253
        }
    },
    "DU": {
        "GEWONNEN": 239,
        "VERLOREN": 240,
        "WAS": {
            "GEWONNEN": 8807,
            "VERLOREN": 8808
        }
    },
    "DUNGEON": {
        "INFO": 8250,
        "NAME": 8200,
        "NAMES": 8840
    },
    "ECONOMIC": {
        "LOSS": {
            "TXT": 9528,
            "NEXT": 9529,
            "SUFFIX": 9530
        }
    },
    "EMAIL": {
        "TXT": 19,
        "CHANGED": 154,
        "NAG": 234,
        "NAG_TITLE": 237,
        "RESEND": 235,
        "RESENT": 236
    },
    "ENCHANT": {
        "HINT": 10121,
        "NAMES": 10200,
        "VALUES": 10400
    },
    "ERROR": {
        "AGB": 507,
        "ALREADY_IN_GUILD": 520,
        "ARBEITEN": {
            "ARENA": 604,
            "MAINQUEST": 606,
            "TAVERNE": 605
        },
        "ATTACK_AGAIN": 554,
        "BEER": 541,
        "COMPROMISED_ACCOUNT": 9103,
        "EMAIL": {
            "MISMATCH": 517,
            "REJECTED": 504,
            "WRONG": 515
        },
        "EMPTY_GUILD_NAME": 519,
        "FACE_DATA_INCORRECT": 0x0202,
        "FIGHT_SELF": 522,
        "GUILD": {
            "ALREADY_ATTACKING": 8603,
            "ALREADY_MEMBER": 545,
            "ALREADY_UNDER_ATTACK": 8601,
            "ALREADY_YOU_OTHER": 532,
            "ALREADY_YOU_THIS": 534,
            "ATTACK_DELAY": 8602,
            "ATTACK_STATUS": 8604,
            "BUILDING_MAX": 528,
            "BUILDING_NOT_FOUND": 527,
            "CASH_FULL": 9468,
            "CHAT_HISTORY": 539,
            "CHAT_NOT_MEMBER": 538,
            "CHAT_TEXT_ERROR": 540,
            "DESCR_TOO_LONG": 9531,
            "DONATE_FRA": 558,
            "DONATE_NEG": 557,
            "EMAIL_VALIDATE": 552,
            "FIGHT_TOO_EXPENSIVE": 8600,
            "IS_FULL": 531,
            "LACK_GOLD": 526,
            "LACK_MUSH": 525,
            "MASTER_CANT_BE_OFFICER": 530,
            "MUSH_FREE": 553,
            "NAME_CHARACTERS": 551,
            "NAME_LENGTH": 550,
            "NAME_REJECTED": 549,
            "NOT_ALLOWED": 524,
            "NOT_FOUND": 523,
            "NOT_MEMBER": 529,
            "NOT_REAL_MEMBER": 533,
            "PLAYER_NOT_FOUND": 535,
            "RANK_WRONG": 9400,
            "TOO_EXPENSIVE": 537
        },
        "IMGSVR_DOWN": 607,
        "INBOX_FULL": 508,
        "INPUT_REQUIRED": 562,
        "INVENTORY_FULL": 609,
        "INVENTORY_FULL_ADV": 610,
        "INVITE": {
            "EMAIL_REJECTED": 565,
            "NOT_VALIDATED": 563,
            "TOO_MANY": 564
        },
        "LOGIN_FAILED": 506,
        "MAIL_EXISTS": 556,
        "MSG_LEVEL_TOO_LOW": 8811,
        "MSG_NOT_VALIDATED": 8812,
        "NAME": {
            "EXISTS": 501,
            "MISMATCH": 516,
            "REJECTED": 505,
            "TOO_SHORT": 502
        },
        "NO_ENDURANCE": 543,
        "NO_INDEX_FREE": 521,
        "NO_MUSH_BAR": 542,
        "NO_MUSH_MQ": 548,
        "NO_MUSH_PVP": 547,
        "NO_SLOT_FOR_FLUSHING": 9455,
        "NOT_INVITED": 546,
        "PASSWORD_MISMATCH": 511,
        "PASSWORD_TOO_SHORT": 503,
        "PLAYER_NOT_FOUND": 518,
        "RECIPIENT_NOT_FOUND": 509,
        "RECIPIENT_SELF": 510,
        "REQUEST_PW": 555,
        "SELECTCLASS": 600,
        "SELL_ITEM": 561,
        "SUBJECT_TOO_SHORT": 536,
        "TAVERNE": {
            "ARBEITEN": 602,
            "ARENA": 601,
            "MAINQUEST": 603
        },
        "TOILET_EMPTY": 9456,
        "TOO_EXPENSIVE": 0x0200,
        "TOO_SOON_SUGGESTION": 9419,
        "UNKNOWN": 999,
        "WORSE_MOUNT": 544,
        "WRONG_PASSWORD": 513,
        "ACCOUNTS_PER_IP": 608,
        "LOCKED_ADMIN": 560,
        "LOCKED_PAYMENT": 559
    },
    "GUILD": {
        "AUSBAUEN": 228,
        "GEBAEUDE": {
            "1_POPUP": 225,
            "1_POPUP_EX": 8993,
            "2_POPUP": 226,
            "3_POPUP": 227,
            "NAME1": 4500,
            "STUFE": 181,
            "WERT1": 4510
        },
        "GOLD": 0x0100,
        "GRUENDEN": {
            "TXT": 157,
            "OK": 158,
            "TITLE": 159
        },
        "INVITE": 174,
        "INVITE_TITLE": 175,
        "KICK": 170,
        "KICK_TITLE": 171,
        "MASTER": 172,
        "MASTER_TITLE": 173,
        "MUSH": 0x0101,
        "QUIT": 176,
        "QUIT_1": 271,
        "QUIT_TITLE": 177,
        "RAIDSTART": 9101,
        "RAIDSTART_TITLE": 9100,
        "ATTACK": {
            "FAIL": 8656,
            "PLAYER": 8450,
            "SUCCESS": 8654
        },
        "BATTLE": {
            "LOST": 8505,
            "MSG": 8440,
            "POPUP": 8420,
            "SKIP": 8400,
            "WON": 8500
        },
        "DEFENSE_FAIL": 8658,
        "DEFENSE_SUCCESS": 8657,
        "DUNGEON_COMPLETED": 9449,
        "EPICITEM": 9450,
        "HONOR_GAINED": 8510,
        "HONOR_LOST": 8511,
        "JOINED": 270,
        "JOINED_TOO_RECENTLY": 8660,
        "LEVEL_UP": 9448,
        "RAID_FAIL": 8991,
        "RAID_SUCCESS": 8990
    },
    "GOLD": {
        "TXT": 75,
        "GAINED": 123,
        "LOST": 124,
        "SPENT": 203,
        "BONUS_PREFIX": 232,
        "BONUS_SUFFIX": 233
    },
    "GOTO": {
        "GILDEN": 51,
        "LOGIN": 24,
        "SIGNUP": 25,
        "SPIELER": 50
    },
    "HALL": {
        "LIST": {
            "COLUMN": {
                "1": 52,
                "2": 53,
                "3": 54,
                "3G": 57,
                "4": 55,
                "4G": 58,
                "5": 56
            }
        },
        "GOTO": 49,
        "SUCHFELD_TEXT": 59
    },
    "HUTMANN": {
        "BACK": 303,
        "BETCOMMENT": {
            "1": 297,
            "2": 298,
            "3": 299
        },
        "CANTAFFORD": 300,
        "CHOOSECUP": 292,
        "DAMN": 302,
        "GOLDBET": 290,
        "INSTR": 293,
        "LOSE": 289,
        "MUSHBET": 291,
        "NEWGAME": 296,
        "OFFER": 287,
        "OK": 295,
        "START": 294,
        "WIN": 288,
        "YEAH": 301
    },
    "INV": {
        "ACC_TEXT": 8801,
        "ACC_TITLE": 8800,
        "VAL_TEXT": 8803,
        "VAL_TITLE": 8802
    },
    "INVITE": {
        "EMAIL": 9106,
        "INSTR": 9109,
        "SUBJECT": 9108,
        "SUCCESS": 9110,
        "TITLE": 9107
    },
    "ITEM": {
        "ATTRIB": {
            "CLASS": {
                "1": 1031,
                "10": 1040,
                "11": 1041,
                "12": 1042,
                "2": 1032,
                "3": 1033,
                "4": 1034,
                "5": 1035,
                "6": 1036,
                "7": 1037,
                "8": 1038,
                "9": 1039
            },
            "CLASSES": 1030
        },
        "CLASS": {
            "1": 1001,
            "10": 1010,
            "2": 1002,
            "3": 1003,
            "4": 1004,
            "5": 1005,
            "6": 1006,
            "7": 1007,
            "8": 1008,
            "9": 1009
        },
        "CLASSES": 1000
    },
    "ITMNAME": {
        "10": 3450,
        "10_EPIC": 7450,
        "11": 8300,
        "12": 8350,
        "13": 9112,
        "14": 10000,
        "1": {
            "1": 3000,
            "1_EPIC": 7000,
            "2": 3500,
            "2_EPIC": 7500,
            "3": 3850,
            "3_EPIC": 7850
        },
        "2": {
            "1": 3050,
            "1_EPIC": 7050
        },
        "3": {
            "1": 3100,
            "1_EPIC": 7100,
            "2": 3600,
            "2_EPIC": 7600,
            "3": 3950,
            "3_EPIC": 7950
        },
        "4": {
            "1": 3150,
            "1_EPIC": 7150,
            "2": 3650,
            "2_EPIC": 7650,
            "3": 4000,
            "3_EPIC": 8000
        },
        "5": {
            "1": 3200,
            "1_EPIC": 7200,
            "2": 3700,
            "2_EPIC": 7700,
            "3": 4050,
            "3_EPIC": 8050
        },
        "6": {
            "1": 3250,
            "1_EPIC": 7250,
            "2": 3750,
            "2_EPIC": 7750,
            "3": 4100,
            "3_EPIC": 8100
        },
        "7": {
            "1": 3300,
            "1_EPIC": 7300,
            "2": 3800,
            "2_EPIC": 7800,
            "3": 4150,
            "3_EPIC": 8150
        },
        "8": 3350,
        "8_EPIC": 7350,
        "9": 3400,
        "9_EPIC": 7400,
        "EXT": 4600
    },
    "LUXURY": {
        "ALREADY": 9260,
        "BTN": 9259,
        "BTN2": 9262,
        "BTN3": 9264,
        "BUTTON": 9256,
        "CONFIRM": 9261,
        "CONFIRM2": 9263,
        "TEXT": 9258,
        "TITLE": 9257
    },
    "MOUNT": {
        "TXT": 194,
        "DURATION": 195,
        "FOREVER": 9150,
        "GAIN1": 4520
    },
    "PASSWORD": {
        "TXT": 17,
        "CHANGED": 152,
        "SMILEY": {
            "HAPPY": 8997,
            "NEUTRAL": 8996,
            "SAD": 0x2323
        }
    },
    "PAYICON": {
        "1": 1200,
        "2": 1201,
        "3": 1202,
        "4": 1203,
        "5": 1204,
        "6": 1205
    },
    "POPUP": {
        "INVITE": 205,
        "KICK": 207,
        "LEITER": 209,
        "OFFIZIER": 208,
        "PROFILE": 206,
        "REVOLT": 8650
    },
    "POST": {
        "TXT": 8,
        "ACCEPT": 97,
        "CANCEL": 84,
        "DELETE": 81,
        "FLUSH_TEXT": 9451,
        "FORWARD": 9401,
        "FROM": 94,
        "LIST": {
            "COLUMN": {
                "1": 85,
                "2": 86,
                "3": 87
            }
        },
        "READ": 80,
        "REPLY": 178,
        "RETURN": 96,
        "SEND": 83,
        "TIME": 95,
        "TITLE": {
            "INBOX": 88,
            "READ": 89,
            "WRITE": 90
        },
        "VIEWFIGHT": 238,
        "WRITE": 82
    },
    "PURCHASE": {
        "CANCELLED": 9901,
        "CHECKIN_ERROR": 9905,
        "ERROR": 9902,
        "PAYWAIT": 9904,
        "SUCCESS": 9906,
        "WAIT": 9903
    },
    "QO": {
        "CHOOSE": 98,
        "NO_THIRST": 9784,
        "RETURN": 101,
        "REWARD": 99,
        "START": 100
    },
    "QUEST": {
        "CANCEL": 104,
        "CLOSER": 1450,
        "COLLECT": {
            "AMOUNT": 2050,
            "TITLE": 1330,
            "WHAT": 1650
        },
        "ESCORT": {
            "LOCATION": 6200,
            "PRECLOSER": 6250,
            "TITLE": 6100,
            "WHOM": 6150
        },
        "FETCH": {
            "FROM": 1800,
            "PRECLOSER": 2100,
            "TITLE": 1360,
            "WHAT": 2000
        },
        "KILL": {
            "LOCATION": 1600,
            "PRECLOSER": 1700,
            "TITLE": 5500,
            "WHOM": 5700
        },
        "LOCATION": 1500,
        "OFFER": {
            "TEXT": 6405,
            "TITLE": 0x1900
        },
        "OPENER": 1400,
        "SCOUT": {
            "TASK1": 1550,
            "TASK2": 1750,
            "TITLE": 1300
        },
        "TEXT": 5000,
        "TRANSPORT": {
            "LOCATION": 6000,
            "PRECLOSER": 6050,
            "TITLE": 5900,
            "WHAT": 5950
        }
    },
    "RAID": {
        "LOST": 9005,
        "TEXT": 8820,
        "WON": 9000
    },
    "RANKMSG": {
        "1": 260,
        "2": 261,
        "3": 262,
        "4": 263,
        "5": 264,
        "6": 265,
        "7": 266,
        "8": 267,
        "9": 268,
        "10": 269
    },
    "RESEND": {
        "BTN1": 281,
        "BTN2": 283,
        "TEXT": 282,
        "TITLE": 284
    },
    "REVOLT": {
        "CHAT_MSG": 8653,
        "WARNING": 8651,
        "WARNING_TITLE": 8652
    },
    "RUESTUNG": {
        "TXT": 163,
        "SUM": 199,
        "SUM_HINT": 202
    },
    "SCROLL": {
        "BOUGHT": 10128,
        "BUYHINT": 10123,
        "BUYNOW": 10127,
        "DATE": 10122,
        "NAME": 10120
    },
    "SPECIAL_ACTION": {
        "TEXT_OK": 9226,
        "TEXT_TOOHEALTHY": 0x2400,
        "TITLE": 9206
    },
    "STALL": {
        "STALL": 5,
        "BUY": 112,
        "LAUFZEIT": 111,
        "MOUNTTEXT": 2430,
        "MOUNTTITEL": 2420,
        "PROLONG": 213,
        "SCHATZ": 278,
        "TEXT": 110,
        "TITEL": 109,
        "UPGRADE": 214
    },
    "SUBJECT": {
        "GUILD": {
            "DELETED": 4400,
            "DELETED_BY_ADMIN": 4401,
            "EXPELLED": 4402,
            "EXPELLED_BY_ADMIN": 4403,
            "INVITE": 4404
        },
        "PVP": 4410
    },
    "TITLE": {
        "FORGOT_PASSWORD": 27,
        "SIGNUP": 26,
        "WORK": 40
    },
    "TOILET": {
        "DROPTWICE": 9786,
        "FULL": 9465,
        "HINT": 9457,
        "ITEM": 9785,
        "TANKFULL": 9466
    },
    "TOWER": {
        "TXT": 9470,
        "BONUS": 9773,
        "ENEMY_NAMES": 9570,
        "GUYS": 9770,
        "INFO": 9772,
        "LEVEL": 9771,
        "LOST": 9779,
        "TRY": 9565,
        "WON": 9774
    },
    "VALIDATE": {
        "ERR": 246,
        "ERR_TITLE": 243,
        "OK": 245,
        "OK_TITLE": 242,
        "UNN": 247,
        "UNN_TITLE": 244
    },
    "WITCH": {
        "BOOK": 10124,
        "HINT": 9907,
        "WRONGTYPE": 9915
    },
    "ABBRECHEN": 71,
    "AGB": 28,
    "AGB_LINK": 272,
    "ALBUM": 9111,
    "ALERT_TEXT": 8810,
    "ALERT_WORDS": 8809,
    "ALREADY_VALID": 285,
    "ANLEITUNG_LINK": 274,
    "ARBEITEN": 39,
    "ARENA_TITLE": 115,
    "AUSDAUER": 193,
    "AUSGEWICHEN": 106,
    "BACK": 37,
    "BAD_PASSWORDS": 8994,
    "BASIS": 167,
    "BEARD": 30,
    "BETREFF": 92,
    "BLOCKEN": 119,
    "BONUS": 168,
    "BOOST_COPYCAT": 9564,
    "BROWS": 33,
    "CATAPULT": 9246,
    "CHAT_CAPTION": 182,
    "CHARAKTER": 7,
    "CLASSDESC": 2459,
    "CLASSNAME": 2456,
    "CMD_DONATE_GOLD": 254,
    "CMD_DONATE_MUSH": 0xFF,
    "COLLECTION": 9114,
    "COLOR": 120,
    "COMPARE": 9469,
    "CONGRATS": 8804,
    "COPYCAT_NAME": 9471,
    "COUNTRY_NAMES": 9800,
    "CS": 9204,
    "DATENSCHUTZ": 275,
    "DATENSCHUTZ_LINK": 273,
    "DAY": 309,
    "DAYS": 310,
    "DEBUG_INFO": 286,
    "DISCONNECTED": 216,
    "DURATION": 103,
    "EARS": 34,
    "EHRENHALLE": 10,
    "EMPFAENGER": 91,
    "ENEMY_SELF": 307,
    "ENTERDESC": 116,
    "ENTERGUILDDESC": 179,
    "EXP": 102,
    "EXPBONUS_PREFIX": 230,
    "EXPBONUS_SUFFIX": 231,
    "EXPNEXTLEVEL": 108,
    "EYES": 32,
    "FIGHT_LOSE": 4320,
    "FIGHT_WIN": 4300,
    "FIGHTS_COUNTER": 9105,
    "FONT_NAME": 8700,
    "FORGOT_PASSWORD": 22,
    "FORUM_LINK": 223,
    "FRIEND_SUBJECT": 279,
    "GAMETITLE": 222,
    "GEBLOCKT": 164,
    "GEGNERSTUFE": 229,
    "GENDER_F": 249,
    "GENDER_M": 248,
    "GESAMT": 169,
    "GILDEN": 9,
    "GUILDHALL_LEADER": 304,
    "GUILDHALL_MEMBERS": 305,
    "GUILDNOTEXT": 180,
    "HAIR": 35,
    "HAPPY_HOUR": 9151,
    "HERO_OF_THE_DAY": 8452,
    "HERO_OF_THE_DAY_TITLE": 8451,
    "HEROES_OF_THE_DAY_TITLE": 8453,
    "HL_MAINQUESTS_NAME": 9534,
    "HL_MAINQUESTS_TITLE": 9533,
    "HONOR_GAINED": 121,
    "HONOR_LOST": 122,
    "HOUR": 311,
    "HOURS": 312,
    "IMPRESSUM_LINK": 161,
    "IMPRESSUM_TEXT": 162,
    "ITM_ILLEGAL_COPY": 9475,
    "KRITISCHMINMAX": 200,
    "LEGALCHARS": 280,
    "LM": 317,
    "LOCK_REASON": 9236,
    "LOGIN": 14,
    "LOGIN_LEGAL_1": 276,
    "LOGIN_LEGAL_2": 277,
    "LOGOUT": 48,
    "MAX": 215,
    "MESSAGE": 165,
    "MODIFY_CHARACTER": 155,
    "MONSTER_NAME": 2200,
    "MOUTH": 29,
    "MQ_MUSHHINT": 210,
    "MUSH_DONATE_OBSOLETE": 8998,
    "MUSH_SPENT": 204,
    "MUSHBET_BOUGHT": 308,
    "MUSHROOMS_BOUGHT": 9102,
    "MUTE": 150,
    "NACHRICHT": 93,
    "NAME": 16,
    "NAME_CHANGED": 153,
    "NECESSARY_CLASS": 9559,
    "NEW_HONOR_ACH": 8655,
    "NEW_HONOR_ACH2": 8659,
    "NEW_MONSTER_NAMES": 9010,
    "NOCLASS": 218,
    "NOCLASS_DESC": 219,
    "NODESC": 118,
    "NOGUILD": 107,
    "NOMOUNT": 196,
    "NOSE": 31,
    "OK": 44,
    "OLD_EMAIL": 9104,
    "OPTION_TITLE": 151,
    "OPTIONEN": 12,
    "PILZDEALER": 6,
    "PILZE": 77,
    "POTION_KILL_INSTRUCTIONS": 316,
    "PVP_LOSE": 4235,
    "PVP_WIN": 4215,
    "RACEDESC": 2448,
    "RACENAME": 2440,
    "RANDOM": 47,
    "RANKNAME": 4543,
    "RE": 221,
    "RECONNECT": 217,
    "REMAINING": 315,
    "REQUEST_PASSWORD": 20,
    "REQUEST_SIGNUP": 23,
    "ROB": 9526,
    "ROUNDS_PLURAL": 241,
    "SCHADEN": 160,
    "SCHMIEDE": 3,
    "SELECT_WORLD": 9900,
    "SERVER_STARTED": 8992,
    "SHIELD_FORMULA": 9205,
    "SHOP_LINK": 8805,
    "SHOPS_NEWWAREZ": 79,
    "SIGNUP": 13,
    "SILBER": 76,
    "SILVER_HINT": 220,
    "SKIP_FIGHT": 105,
    "SPECIAL": 45,
    "SPECIAL2": 46,
    "TAG": 197,
    "TAGE": 198,
    "TATTOO": 38,
    "TAVERNE": 1,
    "TEMPORARY": 313,
    "TIMEBAR": 224,
    "TV_DISABLE": 10125,
    "TV_HINT": 10126,
    "UND": 78,
    "UNKNOWN": 9113,
    "UNTIL": 314,
    "VOLUME": 149,
    "WAFFENSCHADEN": 201,
    "WELCOME": 15,
    "WELTKARTE": 11,
    "WHISPER": 8813,
    "WORK_FINISH": 8806,
    "ZAUBERLADEN": 4,
    "ZURGILDE": 183,
}


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


# Image Indices
IMG = {
    "ALBUM": {
        "BG": 24376,
        "CAT_IN": 24425,
        "CAT_OUT": 24420
    },
    "ARENA": {
        "BG": {
            "DAWN": 23297,
            "DAY": 23295,
            "NIGHT": 0x5B00
        },
        "FEUER": 23298
    },
    "BO": {
        "PORTRAIT": {
            "NO": 23627,
            "OK": 23626,
            "TH": 23628
        }
    },
    "BUBBLE": {
        "ARENA": 269,
        "DEALER": 275,
        "ESEL": 270,
        "KRISTALL": 273,
        "ORAKEL": 274,
        "POST": 276,
        "RUHMESHALLE": 272,
        "SHAKES": 279,
        "STATUE": 278,
        "TAVERNE": 271,
        "WACHE": 277,
        "ZAUBERLADEN": 280
    },
    "CHAR": {
        "ACH": 22993,
        "ALBUM": 22965,
        "MOUNT_1": 22979,
        "RUESTUNG": 22991,
        "BACKGROUND": 319,
        "BACKGROUND2": 330,
        "BEARD": 321,
        "BEARD2": 332,
        "BROWS": 324,
        "BROWS2": 335,
        "EARS": 325,
        "EARS2": 336,
        "EYES": 323,
        "EYES2": 334,
        "HAIR": 326,
        "HAIR2": 337,
        "MOUTH": 320,
        "MOUTH2": 331,
        "NOSE": 322,
        "NOSE2": 333,
        "SPECIAL": 327,
        "SPECIAL12": 338,
        "SPECIAL2": 328,
        "SPECIAL22": 339
    },
    "CITY": {
        "ARENA": {
            "IMG": 222,
            "ONO": {
                "1": 223,
                "2": 224,
                "3": 225,
                "4": 226
            }
        },
        "DEALER": {
            "IMG": 228,
            "ANI": {
                "1": 229,
                "2": 230,
                "3": 231,
                "4": 232,
                "5": 233
            }
        },
        "ELF1": 0x0101,
        "ELF2": 258,
        "ESEL1": 235,
        "ESEL2": 236,
        "MAGIER1": 249,
        "MAGIER2": 250,
        "ORK1": 251,
        "ORK2": 252,
        "POST": 240,
        "RUHMESHALLE": 220,
        "SANDWICH1": 253,
        "SANDWICH2": 254,
        "SCHILD": {
            "1": 245,
            "2": 246,
            "3": 247,
            "4": 248
        },
        "SHAKES": 216,
        "TAVERNE": 238,
        "WACHE_DAY": 242,
        "WACHE_NIGHT": 243,
        "ZAUBERLADEN": 218,
        "ZWERG1": 0xFF,
        "ZWERG2": 0x0100
    },
    "DEALER": {
        "ARM": {
            "1": 23215,
            "2": 23216,
            "3": 23217,
            "4": 23218
        },
        "AUGEN": {
            "1": 23219,
            "2": 23220,
            "3": 23221,
            "4": 23222
        },
        "EFFECT": 23253,
        "PAYICON": {
            "1": 23226,
            "2": 23227,
            "3": 23228,
            "4": 23229,
            "5": 23230,
            "6": 23231,
            "7": 23232,
            "8": 23233,
            "9": 23234
        },
        "PAYICONHOVER": {
            "1": 23235,
            "2": 23236,
            "3": 23237,
            "4": 23238,
            "5": 23239,
            "6": 23240,
            "7": 23241,
            "8": 23242,
            "9": 23243
        }
    },
    "DUNGEON_CONGRATS": 24354,
    "EMPTY": {
        "SLOT": {
            "1": 438,
            "9_1": 446,
            "9_2": 447,
            "9_3": 448,
            "10": 449
        }
    },
    "FIDGET": {
        "AFFE": {
            "1": 23080,
            "2": 23081,
            "3": 23082
        },
        "BLINZELN": 23089,
        "DAY": 23085,
        "EPCIOVL": 24536,
        "IDLE": 23086,
        "NACHTKERZE": 23084,
        "NIGHT": 23088,
        "SALE": 23087,
        "TAGKERZE": 23083
    },
    "FIGHT": {
        "ARROW_SMASH": 24219,
        "BOX1": 24198,
        "BOX2": 24199,
        "CHAR_BORDER": 24184,
        "COPYCAT": 24759,
        "MUSH": 24534,
        "ONO": 24213
    },
    "GILDE": {
        "ATTACK_GRAY": 23383,
        "ATTACK_OK": 23384,
        "CREST": {
            "IMG": 24543,
            "COLOR": {
                "FILLIN": 24579,
                "SELECTED": 24575,
                "UNSELECTED": 24571
            },
            "SHIELDCOLOR": 24590
        },
        "DEFEND_GRAY": 23385,
        "DEFEND_OK": 23386,
        "GEBAEUDE": 23450,
        "GEBAEUDE_IMPROVE_GRAY": 23483,
        "INVITE_GRAY": 23391,
        "KATAPULT_GRAY": 24517,
        "KATAPULT_OK": 24518,
        "KICK_GRAY": 23393,
        "MASTER_GRAY": 23395,
        "PROFILE_GRAY": 23392,
        "PROMOTE_GRAY": 23394,
        "RAHMEN": 23360,
        "RAID_GRAY": 23379,
        "RAID_OK": 23380,
        "RANK": 23397,
        "GILDEN_BG": 23359
    },
    "HLMQS": {
        "BUTTON": 24773,
        "COMPLETED": 24764,
        "DISABLED": 24763,
        "TOWER_COMPLETED": 24766,
        "TOWER_DISABLED": 24765
    },
    "HUTBECHER": {
        "1_CLICK": 23555,
        "1_HOVER": 23554,
        "1_IDLE": 23553,
        "2_CLICK": 23558,
        "2_HOVER": 23557,
        "2_IDLE": 23556,
        "3_CLICK": 23561,
        "3_HOVER": 23560,
        "3_IDLE": 23559
    },
    "HUTFACE": {
        "HOVER": 23548,
        "IDLE": 23547,
        "LOSE": {
            "1": 23550,
            "2": 23551,
            "3": 0x5C00
        },
        "WIN": 23549
    },
    "IF": {
        "BACKGROUND": 5,
        "GOLD": 27,
        "HUTMANN": {
            "1": 37,
            "2": 38,
            "OVL": 40
        },
        "JAEGER": 35,
        "KRIEGER": 34,
        "LEFT": 6,
        "MAGIER": 36,
        "MAIN": 8,
        "PILZE": 29,
        "SILBER": 28,
        "SPONSOR": 17,
        "TOILET": 25610,
        "TOP": 7,
        "WINDOW": {
            "IMG": 45,
            "HIGH": 25612,
            "TOPHALF": 25613
        }
    },
    "KASTE": {
        "1_ACT": 158,
        "1_IDLE": 157,
        "2_ACT": 160,
        "2_IDLE": 159,
        "3_ACT": 162,
        "3_IDLE": 161
    },
    "MQS": {
        "BUTTON": 24321,
        "COMPLETED": 24352,
        "DISABLED": 24341
    },
    "OP": {
        "BEARD": 23836,
        "BEARD2": 23847,
        "BROWS": 23839,
        "BROWS2": 23850,
        "EARS": 23840,
        "EARS2": 23851,
        "HAIR": 23841,
        "HAIR2": 23852,
        "SPECIAL": 23842,
        "SPECIAL12": 23853,
        "SPECIAL2": 23843,
        "SPECIAL22": 23854
    },
    "OPP": {
        "BACKGROUND": 23834,
        "BACKGROUND2": 23845,
        "EYES": 23838,
        "EYES2": 23849,
        "MONSTER": 24800,
        "MOUTH": 23835,
        "MOUTH2": 23846,
        "NOSE": 23837,
        "NOSE2": 23848
    },
    "OPTION": {
        "BOX": 24256,
        "FLAG": 24627,
        "IMAGEBORDER": 24248
    },
    "PASSWORD": {
        "SMILEY": {
            "HAPPY": 58,
            "NEUTRAL": 57,
            "SAD": 56
        }
    },
    "POST": {
        "BG": 23258,
        "DAWN1": 23259,
        "DAWN2": 23260,
        "NIGHT1": 23261,
        "NIGHT2": 23262
    },
    "QUESTBAR": {
        "BG": 23207,
        "FILL": 23208,
        "LIGHT": 23209
    },
    "SCR": {
        "BUILDCHAR_BACKGROUND": 117,
        "CHAR": {
            "BG": {
                "IMG": 352,
                "GOLDEN": 24530,
                "RIGHT": 353
            },
            "EXPBAR": 358,
            "KLASSE": {
                "1": 22952,
                "2": 22953,
                "3": 22954
            }
        },
        "CITY": {
            "BACKG": {
                "DAWN": 205,
                "DAY": 206,
                "NIGHT": 204
            },
            "CLOUDS": {
                "DAWN": 211,
                "DAY": 212,
                "NIGHT": 210
            },
            "FOREG": {
                "DAWN": 214,
                "DAY": 215,
                "NIGHT": 213
            },
            "MAIN": {
                "DAWN": 208,
                "DAY": 209,
                "NIGHT": 207
            }
        },
        "DEALER_BG": 23214,
        "FIDGET_BG": 23101,
        "HALLE_BG": 282,
        "QUEST_BG_1": 23107,
        "SHAKES_BG": 23100,
        "TOWER_BG": 24792,
        "WORLDMAP_BG": 23105
    },
    "SHAKES": {
        "BLINZELN1": 23098,
        "BLINZELN2": 23099,
        "DAY": 23092,
        "EPCIOVL": 24537,
        "IDLE": {
            "IMG": 23093,
            "1": 23095,
            "2": 23096,
            "3": 23097
        },
        "NIGHT": 23094
    },
    "STALL": {
        "ARME": {
            "1": 23312,
            "2": 23313,
            "3": 23314,
            "4": 23315,
            "5": 23316
        },
        "BG_BOESE": 23309,
        "BG_GUT": 23308,
        "DAWN": 23310,
        "NIGHT": 23311,
        "OVL": {
            "BOESE": {
                "1": 23321,
                "2": 23322,
                "3": 23323,
                "4": 23324
            },
            "GUT": {
                "1": 23317,
                "2": 23318,
                "3": 23319,
                "4": 23320
            }
        }
    },
    "TAVERN": {
        "ADVENT": 25711,
        "BARKEEPER1": 23520,
        "BARKEEPER2": 23521,
        "BARKEEPER_HINT": 24538,
        "BAROVL": 23540,
        "BG": 23519,
        "HUTMANN_BLINZELN": 23522,
        "HUTMANN_OVL": 23523,
        "KERZEN": 23525,
        "QUEST": {
            "1": 23526,
            "2": 23527,
            "3": 23528,
            "4": 23529,
            "5": 23530
        },
        "QUESTOVL": {
            "1": 23534,
            "2": 23535,
            "3": 23536,
            "4": 23537,
            "5": 23538
        }
    },
    "TOILET": {
        "IMG": 24599,
        "CHAIN": 24610,
        "DROP": 24618,
        "FLUSH": 24602,
        "IDLE": 24617
    },
    "TOWER": {
        "BASE": 24744,
        "BG": 24715,
        "LEVEL": 24745,
        "PORTRAIT": 24756,
        "PORTRAIT1": 24717,
        "ROOF": 24748,
        "WINDOW": {
            "BURNT": 24751,
            "CLOSED": 24750,
            "OPEN": 24749
        }
    },
    "VOLK": {
        "1": {
            "F_ACT": 145,
            "F_IDLE": 137,
            "M_ACT": 129,
            "M_IDLE": 120
        },
        "2": {
            "F_ACT": 146,
            "F_IDLE": 138,
            "M_ACT": 130,
            "M_IDLE": 121
        },
        "3": {
            "F_ACT": 147,
            "F_IDLE": 139,
            "M_ACT": 131,
            "M_IDLE": 122
        },
        "4": {
            "F_ACT": 148,
            "F_IDLE": 140,
            "M_ACT": 132,
            "M_IDLE": 123
        },
        "5": {
            "F_ACT": 149,
            "F_IDLE": 141,
            "M_ACT": 133,
            "M_IDLE": 124
        },
        "6": {
            "F_ACT": 150,
            "F_IDLE": 142,
            "M_ACT": 134,
            "M_IDLE": 125
        },
        "7": {
            "F_ACT": 151,
            "F_IDLE": 143,
            "M_ACT": 135,
            "M_IDLE": 126
        },
        "8": {
            "F_ACT": 152,
            "F_IDLE": 144,
            "M_ACT": 136,
            "M_IDLE": 127
        },
        "MARKER": 128
    },
    "WEAPON": {
        "BONE": 24223,
        "CLAW": 24231,
        "CLAW2": 24232,
        "CLAW3": 24233,
        "CLAW4": 24234,
        "FIRE": 24228,
        "FIRE2": 24229,
        "FIRE3": 24230,
        "FIST": 24221,
        "SPLAT": 24225,
        "SPLAT2": 24226,
        "SPLAT3": 24227,
        "STICK": 24224,
        "STONEFIST": 24222,
        "SWOOSH": 24235,
        "SWOOSH2": 24236,
        "SWOOSH3": 24237
    },
    "BEERFEST": 24480,
    "BG_DEMO": 24241,
    "GOLD": 42,
    "PILZE": 44,
    "SILBER": 43,
    "F_ACT": 156,
    "F_IDLE": 155,
    "FILLSPACE": 68,
    "GOLDEN_FRAME": 24506,
    "GOTO_WITCH_OVL": 25672,
    "GUILD_BATTLE_BG": 24238,
    "GUILD_RAID_BG": 24239,
    "HUTKUGEL": 23565,
    "HUTMANN_BG": 23546,
    "HUTMANN_MUSHBET_DISABLED": 23573,
    "LIFEBAR_CHAR": 0x5E5E,
    "LIFEBAR_FILL_CHAR": 24160,
    "LUXURY_SELLER": 24535,
    "M_ACT": 154,
    "M_IDLE": 153,
    "MAINQUEST_COMINGSOON": 24365,
    "MIRROR_PIECE": 24701,
    "NO_SHIELD": 25609,
    "QO_PORTRAIT1": 23620,
    "SLOT_SUGGESTION": 437,
    "SOCIAL": 24440,
    "SPECIAL_ACTION": 24486,
    "TIMEBAR_BG": 23542,
    "TIMEBAR_FILL": 23543,
    "TV": 25707,
    "UNKNOWN_ENEMY": 24439,
    "WITCH": 25637,
    "WITCH_ANI": 25673,
}


# Absolute positions X/Y
POS = {
    "BUBBLE": {
        "ARENA_X": 375,
        "ARENA_Y": 228,
        "DEALER_X": 606,
        "DEALER_Y": 480,
        "ESEL_X": 289,
        "ESEL_Y": 495,
        "KRISTALL_X": 582,
        "KRISTALL_Y": 175,
        "ORAKEL_X": 782,
        "ORAKEL_Y": 155,
        "POST_X": 775,
        "POST_Y": 440,
        "RUHMESHALLE_X": 1076,
        "RUHMESHALLE_Y": 593,
        "SHAKES_X": 1032,
        "SHAKES_Y": 517,
        "STATUE_X": 1136,
        "STATUE_Y": 381,
        "TAVERNE_X": 468,
        "TAVERNE_Y": 441,
        "WACHE_X": 500,
        "WACHE_Y": 625,
        "ZAUBERLADEN_X": 964,
        "ZAUBERLADEN_Y": 343
    },
    "CHAR": {
        "MOUNT_X": 805,
        "MOUNT_Y": 429,
        "NAME_X": 410,
        "NAME_Y": 345,
        "PLAYER": {
            "X1": 830,
            "X2": 1030,
            "Y": 715
        },
        "PROP": {
            "COLUMN": {
                "1_X": 304,
                "2_X": 405,
                "3_X": 470,
                "4_X": 520,
                "5_X": 520,
                "6_X": 650
            },
            "Y": 517
        },
        "SLOTS": {
            "LEFT_X": 304,
            "R4C2_X": 441,
            "R4C3_X": 543,
            "R5C2_X": 398,
            "R5C3_X": 493,
            "R5C4_X": 588,
            "RIGHT_X": 680,
            "ROW2_Y": 217,
            "ROW3_Y": 317,
            "ROW4_Y": 417,
            "ROW5_Y": 679,
            "TOP_Y": 117
        }
    },
    "CITY": {
        "ARENA_X": 280,
        "ARENA_Y": 100,
        "CA": {
            "ARENA_X": 280,
            "ARENA_Y": 170,
            "BUH_X": 1105,
            "BUH_Y": 410,
            "DEALER_X": 570,
            "DEALER_Y": 580,
            "ESEL_X": 280,
            "ESEL_Y": 618,
            "POST_X": 830,
            "POST_Y": 500,
            "RUHMESHALLE_X": 1150,
            "RUHMESHALLE_Y": 400,
            "SHAKES_X": 945,
            "SHAKES_Y": 550,
            "TAVERNE_X": 440,
            "TAVERNE_Y": 530,
            "WACHE_X": 670,
            "WACHE_Y": 570,
            "ZAUBERLADEN_X": 985,
            "ZAUBERLADEN_Y": 410
        },
        "DEALER_X": 578,
        "DEALER_Y": 593,
        "ELF_X": 943,
        "ELF_Y": 405,
        "ESEL_X": 280,
        "ESEL_Y": 618,
        "MAGIER_X": 655,
        "MAGIER_Y": 630,
        "ORK_X": 850,
        "ORK_Y": 580,
        "POST_X": 872,
        "POST_Y": 546,
        "RUHMESHALLE_X": 1135,
        "RUHMESHALLE_Y": 340,
        "SANDWICH_X": 780,
        "SANDWICH_Y": 610,
        "SCHILD_X": 739,
        "SCHILD_Y": 623,
        "SHAKES_X": 1023,
        "SHAKES_Y": 585,
        "TAVERNE_X": 471,
        "TAVERNE_Y": 560,
        "WACHE_X": 670,
        "WACHE_Y": 582,
        "ZAUBERLADEN_X": 1014,
        "ZAUBERLADEN_Y": 446,
        "ZWERG_X": 480,
        "ZWERG_Y": 580
    },
    "DEALER": {
        "AKTION_X": 290,
        "AKTION_Y": 235,
        "ARM_X": 455,
        "ARM_Y": 265,
        "AUGEN_X": 605,
        "AUGEN_Y": 265,
        "MENU_X": 760,
        "MENU_Y": 430,
        "SPONSOR_X": 1080,
        "SPONSOR_Y": 520
    },
    "DEMO": {
        "X": 1050,
        "Y": 700,
        "Y1": 380
    },
    "FIGHT": {
        "Y": 710,
        "CHAR": {
            "PROP": {
                "COLUMN": {
                    "1_X": 324,
                    "2_X": 450,
                    "3_X": 1059,
                    "4_X": 1185
                },
                "Y": 520
            },
            "X": 315
        },
        "REWARD": {
            "EXP_X": 535,
            "GOLD_X": 1000,
            "GOLD_Y": 640,
            "MUSH_Y": 610
        },
        "SLOT_Y": 580,
        "SUMMARY_Y": 520,
        "WEAPONS_Y": 350
    },
    "GILDE": {
        "ATTACKX": 450,
        "ATTACKLABEL_X": 570,
        "CHAT": {
            "FIELD_Y": 743,
            "X": 305,
            "Y": 624
        },
        "DEFENDX": 505,
        "GEBAEUDE_X": 310,
        "GEBAEUDE_Y": 162,
        "GOLD_Y": 488,
        "GOLDMUSH_X": 670,
        "LIST": {
            "SCROLLX": 1205,
            "SCROLLY": 520,
            "X": 997,
            "Y": 160
        },
        "RANG_X": 300,
        "RANG_Y": 115,
        "TEXT_X": 580,
        "TOOLX": 989,
        "TOOLY": 564
    },
    "HALL": {
        "LIST_X": 580,
        "LIST_Y": 235,
        "GOTO": {
            "X": 875,
            "Y": 570,
            "GILDEN_X": 870,
            "SPIELER_X": 670,
            "SPIELERGILDEN_Y": 145
        },
        "DOWN_Y": 565,
        "INP_GOTO_X": 615,
        "INP_GOTO_Y": 585,
        "UP_Y": 195,
        "UPDOWN_X": 980
    },
    "HUTMANN": {
        "BACK_X": 1140,
        "BACK_Y": 620,
        "GOLD_Y": 660,
        "INSTR_X": 300,
        "INSTR_Y": 115,
        "KUGEL_X1": 535,
        "KUGEL_X2": 762,
        "KUGEL_X3": 1004,
        "OK_X": 960,
        "OK_Y": 650,
        "TEXT_Y": 635
    },
    "IF": {
        "X": 20,
        "Y": 180,
        "ERROR_X": 770,
        "ERROR_Y": 670,
        "EXIT_X": 1220,
        "EXIT_Y": 120,
        "HUTLINK_X": 35,
        "HUTLINK_Y": 185,
        "LBL_GOLD_Y": 115,
        "LBL_GOLDPILZE_X": 230,
        "LBL_PILZE_Y": 145,
        "WIN_X": 540,
        "WIN_Y": 250
    },
    "MQ": {
        "CS_X": 680,
        "CS_Y": 450,
        "ERROR_Y": 735,
        "SQUARE_X": 470,
        "SQUARE_Y": 80
    },
    "MQS": {
        "BUTTON_X": 380,
        "BUTTON_Y": 170,
        "TITLE_Y": 115
    },
    "POST": {
        "ADDRESS_Y": 190,
        "BUTTONS_X": 330,
        "BUTTONS_Y": 685,
        "ERROR_Y": 740,
        "INP_X": 330,
        "LIST_X": 330,
        "LIST_Y": 190,
        "PROFILE_X": 1170,
        "SCROLLX": 1190,
        "SCROLLDOWN_Y": 695,
        "SCROLLUP_Y": 190,
        "SENDBUTTON_Y": 685,
        "SQUARE_X": 320,
        "SQUARE_Y": 100,
        "SUBJECT_Y": 220,
        "TEXT_Y": 250
    },
    "QUEST": {
        "CANCEL_X": 780,
        "CANCEL_Y": 700,
        "ERROR_Y": 540
    },
    "QUESTBAR": {
        "LABEL_X": 778,
        "LABEL_Y": 625,
        "X": 390,
        "Y": 580
    },
    "SCR": {
        "BUILDCHAR": {
            "1_X": 312,
            "1_Y": 134,
            "CASTE_X": 332,
            "CASTE_Y": 610,
            "CREATE_X": 702,
            "CREATE_Y": 715,
            "GENDER_X": 372,
            "GENDER_Y": 195,
            "LOGIN_X": 1230,
            "LOGIN_Y": 725,
            "VOLK_X": 345,
            "VOLK_Y": 300
        },
        "CHAR": {
            "ACH_X": 795,
            "ACH_Y": 635,
            "CHARX": 408,
            "CHARY": 119
        },
        "SHOP_BG_X": 780
    },
    "SCREEN": {
        "BACK_BUTTON_X": 1120,
        "BACK_BUTTON_Y": 650,
        "RANDOM_BUTTON_X": 1030,
        "RANDOM_BUTTON_Y": 620,
        "TITLE": {
            "X": 770,
            "Y": 120,
            "Y_GUILD": 110,
            "Y_QUEST": 120
        }
    },
    "SHOP": {
        "ERROR_X": 1030,
        "ERROR_Y": 185,
        "SLOTS": {
            "C1_X": 856,
            "C2_X": 972,
            "C3_X": 1088,
            "R1_Y": 560,
            "R2_Y": 680
        },
        "X": 860
    },
    "STADT": {
        "BACKG_X": 280,
        "BACKG_Y": 101,
        "MAIN_X": 280,
        "MAIN_Y": 365
    },
    "STALL_ERROR_Y": 500,
    "STALL_SQUARE_Y": 560,
    "TAVERNE": {
        "BAR_X": 1030,
        "BAR_Y": 320,
        "BAROVL_X": 1093,
        "BAROVL_Y": 320
    },
    "TIMEBAR": {
        "LABEL_X": 0x0300,
        "LABEL_Y": 705,
        "X": 380,
        "Y": 660
    },
    "LBL": {
        "ARBEITEN": {
            "TEXT": {
                "2_Y": 475,
                "X": 590,
                "Y": 340
            }
        }
    },
    "AGB_X": 150,
    "ANLEITUNG_X": 1000,
    "ANLEITUNG_X_WITH_SHOP": 1035,
    "ARBEITEN_SLIDER_X": 650,
    "ARBEITEN_SLIDER_Y": 420,
    "ARENA_FEUER_X": 442,
    "ARENA_FEUER_Y": 126,
    "CREATE_RACE_X": 640,
    "CREATE_RACE_Y": 520,
    "DATENSCHUTZ_X": 250,
    "DISCONNECTED_X": 780,
    "DISCONNECTED_Y": 360,
    "EMAIL_NAG_X": 580,
    "EMAIL_NAG_Y": 340,
    "EXPERIENCE_BAR_X": 409,
    "EXPERIENCE_BAR_Y": 381,
    "FORUM_X": 900,
    "FORUM_X_WITH_SHOP": 945,
    "GILDEEHRE_X": 795,
    "GILDEEHRE_Y": 120,
    "IMPRESSUM_X": 380,
    "LM_X": 370,
    "LM_Y": 600,
    "LOGOUT_X": 1100,
    "LOGOUT_X_WITH_SHOP": 1130,
    "LOGOUT_Y": 50,
    "MAINQUEST_ENEMY_X": 630,
    "MAINQUEST_ENEMY_Y": 330,
    "MODIFY_CHARACTER_BUTTONS_X": 1020,
    "MODIFY_CHARACTER_BUTTONS_Y": 160,
    "NEW_WAREZ_X": 1025,
    "NEW_WAREZ_Y": 495,
    "OPPX": 930,
    "OPPY": 130,
    "OPTION_X": 350,
    "OPTION_Y": 180,
    "POTION_X": 1079,
    "POTION_Y": 590,
    "QO_BLACK_SQUARE_X": 410,
    "QO_BLACK_SQUARE_Y": 230,
    "SPONSOR_X": 1020,
    "SPONSOR_Y": 0
}


# Relative positions
REL = {
    "ARBEITEN": {
        "BAR_X": 55,
        "BAR_Y": 200,
        "Y": 270,
        "FILL_X": 110,
        "FILL_Y": 222
    },
    "ARENA": {
        "DELAY_X": 75,
        "DELAY_Y": 292,
        "INP_Y": 220,
        "OK_Y": 280,
        "TEXT_Y": 80
    },
    "CHAR": {
        "DELAY_X": 335,
        "DELAY_Y": 655,
        "EHRE_X": 20,
        "MOUNT_X": 274,
        "MOUNT_LINE_Y": 25,
        "PROP_Y": 32,
        "RUESTUNG": {
            "TEXT_X": 45,
            "TEXT_Y": 7,
            "X": 15,
            "Y": 495
        },
        "X": 20,
        "Y": 51
    },
    "FIDGET": {
        "AFFE_X": 425,
        "AFFE_Y": 128,
        "BLINZELN_X": 107,
        "BLINZELN_Y": 88,
        "NACHTKERZE_X": 63,
        "NACHTKERZE_Y": 236,
        "TAGKERZE_X": 212,
        "TAGKERZE_Y": 12,
        "X": 74,
        "Y": 168
    },
    "FIGHT": {
        "BOX": {
            "1_X": -17,
            "1_Y": -15,
            "3_X": -17
        },
        "CHAR_PROP_Y": 32
    },
    "GILDE": {
        "BUILDING_Y": 100,
        "CHAT": {
            "CAPTION_Y": 32,
            "DOWN_Y": 75,
            "UP_Y": 5,
            "Y": 22
        },
        "DEFENSELABEL_Y": 24,
        "GEBAEUDE": {
            "IMPROVE_X": 105,
            "IMPROVE_Y": 53,
            "LINE": 24,
            "Y": 133
        },
        "GOLDMUSH": {
            "C1": 10,
            "C2": 205,
            "C3": 0
        },
        "GRUENDEN": {
            "INP_Y": 220,
            "OK_Y": 280,
            "TEXT_Y": 80
        },
        "INP_Y": 220,
        "LIST": {
            "C1": 23,
            "X": 200,
            "Y": 26
        },
        "MUSH_Y": 27,
        "OK_Y": 280,
        "TEXT": {
            "IMPROVE_X": 143,
            "X": 105,
            "Y": 80
        },
        "TOOLX": 53,
        "EHRE_X": 10,
        "EHRE_Y": 10
    },
    "HALL": {
        "LIST": {
            "COLUMN": {
                "1_X": 0,
                "2_X": 60,
                "3_X": 80,
                "4_X": 200,
                "5_X": 320,
                "6_X": 370,
            },
            "LINE_Y": 20,
            "LINES_Y": 0
        }
    },
    "HUTMANN": {
        "BECHER": {
            "1_X": 204,
            "1_X2": 0,
            "1_X3": 0,
            "1_Y": 417,
            "1_Y2": -72,
            "1_Y3": -127,
            "2_X": 430,
            "2_X2": -201,
            "2_X3": -203,
            "2_Y": 417,
            "2_Y2": -54,
            "2_Y3": -120,
            "3_X": 669,
            "3_X2": -16,
            "3_X3": -16,
            "3_Y": 417,
            "3_Y2": -39,
            "3_Y3": -89
        },
        "FACE_X": 389,
        "FACE_Y": 115
    },
    "IF": {
        "1": 44,
        "2": 20,
        "GOTO_LOGIN_X": 450,
        "WIN": {
            "2_Y": 35,
            "X": -87,
            "Y": 250,
            "CB_X": 70,
            "CB_Y": 245,
            "INPUTS": {
                "DISTANCE_Y": 55,
                "FIELD_X": 80,
                "FIELD_Y": -15,
                "X": 70,
                "Y": 100
            },
            "LNK_1_Y": -40,
            "LNK_2_Y": 50,
            "WELCOME_X": 250,
            "WELCOME_Y": 45
        }
    },
    "MODIFY": {
        "CHARACTER": {
            "BUTTONS_1": 45,
            "BUTTONS_2": 55,
            "LABEL_X": 50,
            "LABEL_Y": 6
        }
    },
    "MQ": {
        "BORDER_X": 10,
        "BORDER_Y": 10,
        "BUTTON_Y": -20,
        "MUSHHINT_Y": -15,
        "TEXT_X": 20,
        "TEXT_Y": 130,
        "TITLE_Y": 90
    },
    "OPTION": {
        "BOX": {
            "1_X": -5,
            "1_Y": -5,
            "2_X": -5,
            "2_Y": -5
        },
        "CHANGE_X": 230,
        "DOCHANGE": {
            "X": 640,
            "FIELD_X": 570,
            "LABEL_X": 440,
            "X1": 430
        },
        "IMAGE_X": 20,
        "TEXT_Y": 13,
        "VER_X": 825,
        "VER_Y": 450,
        "VOLUME_X": 287,
        "Y0": 15,
        "Y1": 65,
        "Y2": 105,
        "Y3": 170,
        "Y4": 235,
        "Y5": 300,
        "Y6": 380,
        "Y7": 430
    },
    "POPUP": {
        "TAB": 120,
        "TAB1": 35,
        "TAB2": 100,
        "TAB3": 130,
        "TAB_ADD": 17
    },
    "POST": {
        "BUTTONS_X": 5,
        "FENSTER_X": 479,
        "FENSTER_Y": 14,
        "LIMIT_X": -10,
        "LIMIT_Y": -55,
        "LIST": {
            "COLUMN": {
                "1_X": 0,
                "2_X": 160,
                "3_X": 660
            },
            "LINE_Y": 30,
            "LINES_Y": 0
        },
        "SQUARE_X": 910,
        "SQUARE_Y": 560,
        "VOGEL_X": 234,
        "VOGEL_Y": 100
    },
    "QO": {
        "CHOICES_Y": 40,
        "CHOOSE_X": 20,
        "CHOOSE_Y": 280,
        "PORTRAIT_X": 20,
        "PORTRAIT_Y": 20,
        "QUESTNAME_X": 480,
        "QUESTNAME_Y": 20,
        "QUESTSTODAY_X": 500,
        "QUESTSTODAY_Y": 20,
        "QUESTTEXT_X": 250,
        "QUESTTEXT_Y": 60,
        "RETURN_Y": 325,
        "REWARD_Y": 280,
        "REWARDS_Y": 40,
        "SLOT_X": 400,
        "SLOT_Y": 335,
        "START_X": 550,
        "START_Y": 380
    },
    "SCR": {
        "BUILDCHAR": {
            "CASTE_X": 80,
            "GENDER_X": 80,
            "VOLK_X": 130,
            "VOLK_Y": 70
        },
        "CHAR_ACH_X": 55,
        "CHAR_ACH_X_BUFFED": 65
    },
    "SHAKES": {
        "BLINZELN_X": 56,
        "BLINZELN_Y": 33,
        "IDLE2_X": 54,
        "IDLE2_Y": 115,
        "IDLE_X": 88,
        "IDLE_Y": 212,
        "X": 171,
        "Y": 112
    },
    "STALL": {
        "ARME_X": 373,
        "ARME_Y": 181,
        "BOX": {
            "1_X": 0,
            "1_Y": 50,
            "2_X": 225,
            "2_Y": 81,
            "3_X": 585,
            "3_Y": 78,
            "4_X": 778,
            "4_Y": 50
        },
        "GAIN_Y": 40,
        "OVL": {
            "BOESE": {
                "1_X": 100,
                "1_Y": 305,
                "2_X": 254,
                "2_Y": 217,
                "3_X": 578,
                "3_Y": 310,
                "4_X": 756,
                "4_Y": 168
            },
            "GUT": {
                "1_X": 80,
                "1_Y": 265,
                "2_X": 303,
                "2_Y": 291,
                "3_X": 580,
                "3_Y": 145,
                "4_X": 761,
                "4_Y": 263
            },
        },
        "TITEL_X": 10,
        "TITEL_Y": 10,
        "TUER_X": 428,
        "TUER_Y": 96,
        "ZEILEN_Y": 10
    },
    "TAVERNE": {
        "BARKEEPER_X": 796,
        "BARKEEPER_Y": 322,
        "HUT_X": 136,
        "HUT_Y": 344,
        "HUTAUGEN_X": 171,
        "HUTAUGEN_Y": 377,
        "KERZEN_X": 364,
        "KERZEN_Y": 21,
        "QUEST_X": 285,
        "QUEST_Y": 281,
        "QUESTOVL": {
            "1_X": 182,
            "1_Y": 60,
            "2_X": 149,
            "2_Y": 116,
            "3_X": 180,
            "3_Y": 58,
            "4_X": 169,
            "4_Y": 44,
            "5_X": 30,
            "5_Y": 31
        }
    },
    "AGB_LBL_X": 50,
    "AGB_LBL_Y": 8,
    "BLACK_CHARDESC_Y": 15,
    "BUILDCHAR_LINES_Y": 10,
    "COMPARE_TAB": 280,
    "DEALER_2Y": -15,
    "DEALER_3Y": -40,
    "DRAGON_X": 180,
    "DRAGON_Y": -10,
    "EMAIL_NAG_Y": 280,
    "EMAIL_RESEND_Y": 150,
    "HUTKUGEL_Y": 500,
    "LBL_ARBEITEN_TIME_Y": 160,
    "LIFEBAR_Y": 15,
    "LM_X": 50,
    "LM_Y": 6,
    "MQS_BUTTON_X": 280,
    "MQS_BUTTON_Y": 195,
    "POTION_X": 50,
    "STADT_FOREG_Y": 96,
}


# Element Sizes
SIZE = {
    "CITY": {
        "CA": {
            "ARENA_X": 360,
            "ARENA_Y": 220,
            "BUH_X": 45,
            "BUH_Y": 55,
            "DEALER_X": 60,
            "DEALER_Y": 85,
            "ESEL_X": 150,
            "ESEL_Y": 150,
            "POST_X": 120,
            "POST_Y": 140,
            "RUHMESHALLE_X": 150,
            "RUHMESHALLE_Y": 380,
            "SHAKES_X": 160,
            "SHAKES_Y": 170,
            "TAVERNE_X": 120,
            "TAVERNE_Y": 150,
            "WACHE_X": 115,
            "WACHE_Y": 130,
            "ZAUBERLADEN_X": 110,
            "ZAUBERLADEN_Y": 120
        }
    },
    "DEALER": {
        "AKTION_X": 190,
        "AKTION_Y": 170,
        "SPONSOR_X": 190,
        "SPONSOR_Y": 170
    },
    "GILDE": {
        "CHAT_EXT_X": 950,
        "GRUENDEN_TEXT_X": 400,
        "TEXT2_X": 400,
        "TEXT_X": 900,
        "EHRE_X": 375,
        "EHRE_Y": 40
    },
    "STALL": {
        "BOX": {
            "1_X": 200,
            "1_Y": 480,
            "2_X": 183,
            "2_Y": 382,
            "3_X": 176,
            "3_Y": 392,
            "4_X": 218,
            "4_Y": 476
        },
        "SQUARE_X": 700,
        "SQUARE_Y": 200
    },
    "TAVERNE": {
        "BAR_X": 200,
        "BAR_Y": 200,
        "HUT_X": 100,
        "HUT_Y": 130,
        "QUEST_X": 312,
        "QUEST_Y": 307
    },
    "ARENA_TEXT_X": 400,
    "BLACK_CHARDESC_X": 440,
    "BLACK_CHARDESC_Y": 200,
    "BUILDCHAR_LINES_X": 300,
    "COPYCAT": 148,
    "DISCONNECTED_X": 500,
    "EMAIL_NAG_TEXT_X": 420,
    "FIGHT_RESULT_TEXT_X": 490,
    "HUTMANN_BECHER_X": 130,
    "HUTMANN_BECHER_Y": 130,
    "LBL_ARBEITEN_TEXT_X": 400,
    "LBL_QO_TEXT_X": 470,
    "MQ_SQUARE_X": 610,
    "MQ_SQUARE_Y": 570,
    "OPTION_X": 845,
    "OPTION_Y": 520,
    "QO_BLACK_SQUARE_X": 740,
    "QO_BLACK_SQUARE_Y": 440,
    "TSG": 477
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


# Shape indices
SHP = {
    "BLACK_CHARDESC": 22958,
    "BLACK_GILDEEHRE": 22951,
    "DISCONNECTED": 24367,
    "FIGHT_BLACK_SQUARE": 23831,
    "FUCK_BLACK_SQUARE": 82,
    "MAINQUEST": 24357,
    "OPTION_BLACK": 24245,
    "POST_BLACK_SQUARE": 23265,
    "QO_BLACK_SQUARE": 23589,
    "STALL_BLACK_SQUARE": 23343
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
