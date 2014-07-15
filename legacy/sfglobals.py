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
