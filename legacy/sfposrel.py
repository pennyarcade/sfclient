#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Absolute and relative positions, sizes

'''


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
