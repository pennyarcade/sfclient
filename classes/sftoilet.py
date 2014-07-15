#!/usr/bin/python
# coding=utf-8

'''
    Shakes & Fidget command line client

    by Chocokiko

    Toilet Object

'''


class Toilet(object):
    '''
        handle toilet data
    '''
    def __init__(self, is_full=False, toilet_level=0, toilet_exp=0,
                 toilet_max_exp=0, item_added=-1):
        '''
            setup toilet object
        '''
        self.is_full = is_full
        self.level = toilet_level
        self.exp = toilet_exp
        self.max_ext = toilet_max_exp
        self.item_added = item_added

    def show(self):
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
                (SCR_SHOP_BG_X + 248) - actor[LBL_TOILET_AURA].text_width / 2))
            toilet_tank_adjust_event();
            if (toiletTankDest != toiletTankCurrent){
                toiletTankAdjustTimer.start();
            };
            if (item_added >= 0){
                toiletItemAddFrameEvent = function (evt:TimerEvent){
                    if (((toiletItemAddFrame >= 50) or (!(on_stage(TOILET))))):
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
                            actor[gatheredItemId].alpha =
                                (toiletItemAddFrame / 35)
                            actor[gatheredItemId].y =
                                (actor[gatheredItemId].y - 5)
                        };
                    };
                    i = 0;
                    while (i < 7) {
                        hide((TOILET_FLUSH + i));
                        i++;
                    };
                    show(TOILET_FLUSH + int(((toiletItemAddFrame / 50) * 7)))
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
        print self

    def tank_adjust_event(self):
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
        print self
