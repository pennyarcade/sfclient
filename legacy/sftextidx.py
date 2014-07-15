#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html

    Text Snippet Ids
'''


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
