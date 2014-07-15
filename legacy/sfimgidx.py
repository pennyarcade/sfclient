#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html

    Image Ids
'''


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
