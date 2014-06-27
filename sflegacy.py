#!/usr/bin/python
'''
    Shakes & Fidget command line client

    by Chocokiko

    Module for obsolete legacy stuff
'''


def get_quest_bg():
    '''
        Get quest background index

        @return int

        TODO: obsolete
    '''
    action = savegame[SG['ACTION']['INDEX']]
    location = savegame[SG['QUEST']['OFFER']['LOCATION1'] + action - 1]
    return LBL['SCR']['QUEST']['BG'][str(location)]


def get_quest_title(quest_id):
    '''
        gets quest title snippet

        @param int quest_id
        @return string

        TODO: obsolete
    '''
    quest = Quest.from_sg(quest_id, savegame)
    return quest.get_title()


def get_quest_text(quest_id):
    '''
        get quest description

        @param int quest_id
        @return str

        TODO: obsolete
    '''
    quest = Quest.from_sg(quest_id, savegame)
    quest.get_text()


def get_quest_random(quest_id, random_range, random_mod):
    '''
        Get quest random number

        @param int quest_id
        @param int random_range
        @param int random_mod
        @return int

        TODO: obsolete
    '''
    quest = Quest.from_sg(quest_id, savegame)
    return quest.get_random(random_range, random_mod)


def load_configuration_file():
    '''
        configuration loader
    '''
    loader = URLLoader()
    loader2 = URLLoader()

    with loader:
        data_format = URLLoaderdata_format.TEXT
        add_event_listener(Event.COMPLETE, configuration_file_loaded)
        load(URLRequest("client_cfg.php"))

    with loader2:
        data_format = URLLoaderdata_format.TEXT
        add_event_listener(Event.COMPLETE, configuration_file_loaded)

    pending_loaders += 2
    # TODO WTF?
    pending_configuration_files = 1
    pending_configuration_files = True
