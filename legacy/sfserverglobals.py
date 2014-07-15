#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html

    Image, Shape Ids
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
