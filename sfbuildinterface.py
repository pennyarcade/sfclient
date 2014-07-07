#!/usr/bin/python
# coding=utf-8
'''
    Shakes & Fidget command line client

    by Chocokiko

    @see: (Curses Example)
            http://gnosis.cx/publish/programming/charming_python_6.html

    Module to hold monster method until refactored
'''


def build_interface():
    '''
    var i:* = 0;
    var ii:* = 0;
    var iii:* = 0;
    var attPriceLimitation:* = False;
    var iPosi:* = None;
    var yOffs:* = None;
    var dungeonBtnUpdateDelayTimer:* = None;
    var dungeonBtnHover:* = None;
    var dungeonBtnLeave:* = None;
    var dungeonBtnUpdateDelay:* = None;
    var workBtnUpdateDelayTimer:* = None;
    var workBtnHover:* = None;
    var workBtnLeave:* = None;
    var workBtnUpdateDelay:* = None;
    var tavBtnUpdateDelayTimer:* = None;
    var tavBtnHover:* = None;
    var tavBtnLeave:* = None;
    var tavBtnUpdateDelay:* = None;
    var arenaBtnUpdateDelayTimer:* = None;
    var arenaBtnHover:* = None;
    var arenaBtnLeave:* = None;
    var arenaBtnUpdateDelay:* = None;
    var HutmannLinkTimer:* = None;
    var HutmannLinkVis:* = False;
    var HutmannLinkOver:* = False;
    var HutmannRelY:* = 0;
    var HutmannAniStep:* = 0;
    var HutmannCountdown:* = 0;
    var HutmannLinkAniEvent:* = None;
    var AIRRelMoveY:* = 0;
    var AIRRelMoveYButton:* = 0;
    var AIRRelMoveYButton2:* = 0;
    var gradePassword:* = None;
    var RequestPassword:* = None;
    var CheckAGB:* = None;
    var UncheckAGB:* = None;
    var CheckFuck:* = None;
    var UncheckFuck:* = None;
    var PulseTimer:* = None;
    var PulseLevel:* = 0;
    var CloneMarker:* = None;
    var pos_x:* = 0;
    var pos_y:* = 0;
    var volk:* = None;
    var SelectRace:* = None;
    var SelectGender:* = None;
    var SelectCaste:* = None;
    var MimickInterfaceButtonHover:* = None;
    var Buh:* = False;
    var BuhHover:* = None;
    var BuhOut:* = None;
    var BubbleTimer:* = None;
    var BubbleWait:* = 0;
    var Bubbles:* = None;
    var CityAniTimer:* = None;
    var CityAniFrame:* = 0;
    var SandwichPause:* = 0;
    var ZwergFussTapp:* = 0;
    var CityAni:* = None;
    var iFrame:* = 0;
    var SchildDir:* = 0;
    var SchildTimer:* = None;
    var WacheOver:* = None;
    var WacheOut:* = None;
    var SchildFrame:* = None;
    var EselOver:* = None;
    var EselOut:* = None;
    var DealerAniTimer:* = None;
    var DealerStepTimer:* = None;
    var DealerAniStep:* = 0;
    var ShowDealerEyes:* = None;
    var HideDealerEyes:* = None;
    var DealerStep:* = None;
    var OnoTimer:* = None;
    var LastOno:* = 0;
    var ThisOno:* = 0;
    var OnoPopupTimer:* = None;
    var PopupDir:* = False;
    var ShowArenaOno:* = None;
    var HideArenaOno:* = None;
    var PopupArenaOno:* = None;
    var StepArenaOno:* = None;
    var InterfaceButtonHover:* = None;
    var ExitScreen:* = None;
    var HalleSuchClick:* = None;
    var RuhmesHalleScroll:* = None;
    var RemoveInviteWindow:* = None;
    var SendPlayerInvite:* = None;
    var PrevPlayer:* = None;
    var NextPlayer:* = None;
    var RequestAlbum:* = None;
    var PlayerGuildInviteCancel:* = None;
    var PlayerGuildInviteOK:* = None;
    var PlayerGuildInvite:* = None;
    var ZurGilde:* = None;
    var PlayerSendMessage:* = None;
    var PlayerAttack:* = None;
    var PlayerInvite:* = None;
    var BoostBtnRepeatTimer:* = None;
    var DestroyBoostBtnTimer:* = False;
    var BoostAttribute:* = None;
    var inBoostBtn:* = False;
    var BoostBtnChange:* = 0;
    var BoostBtnTimer:* = None;
    var BoostBtnTimerFunction:* = None;
    var itmTyp:* = 0;
    var itm_pic:* = 0;
    var itm_color:* = 0;
    var itm_class:* = 0;
    var InventoryItemMouseDown:* = None;
    var BackpackItemMouseDown:* = None;
    var InventoryItemMouseUp:* = None;
    var DropHandler:* = None;
    var PotionSingleClick:* = None;
    var PotionDoubleClick:* = None;
    var tower_levelLabelTimer:* = None;
    var towerBoostPriceFadeoutTimer:* = None;
    var towerBoostPriceFadeout:* = None;
    var tower_levelLabelMoveFn:* = None;
    var ShowTowerBoostPrices:* = None;
    var HideTowerBoostPrices:* = None;
    var BoostCopycat:* = None;
    var AffeBlinzeln:* = 0;
    var FidgetBlinzeln:* = 0;
    var ShakesBlinzeln:* = 0;
    var ShakesIdleStep:* = 0;
    var ShakesIdlePhase:* = 0;
    var WasIdleCount:* = 0;
    var ShopIdle:* = NaN;
    var PlayerIdle:* = False;
    var ShopAniTimer:* = None;
    var SaleRecoverTime:* = NaN;
    var ShopAniFrame:* = None;
    var ShopMouseDownEvent:* = None;
    var ShopMouseUpEvent:* = None;
    var RequestNewWarez:* = None;
    var RequestWitchScreen:* = None;
    var spellClicking:* = False;
    var CancelQuest:* = None;
    var SkipQuest:* = None;
    var Attackenemy:* = None;
    var SelectedMount:* = 0;
    var OldMount:* = 0;
    var ClickMount:* = None;
    var BuyMount:* = None;
    var crestClaI:* = 0;
    var ShowExtendedHistory:* = None;
    var HideExtendedHistory:* = None;
    var lastChatLine:* = None;
    var AdvancedChatHandler:* = None;
    var SendChatMsg:* = None;
    var nextSuggestionTimer:* = None;
    var suggestionAllowed:* = False;
    var nextSuggestionAllow:* = None;
    var GildeBtnHandler:* = None;
    var GildeGruenden:* = None;
    var HutBtnRepeatTimer:* = None;
    var DestroyHutBtnTimer:* = False;
    var HutFaceResetTimer:* = None;
    var HutFaceReset:* = None;
    var HutBtnHandler:* = None;
    var ChooseCup:* = None;
    var cursedDescr:* = None;
    var RequestToilet:* = None;
    var ShowHutmann:* = None;
    var BuyBeer:* = None;
    var ShowBeerOffer:* = None;
    var TimeBarAniTimer:* = None;
    var timeBarAni:* = NaN;
    var TimeBarAniEvent:* = None;
    var ShowQuestOffer:* = None;
    var ReturnQuest:* = None;
    var RequestQuest:* = None;
    var toiletChainTimer:* = None;
    var toiletChainFrame:* = 0;
    var toiletChainAni:* = None;
    var ToiletHandler:* = None;
    var k:* = 0;
    var monsterChecksum:* = None;
    var SkipFight:* = None;
    var CheckLM:* = None;
    var UncheckLM:* = None;
    var CheckCS:* = None;
    var UncheckCS:* = None;
    var CheckCompare:* = None;
    var UncheckCompare:* = None;
    var CheckTV:* = None;
    var UncheckTV:* = None;
    var VolumeChange:* = None;
    var Filter_Glow:* = None;
    var ChooseLanguageIcon:* = None;
    var optionMenuSelect:* = 0;
    var OptionBtnHandler:* = None;
    var RequestMainQuest:* = None;
    var AdvancedPostHandler:* = None;
    var killFieldContent:* = None;
    var fillFieldContent:* = None;
    var ShowSocial:* = function (evt:MouseEvent){
        var thisActor;
        thisActor = get_actor_id(evt.target);
        ExternalIF.call(
            "showSocial",
            param_social_buttons[(thisActor - SOCIAL)].split(":")[0]
        )
    };
    var ShowDatenschutz:* = function (){
        navigateToURLEx(new URLRequest(dataprot_url), "_blank");
    };
    var ShowAnleitung:* = function (){
        navigateToURLEx(new URLRequest(instr_url), "_blank");
    };
    var ShowImpressum:* = function (){
        navigateToURLEx(new URLRequest(imprint_url), "_blank");
    };
    var ShowForum:* = function (){
        navigateToURLEx(new URLRequest(forum_url), "_blank");
    };
    var ShowShop:* = function (){
        navigateToURLEx(new URLRequest(
            shop_url.split("<playerid>").join(
                savegame[SG['PLAYER_ID']]
            ).split("<paymentid>").join(
                savegame[SG_PAYMENT_ID]
            ).split("<player_name>").join(
                actor[INP['NAME']].getChildAt(1).text
            ).split("<face>").join(
                (char_volk + "/" + str(((char_male)
                 ? 1 : 2))) + "/") + char_class) + "/")
                + char_mouth) + "/") + char_hair) + "/")
                + char_brows) + "/") + char_eyes) + "/") +
                char_beard) + "/") + char_nose) + "/") +
                char_ears) + "/") + char_special) + "/") +
                char_special2) + "/"))), "_blank");
    };
    var navigateToURLEx:* = function (req:URLRequest, frameName:str){
        var req:* = req;
        var frameName:* = frameName;
        try {
            ExternalIF.call("openUrl", req.url);
        } catch(e:Error) {
            navigate_to_url(req, frameName);
        };
    };
    dungeonBtnHover = function (evt:MouseEvent){
        dungeonBtnUpdateDelay();
        dungeonBtnUpdateDelayTimer.start();
    };
    dungeonBtnLeave = function (evt:MouseEvent=None){
        dungeonBtnUpdateDelayTimer.stop();
        set_btn_text(IF_WELTKARTE, texts[TXT_WELTKARTE]);
    };
    dungeonBtnUpdateDelay = function (evt:TimerEvent=None){
        if (waiting_for(savegame[SG_MQ_REROLL_TIME])){
            set_btn_text(
                IF_WELTKARTE,
                waiting_time(savegame[SG_MQ_REROLL_TIME])
            )
        } else {
            dungeonBtnLeave();
        };
    };
    workBtnHover = function (evt:MouseEvent){
        workBtnUpdateDelay();
        workBtnUpdateDelayTimer.start();
    };
    workBtnLeave = function (evt:MouseEvent=None){
        workBtnUpdateDelayTimer.stop();
        set_btn_text(IF_ARBEITEN, texts[TXT_ARBEITEN]);
    };
    workBtnUpdateDelay = function (evt:TimerEvent=None){
        if (((waiting_for(savegame[SG_ACTION_ENDTIME]))
            and ((savegame[SG_ACTION_STATUS] == 1)))){
            set_btn_text(
                IF_ARBEITEN,
                waiting_time(savegame[SG_ACTION_ENDTIME])
            );
        } else {
            workBtnLeave();
        };
    };
    tavBtnHover = function (evt:MouseEvent){
        tavBtnUpdateDelay();
        tavBtnUpdateDelayTimer.start();
    };
    tavBtnLeave = function (evt:MouseEvent=None){
        tavBtnUpdateDelayTimer.stop();
        set_btn_text(IF_TAVERNE, texts[TXT_TAVERNE]);
    };
    tavBtnUpdateDelay = function (evt:TimerEvent=None){
        if (((waiting_for(savegame[SG_ACTION_ENDTIME]))
            and ((savegame[SG_ACTION_STATUS] == 2)))){
            set_btn_text(
                IF_TAVERNE,
                waiting_time(savegame[SG_ACTION_ENDTIME])
            );
        } else {
            tavBtnLeave();
        };
    };
    arenaBtnHover = function (evt:MouseEvent){
        arenaBtnUpdateDelay();
        arenaBtnUpdateDelayTimer.start();
    };
    arenaBtnLeave = function (evt:MouseEvent=None){
        arenaBtnUpdateDelayTimer.stop();
        set_btn_text(IF_ARENA, texts[TXT_ARENA]);
    };
    arenaBtnUpdateDelay = function (evt:TimerEvent=None){
        if (waiting_for(savegame[SG_PVP_REROLL_TIME])){
            set_btn_text(
                IF_ARENA,
                waiting_time(savegame[SG_PVP_REROLL_TIME])
            );
        } else {
            arenaBtnLeave();
        };
    };
    var TaverneBtnIn:* = function (evt:Event){
        actor[IF_TOILET].visible = (
            (!((savegame[SG_TOILET] == 0)))
            and (!(on_stage(CA_TOILET_BOWL))));
        actor[IF_HUTMANN].visible = !(on_stage(HUTMANN_BG));
        if (
            ((!((int(savegame[SG_ACTION_STATUS]) == 0)))
            and (!(pulse_taverne)))
        ){
            HutmannCountdown = 20;
            HutmannLinkOver = True;
        };
    };
    var TaverneBtnOut:* = function (evt:Event){
        HutmannCountdown = 1;
        HutmannLinkOver = False;
    };
    HutmannLinkAniEvent = function (evt:Event){
        var i:* = 0;
        var evt:* = evt;
        if (HutmannCountdown > 0){
            HutmannCountdown--;
            if (HutmannCountdown == 0){
                HutmannLinkVis = HutmannLinkOver;
            };
        };
        if (HutmannLinkVis){
            if (HutmannRelY > -(actor[IF_HUTMANN1].height)){
                HutmannRelY = (HutmannRelY - 10);
            } else {
                if (HutmannAniStep < 100){
                    HutmannAniStep++;
                };
                Switch (HutmannAniStep){
                    if case(2:
                    if case(8:
                    if case(14:
                    if case(20:
                    if case(26:
                        HutmannFrame = 1;
                        break;
                    if case(4:
                    if case(10:
                    if case(16:
                    if case(22:
                    if case(28:
                        HutmannFrame = 0;
                        break;
                };
            };
        } else {
            if (HutmannRelY < 0){
                HutmannRelY = (HutmannRelY + 10);
            };
            HutmannAniStep = 0;
            HutmannFrame = 0;
        };
        i = 0;
        while (i < 2) {
            var _local3 = actor[(IF_HUTMANN1 + i)];
            with (_local3) {
                visible = (i == HutmannFrame);
            };
            i = (i + 1);
        };
        _local3 = actor[IF_HUTMANN];
        with (_local3) {
            y = (IF_HUTLINK_Y + HutmannRelY);
        };
        _local3 = actor[IF_TOILET];
        with (_local3) {
            y = ((IF_HUTLINK_Y + HutmannRelY) + 40);
        };
    };
    var DefiniereInterfaceButton:* = function (
        actor_id, txtID
        ){
        var dragonID:* = 0;
        var InterfaceButtonDown:* = None;
        var InterfaceButtonUp:* = None;
        var actor_id:* = actor_id;
        var txtID:* = txtID;
        InterfaceButtonDown = function (evt:MouseEvent):
            var x;
            var y;
            var i;
            i = dragonID;
            x = actor[i].x;
            y = actor[i].y;
            removeChild(actor[i]);
            delete actor[i];
            actor[i] = new interface_dragon5_png();
            actor[i].x = x;
            actor[i].y = y;
            addChild(actor[i]);
        };
        InterfaceButtonUp = function (evt:MouseEvent):
            var x;
            var y;
            var i;
            var d;
            i = dragonID;
            if (actor[i]){
                x = actor[i].x;
                y = actor[i].y;
                removeChild(actor[i]);
                delete actor[i];
                d = actorBitmap[i];
                Switch (d){
                    if case(0:
                        actor[i] = new interface_dragon1_png();
                        break;
                    if case(1:
                        actor[i] = new interface_dragon2_png();
                        break;
                    if case(2:
                        actor[i] = new interface_dragon3_png();
                        break;
                    if case(3:
                        actor[i] = new interface_dragon4_png();
                        break;
                    if case(4:
                    if case(5:
                        actor[i] = new interface_dragon6_png();
                        break;
                };
                actor[i].x = x;
                actor[i].y = y;
                addChild(actor[i]);
            };
            remove(CITY_OVERLAYS);
            HideArenaOno();
            WacheOut();
            if ((((
                (on_stage(SCR_CITY_BACKG_NIGHT))
                or (on_stage(SCR_CITY_BACKG_DAWN))))
                or (on_stage(SCR_CITY_BACKG_DAY)))
            ){
                add(CITY_ESEL1);
                add(CITY_CA_OVL);
            };
            if (on_stage(CA_SCR_ARBEITEN_BLOCKCITY)){
                if (on_stage(LBL_SCR_ARBEITEN_TIME)){
                    add(SCREEN_ARBEITEN_WAIT);
                } else {
                    if (on_stage(SCR_ARBEITEN_OK)){
                        add(SCREEN_ARBEITEN);
                    } else {
                        add(SCREEN_ARBEITEN_SUCCESS);
                    };
                };
            };
            if (on_stage(CA_SCR_INVITE_BLOCKCITY)){
                add(SCREEN_INVITE);
            };
            if (on_stage(BLACK_SQUARE)){
                add(BLACK_SQUARE);
            };
        };
        define_btn(
            actor_id,
            texts[txtID],
            interface_btn_handler,
            btn_classInterface,
            IF_X,
            ((IF_Y + (IF_1 * iPosi++)) + yOffs)
        );
        define_from_class(
            ((IF_DRAGON_1 + iPosi) - 1),
            interface_dragon1_png,
            (actor[actor_id].x + DRAGON_X),
            (actor[actor_id].y + DRAGON_Y)
        );
        dragonID = ((IF_DRAGON_1 + iPosi) - 1);
        actor[actor_id].add_event_listener(
            MouseEvent.MOUSE_DOWN,
            InterfaceButtonDown
        );
        actor[actor_id].add_event_listener(
            MouseEvent.MOUSE_UP,
            InterfaceButtonUp
        );
        actor[actor_id].add_event_listener(
            MouseEvent.MOUSE_OUT,
            InterfaceButtonUp
        );
        actor[actor_id].add_event_listener(
            MouseEvent.MOUSE_OVER,
            InterfaceButtonHover
        );
        MakePersistent(
            ((IF_DRAGON_1 + iPosi) - 1),
            actor_id
        );
    };
    gradePassword = function (
        evt:Event=None,
        pwd_str:String=""
    ){
        var pwd:String;
        var badWords:Array;
        var newPwd:String;
        var lastChar:String;
        var pwdScore;
        var i;
        var ii;
        var cmp:String;
        var badSequences:*;
        var hasBadSequence:Boolean;
        var hasNumerals:Boolean;
        var hasUpperCase:Boolean;
        var hasLowerCase:Boolean;
        var hasSpecial:Boolean;
        pwd = pwd_str;
        badWords = list();
        if (texts[TXT_BAD_PASSWORDS]){
            badWords = texts[TXT_BAD_PASSWORDS].split(" ");
        };
        if (len(actor[INP['NAME']].getChildAt(1).text) >= 3){
            badWords.append(actor[INP['NAME']].getChildAt(1).text);
        };
        if (evt){
            if (get_actor_id(evt.target.parent) == INP['PASSWORD']){
                pwd = actor[INP['PASSWORD']].getChildAt(1).text;
                hide(PASSWORD_SMILEY_SAD);
                hide(PASSWORD_SMILEY_NEUTRAL);
                hide(PASSWORD_SMILEY_HAPPY);
            } else {
                if (optionMenuSelect == 3){
                    hide(CHANGE_PASSWORD_SMILEY_SAD);
                    hide(CHANGE_PASSWORD_SMILEY_NEUTRAL);
                    hide(CHANGE_PASSWORD_SMILEY_HAPPY);
                    if (
                        actor[INP_OPTION_FIELD2].getChildAt(
                            1
                        ).text == actor[INP_OPTION_FIELD3].getChildAt(
                            1
                        ).text
                    ){
                        pwd = actor[INP_OPTION_FIELD2].getChildAt(1).text;
                    } else {
                        return;
                    };
                } else {
                    return;
                };
            };
        };
        newPwd = "";
        lastChar = "";
        pwdScore = 0;
        cmp = "";
        badSequences = [
            "01234567890",
            "abcdefghijklmnopqrstuvwxyz",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            qwertzuiopasdfghjklyxcvbnm",
            "qwertyuiopasdfghjklzxcvbnm",
            "09876543210",
            "mnbvcxylkjhgfdsapoiuztrewq",
            "mnbvcxzlkjhgfdsapoiuytrewq"
        ];
        i = 0;
        while (i < len(badWords)) {
            if (pwd.lower().find(badWords[i].lower()) != -1){
                pwdScore = (pwdScore - 5);
            };
            i++;
        };
        i = 0;
        while (i < len(pwd)) {
            if (pwd[i: 1] != lastChar){
                newPwd = (newPwd + pwd.[i: 1]);
            };
            lastChar = pwd[i, 1];
            i++;
        };
        pwd = newPwd;
        newPwd = "";
        hasBadSequence = False;
        i = 0;
        while (i < len(pwd)) {
            if (i >= 2){
                cmp = pwd[(i - 2): 3];
            } else {
                cmp = "";
                newPwd = (newPwd + pwd[i: 1]);
            };
            hasBadSequence = False;
            ii = 0;
            while (ii < len(badSequences)) {
                if (badSequences[ii].find(cmp) != -1){
                    hasBadSequence = True;
                    break;
                };
                ii++;
            };
            if (!hasBadSequence){
                newPwd = (newPwd + pwd[i: 1]);
            };
            i++;
        };
        pwd = newPwd;
        i = 3;
        while (i < len(pwd)) {
            ii = 0;
            while (ii < (len(pwd) - i)) {
                cmp = pwd[ii: i];
                if (pwd.last_indexOf(cmp) != ii){
                    pwdScore--;
                };
                ii++;
            };
            i++;
        };
        if (len(pwd) >= 12){
            pwdScore = (pwdScore + 2);
        } else {
            if (len(pwd) >= 8){
                pwdScore = (pwdScore + 1);
            } else {
                if (len(pwd) >= 5){
                    pwdScore = (pwdScore + 0);
                } else {
                    pwdScore = (pwdScore - 10);
                };
            };
        };
        hasNumerals = False;
        hasUpperCase = False;
        hasLowerCase = False;
        hasSpecial = False;
        i = 0;
        while (i < len(pwd)) {
            if (pwd[i: 1] == str(int(pwd[i: 1]))){
                hasNumerals = True;
            } else {
                if (pwd[i: 1] != pwd.[i: 1].lower()){
                    hasUpperCase = True;
                } else {
                    if (pwd[i: 1] != pwd[i: 1].upper()){
                        hasLowerCase = True;
                    } else {
                        hasSpecial = True;
                    };
                };
            };
            i++;
        };
        if (hasNumerals){
            pwdScore = (pwdScore + 1);
        };
        if (hasUpperCase){
            pwdScore = (pwdScore + 1);
        };
        if (hasLowerCase){
            pwdScore = (pwdScore + 1);
        };
        if (hasSpecial){
            pwdScore = (pwdScore + 1);
        };
        if (evt){
            if (get_actor_id(evt.target.parent) == INP['PASSWORD']){
                if (pwdScore >= 3){
                    show(PASSWORD_SMILEY_HAPPY);
                } else {
                    if (pwdScore >= 2){
                        show(PASSWORD_SMILEY_NEUTRAL);
                    } else {
                        show(PASSWORD_SMILEY_SAD);
                    };
                };
            } else {
                if (pwdScore >= 3){
                    show(CHANGE_PASSWORD_SMILEY_HAPPY);
                } else {
                    if (pwdScore >= 2){
                        show(CHANGE_PASSWORD_SMILEY_NEUTRAL);
                    } else {
                        show(CHANGE_PASSWORD_SMILEY_SAD);
                    };
                };
            };
        } else {
            if (pwdScore >= 3){
                chat_line("Your password is secure.");
            } else {
                if (pwdScore >= 2){
                    chat_line("Your password is ok, could be better.");
                } else {
                    chat_line("Your password is insecure.");
                };
            };
        };
    };
    var DoGotoSignup:* = function (evt:Event){
        if (buffed_mode){
            navigate_to_url(new URLRequest(buffed_link_url));
        } else {
            show_build_character_screen(evt);
        };
    };
    var ShowAGB:* = function (evt:Event=None){
        navigate_to_url(new URLRequest(legal_url), "_blank");
    };
    var ShowForgotPasswordScreen:* = function (evt:Event=None):
        remove_all();
        actor[LBL_WINDOW_TITLE].text = texts[TXT_TITLE_FORGOT_PASSWORD];
        actor[LBL_WINDOW_TITLE].x = (
            (IF_WIN_X + IF_WIN_WELCOME_X) - int(
                (actor[LBL_WINDOW_TITLE].text_width / 2)
            )
        );
        actor[INP['NAME']].add_event_listener(
            KeyboardEvent.KEY_DOWN,
            RequestPassword
        );
        actor[INP['EMAIL']].add_event_listener(
            KeyboardEvent.KEY_DOWN,
            RequestPassword
        );
        log_on_rtl();
        add(WINDOW_FORGOT_PASSWORD);
    };
    RequestPassword = function (evt:Event):
        if ((evt is KeyboardEvent)){
            if (
                ((((!((KeyboardEvent(evt).keyCode == 13)))
                and (!((KeyboardEvent(evt).keyCode == 10)))))
                and (!((KeyboardEvent(evt).keyCode == 16777230))))
            ){
                return;
            };
        };
        send_action(
            ACT_FORGOT_PASSWORD,
            actor[INP['NAME']].getChildAt(1).text,
            actor[INP['EMAIL']].getChildAt(1).text
        );
    };
    CheckAGB = function (evt:MouseEvent):
        add(CB['AGB_CHECKED']);
    };
    UncheckAGB = function (evt:MouseEvent):
        remove(CB['AGB_CHECKED']);
    };
    CheckFuck = function (evt:MouseEvent):
        add(CB_FUCK_CHECKED);
    };
    UncheckFuck = function (evt:MouseEvent):
        remove(CB_FUCK_CHECKED);
    };
    var PulseEvent:* = function (evt:Event){
        var evt:* = evt;
        var ButtonPulse:* = function (doPulse:Boolean, btnID){
            var doPulse:* = doPulse;
            var btnID:* = btnID;
            var LabelPulse:* = function (obj:DisplayObjectContainer){
                var obj:* = obj;
                var _local3 = obj.getChildAt(1);
                with (_local3) {
                    alpha = ((doPulse)
                        ? ((math.sin((((PulseLevel / 200) * 2)
                            * math.pi)) * 0.4) + 0.8)
                        : 1
                    );
                };
            };
            PulseLevel = (PulseLevel + 1);
            if (PulseLevel > 200){
                PulseLevel = 0;
            };
            var _local4 = actor[btnID];
            with (_local4) {
                LabelPulse(upState);
                LabelPulse(overState);
                LabelPulse(downState);
                LabelPulse(hitTestState);
            };
        };
        if (len(savegame) == 0){
            return;
        };
        if (int(savegame[SG_ACTION_STATUS]) == 1){
            if (!waiting_for(savegame[SG_ACTION_ENDTIME])){
                pulse_arbeiten = True;
            };
        };
        if (int(savegame[SG_ACTION_STATUS]) == 2){
            if (!waiting_for(savegame[SG_ACTION_ENDTIME])){
                pulse_taverne = True;
            };
        };
        if (
            ((((on_stage(TAVERNE_BG))
            or (on_stage(FIGHT_BOX1))))
            or (on_stage(QUESTBAR_BG)))
        ){
            pulse_taverne = False;
        };
        if (on_stage(LBL_SCR_ARBEITEN_TEXT)){
            pulse_arbeiten = False;
        };
        if (on_stage(GILDEN_BG)){
            pulse_gilde = False;
            pulse_gilde_on_history = False;
        };
        if (on_stage(SCR_DEALER_BG)){
            pulse_dealer = False;
        };
        if (on_stage(POST_LIST)){
            pulse_post = False;
        };
        if (
            ((((on_stage(SCR_CHAR_BG_RIGHT))
            or (on_stage(SCR_SHAKES_BG))))
            or (on_stage(SCR_FIDGET_BG)))
        ){
            pulse_char = False;
        };
        if (
            ((((((((((pulse_taverne)
            or (pulse_arbeiten)))
            or (pulse_gilde)))
            or (pulse_post)))
            or (pulse_char)))
            or (pulse_dealer))
        ){
            PulseTimer.delay = 20;
        } else {
            PulseTimer.delay = 500;
        };
        ButtonPulse(pulse_taverne, IF_TAVERNE);
        ButtonPulse(pulse_arbeiten, IF_ARBEITEN);
        ButtonPulse(pulse_gilde, IF_GILDEN);
        ButtonPulse(pulse_post, IF_POST);
        ButtonPulse(pulse_char, IF_CHARAKTER);
        ButtonPulse(pulse_dealer, IF_PILZDEALER);
    };
    CloneMarker = function ():
        var i;
        SetCnt(M_ACT, VOLK_MARKER);
        SetCnt(F_ACT, VOLK_MARKER);
        SetCnt(KASTE_1_ACT, VOLK_MARKER);
        SetCnt(KASTE_2_ACT, VOLK_MARKER);
        SetCnt(KASTE_3_ACT, VOLK_MARKER);
        i = 0;
        while (i <= 7) {
            SetCnt((VOLK_1_M_ACT + i), VOLK_MARKER);
            SetCnt((VOLK_1_F_ACT + i), VOLK_MARKER);
            i++;
        };
    };
    SelectRace = function (evt:MouseEvent):
        var actor_id;
        actor_id = get_actor_id(evt.target);
        if (
            (((actor_id >= VOLK_1_M_IDLE))
            and ((actor_id <= VOLK_8_M_IDLE)))
        ){
            char_volk = ((actor_id - VOLK_1_M_IDLE) + 1);
            char_male = True;
        };
        if (
            (((actor_id >= VOLK_1_F_IDLE))
            and ((actor_id <= VOLK_8_F_IDLE)))
        ){
            char_volk = ((actor_id - VOLK_1_F_IDLE) + 1);
            char_male = False;
        };
        randomize_char_image();
        if (on_stage(POPUP_INFO)){
            add(POPUP_INFO);
        };
    };
    SelectGender = function (evt:MouseEvent):
        var actor_id;
        actor_id = get_actor_id(evt.target);
        if (actor_id == M_IDLE){
            char_male = True;
        };
        if (actor_id == F_IDLE){
            char_male = False;
        };
        randomize_char_image();
        if (on_stage(POPUP_INFO)){
            add(POPUP_INFO);
        };
    };
    SelectCaste = function (evt:MouseEvent):
        var actor_id;
        actor_id = get_actor_id(evt.target);
        KlasseGewählt = True;
        if (actor_id == KASTE_1_IDLE){
            char_class = 1;
        };
        if (actor_id == KASTE_2_IDLE){
            char_class = 2;
        };
        if (actor_id == KASTE_3_IDLE){
            char_class = 3;
        };
        load_character_image();
        if (on_stage(POPUP_INFO)){
            add(POPUP_INFO);
        };
    };
    def AddMimickInterfaceButtonHoverHandler(actor_id){
        actor[actor_id].add_event_listener(
            MouseEvent.MOUSE_OVER,
            MimickInterfaceButtonHover
        );
    };
    MimickInterfaceButtonHover = function (evt:MouseEvent):
        var tmpContainer:* = None;
        var EndMimickInterfaceButtonHover:* = None;
        var evt:* = evt;
        var MimickHover:* = function (actor_id){
            tmpContainer = new MovieClip();
            tmpContainer.x = actor[actor_id].x;
            tmpContainer.y = actor[actor_id].y;
            tmpContainer.addChild(actor[actor_id].overState);
            addChild(tmpContainer);
        };
        EndMimickInterfaceButtonHover = function (evt:MouseEvent):
            if (get_child_by_name(tmpContainer.name)){
                removeChild(tmpContainer);
            };
        };
        evt.target.add_event_listener(
            MouseEvent.MOUSE_OUT,
            EndMimickInterfaceButtonHover
        );
        Switch (get_actor_id(evt.target)){
            if case(CA_CITY_SHAKES:
                MimickHover(IF_SCHMIEDE);
                break;
            if case(CA_CITY_ZAUBERLADEN:
                MimickHover(IF_ZAUBERLADEN);
                break;
            if case(CA_CITY_RUHMESHALLE:
                MimickHover(IF_EHRENHALLE);
                break;
            if case(CA_CITY_ARENA:
                MimickHover(IF_ARENA);
                break;
            if case(CA_CITY_DEALER:
                MimickHover(IF_PILZDEALER);
                break;
            if case(CA_CITY_ESEL:
                MimickHover(IF_STALL);
                break;
            if case(CA_CITY_TAVERNE:
                MimickHover(IF_TAVERNE);
                break;
            if case(CA_CITY_POST:
                MimickHover(IF_POST);
                break;
            if case(CA_CITY_WACHE:
                MimickHover(IF_ARBEITEN);
                break;
        };
    };
    BuhHover = function ():
        Buh = True;
    };
    BuhOut = function ():
        Buh = False;
    };
    Bubbles = function (evt:Event):
        var evt:* = evt;
        var BubbleFade:* = function (inOut:Boolean, bubbleID):
            if (inOut){
                if (
                    ((((!(on_stage(bubbleID)))
                    and (!(on_stage(CA_SCR_ARBEITEN_BLOCKCITY)))))
                    and (!(on_stage(CA_SCR_INVITE_BLOCKCITY))))
                ){
                    add(bubbleID);
                    add(CITY_CA_OVL);
                    actor[bubbleID].alpha = 0;
                    BubbleWait = 30;
                } else {
                    if (actor[bubbleID].alpha < 1){
                        if (
                            ((on_stage(CA_SCR_ARBEITEN_BLOCKCITY))
                            or (on_stage(CA_SCR_INVITE_BLOCKCITY)))
                        ){
                            remove(bubbleID);
                            actor[bubbleID].alpha = 0;
                            BubbleWait = 0;
                        } else {
                            if (BubbleWait > 0){
                                BubbleWait--;
                            } else {
                                add(bubbleID);
                                add(CITY_CA_OVL);
                                if (light_mode){
                                    actor[bubbleID].alpha = 1;
                                } else {
                                    actor[bubbleID].alpha = (
                                        actor[bubbleID].alpha + 0.1
                                    );
                                };
                            };
                        };
                    } else {
                        if (
                            ((on_stage(CA_SCR_ARBEITEN_BLOCKCITY))
                            or (on_stage(CA_SCR_INVITE_BLOCKCITY)))
                        ){
                            remove(bubbleID);
                        };
                    };
                };
            } else {
                if (on_stage(bubbleID)){
                    if (
                        ((on_stage(CA_SCR_ARBEITEN_BLOCKCITY))
                        or (on_stage(CA_SCR_INVITE_BLOCKCITY)))
                    ){
                        remove(bubbleID);
                        actor[bubbleID].alpha = 0;
                        BubbleWait = 0;
                    };
                    if (actor[bubbleID].alpha > 0){
                        if (light_mode){
                            actor[bubbleID].alpha = 0;
                        } else {
                            actor[bubbleID].alpha = (
                                actor[bubbleID].alpha - 0.1
                            );
                        };
                        add(bubbleID);
                        add(CITY_CA_OVL);
                        BubbleWait = 30;
                    };
                    if (actor[bubbleID].alpha == 0){
                        remove(bubbleID);
                    };
                };
            };
        };
        if (
            ((((on_stage(SCR_CITY_MAIN_DAWN))
            or (on_stage(SCR_CITY_MAIN_DAY))))
            or (on_stage(SCR_CITY_MAIN_NIGHT)))
        ){
            BubbleTimer.delay = 20;
        } else {
            BubbleTimer.delay = 500;
        };
        BubbleFade(Buh, BUBBLE_STATUE);
        BubbleFade(on_stage(CITY_ARENA), BUBBLE_ARENA);
        BubbleFade(on_stage(CITY_ESEL2), BUBBLE_ESEL);
        BubbleFade(on_stage(CITY_TAVERNE), BUBBLE_TAVERNE);
        BubbleFade(on_stage(CITY_RUHMESHALLE), BUBBLE_RUHMESHALLE);
        BubbleFade(on_stage(CITY_DEALER), BUBBLE_DEALER);
        BubbleFade(on_stage(CITY_POST), BUBBLE_POST);
        BubbleFade(
            ((((((on_stage(CITY_SCHILD1))
            or (on_stage(CITY_SCHILD2))))
            or (on_stage(CITY_SCHILD3))))
            or (on_stage(CITY_SCHILD4))),
            BUBBLE_WACHE
        );
        BubbleFade(on_stage(CITY_SHAKES), BUBBLE_SHAKES);
        BubbleFade(on_stage(CITY_ZAUBERLADEN), BUBBLE_ZAUBERLADEN);
    };
    CityAni = function (evt:Event):
        if (!light_mode){
            CityAniFrame++;
            if (
                (((CityAniFrame == 5))
                and (get_child_by_name(actor[CITY_ELF1].name)))
            ){
                remove(CITY_ELF1);
                add(CITY_ELF2);
                if (on_stage(BUBBLE_POST)){
                    add(BUBBLE_POST);
                };
                add(CITY_CA_OVL);
            } else {
                if (get_child_by_name(actor[CITY_ELF2].name)){
                    remove(CITY_ELF2);
                    add(CITY_ELF1);
                    if (on_stage(BUBBLE_POST)){
                        add(BUBBLE_POST);
                    };
                    add(CITY_CA_OVL);
                };
            };
            if (
                (((CityAniFrame == 3))
                and ((int((random.random() * 2)) == 0)))
            ){
                if (get_child_by_name(actor[CITY_ORK1].name)){
                    remove(CITY_ORK1);
                    add(CITY_ORK2);
                    define_bunch(CITY_ORK, CITY_ORK2);
                    add(CITY_CA_OVL);
                    if (on_stage(LBL['ERROR'])){
                        add(LBL['ERROR']);
                    };
                } else {
                    if (get_child_by_name(actor[CITY_ORK2].name)){
                        remove(CITY_ORK2);
                        add(CITY_ORK1);
                        define_bunch(CITY_ORK, CITY_ORK1);
                        add(CITY_CA_OVL);
                        if (on_stage(LBL['ERROR'])){
                            add(LBL['ERROR']);
                        };
                    };
                };
            };
            if (
                (((((CityAniFrame == 2))
                and ((int((random.random() * 2)) == 0))))
                and (get_child_by_name(actor[CITY_ZWERG1].name)))
            ){
                remove(CITY_ZWERG1);
                add(CITY_ZWERG2);
                define_bunch(CITY_ZWERG, CITY_ZWERG2);
                add(CITY_CA_OVL);
            } else {
                if (
                    (((CityAniFrame == 3))
                    and (on_stage(CITY_ZWERG2)))
                ){
                    remove(CITY_ZWERG2);
                    add(CITY_ZWERG1);
                    define_bunch(CITY_ZWERG, CITY_ZWERG1);
                    add(CITY_CA_OVL);
                };
            };
            if (SandwichPause > 0){
                SandwichPause--;
            } else {
                if (
                    ((((CityAniFrame % 2) == 0))
                    and (get_child_by_name(actor[CITY_SANDWICH1].name)))
                ){
                    remove(CITY_SANDWICH1);
                    add(CITY_SANDWICH2);
                    if (on_stage(LBL['ERROR'])){
                        add(LBL['ERROR']);
                    };
                };
                if (
                    ((!(((CityAniFrame % 2) == 0)))
                    and (get_child_by_name(actor[CITY_SANDWICH2].name)))
                ){
                    remove(CITY_SANDWICH2);
                    add(CITY_SANDWICH1);
                    if (on_stage(LBL['ERROR'])){
                        add(LBL['ERROR']);
                    };
                    if (int((random.random() * 8)) == 0){
                        SandwichPause = 4;
                    };
                };
            };
            if (ZwergFussTapp > 0){
                if (
                    ((on_stage(CITY_MAGIER1))
                    or (on_stage(CITY_MAGIER2)))
                ){
                    if ((ZwergFussTapp % 2) == 0){
                        remove(CITY_MAGIER1);
                        add(CITY_MAGIER2);
                        if (on_stage(BUBBLE_WACHE)){
                            add(BUBBLE_WACHE);
                        };
                        if (on_stage(LBL['ERROR'])){
                            add(LBL['ERROR']);
                        };
                        add(CITY_CA_OVL);
                    } else {
                        remove(CITY_MAGIER2);
                        add(CITY_MAGIER1);
                        if (on_stage(BUBBLE_WACHE)){
                            add(BUBBLE_WACHE);
                        };
                        if (on_stage(LBL['ERROR'])){
                            add(LBL['ERROR']);
                        };
                        add(CITY_CA_OVL);
                    };
                    ZwergFussTapp--;
                };
            } else {
                if (
                    ((on_stage(CITY_MAGIER1))
                    and ((int((random.random() * 15)) == 0)))
                ){
                    ZwergFussTapp = 6;
                };
            };
        };
        if (CityAniFrame >= 10){
            CityAniFrame = 0;
        };
        if (on_stage(CA_SCR_ARBEITEN_BLOCKCITY)){
            if (on_stage(LBL_SCR_ARBEITEN_TIME)){
                add(SCREEN_ARBEITEN_WAIT);
            } else {
                if (on_stage(SCR_ARBEITEN_OK)){
                    add(SCREEN_ARBEITEN);
                } else {
                    add(SCREEN_ARBEITEN_SUCCESS);
                };
            };
        };
        if (on_stage(CA_SCR_INVITE_BLOCKCITY)){
            add(SCREEN_INVITE);
        };
    };
    WacheOver = function ():
        SchildTimer.add_event_listener(TimerEvent.TIMER, SchildFrame);
        SchildTimer.start();
        SchildDir = 1;
    };
    WacheOut = function ():
        SchildTimer.add_event_listener(TimerEvent.TIMER, SchildFrame);
        SchildTimer.start();
        SchildDir = -1;
    };
    SchildFrame = function (evt:Event):
        if (
            ((((!(((on_stage(CITY_WACHE_DAY))
            or (on_stage(CITY_WACHE_NIGHT)))))
            or (on_stage(CA_SCR_ARBEITEN_BLOCKCITY))))
            or (on_stage(CA_SCR_INVITE_BLOCKCITY)))
        ){
            SchildTimer.stop();
            SchildTimer.remove_event_listener(
                TimerEvent.TIMER, SchildFrame
            );
            return;
        };
        remove(
            CITY_SCHILD1,
            CITY_SCHILD2,
            CITY_SCHILD3,
            CITY_SCHILD4
        );
        if (iFrame >= 0){
            add((CITY_SCHILD1 + iFrame));
        };
        add(CA_CITY_WACHE);
        if ((((iFrame < 0)) and ((SchildDir < 0)))){
            iFrame = -1;
            SchildTimer.stop();
            SchildTimer.remove_event_listener(TimerEvent.TIMER,
                                              SchildFrame)
            return;
        };
        if ((((iFrame >= 3)) and ((SchildDir > 0)))){
            iFrame = 3;
            SchildTimer.stop();
            SchildTimer.remove_event_listener(
                TimerEvent.TIMER, SchildFrame
            );
            return;
        };
        iFrame = (iFrame + SchildDir);
    };
    EselOver = function ():
        remove(CITY_ESEL1);
    };
    EselOut = function ():
        if (
            ((on_stage(STALL_BG_GUT))
            or (on_stage(STALL_BG_BOESE)))
        ){
            return;
        };
        add(CITY_ESEL1);
        add(CITY_CA_OVL);
    };
    ShowDealerEyes = function ():
        if (
            ((((on_stage(SCR_CITY_BACKG_NIGHT))
            or (on_stage(SCR_CITY_BACKG_DAWN))))
            or (on_stage(SCR_CITY_BACKG_DAY)))
        ){
            add(CITY_DEALER_ANI5);
            add(CA_CITY_DEALER);
            if (on_stage(CA_SCR_ARBEITEN_BLOCKCITY)){
                if (on_stage(LBL_SCR_ARBEITEN_TIME)){
                    add(SCREEN_ARBEITEN_WAIT);
                } else {
                    if (on_stage(SCR_ARBEITEN_OK)){
                        add(SCREEN_ARBEITEN);
                    } else {
                        add(SCREEN_ARBEITEN_SUCCESS);
                    };
                };
            };
            if (on_stage(CA_SCR_INVITE_BLOCKCITY)){
                add(SCREEN_INVITE);
            };
        };
    };
    HideDealerEyes = function ():
        DealerStepTimer.stop();
        DealerStepTimer.remove_event_listener(TimerEvent.TIMER, DealerStep)
    };
    var DealerAni:* = function (evt:Event):
        if (
            ((((on_stage(SCR_CITY_BACKG_NIGHT))
            or (on_stage(SCR_CITY_BACKG_DAWN))))
            or (on_stage(SCR_CITY_BACKG_DAY)))
        ){
            if (!get_child_by_name(actor[CITY_DEALER].name)){
                DealerStepTimer.add_event_listener(
                    TimerEvent.TIMER, DealerStep
                );
                if (int((random.random() * 5)) == 0){
                    DealerAniStep = 5;
                } else {
                    DealerAniStep = 1;
                };
                DealerStepTimer.start();
            };
        } else {
            DealerStepTimer.stop();
            DealerStepTimer.remove_event_listener(
                TimerEvent.TIMER, DealerStep
            );
        };
    };
    DealerStep = function (evt:Event):
        if (
            ((((on_stage(SCR_CITY_BACKG_NIGHT))
            or (on_stage(SCR_CITY_BACKG_DAWN))))
            or (on_stage(SCR_CITY_BACKG_DAY)))
        ){
            Switch (DealerAniStep){
                if case(1:
                    add(CITY_DEALER_ANI2);
                    break;
                if case(2:
                    add(CITY_DEALER_ANI1);
                    break;
                if case(3:
                    add(CITY_DEALER_ANI2);
                    break;
                if case(4:
                    add(CITY_DEALER_ANI5);
                    DealerAniStep = 0;
                    break;
                if case(5:
                if case(6:
                if case(7:
                    add(CITY_DEALER_ANI3);
                    break;
                if case(8:
                    add(CITY_DEALER_ANI5);
                    break;
                if case(9:
                if case(10:
                if case(11:
                    add(CITY_DEALER_ANI4);
                    break;
                if case(12:
                    add(CITY_DEALER_ANI5);
                    DealerAniStep = 0;
                    break;
            };
            add(CA_CITY_DEALER);
            if (on_stage(CA_SCR_ARBEITEN_BLOCKCITY)){
                if (on_stage(LBL_SCR_ARBEITEN_TIME)){
                    add(SCREEN_ARBEITEN_WAIT);
                } else {
                    if (on_stage(SCR_ARBEITEN_OK)){
                        add(SCREEN_ARBEITEN);
                    } else {
                        add(SCREEN_ARBEITEN_SUCCESS);
                    };
                };
            };
            if (on_stage(CA_SCR_INVITE_BLOCKCITY)){
                add(SCREEN_INVITE);
            };
            if (DealerAniStep == 0){
                DealerStepTimer.stop();
                DealerStepTimer.remove_event_listener(
                    TimerEvent.TIMER, DealerStep
                );
                return;
            };
            DealerAniStep++;
        };
    };
    ShowArenaOno = function ():
        OnoTimer = new Timer(2000);
        OnoTimer.add_event_listener(TimerEvent.TIMER, PopupArenaOno);
        OnoTimer.start();
        PopupArenaOno();
    };
    HideArenaOno = function ():
        if (OnoTimer){
            OnoTimer.remove_event_listener(TimerEvent.TIMER, PopupArenaOno)
        };
        OnoPopupTimer.remove_event_listener(TimerEvent.TIMER, StepArenaOno)
        remove(ThisOno);
    };
    PopupArenaOno = function (evt:Event=None):
        while (ThisOno == LastOno) {
            ThisOno = (CITY_ARENA_ONO1 + int((random.random() * 4)));
        };
        LastOno = ThisOno;
        OnoPopupTimer.add_event_listener(TimerEvent.TIMER, StepArenaOno);
        OnoPopupTimer.start();
        add(ThisOno);
        add(CA_CITY_ARENA);
        actor[ThisOno].alpha = 0;
    };
    StepArenaOno = function (evt:Event):
        if (PopupDir){
            actor[ThisOno].alpha = (actor[ThisOno].alpha - 0.1);
            if (actor[ThisOno].alpha <= 0){
                PopupDir = False;
                remove(ThisOno);
                OnoPopupTimer.remove_event_listener(
                    TimerEvent.TIMER, StepArenaOno
                );
            };
        } else {
            actor[ThisOno].alpha = (actor[ThisOno].alpha + 0.1);
            if (actor[ThisOno].alpha >= 1){
                PopupDir = True;
            };
        };
    };
    InterfaceButtonHover = function (evt:MouseEvent):
        if (
            ((((((((on_stage(SCR_CITY_BACKG_NIGHT))
            or (on_stage(SCR_CITY_BACKG_DAWN))))
            or (on_stage(SCR_CITY_BACKG_DAY))))
            and (!(on_stage(CA_SCR_ARBEITEN_BLOCKCITY)))))
            and (!(on_stage(CA_SCR_INVITE_BLOCKCITY))))
        ){
            Switch (get_actor_id(evt.target)){
                if case(IF_SCHMIEDE:
                    add(CITY_SHAKES);
                    break;
                if case(IF_ZAUBERLADEN:
                    add(CITY_ZAUBERLADEN);
                    break;
                if case(IF_EHRENHALLE:
                    add(CITY_RUHMESHALLE);
                    add(CITY_CA_OVL);
                    break;
                if case(IF_ARENA:
                    add(CITY_ARENA);
                    add(CITY_CA_OVL);
                    ShowArenaOno();
                    break;
                if case(IF_PILZDEALER:
                    add(CITY_DEALER_ANI5);
                    add(CITY_DEALER);
                    HideDealerEyes();
                    break;
                if case(IF_STALL:
                    add(CITY_ESEL2);
                    remove(CITY_ESEL1);
                    add(CITY_CA_OVL);
                    break;
                if case(IF_TAVERNE:
                    add(CITY_TAVERNE);
                    add(CITY_ZWERG);
                    add(CITY_CA_OVL);
                    break;
                if case(IF_POST:
                    add(CITY_POST);
                    add(CITY_ORK);
                    add(CITY_CA_OVL);
                    break;
                if case(IF_ARBEITEN:
                    WacheOver();
                    break;
            };
            if (on_stage(CA_SCR_ARBEITEN_BLOCKCITY)){
                add(SCREEN_ARBEITEN);
            };
            if (on_stage(CA_SCR_INVITE_BLOCKCITY)){
                add(SCREEN_INVITE);
            };
        };
    };
    ExitScreen = function (evt:Event=None){
        if (on_stage(TOILET)){
            send_action(ACT_SCREEN_TAVERNE);
        } else {
            if (on_stage(WITCH)){
                send_action(ACT_SCREEN_ZAUBERLADEN);
            } else {
                if (
                    ((on_stage(TOWER_SCROLLAREA))
                    or (on_stage(LBL_MAINQUEST_TITLE)))
                ){
                    send_action(ACT_SCREEN_WELTKARTE);
                } else {
                    show_city_screen();
                };
            };
        };
    };
    HalleSuchClick = function (evt:Event):
        if (actor[INP_HALLE_GOTO].getChildAt(
            1
        ).text == texts[TXT_HALLE_SUCHFELD_TEXT]){
            actor[INP_HALLE_GOTO].getChildAt(1).text = "";
        };
    };
    RuhmesHalleScroll = function (evt:Event):
        var evt:* = evt;
        if ((evt is KeyboardEvent)){
            if (
                ((((!((KeyboardEvent(evt).keyCode == 13)))
                and (!((KeyboardEvent(evt).keyCode == 10)))))
                and (!((KeyboardEvent(evt).keyCode == 16777230))))
            ){
                return;
            };
        };
        Switch (get_actor_id(evt.target)){
            if case(HALL_GOTO_SPIELER:
                ruhmes_halle_such_name = True;
                ruhmes_halle_such_string = actor[
                    INP['NAME']
                ].getChildAt(1).text;
                send_action(
                    ACT_SCREEN_EHRENHALLE,
                    actor[INP['NAME']].getChildAt(1).text,
                    -1
                );
                break;
            if case(HALL_GOTO_GILDEN:
                if (savegame[SG_GUILD_INDEX] > 0){
                    ruhmes_halle_such_name = True;
                    ruhmes_halle_such_string = gilde;
                    send_action(
                        ACT_SCREEN_GILDENHALLE,
                        "",
                        savegame[SG_GUILD_INDEX],
                        0
                    );
                } else {
                    ruhmes_halle_such_name = False;
                    ruhmes_halle_such_string = "";
                    send_action(ACT_SCREEN_GILDENHALLE, "", 0, 1);
                };
                break;
            if case(HALLE_UP:
                if (guild_hall_mode){
                    send_action(
                        ACT_SCREEN_GILDENHALLE,
                        "",
                        "0",
                        abs(int(
                            actor[HALL_LIST].getChildAt(6 * 7 + 5).text
                        )) - 15
                    );
                } else {
                    send_action(
                        ACT_SCREEN_EHRENHALLE,
                        "",
                        abs(int(
                            actor[HALL_LIST].getChildAt(((6 * 7) + 5)).text
                        )) - 15
                };
                break;
            if case(HALLE_DOWN:
                if (guild_hall_mode){
                    send_action(
                        ACT_SCREEN_GILDENHALLE,
                        "",
                        "0",
                        abs(int(
                            actor[HALL_LIST].getChildAt(((6 * 7) + 5)).text
                        )) + 15
                } else {
                    send_action(
                        ACT_SCREEN_EHRENHALLE,
                        "",
                        abs(int(
                            actor[HALL_LIST].getChildAt(((6 * 7) + 5)).text
                        )) + 15)
                };
                break;
            default:
                ruhmes_halle_such_string = actor[
                    INP_HALLE_GOTO
                ].getChildAt(1).text;
                if (
                    (((((ruhmes_halle_such_string.lower() == "/s [p: 332]")
                    or (ruhmes_halle_such_string.lower() == "/s[p: 332]")))
                    or (ruhmes_halle_such_string.lower() == "/s [p:332]")))
                    or (ruhmes_halle_such_string.lower() == "/s[p:332]"))
                ){
                    play(SND_MOUNT_1);
                    send_action(
                        ACT_SEND_CHAT,
                        EncodeChat("Moo!"),
                        last_chat_index
                    );
                    if (text_dir == "right"){
                        var _local3 = actor[IF_GOLD];
                        with (_local3) {
                            x = IF_LBL_GOLDPILZE_X;
                        };
                        _local3 = actor[LBL_IF_GOLD];
                        with (_local3) {
                            text = "0";
                            x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
                        };
                        _local3 = actor[IF_SILBER];
                        with (_local3) {
                            x = ((actor[LBL_IF_GOLD].x - width) - 10);
                        };
                        _local3 = actor[LBL_IF_SILBER];
                        with (_local3) {
                            text = "00";
                            x = ((actor[IF_SILBER].x - text_width) - 10);
                        };
                        _local3 = actor[LBL_IF_PILZE];
                        with (_local3) {
                            text = "0";
                            x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
                        };
                        enable_popup(LBL_IF_PILZE);
                    } else {
                        _local3 = actor[LBL_IF_SILBER];
                        with (_local3) {
                            text = "00";
                            x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
                        };
                        _local3 = actor[IF_GOLD];
                        with (_local3) {
                            x = ((actor[LBL_IF_SILBER].x - 24) - 10);
                        };
                        _local3 = actor[LBL_IF_GOLD];
                        with (_local3) {
                            text = "0";
                            x = ((actor[IF_GOLD].x - text_width) - 10);
                        };
                        _local3 = actor[LBL_IF_PILZE];
                        with (_local3) {
                            text = "0";
                            x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
                        };
                        enable_popup(LBL_IF_PILZE);
                    };
                };
                if (int(actor[INP_HALLE_GOTO].getChildAt(1).text) > 0){
                    ruhmes_halle_such_name = False;
                    if (guild_hall_mode){
                        send_action(
                            ACT_SCREEN_GILDENHALLE,
                            "",
                            "0",
                            int(actor[INP_HALLE_GOTO].getChildAt(1).text)
                        );
                    } else {
                        send_action(
                            ACT_SCREEN_EHRENHALLE,
                            "",
                            int(actor[INP_HALLE_GOTO].getChildAt(1).text)
                        );
                    };
                } else {
                    ruhmes_halle_such_name = True;
                    if (guild_hall_mode){
                        send_action(
                            ACT_SCREEN_GILDENHALLE,
                            actor[INP_HALLE_GOTO].getChildAt(1).text,
                            "0",
                            "0"
                        );
                    } else {
                        send_action(
                            ACT_SCREEN_EHRENHALLE,
                            actor[INP_HALLE_GOTO].getChildAt(1).text,
                            -1
                        );
                    };
                };
        };
    };
    RemoveInviteWindow = function (evt:Event=None){
        remove_all();
        show_city_screen();
    };
    SendPlayerInvite = function (evt:Event=None){
        if ((evt is KeyboardEvent)){
            if (
                ((((!((KeyboardEvent(evt).keyCode == 13)))
                and (!((KeyboardEvent(evt).keyCode == 10)))))
                and (!((KeyboardEvent(evt).keyCode == 16777230))))
            ){
                return;
            };
        };
        if (
            ((!((actor[INP_CHAR_INVITE].getChildAt(1).text == "")))
            and (!((actor[INP_CHAR_INVITE2].getChildAt(1).text == ""))))
        ){
            send_action(
                ACT_INVITE_PLAYER,
                actor[INP_CHAR_INVITE].getChildAt(1).text.split(
                    ";"
                ).join("AAASEMIAAA"),
                actor[INP_CHAR_INVITE2].getChildAt(1).text.split(
                ";").join("AAASEMIAAA")
            );
        } else {
            error_message(texts[TXT_ERROR_INPUT_REQUIRED]);
        };
    };
    var Gotoplayer_gilde:* = function (evt:MouseEvent){
        if (on_stage(TOWER_SCROLLAREA)){
            return;
        };
        if (SelectedGuild != ""){
            if (SelectedGuild == gilde){
                send_action(ACT_SCREEN_GILDEN);
            } else {
                send_action(ACT_SCREEN_FREMDGILDE, SelectedGuild);
            };
        };
    };
    PrevPlayer = function (evt:MouseEvent=None){
        if (arrow_hall_mode){
            sel_name = last_hall_members[indexInHall];
            send_action(ACT['REQUEST']['CHAR'],
                        last_hall_members[indexInHall]);
        } else {
            sel_name = lastguild_members[indexInGuild];
            send_action(ACT['REQUEST']['CHAR'],
                        lastguild_members[indexInGuild]);
        };
    };
    NextPlayer = function (evt:MouseEvent=None){
        if (arrow_hall_mode){
            sel_name = last_hall_members[(indexInHall + 2)];
            send_action(
                ACT['REQUEST']['CHAR'],
                last_hall_members[(indexInHall + 2)]
            );
        } else {
            sel_name = lastguild_members[(indexInGuild + 2)];
            send_action(
                ACT['REQUEST']['CHAR'],
                lastguild_members[(indexInGuild + 2)]
            );
        };
    };
    var JumpToPlayerHall:* = function (evt:Event=None){
        ruhmes_halle_such_string = lastPlayer;
        ruhmes_halle_such_name = True;
        send_action(
            ACT_SCREEN_EHRENHALLE,
            ruhmes_halle_such_string,
            -1
        );
    };
    var Enterplayer_desc:* = function (evt:FocusEvent){
        var evt:* = evt;
        var _local3 = actor[INP_CHARDESC].getChildAt(0);
        with (_local3) {
            if (type == TextFieldType.INPUT){
                if (text == texts[TXT_ENTERDESC]){
                    text = "";
                };
            };
        };
    };
    var Leaveplayer_desc:* = function (evt:FocusEvent){
        var evt:* = evt;
        var _local3 = actor[INP_CHARDESC].getChildAt(0);
        with (_local3) {
            if (type == TextFieldType.INPUT){
                if (text != player_desc){
                    send_action(
                        ACT_SET_PLAYER_DESC,
                        RemoveIllegalChars(SemiStrip(text))
                    );
                };
                if (text == ""){
                    text = texts[TXT_ENTERDESC];
                };
            };
        };
    };
    RequestAlbum = function (evt:Event=None){
        send_action(ACT_ALBUM);
        show_screen_album();
    };
    PlayerGuildInviteCancel = function (evt:Event=None){
        if (!on_stage(PLAYER_GUILD_INVITE)){
            return;
        };
        remove(GILDE_DIALOG_INVITE);
    };
    PlayerGuildInviteOK = function (evt:Event=None){
        if (!on_stage(PLAYER_GUILD_INVITE)){
            return;
        };
        send_action(
            ACT_GUILD_INVITE,
            actor[INP['NAME']].getChildAt(1).text,
            gilde,
            actor[INP_GILDE_DIALOG_INVITE].getChildAt(1).text,
            MD5(actor[INP['LOGIN_PASSWORD']].getChildAt(1).text),
            ""
        );
    };
    PlayerGuildInvite = function (evt:Event=None){
        var evt:* = evt;
        add(GILDE_DIALOG_INVITE);
        actor[INP_GILDE_DIALOG_INVITE].getChildAt(1).text = lastPlayer;
        var _local3 = actor[LBL_WINDOW_TITLE];
        with (_local3) {
            text = texts[TXT_GILDE_INVITE_TITLE];
            x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((text_width / 2)));
        };
    };
    var RequestStableScreen:* = function (evt:Event){
        send_action(ACT_SCREEN_STALL);
    };
    ZurGilde = function (evt:Event=None){
        send_action(ACT_SCREEN_GILDEN);
    };
    PlayerSendMessage = function (){
        show_post_screen();
    };
    PlayerAttack = function (){
        if (waiting_for(savegame[SG_PVP_REROLL_TIME])){
            var _local2 = actor[LBL_IF_PILZE];
            with (_local2) {
                if (int(savegame[SG_MUSH]) > 0){
                    text = str((int(savegame[SG_MUSH]) - 1));
                };
                x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
            };
            enable_popup(LBL_IF_PILZE);
        };
        send_action(ACT_START_FIGHT, sel_name);
        if (lastAttacked.find(sel_name.lower()) == -1){
            lastAttacked.append(sel_name.lower());
        };
    };
    PlayerInvite = function (){
        var ShowInviteScreen:* = None;
        ShowInviteScreen = function (){
            remove_all();
            show_city_screen();
            hide(INVITE_SUCCESS);
            show(INVITE_INPUTDIALOGUE);
            actor[INP_CHAR_INVITE].getChildAt(1).text = "";
            stage.focus = actor[INP_CHAR_INVITE].getChildAt(1);
            actor[INP_CHAR_INVITE2].getChildAt(1).text = "";
            actor[LBL_WINDOW_TITLE].text = texts[TXT_INVITETITLE];
            actor[LBL_WINDOW_TITLE].x = (
                (IF_WIN_X + IF_WIN_WELCOME_X)
                - int((actor[LBL_WINDOW_TITLE].text_width / 2))
            );
            add(SCREEN_INVITE);
        };
        load(SCREEN_INVITE);
        when_loaded(ShowInviteScreen);
    };
    var BoostBtnDownHandler:* = function (evt:Event){
        var ClickCount:* = 0;
        var evt:* = evt;
        var DoPushBoostBtn:* = function (timerevt:Event){
            var timerevt:* = timerevt;
            if (DestroyBoostBtnTimer){
                DestroyBoostBtnTimer = False;
                var _local3 = BoostBtnRepeatTimer;
                with (_local3) {
                    stop();
                    delay = 1000;
                    remove_event_listener(TimerEvent.TIMER, DoPushBoostBtn)
                };
            } else {
                ClickCount++;
                Switch (ClickCount){
                    if case(1:
                        BoostBtnRepeatTimer.delay = 500;
                        break;
                    if case(3:
                        BoostBtnRepeatTimer.delay = 250;
                        break;
                };
                if (BoostAttribute(evt)){
                    play(SND['CLICK']);
                };
            };
        };
        ClickCount = 0;
        if (BoostBtnRepeatTimer.running){
            return;
        };
        DestroyBoostBtnTimer = False;
        var _local3 = BoostBtnRepeatTimer;
        with (_local3) {
            delay = 1000;
            add_event_listener(TimerEvent.TIMER, DoPushBoostBtn);
            start();
        };
    };
    var BoostBtnUpHandler:* = function (evt:Event){
        if (BoostBtnRepeatTimer.running){
            DestroyBoostBtnTimer = True;
        };
    };
    BoostAttribute = function (evt:Event):
        if (canBoost[(get_actor_id(evt.target) - SCR_CHAR_STEIGERN1)]){
            send_action(
                ACT_BUY_ATTRIB,
                ((get_actor_id(evt.target) - SCR_CHAR_STEIGERN1) + 1)
            );
        };
        return (canBoost[(get_actor_id(evt.target) - SCR_CHAR_STEIGERN1)]);
    };
    BoostBtnTimerFunction = function (evt:TimerEvent){
        if (BoostBtnChange > 1){
            BoostBtnChange--;
            return;
        };
        if (BoostBtnChange == 1){
            BoostBtnChange = 0;
            if (inBoostBtn){
                if (light_mode){
                    set_alpha(CHAR_PREISE, 1);
                    set_alpha(CHAR_SECONDPROP, 0);
                } else {
                    fade_in(CHAR_PREISE, 20, 0.2);
                    fade_out(CHAR_SECONDPROP, 20, 0.2);
                };
            } else {
                if (on_stage(LBL_SCR_CHAR_PREIS1)){
                    if (light_mode){
                        add(CHAR_SECONDPROP);
                        if (on_stage(POPUP_INFO)){
                            add(POPUP_INFO);
                        };
                        set_alpha(CHAR_PREISE, 0);
                        set_alpha(CHAR_SECONDPROP, 1);
                    } else {
                        fade_out(CHAR_PREISE, 20, 0.2);
                        add(CHAR_SECONDPROP);
                        if (on_stage(POPUP_INFO)){
                            add(POPUP_INFO);
                        };
                        fade_in(CHAR_SECONDPROP, 20, 0.2);
                    };
                };
            };
        };
    };
    var BoostBtnOver:* = function (evt:Event){
        if (!inBoostBtn){
            BoostBtnChange = 6;
        };
        inBoostBtn = True;
    };
    var BoostBtnOut:* = function (evt:Event){
        if (inBoostBtn){
            BoostBtnChange = 6;
        };
        inBoostBtn = False;
    };
    InventoryItemMouseDown = function (evt:MouseEvent){
        if (
            ((((on_stage(SCR_FIDGET_BG))
            or (on_stage(SCR_SHAKES_BG))))
            or (on_stage(TOWER_SCROLLAREA)))
        ){
            add(CA_SELL_ITEM);
        };
    };
    BackpackItemMouseDown = function (evt:MouseEvent){
        add(CA_USE_ITEM);
    };
    InventoryItemMouseUp = function (evt:MouseEvent){
        remove(CA_SELL_ITEM);
        remove(CA_USE_ITEM);
    };
    DropHandler = function (actor_id, targetID):
        var tower_mode:Boolean;
        var sourceSlot;
        var targetSlot;
        tower_mode = on_stage(PREV_COPYCAT);
        trc("dragdrop", actor_id, targetID, tower_mode);
        sourceSlot = 0;
        targetSlot = 0;
        if (targetID == CA_SELL_ITEM){
            trc("sell item");
            if (
                (((actor_id >= CHAR_SLOT_1))
                and ((actor_id <= CHAR_SLOT_15)))
            ){
                trc("selling can be done");
                sourceSlot = ((actor_id - CHAR_SLOT_1) + 1);
                if (tower_mode){
                    trc("impossible here");
                    return (False);
                };
                send_action(
                    ACT_INVENTORY_CHANGE,
                    (((sourceSlot <= 10))
                    ? 1
                    : (((sourceSlot <= 15))
                       ? 2
                       : (((sourceSlot <= 21))
                          ? 4
                          : 3))),
                    (sourceSlot - (((sourceSlot <= 10))
                    ? 0
                    : (((sourceSlot <= 15))
                       ? 10
                       : (((sourceSlot <= 21))
                          ? 15
                          : 21)))),
                    0,
                    0
                );
                return (True);
            };
            trc("wrong source");
        } else {
            if (targetID == CA_USE_ITEM){
                trc("use item");
                if (
                    (((actor_id >= CHAR_SLOT_10))
                    and ((actor_id <= CHAR_SLOT_SHAKES_6)))
                ){
                    trc("using can be done");
                    sourceSlot = ((actor_id - CHAR_SLOT_1) + 1);
                    if (tower_mode){
                        send_action(
                            ACT_MOVE_COPYCAT_ITEM,
                            2,
                            (sourceSlot - 10),
                            (copyCatSel + 101),
                            -1
                        );
                    } else {
                        send_action(
                            ACT_INVENTORY_CHANGE,
                            (((sourceSlot <= 10))
                                ? 1
                                : (((sourceSlot <= 15))
                                   ? 2
                                   : (((sourceSlot <= 21))
                                      ? 4
                                      : 3))),
                            (sourceSlot - (((sourceSlot <= 10))
                                ? 0
                                : (((sourceSlot <= 15))
                                   ? 10
                                   : (((sourceSlot <= 21))
                                       ? 15
                                       : 21)))),
                            1,
                            -1
                        );
                    };
                    return (True);
                };
                trc("wrong source");
            } else {
                if (targetID == CA_CHALDRON){
                    if (
                        (((actor_id >= CHAR_SLOT_1))
                        and ((actor_id <= CHAR_SLOT_15)))
                    ){
                        trc("donating to witch can be done");
                        sourceSlot = ((actor_id - CHAR_SLOT_1) + 1);
                        if (tower_mode){
                            trc("impossible here");
                            return (False);
                        };
                        send_action(
                            ACT_WITCH_DONATE,
                            (((sourceSlot <= 10))
                                ? 1
                                : (((sourceSlot <= 15))
                                   ? 2
                                   : (((sourceSlot <= 21))
                                      ? 4
                                      : 3))),
                            (sourceSlot - (((sourceSlot <= 10))
                                ? 0
                                : (((sourceSlot <= 15))
                                   ? 10
                                   : (((sourceSlot <= 21))
                                      ? 15
                                      : 21))))
                        );
                        return (True);
                    };
                    trc("wrong source");
                } else {
                    trc("moving items around");
                    if (
                        (((((actor_id >= CHAR_SLOT_1))
                        and ((actor_id <= CHAR_SLOT_SHAKES_6))))
                        and (!((targetID == CA_TOILET_BOWL))))
                    ){
                        trc("source is ok");
                        sourceSlot = ((actor_id - CHAR_SLOT_1) + 1);
                        if (
                            (((targetID >= CHAR_SLOT_1))
                            and ((targetID <= CHAR_SLOT_SHAKES_6)))
                        ){
                            trc("target is ok");
                            targetSlot = ((targetID - CHAR_SLOT_1) + 1);
                            if (tower_mode){
                                if (
                                    towerSG[(((((sourceSlot <= 10))
                                        ? ((
                                           TSG_COPYCATS
                                           + (copyCatSel * COPYCAT
                                        )) + CPC_ITEMS)
                                        : TSG_LOOT_SACK) +
                                        ((((sourceSlot <= 10))
                                            ? (sourceSlot - 1)
                                            : (sourceSlot - 11))
                                                * SG['ITM']['SIZE']))
                                                + SG_ITM_TYP)] > 0
                            ){
                                    trc("do it");
                                    send_action(
                                        ACT_MOVE_COPYCAT_ITEM,
                                        (((sourceSlot <= 10))
                                            ? (copyCatSel + 101)
                                            : 2),
                                        (((sourceSlot <= 10))
                                            ? sourceSlot
                                            : (sourceSlot - 10)),
                                        (((targetSlot <= 10))
                                            ? (copyCatSel + 101)
                                            : 2),
                                        (((targetSlot <= 10))
                                            ? targetSlot :
                                            (targetSlot - 10))
                                        );
                                    return (True);
                                };
                                trc("source slot empty");
                            } else {
                                if (
                                    savegame[
                                        (((((sourceSlot <= 15))
                                            ? SG_INVENTORY_OFFS
                                            : (((sourceSlot <= 21))
                                            ? SG_FIDGET_ITEM1
                                            : SG_SHAKES_ITEM1))
                                              + ((sourceSlot
                                              - (((sourceSlot <= 15))
                                                 ? 1
                                                 : (((sourceSlot <= 21))
                                                    ? 16
                                                    : 22)))
                                                      * SG['ITM']['SIZE']))
                                                      + SG_ITM_TYP)] > 0
                                ){
                                    trc("do it");
                                    send_action(
                                        ACT_INVENTORY_CHANGE,
                                        (((sourceSlot <= 10))
                                            ? 1
                                            : (((sourceSlot <= 15))
                                               ? 2
                                               : (((sourceSlot <= 21))
                                                  ? 4
                                                  : 3))),
                                        (sourceSlot - (((sourceSlot <= 10))
                                            ? 0
                                            : (((sourceSlot <= 15))
                                               ? 10
                                               : (((sourceSlot <= 21))
                                                  ? 15
                                                  : 21)))),
                                        (((targetSlot <= 10))
                                            ? 1
                                            : (((targetSlot <= 15))
                                               ? 2
                                               : (((targetSlot <= 21))
                                                  ? 4
                                                  : 3))),
                                        (targetSlot - (((targetSlot <= 10))
                                            ? 0
                                            : (((targetSlot <= 15))
                                               ? 10
                                               : (((targetSlot <= 21))
                                                  ? 15
                                                  : 21))))
                                    );
                                    return (True);
                                };
                                trc("source slot empty");
                            };
                        } else {
                            trc("target wrong");
                        };
                    } else {
                        if (targetID == CA_TOILET_BOWL){
                            trc("drop in toilet");
                            if (
                                (((actor_id >= CHAR_SLOT_10))
                                and ((actor_id <= CHAR_SLOT_SHAKES_6)))
                            ){
                                sourceSlot = ((actor_id - CHAR_SLOT_1) + 1)
                                send_action(
                                    ACT_INVENTORY_CHANGE,
                                    (((sourceSlot <= 10))
                                        ? 1
                                        : (((sourceSlot <= 15))
                                           ? 2
                                           : (((sourceSlot <= 21))
                                              ? 4
                                              : 3))),
                                    (sourceSlot - (((sourceSlot <= 10))
                                        ? 0
                                        : (((sourceSlot <= 15))
                                           ? 10
                                           : (((sourceSlot <= 21))
                                              ? 15
                                              : 21)))),
                                    10,
                                    0
                                );
                                show(TOILET_DROP);
                                return (True);
                            };
                        } else {
                            trc("source wrong");
                        };
                    };
                };
            };
        };
        return (False);
    };
    PotionSingleClick = function (evt:Event=None){
    };
    PotionDoubleClick = function (evt:Event=None){
        if (!on_stage(CHAR_MESSAGE)){
            send_action(
                ACT_KILL_POTION,
                ((get_actor_id(evt.target) - CHAR_POTION)
                + 1)
            );
        };
    };
    var Openfriend_link:* = function (evt:Event){
        navigate_to_url(
            new URLRequest(
                ((("mailto:?subject=" + texts[TXT_FRIEND_SUBJECT].split(
                    " "
                ).join("%20").split(
                    "&"
                ).join("%26")) + "&body=") + friend_link)
            )
        );
    };
    var TowerScrollSingle:* = function (evt:Event){
    };
    towerBoostPriceFadeout = function (evt:TimerEvent){
        fade_out(TOWER_BOOSTPRICE);
    };
    tower_levelLabelMoveFn = function (evt:TimerEvent){
        if (abs((actor[LBL_TOWER_EXPLABEL].x - tower_levelLabelPos)) >= 1){
            actor[LBL_TOWER_EXPLABEL].x = (
                (actor[LBL_TOWER_EXPLABEL].x + tower_levelLabelPos) / 2
            );
        } else {
            actor[LBL_TOWER_EXPLABEL].x = tower_levelLabelPos;
            tower_levelLabelTimer.stop();
        };
    };
    ShowTowerBoostPrices = function (evt:MouseEvent){
        var i;
        towerBoostPriceFadeoutTimer.stop();
        fade_in(TOWER_BOOSTPRICE);
        tower_levelLabelPos = (SCR_CHAR_CHARX + 3);
        tower_levelLabelTimer.start();
    };
    HideTowerBoostPrices = function (evt:MouseEvent){
        var i;
        towerBoostPriceFadeoutTimer.start();
        tower_levelLabelPos = (
            (SCR_CHAR_CHARX + 127)
            - int((actor[LBL_TOWER_EXPLABEL].text_width / 2))
        );
        tower_levelLabelTimer.start();
    };
    BoostCopycat = function (){
        send_action(
            ACT_COPYCAT_BOOST,
            (copyCatSel + 1),
            ((towerSG[
                ((TSG_COPYCATS + (COPYCAT * copyCatSel)) + CPC_LEVEL)
            ] * 1) + 1)
        );
    };
    ShopAniFrame = function (evt:TimerEvent){
        var pv:Boolean;
        var AffeStep;
        var FidgetAugenZu:Boolean;
        var ShakesAugenZu;
        var WasPassiert:Boolean;
        pv = on_stage(POPUP_INFO);
        WasPassiert = False;
        if (dragDropActive){
            PlayerIdle = False;
            WasIdleCount = 0;
            ShopIdle = 0;
            remove(FIDGET_DAY);
            remove(FIDGET_IDLE);
            SaleRecoverTime = 10;
            return;
        };
        if (ShopIdle == 400){
            PlayerIdle = True;
            WasPassiert = True;
            if (on_stage(SCR_SHAKES_BG)){
                if (WasIdleCount > 2){
                    ShakesIdlePhase = 4;
                    ShakesIdleStep = 0;
                } else {
                    ShakesIdleStep++;
                    Switch (int(ShakesIdleStep)){
                        if case(1:
                        if case(5:
                        if case(9:
                        if case(12:
                        if case(15:
                        if case(19:
                        if case(23:
                        if case(27:
                        if case(33:
                            ShakesIdlePhase = 1;
                            break;
                        if case(2:
                        if case(4:
                        if case(6:
                        if case(8:
                        if case(10:
                        if case(13:
                        if case(16:
                        if case(18:
                        if case(20:
                        if case(22:
                        if case(24:
                        if case(26:
                        if case(28:
                        if case(31:
                            ShakesIdlePhase = 2;
                            break;
                        if case(3:
                        if case(7:
                        if case(11:
                        if case(14:
                        if case(17:
                        if case(21:
                        if case(25:
                        if case(29:
                            ShakesIdlePhase = 3;
                            break;
                        if case(35:
                            WasIdleCount++;
                            PlayerIdle = False;
                            ShakesIdlePhase = 0;
                            ShopIdle = 0;
                            ShakesIdleStep = 0;
                            break;
                        default:
                            WasPassiert = False;
                    };
                };
            };
        } else {
            ShopIdle++;
        };
        if (SaleRecoverTime > 0){
            SaleRecoverTime--;
            if (SaleRecoverTime == 0){
                WasPassiert = True;
            };
        };
        if (on_stage(SCR_SHAKES_BG)){
            ShakesBlinzeln++;
            if (ShakesBlinzeln > 73){
                ShakesBlinzeln = int((random.random() * 30));
                WasPassiert = True;
                ShakesAugenZu = 0;
            } else {
                if (ShakesBlinzeln > 72){
                    WasPassiert = True;
                    ShakesAugenZu = 0;
                } else {
                    if (ShakesBlinzeln > 71){
                        WasPassiert = True;
                        ShakesAugenZu = 0;
                    } else {
                        if (ShakesBlinzeln > 70){
                            WasPassiert = True;
                            ShakesAugenZu = 2;
                        };
                    };
                };
            };
            if (WasPassiert){
                add(SCREEN_SHAKES);
                if ((((special_action == 2)) or ((special_action == 5)))){
                    add(SHAKES_EPCIOVL);
                    actor[SHAKES_EPCIOVL].mouse_enabled = False;
                };
                if (!sleep_time()){
                    if (((PlayerIdle) and (!((ShakesIdlePhase == 0))))){
                        remove(SHAKES_NIGHT);
                        remove(SHAKES_DAY);
                        remove(SHAKES_BLINZELN1, SHAKES_BLINZELN2);
                        Switch (ShakesIdlePhase){
                            if case(1:
                                remove(
                                    SHAKES_IDLE,
                                    SHAKES_IDLE2,
                                    SHAKES_IDLE3
                                );
                                break;
                            if case(2:
                                remove(
                                   SHAKES_IDLE,
                                   SHAKES_IDLE1,
                                   SHAKES_IDLE3
                                );
                                break;
                            if case(3:
                                remove(
                                   SHAKES_IDLE, SHAKES_IDLE1, SHAKES_IDLE2
                                );
                                break;
                            if case(4:
                                remove(
                                   SHAKES_IDLE1, SHAKES_IDLE2, SHAKES_IDLE3
                                );
                                break;
                        };
                    } else {
                        remove(
                           SHAKES_IDLE,
                           SHAKES_IDLE1,
                           SHAKES_IDLE2,
                           SHAKES_IDLE3
                        );
                        remove(SHAKES_NIGHT);
                        if (ShakesAugenZu != 2){
                            remove(SHAKES_BLINZELN2);
                        };
                        if (ShakesAugenZu != 1){
                            remove(SHAKES_BLINZELN1);
                        };
                    };
                } else {
                    remove(
                        SHAKES_IDLE,
                        SHAKES_IDLE1,
                        SHAKES_IDLE2,
                        SHAKES_IDLE3
                    );
                    remove(SHAKES_DAY);
                };
                if (pv){
                    add(POPUP_INFO);
                };
            };
            add(LBL['ERROR']);
        } else {
            if (on_stage(SCR_FIDGET_BG)){
                AffeBlinzeln++;
                FidgetBlinzeln++;
                if (AffeBlinzeln > 73){
                    AffeBlinzeln = int((random.random() * 30));
                    if (int((random.random() * 2)) == 1){
                        AffeStep = 1;
                        WasPassiert = True;
                    } else {
                        AffeStep = 3;
                        WasPassiert = True;
                    };
                } else {
                    if (AffeBlinzeln > 70){
                        AffeStep = 2;
                        WasPassiert = True;
                    };
                };
                if (FidgetBlinzeln > 73){
                    FidgetBlinzeln = int((random.random() * 30));
                    FidgetAugenZu = False;
                    WasPassiert = True;
                } else {
                    if (FidgetBlinzeln > 70){
                        if (on_stage(FIDGET_DAY)){
                            FidgetAugenZu = True;
                            WasPassiert = True;
                        };
                    };
                };
                if (((WasPassiert) and (!(on_stage(GOTO_WITCH_OVL))))){
                    add(SCREEN_FIDGET);
                    if (savegame[SG_LEVEL] >= 66){
                        add(CA_GOTO_WITCH);
                    };
                    if (
                        (((special_action == 2))
                        or ((special_action == 5)))
                    ){
                        add(FIDGET_EPCIOVL);
                        actor[FIDGET_EPCIOVL].mouse_enabled = False;
                    };
                    if (AffeStep >= 2){
                        remove(FIDGET_AFFE1);
                    };
                    if (AffeStep == 2){
                        remove(FIDGET_AFFE3);
                    };
                    if (!sleep_time()){
                        if (PlayerIdle){
                            remove(FIDGET_DAY);
                        };
                        remove(FIDGET_NIGHT);
                    } else {
                        remove(FIDGET_DAY);
                    };
                    if (((!(FidgetAugenZu)) or (PlayerIdle))){
                        remove(FIDGET_BLINZELN);
                    };
                    if (pv){
                        add(POPUP_INFO);
                    };
                };
                add(LBL['ERROR']);
            } else {
                PlayerIdle = False;
                WasIdleCount = 0;
                ShopIdle = 0;
            };
        };
    };
    ShopMouseDownEvent = function (evt:MouseEvent){
        add(CA_USE_ITEM);
    };
    ShopMouseUpEvent = function (evt:MouseEvent){
        remove(CA_USE_ITEM);
    };
    RequestNewWarez = function (evt:Event=None){
        var RerollResetTimer:* = None;
        var RerollReset:* = None;
        var evt:* = evt;
        RerollReset = function (evt:Event){
            BlockReroll = False;
            RerollResetTimer.remove_event_listener(
                TimerEvent.TIMER, RerollReset
            );
        };
        if ((((evt is MouseEvent)) and (FrenzyMode))){
            if (RollFrenzy.running){
                error_message("Frenzy stopped!");
                RollFrenzy.stop();
                return;
            };
            error_message("Frenzy started!");
            RollFrenzy.start();
        };
        if (!BlockReroll){
            BlockReroll = True;
            RerollResetTimer = new Timer(5000, 1);
            RerollResetTimer.add_event_listener(
                TimerEvent.TIMER, RerollReset
            );
            RerollResetTimer.start();
            PlayerIdle = False;
            ShopIdle = 0;
            remove(FIDGET_DAY);
            remove(FIDGET_IDLE);
            SaleRecoverTime = 10;
            send_action(
                ACT_REQUEST_NEWWAREZ,
                ((on_stage(SCR_FIDGET_BG)) ? 1 : 2)
            );
        };
    };
    RequestWitchScreen = function (evt:Event=None){
        send_action(ACT_SCREEN_WITCH);
    };
    CancelQuest = function (evt:Event=None){
        send_action(ACT_QUEST_CANCEL);
    };
    SkipQuest = function (evt:Event=None){
        send_action(ACT_QUEST_SKIP);
    };
    var GuildMsgMode:* = function (evt:Event){
        if (on_stage(INP_POST_ADDRESS)){
            if (text_dir == "right"){
                actor[POST_GUILD].x = (
                    ((POST_INP_X + actor[INP_POST_ADDRESS].width)
                    - actor[POST_GUILD].width) - 5
                );
            } else {
                actor[POST_GUILD].x = (POST_INP_X + 5);
            };
            remove(INP_POST_ADDRESS);
            actor[INP_POST_ADDRESS].getChildAt(1).text = "";
        } else {
            if (text_dir == "right"){
                actor[POST_GUILD].x = (POST_INP_X + 5);
            } else {
                actor[POST_GUILD].x = (
                    ((POST_INP_X + actor[INP_POST_ADDRESS].width)
                    - actor[POST_GUILD].width) - 5
                );
            };
            add(INP_POST_ADDRESS);
            add(POST_GUILD);
            actor[INP_POST_ADDRESS].getChildAt(1).text = texts[
                TXT_EMPFAENGER
            ];
        };
    };
    Attackenemy = function (evt:Event=None){
        var evt:* = evt;
        if ((evt is KeyboardEvent)){
            if (
                ((((!((KeyboardEvent(evt).keyCode == 13)))
                and (!((KeyboardEvent(evt).keyCode == 10)))))
                and (!((KeyboardEvent(evt).keyCode == 16777230))))
            ){
                return;
            };
        };
        if (waiting_for(savegame[SG_PVP_REROLL_TIME])){
            var _local3 = actor[LBL_IF_PILZE];
            with (_local3) {
                if (int(savegame[SG_MUSH]) > 0){
                    text = str((int(savegame[SG_MUSH]) - 1));
                };
                x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
            };
        };
        enable_popup(LBL_IF_PILZE);
        send_action(
            ACT_START_FIGHT,
            actor[INP_ARENA_enemy].getChildAt(1).text
        );
        if (
            lastAttacked.find(
                actor[INP_ARENA_enemy].getChildAt(1).text.lower()) == -1
            ){
            lastAttacked.append(
                actor[INP_ARENA_enemy].getChildAt(1).text.lower()
            );
        };
    };
    ClickMount = function (evt:MouseEvent){
        var actor_id;
        var GoldKosten;
        var PilzKosten;
        var tmpX;
        actor_id = get_actor_id(evt.target);
        GoldKosten = 0;
        PilzKosten = 0;
        tmpX = 0;
        if (!on_stage(LBL_STALL_LAUFZEIT)){
            OldMount = 0;
        };
        Switch (actor_id){
            if case(CA_STALL_BOX_GUT1:
                SelectedMount = 3;
                break;
            if case(CA_STALL_BOX_GUT2:
                SelectedMount = 1;
                break;
            if case(CA_STALL_BOX_GUT3:
                SelectedMount = 2;
                break;
            default:
                SelectedMount = (
                    (((((actor_id >= CA_STALL_BOX_GUT1))
                    and ((actor_id <= CA_STALL_BOX_GUT4))))
                        ? (actor_id - CA_STALL_BOX_GUT1)
                        : (actor_id - CA_STALL_BOX_BOESE1)) + 1
                );
        };
        add_some(LBL_STALL_LAUFZEIT, STALL_BUY);
        SetCnt(STALL_MUSH, IF_PILZE);
        SetCnt(STALL_GOLD, IF_GOLD);
        SetCnt(STALL_SCHATZGOLD, IF_GOLD);
        SetCnt(STALL_SCHATZSILBER, IF_SILBER);
        actor[LBL_STALL_TITEL].text = texts[
            ((TXT_STALL_MOUNTTITEL + SelectedMount)
            + (((char_volk >= 5))
               ? 3
               : -1))
        ];
        actor[LBL_STALL_TEXT].text = texts[
            ((TXT_STALL_MOUNTTEXT + SelectedMount)
             + (((char_volk >= 5))
                ? 3
                : -1))
        ];
        actor[LBL_STALL_GAIN].text = texts[
            ((TXT_MOUNT_GAIN1 + SelectedMount) - 1)
        ].split("|").join("");
        if (text_dir == "right"){
            actor[LBL_STALL_TITEL].x = (
                (actor[LBL_STALL_TEXT].x + actor[LBL_STALL_TEXT].width)
                - actor[LBL_STALL_TITEL].text_width
            );
            actor[LBL_STALL_GAIN].x = (
                (actor[LBL_STALL_TEXT].x + actor[LBL_STALL_TEXT].width)
                - actor[LBL_STALL_GAIN].text_width
            );
        };
        remove(
            LBL_STALL_SCHATZGOLD,
            STALL_SCHATZGOLD,
            LBL_STALL_SCHATZSILBER,
            STALL_SCHATZSILBER,
            LBL_STALL_SCHATZ
        );
        if (
            len(texts[((TXT_MOUNT_GAIN1 + SelectedMount) - 1)].split(
                "|"
            )) > 1
        ){
            if (text_dir == "right"){
                tmpX = (actor[LBL_STALL_GAIN].x - 10);
            } else {
                tmpX = ((actor[LBL_STALL_GAIN].x
                        + actor[LBL_STALL_GAIN].width
                ) + 10);
            };
            if (gold_anteil(stundenlohn) > 0){
                add_some(LBL_STALL_SCHATZGOLD, STALL_SCHATZGOLD);
                actor[LBL_STALL_SCHATZGOLD].text = str(
                    gold_anteil(stundenlohn)
                );
                if (text_dir == "right"){
                    actor[STALL_SCHATZGOLD].x = (
                        tmpX - actor[STALL_SCHATZGOLD].width
                    );
                    tmpX = (tmpX - (actor[STALL_SCHATZGOLD].width + 10));
                    actor[LBL_STALL_SCHATZGOLD].x = (
                        tmpX - actor[LBL_STALL_SCHATZGOLD].text_width
                    );
                    tmpX = (tmpX - (
                        actor[LBL_STALL_SCHATZGOLD].text_width + 10
                    ));
                } else {
                    actor[LBL_STALL_SCHATZGOLD].x = tmpX;
                    tmpX += (actor[LBL_STALL_SCHATZGOLD].text_width + 10)
                    actor[STALL_SCHATZGOLD].x = tmpX;
                    tmpX = (tmpX + (actor[STALL_SCHATZGOLD].width + 10));
                };
            };
            if (silber_anteil(stundenlohn) > 0){
                add_some(LBL_STALL_SCHATZSILBER, STALL_SCHATZSILBER);
                actor[LBL_STALL_SCHATZSILBER].text = str(
                    silber_anteil(stundenlohn)
                );
                if (text_dir == "right"){
                    actor[STALL_SCHATZSILBER].x = (
                        tmpX - actor[STALL_SCHATZSILBER].width
                    );
                    tmpX -= (actor[STALL_SCHATZSILBER].width + 10)
                    actor[LBL_STALL_SCHATZSILBER].x = (
                        tmpX - actor[LBL_STALL_SCHATZSILBER].text_width
                    );
                    tmpX -= (actor[LBL_STALL_SCHATZSILBER].text_width + 10)
                } else {
                    actor[LBL_STALL_SCHATZSILBER].x = tmpX;
                    tmpX += (actor[LBL_STALL_SCHATZSILBER].text_width + 10)
                    actor[STALL_SCHATZSILBER].x = tmpX;
                    tmpX += (actor[STALL_SCHATZSILBER].width + 10)
                };
            };
            add(LBL_STALL_SCHATZ);
            if (text_dir == "right"){
                actor[LBL_STALL_SCHATZ].x = (
                    tmpX - actor[LBL_STALL_SCHATZ].text_width
                );
            } else {
                actor[LBL_STALL_SCHATZ].x = tmpX;
            };
        };
        Switch ((SelectedMount + (((char_volk >= 5)) ? 4 : 0))){
            if case(1:
                if ((((ststep == 0)) or ((ststep == 4)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 1;
                PilzKosten = 0;
                break;
            if case(2:
                if ((((ststep == 1)) or ((ststep == 5)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 5;
                PilzKosten = 0;
                break;
            if case(3:
                if ((((ststep == 2)) or ((ststep == 6)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 10;
                PilzKosten = 1;
                break;
            if case(4:
                if ((((ststep == 3)) or ((ststep == 7)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 0;
                PilzKosten = 25;
                break;
            if case(5:
                if ((((ststep == 0)) or ((ststep == 4)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 1;
                PilzKosten = 0;
                break;
            if case(6:
                if ((((ststep == 1)) or ((ststep == 5)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 5;
                PilzKosten = 0;
                break;
            if case(7:
                if ((((ststep == 2)) or ((ststep == 6)))){
                    ststep++;
                } else {
                    ststep = 0;
                };
                GoldKosten = 10;
                PilzKosten = 1;
                break;
            if case(8:
                if ((((ststep == 3)) or ((ststep == 7)))){
                    ststep++;
                };
                GoldKosten = 0;
                PilzKosten = 25;
                break;
        };
        if (((!((SelectedMount == OldMount))) or ((OldMount == 0)))){
            play(
                (((SND_MOUNT_1 + SelectedMount) + (((((char_volk >= 5))
                and (!(param_censored)))) ? 4 : 0)) - 1)
            );
        };
        OldMount = SelectedMount;
        if (savegame[SG_MOUNT] > SelectedMount){
            remove(STALL_BUY);
        } else {
            if (savegame[SG_MOUNT] == 0){
                set_btn_text(STALL_BUY, texts[TXT_STALL_BUY]);
            } else {
                set_btn_text(STALL_BUY, texts[
                    (((savegame[SG_MOUNT] < SelectedMount))
                        ? TXT_STALL_UPGRADE
                        : TXT_STALL_PROLONG)
                ]);
            };
        };
        remove(LBL_STALL_GOLD, STALL_GOLD, LBL_STALL_MUSH, STALL_MUSH);
        if (GoldKosten > 0){
            if (GoldKosten > int((savegame[SG_GOLD] / 100))){
                remove(STALL_BUY);
            };
            add_some(LBL_STALL_GOLD, STALL_GOLD);
            actor[LBL_STALL_GOLD].text = str(GoldKosten);
            actor[STALL_GOLD].x = (
                (actor[LBL_STALL_GOLD].x
                + actor[LBL_STALL_GOLD].text_width) + 10
            );
        };
        if (PilzKosten > 0){
            if (PilzKosten > int(savegame[SG_MUSH])){
                remove(STALL_BUY);
            };
            add_some(LBL_STALL_MUSH, STALL_MUSH);
            actor[LBL_STALL_MUSH].text = str(PilzKosten);
            if (GoldKosten > 0){
                actor[LBL_STALL_MUSH].x = (
                    (actor[STALL_GOLD].x + actor[STALL_GOLD].width) + 15
                );
            } else {
                actor[LBL_STALL_MUSH].x = actor[LBL_STALL_GOLD].x;
            };
            actor[STALL_MUSH].x = (
               (actor[LBL_STALL_MUSH].x
               + actor[LBL_STALL_MUSH].text_width) + 10
            );
        };
    };
    BuyMount = function (evt:Event=None){
        send_action(ACT_BUY_MOUNT, SelectedMount);
    };
    var JumpToGuildHall:* = function (evt:Event=None){
        ruhmes_halle_such_string = last_guild_shown;
        ruhmes_halle_such_name = True;
        send_action(
            ACT_SCREEN_GILDENHALLE,
            ruhmes_halle_such_string,
            "0",
            "0"
        );
    };
    var AttackLinkClick:* = function (evt:Event){
        if (guild_attacked != ""){
            if (guild_attacked == gilde){
                send_action(ACT_SCREEN_GILDEN);
            } else {
                send_action(ACT_SCREEN_FREMDGILDE, guild_attacked);
            };
        };
    };
    var DefenceLinkClick:* = function (evt:Event){
        if (guild_attacking != ""){
            if (guild_attacking == gilde){
                send_action(ACT_SCREEN_GILDEN);
            } else {
                send_action(ACT_SCREEN_FREMDGILDE, guild_attacking);
            };
        };
    };
    var OpenGuildLink:* = function (evt:MouseEvent=None){
        navigate_to_url(new URLRequest(guildForumLink), "_blank");
    };
    var CleanupField:* = function (actor_id){
        var actor_id:* = actor_id;
        var FixContent:* = function (evt:KeyboardEvent){
            if (actor[actor_id].getChildAt(0).text != RemoveIllegalChars(
                    actor[actor_id].getChildAt(0).text)
            ){
                actor[actor_id].getChildAt(0).text = RemoveIllegalChars(
                    actor[actor_id].getChildAt(0).text
                );
            };
        };
        var _local3 = actor[actor_id];
        with (_local3) {
            add_event_listener(KeyboardEvent.KEY_UP, FixContent);
            add_event_listener(KeyboardEvent.KEY_DOWN, FixContent);
        };
    };
    ShowExtendedHistory = function (evt:Event){
    };
    HideExtendedHistory = function (evt:Event){
    };
    AdvancedChatHandler = function (evt:KeyboardEvent){
        var whisperCmd:String;
        var i;
        var textEntered:String;
        whisperCmd = "/whisper ";
        if (texts[TXT_WHISPER]){
            whisperCmd = (texts[TXT_WHISPER] + " ");
        };
        if (evt.keyCode == 38){
            actor[INP_GILDE_CHAT].getChildAt(0).text = lastChatLine;
            actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                len(lastChatLine), len(lastChatLine)
            );
            return;
        };
        if (
            (((((((((((evt.keyCode == 37))
            or ((evt.keyCode == 39))))
            or ((evt.keyCode == 40))))
            or ((evt.keyCode == 8))))
            or ((evt.keyCode == 16))))
            or ((evt.keyCode == 17)))
        ){
        } else {
            textEntered = actor[INP_GILDE_CHAT].getChildAt(0).text[
                0: actor[INP_GILDE_CHAT].getChildAt(0).caretIndex
            ];
            i = 0;
            while (i < len(suggestNames)) {
                if (
                    (((len(textEntered) >= 3))
                    and ((textEntered.lower() == (
                        "/w " + suggestNames[i].lower().split(
                            " ").join("#")
                        )[0: len(textEntered) ])))
                ){
                    actor[INP_GILDE_CHAT].getChildAt(0).text = (
                        actor[INP_GILDE_CHAT].getChildAt(0).text[
                            0: actor[INP_GILDE_CHAT].getChildAt(
                                0
                            ).caretIndex
                        ] + ("/w " + suggestNames[i].split(
                           " "
                        ).join("#")).substr(
                            actor[INP_GILDE_CHAT].getChildAt(0).caretIndex
                        )
                    );
                    actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                        actor[INP_GILDE_CHAT].getChildAt(0).caretIndex,
                        len(actor[INP_GILDE_CHAT].getChildAt(0).text)
                    );
                    break;
                };
                if (
                    (((len(textEntered) >= len(whisperCmd)))
                    and ((textEntered.lower() == (
                        whisperCmd + suggestNames[i].lower())[
                            0: len(textEntered)]))
                        )
                ){
                    actor[INP_GILDE_CHAT].getChildAt(0).text = (
                        actor[INP_GILDE_CHAT].getChildAt(0).text[
                            0:
                            actor[INP_GILDE_CHAT].getChildAt(0).caretIndex
                        ] + (whisperCmd + suggestNames[i].split(
                            " "
                        ).join("#"))[
                            actor[INP_GILDE_CHAT].getChildAt(0).caretIndex:
                        ]
                    );
                    actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                        actor[INP_GILDE_CHAT].getChildAt(0).caretIndex,
                        len(actor[INP_GILDE_CHAT].getChildAt(0).text)
                    );
                    break;
                };
                i++;
            };
        };
    };

    SendChatMsg = function (evt:KeyboardEvent=None){
        var whisperCmd:* = None;
        var textToSend:* = None;
        var destR:* = 0;
        var destG:* = 0;
        var destB:* = 0;
        var req:* = None;
        var myFlt:* = None;
        var evt:* = evt;
        whisperCmd = "/whisper ";
        if (texts[TXT_WHISPER]){
            whisperCmd = (texts[TXT_WHISPER] + " ");
        };
        if (evt){
            trc("Keycode", KeyboardEvent(evt).keyCode);
            if (
                ((((!((KeyboardEvent(evt).keyCode == 13)))
                and (!((KeyboardEvent(evt).keyCode == 10)))))
                and (!((KeyboardEvent(evt).keyCode == 16777230))))
            ){
                return;
            };
        };
        lastChatLine = actor[INP_GILDE_CHAT].getChildAt(0).text;
        GildeChatScroll = 0;
        i = 0;
        while (i < 40) {
            var _local3 = actor[(LBL['GILDE']['CHAT'] + i)];
            with (_local3) {
                y = (GILDE_CHAT_Y + ((
                     (i - 35) + GildeChatScroll
                ) * GILDE_CHAT_Y));
                visible = (
                    ((i >= (35 - GildeChatScroll)))
                    and ((i < (40 - GildeChatScroll)))
                );
            };
            i++;
        };
        textToSend = RemoveIllegalChars(
            actor[INP_GILDE_CHAT].getChildAt(0).text
        );
        if (textToSend.length <= 0){
            return;
        };
        if (textToSend.lower() == "/level"){
            chat_line(("Average level of guild members: " + str(avgLevel)))
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower()[0: 5] == "/coa "){
            set_crest_str(textToSend[5:]);
            remove(GILDE_GEBAEUDE);
            add(GILDE_CREST);
            if (actor[GILDE_CREST].y == GILDE_GEBAEUDE_Y){
                set_alpha(GILDE_CREST_CONTROLS, 1);
                add(GILDE_CREST_CONTROLS);
            };
            load_crest();
            actor[INP_GILDE_CHAT].getChildAt(0).text = old_crest_str();
            actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                0, len(old_crest_str())
            );
            return;
        };
        if (textToSend.lower() == "/coa"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = old_crest_str();
            actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                0, len(old_crest_str())
            );
            return;
        };
        if (textToSend.lower() == "/delfights"){
            post_scroll = 1;
            fight_flush_mode = True;
            send_action(ACT_SCREEN_POST);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/test"){
            if ((len(actor[INP['NAME']].getChildAt(1).text) % 2) == 0){
                chat_line("Test successful!");
            } else {
                chat_line("Test failed!");
            };
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower()[0: 9] == "/apptest "){
            chat_line("Command unavailable in SWF mode.");
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/upload virus"){
            chat_line(''.join([
                "Error: Could not upload virus. ",
                "Please install backdoor first!"
            ]));
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/install backdoor"){
            chat_line(''.join([
                "Error: Could not install backdoor. ",
                "Please apply crack first!"
            ]));
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/apply crack"){
            chat_line(' '.join(
                "Error: Could not apply crack.",
                "Please generate master password first!"
            ));
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/generate master password"){
            chat_line(' '.join(
                "Error: Could not generate master password.",
                "Please hack gibson first!"
            ));
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/hack gibson"){
            chat_line(' '.join(
                "Error: Could not hack gibson.",
                "Please disable firewall first!"
            ));
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/disable firewall"){
            chat_line(' '.join(
                "Error: Could not disable firewall.",
                "Please upload virus first!"
            ));
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (
            (((textToSend.lower()[0: 4] == "/bg "))
            or ((textToSend.lower() == "/bg")))
        ){
            if (len(textToSend) == 10){
                destR = int(("0x" + textToSend[4: 2]));
                destG = int(("0x" + textToSend[6: 2]));
                destB = int(("0x" + textToSend[8: 2]));
                actor[GILDEN_BG].filters = [
                    new ColorMatrixFilter(
                        [0, 0, 0, 0, destR, 0, 0, 0, 0,
                            destG, 0, 0, 0, 0, destB, 0, 0, 0, 0, 0xFF
                        ]
                    )
                ];
                hide(GILDE_RAHMEN);
            } else {
                actor[GILDEN_BG].filters = list();
                show(GILDE_RAHMEN);
            };
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower()[0: 13] == "/cleandungeon"){
            if (len(textToSend) > 17){
                chat_line(' '.join(
                    "Error: Dungeon code too long.",
                    "Must be exactly 4 digits."
                ));
            } else {
                if (len(textToSend) == 17){
                    if (
                        actor[INP['NAME']].getChildAt(
                            1
                        ).text.lower() == "dream 25"
                    ){
                        chat_line(' '.join(
                            "Please stop leaking our top secret cheat",
                            "commands. Seriously."
                        );
                    } else {
                        chat_line(' '.join(
                            "Error: Dungeon already cleaned",
                            "by player 'dream 25'.",
                            "Please try another code."
                        ));
                    };
                } else {
                    if (len(textToSend) > 13){
                        chat_line(' '.join(
                            "Error: Dungeon code too short.",
                            "Must be exactly 4 digits."
                        ));
                    } else {
                        chat_line("Error: Dungeon code missing.");
                    };
                };
            };
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/act"){
            showActivityTime = !(showActivityTime);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line(
                ("/act mode is now " + ((showActivityTime) ? "on" : "off"))
            );
            return;
        };
        if (textToSend.lower() == "/album"){
            showAlbumOffset = !(showAlbumOffset);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line(
                ("/album mode is now " +
                 ((showAlbumOffset) ? "on" : "off"))
            );
            return;
        };
        if (textToSend.lower()[0: 6] == "/lang "){
            if (
                (((textToSend[6:] == ""))
                or ((textToSend[6:]) == original_lang_code)))
            ){
                so.data.lang_code = None;
            } else {
                so.data.lang_code = textToSend.substr[6:];
            };
            so.flush();
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line(
                (("Language code set to " + so.data.lang_code)
                + ". Requires reload.")
            );
            req = new URLRequest("index.php");
            navigate_to_url(req, "_self");
            return;
        };
        if (textToSend.lower() == "/sysblink off"){
            so.data.noPulseOnSysMsg = True;
            so.flush();
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("/sysblink mode is now off");
            return;
        };
        if (textToSend.lower() == "/sysblink on"){
            so.data.noPulseOnSysMsg = False;
            so.flush();
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("/sysblink mode is now on");
            return;
        };
        if (textToSend.lower() == "/powerplay"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("Nope damnit!");
            return;
        };
        if (textToSend.lower() == "/heybigspender"){
            FrenzyMode = !(FrenzyMode);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line(("Frenzy is now " + ((FrenzyMode) ? "on" : "off")));
            return;
        };
        if (textToSend.lower() == "/cheat"){
            i = 0;
            while (i < len(actor)) {
                myFlt = [new ColorMatrixFilter(
                    [random.random(),
                    random.random(), 0, 0, 0, 0,
                    random.random(), random.random(), 0, 0,
                    random.random(), 0, random.random(),
                    0, 0, 0, 0, 0,
                    ((random.random() * 0.5) + 0.5), 0]),
                    new BlurFilter((10 * random.random()),
                    (10 * random.random()), 1)
                    ];
                if ((actor[i] is DisplayObject)){
                    actor[i].filters = myFlt;
                    actor[i].scaleX = (
                        actor[i].scaleX * (1.1 - (random.random() * 0.2))
                    );
                    actor[i].scaleY = (
                        actor[i].scaleY * (1.1 - (random.random() * 0.2))
                    );
                    actor[i].x = (actor[i].x + (2 - (random.random() * 4)))
                    actor[i].y = (actor[i].y + (2 - (random.random() * 4)))
                };
                i++;
            };
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower() == "/pudo shroomster"){
            FrenzyMode = False;
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("Also nope.");
            return;
        };
        if (textToSend.lower() == "/frenzy"){
            FrenzyMode = False;
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("Nope.");
            return;
        };
        if (textToSend.lower() == "/steal"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            if (int(actor[LBL_GILDE_MUSH].text) > 0){
                actor[LBL_GILDE_MUSH].text = str(
                    (int(actor[LBL_GILDE_MUSH].text) - 1)
                );
                _local3 = actor[LBL_IF_PILZE];
                with (_local3) {
                    text = str((int(text) + 1));
                    x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
                };
                chat_line("1 mushroom stolen from guild!");
            } else {
                chat_line("No mushrooms to steal from guild!");
            };
            return;
        };
        if (textToSend.lower() == "/tvtest"){
            tvTest = True;
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("TV test");
            return;
        };
        if (textToSend.lower() == "/gid"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line(("Guild id: " + last_guild_data[0]));
            return;
        };
        if (textToSend.lower() == "/pid"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line(("Player id: " + savegame[SG['PLAYER_ID']]));
            return;
        };
        if (textToSend.lower() == "/pwdscore"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            gradePassword(
                None,
                actor[INP['LOGIN_PASSWORD']].getChildAt(1).text
            );
            return;
        };
        if (
            textToSend[
                0: (len(texts[TXT_CMD_DONATE_GOLD]) + 5)
            ].lower() == (texts[TXT_CMD_DONATE_GOLD].lower() + " ;-) ")
        ){
            PresetGold = int(textToSend.split(" ")[2]);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("ok");
            return;
        };
        if (
            textToSend[
                0] (len(texts[TXT_CMD_DONATE_MUSH]) + 5)
            ].lower() == (texts[TXT_CMD_DONATE_MUSH].lower() + " ;-) ")
        ){
            PresetMush = int(textToSend.split(" ")[2]);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("ok");
            return;
        };
        if (
            textToSend[
                0: (len(texts[TXT_CMD_DONATE_GOLD]) + 1)
            ].lower() == (texts[TXT_CMD_DONATE_GOLD].lower() + " ")
        ){
            if (textToSend.split(" ")[1] == "*"){
                if (
                    (int(actor[LBL_GILDE_GOLD].text)
                    + int((actor[LBL_IF_GOLD].text + "00"))) <= 10000000
                ){
                    send_action(
                        ACT_GUILD_DONATE,
                        1,
                        (actor[LBL_IF_GOLD].text + "00")
                    );
                } else {
                    error_message(texts[TXT_ERROR_GUILD_CASH_FULL]);
                };
            } else {
                if (int(textToSend.split(" ")[1]) != 0){
                    if (
                        (int(actor[LBL_GILDE_GOLD].text)
                        + int(textToSend.split(" ")[1])) <= 10000000
                    ){
                        send_action(
                            ACT_GUILD_DONATE,
                            1,
                            str((int(textToSend.split(" ")[1]) * 100))
                        );
                    } else {
                        error_message(texts[TXT_ERROR_GUILD_CASH_FULL]);
                    };
                };
            };
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (
            textToSend[
                0: (len(texts[TXT_CMD_DONATE_MUSH]) + 1)
            ].lower() == (texts[TXT_CMD_DONATE_MUSH].lower() + " ")
        ){
            if (noMush){
                chat_line(
                    ((texts[TXT_MUSH_DONATE_OBSOLETE])
                        ? texts[TXT_MUSH_DONATE_OBSOLETE]
                        : "Command is obsolete."
                    )
                );
                return;
            };
            send_action(ACT_GUILD_DONATE, 2, textToSend.split(" ")[1]);
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            return;
        };
        if (textToSend.lower()[0: 3] == "/w "){
            textToSend = textToSend[3:]
            if (textToSend.find(" ") != -1){
                last_whisper_target = textToSend[
                    0: textToSend.find(" ")
                ].split("#").join(" ");
                send_action(
                    ACT_WHISPER,
                    textToSend.[
                        0: textToSend.find(" ")
                    ].split("#").join(" "),
                    EncodeChat(
                        textToSend[(textToSend.find(" ") + 1):]
                    )
                );
                actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            } else {
                if (actor[INP_GILDE_CHAT].getChildAt(0).text[-1:] != " "){
                    actor[INP_GILDE_CHAT].getChildAt(0).text = (
                        actor[INP_GILDE_CHAT].getChildAt(0).text + " ");
                };
                len(actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                    actor[INP_GILDE_CHAT].getChildAt(0)),
                    actor[INP_GILDE_CHAT].getChildAt(0).length);
            };
            return;
        };
        if (textToSend.lower()[0: len(whisperCmd)] == whisperCmd){
            textToSend = textToSend[whisperCmd.length:]
            if (textToSend.find(" ") != -1){
                last_whisper_target = textToSend[0: textToSend.find(" ")]
                    .split("#").join(" ");
                send_action(ACT_WHISPER,
                            textToSend[0: textToSend.find(" ")]
                                .split("#").join(" "),
                            EncodeChat(textToSend.substr(
                                       (textToSend.find(" ") + 1))));
                actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            } else {
                if (actor[INP_GILDE_CHAT].getChildAt(0).text[-1:] != " "){
                    actor[INP_GILDE_CHAT].getChildAt(0).text = (
                        actor[INP_GILDE_CHAT].getChildAt(0).text + " ");
                };
                actor[INP_GILDE_CHAT].getChildAt(0).setSelection(
                    actor[INP_GILDE_CHAT].getChildAt(0).length,
                    actor[INP_GILDE_CHAT].getChildAt(0).length);
            };
            return;
        };
        if (textToSend[0: 1] == "/"){
            actor[INP_GILDE_CHAT].getChildAt(0).text = "";
            chat_line("Unknown command.");
            return;
        };
        textToSend = textToSend.split("/steal")
            .join((texts[TXT_CMD_DONATE_MUSH] + " 1"));
        send_action(ACT_SEND_CHAT, EncodeChat(textToSend), last_chat_index)
        actor[INP_GILDE_CHAT].getChildAt(0).text = "";
    };
    var EncodeChat:* = function (in_str:String):String{
        in_str = in_str.split("#").join("##");
        in_str = in_str.split("/").join("#{");
        in_str = in_str.split(";").join("#}");
        return (in_str);
    };
    nextSuggestionAllow = function (evt:TimerEvent){
        nextSuggestionTimer.stop();
        suggestionAllowed = True;
    };
    GildeBtnHandler = function (evt:Event=None){
        var i:* = 0;
        var evt:* = evt;
        Switch (get_actor_id(evt.target)){
            if case((GILDE_CREST_COLOR + 1):
            if case((GILDE_CREST_COLOR + 2):
            if case((GILDE_CREST_COLOR + 3):
                crestColorSelection = (get_actor_id(evt.target)
                                       - GILDE_CREST_COLOR);
                i = 1;
                while (i < crestColor.length) {
                    if (i == crestColorSelection){
                        show((GILDE_CREST_COLOR_SELECTED + i));
                    } else {
                        hide((GILDE_CREST_COLOR_SELECTED + i));
                    };
                    i = (i + 1);
                };
                load_crest();
                break;
            if case(GILDE_CREST_COLOR_PREV:
                crestSuggested = False;
                set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST]);
                var _local3 = crestColor;
                var _local4 = crestColorSelection;
                var _local5 = (_local3[_local4] - 1);
                _local3[_local4] = _local5;
                if (crestColor[crestColorSelection] < 0){
                    crestColor[crestColorSelection] = (
                               heraldicColors.length - 1);
                };
                load_crest();
                break;
            if case(GILDE_CREST_COLOR_NEXT:
                crestSuggested = False;
                set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST]);
                _local3 = crestColor;
                _local4 = crestColorSelection;
                _local5 = (_local3[_local4] + 1);
                _local3[_local4] = _local5;
                if (crestColor[crestColorSelection] >=
                        heraldicColors.length){
                    crestColor[crestColorSelection] = 0;
                };
                load_crest();
                break;
            if case(GILDE_CREST_CHANGE_PREV:
                crestSuggested = False;
                set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST]);
                _local3 = crest;
                _local4 = selecterCrestElement;
                _local5 = (_local3[_local4] - 1);
                _local3[_local4] = _local5;
                if (crest[selecterCrestElement] < 0){
                    crest[selecterCrestElement] = (
                        crestElementPos[selecterCrestElement][4] - 1);
                };
                load_crest();
                break;
            if case(GILDE_CREST_CHANGE_NEXT:
                crestSuggested = False;
                set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST]);
                _local3 = crest;
                _local4 = selecterCrestElement;
                _local5 = (_local3[_local4] + 1);
                _local3[_local4] = _local5;
                if (crest[selecterCrestElement] >= crestElementPos[
                        selecterCrestElement][4]){
                    crest[selecterCrestElement] = 0;
                };
                load_crest();
                break;
            if case(GILDE_CREST_OK:
                if ((((my_own_rank == 1)) and (crestSuggested))){
                    send_action(ACT_GUILD_SET_DESC,
                                actor[INP['NAME']].getChildAt(1).text,
                                gilde,
                                ((old_crest_str() + "§")
                                    + RemoveIllegalChars(SemiStrip(
                                    actor[INP_GILDE_TEXT].getChildAt(0)
                                    .text))),
                                MD5(actor[INP['LOGIN_PASSWORD']]
                                    .getChildAt(1).text));
                    old_crest_str = old_crest_str();
                } else {
                    if (suggestionAllowed){
                        nextSuggestionTimer.start();
                        suggestionAllowed = False;
                        if (my_own_rank == 1){
                            crestSuggested = True;
                            set_btn_text(GILDE_CREST_OK,
                                         texts[TXT_CREST_APPLY]);
                        };
                        send_action(ACT_SEND_CHAT,
                                    ("#?" + old_crest_str()),
                                    last_chat_index);
                    } else {
                        error_message(texts[TXT_ERROR_TOO_SOON_SUGGESTION])
                    };
                };
                break;
            if case(CLA_GILDE_CREST:
            if case((CLA_GILDE_CREST + 1):
            if case((CLA_GILDE_CREST + 2):
            if case((CLA_GILDE_CREST + 3):
            if case((CLA_GILDE_CREST + 4):
            if case((CLA_GILDE_CREST + 5):
            if case((CLA_GILDE_CREST + 6):
            if case((CLA_GILDE_CREST + 7):
            if case((CLA_GILDE_CREST + 8):
                if (last_guild_shown == gilde){
                    if (!on_stage(LBL_GILDE_CREST_ELEMENT)){
                        crestMoveDest = GILDE_GEBAEUDE_Y;
                        crestMoveTimer.start();
                        set_alpha(GILDE_CREST_CONTROLS, 0);
                        add(GILDE_CREST_CONTROLS);
                        fade_in(GILDE_CREST_CONTROLS);
                    };
                };
                selecterCrestElement = (get_actor_id(evt.target)
                                        - CLA_GILDE_CREST);
                i = 0;
                while (i < crestColor.length) {
                    if (i == crestColorSelection){
                        show((GILDE_CREST_COLOR_SELECTED + i));
                    } else {
                        hide((GILDE_CREST_COLOR_SELECTED + i));
                    };
                    load((GILDE_CREST_COLOR_UNSELECTED + i));
                    load((GILDE_CREST_COLOR_SELECTED + i));
                    load((GILDE_CREST_COLOR_FILLIN + i));
                    i = (i + 1);
                };
                load_crest();
                break;
            if case(GILDE_GEBAEUDE_GOTO_CREST:
                remove(GILDE_GEBAEUDE);
                add(GILDE_CREST);
                if (actor[GILDE_CREST].y == GILDE_GEBAEUDE_Y){
                    set_alpha(GILDE_CREST_CONTROLS, 1);
                    add(GILDE_CREST_CONTROLS);
                } else {
                    set_crest_str(old_crest_str);
                    selecterCrestElement = -1;
                };
                crestSuggested = False;
                set_btn_text(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST]);
                load_crest();
                break;
            if case(GILDE_CREST_GOTO_GEBAEUDE:
                set_crest_str(old_crest_str);
                selecterCrestElement = -1;
                remove(GILDE_CREST);
                remove(GILDE_CREST_CONTROLS);
                actor[GILDE_CREST].y = (GILDE_GEBAEUDE_Y + 60);
                add(GILDE_GEBAEUDE);
                break;
            if case(GILDE_RAID:
                if (my_own_attack_target == 0){
                    if (texts[TXT_GILDE_RAIDSTART]){
                        add(GILDE_DIALOG_RAID);
                        _local3 = actor[LBL_GILDE_DIALOG_TEXT_RAID];
                        with (_local3) {
                            wordWrap = True;
                            width = GILDE_TEXT2_X;
                            text = texts[TXT_GILDE_RAIDSTART]
                                .split("%1").join(texts[(TXT_DUNGEON_NAMES
                                + int(last_guild_data[GUILD_RAID_LEVEL]))])
                                .split("%2").join(str(lastRaidCost));
                        };
                        _local3 = actor[LBL_WINDOW_TITLE];
                        with (_local3) {
                            text = texts[TXT_GILDE_RAIDSTART_TITLE];
                            x = ((IF_WIN_X + IF_WIN_WELCOME_X)
                                 - int((text_width / 2)));
                        };
                    } else {
                        send_action(ACT_GUILD_COMMENCE_ATTACK, -1);
                    };
                } else {
                    send_action(ACT_GUILD_JOIN_ATTACK, "", "");
                };
                break;
            if case(GILDE_ATTACK:
                if (my_own_attack_target == 0){
                    if (last_guild_shown == gilde){
                        send_action(ACT_SCREEN_GILDENHALLE,
                                    "",
                                    savegame[SG_GUILD_INDEX],
                                    0);
                    } else {
                        send_action(ACT_GUILD_COMMENCE_ATTACK,
                                    last_guild_shown);
                    };
                } else {
                    send_action(ACT_GUILD_JOIN_ATTACK, "", "");
                };
                break;
            if case(GILDE_DEFEND:
                send_action(ACT_GUILD_JOIN_DEFENSE, "", "");
                break;
            if case(GILDE_CHAT_DOWN:
                GildeChatScroll--;
                if (GildeChatScroll < 0){
                    GildeChatScroll = 0;
                };
                break;
            if case(GILDE_CHAT_UP:
                GildeChatScroll++;
                if (GildeChatScroll > 35){
                    GildeChatScroll = 35;
                };
                while (actor[((LBL['GILDE']['CHAT'] + 35)
                       - GildeChatScroll)].text == "") {
                    GildeChatScroll--;
                    if (GildeChatScroll < 0){
                        GildeChatScroll = 0;
                        break;
                    };
                };
                break;
        };
        i = 0;
        while (i < 40) {
            _local3 = actor[(LBL['GILDE']['CHAT'] + i)];
            with (_local3) {
                y = (GILDE_CHAT_Y + (((i - 35) + GildeChatScroll)
                     * GILDE_CHAT_Y));
                visible = (((i >= (35 - GildeChatScroll)))
                           and ((i < (40 - GildeChatScroll))));
            };
            i = (i + 1);
        };
    };
    GildeGruenden = function (){
        var GildenName:String;
        GildenName = actor[INP_GILDE_GRUENDEN].getChildAt(1).text;
        if (GildenName == ""){
            error_message(texts[TXT_ERROR_EMPTY_GUILD_NAME]);
        } else {
            send_action(ACT_GUILD_FOUND,
                        actor[INP['NAME']].getChildAt(1).text,
                        actor[INP_GILDE_GRUENDEN].getChildAt(1).text,
                        MD5(actor[INP['LOGIN_PASSWORD']]
                            .getChildAt(1).text));
        };
    };
    var HutBtnDownHandler:* = function (evt:Event){
        var ClickCount:* = 0;
        var evt:* = evt;
        var DoPushHutBtn:* = function (timerevt:Event){
            var timerevt:* = timerevt;
            if (DestroyHutBtnTimer){
                DestroyHutBtnTimer = False;
                var _local3 = HutBtnRepeatTimer;
                with (_local3) {
                    stop();
                    delay = 1000;
                    remove_event_listener(TimerEvent.TIMER, DoPushHutBtn);
                };
            } else {
                ClickCount++;
                Switch (ClickCount){
                    if case(1:
                        HutBtnRepeatTimer.delay = 500;
                        break;
                    if case(3:
                        HutBtnRepeatTimer.delay = 250;
                        break;
                    if case(10:
                        HutBtnRepeatTimer.delay = 125;
                        break;
                    if case(20:
                        HutBtnRepeatTimer.delay = 62;
                        break;
                };
                if (HutBtnHandler(evt)){
                    play(SND['CLICK']);
                };
            };
        };
        ClickCount = 0;
        if (HutBtnRepeatTimer.running){
            return;
        };
        DestroyHutBtnTimer = False;
        var _local3 = HutBtnRepeatTimer;
        with (_local3) {
            delay = 1000;
            add_event_listener(TimerEvent.TIMER, DoPushHutBtn);
            start();
        };
    };
    var HutBtnUpHandler:* = function (evt:Event){
        if (HutBtnRepeatTimer.running){
            DestroyHutBtnTimer = True;
        };
    };
    HutFaceReset = function (evt:TimerEvent){
        if (on_stage(HUTMANN_BG)){
            add(HUTFACE_IDLE);
        };
    };
    HutBtnHandler = function (evt:Event=None):
        var evt:* = evt;
        var BetRisen:* = function (){
            if ((int(actor[LBL_HUTMANN_GOLDBET].text)
                    + int(actor[LBL_HUTMANN_MUSHBET].text)) > 0){
                set_btn_text(HUTMANN_OK, texts[TXT_HUTMANN_START]);
                add(HUTMANN_OK);
                if ((((int(actor[LBL_HUTMANN_GOLDBET].text) >= (
                        50 * int(GetSpendAmount()))))
                        or (int(actor[LBL_HUTMANN_MUSHBET].text) >= 20))):
                    actor[LBL_HUTMANN_TEXT].text = texts[
                        TXT_HUTMANN_BETCOMMENT3];
                    add(HUTFACE_LOSE3);
                } else {
                    if ((((int(actor[LBL_HUTMANN_GOLDBET].text) >= (
                            10 * int(GetSpendAmount()))))
                            or ((int(actor[LBL_HUTMANN_MUSHBET].text)
                                >= 10)))){
                        actor[LBL_HUTMANN_TEXT].text = texts[
                            TXT_HUTMANN_BETCOMMENT2];
                        add(HUTFACE_WIN);
                    } else {
                        actor[LBL_HUTMANN_TEXT].text = texts[
                            TXT_HUTMANN_BETCOMMENT1];
                        add(HUTFACE_WIN);
                    };
                };
                actor[LBL_HUTMANN_TEXT].x = (SCREEN_TITLE_X
                             - (actor[LBL_HUTMANN_TEXT].text_width / 2));
                HutFaceResetTimer.stop();
                HutFaceResetTimer.start();
            };
        };
        remove(HUTBECHER_1_CLICK, HUTBECHER_2_CLICK, HUTBECHER_3_CLICK);
        add_some(HUTBECHER_1_IDLE, HUTBECHER_2_IDLE, HUTBECHER_3_IDLE);
        Switch (get_actor_id(evt.target)){
            if case(HUTMANN_GOLDBET:
                if (int((int(savegame[SG_GOLD]) / 100))
                        > int(actor[LBL_HUTMANN_GOLDBET2].text)){
                    actor[LBL_HUTMANN_GOLDBET].text = str((int(
                          actor[LBL_HUTMANN_GOLDBET].text)
                            + int(actor[LBL_HUTMANN_GOLDBET2].text)));
                    BetRisen();
                } else {
                    var _local3 = actor[LBL_HUTMANN_TEXT];
                    with (_local3) {
                        text = texts[TXT_HUTMANN_CANTAFFORD];
                        x = (SCREEN_TITLE_X - (text_width / 2));
                    };
                    add(HUTFACE_LOSE2);
                    HutFaceResetTimer.stop();
                    HutFaceResetTimer.start();
                    if (HutBtnRepeatTimer.running){
                        DestroyHutBtnTimer = True;
                    };
                    return (False);
                };
                break;
            if case(HUTMANN_MUSHBET:
                if (int(savegame[SG_MUSH]) >
                        int(actor[LBL_HUTMANN_MUSHBET2].text)){
                    actor[LBL_HUTMANN_MUSHBET].text = str(
                      (int(actor[LBL_HUTMANN_MUSHBET].text)
                       + int(actor[LBL_HUTMANN_MUSHBET2].text)));
                    BetRisen();
                } else {
                    _local3 = actor[LBL_HUTMANN_TEXT];
                    with (_local3) {
                        text = texts[TXT_HUTMANN_CANTAFFORD];
                        x = (SCREEN_TITLE_X - (text_width / 2));
                    };
                    add(HUTFACE_LOSE2);
                    HutFaceResetTimer.stop();
                    HutFaceResetTimer.start();
                    if (HutBtnRepeatTimer.running){
                        DestroyHutBtnTimer = True;
                    };
                    return (False);
                };
                break;
            if case(HUTMANN_OK:
                if (((((int(actor[LBL_HUTMANN_GOLDBET].text)
                        + int(actor[LBL_HUTMANN_MUSHBET].text)) > 0))
                        and (on_stage(HUTMANN_GOLDBET)))){
                    remove(HUTMANN_OK, HUTMANN_PLACEBET);
                    add(HUTMANN_BECHERCHOOSE);
                    PlaceHutBet(True);
                    HutFaceResetTimer.stop();
                    _local3 = actor[LBL_HUTMANN_TEXT];
                    with (_local3) {
                        text = texts[TXT_HUTMANN_CHOOSECUP];
                        x = (SCREEN_TITLE_X - (text_width / 2));
                    };
                } else {
                    remove(HUTMANN_OK);
                    add(HUTMANN_PLACEBET);
                    if (int(savegame[SG_FIRST_PAYMENT]) == 0){
                        remove(HUTMANN_MUSHBET);
                    };
                    actor[LBL_HUTMANN_GOLDBET].text = "0";
                    actor[LBL_HUTMANN_MUSHBET].text = "0";
                    PlaceHutBet();
                    _local3 = actor[LBL_HUTMANN_TEXT];
                    with (_local3) {
                        text = texts[TXT_HUTMANN_NEWGAME];
                        x = (SCREEN_TITLE_X - (text_width / 2));
                    };
                };
                break;
        };
        return (True);
    };
    ChooseCup = function (evt:Event=None){
        remove(HUTMANN_BECHERCHOOSE);
        add(HUTFACE_HOVER);
        CupChosen = (get_actor_id(evt.target) - CA_HUTBECHER_1);
        send_action(ACT_PLACE_BET,
                    str((int(actor[LBL_HUTMANN_GOLDBET].text) * 100)),
                    actor[LBL_HUTMANN_MUSHBET].text);
    };
    var PlaceHutBet:* = function (LeftToCenter=False){
        var LeftBoxWidth:* = 0;
        var RightBoxWidth:* = 0;
        var LeftToCenter:Boolean = LeftToCenter;
        RightBoxWidth = ((((actor[HUTMANN_GOLDBET].width
                         + GILDE_GOLDMUSH_C1)
                        + actor[LBL_HUTMANN_GOLDBET2].text_width)
                        + GILDE_GOLDMUSH_C1)
                        + actor[HUTMANN_GOLDBET2].width);
        if (((((actor[HUTMANN_MUSHBET].width + GILDE_GOLDMUSH_C1)
                + actor[LBL_HUTMANN_MUSHBET2].text_width)
                + GILDE_GOLDMUSH_C1) + actor[HUTMANN_MUSHBET2].width) >
                RightBoxWidth){
            RightBoxWidth = ((((actor[HUTMANN_MUSHBET].width
                             + GILDE_GOLDMUSH_C1)
                            + actor[LBL_HUTMANN_MUSHBET2].text_width)
                            + GILDE_GOLDMUSH_C1)
                            + actor[HUTMANN_MUSHBET2].width);
        };
        actor[HUTMANN_GOLDBET].x = ((GILDE_GOLDMUSH_X + GILDE_GOLDMUSH_C2)
                                    - int((RightBoxWidth / 2)));
        actor[HUTMANN_MUSHBET].x = actor[HUTMANN_GOLDBET].x;
        actor[HUTMANN_MUSHBET_DISABLED].x = actor[HUTMANN_GOLDBET].x;
        actor[LBL_HUTMANN_GOLDBET2].x = ((actor[HUTMANN_GOLDBET].x
                                         + actor[HUTMANN_GOLDBET].width)
                                            + GILDE_GOLDMUSH_C1);
        actor[LBL_HUTMANN_MUSHBET2].x = ((actor[HUTMANN_MUSHBET].x
                                         + actor[HUTMANN_MUSHBET].width)
                                        + GILDE_GOLDMUSH_C1);
        actor[HUTMANN_GOLDBET2].x = ((actor[LBL_HUTMANN_GOLDBET2].x
                                     + actor[LBL_HUTMANN_GOLDBET2]
                                     .text_width)
                                    + GILDE_GOLDMUSH_C1);
        actor[HUTMANN_MUSHBET2].x = ((actor[LBL_HUTMANN_MUSHBET2].x
                            + actor[LBL_HUTMANN_MUSHBET2].text_width)
                            + GILDE_GOLDMUSH_C1);
        var _local3 = actor[LBL_HUTMANN_GOLDBET];
        with (_local3) {
            LeftBoxWidth = ((text_width + GILDE_GOLDMUSH_C1)
                            + actor[HUTMANN_GOLDBET].width);
        };
        _local3 = actor[LBL_HUTMANN_MUSHBET];
        with (_local3) {
            if (((text_width + GILDE_GOLDMUSH_C1)
                + actor[HUTMANN_MUSHBET].width) > LeftBoxWidth){
                LeftBoxWidth = ((text_width + GILDE_GOLDMUSH_C1)
                                + actor[HUTMANN_MUSHBET].width);
            };
            actor[HUTMANN_MUSHBET].x = ((LeftToCenter)
                                        ? SCREEN_TITLE_X
                                        : (GILDE_GOLDMUSH_X
                                           - int((LeftBoxWidth / 2))));
            actor[HUTMANN_GOLDBET].x = actor[HUTMANN_MUSHBET].x;
            actor[LBL_HUTMANN_GOLDBET].x = ((actor[HUTMANN_GOLDBET].x
                                            + actor[HUTMANN_GOLDBET].width)
                                            + GILDE_GOLDMUSH_C1);
            x = ((actor[HUTMANN_MUSHBET].x + actor[HUTMANN_MUSHBET].width)
                                        + GILDE_GOLDMUSH_C1);
        };
    };
    RequestToilet = function (evt:Event=None){
        send_action(ACT_SCREEN_TOILET);
    };
    ShowHutmann = function (evt:Event=None){
        var doShowHutmann:* = None;
        var evt:* = evt;
        doShowHutmann = function (){
            remove_all();
            var _local2 = actor[LBL_HUTMANN_TEXT];
            with (_local2) {
                text = texts[TXT_HUTMANN_OFFER];
                x = (SCREEN_TITLE_X - (text_width / 2));
            };
            if (PresetGold > int((int(savegame[SG_GOLD]) / 100))){
                PresetGold = int((int(savegame[SG_GOLD]) / 100));
            };
            if (PresetMush > int(savegame[SG_MUSH])){
                PresetMush = int(savegame[SG_MUSH]);
            };
            if (int(savegame[SG_FIRST_PAYMENT]) == 0){
                PresetMush = 0;
            };
            actor[LBL_HUTMANN_GOLDBET].text = str(PresetGold);
            actor[LBL_HUTMANN_MUSHBET].text = str(PresetMush);
            SetCnt(HUTMANN_GOLDBET, IF_GOLD);
            SetCnt(HUTMANN_GOLDBET2, IF_GOLD);
            SetCnt(HUTMANN_MUSHBET, IF_PILZE);
            SetCnt(HUTMANN_MUSHBET2, IF_PILZE);
            PlaceHutBet();
            add(SCREEN_HUTMANN);
            if ((((PresetGold > 0)) or ((PresetMush > 0)))){
                add(HUTMANN_OK);
            };
            PresetGold = 0;
            PresetMush = 0;
            if (int(savegame[SG_ACTION_STATUS]) != 0){
                remove(HUTMANN_BACK);
            };
            if (int(savegame[SG_FIRST_PAYMENT]) == 0){
                remove(HUTMANN_MUSHBET);
            };
        };
        load(SCREEN_HUTMANN);
        load(HUTBECHER_1_HOVER, HUTBECHER_1_HOVER, HUTBECHER_1_HOVER);
        actor[LBL_HUTMANN_GOLDBET2].text = GetSpendAmount();
        when_loaded(doShowHutmann);
    };
    BuyBeer = function (evt:Event=None){
        send_action(ACT_BUY_BEER);
    };
    ShowBeerOffer = function (evt:Event=None){
        var i:* = 0;
        var canBuy:* = False;
        var tooHealthy:* = False;
        var evt:* = evt;
        canBuy = (int(savegame[SG_BEERS]) < 10);
        if (savegame[((SG_INVENTORY_OFFS + (SG['ITM']['SIZE'] * 5))
                + SG_ITM_EXT_ENCHANT)] == 71){
            canBuy = (int(savegame[SG_BEERS]) < 11);
        };
        tooHealthy = False;
        special_actionHint = True;
        remove(TAVERNE_BARKEEPER_HINT);
        if (((canBuy) and ((int(savegame[SG_TIMEBAR]) > (80 * 60))))){
            canBuy = False;
            tooHealthy = True;
        };
        RefreshTimeBar(((canBuy) ? (20 * 60) : 0));
        remove(TAVERNE_CAS);
        add(BEEROFFER);
        enable_popup(QO_REWARDGOLD);
        enable_popup(QO_REWARDSILVER);
        enable_popup(LBL_QO_REWARDGOLD);
        enable_popup(LBL_QO_REWARDSILVER);
        enable_popup(LBL_QO_REWARDEXP);
        if (!texts[TXT_BEERFEST_TITLE_TOOHEALTHY]){
            texts[TXT_BEERFEST_TITLE_TOOHEALTHY] = "Beerfest!";
            texts[TXT_BEERFEST_TITLE_OK] = "Beerfest!";
            texts[TXT_BEERFEST_TEXT_TOOHEALTHY] = texts[
                TXT_BO_TEXT_TOOHEALTHY];
            texts[TXT_BEERFEST_TEXT_OK] = texts[TXT_BO_TEXT_OK];
        };
        var _local3 = actor[LBL_QO_QUESTNAME];
        with (_local3) {
            if (beer_fest){
                text = texts[((tooHealthy)
                              ? TXT_BEERFEST_TITLE_TOOHEALTHY
                              : ((canBuy)
                                 ? TXT_BEERFEST_TITLE_OK
                                 : TXT_BO_TITLE_NO))];
            } else {
                if (special_action > 0){
                    text = texts[((((canBuy) or (tooHealthy)))
                                  ? ((TXT_SPECIAL_ACTION_TITLE
                                     + special_action) - 1)
                                    : TXT_BO_TITLE_NO)];
                } else {
                    text = texts[((canBuy)
                                  ? TXT_BO_TITLE_OK
                                  : ((tooHealthy)
                                     ? TXT_BO_TITLE_TOOHEALTHY
                                     : TXT_BO_TITLE_NO))];
                };
            };
            x = ((QO_BLACK_SQUARE_X + QO_QUESTNAME_X)
                 - int((text_width / 2)));
        };
        _local3 = actor[LBL_QO_QUESTTEXT];
        with (_local3) {
            if (beer_fest){
                text = texts[((tooHealthy)
                              ? TXT_BEERFEST_TEXT_TOOHEALTHY
                              : ((canBuy)
                                 ? TXT_BEERFEST_TEXT_OK
                                 : TXT_BO_TEXT_NO))];
            } else {
                if (special_action > 0){
                    text = texts[((canBuy)
                      ? ((TXT_SPECIAL_ACTION_TEXT_OK + special_action) - 1)
                      : ((tooHealthy)
                         ? ((TXT_SPECIAL_ACTION_TEXT_TOOHEALTHY
                            + special_action) - 1)
                            : TXT_BO_TEXT_NO))];
                } else {
                    text = texts[((canBuy)
                                  ? TXT_BO_TEXT_OK
                                  : ((tooHealthy)
                                     ? TXT_BO_TEXT_TOOHEALTHY
                                     : TXT_BO_TEXT_NO))];
                };
            };
        };
        arabize(LBL_QO_QUESTTEXT);
        actor[LBL_QO_REWARDEXP].text = ((canBuy) ? texts[TXT_BO_TIME] : "")
        if (savegame[((SG_INVENTORY_OFFS
                + (SG['ITM']['SIZE'] * 5))
                + SG_ITM_EXT_ENCHANT)] == 71){
            if (text_dir == "right"){
                actor[LBL_QO_TIME].text = ((("11/" + savegame[SG_BEERS])
                                           + " ") + texts[TXT_BO_BOUGHT]);
            } else {
                actor[LBL_QO_TIME].text = (((texts[TXT_BO_BOUGHT] + " ")
                                           + savegame[SG_BEERS]) + "/11");
            };
        } else {
            if (text_dir == "right"){
                actor[LBL_QO_TIME].text = ((("10/" + savegame[SG_BEERS])
                                           + " ") + texts[TXT_BO_BOUGHT]);
            } else {
                actor[LBL_QO_TIME].text = (((texts[TXT_BO_BOUGHT] + " ")
                                           + savegame[SG_BEERS]) + "/10");
            };
        };
        if (beer_fest){
            set_btn_text(BO_BUY, texts[TXT_BO_BUY_FREE]);
        } else {
            set_btn_text(BO_BUY, texts[TXT_BO_BUY]);
        };
        if (!canBuy){
            remove(BO_BUY);
        };
        add(((canBuy) ? BO_PORTRAIT_OK : ((tooHealthy)
            ? BO_PORTRAIT_TH
            : BO_PORTRAIT_NO)));
    };
    TimeBarAniEvent = function (evt:Event=None){
        var evt:* = evt;
        if (on_stage(TIMEBAR_FILL)){
            TimeBarAniTimer.delay = 20;
            timeBarAni = (timeBarAni + 0.2);
            if (timeBarAni > (2 * math.pi)){
                timeBarAni = 0;
            };
            var _local3 = actor[TIMEBAR_FILL];
            with (_local3) {
                alpha = ((math.sin(timeBarAni) * 0.2) + 0.5);
            };
        } else {
            TimeBarAniTimer.delay = 500;
        };
    };
    ShowQuestOffer = function (evt:Event=None){
        var i;
        var enoughTime:Boolean;
        var highStakes:Boolean;
        i = 0;
        while (i < 3) {
            highStakes = False;
            Switch (math.abs(int(savegame[(SG_QUEST_OFFER_enemy1 + i)]))){
                if case(139:
                if case(145:
                if case(148:
                if case(152:
                if case(155:
                if case(157:
                    highStakes = True;
                    break;
            };
            enoughTime = (int(savegame[(SG_QUEST_OFFER_DURATION1 + i)]) <=
                          int(savegame[SG_TIMEBAR]));
            if (highStakes){
                if (enoughTime){
                    actor[(LBL_QO_CHOICE1 + i)].default_text_format =
                            FontFormat_HighStakes;
                    actor[(LBL_QO_CHOICE1_HL + i)].default_text_format =
                            FontFormat_HighStakesHighLight;
                } else {
                    actor[(LBL_QO_CHOICE1 + i)].default_text_format =
                            FontFormat_HighStakesGrayed;
                    actor[(LBL_QO_CHOICE1_HL + i)].default_text_format =
                            FontFormat_HighStakesHighLightGrayed;
                };
            } else {
                if (enoughTime){
                    actor[(LBL_QO_CHOICE1 + i)].default_text_format =
                            FontFormat_Default;
                    actor[(LBL_QO_CHOICE1_HL + i)].default_text_format =
                            FontFormat_Highlight;
                } else {
                    actor[(LBL_QO_CHOICE1 + i)].default_text_format =
                        FontFormat_Grayed;
                    actor[(LBL_QO_CHOICE1_HL + i)].default_text_format =
                        FontFormat_GrayedHighLight;
                };
            };
            actor[(LBL_QO_CHOICE1 + i)].text = get_quest_title(i);
            actor[(LBL_QO_CHOICE1_HL + i)].text = get_quest_title(i);
            hide((LBL_QO_CHOICE1_HL + i));
            if (text_dir == "right"){
                actor[LBL_QO_CHOOSE].x = (((QO_BLACK_SQUARE_X
                                          + QO_CHOOSE_X) + 140)
                                    - actor[LBL_QO_CHOOSE].text_width);
                actor[(QO_CHOICE1 + i)].x = (((QO_BLACK_SQUARE_X
                                             + QO_CHOOSE_X) + 140)
                                - actor[(LBL_QO_CHOICE1 + i)].text_width);
            };
            i++;
        };
        SelectQuestOffer(-1);
        remove(TAVERNE_CAS);
        add(QUESTOFFER);
        add((QO_PORTRAIT1 + get_quest_random(0, 5)));
    };
    ReturnQuest = function (evt:Event=None){
        actor[QUEST_SLOT].alpha = 1;
        force_adventure = False;
        add(TAVERNE_CAS);
        remove(QUESTOFFER);
        remove(BEEROFFER);
        RefreshTimeBar();
    };

    var ChooseQuest:* = function (evt:Event=None){
        var quest_id;
        quest_id = (get_actor_id(evt.target) - QO_CHOICE1);
        SelectQuestOffer(quest_id);
    };
    var SelectQuestOffer:* = function (quest_id){
        var i:* = 0;
        var rewardX:* = 0;
        var GoldBonusText:* = None;
        var quest_id:* = quest_id;
        SelectedQuest = quest_id;
        rewardX = ((QO_BLACK_SQUARE_X + QO_QUESTTEXT_X) +
                   (((text_dir == "right")) ? 130 : 0));
        GoldBonusText = "";
        if ((int(savegame[SG_GOLD_BONUS]) > 0)){
            GoldBonusText = (texts[TXT_GOLDBONUS_PREFIX] + " ");
            if ((int(savegame[SG_GOLD_BONUS]) > 0)){
                GoldBonusText = (((GoldBonusText + savegame[SG_GOLD_BONUS])
                                 + "% ") + texts[TXT_GOLDBONUS_SUFFIX]);
                if (tower_level > 0){
                    GoldBonusText = ((((GoldBonusText + " + ")
                                     + str(tower_level)) + "% ")
                                    + texts[TXT_TOWER_BONUS]);
                };
            };
        };
        i = 0;
        while (i < 3) {
            actor[(LBL_QO_CHOICE1_HL + i)].visible = (i == quest_id);
            actor[(LBL_QO_CHOICE1 + i)].visible = !((i == quest_id));
            i = (i + 1);
        };
        var _local3 = actor[LBL_QO_QUESTNAME];
        with (_local3) {
            text = ((quest_id)==-1)
                ? texts[(TXT_QUEST_OFFER_TITLE + get_quest_random(0, 5))]
                : get_quest_title(quest_id);
            x = ((QO_BLACK_SQUARE_X + QO_QUESTNAME_X)
                 - int((text_width / 2)));
        };
        actor[LBL_QO_QUESTTEXT].text = ((quest_id)==-1)
                ? texts[(TXT_QUEST_OFFER_TEXT + get_quest_random(0, 5))]
                : get_quest_text(quest_id);
        arabize(LBL_QO_QUESTTEXT);
        if (quest_id == -1){
            hide(QO_REWARDGOLD,
                 LBL_QO_REWARDGOLD,
                 QO_REWARDSILVER,
                 LBL_QO_REWARDSILVER);
            hide(LBL_QO_REWARD);
            hide(QO_START);
            actor[LBL_QO_REWARDEXP].text = "";
            actor[LBL_QO_TIME].text = "";
            SetCnt(QUEST_SLOT, C_EMPTY);
            enable_popup(FIGHT_SLOT);
        } else {
            show(LBL_QO_REWARD);
            show(QO_START);
            hide(QO_REWARDGOLD,
                 LBL_QO_REWARDGOLD,
                 QO_REWARDSILVER,
                 LBL_QO_REWARDSILVER);
            if (text_dir == "right"){
                actor[LBL_QO_REWARD].x = (rewardX
                                        - actor[LBL_QO_REWARD].text_width);
            };
            if (gold_anteil(savegame[(SG_QUEST_OFFER_GOLD1
                    + quest_id)]) > 0){
                _local3 = actor[QO_REWARDGOLD];
                with (_local3) {
                    visible = True;
                    if (text_dir == "right"){
                        x = (rewardX - width);
                        rewardX = (x - 8);
                    } else {
                        x = rewardX;
                        rewardX = ((x + width) + 8);
                    };
                };
                _local3 = actor[LBL_QO_REWARDGOLD];
                with (_local3) {
                    visible = True;
                    text = gold_anteil(savegame[(SG_QUEST_OFFER_GOLD1
                                       + quest_id)]);
                    if (text_dir == "right"){
                        x = (rewardX - text_width);
                        rewardX = (x - 8);
                    } else {
                        x = rewardX;
                        rewardX = ((x + text_width) + 14);
                    };
                };
            };
            if (silber_anteil(savegame[(SG_QUEST_OFFER_GOLD1
                + quest_id)]) > 0){
                _local3 = actor[QO_REWARDSILVER];
                with (_local3) {
                    visible = True;
                    if (text_dir == "right"){
                        x = (rewardX - width);
                        rewardX = (x - 8);
                    } else {
                        x = rewardX;
                        rewardX = ((x + width) + 8);
                    };
                };
                _local3 = actor[LBL_QO_REWARDSILVER];
                with (_local3) {
                    visible = True;
                    text = silber_anteil(savegame[(SG_QUEST_OFFER_GOLD1
                                         + quest_id)]);
                    if (text_dir == "right"){
                        x = (rewardX - text_width);
                        rewardX = (x - 8);
                    } else {
                        x = rewardX;
                        rewardX = ((x + text_width) + 14);
                    };
                };
            };
            if (text_dir == "right"){
                actor[LBL_QO_REWARDEXP].text = ((savegame[(
                        SG_QUEST_OFFER_EXP1 + quest_id)] + " :")
                        + texts[TXT_EXP]);
                actor[LBL_QO_REWARDEXP].x = (((QO_BLACK_SQUARE_X
                                             + QO_QUESTTEXT_X) + 130)
                                    - actor[LBL_QO_REWARDEXP].text_width);
            } else {
                actor[LBL_QO_REWARDEXP].text = ((texts[TXT_EXP] + ": ")
                            + savegame[(SG_QUEST_OFFER_EXP1 + quest_id)]);
            };
            if (int(savegame[SG_EXP_BONUS]) > 0){
                if (math.round((((savegame[SG_ALBUM] - 10000) / contentMax)
                        * 100)) >= 1){
                    enable_popup(LBL_QO_REWARDEXP,
                                 ((((((((texts[TXT_EXPBONUS_PREFIX] + " ")
                                  + savegame[SG_EXP_BONUS]) + "% ")
                                    + texts[TXT_EXPBONUS_SUFFIX]) + " + ")
                                    + str(math.round((((savegame[SG_ALBUM]
                                          - 10000) / contentMax) * 100))))
                                + "% ") + texts[(TXT_COLLECTION + 1)]));
                } else {
                    enable_popup(LBL_QO_REWARDEXP,
                                 ((((texts[TXT_EXPBONUS_PREFIX] + " ")
                                  + savegame[SG_EXP_BONUS]) + "% ")
                                    + texts[TXT_EXPBONUS_SUFFIX]));
                };
            } else {
                if (math.round((((savegame[SG_ALBUM] - 10000) / contentMax)
                    * 100)) >= 1){
                    enable_popup(LBL_QO_REWARDEXP,
                                 ((((texts[TXT_EXPBONUS_PREFIX] + " ")
                                  + str(math.round((((savegame[SG_ALBUM]
                                        - 10000) / contentMax) * 100))))
                                    + "% ") + texts[(TXT_COLLECTION + 1)]))
                } else {
                    enable_popup(LBL_QO_REWARDEXP);
                };
            };
            if (GoldBonusText != ""){
                enable_popup(QO_REWARDGOLD, GoldBonusText);
                enable_popup(QO_REWARDSILVER, GoldBonusText);
                enable_popup(LBL_QO_REWARDGOLD, GoldBonusText);
                enable_popup(LBL_QO_REWARDSILVER, GoldBonusText);
            } else {
                enable_popup(QO_REWARDGOLD);
                enable_popup(QO_REWARDSILVER);
                enable_popup(LBL_QO_REWARDGOLD);
                enable_popup(LBL_QO_REWARDSILVER);
            };
            if (int(savegame[((SG['QUEST']['OFFER']['REWARD_ITM1']
                    + (quest_id * SG['ITM']['SIZE'])) + SG_ITM_TYP)]) > 0){
                SetCnt(QUEST_SLOT,
                       GetItemID(SG['QUEST']['OFFER']['REWARD_ITM1'],
                                 quest_id));
                item_popup(QUEST_SLOT,
                          (SG['QUEST']['OFFER']['REWARD_ITM1']
                           + (quest_id * SG['ITM']['SIZE'])),
                            None, False, False, False);
            } else {
                SetCnt(QUEST_SLOT, C_EMPTY);
                enable_popup(FIGHT_SLOT);
            };
            if (text_dir == "right"){
                actor[LBL_QO_TIME].text = (((((str(int((int(savegame[
                                           (SG_QUEST_OFFER_DURATION1
                                            + quest_id)]) / 60))) + ":")
                        + (((str(int((int(
                           savegame[(SG_QUEST_OFFER_DURATION1
                           + quest_id)]) % 60))).length == 1)) ? "0" : ""))
                        + str(int((int(savegame[(SG_QUEST_OFFER_DURATION1
                              + quest_id)]) % 60)))) + " :") +
                        texts[TXT_DURATION]);
                actor[LBL_QO_TIME].x = (QO_BLACK_SQUARE_X + QO_QUESTTEXT_X)
                    + 130) - actor[LBL_QO_TIME].text_width);
            } else {
                actor[LBL_QO_TIME].text = (((((texts[TXT_DURATION] + ": ")
                       + str(int((int(savegame[(SG_QUEST_OFFER_DURATION1
                         + quest_id)]) / 60)))) + ":")
                    + (((str(int((int(savegame[(SG_QUEST_OFFER_DURATION1
                       + quest_id)]) % 60))).length == 1)) ? "0" : ""))
                    + str(int((int(savegame[(SG_QUEST_OFFER_DURATION1
                          + quest_id)]) % 60))));
            };
            RefreshTimeBar(-(int(savegame[(SG_QUEST_OFFER_DURATION1
                           + quest_id)])));
        };
    };
    RequestQuest = function (evt:Event=None){
        if (SelectedQuest >= 0){
            send_action(ACT_QUEST_BEGIN,
                        (SelectedQuest + 1),
                        ((force_adventure) ? 1 : 0));
        };
    };
    toiletChainAni = function (evt:TimerEvent){
        var i;
        if (toiletChainFrame >= 6){
            toiletChainTimer.stop();
            return;
        };
        i = 0;
        while (i < 3) {
            hide((TOILET_CHAIN + i));
            i++;
        };
        if (toiletChainFrame <= 2){
            show((TOILET_CHAIN + toiletChainFrame));
        } else {
            show(((TOILET_CHAIN + 5) - toiletChainFrame));
        };
        toiletChainFrame++;
    };
    ToiletHandler = function (evt:Event=None){
        if (get_actor_id(evt.target) == CA_TOILET_CHAIN){
            toiletChainFrame = 0;
            toiletChainTimer.start();
            play(SND_TOILET_FLUSHTRY);
            send_action(ACT_TOILET_FLUSH);
        };
    };
    SkipFight = function (evt:Event=None){
    };
    CheckLM = function (evt:Event=None){
        var req:URLRequest;
        add(CB_LM_CHECKED);
        light_mode = True;
        so.data.light_mode = light_mode;
        so.flush();
        if (param_lowres_url != ""){
            req = new URLRequest("index.php");
            navigate_to_url(req, "_self");
        };
    };
    UncheckLM = function (evt:Event=None){
        var req:URLRequest;
        remove(CB_LM_CHECKED);
        light_mode = False;
        so.data.light_mode = light_mode;
        so.flush();
        if (param_lowres_url != ""){
            req = new URLRequest("index.php");
            navigate_to_url(req, "_self");
        };
    };
    CheckCS = function (evt:Event=None){
        add(CB_CS_CHECKED);
        chat_sound = True;
        so.data.chat_sound = chat_sound;
        so.flush();
        play(SND_ERROR);
    };
    UncheckCS = function (evt:Event=None){
        remove(CB_CS_CHECKED);
        chat_sound = False;
        so.data.chat_sound = chat_sound;
        so.flush();
    };
    CheckCompare = function (evt:Event=None){
        add(CB_COMPARE_CHECKED);
        compare_items = True;
        so.data.compare_items = compare_items;
        so.flush();
    };
    UncheckCompare = function (evt:Event=None){
        remove(CB_COMPARE_CHECKED);
        compare_items = False;
        so.data.compare_items = compare_items;
        so.flush();
    };
    CheckTV = function (evt:Event=None){
        add(CB_TV_CHECKED);
        disable_tv = True;
        so.data.disable_tv = disable_tv;
        so.flush();
    };
    UncheckTV = function (evt:Event=None){
        remove(CB_TV_CHECKED);
        disable_tv = False;
        so.data.disable_tv = disable_tv;
        so.flush();
    };
    VolumeChange = function (value):
        var value:* = value;
        if (notFirstVolChange){
            notFirstVolChange = False;
            if (so.data.volume is None){
                so.data.volume = 5;
            };
            so.flush();
            set_volume((so.data.volume / 10));
            SetSliderValue(SLDR_OPTION_VOLUME, (so.data.volume + 1));
        } else {
            so.data.volume = (value - 1);
            so.flush();
            set_volume((so.data.volume / 10));
            if (notSecondVolChange){
                notSecondVolChange = False;
            } else {
                play(SND_TEST);
            };
        };
        var _local3 = actor[LBL_OPTION_VOLUME];
        with (_local3) {
            if (text_dir == "right"){
                text = (((so.data.volume == 0))
                        ? texts[TXT_MUTE]
                        : ((str((so.data.volume * 10)) + "% ")
                           + texts[TXT_VOLUME]));
            } else {
                text = (((so.data.volume == 0))
                        ? texts[TXT_MUTE]
                        : (((texts[TXT_VOLUME] + " ")
                           + str((so.data.volume * 10))) + "%"));
            };
            x = (((OPTION_X + 250) + int((OPTION_X / 2)))
                 - int((text_width / 2)));
        };
    };
    ChooseLanguageIcon = function (evt:MouseEvent){
        var req:URLRequest;
        so.data.lang_code = param_languages[(get_actor_id(evt.target)
                                             - OPTION_FLAG)];
        so.flush();
        trc("Language set:", so.data.lang_code);
        req = new URLRequest("index.php");
        navigate_to_url(req, "_self");
    };
    OptionBtnHandler = function (evt:Event){
        hide(CHANGE_PASSWORD_SMILEY_SAD);
        hide(CHANGE_PASSWORD_SMILEY_NEUTRAL);
        hide(CHANGE_PASSWORD_SMILEY_HAPPY);
        if ((evt is KeyboardEvent)){
            if (((((!((KeyboardEvent(evt).keyCode == 13)))
                    and (!((KeyboardEvent(evt).keyCode == 10)))))
                    and (!((KeyboardEvent(evt).keyCode == 16777230))))){
                return;
            };
        };
        remove(LUXURY_SELLER);
        Switch (get_actor_id(evt.target)){
            if case(OPTION_LUXURY:
                remove(OPTION_DOCHANGE);
                optionMenuSelect = 6;
                actor[LBL_OPTION_DOCHANGE].text = texts[TXT_LUXURY_TITLE];
                actor[LBL_OPTION_FIELD1].text = texts[TXT_LUXURY_TEXT];
                set_btn_text(OPTION_DOCHANGE, texts[TXT_LUXURY_BTN]);
                add(OPTION_DORESEND);
                add(LUXURY_SELLER);
                if ((uint(savegame[SG_NEW_FLAGS]) & 32)){
                    actor[LBL_OPTION_FIELD1].text = texts[
                        TXT_LUXURY_ALREADY];
                    remove(OPTION_DOCHANGE);
                };
                arabize(LBL_OPTION_FIELD1);
                break;
            if case(OPTION_CHANGE_NAME:
                optionMenuSelect = 1;
                actor[LBL_OPTION_DOCHANGE].text = texts[
                    TXT_DOCHANGE_NAME_TITLE];
                actor[LBL_OPTION_FIELD1].text = texts[
                    TXT_DOCHANGE_NAME_FIELD_1];
                actor[LBL_OPTION_FIELD2].text = texts[
                    TXT_DOCHANGE_NAME_FIELD_2];
                actor[LBL_OPTION_FIELD3].text = texts[
                    TXT_DOCHANGE_NAME_FIELD_3];
                set_btn_text(OPTION_DOCHANGE, texts[TXT_DOCHANGENAME]);
                actor[INP_OPTION_FIELD1].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD2].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD3].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD1].getChildAt(1)
                    .displayAsPassword = True;
                actor[INP_OPTION_FIELD2].getChildAt(1)
                    .displayAsPassword = False;
                actor[INP_OPTION_FIELD3].getChildAt(1)
                    .displayAsPassword = False;
                add(OPTION_DOCHANGE);
                break;
            if case(OPTION_CHANGE_EMAIL:
                optionMenuSelect = 2;
                actor[LBL_OPTION_DOCHANGE].text = texts[
                    TXT_DOCHANGE_EMAIL_TITLE];
                actor[LBL_OPTION_FIELD1].text = texts[
                    TXT_DOCHANGE_EMAIL_FIELD_1];
                if (savegame[SG_EMAIL_VALID] == 1){
                    actor[LBL_OPTION_FIELD2].text = ((texts[TXT_OLD_EMAIL])
                                                     ? texts[TXT_OLD_EMAIL]
                                                     : "Old E-Mail:");
                    actor[LBL_OPTION_FIELD3].text = texts[
                        TXT_DOCHANGE_EMAIL_FIELD_2];
                } else {
                    actor[LBL_OPTION_FIELD2].text = texts[
                        TXT_DOCHANGE_EMAIL_FIELD_2];
                    actor[LBL_OPTION_FIELD3].text = texts[
                        TXT_DOCHANGE_EMAIL_FIELD_3];
                };
                set_btn_text(OPTION_DOCHANGE, texts[TXT_DOCHANGE]);
                actor[INP_OPTION_FIELD1].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD2].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD3].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD1].getChildAt(1)
                    .displayAsPassword = True;
                actor[INP_OPTION_FIELD2].getChildAt(1)
                    .displayAsPassword = False;
                actor[INP_OPTION_FIELD3].getChildAt(1)
                    .displayAsPassword = False;
                add(OPTION_DOCHANGE);
                break;
            if case(OPTION_CHANGE_PASSWORD:
                optionMenuSelect = 3;
                actor[LBL_OPTION_DOCHANGE].text = texts[
                    TXT_DOCHANGE_PASSWORD_TITLE];
                actor[LBL_OPTION_FIELD1].text = texts[
                    TXT_DOCHANGE_PASSWORD_FIELD_1];
                actor[LBL_OPTION_FIELD2].text = texts[
                    TXT_DOCHANGE_PASSWORD_FIELD_2];
                actor[LBL_OPTION_FIELD3].text = texts[
                    TXT_DOCHANGE_PASSWORD_FIELD_3];
                set_btn_text(OPTION_DOCHANGE, texts[TXT_DOCHANGE]);
                actor[INP_OPTION_FIELD1].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD2].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD3].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD1].getChildAt(1)
                    .displayAsPassword = True;
                actor[INP_OPTION_FIELD2].getChildAt(1)
                    .displayAsPassword = True;
                actor[INP_OPTION_FIELD3].getChildAt(1)
                    .displayAsPassword = True;
                add(OPTION_DOCHANGE);
                break;
            if case(OPTION_DELETE:
                optionMenuSelect = 4;
                actor[LBL_OPTION_DOCHANGE].text = texts[
                    TXT_DELETE_ACCOUNT_TITLE];
                actor[LBL_OPTION_FIELD1].text = texts[
                    TXT_DELETE_ACCOUNT_FIELD_1];
                actor[LBL_OPTION_FIELD2].text = texts[
                    TXT_DELETE_ACCOUNT_FIELD_2];
                actor[LBL_OPTION_FIELD3].text = texts[
                    TXT_DELETE_ACCOUNT_FIELD_3];
                set_btn_text(OPTION_DOCHANGE, texts[TXT_DOCHANGE]);
                actor[INP_OPTION_FIELD1].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD2].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD3].getChildAt(1).text = "";
                actor[INP_OPTION_FIELD1].getChildAt(1)
                    .displayAsPassword = True;
                actor[INP_OPTION_FIELD2].getChildAt(1)
                    .displayAsPassword = True;
                actor[INP_OPTION_FIELD3].getChildAt(1)
                    .displayAsPassword = False;
                add(OPTION_DOCHANGE);
                break;
            if case(OPTION_RESEND:
                remove(OPTION_DOCHANGE);
                optionMenuSelect = 5;
                actor[LBL_OPTION_DOCHANGE].text = texts[TXT_RESEND_TITLE];
                actor[LBL_OPTION_FIELD1].text = texts[TXT_RESEND_TEXT];
                set_btn_text(OPTION_DOCHANGE, texts[TXT_RESEND_BTN2]);
                add(OPTION_DORESEND);
                if (int(savegame[SG_EMAIL_VALID]) == 1){
                    actor[LBL_OPTION_FIELD1].text = texts[
                        TXT_ALREADY_VALID];
                    remove(OPTION_DOCHANGE);
                };
                arabize(LBL_OPTION_FIELD1);
                break;
            if case(OPTION_CHANGEIMG:
                show_build_character_screen(evt);
                break;
            default:
                Switch (optionMenuSelect){
                    if case(1:
                        if (actor[INP_OPTION_FIELD2].getChildAt(1).text ==
                                actor[INP_OPTION_FIELD3]
                                .getChildAt(1).text){
                            send_action(ACT_CHANGE_NAME,
                                   actor[INP['NAME']].getChildAt(1).text,
                               actor[INP_OPTION_FIELD1].getChildAt(1).text,
                               actor[INP_OPTION_FIELD2].getChildAt(1).text,
                               actor[INP_OPTION_FIELD3].getChildAt(1).text)
                            option_new_data = actor[
                                INP_OPTION_FIELD2].getChildAt(1).text;
                        } else {
                            error_message(texts[TXT_ERROR_NAME_MISMATCH]);
                        };
                        break;
                    if case(2:
                        if ((((actor[INP_OPTION_FIELD2]
                                .getChildAt(1).text == actor[
                                INP_OPTION_FIELD3].getChildAt(1).text))
                                or ((savegame[SG_EMAIL_VALID] == 1)))){
                            send_action(ACT_CHANGE_MAIL,
                               actor[INP['NAME']].getChildAt(1).text,
                               actor[INP_OPTION_FIELD1].getChildAt(1).text,
                               actor[INP_OPTION_FIELD2].getChildAt(1).text,
                               actor[INP_OPTION_FIELD3].getChildAt(1).text)
                            option_new_data = actor[INP_OPTION_FIELD2]
                                .getChildAt(1).text;
                        } else {
                            error_message(texts[TXT_ERROR_EMAIL_MISMATCH]);
                        };
                        break;
                    if case(3:
                        if (actor[INP_OPTION_FIELD2].getChildAt(1).text ==
                            actor[INP_OPTION_FIELD3].getChildAt(1).text){
                            send_action(ACT_CHANGE_PASS,
                               actor[INP['NAME']].getChildAt(1).text,
                               actor[INP_OPTION_FIELD1].getChildAt(1).text,
                               actor[INP_OPTION_FIELD2].getChildAt(1).text,
                               actor[INP_OPTION_FIELD3].getChildAt(1).text)
                            option_new_data = actor[
                                INP_OPTION_FIELD2].getChildAt(1).text;
                        } else {
                            error_message(
                                  texts[TXT_ERROR_PASSWORD_MISMATCH]);
                        };
                        break;
                    if case(4:
                        if (actor[INP_OPTION_FIELD1].getChildAt(1).text ==
                            actor[INP_OPTION_FIELD2].getChildAt(1).text){
                            send_action(ACT_DELETE_ACCOUNT,
                               actor[INP['NAME']].getChildAt(1).text,
                               actor[INP_OPTION_FIELD1].getChildAt(1).text,
                               actor[INP_OPTION_FIELD3].getChildAt(1)
                                .text.lower());
                        } else {
                            error_message(
                                  texts[TXT_ERROR_PASSWORD_MISMATCH]);
                        };
                        break;
                    if case(5:
                        ResendConfirmationEmail();
                        break;
                    if case(6:
                        remove(OPTION_DOCHANGE);
                        optionMenuSelect = 7;
                        actor[LBL_OPTION_DOCHANGE].text = texts[
                            TXT_LUXURY_TITLE];
                        actor[LBL_OPTION_FIELD1].text = texts[
                            TXT_LUXURY_CONFIRM];
                        set_btn_text(OPTION_DOCHANGE,
                                     texts[TXT_LUXURY_BTN2]);
                        add(OPTION_DORESEND);
                        add(LUXURY_SELLER);
                        arabize(LBL_OPTION_FIELD1);
                        break;
                    if case(7:
                        remove(OPTION_DOCHANGE);
                        optionMenuSelect = 8;
                        actor[LBL_OPTION_DOCHANGE].text = texts[
                            TXT_LUXURY_TITLE];
                        actor[LBL_OPTION_FIELD1].text = texts[
                            TXT_LUXURY_CONFIRM2];
                        set_btn_text(OPTION_DOCHANGE, texts[
                                     TXT_LUXURY_BTN3]);
                        add(OPTION_DORESEND);
                        add(LUXURY_SELLER);
                        arabize(LBL_OPTION_FIELD1);
                        break;
                    if case(8:
                        send_action(ACT_BUY_LUXURY);
                        break;
                };
                break;
            if case(OPTION_CHANGEIMG:
        };
        if (text_dir == "right"){
            actor[LBL_OPTION_DOCHANGE].x = ((OPTION_X + OPTION_VER_X)
                                - actor[LBL_OPTION_DOCHANGE].text_width);
            actor[LBL_OPTION_FIELD1].width = 385;
            actor[LBL_OPTION_FIELD2].x = ((OPTION_X + OPTION_VER_X)
                                  - actor[LBL_OPTION_FIELD2].text_width);
            actor[LBL_OPTION_FIELD3].x = ((OPTION_X + OPTION_VER_X)
                                  - actor[LBL_OPTION_FIELD3].text_width);
            actor[INP_OPTION_FIELD1].x = (OPTION_X
                                          + OPTION_DOCHANGE_LABEL_X);
            actor[INP_OPTION_FIELD2].x = (OPTION_X
                                          + OPTION_DOCHANGE_LABEL_X);
            actor[INP_OPTION_FIELD3].x = (OPTION_X
                                          + OPTION_DOCHANGE_LABEL_X);
        };
    };
    RequestMainQuest = function (evt:Event=None){
        var evt:* = evt;
        if (waiting_for(savegame[SG_MQ_REROLL_TIME])){
            if (int(actor[LBL_IF_PILZE].text) <= 0){
                return;
            };
            var _local3 = actor[LBL_IF_PILZE];
            with (_local3) {
                text = str((int(savegame[SG_MUSH]) - 1));
                x = ((IF_LBL_GOLDPILZE_X - text_width) - 10);
            };
        };
        enable_popup(LBL_IF_PILZE);
        if (SelectedDungeon == 100){
            send_action(ACT_TOWER_TRY,
                        str((tower_level + 1)),
                        ((waiting_for(savegame[SG_MQ_REROLL_TIME]))
                         ? 1 : 0));
        } else {
            send_action(ACT_MAINQUEST, str((SelectedDungeon + 1)));
        };
    };
    var ResendConfirmationEmail:* = function (evt:Event=None){
        send_action(ACT_RESEND_EMAIL);
    };
    attPriceLimitation = False;
    GoldKurve = list();
    TrueAttPreis = list();
    GoldKurve[1] = 25;
    GoldKurve[2] = 50;
    GoldKurve[3] = 75;
    i = 4;
    while (i <= 15000) {
        GoldKurve[i] = ((int(GoldKurve[(i - 1)])
                        + int((GoldKurve[int((i / 2))] / 3)))
                        + int((GoldKurve[int((i / 3))] / 4)));
        GoldKurve[i] = int((GoldKurve[i] / 5));
        GoldKurve[i] = (GoldKurve[i] * 5);
        i = (i + 1);
    };
    i = 0;
    while (i <= 15000) {
        TrueAttPreis[i] = GoldKurve[int((1 + (i / 5)))];
        i = (i + 1);
    };
    i = 0;
    while (i <= 14996) {
        if (attPriceLimitation){
            TrueAttPreis[i] = 0x3B9ACA00;
        } else {
            TrueAttPreis[i] = ((((int(TrueAttPreis[i])
                               + int(TrueAttPreis[(i + 1)]))
                                + int(TrueAttPreis[(i + 2)]))
                                + int(TrueAttPreis[(i + 3)]))
                                + int(TrueAttPreis[(i + 4)]));
            TrueAttPreis[i] = int((TrueAttPreis[i] / 5));
            TrueAttPreis[i] = int((TrueAttPreis[i] / 5));
            TrueAttPreis[i] = int((TrueAttPreis[i] * 5));
            if (TrueAttPreis[i] > 0x3B9ACA00){
                TrueAttPreis[i] = 0x3B9ACA00;
                attPriceLimitation = True;
            };
        };
        i = (i + 1);
    };
    i = 1;
    while (i <= 200) {
        GildeBuildingGold[i] = int((GoldKurve[(i * 2)] * 10));
        GildeBuildingGold[i] = (GildeBuildingGold[i] / 100);
        GildeBuildingGold[i] = int(GildeBuildingGold[i]);
        GildeBuildingGold[i] = (GildeBuildingGold[i] * 100);
        if (GildeBuildingGold[i] < 100){
            GildeBuildingGold[i] = 100;
        };
        if (i > 50){
            GildeBuildingGold[i] = (GildeBuildingGold[i] * 30);
            GildeBuildingPilz[i] = 0;
        } else {
            if (i > 25){
                if (noMush){
                    GildeBuildingGold[i] = (
                                    GildeBuildingGold[i] * (i - 25));
                };
                GildeBuildingPilz[i] = ((noMush) ? 0 : ((i - 25) * 5));
            };
        };
        i = (i + 1);
    };
    define_snd(SND['CLICK'], "res/sfx/click.mp3", True);
    define_snd(SND_ERROR, "res/sfx/error.mp3", False);
    define_snd(SND_JINGLE, "res/sfx/jingle.mp3", True);
    define_img(IF_BACKGROUND,
              (("res/gfx/if/login" + login_background_id) + ".jpg"),
              True, 280, 100);
    define_from_class(IF_LEFT, interface_left_jpg, 0, 100);
    define_from_class(IF_TOP, interface_top_jpg, 0, 0);
    define_from_class(IF_MAIN, interface_main_jpg, 280, 100);
    actor[IF_MAIN].mouse_enabled = False;
    define_bunch(IF_MAIN,
                 IF_BACKGROUND,
                 IF_LEFT,
                 IF_TOP,
                 IF_MAIN,
                 IF_IMPRESSUM,
                 IF_FORUM,
                 IF_AGB,
                 IF_DATENSCHUTZ,
                 IF_ANLEITUNG);
    if (shop_url != ""){
        add_bunch(IF_MAIN, IF_SHOP);
    };
    i = 0;
    while (i < param_social_buttons.length) {
        DefineCnt((SOCIAL + i), (120 + (i * 40)), 2);
        define_img((SOCIAL + i),
                  (("res/gfx/if/social_"
                   + param_social_buttons[i].split(":")[0]) + ".png"),
                    True, 0, 0);
        MakePersistent((SOCIAL + i), (SOCIAL + i));
        var _local2 = actor[(SOCIAL + i)];
        with (_local2) {
            addChild(actor[(SOCIAL + i)]);
            textLinkMakeClickable(getChildAt(0).parent);
            add_event_listener(MouseEvent.CLICK, ShowSocial);
            buttonMode = True;
            useHandCursor = True;
            mouseChildren = False;
        };
        if (param_social_buttons[i].split(":").length > 1){
            if (texts[int(param_social_buttons[i].split(":")[1])]){
                enable_popup((SOCIAL + i),
                             texts[param_social_buttons[i].split(":")[1]]);
            };
        };
        add_bunch(IF_MAIN, (SOCIAL + i));
        i = (i + 1);
    };
    define_bunch(IF_OVL, IF_MAIN);
    if (param_sponsor != ""){
        var ShowSponsor:* = function (evt:MouseEvent=None){
            navigate_to_url(new URLRequest(param_sponsor_url), "_blank");
        };
        DefineCnt(IF_SPONSOR, SPONSOR_X, SPONSOR_Y);
        define_img(IF_SPONSOR, (("res/gfx/if/sponsor_"
                  + param_sponsor) + ".png"), True, 0, 0);
        if (param_sponsor_url != ""){
            MakePersistent(IF_SPONSOR, IF_SPONSOR);
            add_bunch(IF_MAIN, IF_SPONSOR);
            _local2 = actor[IF_SPONSOR];
            with (_local2) {
                addChild(actor[IF_SPONSOR]);
                add_event_listener(MouseEvent.CLICK, ShowSponsor);
                mouseChildren = False;
                useHandCursor = True;
                buttonMode = True;
            };
        } else {
            MakePersistent(IF_SPONSOR);
            add_bunch(IF_MAIN, IF_SPONSOR);
            _local2 = actor[IF_SPONSOR];
            with (_local2) {
                x = SPONSOR_X;
                y = SPONSOR_Y;
            };
        };
    };
    DefineCnt(IF_LOGOUT,
              ((shop_url)!="") ? LOGOUT_X_WITH_SHOP : LOGOUT_X, LOGOUT_Y);
    define_lbl(LBL_IF_LOGOUT,
              texts[TXT_LOGOUT], 0, 0,
              FontFormat_LOGoutLink);
    add_filter(LBL_IF_LOGOUT, Filter_Shadow);
    MakePersistent(IF_LOGOUT, LBL_IF_LOGOUT);
    _local2 = actor[IF_LOGOUT];
    with (_local2) {
        addChild(actor[LBL_IF_LOGOUT]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (((shop_url)!="")
             ? LOGOUT_X_WITH_SHOP : LOGOUT_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, RequestLOGout);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(IF_IMPRESSUM, IMPRESSUM_X, LOGOUT_Y);
    define_lbl(LBL_IF_IMPRESSUM,
              texts[TXT_IMPRESSUM_LINK], 0, 0,
              FontFormat_LOGoutLink);
    add_filter(LBL_IF_IMPRESSUM, Filter_Shadow);
    MakePersistent(IF_IMPRESSUM, LBL_IF_IMPRESSUM);
    _local2 = actor[IF_IMPRESSUM];
    with (_local2) {
        addChild(actor[LBL_IF_IMPRESSUM]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (IMPRESSUM_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, ShowImpressum);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(IF_FORUM,
              ((shop_url)!="") ? FORUM_X_WITH_SHOP : FORUM_X, LOGOUT_Y);
    define_lbl(LBL_IF_FORUM,
              texts[TXT_FORUM_LINK], 0, 0, FontFormat_LOGoutLink);
    add_filter(LBL_IF_FORUM, Filter_Shadow);
    MakePersistent(IF_FORUM, LBL_IF_FORUM);
    _local2 = actor[IF_FORUM];
    with (_local2) {
        addChild(actor[LBL_IF_FORUM]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (((shop_url)!="")
             ? FORUM_X_WITH_SHOP : FORUM_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, ShowForum);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(IF_AGB, AGB_X, LOGOUT_Y);
    define_lbl(LBL_IF_AGB, texts[TXT_AGB_LINK], 0, 0, FontFormat_LOGoutLink)
    add_filter(LBL_IF_AGB, Filter_Shadow);
    MakePersistent(IF_AGB, LBL_IF_AGB);
    _local2 = actor[IF_AGB];
    with (_local2) {
        addChild(actor[LBL_IF_AGB]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (AGB_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, ShowAGB);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(IF_DATENSCHUTZ, DATENSCHUTZ_X, LOGOUT_Y);
    define_lbl(LBL_IF_DATENSCHUTZ,
              texts[TXT_DATENSCHUTZ_LINK], 0, 0, FontFormat_LOGoutLink);
    add_filter(LBL_IF_DATENSCHUTZ, Filter_Shadow);
    MakePersistent(IF_DATENSCHUTZ, LBL_IF_DATENSCHUTZ);
    _local2 = actor[IF_DATENSCHUTZ];
    with (_local2) {
        addChild(actor[LBL_IF_DATENSCHUTZ]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (DATENSCHUTZ_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, ShowDatenschutz);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(IF_ANLEITUNG,
              ((shop_url)!="")
                ? ANLEITUNG_X_WITH_SHOP
                : ANLEITUNG_X, LOGOUT_Y);
    define_lbl(LBL_IF_ANLEITUNG,
              texts[TXT_ANLEITUNG_LINK], 0, 0, FontFormat_LOGoutLink);
    add_filter(LBL_IF_ANLEITUNG, Filter_Shadow);
    MakePersistent(IF_ANLEITUNG, LBL_IF_ANLEITUNG);
    _local2 = actor[IF_ANLEITUNG];
    with (_local2) {
        addChild(actor[LBL_IF_ANLEITUNG]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (((shop_url)!="")
             ? ANLEITUNG_X_WITH_SHOP : ANLEITUNG_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, ShowAnleitung);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(IF_SHOP, SHOP_X, LOGOUT_Y);
    define_lbl(LBL_IF_SHOP,
              texts[TXT_SHOP_LINK], 0, 0, FontFormat_LOGoutLink);
    add_filter(LBL_IF_SHOP, Filter_Shadow);
    MakePersistent(IF_SHOP, LBL_IF_SHOP);
    _local2 = actor[IF_SHOP];
    with (_local2) {
        addChild(actor[LBL_IF_SHOP]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (SHOP_X - int((width / 2)));
        add_event_listener(MouseEvent.CLICK, ShowShop);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    define_img(IF_KRIEGER, "res/gfx/scr/hall/punkt_krieger.png", True, 0, 0)
    define_img(IF_JAEGER, "res/gfx/scr/hall/punkt_dieb.png", True, 0, 0);
    define_img(IF_MAGIER, "res/gfx/scr/hall/punkt_magier.png", True, 0, 0);
    define_img(IF_GOLD, "res/gfx/if/icon_gold.png", True, 0, IF_LBL_GOLD_Y);
    define_lbl(LBL_IF_GOLD, "", 0, IF_LBL_GOLD_Y, FontFormat_Default);
    define_img(IF_SILBER,
              "res/gfx/if/icon_silber.png", True,
              IF_LBL_GOLDPILZE_X, IF_LBL_GOLD_Y);
    define_lbl(LBL_IF_SILBER, "", 0, IF_LBL_GOLD_Y, FontFormat_Default);
    enable_popup(LBL_IF_SILBER, texts[TXT_SILVER_HINT]);
    enable_popup(IF_SILBER, texts[TXT_SILVER_HINT]);
    define_img(IF_PILZE, "res/gfx/if/icon_pilz.png", True,
              IF_LBL_GOLDPILZE_X, IF_LBL_PILZE_Y);
    define_lbl(LBL_IF_PILZE, "", 0, IF_LBL_PILZE_Y, FontFormat_Default);
    MakePersistent(LBL_IF_GOLD, LBL_IF_PILZE, LBL_IF_SILBER, IF_GOLD,
                   IF_SILBER, IF_PILZE);
    define_bunch(IF_STATS, LBL_IF_GOLD, LBL_IF_PILZE, LBL_IF_SILBER,
                 IF_GOLD, IF_SILBER, IF_PILZE);
    define_img(IF_HUTMANN1,
              "res/gfx/scr/taverne/huetchenspieler/hatplayer1.png",
              True, 0, 0);
    define_img(IF_HUTMANN2,
              "res/gfx/scr/taverne/huetchenspieler/hatplayer2.png",
              True, 0, 0);
    define_img(IF_HUTMANN_OVL,
              "res/gfx/scr/taverne/huetchenspieler/hatplayer_ovl.jpg",
              True, IF_HUTLINK_X, IF_HUTLINK_Y);
    DefineCnt(IF_HUTMANN, IF_HUTLINK_X, IF_HUTLINK_Y);
    define_img(IF_TOILET, "res/gfx/scr/taverne/wc_sign.png", True, 0, 0);
    DefineCnt(IF_TOILET, (IF_HUTLINK_X + 90), (IF_HUTLINK_Y + 40));
    MakePersistent(IF_HUTMANN1, IF_HUTMANN2, IF_HUTMANN_OVL, IF_HUTMANN,
                   IF_TOILET, IF_TOILET);
    _local2 = actor[IF_HUTMANN];
    with (_local2) {
        addChild(actor[IF_HUTMANN1]);
        addChild(actor[IF_HUTMANN2]);
    };
    _local2 = actor[IF_TOILET];
    with (_local2) {
        addChild(actor[IF_TOILET]);
    };
    iPosi = 0;
    yOffs = 0;
    DefiniereInterfaceButton(IF_TAVERNE, TXT_TAVERNE);
    DefiniereInterfaceButton(IF_ARENA, TXT_ARENA);
    DefiniereInterfaceButton(IF_ARBEITEN, TXT_ARBEITEN);
    DefiniereInterfaceButton(IF_SCHMIEDE, TXT_SCHMIEDE);
    DefiniereInterfaceButton(IF_ZAUBERLADEN, TXT_ZAUBERLADEN);
    DefiniereInterfaceButton(IF_STALL, TXT_STALL);
    DefiniereInterfaceButton(IF_PILZDEALER, TXT_PILZDEALER);
    yOffs = (yOffs + IF_2);
    DefiniereInterfaceButton(IF_CHARAKTER, TXT_CHARAKTER);
    DefiniereInterfaceButton(IF_POST, TXT_POST);
    DefiniereInterfaceButton(IF_GILDEN, TXT_GILDEN);
    DefiniereInterfaceButton(IF_EHRENHALLE, TXT_EHRENHALLE);
    DefiniereInterfaceButton(IF_WELTKARTE, TXT_WELTKARTE);
    DefiniereInterfaceButton(IF_OPTIONEN, TXT_OPTIONEN);
    actor[IF_WELTKARTE].add_event_listener(MouseEvent.MOUSE_OVER,
                                           dungeonBtnHover);
    actor[IF_WELTKARTE].add_event_listener(MouseEvent.MOUSE_OUT,
                                           dungeonBtnLeave);
    dungeonBtnUpdateDelayTimer = new Timer(500);
    dungeonBtnUpdateDelayTimer.add_event_listener(TimerEvent.TIMER,
                                                  dungeonBtnUpdateDelay);
    actor[IF_ARBEITEN].add_event_listener(MouseEvent.MOUSE_OVER,
                                          workBtnHover);
    actor[IF_ARBEITEN].add_event_listener(MouseEvent.MOUSE_OUT,
                                          workBtnLeave);
    workBtnUpdateDelayTimer = new Timer(500);
    workBtnUpdateDelayTimer.add_event_listener(TimerEvent.TIMER,
                                               workBtnUpdateDelay);
    actor[IF_TAVERNE].add_event_listener(MouseEvent.MOUSE_OVER,
                                         tavBtnHover);
    actor[IF_TAVERNE].add_event_listener(MouseEvent.MOUSE_OUT,
                                         tavBtnLeave);
    tavBtnUpdateDelayTimer = new Timer(500);
    tavBtnUpdateDelayTimer.add_event_listener(TimerEvent.TIMER,
                                              tavBtnUpdateDelay);
    actor[IF_ARENA].add_event_listener(MouseEvent.MOUSE_OVER,
                                       arenaBtnHover);
    actor[IF_ARENA].add_event_listener(MouseEvent.MOUSE_OUT,
                                       arenaBtnLeave);
    arenaBtnUpdateDelayTimer = new Timer(500);
    arenaBtnUpdateDelayTimer.add_event_listener(TimerEvent.TIMER,
                                                arenaBtnUpdateDelay);
    define_bunch(IF_BUTTONS, IF_HUTMANN, IF_TOILET, IF_HUTMANN_OVL,
                 IF_TAVERNE, IF_ARENA, IF_ARBEITEN, IF_SCHMIEDE,
                 IF_ZAUBERLADEN);
    add_bunch(IF_BUTTONS, IF_STALL, IF_PILZDEALER, IF_CHARAKTER, IF_POST,
              IF_GILDEN, IF_EHRENHALLE, IF_WELTKARTE, IF_OPTIONEN);
    i = IF_DRAGON_1;
    while (i <= IF_DRAGON_13) {
        add_bunch(IF_BUTTONS, i);
        i = (i + 1);
    };
    HutmannLinkTimer = new Timer(50);
    HutmannLinkTimer.add_event_listener(TimerEvent.TIMER,
                                        HutmannLinkAniEvent);
    HutmannLinkTimer.start();
    HutmannLinkVis = False;
    HutmannLinkOver = False;
    HutmannRelY = 0;
    var HutmannFrame:* = 0;
    HutmannAniStep = 0;
    HutmannCountdown = 0;
    _local2 = actor[IF_TAVERNE];
    with (_local2) {
        add_event_listener(MouseEvent.MOUSE_OVER, TaverneBtnIn);
        add_event_listener(MouseEvent.MOUSE_OUT, TaverneBtnOut);
        add_event_listener(MouseEvent.MOUSE_UP, TaverneBtnOut);
    };
    _local2 = actor[IF_HUTMANN];
    with (_local2) {
        add_event_listener(MouseEvent.MOUSE_OVER, TaverneBtnIn);
        add_event_listener(MouseEvent.MOUSE_OUT, TaverneBtnOut);
        add_event_listener(MouseEvent.MOUSE_UP, TaverneBtnOut);
        add_event_listener(MouseEvent.MOUSE_DOWN, ShowHutmann);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    _local2 = actor[IF_TOILET];
    with (_local2) {
        add_event_listener(MouseEvent.MOUSE_OVER, TaverneBtnIn);
        add_event_listener(MouseEvent.MOUSE_OUT, TaverneBtnOut);
        add_event_listener(MouseEvent.MOUSE_UP, TaverneBtnOut);
        add_event_listener(MouseEvent.MOUSE_DOWN, RequestToilet);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    MakePersistent(IF_BACKGROUND, IF_LEFT, IF_TOP, IF_MAIN);
    define_from_class(IF_WINDOW, interface_window_png, IF_WIN_X, IF_WIN_Y);
    define_from_class(BLACK_SQUARE, black_square, 0, 0);
    actor[BLACK_SQUARE].alpha = 0.5;
    define_lbl(LBL_WINDOW_TITLE, "", 0, (IF_WIN_Y + IF_WIN_WELCOME_Y),
              FontFormat_Heading);
    add_filter(LBL_WINDOW_TITLE, Filter_Shadow);
    iPosi = 0;
    AIRRelMoveY = 0;
    AIRRelMoveYButton = 0;
    AIRRelMoveYButton2 = 0;
    iPosi = (iPosi + 1);
    define_lbl(LBL_NAME, texts[TXT_NAME], (IF_WIN_X + IF_WIN_INPUTS_X),
              (((IF_WIN_Y + IF_WIN_INPUTS_Y)
               + (IF_WIN_INPUTS_DISTANCE_Y * iPosi))
                + AIRRelMoveY), FontFormat_Default);
    define_lbl(LBL_LOGIN_PASSWORD, texts[TXT_PASSWORD],
              (IF_WIN_X + IF_WIN_INPUTS_X),
              (((IF_WIN_Y + IF_WIN_INPUTS_Y)
               + (IF_WIN_INPUTS_DISTANCE_Y * iPosi)) + AIRRelMoveY),
                FontFormat_Default);
    iPosi = (iPosi + 1);
    define_lbl(LBL_EMAIL, texts[TXT_EMAIL], (IF_WIN_X + IF_WIN_INPUTS_X),
              (((IF_WIN_Y + IF_WIN_INPUTS_Y)
               + (IF_WIN_INPUTS_DISTANCE_Y * iPosi)) + AIRRelMoveY),
                FontFormat_Default);
    iPosi = (iPosi + 1);
    define_lbl(LBL_PASSWORD, texts[TXT_PASSWORD],
              (IF_WIN_X + IF_WIN_INPUTS_X),
              (((IF_WIN_Y + IF_WIN_INPUTS_Y)
               + (IF_WIN_INPUTS_DISTANCE_Y * iPosi)) + AIRRelMoveY),
                FontFormat_Default);
    add_filter(LBL_NAME, Filter_Shadow);
    add_filter(LBL_LOGIN_PASSWORD, Filter_Shadow);
    add_filter(LBL_EMAIL, Filter_Shadow);
    add_filter(LBL_PASSWORD, Filter_Shadow);
    define_from_class(INP['NAME'], text_input1,
                    (actor[LBL_NAME].x + IF_WIN_INPUTS_FIELD_X),
                    (actor[LBL_NAME].y + IF_WIN_INPUTS_FIELD_Y), 2, "name")
    define_from_class(INP['LOGIN_PASSWORD'], text_input2,
                    (actor[LBL_LOGIN_PASSWORD].x + IF_WIN_INPUTS_FIELD_X),
                    (actor[LBL_LOGIN_PASSWORD].y + IF_WIN_INPUTS_FIELD_Y),
                    2, "password");
    define_from_class(INP['EMAIL'], text_input2,
                    (actor[LBL_EMAIL].x + IF_WIN_INPUTS_FIELD_X),
                    (actor[LBL_EMAIL].y + IF_WIN_INPUTS_FIELD_Y),
                    2, "email");
    define_from_class(INP['PASSWORD'], text_input1,
                    (actor[LBL_PASSWORD].x + IF_WIN_INPUTS_FIELD_X),
                    (actor[LBL_PASSWORD].y + IF_WIN_INPUTS_FIELD_Y),
                    2, "password");
    define_img(FILLSPACE, (("res/gfx/if/file" + "space.pn") + "g"), False,
              280, 100);
    define_img(PASSWORD_SMILEY_SAD, "res/gfx/if/smiley_sad.png", False,
              (((actor[LBL_PASSWORD].x + IF_WIN_INPUTS_FIELD_X)
               + actor[INP['PASSWORD']].width) + 5),
                ((actor[LBL_PASSWORD].y + IF_WIN_INPUTS_FIELD_Y) + 3));
    define_img(PASSWORD_SMILEY_NEUTRAL, "res/gfx/if/smiley_neutral.png",
              False,
              (((actor[LBL_PASSWORD].x + IF_WIN_INPUTS_FIELD_X)
               + actor[INP['PASSWORD']].width) + 5),
                ((actor[LBL_PASSWORD].y + IF_WIN_INPUTS_FIELD_Y) + 3));
    define_img(PASSWORD_SMILEY_HAPPY, "res/gfx/if/smiley_happy.png", False,
              (((actor[LBL_PASSWORD].x + IF_WIN_INPUTS_FIELD_X)
               + actor[INP['PASSWORD']].width) + 5),
                ((actor[LBL_PASSWORD].y + IF_WIN_INPUTS_FIELD_Y) + 3));
    enable_popup(PASSWORD_SMILEY_SAD,
                 texts[TXT_PASSWORD_SMILEY_SAD].split("#").join(chr(13)));
    enable_popup(PASSWORD_SMILEY_NEUTRAL,
                 texts[TXT_PASSWORD_SMILEY_NEUTRAL]
                    .split("#").join(chr(13)));
    enable_popup(PASSWORD_SMILEY_HAPPY,
                 texts[TXT_PASSWORD_SMILEY_HAPPY].split("#").join(chr(13)))
    actor[INP['PASSWORD']].add_event_listener(KeyboardEvent.KEY_UP,
                                              gradePassword);
    DefineCnt(FORGOT_PASSWORD, 0,
              (((IF_WIN_Y + IF_WIN_Y) + IF_WIN_LNK_1_Y) + AIRRelMoveY));
    define_lbl(LBL_FORGOT_PASSWORD, texts[TXT_FORGOT_PASSWORD], 0, 0,
              FontFormat_Default);
    add_filter(LBL_FORGOT_PASSWORD, Filter_Shadow);
    DefineCnt(GOTO_LOGIN, 0,
              ((IF_WIN_Y + IF_WIN_Y) + IF_WIN_LNK_2_Y) + AIRRelMoveYButton)
    define_lbl(LBL_GOTO_LOGIN, texts[TXT_GOTO_LOGIN], 0, 0,
              FontFormat_Default);
    DefineCnt(GOTO_SIGNUP, 0,
              (IF_WIN_Y + IF_WIN_Y + IF_WIN_LNK_2_Y) + AIRRelMoveYButton2)
    define_lbl(LBL_GOTO_SIGNUP, texts[TXT_GOTO_SIGNUP], 0, 0,
              FontFormat_Default);
    add_filter(LBL_GOTO_LOGIN, Filter_Shadow);
    add_filter(LBL_GOTO_SIGNUP, Filter_Shadow);
    MakePersistent(LBL_FORGOT_PASSWORD, LBL_GOTO_LOGIN, LBL_GOTO_SIGNUP);
    _local2 = actor[FORGOT_PASSWORD];
    with (_local2) {
        x = ((IF_WIN_X + IF_WIN_WELCOME_X)
             - int((actor[LBL_FORGOT_PASSWORD].text_width / 2)));
        addChild(actor[LBL_FORGOT_PASSWORD]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, ShowForgotPasswordScreen);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    _local2 = actor[GOTO_LOGIN];
    with (_local2) {
        x = ((IF_WIN_X + IF_GOTO_LOGIN_X)
             - int(actor[LBL_GOTO_LOGIN].text_width));
        addChild(actor[LBL_GOTO_LOGIN]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, ShowBuildCharacterScreen);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    _local2 = actor[GOTO_SIGNUP];
    with (_local2) {
        x = ((IF_WIN_X + IF_WIN_WELCOME_X)
             - int((actor[LBL_GOTO_SIGNUP].text_width / 2)));
        addChild(actor[LBL_GOTO_SIGNUP]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, DoGotoSignup);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    actor[INP['PASSWORD']].getChildAt(1).displayAsPassword = True;
    actor[INP['LOGIN_PASSWORD']].getChildAt(1).displayAsPassword = True;
    define_from_class(CB_AGB_UNCHECKED, cb_unchecked,
                    (IF_WIN_X + IF_WIN_CB_X),
                    ((IF_WIN_Y + IF_WIN_CB_Y) + AIRRelMoveY));
    actor[CB_AGB_UNCHECKED].add_event_listener(MouseEvent.CLICK, CheckAGB);
    define_from_class(CB['AGB_CHECKED'], cb_checked,
                    (IF_WIN_X + IF_WIN_CB_X),
                    ((IF_WIN_Y + IF_WIN_CB_Y) + AIRRelMoveY));
    actor[CB['AGB_CHECKED']].add_event_listener(MouseEvent.CLICK,
                                                UncheckAGB);
    define_lbl(LBL_LOGIN_LEGAL_0,
              (((texts[TXT_LOGIN_LEGAL_2] == ""))
               ? texts[TXT_LOGIN_LEGAL_1].split("%link")[0] : ""),
                (actor[CB_AGB_UNCHECKED].x + AGB_LBL_X),
                (actor[CB_AGB_UNCHECKED].y + AGB_LBL_Y));
    add_filter(LBL_LOGIN_LEGAL_0, Filter_Shadow);
    DefineCnt(AGB, ((actor[LBL_LOGIN_LEGAL_0].x + 6)
              + actor[LBL_LOGIN_LEGAL_0].width),
                (actor[CB_AGB_UNCHECKED].y + AGB_LBL_Y));
    define_lbl(LBL_AGB, texts[TXT_AGB], 0, 0, FontFormat_Default);
    add_filter(LBL_AGB, Filter_Shadow);
    MakePersistent(LBL_AGB);
    _local2 = actor[AGB];
    with (_local2) {
        addChild(actor[LBL_AGB]);
        add_event_listener(MouseEvent.CLICK, ShowAGB);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    define_lbl(LBL_LOGIN_LEGAL_1,
              (((texts[TXT_LOGIN_LEGAL_2] == ""))
               ? texts[TXT_LOGIN_LEGAL_1].split("%link")[1]
               : texts[TXT_LOGIN_LEGAL_1]),
                ((actor[AGB].x + 6) + actor[AGB].width),
                (actor[CB_AGB_UNCHECKED].y + AGB_LBL_Y));
    add_filter(LBL_LOGIN_LEGAL_1, Filter_Shadow);
    DefineCnt(DATENSCHUTZ,
              ((actor[LBL_LOGIN_LEGAL_1].x + 6)
               + actor[LBL_LOGIN_LEGAL_1].width),
                (actor[CB_AGB_UNCHECKED].y + AGB_LBL_Y));
    define_lbl(LBL_DATENSCHUTZ, texts[TXT_DATENSCHUTZ], 0, 0,
              FontFormat_Default);
    add_filter(LBL_DATENSCHUTZ, Filter_Shadow);
    MakePersistent(LBL_DATENSCHUTZ);
    _local2 = actor[DATENSCHUTZ];
    with (_local2) {
        addChild(actor[LBL_DATENSCHUTZ]);
        add_event_listener(MouseEvent.CLICK, ShowDatenschutz);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    define_lbl(LBL_LOGIN_LEGAL_2,
              (((texts[TXT_LOGIN_LEGAL_2] == ""))
               ? texts[TXT_LOGIN_LEGAL_1].split("%link")[2]
               : texts[TXT_LOGIN_LEGAL_2]),
              ((actor[DATENSCHUTZ].x + 6) + actor[DATENSCHUTZ].width),
              (actor[CB_AGB_UNCHECKED].y + AGB_LBL_Y));
    add_filter(LBL_LOGIN_LEGAL_2, Filter_Shadow);
    textLinkMakeClickable(actor[AGB]);
    textLinkMakeClickable(actor[DATENSCHUTZ]);
    define_from_class(SHP_FUCK_BLACK_SQUARE, black_square, 310,
                    ((IF_WIN_Y + IF_WIN_CB_Y) + 125));
    _local2 = actor[SHP_FUCK_BLACK_SQUARE];
    with (_local2) {
        width = 930;
        height = 90;
        alpha = 0.6;
    };
    define_from_class(CB_FUCK_UNCHECKED, cb_unchecked, 320,
                    ((IF_WIN_Y + IF_WIN_CB_Y) + 150));
    actor[CB_FUCK_UNCHECKED].add_event_listener(MouseEvent.CLICK,
                                                CheckFuck);
    define_from_class(CB_FUCK_CHECKED, cb_checked, 320,
                    ((IF_WIN_Y + IF_WIN_CB_Y) + 150));
    actor[CB_FUCK_CHECKED].add_event_listener(MouseEvent.CLICK,
                                              UncheckFuck);
    define_lbl(LBL_FUCK, param_bullshit_text, 380,
              ((IF_WIN_Y + IF_WIN_CB_Y) + 150), FontFormat_Bullshit);
    add_filter(LBL_FUCK, Filter_Shadow);
    _local2 = actor[LBL_FUCK];
    with (_local2) {
        width = 840;
        wordWrap = True;
    };
    define_bunch(FUCK, SHP_FUCK_BLACK_SQUARE, CB_FUCK_UNCHECKED, LBL_FUCK);
    define_btn(IF_LOGIN, texts[TXT_LOGIN], RequestLOGin, btn_classBasic,
               ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               ((IF_WIN_Y + IF_WIN_Y) + AIRRelMoveYButton2));
    define_btn(IF_SIGNUP, texts[TXT_SIGNUP], request_signup,
               btn_classBasic, ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (((IF_WIN_Y + IF_WIN_Y) + IF_WIN_2_Y) + AIRRelMoveYButton));
    define_btn(IF_REQUEST_PASSWORD, texts[TXT_REQUEST_PASSWORD],
               RequestPassword, btn_classBasic,
               ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               ((IF_WIN_Y + IF_WIN_Y) + AIRRelMoveY));
    define_lbl(LBL['ERROR'], "", IF_ERROR_X, IF_ERROR_Y, FontFormat_Error);
    add_filter(LBL['ERROR'], Filter_Shadow);
    define_bunch(WINDOW_LOGIN, BLACK_SQUARE, IF_WINDOW, LBL_WINDOW_TITLE,
                 IF_LOGIN, LBL_NAME, INP['NAME']);
    add_bunch(WINDOW_LOGIN, LBL_LOGIN_PASSWORD, INP['LOGIN_PASSWORD'],
              GOTO_SIGNUP, FORGOT_PASSWORD);
    define_bunch(WINDOW_SIGNUP, BLACK_SQUARE, IF_WINDOW, LBL_WINDOW_TITLE,
                 IF_SIGNUP, LBL_NAME, INP['NAME']);
    add_bunch(WINDOW_SIGNUP, LBL_EMAIL, INP['EMAIL'], LBL_PASSWORD,
              INP['PASSWORD'], GOTO_LOGIN, CB_AGB_UNCHECKED, AGB,
              LBL_LOGIN_LEGAL_0, LBL_LOGIN_LEGAL_1, LBL_LOGIN_LEGAL_2,
              DATENSCHUTZ);
    add_bunch(WINDOW_SIGNUP, PASSWORD_SMILEY_SAD, PASSWORD_SMILEY_NEUTRAL,
              PASSWORD_SMILEY_HAPPY);
    define_bunch(WINDOW_FORGOT_PASSWORD, BLACK_SQUARE, IF_WINDOW,
                 LBL_WINDOW_TITLE, IF_REQUEST_PASSWORD, LBL_NAME,
                 INP['NAME']);
    add_bunch(WINDOW_FORGOT_PASSWORD, LBL_EMAIL, INP['EMAIL'], GOTO_LOGIN);
    drachen_setzen();
    PulseTimer = new Timer(20);
    PulseLevel = 0;
    _local2 = PulseTimer;
    with (_local2) {
        add_event_listener(TimerEvent.TIMER, PulseEvent);
        start();
    };
    define_img(SCR_BUILDCHAR_BACKGROUND,
              "res/gfx/scr/buildchar/char_erstellung.png", False,
              SCR_BUILDCHAR_1_X, SCR_BUILDCHAR_1_Y);
    define_bunch(SCR_BUILDCHAR, SCR_BUILDCHAR_BACKGROUND, IF_MAIN);
    define_lbl(LBL_SCREEN_TITLE, texts[TXT_CREATE_CHARACTER],
              SCREEN_TITLE_X, SCREEN_TITLE_Y, FontFormat_ScreenTitle);
    add_filter(LBL_SCREEN_TITLE, Filter_Shadow);
    actor[LBL_SCREEN_TITLE].x = (SCREEN_TITLE_X
                         - int((actor[LBL_SCREEN_TITLE].text_width / 2)));
    define_btn(RANDOM, texts[TXT_RANDOM], randomize_char_image,
               btn_classLOGin, SCREEN_RANDOM_BUTTON_X,
               SCREEN_RANDOM_BUTTON_Y);
    define_btn(CREATE_CHARACTER, texts[TXT_CREATE_CHARACTER],
               show_signup_screen, btn_classBasic, SCR_BUILDCHAR_CREATE_X,
               SCR_BUILDCHAR_CREATE_Y);
    define_btn(MODIFY_CHARACTER, texts[TXT_MODIFY_CHARACTER],
               RequestChangeFace, btn_classBasic, SCR_BUILDCHAR_CREATE_X,
               SCR_BUILDCHAR_CREATE_Y);
    define_lbl(LBL_CREATE_RACE, "", CREATE_RACE_X, CREATE_RACE_Y,
              FontFormat_Default);
    define_lbl(LBL_CREATE_RACE_DESC, "", CREATE_RACE_X, 0,
              FontFormat_DefaultLeft);
    _local2 = actor[LBL_CREATE_RACE_DESC];
    with (_local2) {
        width = BUILDCHAR_LINES_X;
        wordWrap = True;
    };
    define_lbl(LBL_CREATE_CLASS, "", CREATE_RACE_X, 0, FontFormat_Default);
    define_lbl(LBL_CREATE_CLASS_DESC, "", CREATE_RACE_X, 0,
              FontFormat_DefaultLeft);
    _local2 = actor[LBL_CREATE_CLASS_DESC];
    with (_local2) {
        width = BUILDCHAR_LINES_X;
        wordWrap = True;
    };
    add_filter(LBL_CREATE_RACE, Filter_Shadow);
    add_filter(LBL_CREATE_RACE_DESC, Filter_Shadow);
    add_filter(LBL_CREATE_CLASS, Filter_Shadow);
    add_filter(LBL_CREATE_CLASS_DESC, Filter_Shadow);
    define_lbl(LBL_CREATE_GOTO_LOGIN, texts[TXT_CREATE_GOTO_LOGIN], 0, 0,
              FontFormat_Default);
    add_filter(LBL_CREATE_GOTO_LOGIN, Filter_Shadow);
    MakePersistent(LBL_CREATE_GOTO_LOGIN);
    DefineCnt(CREATE_GOTO_LOGIN, 0, SCR_BUILDCHAR_LOGIN_Y);
    _local2 = actor[CREATE_GOTO_LOGIN];
    with (_local2) {
        addChild(actor[LBL_CREATE_GOTO_LOGIN]);
        textLinkMakeClickable(getChildAt(0).parent);
        mouseChildren = False;
        mouse_enabled = True;
        buttonMode = True;
        useHandCursor = True;
        add_event_listener(MouseEvent.CLICK, ShowLOGinScreen);
        x = (SCR_BUILDCHAR_LOGIN_X
             - actor[LBL_CREATE_GOTO_LOGIN].text_width);
    };
    define_img(M_IDLE, "res/gfx/scr/buildchar/button_male_idle.jpg", False,
              SCR_BUILDCHAR_GENDER_X, SCR_BUILDCHAR_GENDER_Y);
    DefineCnt(M_ACT, SCR_BUILDCHAR_GENDER_X, SCR_BUILDCHAR_GENDER_Y);
    define_img(F_IDLE, "res/gfx/scr/buildchar/button_female_idle.jpg",
              False, (SCR_BUILDCHAR_GENDER_X + SCR_BUILDCHAR_GENDER_X),
              SCR_BUILDCHAR_GENDER_Y);
    DefineCnt(F_ACT, (SCR_BUILDCHAR_GENDER_X + SCR_BUILDCHAR_GENDER_X),
              SCR_BUILDCHAR_GENDER_Y);
    actor[M_IDLE].add_event_listener(MouseEvent.CLICK, SelectGender);
    actor[F_IDLE].add_event_listener(MouseEvent.CLICK, SelectGender);
    i = 0;
    while (i < 2) {
        enable_popup((M_IDLE + (i * 2)), texts[(TXT_GENDER_M + i)]);
        enable_popup((M_ACT + (i * 2)), texts[(TXT_GENDER_M + i)]);
        i = (i + 1);
    };
    define_img(KASTE_1_IDLE,
              "res/gfx/scr/buildchar/button_warrior_idle.jpg", False,
              SCR_BUILDCHAR_CASTE_X, SCR_BUILDCHAR_CASTE_Y);
    DefineCnt(KASTE_1_ACT, SCR_BUILDCHAR_CASTE_X, SCR_BUILDCHAR_CASTE_Y);
    define_img(KASTE_2_IDLE, "res/gfx/scr/buildchar/button_mage_idle.jpg",
              False, (SCR_BUILDCHAR_CASTE_X + SCR_BUILDCHAR_CASTE_X),
              SCR_BUILDCHAR_CASTE_Y);
    DefineCnt(KASTE_2_ACT, (SCR_BUILDCHAR_CASTE_X + SCR_BUILDCHAR_CASTE_X),
              SCR_BUILDCHAR_CASTE_Y);
    define_img(KASTE_3_IDLE, "res/gfx/scr/buildchar/button_hunter_idle.jpg",
              False, (SCR_BUILDCHAR_CASTE_X + (SCR_BUILDCHAR_CASTE_X * 2)),
              SCR_BUILDCHAR_CASTE_Y);
    DefineCnt(KASTE_3_ACT,
              (SCR_BUILDCHAR_CASTE_X + (SCR_BUILDCHAR_CASTE_X * 2)),
              SCR_BUILDCHAR_CASTE_Y);
    actor[KASTE_1_IDLE].add_event_listener(MouseEvent.CLICK, SelectCaste);
    actor[KASTE_2_IDLE].add_event_listener(MouseEvent.CLICK, SelectCaste);
    actor[KASTE_3_IDLE].add_event_listener(MouseEvent.CLICK, SelectCaste);
    i = 0;
    while (i < 3) {
        enable_popup((KASTE_1_IDLE + (i * 2)), texts[(TXT_CLASSNAME + i)]);
        enable_popup((KASTE_1_ACT + (i * 2)), texts[(TXT_CLASSNAME + i)]);
        i = (i + 1);
    };
    define_bunch(VOLK_BTNS_M);
    define_bunch(VOLK_BTNS_F);
    define_bunch(VOLK_BTNS_ALL);
    define_img(VOLK_MARKER, "res/gfx/scr/buildchar/button_marked.png", True)
    when_loaded(CloneMarker);
    i = 0;
    while (i <= 7) {
        pos_x = (SCR_BUILDCHAR_VOLK_X + ((i)<4) ? 0 : SCR_BUILDCHAR_VOLK_X)
        pos_y = (SCR_BUILDCHAR_VOLK_Y
                 + (((i)<4) ? i : (i - 4) * SCR_BUILDCHAR_VOLK_Y));
        Switch ((i + 1)){
            if case(1:
                volk = "human";
                break;
            if case(2:
                volk = "elf";
                break;
            if case(3:
                volk = "dwarf";
                break;
            if case(4:
                volk = "gnome";
                break;
            if case(5:
                volk = "orc";
                break;
            if case(6:
                volk = "darkelf";
                break;
            if case(7:
                volk = "goblin";
                break;
            if case(8:
                volk = "demon";
                break;
        };
        define_img((VOLK_1_M_IDLE + i),
                  "res/gfx/scr/buildchar/button_" + volk
                  + "_male_idle.jpg", False, pos_x, pos_y);
        DefineCnt((VOLK_1_M_ACT + i), pos_x, pos_y);
        define_img((VOLK_1_F_IDLE + i),
                  "res/gfx/scr/buildchar/button_" + volk
                  + "_female_idle.jpg", False, pos_x, pos_y);
        DefineCnt((VOLK_1_F_ACT + i), pos_x, pos_y);
        add_bunch(VOLK_BTNS_M, (VOLK_1_M_IDLE + i));
        add_bunch(VOLK_BTNS_F, (VOLK_1_F_IDLE + i));
        add_bunch(VOLK_BTNS_ALL, (VOLK_1_M_IDLE + i),
                  (VOLK_1_M_ACT + i), (VOLK_1_F_IDLE + i),
                  (VOLK_1_F_ACT + i));
        actor[(VOLK_1_M_IDLE + i)].add_event_listener(MouseEvent.CLICK,
                                                      SelectRace);
        actor[(VOLK_1_F_IDLE + i)].add_event_listener(MouseEvent.CLICK,
                                                      SelectRace);
        enable_popup((VOLK_1_M_IDLE + i), texts[(TXT_RACENAME + i)]);
        enable_popup((VOLK_1_M_ACT + i), texts[(TXT_RACENAME + i)]);
        enable_popup((VOLK_1_F_IDLE + i), texts[(TXT_RACENAME + i)]);
        enable_popup((VOLK_1_F_ACT + i), texts[(TXT_RACENAME + i)]);
        i = (i + 1);
    };
    i = 0;
    while (i < 10) {
        define_img((CHARBACKGROUND + i), "", False,
                  ((SCREEN_TITLE_X - 150) + CHARX),
                  (SCREEN_TITLE_Y + CHARY));
        define_img((CHARBACKGROUND2 + i), "", False,
                  ((SCREEN_TITLE_X - 150) + CHARX),
                  (SCREEN_TITLE_Y + CHARY));
        i = (i + 1);
    };
    define_btn(MOUTH_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(MOUTH_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(HAIR_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(HAIR_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(BROWS_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(BROWS_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(EYES_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(EYES_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(NOSE_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(NOSE_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(EARS_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(EARS_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(BEARD_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(BEARD_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(SPECIAL_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(SPECIAL_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(SPECIAL2_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(SPECIAL2_PLUS, "", modify_character, btn_classArrowRight);
    define_btn(COLOR_MINUS, "", modify_character, btn_classArrowLeft);
    define_btn(COLOR_PLUS, "", modify_character, btn_classArrowRight);
    i = 0;
    while (i < 10) {
        define_lbl((LBL_MOUTH + i),
                  (((i == 9))
                   ? texts[TXT_COLOR] : ((i)<7)
                   ? texts[(TXT_MOUTH + i)]
                   : texts[((TXT_SPECIAL + i) - 7)]),
                    0, 0, FontFormat_Default);
        add_filter((LBL_MOUTH + i), Filter_Shadow);
        i = (i + 1);
    };
    define_bunch(CHARIMG, CHARBACKGROUND, CHARMOUTH, CHAREARS, CHARBEARD,
                 CHARNOSE, CHAREYES, CHARBROWS, CHARSPECIAL, CHARSPECIAL2,
                 CHARHAIR);
    define_bunch(CHARIMG2, CHARBACKGROUND2, CHARMOUTH2, CHAREARS2,
                 CHARBEARD2, CHARNOSE2, CHAREYES2, CHARBROWS2,
                 CHARSPECIAL12, CHARSPECIAL22, CHARHAIR2);
    define_bunch(CHARSPECIALOVL_ELF_M, CHARBROWS);
    define_bunch(CHARSPECIALOVL_GOBLIN_M, CHARBROWS, CHAREARS, CHARBEARD,
                 CHARMOUTH, CHARNOSE);
    define_bunch(CHARSPECIALOVL_DWARF_M, CHAREYES, CHARSPECIAL, CHARHAIR);
    define_bunch(CHARSPECIALOVL_HUMAN_M, CHARBEARD);
    define_bunch(CHARSPECIALOVL_GOBLIN_F, CHARMOUTH, CHARHAIR, CHARNOSE);
    define_bunch(CHARSPECIALOVL_ORC_F, CHARMOUTH, CHARHAIR);
    define_bunch(CHARSPECIALOVL_ELF_F, CHARNOSE, CHAREYES, CHARBROWS,
                 CHARHAIR, CHAREARS, CHARMOUTH);
    define_bunch(CHARSPECIALOVL_HUMAN_F, CHARBROWS, CHAREYES, CHARHAIR,
                 CHAREARS);
    define_bunch(CHARSPECIALOVL_DWARF_F, CHARBROWS, CHAREYES, CHARHAIR);
    define_bunch(CHARSPECIALOVL_GNOM_M, CHARBEARD, CHARHAIR);
    define_bunch(CHARSPECIALOVL_DARKELF_M, CHAREARS);
    define_bunch(SCREEN_BUILDCHAR, SCR_BUILDCHAR, BLACK_SQUARE,
                 LBL_SCREEN_TITLE, CHARIMG, RANDOM, CREATE_CHARACTER);
    add_bunch(SCREEN_BUILDCHAR, LBL_CREATE_RACE, LBL_CREATE_RACE_DESC,
              LBL_CREATE_CLASS, LBL_CREATE_CLASS_DESC, CREATE_GOTO_LOGIN);
    add_bunch(SCREEN_BUILDCHAR, MOUTH_MINUS, MOUTH_PLUS);
    add_bunch(SCREEN_BUILDCHAR, HAIR_MINUS, HAIR_PLUS);
    add_bunch(SCREEN_BUILDCHAR, COLOR_MINUS, COLOR_PLUS);
    add_bunch(SCREEN_BUILDCHAR, BROWS_MINUS, BROWS_PLUS);
    add_bunch(SCREEN_BUILDCHAR, EYES_MINUS, EYES_PLUS);
    add_bunch(SCREEN_BUILDCHAR, BEARD_MINUS, BEARD_PLUS);
    add_bunch(SCREEN_BUILDCHAR, NOSE_MINUS, NOSE_PLUS);
    add_bunch(SCREEN_BUILDCHAR, EARS_MINUS, EARS_PLUS);
    add_bunch(SCREEN_BUILDCHAR, SPECIAL_MINUS, SPECIAL_PLUS);
    add_bunch(SCREEN_BUILDCHAR, SPECIAL2_MINUS, SPECIAL2_PLUS);
    i = 0;
    while (i < 9) {
        add_bunch(SCREEN_BUILDCHAR, (LBL_MOUTH + i));
        i = (i + 1);
    };
    define_img(SCR_CITY_BACKG_NIGHT,
              "res/gfx/scr/stadt/stadt_nacht_background.jpg",
              False, STADT_BACKG_X, STADT_BACKG_Y);
    define_img(SCR_CITY_BACKG_DAWN,
              "res/gfx/scr/stadt/stadt_abend_background.jpg",
              False, STADT_BACKG_X, STADT_BACKG_Y);
    define_img(SCR_CITY_BACKG_DAY,
              "res/gfx/scr/stadt/stadt_tag_background.jpg",
              False, STADT_BACKG_X, STADT_BACKG_Y);
    define_img(SCR_CITY_MAIN_NIGHT,
              "res/gfx/scr/stadt/stadt_nacht_unten.jpg", False,
              STADT_MAIN_X, STADT_MAIN_Y);
    define_img(SCR_CITY_MAIN_DAWN,
              "res/gfx/scr/stadt/stadt_abend_unten.jpg",
              False, STADT_MAIN_X, STADT_MAIN_Y);
    define_img(SCR_CITY_MAIN_DAY,
              "res/gfx/scr/stadt/stadt_tag_unten.jpg",
              False, STADT_MAIN_X, STADT_MAIN_Y);
    define_img(SCR_CITY_FOREG_NIGHT,
              "res/gfx/scr/stadt/stadt_nacht_vordergrund.png",
              False, STADT_BACKG_X, (STADT_BACKG_Y + STADT_FOREG_Y));
    define_img(SCR_CITY_FOREG_DAWN,
              "res/gfx/scr/stadt/stadt_abend_vordergrund.png",
              False, STADT_BACKG_X, (STADT_BACKG_Y + STADT_FOREG_Y));
    define_img(SCR_CITY_FOREG_DAY,
              "res/gfx/scr/stadt/stadt_tag_vordergrund.png",
              False, STADT_BACKG_X, (STADT_BACKG_Y + STADT_FOREG_Y));
    if (Capabilities.version[0: 3] == "IOS"){
        define_bunch(SCREEN_CITY_NIGHT, SCR_CITY_BACKG_NIGHT,
                     SCR_CITY_MAIN_NIGHT, SCR_CITY_FOREG_NIGHT,
                     CITY_WACHE_NIGHT);
        define_bunch(SCREEN_CITY_DAWN, SCR_CITY_BACKG_DAWN,
                     SCR_CITY_MAIN_DAWN, SCR_CITY_FOREG_DAWN,
                     CITY_WACHE_NIGHT);
        define_bunch(SCREEN_CITY_DAY, SCR_CITY_BACKG_DAY,
                     SCR_CITY_MAIN_DAY, SCR_CITY_FOREG_DAY,
                     CITY_WACHE_DAY);
    } else {
        define_img(SCR_CITY_CLOUDS_NIGHT,
                  "res/gfx/scr/stadt/wolken_nacht.swf", False,
                  STADT_BACKG_X, STADT_BACKG_Y);
        define_img(SCR_CITY_CLOUDS_DAWN,
                  "res/gfx/scr/stadt/wolken_abend.swf", False,
                  STADT_BACKG_X, STADT_BACKG_Y);
        define_img(SCR_CITY_CLOUDS_DAY,
                  "res/gfx/scr/stadt/wolken_tag.swf", False,
                  STADT_BACKG_X, STADT_BACKG_Y);
        define_bunch(SCREEN_CITY_NIGHT,
                     SCR_CITY_BACKG_NIGHT, SCR_CITY_MAIN_NIGHT,
                     SCR_CITY_CLOUDS_NIGHT, SCR_CITY_FOREG_NIGHT,
                     CITY_WACHE_NIGHT);
        define_bunch(SCREEN_CITY_DAWN, SCR_CITY_BACKG_DAWN,
                     SCR_CITY_MAIN_DAWN, SCR_CITY_CLOUDS_DAWN,
                     SCR_CITY_FOREG_DAWN, CITY_WACHE_NIGHT);
        define_bunch(SCREEN_CITY_DAY, SCR_CITY_BACKG_DAY,
                     SCR_CITY_MAIN_DAY, SCR_CITY_CLOUDS_DAY,
                     SCR_CITY_FOREG_DAY, CITY_WACHE_DAY);
    };
    define_img(CITY_SHAKES,
              "res/gfx/scr/stadt/overlay_waffenladen.png",
              False, CITY_SHAKES_X, CITY_SHAKES_Y);
    define_img(CITY_ZAUBERLADEN,
              "res/gfx/scr/stadt/overlay_zauberladen.png",
              False, CITY_ZAUBERLADEN_X, CITY_ZAUBERLADEN_Y);
    define_img(CITY_RUHMESHALLE,
              "res/gfx/scr/stadt/overlay_ruhmeshalle.png",
              False, CITY_RUHMESHALLE_X, CITY_RUHMESHALLE_Y);
    define_img(CITY_ARENA,
              "res/gfx/scr/stadt/arena_glow.png", False,
              CITY_ARENA_X, CITY_ARENA_Y);
    define_img(CITY_ARENA_ONO1,
              "res/gfx/scr/stadt/arena2.png", False, CITY_ARENA_X,
              CITY_ARENA_Y);
    define_img(CITY_ARENA_ONO2,
              "res/gfx/scr/stadt/arena3.png", False, CITY_ARENA_X,
              CITY_ARENA_Y);
    define_img(CITY_ARENA_ONO3,
              "res/gfx/scr/stadt/arena4.png",
              False, CITY_ARENA_X, CITY_ARENA_Y);
    define_img(CITY_ARENA_ONO4,
              "res/gfx/scr/stadt/arena5.png",
               False, CITY_ARENA_X, CITY_ARENA_Y);
    define_img(CITY_DEALER,
              "res/gfx/scr/stadt/dealer_mouseover.png",
              False, CITY_DEALER_X, CITY_DEALER_Y);
    define_img(CITY_DEALER_ANI1,
              "res/gfx/scr/stadt/dealer1.png",
              False, CITY_DEALER_X, CITY_DEALER_Y);
    define_img(CITY_DEALER_ANI2,
              "res/gfx/scr/stadt/dealer2.png",
              False, CITY_DEALER_X, CITY_DEALER_Y);
    define_img(CITY_DEALER_ANI3,
              "res/gfx/scr/stadt/dealer3.png",
              False, CITY_DEALER_X, CITY_DEALER_Y);
    define_img(CITY_DEALER_ANI4,
              "res/gfx/scr/stadt/dealer4.png",
              False, CITY_DEALER_X, CITY_DEALER_Y);
    define_img(CITY_DEALER_ANI5,
              "res/gfx/scr/stadt/dealer5.png",
              False, CITY_DEALER_X, CITY_DEALER_Y);
    define_img(CITY_ESEL1,
              "res/gfx/scr/stadt/esel1.png",
              False, CITY_ESEL_X, CITY_ESEL_Y);
    define_img(CITY_ESEL2,
              "res/gfx/scr/stadt/esel2.png",
              True, CITY_ESEL_X, CITY_ESEL_Y);
    define_img(CITY_TAVERNE,
              "res/gfx/scr/stadt/kneipe.png",
              False, CITY_TAVERNE_X, CITY_TAVERNE_Y);
    define_img(CITY_POST,
              "res/gfx/scr/stadt/post.png",
              False, CITY_POST_X, CITY_POST_Y);
    define_img(CITY_WACHE_DAY,
              "res/gfx/scr/stadt/stadtwache_tag.png",
              False, CITY_WACHE_X, CITY_WACHE_Y);
    define_img(CITY_WACHE_NIGHT,
              "res/gfx/scr/stadt/stadtwache_abend_nacht.png",
              False, CITY_WACHE_X, CITY_WACHE_Y);
    define_img(CITY_SCHILD1,
              "res/gfx/scr/stadt/schild1.png",
              True, CITY_SCHILD_X, CITY_SCHILD_Y);
    define_img(CITY_SCHILD2,
              "res/gfx/scr/stadt/schild2.png",
              True, CITY_SCHILD_X, CITY_SCHILD_Y);
    define_img(CITY_SCHILD3,
              "res/gfx/scr/stadt/schild3.png",
              True, CITY_SCHILD_X, CITY_SCHILD_Y);
    define_img(CITY_SCHILD4,
              "res/gfx/scr/stadt/schild4.png",
              True, CITY_SCHILD_X, CITY_SCHILD_Y);
    define_img(CITY_MAGIER1,
              "res/gfx/scr/stadt/magier1.png",
              False, CITY_MAGIER_X, CITY_MAGIER_Y);
    define_img(CITY_MAGIER2,
              "res/gfx/scr/stadt/magier2.png",
              True, CITY_MAGIER_X, CITY_MAGIER_Y);
    define_img(CITY_ORK1,
              "res/gfx/scr/stadt/ork1.png",
              False, CITY_ORK_X, CITY_ORK_Y);
    define_img(CITY_ORK2,
              "res/gfx/scr/stadt/ork2.png",
              True, CITY_ORK_X, CITY_ORK_Y);
    define_img(CITY_SANDWICH1,
              "res/gfx/scr/stadt/sandwichtyp1.png",
              False, CITY_SANDWICH_X, CITY_SANDWICH_Y);
    define_img(CITY_SANDWICH2,
              "res/gfx/scr/stadt/sandwichtyp2.png",
              True, CITY_SANDWICH_X, CITY_SANDWICH_Y);
    define_img(CITY_ZWERG1,
              "res/gfx/scr/stadt/zwerg2.png",
              False, CITY_ZWERG_X, CITY_ZWERG_Y);
    define_img(CITY_ZWERG2,
              "res/gfx/scr/stadt/zwerg1.png",
              True, CITY_ZWERG_X, CITY_ZWERG_Y);
    define_img(CITY_ELF1,
              "res/gfx/scr/stadt/elf1.png", False,
              CITY_ELF_X, CITY_ELF_Y);
    define_img(CITY_ELF2,
              "res/gfx/scr/stadt/elf2.png",
              True, CITY_ELF_X, CITY_ELF_Y);
    define_bunch(CITY_STATISTEN, CITY_MAGIER1, CITY_MAGIER2, CITY_ORK1,
                 CITY_ORK2, CITY_SANDWICH1, CITY_SANDWICH2);
    add_bunch(CITY_STATISTEN, CITY_ZWERG1, CITY_ZWERG2, CITY_ELF1,
              CITY_ELF2, CITY_ZWERG, CITY_ORK);
    add_bunch(CITY_STATISTEN, CITY_SCHILD1, CITY_SCHILD2, CITY_SCHILD3,
              CITY_SCHILD4);
    define_bunch(CITY_CA_OVL, IF_OVL, CA_CITY_SHAKES, CA_CITY_ZAUBERLADEN,
                 CA_CITY_RUHMESHALLE, CA_CITY_ARENA, CA_CITY_DEALER,
                 CA_CITY_ESEL, CA_CITY_TAVERNE, CA_CITY_POST,
                 CA_CITY_WACHE, CA_CITY_BUH);
    define_click_area(CA_CITY_SHAKES, CITY_SHAKES, interface_btn_handler,
                    CITY_CA_SHAKES_X, CITY_CA_SHAKES_Y, CITY_CA_SHAKES_X,
                    CITY_CA_SHAKES_Y, CITY_CA_OVL);
    define_click_area(CA_CITY_ZAUBERLADEN, CITY_ZAUBERLADEN,
                    interface_btn_handler, CITY_CA_ZAUBERLADEN_X,
                    CITY_CA_ZAUBERLADEN_Y, CITY_CA_ZAUBERLADEN_X,
                    CITY_CA_ZAUBERLADEN_Y, CITY_CA_OVL);
    define_click_area(CA_CITY_RUHMESHALLE, CITY_RUHMESHALLE,
                    interface_btn_handler, CITY_CA_RUHMESHALLE_X,
                    CITY_CA_RUHMESHALLE_Y, (CITY_CA_RUHMESHALLE_X - 45),
                    CITY_CA_RUHMESHALLE_Y, CITY_CA_OVL);
    define_click_area(CA_CITY_ARENA, CITY_ARENA, interface_btn_handler,
                    CITY_CA_ARENA_X, CITY_CA_ARENA_Y, CITY_CA_ARENA_X,
                    CITY_CA_ARENA_Y, CITY_CA_OVL, ShowArenaOno,
                    HideArenaOno);
    define_click_area(CA_CITY_DEALER, CITY_DEALER, interface_btn_handler,
                    CITY_CA_DEALER_X, CITY_CA_DEALER_Y, CITY_CA_DEALER_X,
                    CITY_CA_DEALER_Y, CITY_CA_OVL, HideDealerEyes,
                    ShowDealerEyes);
    define_click_area(CA_CITY_ESEL, CITY_ESEL2, interface_btn_handler,
                    CITY_CA_ESEL_X, CITY_CA_ESEL_Y, CITY_CA_ESEL_X,
                    CITY_CA_ESEL_Y, CITY_CA_OVL, EselOver, EselOut);
    define_click_area(CA_CITY_TAVERNE, CITY_TAVERNE, interface_btn_handler,
                    CITY_CA_TAVERNE_X, CITY_CA_TAVERNE_Y,
                    CITY_CA_TAVERNE_X, CITY_CA_TAVERNE_Y, CITY_ZWERG);
    define_click_area(CA_CITY_POST, CITY_POST, interface_btn_handler,
                    CITY_CA_POST_X, CITY_CA_POST_Y, CITY_CA_POST_X,
                    CITY_CA_POST_Y, CITY_ORK);
    define_click_area(CA_CITY_WACHE, C_EMPTY, interface_btn_handler,
                    CITY_CA_WACHE_X, CITY_CA_WACHE_Y, CITY_CA_WACHE_X,
                    CITY_CA_WACHE_Y, CITY_CA_OVL, WacheOver, WacheOut);
    define_click_area(CA_CITY_BUH, C_EMPTY, interface_btn_handler,
                    CITY_CA_BUH_X, CITY_CA_BUH_Y, CITY_CA_BUH_X,
                    CITY_CA_BUH_Y, CITY_CA_OVL, BuhHover, BuhOut);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_SHAKES);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_ZAUBERLADEN);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_RUHMESHALLE);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_ARENA);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_DEALER);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_ESEL);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_TAVERNE);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_POST);
    AddMimickInterfaceButtonHoverHandler(CA_CITY_WACHE);
    define_bunch(CITY_OVERLAYS, CITY_SHAKES, CITY_ZAUBERLADEN,
                 CITY_RUHMESHALLE, CITY_ARENA, CITY_DEALER, CITY_ESEL2,
                 CITY_TAVERNE, CITY_POST);
    define_bunch(SCREEN_CITY, IF_MAIN, CA_CITY_SHAKES, CA_CITY_ZAUBERLADEN,
                 CA_CITY_RUHMESHALLE, CA_CITY_ARENA, CITY_DEALER_ANI5,
                 CA_CITY_DEALER, CITY_ESEL1, CA_CITY_ESEL, CITY_CA_OVL,
                 CA_CITY_TAVERNE, CA_CITY_POST, CA_CITY_BUH);
    define_bunch(CITY_ZWERG);
    define_bunch(CITY_ORK);
    Buh = False;
    if (lang_code == "de"){
        define_img(BUBBLE_ARENA,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_arena.png"),
                    False, BUBBLE_ARENA_X, BUBBLE_ARENA_Y);
        define_img(BUBBLE_ESEL,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_esel.png"),
                    False, BUBBLE_ESEL_X, BUBBLE_ESEL_Y);
        define_img(BUBBLE_TAVERNE,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_gasthaus.png"),
                    False, BUBBLE_TAVERNE_X, BUBBLE_TAVERNE_Y);
        define_img(BUBBLE_RUHMESHALLE,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_heldenhalle.png"),
                    False, BUBBLE_RUHMESHALLE_X, BUBBLE_RUHMESHALLE_Y);
        define_img(BUBBLE_KRISTALL,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_kristall.png"),
                    False, BUBBLE_KRISTALL_X, BUBBLE_KRISTALL_Y);
        define_img(BUBBLE_ORAKEL,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_orakel.png"),
                    False, BUBBLE_ORAKEL_X, BUBBLE_ORAKEL_Y);
        define_img(BUBBLE_DEALER,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_pilzdealer.png"),
                    False, BUBBLE_DEALER_X, BUBBLE_DEALER_Y);
        define_img(BUBBLE_POST,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_post.png"),
                    False, BUBBLE_POST_X, BUBBLE_POST_Y);
        define_img(BUBBLE_WACHE,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_stadtwache.png"),
                    False, BUBBLE_WACHE_X, BUBBLE_WACHE_Y);
        define_img(BUBBLE_STATUE,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_statue.png"),
                    False, BUBBLE_STATUE_X, BUBBLE_STATUE_Y);
        define_img(BUBBLE_SHAKES,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_waffenladen.png"),
                    False, BUBBLE_SHAKES_X, BUBBLE_SHAKES_Y);
        define_img(BUBBLE_ZAUBERLADEN,
                  (("res/gfx/scr/stadt/" + lang_code)
                   + "/bubble_zauberladen.png"), False,
                    BUBBLE_ZAUBERLADEN_X, BUBBLE_ZAUBERLADEN_Y);
    } else {
        define_img(BUBBLE_ARENA,
                  "res/gfx/empty.png",
                  False, BUBBLE_ARENA_X, BUBBLE_ARENA_Y);
        define_img(BUBBLE_ESEL,
                  "res/gfx/empty.png",
                  False, BUBBLE_ESEL_X, BUBBLE_ESEL_Y);
        define_img(BUBBLE_TAVERNE,
                  "res/gfx/empty.png",
                  False, BUBBLE_TAVERNE_X, BUBBLE_TAVERNE_Y);
        define_img(BUBBLE_RUHMESHALLE,
                  "res/gfx/empty.png",
                  False, BUBBLE_RUHMESHALLE_X, BUBBLE_RUHMESHALLE_Y);
        define_img(BUBBLE_KRISTALL,
                  "res/gfx/empty.png",
                  False, BUBBLE_KRISTALL_X, BUBBLE_KRISTALL_Y);
        define_img(BUBBLE_ORAKEL, "res/gfx/empty.png",
                  False, BUBBLE_ORAKEL_X, BUBBLE_ORAKEL_Y);
        define_img(BUBBLE_DEALER, "res/gfx/empty.png",
                  False, BUBBLE_DEALER_X, BUBBLE_DEALER_Y);
        define_img(BUBBLE_POST, "res/gfx/empty.png",
                  False, BUBBLE_POST_X, BUBBLE_POST_Y);
        define_img(BUBBLE_WACHE, "res/gfx/empty.png",
                  False, BUBBLE_WACHE_X, BUBBLE_WACHE_Y);
        define_img(BUBBLE_STATUE, "res/gfx/empty.png",
                  False, BUBBLE_STATUE_X, BUBBLE_STATUE_Y);
        define_img(BUBBLE_SHAKES, "res/gfx/empty.png",
                  False, BUBBLE_SHAKES_X, BUBBLE_SHAKES_Y);
        define_img(BUBBLE_ZAUBERLADEN, "res/gfx/empty.png",
                  False, BUBBLE_ZAUBERLADEN_X, BUBBLE_ZAUBERLADEN_Y);
    };
    define_bunch(BUBBLES, BUBBLE_ARENA, BUBBLE_ESEL, BUBBLE_TAVERNE,
                 BUBBLE_RUHMESHALLE, BUBBLE_KRISTALL, BUBBLE_ORAKEL);
    add_bunch(BUBBLES, BUBBLE_DEALER, BUBBLE_POST, BUBBLE_WACHE,
              BUBBLE_STATUE, BUBBLE_SHAKES, BUBBLE_ZAUBERLADEN);
    BubbleTimer = new Timer(20);
    BubbleWait = 0;
    BubbleTimer.add_event_listener(TimerEvent.TIMER, Bubbles);
    BubbleTimer.start();
    CityAniTimer = new Timer(400);
    CityAniFrame = 0;
    SandwichPause = 0;
    ZwergFussTapp = 0;
    CityAniTimer.add_event_listener(TimerEvent.TIMER, CityAni);
    CityAniTimer.start();
    iFrame = -1;
    SchildDir = 1;
    SchildTimer = new Timer(100);
    DealerAniTimer = new Timer(4000);
    DealerStepTimer = new Timer(100);
    DealerAniStep = 0;
    _local2 = DealerAniTimer;
    with (_local2) {
        add_event_listener(TimerEvent.TIMER, DealerAni);
        if (!light_mode){
            start();
        } else {
            stop();
        };
    };
    LastOno = 0;
    ThisOno = LastOno;
    OnoPopupTimer = new Timer(50);
    PopupDir = False;
    define_btn(IF_EXIT, "", ExitScreen, btn_classExitScreen,
               IF_EXIT_X, IF_EXIT_Y);
    define_img(SCR_HALLE_BG, "res/gfx/scr/hall/heldenhalle.jpg",
              False, 280, 100);
    define_btn(HALLE_UP, "", RuhmesHalleScroll, btn_classArrowUp,
               HALLE_UPDOWN_X, HALLE_UP_Y);
    define_btn(HALLE_DOWN, "", RuhmesHalleScroll, btn_classArrowDown,
               HALLE_UPDOWN_X, HALLE_DOWN_Y);
    define_btn(HALLE_GOTO, texts[TXT_HALLE_GOTO], RuhmesHalleScroll,
               btn_classLOGin, HALLE_GOTO_X, HALLE_GOTO_Y);
    define_from_class(INP_HALLE_GOTO, text_input1, HALLE_INP_GOTO_X,
                    HALLE_INP_GOTO_Y, 2, "name");
    actor[INP_HALLE_GOTO].add_event_listener(KeyboardEvent.KEY_DOWN,
                                             RuhmesHalleScroll);
    actor[INP_HALLE_GOTO].add_event_listener(MouseEvent.CLICK,
                                             HalleSuchClick);
    DefineCnt(HALL_GOTO_SPIELER, 0, HALLE_GOTO_SPIELERGILDEN_Y);
    DefineCnt(HALL_GOTO_GILDEN, HALLE_GOTO_GILDEN_X,
              HALLE_GOTO_SPIELERGILDEN_Y);
    define_lbl(LBL_HALL_GOTO_SPIELER, texts[TXT_GOTO_SPIELER], 0, 0,
              FontFormat_LOGoutLink);
    add_filter(LBL_HALL_GOTO_SPIELER, Filter_Shadow);
    define_lbl(LBL_HALL_GOTO_GILDEN, texts[TXT_GOTO_GILDEN], 0, 0,
              FontFormat_LOGoutLink);
    add_filter(LBL_HALL_GOTO_GILDEN, Filter_Shadow);
    define_lbl(LBL_HALL_GOTO_SPIELER_HL, texts[TXT_GOTO_SPIELER], 0, 0,
              FontFormat_LOGoutLinkHighLight);
    add_filter(LBL_HALL_GOTO_SPIELER_HL, Filter_Shadow);
    define_lbl(LBL_HALL_GOTO_GILDEN_HL, texts[TXT_GOTO_GILDEN], 0, 0,
              FontFormat_LOGoutLinkHighLight);
    add_filter(LBL_HALL_GOTO_GILDEN_HL, Filter_Shadow);
    MakePersistent(LBL_HALL_GOTO_SPIELER, LBL_HALL_GOTO_GILDEN);
    MakePersistent(LBL_HALL_GOTO_SPIELER_HL, LBL_HALL_GOTO_GILDEN_HL);
    _local2 = actor[HALL_GOTO_SPIELER];
    with (_local2) {
        addChild(actor[LBL_HALL_GOTO_SPIELER]);
        addChild(actor[LBL_HALL_GOTO_SPIELER_HL]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, RuhmesHalleScroll);
        x = (HALLE_GOTO_SPIELER_X
             - actor[LBL_HALL_GOTO_SPIELER].text_width);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    _local2 = actor[HALL_GOTO_GILDEN];
    with (_local2) {
        addChild(actor[LBL_HALL_GOTO_GILDEN]);
        addChild(actor[LBL_HALL_GOTO_GILDEN_HL]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, RuhmesHalleScroll);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    DefineCnt(HALL_LIST, HALL_LIST_X, HALL_LIST_Y);
    define_bunch(SCREEN_HALLE, SCR_HALLE_BG, IF_OVL, IF_EXIT, HALLE_UP,
                 HALLE_DOWN, HALLE_GOTO, INP_HALLE_GOTO, HALL_LIST,
                 HALL_GOTO_SPIELER, HALL_GOTO_GILDEN);
    define_click_area(CA_SCR_ARBEITEN_BLOCKCITY, C_EMPTY,
                    interface_btn_handler, 280, 100, (RES_X - 280),
                    (RES_Y - 100));
    _local2 = actor[CA_SCR_ARBEITEN_BLOCKCITY];
    with (_local2) {
        useHandCursor = False;
        buttonMode = False;
    };
    define_lbl(LBL_SCR_ARBEITEN_TEXT, texts[TXT_ARBEIT_TEXT],
              LBL_ARBEITEN_TEXT_X, LBL_ARBEITEN_TEXT_Y,
              FontFormat_Default);
    define_lbl(LBL_SCR_ARBEITEN_TEXT2, "", LBL_ARBEITEN_TEXT_X,
              LBL_ARBEITEN_TEXT2_Y, FontFormat_Default);
    actor[LBL_SCR_ARBEITEN_TEXT].width = LBL_ARBEITEN_TEXT_X;
    actor[LBL_SCR_ARBEITEN_TEXT].wordWrap = True;
    actor[LBL_SCR_ARBEITEN_TEXT2].width = LBL_ARBEITEN_TEXT_X;
    actor[LBL_SCR_ARBEITEN_TEXT2].wordWrap = True;
    add_filter(LBL_SCR_ARBEITEN_TEXT, Filter_Shadow);
    add_filter(LBL_SCR_ARBEITEN_TEXT2, Filter_Shadow);
    define_lbl(LBL_SCR_ARBEITEN_TIME, "", 0,
              (IF_WIN_Y + LBL_ARBEITEN_TIME_Y), FontFormat_Default);
    add_filter(LBL_SCR_ARBEITEN_TIME, Filter_Shadow);
    DefineCnt(SCR_ARBEITEN_BAR, (IF_WIN_X + ARBEITEN_BAR_X),
              (IF_WIN_Y + ARBEITEN_BAR_Y));
    DefineCnt(SCR_ARBEITEN_FILL, (IF_WIN_X + ARBEITEN_FILL_X),
              (IF_WIN_Y + ARBEITEN_FILL_Y));
    DefineSlider(SLDR['ARBEITEN'], 10, ARBEITEN_SLIDER_X,
                 ARBEITEN_SLIDER_Y, arbeiten_slider_change);
    define_btn(SCR_ARBEITEN_OK, texts[TXT_OK], request_arbeiten,
               btn_classBasic, ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (IF_WIN_Y + ARBEITEN_Y));
    define_btn(SCR_ARBEITEN_CLOSE, texts[TXT_OK], ShowCityScreen,
               btn_classBasic, ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (IF_WIN_Y + ARBEITEN_Y));
    define_btn(SCR_ARBEITEN_CANCEL, texts[TXT_ABBRECHEN],
               request_cancel_arbeiten, btn_classBasic,
               ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (IF_WIN_Y + ARBEITEN_Y));
    define_bunch(SCREEN_ARBEITEN, CA_SCR_ARBEITEN_BLOCKCITY, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_SCR_ARBEITEN_TEXT, SLDR['ARBEITEN'],
                 LBL_SCR_ARBEITEN_TEXT2, SCR_ARBEITEN_OK, IF_EXIT);
    define_bunch(SCREEN_ARBEITEN_WAIT, CA_SCR_ARBEITEN_BLOCKCITY,
                 IF_WINDOW, LBL_WINDOW_TITLE, LBL_SCR_ARBEITEN_TEXT,
                 SCR_ARBEITEN_BAR, SCR_ARBEITEN_FILL,
                 LBL_SCR_ARBEITEN_TIME, SCR_ARBEITEN_CANCEL, IF_EXIT);
    define_bunch(SCREEN_ARBEITEN_SUCCESS, CA_SCR_ARBEITEN_BLOCKCITY,
                 IF_WINDOW, LBL_WINDOW_TITLE, LBL_SCR_ARBEITEN_TEXT,
                 LBL_SCR_ARBEITEN_TEXT2, SCR_ARBEITEN_CLOSE, IF_EXIT);
    define_click_area(CA_SCR_INVITE_BLOCKCITY, C_EMPTY, interface_btn_handler,
                    280, 100, (RES_X - 280), (RES_Y - 100));
    _local2 = actor[CA_SCR_INVITE_BLOCKCITY];
    with (_local2) {
        useHandCursor = False;
        buttonMode = False;
    };
    define_lbl(LBL_INVITE_SUCCESS, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (420 / 2)),
              ((IF_WIN_Y + ARENA_TEXT_Y) + AIRRelMoveY),
              FontFormat_Default);
    add_filter(LBL_INVITE_SUCCESS, Filter_Shadow);
    _local2 = actor[LBL_INVITE_SUCCESS];
    with (_local2) {
        wordWrap = True;
        width = 420;
        text = texts[TXT_INVITESUCCESS];
    };
    define_lbl(LBL_INVITE_TEXT, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (420 / 2)),
              ((IF_WIN_Y + ARENA_TEXT_Y) + AIRRelMoveY),
              FontFormat_Default);
    add_filter(LBL_INVITE_TEXT, Filter_Shadow);
    _local2 = actor[LBL_INVITE_TEXT];
    with (_local2) {
        wordWrap = True;
        width = 420;
        text = texts[TXT_INVITEINSTR];
    };
    define_from_class(INP_CHAR_INVITE, text_input1, 0,
                    (((IF_WIN_Y + ARENA_INP_Y) - 40) + AIRRelMoveY),
                    2, "email");
    _local2 = actor[INP_CHAR_INVITE];
    with (_local2) {
        getChildAt(1).text = "";
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2))) + 40);
        add_event_listener(KeyboardEvent.KEY_DOWN, SendPlayerInvite);
    };
    define_lbl(LBL_INVITE_TEXT2, texts[TXT_INVITEEMAIL], 0,
              ((actor[INP_CHAR_INVITE].y + 10) + AIRRelMoveY),
              FontFormat_Default);
    add_filter(LBL_INVITE_TEXT2, Filter_Shadow);
    actor[LBL_INVITE_TEXT2].x = ((actor[INP_CHAR_INVITE].x
                                 - actor[LBL_INVITE_TEXT2].width) - 5);
    define_from_class(INP_CHAR_INVITE2, text_input1, 0,
                    (((IF_WIN_Y + ARENA_INP_Y) + 10) + AIRRelMoveY),
                    2, "text");
    _local2 = actor[INP_CHAR_INVITE2];
    with (_local2) {
        getChildAt(1).text = "";
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2))) + 40);
        add_event_listener(KeyboardEvent.KEY_DOWN, SendPlayerInvite);
    };
    define_lbl(LBL_INVITE_TEXT3, texts[TXT_INVITESUBJECT], 0,
              ((actor[INP_CHAR_INVITE2].y + 10) + AIRRelMoveY),
              FontFormat_Default);
    add_filter(LBL_INVITE_TEXT3, Filter_Shadow);
    actor[LBL_INVITE_TEXT3].x = ((actor[INP_CHAR_INVITE2].x
                                 - actor[LBL_INVITE_TEXT3].width) - 5);
    define_btn(SCR_INVITE_OK, texts[TXT_OK], SendPlayerInvite,
               btn_classBasic, ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (((IF_WIN_Y + ARBEITEN_Y) + 15) + AIRRelMoveY));
    define_btn(INVITE_SUCCESS_OK, texts[TXT_OK], RemoveInviteWindow,
               btn_classBasic, ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (((IF_WIN_Y + ARBEITEN_Y) + 15) + AIRRelMoveY));
    define_bunch(SCREEN_INVITE, CA_SCR_INVITE_BLOCKCITY, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_INVITE_TEXT, INP_CHAR_INVITE,
                 LBL_INVITE_TEXT2, INP_CHAR_INVITE2, LBL_INVITE_TEXT3,
                 SCR_INVITE_OK, IF_EXIT, LBL_INVITE_SUCCESS,
                 INVITE_SUCCESS_OK);
    define_bunch(INVITE_INPUTDIALOGUE, LBL_INVITE_TEXT, INP_CHAR_INVITE,
                 LBL_INVITE_TEXT2, INP_CHAR_INVITE2, LBL_INVITE_TEXT3,
                 SCR_INVITE_OK);
    define_bunch(INVITE_SUCCESS, LBL_INVITE_SUCCESS, INVITE_SUCCESS_OK);
    define_img(ALBUM_BG, "res/gfx/scr/album/album.jpg", False, 280, 100);
    define_lbl(LBL_ALBUM_PAGENUMBER_LEFT, "", 340, 690, FontFormat_Book);
    define_lbl(LBL_ALBUM_PAGENUMBER_RIGHT, "", 0, 690, FontFormat_Book);
    define_lbl(LBL_ALBUM_COLLECTION, "", 330, 135, FontFormat_BookLeft);
    define_bunch(SCREEN_ALBUM, ALBUM_BG, IF_OVL, IF_EXIT,
                 LBL_ALBUM_PAGENUMBER_LEFT, LBL_ALBUM_PAGENUMBER_RIGHT,
                 LBL_ALBUM_COLLECTION);
    define_img(UNKNOWN_enemy, "res/gfx/scr/fight/monster/unknown.jpg",
              False, 0, 0);
    i = 0;
    while (i < 4) {
        define_lbl((LBL_ALBUM_HEADING + i), "", 0,
                  (((i % 2))==0) ? 135 : 440, FontFormat_Book);
        define_lbl((LBL_ALBUM_HINT + i), "", 0,
                  (((i % 2))==0) ? 165 : 470, FontFormat_BookHint);
        DefineCnt((ALBUM_MONSTER + i),
                  ((i)<=1) ? 420 : 890, (((i % 2))==0) ? 170 : 475);
        DefineCnt((ALBUM_MONSTER_FRAME + i),
                  (actor[(ALBUM_MONSTER + i)].x - 8),
                  (actor[(ALBUM_MONSTER + i)].y - 8));
        actor[(ALBUM_MONSTER + i)].scaleX = 0.8;
        actor[(ALBUM_MONSTER + i)].scaleY = 0.8;
        actor[(ALBUM_MONSTER_FRAME + i)].scaleX = 0.8;
        actor[(ALBUM_MONSTER_FRAME + i)].scaleY = 0.8;
        DefineCnt((ALBUM_WEAPON_1 + i),
                  (actor[(ALBUM_MONSTER + i)].x + 25),
                  (actor[(ALBUM_MONSTER + i)].y
                   + (((i % 2))==0) ? 10 : 130));
        DefineCnt((ALBUM_WEAPON_2 + i),
                  (actor[(ALBUM_MONSTER + i)].x + 135),
                  (actor[(ALBUM_MONSTER + i)].y
                   + (((i % 2))==0) ? 10 : 130));
        DefineCnt((ALBUM_WEAPON_3 + i),
                  (actor[(ALBUM_MONSTER + i)].x - 30),
                  (actor[(ALBUM_MONSTER + i)].y
                   + (((i % 2))==0) ? 130 : 10));
        DefineCnt((ALBUM_WEAPON_4 + i),
                  (actor[(ALBUM_MONSTER + i)].x + 75),
                  (actor[(ALBUM_MONSTER + i)].y
                   + (((i % 2))==0) ? 130 : 10));
        DefineCnt((ALBUM_WEAPON_5 + i),
                  (actor[(ALBUM_MONSTER + i)].x + 180),
                  (actor[(ALBUM_MONSTER + i)].y
                   + (((i % 2))==0) ? 130 : 10));
        DefineCnt((ALBUM_WEAPON_EPIC + i),
                  (actor[(ALBUM_MONSTER + i)].x + 75),
                  (actor[(ALBUM_MONSTER + i)].y + 70));
        add_bunch(SCREEN_ALBUM, (LBL_ALBUM_HEADING + i),
                  (LBL_ALBUM_HINT + i), (ALBUM_MONSTER + i),
                  (ALBUM_MONSTER_FRAME + i));
        add_bunch(SCREEN_ALBUM, (ALBUM_WEAPON_1 + i),
                  (ALBUM_WEAPON_2 + i), (ALBUM_WEAPON_3 + i));
        add_bunch(SCREEN_ALBUM, (ALBUM_WEAPON_4 + i),
                  (ALBUM_WEAPON_5 + i), (ALBUM_WEAPON_EPIC + i));
        i = (i + 1);
    };
    define_bunch(ALBUM_CAT_IN);
    i = 0;
    while (i < 5) {
        define_img((ALBUM_CAT_OUT + i),
                  (("res/gfx/scr/album/tab_" + str(i)) + "_out.jpg"),
                  False, 0, 0);
        define_img((ALBUM_CAT_IN + i),
                  (("res/gfx/scr/album/tab_" + str(i)) + "_in.jpg"),
                  False, 290, (300 + (i * 80)));
        DefineCnt((ALBUM_CAT_OUT + i), 290, (300 + (i * 80)));
        MakePersistent((ALBUM_CAT_OUT + i));
        _local2 = actor[(ALBUM_CAT_OUT + i)];
        with (_local2) {
            addChild(actor[(ALBUM_CAT_OUT + i)]);
            add_event_listener(MouseEvent.CLICK, Showalbum_content);
            mouseChildren = False;
            buttonMode = True;
            useHandCursor = True;
        };
        enable_popup((ALBUM_CAT_IN + i),
                     texts[((TXT_COLLECTION + 2) + i)]);
        enable_popup((ALBUM_CAT_OUT + i),
                     texts[((TXT_COLLECTION + 2) + i)]);
        add_bunch(ALBUM_CAT_IN, (ALBUM_CAT_IN + i));
        add_bunch(SCREEN_ALBUM, (ALBUM_CAT_OUT + i), (ALBUM_CAT_IN + i));
        i = (i + 1);
    };
    define_btn(ALBUM_PREV, "", Showalbum_content,
               btn_classArrowLeft, 340, 715);
    define_btn(ALBUM_NEXT, "", Showalbum_content,
               btn_classArrowRight, 1180, 715);
    add_bunch(SCREEN_ALBUM, ALBUM_PREV, ALBUM_NEXT);
    define_img(SCR_CHAR_BG, "res/gfx/scr/char/charbg.jpg",
              False, 280, 100);
    define_img(SCR_CHAR_BG_GOLDEN, "res/gfx/scr/char/gold_bg.jpg",
              False, 280, 100);
    define_img(SCR_CHAR_BG_RIGHT,
              "res/gfx/scr/char/character_right_new.jpg",
              False, (280 + 500), 100);
    i = 0;
    while (i < 13) {
        define_img((MIRROR_PIECE + i),
                  (("res/gfx/scr/char/mirror/mirror"
                   + str((i + 1))) + ".png"),
                    False, SCR_CHAR_CHARX, SCR_CHAR_CHARY);
        actor[(MIRROR_PIECE + i)].alpha = 0.3;
        actor[(MIRROR_PIECE + i)].mouse_enabled = False;
        i = (i + 1);
    };
    define_img(GOLDEN_FRAME, "res/gfx/scr/char/gold_frame.png",
              False, (SCR_CHAR_CHARX - 3), (SCR_CHAR_CHARY - 5));
    define_click_area(CA_SELL_ITEM, C_EMPTY, None,
                    (280 + 550), 100, 450, 700);
    define_click_area(CA_USE_ITEM, C_EMPTY, None, 280, 100, 500, 415);
    DefineCnt(SCR_CHAR_NAME, CHAR_NAME_X, CHAR_NAME_Y);
    define_lbl(LBL_SCR_CHAR_NAME, "", 0, 0, FontFormat_Default);
    MakePersistent(LBL_SCR_CHAR_NAME);
    _local2 = actor[SCR_CHAR_NAME];
    with (_local2) {
        addChild(actor[LBL_SCR_CHAR_NAME]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, Gotoplayer_gilde);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    define_btn(PREV_PLAYER, "", PrevPlayer, btn_classArrowLeft,
               (SCR_CHAR_CHARX + 10), (SCR_CHAR_CHARY + 10));
    define_btn(NEXT_PLAYER, "", NextPlayer, btn_classArrowRight,
               (SCR_CHAR_CHARX + 215), (SCR_CHAR_CHARY + 10));
    define_from_class(SHP_BLACK_GILDEEHRE, black_square_neutral, GILDEEHRE_X,
                    GILDEEHRE_Y);
    _local2 = actor[SHP_BLACK_GILDEEHRE];
    with (_local2) {
        width = GILDEEHRE_X;
        height = GILDEEHRE_Y;
        alpha = 0.65;
    };
    DefineCnt(SCR_CHAR_GILDE, ((GILDEEHRE_X + GILDEEHRE_X) + 40),
              (GILDEEHRE_Y + GILDEEHRE_Y));
    define_lbl(LBL_SCR_CHAR_GILDE, "", 0, 0, FontFormat_Default);
    MakePersistent(LBL_SCR_CHAR_GILDE);
    _local2 = actor[SCR_CHAR_GILDE];
    with (_local2) {
        addChild(actor[LBL_SCR_CHAR_GILDE]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, JumpToPlayerHall);
        mouse_enabled = True;
        buttonMode = True;
        useHandCursor = True;
        mouseChildren = False;
    };
    define_img(SLOT_SUGGESTION, "res/gfx/scr/char/slot_suggestion.png",
              False, 0, 0);
    actor[SLOT_SUGGESTION].mouse_enabled = False;
    define_lbl(LBL_SCR_CHAR_EHRE, "", 0, (GILDEEHRE_Y + GILDEEHRE_Y),
              FontFormat_Default);
    define_img(SCR_CHAR_KLASSE_1, "res/gfx/scr/char/char_krieger.jpg",
              False, ((GILDEEHRE_X + GILDEEHRE_X) - 10),
              ((GILDEEHRE_Y + GILDEEHRE_Y) - 10));
    define_img(SCR_CHAR_KLASSE_2, "res/gfx/scr/char/char_magier.jpg",
              False, ((GILDEEHRE_X + GILDEEHRE_X) - 10),
              ((GILDEEHRE_Y + GILDEEHRE_Y) - 10));
    define_img(SCR_CHAR_KLASSE_3, "res/gfx/scr/char/char_dieb.jpg",
              False, ((GILDEEHRE_X + GILDEEHRE_X) - 10),
              ((GILDEEHRE_Y + GILDEEHRE_Y) - 10));
    enable_popup(SCR_CHAR_KLASSE_1, texts[TXT_CLASSNAME]);
    enable_popup(SCR_CHAR_KLASSE_2, texts[(TXT_CLASSNAME + 1)]);
    enable_popup(SCR_CHAR_KLASSE_3, texts[(TXT_CLASSNAME + 2)]);
    define_from_class(SHP_BLACK_CHARDESC, black_square_neutral,
                    GILDEEHRE_X,
                    ((GILDEEHRE_Y + GILDEEHRE_Y) + BLACK_CHARDESC_Y));
    _local2 = actor[SHP_BLACK_CHARDESC];
    with (_local2) {
        width = BLACK_CHARDESC_X;
        height = BLACK_CHARDESC_Y;
        alpha = 0.65;
    };
    define_from_class(INP_CHARDESC, SimpleTextAreaSmall,
                    (GILDEEHRE_X + GILDEEHRE_X),
                    (((GILDEEHRE_Y + GILDEEHRE_Y) + BLACK_CHARDESC_Y)
                     + GILDEEHRE_Y), 1, "text");
    CleanupField(INP_CHARDESC);
    add_filter(INP_CHARDESC, Filter_Shadow);
    _local2 = actor[INP_CHARDESC];
    with (_local2) {
        mouse_enabled = True;
        add_event_listener(FocusEvent.FOCUS_IN, Enterplayer_desc);
        add_event_listener(FocusEvent.FOCUS_OUT, Leaveplayer_desc);
    };
    define_lbl(LBL_CHAR_DELAY, "", 0, (100 + CHAR_DELAY_Y),
              FontFormat_Default);
    add_filter(LBL_CHAR_DELAY, Filter_Shadow);
    define_bunch(CHAR_RIGHTPANE, SCR_CHAR_BG_RIGHT, IF_OVL,
                 SCR_CHAR_KLASSE_1, SCR_CHAR_KLASSE_2, SCR_CHAR_KLASSE_3,
                 SCR_CHAR_GILDE, LBL_SCR_CHAR_EHRE, INP_CHARDESC);
    add_filter(LBL_SCR_CHAR_NAME, Filter_Shadow);
    add_filter(LBL_SCR_CHAR_GILDE, Filter_Shadow);
    add_filter(LBL_SCR_CHAR_EHRE, Filter_Shadow);
    define_img(SCR_CHAR_EXPBAR, "res/gfx/scr/char/experience.jpg", False,
              EXPERIENCE_BAR_X, EXPERIENCE_BAR_Y);
    define_lbl(LBL_SCR_CHAR_EXPLABEL, "", 0, (EXPERIENCE_BAR_Y + 2),
              FontFormat_LifeBar);
    add_filter(LBL_SCR_CHAR_EXPLABEL, Filter_Shadow);
    define_click_area(CA_SCR_CHAR_EXPBAR, C_EMPTY, None, EXPERIENCE_BAR_X,
                    EXPERIENCE_BAR_Y, 254, 24);
    define_btn(CHAR_MESSAGE, texts[TXT_MESSAGE], PlayerSendMessage,
               btn_classBasic, CHAR_PLAYERX1, CHAR_PLAYERY);
    define_btn(CHAR_ATTACK, texts[TXT_ATTACK], PlayerAttack,
               btn_classBasic, CHAR_PLAYERX2, CHAR_PLAYERY);
    define_btn(CHAR_GILDE, texts[TXT_ZURGILDE], ZurGilde, btn_classBasic,
               CHAR_PLAYERX2, CHAR_PLAYERY);
    define_btn(CHAR_ALBUM, texts[TXT_ALBUM], RequestAlbum, btn_classBasic,
               CHAR_PLAYERX1, CHAR_PLAYERY);
    define_btn(PLAYER_GUILD_INVITE, "", PlayerGuildInvite, btn_classInvite,
               (((280 + 500) + CHAR_RUESTUNG_X) + 223),
               ((100 + CHAR_RUESTUNG_Y) - 7));
    enable_popup(PLAYER_GUILD_INVITE, texts[TXT_SUBJECT_GUILD_INVITE]);
    define_btn(CHAR_INVITE, texts[(TXT_ACH_4 + 4)], PlayerInvite,
               btn_classBasic, CHAR_PLAYERX2, CHAR_PLAYERY);
    enable_popup(CHAR_INVITE, texts[(TXT_ACH_4 + 5)]);
    i = 0;
    while (i < 8) {
        define_img((CHAR_MOUNT_1 + i),
                  (("res/gfx/scr/char/mount_portrait_"
                   + str((i + 1))) + ".jpg"), False,
                    (CHAR_MOUNT_X + CHAR_MOUNT_X), CHAR_MOUNT_Y);
        _local2 = actor[(CHAR_MOUNT_1 + i)];
        with (_local2) {
            add_event_listener(MouseEvent.CLICK, RequestStableScreen);
        };
        add_bunch(CHAR_RIGHTPANE, (CHAR_MOUNT_1 + i));
        i = (i + 1);
    };
    define_lbl(LBL_CHAR_MOUNT_NAME, "", CHAR_MOUNT_X, CHAR_MOUNT_Y,
              FontFormat_Default);
    add_filter(LBL_CHAR_MOUNT_NAME, Filter_Shadow);
    define_lbl(LBL_CHAR_MOUNT_DESCR, "", CHAR_MOUNT_X,
              (CHAR_MOUNT_Y + CHAR_MOUNT_LINE_Y), FontFormat_DefaultLeft);
    _local2 = actor[LBL_CHAR_MOUNT_DESCR];
    with (_local2) {
        wordWrap = True;
        width = (CHAR_MOUNT_X - 5);
    };
    add_filter(LBL_CHAR_MOUNT_DESCR, Filter_Shadow);
    define_lbl(LBL_CHAR_MOUNT_RUNTIME, "", CHAR_MOUNT_X,
              (CHAR_MOUNT_Y + (CHAR_MOUNT_LINE_Y * 5)), FontFormat_Default)
    add_filter(LBL_CHAR_MOUNT_RUNTIME, Filter_Shadow);
    define_lbl(LBL_CHAR_MOUNT_GAIN, "", CHAR_MOUNT_X,
              (CHAR_MOUNT_Y + (CHAR_MOUNT_LINE_Y * 4)), FontFormat_Default)
    add_filter(LBL_CHAR_MOUNT_GAIN, Filter_Shadow);
    define_img(CHAR_RUESTUNG, "res/gfx/scr/char/icon_schild.jpg", False,
              ((280 + 500) + CHAR_RUESTUNG_X), (100 + CHAR_RUESTUNG_Y));
    define_lbl(LBL_CHAR_RUESTUNG, "",
              (((280 + 500) + CHAR_RUESTUNG_X) + CHAR_RUESTUNG_TEXT_X),
              ((100 + CHAR_RUESTUNG_Y) + CHAR_RUESTUNG_TEXT_Y),
              FontFormat_Default);
    add_filter(LBL_CHAR_RUESTUNG, Filter_Shadow);
    define_img(CHAR_ALBUM, "res/gfx/scr/char/icon_foliant.png", False,
              ((280 + 500) + 350), (100 + 20));
    add_bunch(CHAR_RIGHTPANE, LBL_CHAR_MOUNT_NAME, LBL_CHAR_MOUNT_RUNTIME,
              LBL_CHAR_MOUNT_GAIN, LBL_CHAR_MOUNT_DESCR, CHAR_RUESTUNG,
              LBL_CHAR_RUESTUNG);
    define_bunch(SCREEN_CHAR, SCR_CHAR_BG, SCR_CHAR_EXPBAR, IF_OVL,
                 CHAR_RIGHTPANE, LBL_SCR_CHAR_EXPLABEL, CA_SCR_CHAR_EXPBAR,
                 SCR_CHAR_NAME, IF_EXIT);
    define_bunch(SCREEN_CHAR_GOLDEN, SCR_CHAR_BG, SCR_CHAR_BG_GOLDEN,
                 SCR_CHAR_EXPBAR, IF_OVL, CHAR_RIGHTPANE,
                 LBL_SCR_CHAR_EXPLABEL, CA_SCR_CHAR_EXPBAR, SCR_CHAR_NAME,
                 IF_EXIT);
    define_bunch(CHAR_SECONDPROP);
    define_bunch(CHAR_PREISE);
    BoostBtnRepeatTimer = new Timer(1000);
    DestroyBoostBtnTimer = False;
    i = 0;
    while (i < 5) {
        define_lbl((LBL_SCR_CHAR_STAERKE_CAPTION + i),
                  texts[(TXT_CHAR_STAERKE + i)], CHAR_PROP_COLUMN_1_X,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)), FontFormat_Default);
        define_lbl((LBL_SCR_CHAR_STAERKE + i), "", CHAR_PROP_COLUMN_2_X,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)), FontFormat_Attrib);
        define_btn((SCR_CHAR_STEIGERN1 + i), "", BoostAttribute,
                   btn_classPlus, CHAR_PROP_COLUMN_3_X,
                   ((CHAR_PROP_Y + (i * CHAR_PROP_Y)) - 3));
        _local2 = actor[(SCR_CHAR_STEIGERN1 + i)];
        with (_local2) {
            add_event_listener(MouseEvent.MOUSE_DOWN, BoostBtnDownHandler);
            add_event_listener(MouseEvent.MOUSE_UP, BoostBtnUpHandler);
            add_event_listener(MouseEvent.MOUSE_OUT, BoostBtnUpHandler);
            add_event_listener(MouseEvent.MOUSE_OVER, BoostBtnOver);
            add_event_listener(MouseEvent.MOUSE_OUT, BoostBtnOut);
        };
        define_lbl((LBL_SCR_CHAR_PREIS1 + i), "", 0,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)), FontFormat_Default);
        DefineCnt((SCR_CHAR_GOLD1 + i), 0,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)));
        define_lbl((LBL_SCR_CHAR_SILBER1 + i), "", 0,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)), FontFormat_Default);
        DefineCnt((SCR_CHAR_SILBER1 + i), 0,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)));
        define_lbl((LBL_SCR_CHAR_SCHADEN_CAPTION + i),
                  texts[(TXT_CHAR_SCHADEN + i)], CHAR_PROP_COLUMN_5_X,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)), FontFormat_Default);
        define_lbl((LBL_SCR_CHAR_SCHADEN + i), "", CHAR_PROP_COLUMN_6_X,
                  (CHAR_PROP_Y + (i * CHAR_PROP_Y)), FontFormat_Attrib);
        add_bunch(CHAR_SECONDPROP, (LBL_SCR_CHAR_SCHADEN_CAPTION + i));
        add_bunch(SCREEN_CHAR, (SCR_CHAR_STEIGERN1 + i),
                  (LBL_SCR_CHAR_PREIS1 + i), (SCR_CHAR_GOLD1 + i),
                  (LBL_SCR_CHAR_SILBER1 + i), (SCR_CHAR_SILBER1 + i));
        add_bunch(SCREEN_CHAR, (LBL_SCR_CHAR_STAERKE + i),
                  (LBL_SCR_CHAR_STAERKE_CAPTION + i),
                  (LBL_SCR_CHAR_SCHADEN + i),
                  (LBL_SCR_CHAR_SCHADEN_CAPTION + i));
        add_bunch(SCREEN_CHAR_GOLDEN, (SCR_CHAR_STEIGERN1 + i),
                  (LBL_SCR_CHAR_PREIS1 + i), (SCR_CHAR_GOLD1 + i),
                  (LBL_SCR_CHAR_SILBER1 + i), (SCR_CHAR_SILBER1 + i));
        add_bunch(SCREEN_CHAR_GOLDEN, (LBL_SCR_CHAR_STAERKE + i),
                  (LBL_SCR_CHAR_STAERKE_CAPTION + i),
                  (LBL_SCR_CHAR_SCHADEN + i),
                  (LBL_SCR_CHAR_SCHADEN_CAPTION + i));
        add_bunch(CHAR_PREISE, (LBL_SCR_CHAR_PREIS1 + i),
                  (SCR_CHAR_GOLD1 + i), (LBL_SCR_CHAR_SILBER1 + i),
                  (SCR_CHAR_SILBER1 + i));
        add_bunch(CHAR_RIGHTPANE, (SCR_CHAR_STEIGERN1 + i));
        i = (i + 1);
    };
    BoostBtnChange = 0;
    BoostBtnTimer = new Timer(40);
    BoostBtnTimer.add_event_listener(TimerEvent.TIMER,
                                     BoostBtnTimerFunction);
    BoostBtnTimer.start();
    DefineCnt(CHAR_SLOT_1, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_TOP_Y);
    DefineCnt(CHAR_SLOT_2, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW2_Y);
    DefineCnt(CHAR_SLOT_3, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW3_Y);
    DefineCnt(CHAR_SLOT_4, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW4_Y);
    DefineCnt(CHAR_SLOT_5, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_TOP_Y);
    DefineCnt(CHAR_SLOT_6, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW2_Y);
    DefineCnt(CHAR_SLOT_7, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW3_Y);
    DefineCnt(CHAR_SLOT_8, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW4_Y);
    DefineCnt(CHAR_SLOT_9, CHAR_SLOTS_R4C2_X, CHAR_SLOTS_ROW4_Y);
    DefineCnt(CHAR_SLOT_10, CHAR_SLOTS_R4C3_X, CHAR_SLOTS_ROW4_Y);
    DefineCnt(CHAR_SLOT_11, CHAR_SLOTS_LEFT_X, CHAR_SLOTS_ROW5_Y);
    DefineCnt(CHAR_SLOT_12, CHAR_SLOTS_R5C2_X, CHAR_SLOTS_ROW5_Y);
    DefineCnt(CHAR_SLOT_13, CHAR_SLOTS_R5C3_X, CHAR_SLOTS_ROW5_Y);
    DefineCnt(CHAR_SLOT_14, CHAR_SLOTS_R5C4_X, CHAR_SLOTS_ROW5_Y);
    DefineCnt(CHAR_SLOT_15, CHAR_SLOTS_RIGHT_X, CHAR_SLOTS_ROW5_Y);
    i = 0;
    while (i < 8) {
        define_img((EMPTY_SLOT_1 + i),
                  (("res/gfx/scr/char/slot" + str((i + 1))) + ".png"),
                  False, 0, 0);
        i = (i + 1);
    };
    define_img(EMPTY_SLOT_9_1, "res/gfx/scr/char/slot9_1.png", False, 0, 0);
    define_img(EMPTY_SLOT_9_2, "res/gfx/scr/char/slot9_2.png", False, 0, 0);
    define_img(EMPTY_SLOT_9_3, "res/gfx/scr/char/slot9_3.png", False, 0, 0);
    define_img(EMPTY_SLOT_10, "res/gfx/scr/char/slot10.png", False, 0, 0);
    define_img(NO_SHIELD, "res/gfx/itm/no_shield.png", False, 0, 0);
    itmTyp = 0;
    while (itmTyp <= 14) {
        itm_pic = 0;
        while (itm_pic < C_ITEMS_PER_TYPE) {
            itm_color = 0;
            while (itm_color < 5) {
                Switch (itmTyp){
                    if case(1:
                    if case(2:
                    if case(3:
                    if case(4:
                    if case(5:
                    if case(6:
                    if case(7:
                        itm_class = 0;
                        while (itm_class < 3) {
                            define_img(GetItemID(itmTyp, itm_pic, itm_color,
                                      itm_class),
                                    GetItemFile(itmTyp, itm_pic,
                                                itm_color, itm_class),
                                    False, 0, 0);
                            itm_class = (itm_class + 1);
                        };
                        break;
                    default:
                        define_img(GetItemID(itmTyp, itm_pic, itm_color, 0),
                                  GetItemFile(itmTyp, itm_pic,
                                              itm_color, 0), False, 0, 0);
                };
                itm_color = (itm_color + 1);
            };
            itm_pic = (itm_pic + 1);
        };
        itmTyp = (itmTyp + 1);
    };
    itmTyp = 0;
    while (itmTyp <= 1) {
        itm_pic = 0;
        while (itm_pic < C_ITEMS_PER_TYPE) {
            itm_color = 0;
            while (itm_color < 5) {
                define_img(get_arrow_id(itmTyp, itm_pic, itm_color),
                          (((((((("res/gfx/itm/1-" + str((itmTyp + 2)))
                           + "/shot") + (((itmTyp == 0)) ? 2 : 1)) + "-")
                            + str(itm_pic)) + "-")
                            + str(((((itm_pic >= 50))
                                  ? (((itmTyp == 0))
                                     ? (((itm_color == 3))
                                        ? 3 : 0) : 0) : itm_color) + 1)))
                                        + ".png"), False, 0, 0);
                itm_color = (itm_color + 1);
            };
            itm_pic = (itm_pic + 1);
        };
        itmTyp = (itmTyp + 1);
    };
    i = 0;
    while (i < 15) {
        SetCnt((CHAR_SLOT_1 + i), ITM_OFFS);
        actor[(CHAR_SLOT_1 + i)].add_event_listener(MouseEvent.MOUSE_DOWN,
                                                    InventoryItemMouseDown);
        if (i >= 10){
            actor[(CHAR_SLOT_1 + i)].add_event_listener(
                            MouseEvent.MOUSE_DOWN, BackpackItemMouseDown);
        };
        add_bunch(SCREEN_CHAR, (CHAR_SLOT_1 + i));
        add_bunch(SCREEN_CHAR_GOLDEN, (CHAR_SLOT_1 + i));
        EnableDragDrop((CHAR_SLOT_1 + i), DropHandler);
        actor[(CHAR_SLOT_1 + i)].add_event_listener(MouseEvent.MOUSE_UP,
                                                    InventoryItemMouseUp);
        i = (i + 1);
    };
    define_bunch(CHAR_ACH);
    i = 0;
    while (i < 40) {
        DefineCnt((CHAR_ACH + i),
                  (SCR_CHAR_ACH_X + (((buffed_mode)
                   ? SCR_CHAR_ACH_X_BUFFED
                   : SCR_CHAR_ACH_X) * (i % 8))), SCR_CHAR_ACH_Y);
        define_img((CHAR_ACH + i),
                  (((("res/gfx/scr/char/ach/ach-" + str(((i % 8) + 1)))
                   + "-") + str(int((i / 8)))) + ".png"), False, 0, 0);
        SetCnt((CHAR_ACH + i), (CHAR_ACH + i));
        MakePersistent((CHAR_ACH + i));
        if (!texts[(TXT_ACH_4 + 4)]){
            if ((i % 8) == 7){
                _local2 = actor[(CHAR_ACH + i)];
                with (_local2) {
                    add_event_listener(MouseEvent.CLICK, Openfriend_link);
                    buttonMode = True;
                    useHandCursor = True;
                    mouseChildren = False;
                };
            };
        };
        add_bunch(CHAR_ACH, (CHAR_ACH + i));
        i = (i + 1);
    };
    i = 0;
    while (i < 3) {
        DefineCnt((CHAR_POTION + i), (POTION_X + (POTION_X * i)), POTION_Y)
        _local2 = actor[(CHAR_POTION + i)];
        with (_local2) {
            scaleX = 0.5;
            scaleY = 0.5;
        };
        add_bunch(SCREEN_CHAR, (CHAR_POTION + i));
        add_bunch(SCREEN_CHAR_GOLDEN, (CHAR_POTION + i));
        add_bunch(CHAR_RIGHTPANE, (CHAR_POTION + i));
        double_click_handler(actor[(CHAR_POTION + i)], PotionSingleClick,
                           PotionDoubleClick);
        i = (i + 1);
    };
    define_snd(SND_SHARD, "res/sfx/tower/shard.mp3");
    define_snd(SND_MIRROR, "res/sfx/tower/mirror.mp3");
    define_snd(SND_HATCH, "res/sfx/tower/hatch.mp3");
    DefineCnt(TOWER_SCROLLAREA, (280 + 500), 100);
    _local2 = actor[TOWER_SCROLLAREA];
    with (_local2) {
        scrollRect = new Rectangle(0, 0, 500, 700);
        mouseChildren = False;
        tab_enabled = False;
        tabChildren = False;
        focuseRect = False;
    };
    define_btn(TOWER_TRY, texts[TXT_TOWER_TRY], tower_btn_handler,
               btn_classBasic, 940, 700);
    define_img(SCR_TOWER_BG,
              "res/gfx/scr/quest/locations/location_tower.jpg",
              False, 280, 100);
    define_bunch(SCREEN_TOWER, SCR_CHAR_BG, TOWER_SCROLLAREA, TOWER_TRY,
                 IF_OVL, IF_EXIT);
    tower_levelLabelTimer = new Timer(25);
    tower_levelLabelTimer.add_event_listener(TimerEvent.TIMER,
                                             tower_levelLabelMoveFn);
    towerBoostPriceFadeoutTimer = new Timer(250, 1);
    towerBoostPriceFadeoutTimer.add_event_listener(TimerEvent.TIMER,
                                                   towerBoostPriceFadeout);
    i = 0;
    while (i < 3) {
        define_img((TOWER_PORTRAIT + i),
                  (("res/gfx/npc/copycat_" + str((i + 1))) + ".jpg"),
                  False, SCR_CHAR_CHARX, (SCR_CHAR_CHARY - 1));
        define_img((TOWER_NO_PORTRAIT + i),
                  (("res/gfx/npc/copycat_" + str((i + 1))) + "_empty.jpg"),
                  False, SCR_CHAR_CHARX, (SCR_CHAR_CHARY - 1));
        define_btn((TOWER_STEIGERN1 + i), "", BoostCopycat, btn_classPlus,
                   (SCR_CHAR_CHARX + 232), (SCR_CHAR_CHARY + 260));
        actor[(TOWER_STEIGERN1 + i)].scaleX = 0.8;
        actor[(TOWER_STEIGERN1 + i)].scaleY = 0.8;
        actor[(TOWER_STEIGERN1 + i)].add_event_listener(
                            MouseEvent.MOUSE_OVER, ShowTowerBoostPrices);
        actor[(TOWER_STEIGERN1 + i)].add_event_listener(
                            MouseEvent.MOUSE_OUT, HideTowerBoostPrices);
        enable_popup((TOWER_STEIGERN1 + i), texts[TXT_BOOST_COPYCAT]);
        define_lbl((LBL_TOWER_BOOSTPRICELABEL + i), "", 0,
                  (EXPERIENCE_BAR_Y + 2), FontFormat_Default);
        add_filter((LBL_TOWER_BOOSTPRICELABEL + i),
                  Filter_Shadow);
        actor[(LBL_TOWER_BOOSTPRICELABEL + i)].alpha = 0;
        add_bunch(SCREEN_TOWER, (TOWER_PORTRAIT + i),
                  (TOWER_NO_PORTRAIT + i), (TOWER_STEIGERN1 + i),
                  (LBL_TOWER_BOOSTPRICELABEL + i));
        i = (i + 1);
    };
    i = 0;
    while (i < 15) {
        add_bunch(SCREEN_TOWER, (CHAR_SLOT_1 + i));
        i = (i + 1);
    };
    define_btn(PREV_COPYCAT, "", tower_btn_handler, btn_classArrowLeft,
               (SCR_CHAR_CHARX + 10), (SCR_CHAR_CHARY + 10));
    define_btn(NEXT_COPYCAT, "", tower_btn_handler, btn_classArrowRight,
               (SCR_CHAR_CHARX + 215), (SCR_CHAR_CHARY + 10));
    DefineCnt(TOWER_BOOSTCOIN, (SCR_CHAR_CHARX + 205), EXPERIENCE_BAR_Y);
    actor[TOWER_BOOSTCOIN].alpha = 0;
    define_bunch(TOWER_BOOSTPRICE, LBL_TOWER_BOOSTPRICELABEL,
                 (LBL_TOWER_BOOSTPRICELABEL + 1),
                 (LBL_TOWER_BOOSTPRICELABEL + 2), TOWER_BOOSTCOIN);
    define_lbl(LBL_TOWER_EXPLABEL, "", (SCR_CHAR_CHARX + 3),
              (EXPERIENCE_BAR_Y + 2), FontFormat_LifeBar);
    add_filter(LBL_TOWER_EXPLABEL, Filter_Shadow);
    add_bunch(SCREEN_TOWER, PREV_COPYCAT, NEXT_COPYCAT);
    add_bunch(SCREEN_TOWER, LBL_TOWER_EXPLABEL, TOWER_BOOSTCOIN,
              SCR_CHAR_NAME);
    i = 0;
    while (i < 5) {
        add_bunch(SCREEN_TOWER, (LBL_SCR_CHAR_STAERKE + i),
                  (LBL_SCR_CHAR_STAERKE_CAPTION + i),
                  (LBL_SCR_CHAR_SCHADEN + i),
                  (LBL_SCR_CHAR_SCHADEN_CAPTION + i));
        i = (i + 1);
    };
    define_img(TOWER_BG, "res/gfx/scr/tower/tower_back.jpg", False, 0, 0);
    define_img(TOWER_BASE, "res/gfx/scr/tower/tower_base.png", False, 0, 0);
    define_img(TOWER_LEVEL, "res/gfx/scr/tower/tower_level.png",
              False, 0, 0);
    define_img((TOWER_LEVEL + 1), "res/gfx/scr/tower/tower_level.png",
     False, 0, 0);
    define_img((TOWER_LEVEL + 2), "res/gfx/scr/tower/tower_level.png",
              False, 0, 0);
    define_img(TOWER_ROOF, "res/gfx/scr/tower/tower_roof.png", False, 0, 0);
    define_img(TOWER_WINDOW_OPEN, "res/gfx/scr/tower/tower_window_open.png",
              False, 0, 0);
    define_img(TOWER_WINDOW_CLOSED,
              "res/gfx/scr/tower/tower_window_closed.png", False, 0, 0);
    define_img(TOWER_WINDOW_BURNT,
              "res/gfx/scr/tower/tower_window_destroyed.png", False, 0, 0);
    DefineCnt(TOWER_WINDOW, 0, 0);
    DefineCnt((TOWER_WINDOW + 1), 0, 0);
    DefineCnt((TOWER_WINDOW + 2), 0, 0);
    i = 0;
    while (i < 3) {
        DefineCnt((TOWER_FACE + i), 175, 0);
        actor[(TOWER_FACE + i)].scaleX = 0.5;
        actor[(TOWER_FACE + i)].scaleY = 0.5;
        i = (i + 1);
    };
    define_bunch(TOWER_PIECES, TOWER_BG, TOWER_BASE, TOWER_LEVEL,
                 (TOWER_LEVEL + 1), (TOWER_LEVEL + 2), TOWER_ROOF);
    add_bunch(TOWER_PIECES, TOWER_FACE, (TOWER_FACE + 1), (TOWER_FACE + 2),
              TOWER_WINDOW_OPEN, TOWER_WINDOW_CLOSED, TOWER_WINDOW_BURNT);
    MakePersistent(TOWER_BG, TOWER_BASE, TOWER_LEVEL, (TOWER_LEVEL + 1),
                   (TOWER_LEVEL + 2), TOWER_ROOF);
    MakePersistent(TOWER_WINDOW, (TOWER_WINDOW + 1), (TOWER_WINDOW + 2),
                   TOWER_FACE, (TOWER_FACE + 1), (TOWER_FACE + 2));
    define_img(SCR_FIDGET_BG, "res/gfx/scr/shops/fidget.jpg", False,
              SCR_SHOP_BG_X, 100);
    define_img(FIDGET_AFFE1, "res/gfx/scr/shops/fidget_affe1.jpg", False,
              (SCR_SHOP_BG_X + FIDGET_AFFE_X), (100 + FIDGET_AFFE_Y));
    define_img(FIDGET_AFFE2, "res/gfx/scr/shops/fidget_affe2.jpg", False,
              (SCR_SHOP_BG_X + FIDGET_AFFE_X), (100 + FIDGET_AFFE_Y));
    define_img(FIDGET_AFFE3, "res/gfx/scr/shops/fidget_affe3.jpg", False,
              (SCR_SHOP_BG_X + FIDGET_AFFE_X), (100 + FIDGET_AFFE_Y));
    actor[FIDGET_AFFE1].mouse_enabled = False;
    actor[FIDGET_AFFE2].mouse_enabled = False;
    actor[FIDGET_AFFE3].mouse_enabled = False;
    if (Capabilities.version[0: 3] != "IOS"){
        define_img(FIDGET_TAGKERZE, "res/gfx/scr/shops/tagkerze.swf", False,
                  (SCR_SHOP_BG_X + FIDGET_TAGKERZE_X),
                  (100 + FIDGET_TAGKERZE_Y));
        define_img(FIDGET_NACHTKERZE, "res/gfx/scr/shops/nachtkerze.swf",
                  False, (SCR_SHOP_BG_X + FIDGET_NACHTKERZE_X),
                  (100 + FIDGET_NACHTKERZE_Y));
        actor[FIDGET_TAGKERZE].mouse_enabled = False;
        actor[FIDGET_NACHTKERZE].mouse_enabled = False;
    };
    define_img(FIDGET_DAY, "res/gfx/scr/shops/fidget_normal.jpg", False,
              (SCR_SHOP_BG_X + FIDGET_X), (100 + FIDGET_Y));
    define_img(FIDGET_IDLE, "res/gfx/scr/shops/fidget_langeweile.jpg",
              False, (SCR_SHOP_BG_X + FIDGET_X), (100 + FIDGET_Y));
    define_img(FIDGET_SALE, "res/gfx/scr/shops/fidget_wasverkauft.jpg",
              False, (SCR_SHOP_BG_X + FIDGET_X), (100 + FIDGET_Y));
    define_img(FIDGET_NIGHT, "res/gfx/scr/shops/fidget_nachts.jpg", False,
              (SCR_SHOP_BG_X + FIDGET_X), (100 + FIDGET_Y));
    actor[FIDGET_DAY].mouse_enabled = False;
    actor[FIDGET_IDLE].mouse_enabled = False;
    actor[FIDGET_SALE].mouse_enabled = False;
    actor[FIDGET_NIGHT].mouse_enabled = False;
    define_img(FIDGET_BLINZELN,
              "res/gfx/scr/shops/fidget_normal_blinzeln.jpg", False,
              ((SCR_SHOP_BG_X + FIDGET_X) + FIDGET_BLINZELN_X),
              ((100 + FIDGET_Y) + FIDGET_BLINZELN_Y));
    actor[FIDGET_BLINZELN].mouse_enabled = False;
    define_img(SHAKES_DAY, "res/gfx/scr/shops/shakes_normal.jpg", False,
              (SCR_SHOP_BG_X + SHAKES_X), (100 + SHAKES_Y));
    define_img(SHAKES_NIGHT, "res/gfx/scr/shops/shakes_nacht.jpg", False,
              (SCR_SHOP_BG_X + SHAKES_X), (100 + SHAKES_Y));
    define_img(SHAKES_IDLE, "res/gfx/scr/shops/shakes_gelangweilt.jpg",
              False, (SCR_SHOP_BG_X + SHAKES_IDLE_X),
              (100 + SHAKES_IDLE_Y));
    define_img(SHAKES_IDLE1, "res/gfx/scr/shops/shakes_spielt1.jpg", False,
              (SCR_SHOP_BG_X + SHAKES_IDLE2_X), (100 + SHAKES_IDLE2_Y));
    define_img(SHAKES_IDLE2, "res/gfx/scr/shops/shakes_spielt2.jpg", False,
              (SCR_SHOP_BG_X + SHAKES_IDLE2_X), (100 + SHAKES_IDLE2_Y));
    define_img(SHAKES_IDLE3, "res/gfx/scr/shops/shakes_spielt3.jpg", False,
              (SCR_SHOP_BG_X + SHAKES_IDLE2_X), (100 + SHAKES_IDLE2_Y));
    define_img(SHAKES_BLINZELN1, "res/gfx/scr/shops/shakes_augen1.jpg",
              False, ((SCR_SHOP_BG_X + SHAKES_X) + SHAKES_BLINZELN_X),
              ((100 + SHAKES_Y) + SHAKES_BLINZELN_Y));
    define_img(SHAKES_BLINZELN2, "res/gfx/scr/shops/shakes_augen2.jpg",
              False, ((SCR_SHOP_BG_X + SHAKES_X) + SHAKES_BLINZELN_X),
              ((100 + SHAKES_Y) + SHAKES_BLINZELN_Y));
    if (Capabilities.version[0: 3] == "IOS"){
        define_bunch(FIDGET_DAY, FIDGET_DAY);
        define_bunch(FIDGET_NIGHT, FIDGET_NIGHT);
    } else {
        define_bunch(FIDGET_DAY, FIDGET_DAY, FIDGET_TAGKERZE);
        define_bunch(FIDGET_NIGHT, FIDGET_NIGHT, FIDGET_NACHTKERZE);
    };
    define_img(SCR_SHAKES_BG, "res/gfx/scr/shops/shakes.jpg", False,
              SCR_SHOP_BG_X, 100);
    define_btn(SHOPS_NEWWAREZ, texts[TXT_SHOPS_NEWWAREZ], RequestNewWarez,
               btn_classBasic, 0, NEW_WAREZ_Y);
    actor[SHOPS_NEWWAREZ].x = (NEW_WAREZ_X
                               - int((actor[SHOPS_NEWWAREZ].width / 2)));
    DefineCnt(CHAR_SLOT_FIDGET_1, SHOP_SLOTS_C1_X, SHOP_SLOTS_R1_Y);
    DefineCnt(CHAR_SLOT_FIDGET_2, SHOP_SLOTS_C2_X, SHOP_SLOTS_R1_Y);
    DefineCnt(CHAR_SLOT_FIDGET_3, SHOP_SLOTS_C3_X, SHOP_SLOTS_R1_Y);
    DefineCnt(CHAR_SLOT_FIDGET_4, SHOP_SLOTS_C1_X, SHOP_SLOTS_R2_Y);
    DefineCnt(CHAR_SLOT_FIDGET_5, SHOP_SLOTS_C2_X, SHOP_SLOTS_R2_Y);
    DefineCnt(CHAR_SLOT_FIDGET_6, SHOP_SLOTS_C3_X, SHOP_SLOTS_R2_Y);
    DefineCnt(CHAR_SLOT_SHAKES_1, SHOP_SLOTS_C1_X, SHOP_SLOTS_R1_Y);
    DefineCnt(CHAR_SLOT_SHAKES_2, SHOP_SLOTS_C2_X, SHOP_SLOTS_R1_Y);
    DefineCnt(CHAR_SLOT_SHAKES_3, SHOP_SLOTS_C3_X, SHOP_SLOTS_R1_Y);
    DefineCnt(CHAR_SLOT_SHAKES_4, SHOP_SLOTS_C1_X, SHOP_SLOTS_R2_Y);
    DefineCnt(CHAR_SLOT_SHAKES_5, SHOP_SLOTS_C2_X, SHOP_SLOTS_R2_Y);
    DefineCnt(CHAR_SLOT_SHAKES_6, SHOP_SLOTS_C3_X, SHOP_SLOTS_R2_Y);
    define_bunch(SCREEN_FIDGET, SCR_FIDGET_BG, FIDGET_AFFE2, FIDGET_AFFE3,
                 FIDGET_AFFE1, FIDGET_SALE, FIDGET_IDLE, FIDGET_DAY,
                 FIDGET_BLINZELN, FIDGET_NIGHT, IF_OVL, SHOPS_NEWWAREZ,
                 CA_SCR_CHAR_EXPBAR, IF_EXIT);
    define_bunch(SCREEN_SHAKES, SCR_SHAKES_BG, SHAKES_IDLE, SHAKES_IDLE1,
                 SHAKES_IDLE2, SHAKES_IDLE3, SHAKES_DAY, SHAKES_BLINZELN1,
                 SHAKES_BLINZELN2, SHAKES_NIGHT, IF_OVL, SHOPS_NEWWAREZ,
                 CA_SCR_CHAR_EXPBAR, IF_EXIT);
    define_img(FIDGET_EPCIOVL, "res/gfx/scr/shops/epics_overlay_fidget.png",
              False, (SCR_SHOP_BG_X - 65), (100 + 210));
    define_img(SHAKES_EPCIOVL, "res/gfx/scr/shops/epics_overlay_shakes.png",
              False, (SCR_SHOP_BG_X + 200), (100 + 250));
    AffeBlinzeln = int((random.random() * 30));
    FidgetBlinzeln = int((random.random() * 30));
    ShakesBlinzeln = int((random.random() * 30));
    ShakesIdleStep = 0;
    ShakesIdlePhase = 0;
    WasIdleCount = 0;
    ShopIdle = 0;
    PlayerIdle = False;
    ShopAniTimer = new Timer(100);
    SaleRecoverTime = 0;
    ShopAniTimer.add_event_listener(TimerEvent.TIMER, ShopAniFrame);
    if (!light_mode){
        ShopAniTimer.start();
    } else {
        ShopAniTimer.stop();
    };
    i = 0;
    while (i < 5) {
        add_bunch(SCREEN_FIDGET, (LBL_SCR_CHAR_STAERKE + i),
                  (LBL_SCR_CHAR_STAERKE_CAPTION + i),
                  (LBL_SCR_CHAR_SCHADEN + i),
                  (LBL_SCR_CHAR_SCHADEN_CAPTION + i));
        add_bunch(SCREEN_SHAKES, (LBL_SCR_CHAR_STAERKE + i),
                  (LBL_SCR_CHAR_STAERKE_CAPTION + i),
                  (LBL_SCR_CHAR_SCHADEN + i),
                  (LBL_SCR_CHAR_SCHADEN_CAPTION + i));
        i = (i + 1);
    };
    i = 0;
    while (i < 6) {
        SetCnt((CHAR_SLOT_FIDGET_1 + i), ITM_OFFS);
        SetCnt((CHAR_SLOT_SHAKES_1 + i), ITM_OFFS);
        add_bunch(SCREEN_FIDGET, (CHAR_SLOT_FIDGET_1 + i));
        add_bunch(SCREEN_SHAKES, (CHAR_SLOT_SHAKES_1 + i));
        actor[(CHAR_SLOT_FIDGET_1 + i)].add_event_listener(
                               MouseEvent.MOUSE_DOWN, ShopMouseDownEvent);
        actor[(CHAR_SLOT_SHAKES_1 + i)].add_event_listener(
                               MouseEvent.MOUSE_DOWN, ShopMouseDownEvent);
        EnableDragDrop((CHAR_SLOT_FIDGET_1 + i), DropHandler);
        EnableDragDrop((CHAR_SLOT_SHAKES_1 + i), DropHandler);
        actor[(CHAR_SLOT_FIDGET_1 + i)].add_event_listener(
                               MouseEvent.MOUSE_UP, ShopMouseUpEvent);
        actor[(CHAR_SLOT_SHAKES_1 + i)].add_event_listener(
                               MouseEvent.MOUSE_UP, ShopMouseUpEvent);
        i = (i + 1);
    };
    i = 0;
    while (i < 15) {
        add_bunch(SCREEN_FIDGET, (CHAR_SLOT_1 + i));
        add_bunch(SCREEN_SHAKES, (CHAR_SLOT_1 + i));
        i = (i + 1);
    };
    RollFrenzy.add_event_listener(TimerEvent.TIMER, RequestNewWarez);
    define_img(GOTO_WITCH_OVL, "res/gfx/scr/shops/book_down.jpg", False,
              ((280 + 500) + 360), (100 + 220));
    actor[GOTO_WITCH_OVL].mouse_enabled = False;
    define_click_area(CA_GOTO_WITCH, GOTO_WITCH_OVL, RequestWitchScreen,
                    ((280 + 500) + 359), (100 + 215), 45, 65);
    enable_popup(CA_GOTO_WITCH, texts[TXT_WITCH_BOOK]);
    define_bunch(SCREEN_WITCH);
    define_snd(SND_WITCH_DROP, "res/sfx/toilet/drop.mp3", False);
    add_bunch(SCREEN_WITCH, SND_WITCH_DROP);
    define_img(WITCH, "res/gfx/scr/shops/witch.jpg",
              False, SCR_SHOP_BG_X, 100);
    add_bunch(SCREEN_WITCH, WITCH);
    i = 0;
    while (i < 15) {
        add_bunch(SCREEN_WITCH, (CHAR_SLOT_1 + i));
        i = (i + 1);
    };
    i = 0;
    while (i < 15) {
        define_img((WITCH_ANI + i),
                  (("res/gfx/scr/shops/witch_animation/witch"
                   + str(((i * 2) + 1))) + ".jpg"), False, (280 + 500),
                        (100 + 380));
        hide((WITCH_ANI + i));
        add_bunch(SCREEN_WITCH, (WITCH_ANI + i));
        i = (i + 1);
    };
    spellClicking = False;
    i = 0;
    while (i < 10) {
        DefineCnt((WITCH_SCROLL + i),
                  (((280 + 500) + 37) + ((i % 5) * 83)),
                  ((100 + 11) + (math.floor((i / 5)) * 95)));
        actor[(WITCH_SCROLL + i)].useHandCursor = True;
        actor[(WITCH_SCROLL + i)].buttonMode = True;
        actor[(WITCH_SCROLL + i)].add_event_listener(MouseEvent.CLICK,
                                             function (evt:MouseEvent){
            var id;
            id = ((get_actor_id(evt.target) - WITCH_SCROLL) + 1);
            if (spellClicking){
                send_action(ACT_WITCH_ENCHANT, id);
            };
            spellClicking = False;
        });
        actor[(WITCH_SCROLL + i)].add_event_listener(MouseEvent.MOUSE_DOWN,
                                             function (evt:MouseEvent){
            var actorId;
            var i;
            actorId = get_actor_id(evt.target);
            i = (actorId - WITCH_SCROLL);
            actor[actorId].x = ((((280 + 500) + 37) + ((i % 5) * 83)) + 1);
            actor[actorId].y = ((100 + 11 + math.floor((i / 5)) * 95) + 2);
            spellClicking = True;
        });
        actor[(WITCH_SCROLL + i)].add_event_listener(MouseEvent.MOUSE_UP,
                                             function (evt:MouseEvent){
            var actorId;
            var i;
            actorId = get_actor_id(evt.target);
            i = (actorId - WITCH_SCROLL);
            actor[actorId].x = (((280 + 500) + 37) + ((i % 5) * 83));
            actor[actorId].y = ((100 + 11) + (math.floor((i / 5)) * 95));
        });
        actor[(WITCH_SCROLL + i)].add_event_listener(MouseEvent.MOUSE_OUT,
                                                 function (evt:MouseEvent){
            var actorId;
            var i;
            actorId = get_actor_id(evt.target);
            i = (actorId - WITCH_SCROLL);
            actor[actorId].x = (((280 + 500) + 37) + ((i % 5) * 83));
            actor[actorId].y = ((100 + 11) + (math.floor((i / 5)) * 95));
            spellClicking = False;
        });
        i = (i + 1);
    };
    define_click_area(CA_WITCH, C_EMPTY, None, (SCR_SHOP_BG_X + 180), 400,
                    135, 155);
    define_click_area(CA_CHALDRON, C_EMPTY, None, (SCR_SHOP_BG_X + 120), 585,
                    260, 160);
    enable_popup(CA_WITCH, texts[TXT_WITCH_HINT]);
    enable_popup(CA_CHALDRON, texts[(TXT_WITCH_HINT + 1)]);
    actor[CA_WITCH].useHandCursor = False;
    actor[CA_CHALDRON].useHandCursor = False;
    add_bunch(SCREEN_WITCH, IF_OVL, CA_WITCH, CA_CHALDRON, IF_EXIT);
    define_img(SCR_DEALER_BG, "", False, 280, 100);
    define_bunch(SCREEN_DEALER, SCR_DEALER_BG, IF_OVL, IF_EXIT);
    define_img(SCR_WORLDMAP_BG, "res/gfx/scr/map/worldmap.jpg", False,
              280, 100);
    define_bunch(SCREEN_WORLDMAP, SCR_WORLDMAP_BG, IF_OVL, IF_EXIT);
    i = 0;
    while (i < 100) {
        define_img((SCR_QUEST_BG_1 + i),
                  (("res/gfx/scr/quest/locations/location" + str((i + 1)))
                   + ".jpg"), False, 280, 100);
        i = (i + 1);
    };
    define_img(QUESTBAR_BG, "res/gfx/if/adventurebar.png", False,
              QUESTBAR_X, QUESTBAR_Y);
    define_img(QUESTBAR_FILL, "res/gfx/if/adventurebar_inside.jpg", False,
              (QUESTBAR_X + 110), (QUESTBAR_Y + 44));
    define_img(QUESTBAR_LIGHT, "res/gfx/if/laden_effekt.png", False,
              ((QUESTBAR_X + 110) - 5), (QUESTBAR_Y + 44));
    define_lbl(LBL_QUESTBAR_TEXT, "", 0, QUESTBAR_LABEL_Y,
              FontFormat_QuestBar);
    define_btn(QUEST_CANCEL, texts[TXT_QUEST_CANCEL], CancelQuest,
               btn_classBasic, 0, QUEST_CANCEL_Y);
    define_btn(QUEST_SKIP, (texts[TXT_SKIP_FIGHT] + " ~P"), SkipQuest,
               btn_classBasic, 0, QUEST_CANCEL_Y);
    define_bunch(SCREEN_QUEST, QUESTBAR_BG, QUESTBAR_FILL, QUESTBAR_LIGHT,
                 LBL_QUESTBAR_TEXT, IF_OVL, LBL_SCREEN_TITLE, QUEST_CANCEL,
                 QUEST_SKIP, IF_EXIT);
    i = 0;
    while (i < 4) {
        add_bunch(SCREEN_QUEST, (TV + i));
        i = (i + 1);
    };
    add_bunch(SCREEN_QUEST, CA_TV);
    actor[QUEST_SKIP].x = int(((QUEST_CANCEL_X
                              - actor[QUEST_SKIP].width) - 5));
    actor[QUESTBAR_FILL].scaleX = 0;
    define_img(POST_BG, "res/gfx/scr/post/postamt.jpg", False, 280, 100);
    define_img(POST_DAWN1, "res/gfx/scr/post/postamt_abend1.jpg", False,
              (280 + POST_VOGEL_X), (100 + POST_VOGEL_Y));
    define_img(POST_DAWN2, "res/gfx/scr/post/postamt_abend2.jpg", False,
              (280 + POST_FENSTER_X), (100 + POST_FENSTER_Y));
    define_img(POST_NIGHT1, "res/gfx/scr/post/postamt_nacht1.jpg", False,
              (280 + POST_VOGEL_X), (100 + POST_VOGEL_Y));
    define_img(POST_NIGHT2, "res/gfx/scr/post/postamt_nacht2.jpg", False,
              (280 + POST_FENSTER_X), (100 + POST_FENSTER_Y));
    define_bunch(POST_DAWN, POST_DAWN1, POST_DAWN2);
    define_bunch(POST_NIGHT, POST_NIGHT1, POST_NIGHT2);
    define_from_class(SHP_POST_BLACK_SQUARE, black_square, POST_SQUARE_X,
                    POST_SQUARE_Y);
    _local2 = actor[SHP_POST_BLACK_SQUARE];
    with (_local2) {
        width = POST_SQUARE_X;
        height = POST_SQUARE_Y;
        alpha = 0.6;
    };
    define_lbl(LBL_POST_TITLE_INBOX, texts[TXT_POST_TITLE_INBOX],
              SCREEN_TITLE_X, SCREEN_TITLE_Y, FontFormat_ScreenTitle);
    actor[LBL_POST_TITLE_INBOX].x = (SCREEN_TITLE_X
                     - int((actor[LBL_POST_TITLE_INBOX].text_width / 2)));
    define_lbl(LBL_POST_TITLE_READ, texts[TXT_POST_TITLE_READ],
              SCREEN_TITLE_X, SCREEN_TITLE_Y, FontFormat_ScreenTitle);
    actor[LBL_POST_TITLE_READ].x = (SCREEN_TITLE_X
                    - int((actor[LBL_POST_TITLE_READ].text_width / 2)));
    define_lbl(LBL_POST_TITLE_WRITE, texts[TXT_POST_TITLE_WRITE],
              SCREEN_TITLE_X, SCREEN_TITLE_Y, FontFormat_ScreenTitle);
    actor[LBL_POST_TITLE_WRITE].x = (SCREEN_TITLE_X
                 - int((actor[LBL_POST_TITLE_WRITE].text_width / 2)));
    add_filter(LBL_POST_TITLE_INBOX, Filter_Shadow);
    add_filter(LBL_POST_TITLE_READ, Filter_Shadow);
    add_filter(LBL_POST_TITLE_WRITE, Filter_Shadow);
    DefineCnt(POST_LIST, POST_LIST_X, POST_LIST_Y);
    define_btn(POST_READ, texts[TXT_POST_READ], PostBtnHandler,
               btn_classBasic, POST_BUTTONS_X, POST_BUTTONS_Y);
    define_btn(POST_DELETE, texts[TXT_POST_DELETE], PostBtnHandler,
               btn_classBasic,
               (POST_BUTTONS_X
                + ((actor[POST_READ].width + POST_BUTTONS_X) * 2)),
                POST_BUTTONS_Y);
    define_btn(POST_WRITE, texts[TXT_POST_WRITE], PostBtnHandler,
               btn_classBasic,
               (POST_BUTTONS_X + ((actor[POST_READ].width
                + POST_BUTTONS_X) * 1)), POST_BUTTONS_Y);
    define_btn(POST_FLUSH, texts[(TXT_POST_FLUSH_TEXT + 2)],
               PostBtnHandler, btn_classBasic,
               (POST_BUTTONS_X + ((actor[POST_READ].width
                + POST_BUTTONS_X) * 3)), POST_BUTTONS_Y);
    define_btn(POST_DELETEREAD, texts[TXT_POST_DELETE], PostBtnHandler,
               btn_classBasic,
               (POST_BUTTONS_X + ((actor[POST_READ].width
                + POST_BUTTONS_X) * 2)), POST_BUTTONS_Y);
    define_btn(POST_FORWARD, texts[TXT_POST_FORWARD], PostBtnHandler,
               btn_classBasic, (POST_BUTTONS_X + ((actor[POST_READ].width
                                + POST_BUTTONS_X) * 3)), POST_BUTTONS_Y);
    define_btn(POST_PROFILE, "", PostBtnHandler, btn_classView,
               POST_PROFILE_X, POST_BUTTONS_Y);
    define_btn(POST_UP, "", PostBtnHandler, btn_classArrowUp,
               POST_SCROLLX, POST_SCROLLUP_Y);
    define_btn(POST_DOWN, "", PostBtnHandler, btn_classArrowDown,
               POST_SCROLLX, POST_SCROLLDOWN_Y);
    define_btn(POST_READ_NEXT, "", PostBtnHandler, btn_classArrowRight,
               ((POST_BUTTONS_X + ((actor[POST_READ].width
                + POST_BUTTONS_X) * 4)) + 50), (POST_BUTTONS_Y + 3));
    define_btn(POST_READ_PREV, "", PostBtnHandler, btn_classArrowLeft,
               ((POST_BUTTONS_X + ((actor[POST_READ].width
                + POST_BUTTONS_X) * 4)) + 5), (POST_BUTTONS_Y + 3));
    enable_popup(POST_PROFILE, texts[TXT_POPUP_PROFILE]);
    define_lbl(LBL_POST_FLUSH_TEXT,
              texts[(TXT_POST_FLUSH_TEXT + 1)].split("#").join(chr(13)),
               ((IF_WIN_X + IF_WIN_WELCOME_X) - (ARENA_TEXT_X / 2)),
               (IF_WIN_Y + ARENA_TEXT_Y), FontFormat_DefaultLeft);
    add_filter(LBL_POST_FLUSH_TEXT, Filter_Shadow);
    define_btn(POST_FLUSH_CANCEL, texts[TXT_ABBRECHEN], PostBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    define_btn(POST_FLUSH_OK, texts[TXT_OK], PostBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    _local2 = actor[POST_FLUSH_CANCEL];
    with (_local2) {
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) + 10);
    };
    _local2 = actor[POST_FLUSH_OK];
    with (_local2) {
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int(width)) - 10);
    };
    define_bunch(POST_FLUSHMSG);
    add_bunch(POST_FLUSHMSG, CA_POST_BLOCK, IF_WINDOW, LBL_WINDOW_TITLE,
              LBL_POST_FLUSH_TEXT, POST_FLUSH_OK, POST_FLUSH_CANCEL,
              IF_EXIT);
    define_click_area(CA_POST_BLOCK, C_EMPTY, None, 280, 100, (RES_X - 280),
                    (RES_Y - 100));
    _local2 = actor[CA_POST_BLOCK];
    with (_local2) {
        useHandCursor = False;
        buttonMode = False;
    };
    define_from_class(INP_POST_SUBJECT, SimpleTextField, POST_INP_X,
                    POST_SUBJECT_Y, 2, "text");
    define_from_class(INP_POST_ADDRESS, SimpleTextField, POST_INP_X,
                    POST_ADDRESS_Y, 2, "name");
    define_from_class(INP_POST_TEXT, SimpleTextArea, POST_INP_X, POST_TEXT_Y,
                    2, "text");
    CleanupField(INP_POST_SUBJECT);
    CleanupField(INP_POST_ADDRESS);
    CleanupField(INP_POST_TEXT);
    AdvancedPostHandler = function (evt:TextEvent){
        var i;
        var textEntered:String;
        if (evt.text.length == 1){
            textEntered = (actor[INP_POST_ADDRESS].getChildAt(1).text[
                           0: actor[INP_POST_ADDRESS].getChildAt(1)
                           .selectionBeginIndex] + evt.text);
            i = 0;
            while (i < suggestNames.length) {
                if ((((textEntered.length > 0))
                    and ((textEntered.lower() == suggestNames[i].lower()[
                         0: textEntered.length])))){
                    actor[INP_POST_ADDRESS].getChildAt(1).text = (
                      textEntered + suggestNames[i][textEntered.length:]);
                    actor[INP_POST_ADDRESS].getChildAt(1).setSelection(
                       textEntered.length, actor[INP_POST_ADDRESS]
                       .getChildAt(1).text.length);
                    evt.preventDefault();
                    break;
                };
                i++;
            };
        };
    };
    killFieldContent = function (evt:Event){
        var actor_id;
        actor_id = get_actor_id(evt.target.parent);
        if (actor[actor_id].getChildAt(1).type == TextFieldType.DYNAMIC){
            return;
        };
        Switch (actor_id){
            if case(INP_POST_ADDRESS:
                if (actor[actor_id].getChildAt(1).text == texts[
                    TXT_EMPFAENGER]){
                    actor[actor_id].getChildAt(1).text = "";
                };
                break;
            if case(INP_POST_SUBJECT:
                if (actor[actor_id].getChildAt(1).text == texts[
                    TXT_BETREFF]){
                    actor[actor_id].getChildAt(1).text = "";
                };
                break;
            if case(INP_POST_TEXT:
                if (actor[actor_id].getChildAt(1).text == texts[
                        TXT_NACHRICHT]){
                    actor[actor_id].getChildAt(1).text = "";
                };
                break;
        };
    };
    fillFieldContent = function (evt:Event){
        var actor_id;
        actor_id = get_actor_id(evt.target.parent);
        Switch (actor_id){
            if case(INP_POST_ADDRESS:
                if (actor[actor_id].getChildAt(1).text == ""){
                    actor[actor_id].getChildAt(1).text = texts[
                        TXT_EMPFAENGER];
                };
                break;
            if case(INP_POST_SUBJECT:
                if (actor[actor_id].getChildAt(1).text == ""){
                    actor[actor_id].getChildAt(1).text = texts[
                        TXT_BETREFF];
                };
                break;
            if case(INP_POST_TEXT:
                if (actor[actor_id].getChildAt(1).text == ""){
                    actor[actor_id].getChildAt(1).text = texts[
                        TXT_NACHRICHT];
                };
                break;
        };
    };
    actor[INP_POST_ADDRESS].getChildAt(1).add_event_listener(
                             TextEvent.TEXT_INPUT, AdvancedPostHandler);
    actor[INP_POST_SUBJECT].add_event_listener(
                               MouseEvent.MOUSE_DOWN, killFieldContent);
    actor[INP_POST_ADDRESS].add_event_listener(
                               MouseEvent.MOUSE_DOWN, killFieldContent);
    actor[INP_POST_TEXT].add_event_listener(
                            MouseEvent.MOUSE_DOWN, killFieldContent);
    actor[INP_POST_SUBJECT].add_event_listener(
                               FocusEvent.FOCUS_OUT, fillFieldContent);
    actor[INP_POST_ADDRESS].add_event_listener(
                           FocusEvent.FOCUS_OUT, fillFieldContent);
    actor[INP_POST_TEXT].add_event_listener(
                            FocusEvent.FOCUS_OUT, fillFieldContent);
    define_btn(POST_SEND, texts[TXT_POST_SEND], PostBtnHandler,
               btn_classBasic, POST_BUTTONS_X, POST_SENDBUTTON_Y);
    define_btn(POST_CANCEL, texts[TXT_POST_CANCEL], PostBtnHandler,
               btn_classBasic,
               ((POST_BUTTONS_X + actor[POST_SEND].width)
                + POST_BUTTONS_X), POST_SENDBUTTON_Y);
    define_btn(POST_RETURN, texts[TXT_POST_RETURN], PostBtnHandler,
               btn_classBasic, POST_BUTTONS_X, POST_SENDBUTTON_Y);
    define_btn(POST_ACCEPT, texts[TXT_POST_ACCEPT], PostBtnHandler,
               btn_classBasic,
               (POST_BUTTONS_X + actor[POST_SEND].width + POST_BUTTONS_X),
               POST_SENDBUTTON_Y);
    define_btn(POST_REPLY, texts[TXT_POST_REPLY], PostBtnHandler,
               btn_classBasic,
               (POST_BUTTONS_X + actor[POST_SEND].width + POST_BUTTONS_X),
               POST_SENDBUTTON_Y);
    define_btn(POST_VIEWFIGHT, texts[TXT_POST_VIEWFIGHT], PostBtnHandler,
               btn_classBasic,
               (POST_BUTTONS_X + actor[POST_SEND].width + POST_BUTTONS_X),
               POST_SENDBUTTON_Y);
    define_lbl(LBL_POST_LIMIT, "", POST_SQUARE_X,
              (POST_SQUARE_Y - POST_LIMIT_Y), FontFormat_Default);
    add_filter(LBL_POST_LIMIT, Filter_Shadow);
    DefineCnt(POST_GUILD, 0, (POST_ADDRESS_Y + 2));
    define_lbl(LBL_POST_GUILD, texts[TXT_GILDEN], 0, 0, FontFormat_Default);
    add_filter(LBL_POST_GUILD, Filter_Shadow);
    MakePersistent(LBL_POST_GUILD);
    _local2 = actor[POST_GUILD];
    with (_local2) {
        addChild(actor[LBL_POST_GUILD]);
        textLinkMakeClickable(getChildAt(0).parent);
        x = (((POST_INP_X + actor[INP_POST_ADDRESS].width) - width) - 5);
        add_event_listener(MouseEvent.CLICK, GuildMsgMode);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    define_bunch(POST_LIST, LBL_POST_TITLE_INBOX, POST_LIST, POST_READ,
                 POST_DELETE, POST_FLUSH, POST_WRITE, POST_UP, POST_DOWN,
                 LBL_POST_LIMIT);
    define_bunch(POST_WRITE, LBL_POST_TITLE_WRITE, INP_POST_SUBJECT,
                 INP_POST_ADDRESS, POST_GUILD, INP_POST_TEXT, POST_SEND,
                 POST_CANCEL);
    define_bunch(POST_READ, LBL_POST_TITLE_READ, INP_POST_SUBJECT,
                 INP_POST_ADDRESS, INP_POST_TEXT, POST_RETURN,
                 POST_DELETEREAD, POST_READ_NEXT, POST_READ_PREV,
                 POST_PROFILE, POST_FORWARD);
    define_bunch(SCREEN_POST, POST_BG, IF_OVL, POST_NIGHT, POST_DAWN,
                 SHP_POST_BLACK_SQUARE, POST_LIST, IF_EXIT);
    define_img(ARENA_BG_DAY, "res/gfx/scr/arena/arena_tag.jpg",
              False, 280, 100);
    define_img(ARENA_BG_DAWN, "res/gfx/scr/arena/arena_abend.jpg",
              False, 280, 100);
    define_img(ARENA_BG_NIGHT, "res/gfx/scr/arena/arena_nacht.jpg",
              False, 280, 100);
    if (Capabilities.version[0: 3] != "IOS"){
        define_img(ARENA_FEUER, "res/gfx/scr/arena/arenafeuer.swf",
                  False, ARENA_FEUER_X, ARENA_FEUER_Y);
    };
    define_lbl(LBL_ARENA_TEXT, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (ARENA_TEXT_X / 2)),
              ((IF_WIN_Y + ARENA_TEXT_Y) + AIRRelMoveY),
              FontFormat_Default);
    define_lbl(LBL_ARENA_DELAY, "",
              (IF_WIN_X + ARENA_DELAY_X),
              ((IF_WIN_Y + ARENA_DELAY_Y) + AIRRelMoveY),
              FontFormat_Default);
    add_filter(LBL_ARENA_TEXT, Filter_Shadow);
    add_filter(LBL_ARENA_DELAY, Filter_Shadow);
    _local2 = actor[LBL_ARENA_TEXT];
    with (_local2) {
        wordWrap = True;
        width = ARENA_TEXT_X;
        text = texts[TXT_ARENA_1];
    };
    define_from_class(INP_ARENA_enemy, text_input1, 0,
                    ((IF_WIN_Y + ARENA_INP_Y) + AIRRelMoveY), 2, "name");
    _local2 = actor[INP_ARENA_enemy];
    with (_local2) {
        getChildAt(1).text = "";
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2)));
        add_event_listener(KeyboardEvent.KEY_DOWN, Attackenemy);
    };
    define_btn(ARENA_OK, texts[TXT_OK], Attackenemy, btn_classBasic, 0,
               ((IF_WIN_Y + ARENA_OK_Y) + AIRRelMoveY));
    _local2 = actor[ARENA_OK];
    with (_local2) {
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2)));
    };
    define_bunch(WINDOW_ARENA, IF_WINDOW, LBL_WINDOW_TITLE, LBL_ARENA_TEXT,
                 INP_ARENA_enemy, LBL_ARENA_DELAY, ARENA_OK);
    define_bunch(SCREEN_ARENA_DAY, ARENA_BG_DAY);
    define_bunch(SCREEN_ARENA_DAWN, ARENA_BG_DAWN);
    define_bunch(SCREEN_ARENA_NIGHT, ARENA_BG_NIGHT);
    if (Capabilities.version[0: 3] == "IOS"){
        define_bunch(SCREEN_ARENA, IF_OVL, WINDOW_ARENA, IF_EXIT);
    } else {
        define_bunch(SCREEN_ARENA, ARENA_FEUER, IF_OVL, WINDOW_ARENA,
                     IF_EXIT);
    };
    define_img(STALL_BG_GUT, "res/gfx/scr/stall/stall_gut.jpg",
              False, 280, 100);
    define_img(STALL_BG_BOESE, "res/gfx/scr/stall/stall_boese.jpg",
              False, 280, 100);
    define_img(STALL_DAWN, "res/gfx/scr/stall/stall_abend.jpg",
              False, (280 + STALL_TUER_X), (100 + STALL_TUER_Y));
    define_img(STALL_NIGHT, "res/gfx/scr/stall/stall_nacht.jpg",
              False, (280 + STALL_TUER_X), (100 + STALL_TUER_Y));
    define_img(STALL_ARME1, "res/gfx/scr/stall/stall_arme1.png",
              False, (280 + STALL_ARME_X), (100 + STALL_ARME_Y));
    define_img(STALL_ARME2, "res/gfx/scr/stall/stall_arme2.png",
              False, (280 + STALL_ARME_X), (100 + STALL_ARME_Y));
    define_img(STALL_ARME3, "res/gfx/scr/stall/stall_arme3.png",
              False, (280 + STALL_ARME_X), (100 + STALL_ARME_Y));
    define_img(STALL_ARME4, "res/gfx/scr/stall/stall_arme4.png",
              False, (280 + STALL_ARME_X), (100 + STALL_ARME_Y));
    define_img(STALL_ARME5, "res/gfx/scr/stall/stall_arme5.png",
              False, (280 + STALL_ARME_X), (100 + STALL_ARME_Y));
    define_img(STALL_OVL_GUT1, "res/gfx/scr/stall/tiger2_mouseover.jpg",
              False, (280 + STALL_OVL_GUT1_X), (100 + STALL_OVL_GUT1_Y));
    define_img(STALL_OVL_GUT2, "res/gfx/scr/stall/kuh_mouseover.jpg",
              False, (280 + STALL_OVL_GUT2_X), (100 + STALL_OVL_GUT2_Y));
    define_img(STALL_OVL_GUT3, "res/gfx/scr/stall/horse_mouseover.jpg",
              False, (280 + STALL_OVL_GUT3_X), (100 + STALL_OVL_GUT3_Y));
    define_img(STALL_OVL_GUT4, "res/gfx/scr/stall/greif_mouseover.jpg",
              False, (280 + STALL_OVL_GUT4_X), (100 + STALL_OVL_GUT4_Y));
    define_img(STALL_OVL_BOESE1, "res/gfx/scr/stall/pig_mouseover.jpg",
              False, (280 + STALL_OVL_BOESE1_X),
              (100 + STALL_OVL_BOESE1_Y));
    define_img(STALL_OVL_BOESE2, "res/gfx/scr/stall/wolf_mouseover.jpg",
              False, (280 + STALL_OVL_BOESE2_X),
              (100 + STALL_OVL_BOESE2_Y));
    define_img(STALL_OVL_BOESE3, "res/gfx/scr/stall/raptor_mouseover.jpg",
              False, (280 + STALL_OVL_BOESE3_X),
              (100 + STALL_OVL_BOESE3_Y));
    define_img(STALL_OVL_BOESE4, "res/gfx/scr/stall/dragon_mouseover.jpg",
              False, (280 + STALL_OVL_BOESE4_X),
              (100 + STALL_OVL_BOESE4_Y));
    define_click_area(CA_STALL_BOX_GUT1, STALL_OVL_GUT1, ClickMount,
                    (STALL_BOX1_X + 280), (STALL_BOX1_Y + 100),
                    STALL_BOX1_X, STALL_BOX1_Y);
    define_click_area(CA_STALL_BOX_GUT2, STALL_OVL_GUT2, ClickMount,
                    (STALL_BOX2_X + 280), (STALL_BOX2_Y + 100),
                    STALL_BOX2_X, STALL_BOX2_Y);
    define_click_area(CA_STALL_BOX_GUT3, STALL_OVL_GUT3, ClickMount,
                    (STALL_BOX3_X + 280), (STALL_BOX3_Y + 100),
                    STALL_BOX3_X, STALL_BOX3_Y);
    define_click_area(CA_STALL_BOX_GUT4, STALL_OVL_GUT4, ClickMount,
                    (STALL_BOX4_X + 280), (STALL_BOX4_Y + 100),
                    STALL_BOX4_X, STALL_BOX4_Y);
    define_click_area(CA_STALL_BOX_BOESE1, STALL_OVL_BOESE1, ClickMount,
                    (STALL_BOX1_X + 280), (STALL_BOX1_Y + 100),
                    STALL_BOX1_X, STALL_BOX1_Y);
    define_click_area(CA_STALL_BOX_BOESE2, STALL_OVL_BOESE2, ClickMount,
                    (STALL_BOX2_X + 280), (STALL_BOX2_Y + 100),
                    STALL_BOX2_X, STALL_BOX2_Y);
    define_click_area(CA_STALL_BOX_BOESE3, STALL_OVL_BOESE3, ClickMount,
                    (STALL_BOX3_X + 280), (STALL_BOX3_Y + 100),
                    STALL_BOX3_X, STALL_BOX3_Y);
    define_click_area(CA_STALL_BOX_BOESE4, STALL_OVL_BOESE4, ClickMount,
                    (STALL_BOX4_X + 280), (STALL_BOX4_Y + 100),
                    STALL_BOX4_X, STALL_BOX4_Y);
    i = 0;
    while (i < 8) {
        define_snd((SND_MOUNT_1 + i),
                   (("res/sfx/mounts/mount" + str((i + 1))) + ".mp3"));
        i = (i + 1);
    };
    define_bunch(STALL_GUT, STALL_BG_GUT, IF_OVL, CA_STALL_BOX_GUT1,
                 CA_STALL_BOX_GUT2, CA_STALL_BOX_GUT3, CA_STALL_BOX_GUT4);
    define_bunch(STALL_BOESE, STALL_BG_BOESE, IF_OVL, CA_STALL_BOX_BOESE1,
                 CA_STALL_BOX_BOESE2, CA_STALL_BOX_BOESE3,
                 CA_STALL_BOX_BOESE4);
    define_bunch(SCREEN_STALL, STALL_DAWN, STALL_NIGHT, STALL_ARME1,
                 STALL_ARME2, STALL_ARME3, STALL_ARME4, STALL_ARME5,
                 IF_EXIT);
    define_from_class(SHP_STALL_BLACK_SQUARE, black_square_neutral,
                    (SCREEN_TITLE_X - int((STALL_SQUARE_X / 2))),
                    STALL_SQUARE_Y);
    _local2 = actor[SHP_STALL_BLACK_SQUARE];
    with (_local2) {
        width = STALL_SQUARE_X;
        height = STALL_SQUARE_Y;
        alpha = 0.65;
    };
    define_lbl(LBL_STALL_TITEL, texts[TXT_STALL_TITEL],
              (actor[SHP_STALL_BLACK_SQUARE].x + STALL_TITEL_X),
              (actor[SHP_STALL_BLACK_SQUARE].y + STALL_TITEL_Y),
              FontFormat_Heading);
    define_lbl(LBL_STALL_TEXT, texts[TXT_STALL_TEXT],
              (actor[SHP_STALL_BLACK_SQUARE].x + STALL_TITEL_X),
              ((actor[LBL_STALL_TITEL].y
               + actor[LBL_STALL_TITEL].textHeight) + STALL_ZEILEN_Y),
                FontFormat_DefaultLeft);
    _local2 = actor[LBL_STALL_TEXT];
    with (_local2) {
        wordWrap = True;
        width = (STALL_SQUARE_X - (STALL_TITEL_X * 2));
    };
    define_lbl(LBL_STALL_GAIN, "",
              (actor[SHP_STALL_BLACK_SQUARE].x + STALL_TITEL_X),
              (((actor[LBL_STALL_TITEL].y
               + actor[LBL_STALL_TITEL].textHeight) + STALL_ZEILEN_Y)
            + STALL_GAIN_Y), FontFormat_DefaultLeft);
    define_lbl(LBL_STALL_SCHATZ, texts[TXT_STALL_SCHATZ], 0,
              actor[LBL_STALL_GAIN].y, FontFormat_DefaultLeft);
    define_lbl(LBL_STALL_SCHATZGOLD, "", 0, actor[LBL_STALL_GAIN].y,
              FontFormat_DefaultLeft);
    define_lbl(LBL_STALL_SCHATZSILBER, "", 0, actor[LBL_STALL_GAIN].y,
              FontFormat_DefaultLeft);
    DefineCnt(STALL_SCHATZGOLD, 0, actor[LBL_STALL_GAIN].y);
    DefineCnt(STALL_SCHATZSILBER, 0, actor[LBL_STALL_GAIN].y);
    define_lbl(LBL_STALL_GOLD, "0",
              (actor[SHP_STALL_BLACK_SQUARE].x + STALL_TITEL_X), 0,
              FontFormat_Default);
    _local2 = actor[LBL_STALL_GOLD];
    with (_local2) {
        y = (((STALL_SQUARE_Y + STALL_SQUARE_Y)
             - STALL_TITEL_Y) - textHeight);
        DefineCnt(STALL_GOLD,
                  (actor[SHP_STALL_BLACK_SQUARE].x + STALL_TITEL_X), y);
        define_lbl(LBL_STALL_MUSH, "0", 0, y, FontFormat_Default);
        DefineCnt(STALL_MUSH, 0, y);
        define_lbl(LBL_STALL_LAUFZEIT, texts[TXT_STALL_LAUFZEIT],
                  (actor[SHP_STALL_BLACK_SQUARE].x + STALL_TITEL_X),
                  ((y - textHeight) - STALL_ZEILEN_Y),
                  FontFormat_Default);
    };
    define_btn(STALL_BUY, texts[TXT_STALL_BUY], BuyMount,
               btn_classBasic, 0, 0);
    _local2 = actor[STALL_BUY];
    with (_local2) {
        x = (((SCREEN_TITLE_X + int((STALL_SQUARE_X / 2)))
             - width) - STALL_TITEL_X);
        y = (((STALL_SQUARE_Y + STALL_SQUARE_Y) - STALL_TITEL_Y) - height);
    };
    add_bunch(SCREEN_STALL, SHP_STALL_BLACK_SQUARE, LBL_STALL_TITEL,
              LBL_STALL_TEXT, LBL_STALL_GAIN);
    SelectedMount = 0;
    OldMount = 0;
    define_img(GILDEN_BG, "res/gfx/scr/gilde/gilde.jpg", False, 280, 100);
    define_img(GILDE_RAHMEN, "res/gfx/scr/gilde/gilde_interface.png",
              False, 280, 100);
    define_lbl(LBL_GILDE_GRUENDEN_TEXT, "", ((IF_WIN_X + IF_WIN_WELCOME_X)
              - (GILDE_GRUENDEN_TEXT_X / 2)),
            ((IF_WIN_Y + GILDE_GRUENDEN_TEXT_Y) + AIRRelMoveY),
            FontFormat_Default);
    add_filter(LBL_GILDE_GRUENDEN_TEXT, Filter_Shadow);
    _local2 = actor[LBL_GILDE_GRUENDEN_TEXT];
    with (_local2) {
        wordWrap = True;
        width = GILDE_GRUENDEN_TEXT_X;
        text = texts[TXT_GILDE_GRUENDEN];
    };
    arabize(LBL_GILDE_GRUENDEN_TEXT);
    define_from_class(INP_GILDE_GRUENDEN, text_input1, 0,
                    ((IF_WIN_Y + GILDE_GRUENDEN_INP_Y) + AIRRelMoveY),
                    2, "name");
    _local2 = actor[INP_GILDE_GRUENDEN];
    with (_local2) {
        getChildAt(1).text = "";
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2)));
    };
    define_btn(GILDE_GRUENDEN, texts[TXT_GILDE_GRUENDEN_OK], GildeGruenden,
               btn_classBasic, 0,
               ((IF_WIN_Y + GILDE_GRUENDEN_OK_Y) + AIRRelMoveY));
    _local2 = actor[GILDE_GRUENDEN];
    with (_local2) {
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2)));
    };
    define_bunch(GILDE_GEBAEUDE);
    i = 0;
    while (i < 3) {
        define_img((GILDE_GEBAEUDE + i),
                  (("res/gfx/scr/gilde/building" + str((i + 1))) + ".png"),
                  False, GILDE_GEBAEUDE_X,
                  (GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i)));
        define_lbl((LBL_GILDE_GEBAEUDE_NAME + i),
                  texts[(TXT_GILDE_GEBAEUDE_NAME1 + i)],
                  (GILDE_GEBAEUDE_X + GILDE_TEXT_X),
                  (GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i)),
                  FontFormat_GuildBuilding);
        define_lbl((LBL_GILDE_GEBAEUDE_WERT_CAPTION + i),
                  texts[(TXT_GILDE_GEBAEUDE_WERT1 + i)],
                  (GILDE_GEBAEUDE_X + GILDE_TEXT_X),
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 1)), FontFormat_GuildBuilding);
        define_lbl((LBL_GILDE_GEBAEUDE_WERT + i), "",
                  (GILDE_GEBAEUDE_X + GILDE_TEXT_IMPROVE_X),
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 2)), FontFormat_GuildBuilding);
        define_lbl((LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i),
                  texts[TXT_GILDE_GEBAEUDE_STUFE],
                  (GILDE_GEBAEUDE_X + GILDE_TEXT_IMPROVE_X),
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 3)), FontFormat_GuildBuilding);
        define_lbl((LBL_GILDE_GEBAEUDE_STUFE + i), "",
                  ((actor[(LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i)].x
                   + actor[(LBL_GILDE_GEBAEUDE_STUFE_CAPTION
                            + i)].text_width) + 10),
                    actor[(LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i)].y,
                    FontFormat_GuildBuilding);
        define_lbl((LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i), "", 0,
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 4)), FontFormat_GuildBuilding);
        define_lbl((LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i), "", 0,
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 4)), FontFormat_GuildBuilding);
        DefineCnt((GILDE_GEBAEUDE_GOLD + i), 0,
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 4)));
        DefineCnt((GILDE_GEBAEUDE_MUSH + i), 0,
                  ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                   + (GILDE_GEBAEUDE_LINE * 4)));
        define_btn((GILDE_GEBAEUDE_IMPROVE + i), "", GildeBtnHandler,
                   btn_classPlus,
                   (GILDE_GEBAEUDE_X + GILDE_GEBAEUDE_IMPROVE_X),
                   ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                    + GILDE_GEBAEUDE_IMPROVE_Y));
        define_img((GILDE_GEBAEUDE_IMPROVE_GRAY + i),
                  "res/gfx/scr/gilde/plus_disabled.png", False,
                  (GILDE_GEBAEUDE_X + GILDE_GEBAEUDE_IMPROVE_X),
                   ((GILDE_GEBAEUDE_Y + (GILDE_GEBAEUDE_Y * i))
                    + GILDE_GEBAEUDE_IMPROVE_Y));
        add_filter((LBL_GILDE_GEBAEUDE_NAME + i), Filter_Shadow);
        add_filter((LBL_GILDE_GEBAEUDE_WERT_CAPTION + i), Filter_Shadow);
        add_filter((LBL_GILDE_GEBAEUDE_WERT + i), Filter_Shadow);
        add_filter((LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i), Filter_Shadow);
        add_filter((LBL_GILDE_GEBAEUDE_STUFE + i), Filter_Shadow);
        add_filter((LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i), Filter_Shadow);
        add_filter((LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i), Filter_Shadow);
        enable_popup((GILDE_GEBAEUDE + i),
                     texts[(TXT_GILDE_GEBAEUDE1_POPUP + i)]);
        enable_popup((LBL_GILDE_GEBAEUDE_NAME + i),
                     texts[(TXT_GILDE_GEBAEUDE1_POPUP + i)]);
        enable_popup((LBL_GILDE_GEBAEUDE_WERT_CAPTION + i),
                     texts[(TXT_GILDE_GEBAEUDE1_POPUP + i)]);
        enable_popup((LBL_GILDE_GEBAEUDE_WERT + i),
                     texts[(TXT_GILDE_GEBAEUDE1_POPUP + i)]);
        enable_popup((LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i),
                     texts[(TXT_GILDE_GEBAEUDE1_POPUP + i)]);
        enable_popup((LBL_GILDE_GEBAEUDE_STUFE + i),
                     texts[(TXT_GILDE_GEBAEUDE1_POPUP + i)]);
        enable_popup((GILDE_GEBAEUDE_IMPROVE + i),
                     texts[TXT_GILDE_AUSBAUEN]);
        add_bunch(GILDE_GEBAEUDE, (GILDE_GEBAEUDE + i),
                  (LBL_GILDE_GEBAEUDE_NAME + i),
                  (LBL_GILDE_GEBAEUDE_WERT_CAPTION + i),
                  (LBL_GILDE_GEBAEUDE_WERT + i),
                  (LBL_GILDE_GEBAEUDE_STUFE_CAPTION + i));
        add_bunch(GILDE_GEBAEUDE, (LBL_GILDE_GEBAEUDE_STUFE + i),
                  (LBL_GILDE_GEBAEUDE_KOSTEN_GOLD + i),
                  (LBL_GILDE_GEBAEUDE_KOSTEN_MUSH + i),
                  (GILDE_GEBAEUDE_GOLD + i), (GILDE_GEBAEUDE_MUSH + i),
                  (GILDE_GEBAEUDE_IMPROVE_GRAY + i),
                  (GILDE_GEBAEUDE_IMPROVE + i));
        i = (i + 1);
    };
    define_btn(GILDE_GEBAEUDE_GOTO_CREST, " ", GildeBtnHandler,
               btn_classBack, (GILDE_GEBAEUDE_X + 211),
               (GILDE_GEBAEUDE_Y - 5));
    _local2 = actor[GILDE_GEBAEUDE_GOTO_CREST];
    with (_local2) {
        scaleX = 0.4;
        scaleY = 0.4;
    };
    enable_popup(GILDE_GEBAEUDE_GOTO_CREST,
                 texts[TXT_BUILDINGS_GOTO_CREST]);
    add_bunch(GILDE_GEBAEUDE, GILDE_GEBAEUDE_GOTO_CREST);
    define_bunch(GILDE_CREST);
    DefineCnt(GILDE_CREST, (GILDE_GEBAEUDE_X - 2),
              (GILDE_GEBAEUDE_Y + 60));
    i = 0;
    while (i < crestElementPos.length) {
        define_img((GILDE_CREST + i), "", False, 0, 0);
        actor[(GILDE_CREST + i)].mouse_enabled = False;
        MakePersistent((GILDE_CREST + i));
        crestClaI = i;
        if (crestClaI == 1){
            crestClaI = 0;
        } else {
            if (crestClaI == 0){
                crestClaI = 1;
            };
        };
        define_click_area((CLA_GILDE_CREST + crestClaI), C_EMPTY,
                        GildeBtnHandler, crestElementPos[crestClaI][0],
                        crestElementPos[crestClaI][1],
                        crestElementPos[crestClaI][2],
                        crestElementPos[crestClaI][3],
                        0, None, None, True);
        MakePersistent((CLA_GILDE_CREST + crestClaI));
        _local2 = actor[GILDE_CREST];
        with (_local2) {
            addChild(actor[(GILDE_CREST + i)]);
            addChild(actor[(CLA_GILDE_CREST + crestClaI)]);
            if (i == 2){
                define_img(GILDE_CREST_SHIELDCOLOR, "", False, 0, 0);
                actor[GILDE_CREST_SHIELDCOLOR].mouse_enabled = False;
                MakePersistent(GILDE_CREST_SHIELDCOLOR);
                addChild(actor[GILDE_CREST_SHIELDCOLOR]);
            };
            if (i == 3){
                define_lbl(LBL_GILDE_CREST_INSCRIPTION, "Gildenname", 15,
                          210, FontFormat_Book);
                actor[LBL_GILDE_CREST_INSCRIPTION].mouse_enabled = False;
                MakePersistent(LBL_GILDE_CREST_INSCRIPTION);
                addChild(actor[LBL_GILDE_CREST_INSCRIPTION]);
            };
        };
        i = (i + 1);
    };
    define_btn(GILDE_CREST_GOTO_GEBAEUDE, " ", GildeBtnHandler,
               btn_classBack, (GILDE_GEBAEUDE_X + 211),
               (GILDE_GEBAEUDE_Y - 5));
    _local2 = actor[GILDE_CREST_GOTO_GEBAEUDE];
    with (_local2) {
        scaleX = 0.4;
        scaleY = 0.4;
    };
    enable_popup(GILDE_CREST_GOTO_GEBAEUDE,
                 texts[TXT_CREST_GOTO_BUILDINGS]);
    define_bunch(GILDE_CREST_CONTROLS);
    define_btn(GILDE_CREST_CHANGE_PREV, "", GildeBtnHandler,
               btn_classArrowLeft, (GILDE_GEBAEUDE_X + 10),
               (GILDE_GEBAEUDE_Y + 250));
    define_btn(GILDE_CREST_CHANGE_NEXT, "", GildeBtnHandler,
               btn_classArrowRight, (GILDE_GEBAEUDE_X + 193),
               (GILDE_GEBAEUDE_Y + 250));
    define_lbl(LBL_GILDE_CREST_ELEMENT, "Element",
              (GILDE_GEBAEUDE_X + 120), (GILDE_GEBAEUDE_Y + 0xFF),
              FontFormat_Default);
    add_filter(LBL_GILDE_CREST_ELEMENT, Filter_Shadow);
    define_btn(GILDE_CREST_COLOR_PREV, "", GildeBtnHandler,
               btn_classArrowLeft, (GILDE_GEBAEUDE_X + 10),
               (GILDE_GEBAEUDE_Y + 295));
    define_btn(GILDE_CREST_COLOR_NEXT, "", GildeBtnHandler,
               btn_classArrowRight, (GILDE_GEBAEUDE_X + 193),
               (GILDE_GEBAEUDE_Y + 295));
    define_btn(GILDE_CREST_OK, texts[TXT_CREST_SUGGEST],
               GildeBtnHandler, btn_classBasic, (GILDE_GEBAEUDE_X + 30),
               (GILDE_GEBAEUDE_Y + 340));
    enable_popup(GILDE_CREST_OK,
                 texts[TXT_CREST_INFO].split("#").join(chr(13)));
    i = 1;
    while (i < 4) {
        DefineCnt((GILDE_CREST_COLOR + i),
                  ((GILDE_GEBAEUDE_X + 23) + (i * 40)),
                  (GILDE_GEBAEUDE_Y + 296));
        define_img((GILDE_CREST_COLOR_UNSELECTED + i),
                  "res/gfx/scr/gilde/crest/color_idle.jpg", False, 0, 0);
        define_img((GILDE_CREST_COLOR_SELECTED + i),
                  "res/gfx/scr/gilde/crest/color_hover.jpg", False, 0, 0);
        define_img((GILDE_CREST_COLOR_FILLIN + i),
                  "res/gfx/scr/gilde/crest/color_field.jpg", False, 2, 2);
        MakePersistent((GILDE_CREST_COLOR_UNSELECTED + i));
        MakePersistent((GILDE_CREST_COLOR_SELECTED + i));
        MakePersistent((GILDE_CREST_COLOR_FILLIN + i));
        _local2 = actor[(GILDE_CREST_COLOR + i)];
        with (_local2) {
            addChild(actor[(GILDE_CREST_COLOR_UNSELECTED + i)]);
            addChild(actor[(GILDE_CREST_COLOR_SELECTED + i)]);
            addChild(actor[(GILDE_CREST_COLOR_FILLIN + i)]);
        };
        actor[(GILDE_CREST_COLOR + i)].add_event_listener(
                                  MouseEvent.CLICK, GildeBtnHandler);
        actor[(GILDE_CREST_COLOR + i)].buttonMode = True;
        actor[(GILDE_CREST_COLOR + i)].useHandCursor = True;
        actor[(GILDE_CREST_COLOR + i)].mouseChildren = False;
        add_bunch(GILDE_CREST_CONTROLS, (GILDE_CREST_COLOR + i));
        i = (i + 1);
    };
    add_bunch(GILDE_CREST_CONTROLS, GILDE_CREST_CHANGE_PREV,
              GILDE_CREST_CHANGE_NEXT, LBL_GILDE_CREST_ELEMENT,
              GILDE_CREST_COLOR_PREV, GILDE_CREST_COLOR_NEXT,
              GILDE_CREST_OK);
    add_bunch(GILDE_CREST, GILDE_CREST, GILDE_CREST_GOTO_GEBAEUDE);
    define_lbl(LBL_GILDE_GOLD, "", 0, (GILDE_GOLD_Y + ((noMush) ? 15 : 0)),
              FontFormat_GuildMoney);
    add_filter(LBL_GILDE_GOLD, Filter_Shadow);
    define_lbl(LBL_GILDE_MUSH, "", 0, (GILDE_GOLD_Y + GILDE_MUSH_Y),
              FontFormat_GuildMoney);
    add_filter(LBL_GILDE_MUSH, Filter_Shadow);
    DefineCnt(GILDE_GOLD, GILDE_GOLDMUSH_X,
              (GILDE_GOLD_Y + ((noMush) ? 15 : 0)));
    DefineCnt(GILDE_MUSH, GILDE_GOLDMUSH_X, (GILDE_GOLD_Y + GILDE_MUSH_Y));
    define_btn(GILDE_GOLD, "", GildeBtnHandler, btn_classPlus,
               (GILDE_GOLDMUSH_X + GILDE_GOLDMUSH_C2),
               (GILDE_GOLD_Y + ((noMush) ? 15 : 0)));
    _local2 = actor[GILDE_GOLD];
    with (_local2) {
        scaleX = 0.8;
        scaleY = 0.8;
    };
    enable_popup(GILDE_GOLD, texts[TXT_GILDE_GOLD]);
    define_btn(GILDE_MUSH, "", GildeBtnHandler, btn_classPlus,
               (GILDE_GOLDMUSH_X + GILDE_GOLDMUSH_C2),
               (GILDE_GOLD_Y + GILDE_MUSH_Y));
    _local2 = actor[GILDE_MUSH];
    with (_local2) {
        scaleX = 0.8;
        scaleY = 0.8;
    };
    enable_popup(GILDE_MUSH, texts[TXT_GILDE_MUSH]);
    define_lbl(LBL_GILDE_GOLD2, "1", (GILDE_GOLDMUSH_X + GILDE_GOLDMUSH_C3),
              (GILDE_GOLD_Y + ((noMush) ? 15 : 0)), FontFormat_GuildMoney);
    add_filter(LBL_GILDE_GOLD2, Filter_Shadow);
    enable_popup(LBL_GILDE_GOLD2, texts[TXT_GILDE_GOLD]);
    define_lbl(LBL_GILDE_MUSH2, "1", 0, (GILDE_GOLD_Y + GILDE_MUSH_Y),
              FontFormat_GuildMoney);
    add_filter(LBL_GILDE_MUSH2, Filter_Shadow);
    enable_popup(LBL_GILDE_MUSH2, texts[TXT_GILDE_MUSH]);
    actor[LBL_GILDE_MUSH2].x = ((actor[LBL_GILDE_GOLD2].x
                                + actor[LBL_GILDE_GOLD2].text_width)
                                    - actor[LBL_GILDE_MUSH2].text_width);
    DefineCnt(GILDE_GOLD2,
              ((actor[LBL_GILDE_GOLD2].x
               + actor[LBL_GILDE_GOLD2].text_width) + 15),
                (GILDE_GOLD_Y + ((noMush) ? 15 : 0)));
    DefineCnt(GILDE_MUSH2,
              ((actor[LBL_GILDE_GOLD2].x
               + actor[LBL_GILDE_GOLD2].text_width) + 15),
                (GILDE_GOLD_Y + GILDE_MUSH_Y));
    if (noMush){
        define_bunch(GILDE_SCHATZ, LBL_GILDE_GOLD, GILDE_GOLD, GILDE_GOLD,
                     LBL_GILDE_GOLD2, GILDE_GOLD2);
    } else {
        define_bunch(GILDE_SCHATZ, LBL_GILDE_GOLD, LBL_GILDE_MUSH,
                     GILDE_GOLD, GILDE_MUSH, GILDE_GOLD, GILDE_MUSH,
                     LBL_GILDE_GOLD2, LBL_GILDE_MUSH2, GILDE_GOLD2,
                     GILDE_MUSH2);
    };
    define_bunch(SCREEN_GILDE_GRUENDEN, GILDEN_BG, IF_WINDOW,
                 LBL_WINDOW_TITLE, IF_OVL, LBL_GILDE_GRUENDEN_TEXT,
                 INP_GILDE_GRUENDEN, GILDE_GRUENDEN, IF_EXIT);
    define_bunch(SCREEN_GILDEN, GILDEN_BG, IF_OVL, GILDE_RAHMEN, IF_EXIT,
                 LBL_SCREEN_TITLE, GILDE_GEBAEUDE, GILDE_CREST,
                 GILDE_SCHATZ);
    DefineCnt(GILDE_RANG, GILDE_RANG_X, GILDE_RANG_Y);
    define_lbl(LBL_GILDE_RANG, "", 0, 0, FontFormat_Default);
    add_filter(LBL_GILDE_RANG, Filter_Shadow);
    _local2 = actor[GILDE_RANG];
    with (_local2) {
        addChild(actor[LBL_GILDE_RANG]);
        textLinkMakeClickable(getChildAt(0).parent);
        mouseChildren = False;
        mouse_enabled = True;
        buttonMode = True;
        useHandCursor = True;
        add_event_listener(MouseEvent.CLICK, JumpToGuildHall);
    };
    MakePersistent(LBL_GILDE_RANG);
    define_from_class(INP_GILDE_TEXT, SimpleTextAreaGuild, GILDE_TEXT_X,
                    GILDE_LIST_Y, 1, "text");
    CleanupField(INP_GILDE_TEXT);
    add_filter(INP_GILDE_TEXT, Filter_Shadow);
    DefineCnt(GILDE_LIST, GILDE_LIST_X, GILDE_LIST_Y);
    define_img(GILDE_RANK, "res/gfx/scr/gilde/punkt_krone.png",
              False, 0, 0);
    define_img((GILDE_RANK + 1), "res/gfx/scr/gilde/punkt_orden.png",
              False, 0, 0);
    define_img((GILDE_RANK + 2), "res/gfx/scr/gilde/punkt_normalo.png",
              False, 0, 0);
    define_btn(GILDE_SCROLL_UP, "", GildeBtnHandler, btn_classArrowUp,
               GILDE_LIST_SCROLLX, GILDE_LIST_Y);
    define_btn(GILDE_SCROLL_DOWN, "", GildeBtnHandler, btn_classArrowDown,
               GILDE_LIST_SCROLLX, GILDE_LIST_SCROLLY);
    i = 0;
    define_img(GILDE_INVITE_GRAY,
              "res/gfx/scr/gilde/button_gilde_einladen_grau.jpg", False,
              (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    i = (i + 1);
    define_btn(GILDE_INVITE, "", GildeBtnHandler, btn_classInvite,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    i = (i + 1);
    define_btn(GILDE_PROFILE, "", GildeBtnHandler, btn_classView,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    define_img(GILDE_KICK_GRAY,
              "res/gfx/scr/gilde/button_gilde_rauswerfen_grau.jpg", False,
              (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    i = (i + 1);
    define_btn(GILDE_KICK, "", GildeBtnHandler, btn_classKick,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    define_img(GILDE_PROMOTE_GRAY,
              "res/gfx/scr/gilde/button_gilde_orden_grau.jpg", False,
              (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    define_btn(GILDE_PROMOTE, "", GildeBtnHandler, btn_classPromote,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    i = (i + 1);
    define_btn(GILDE_DEMOTE, "", GildeBtnHandler, btn_classDemote,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    define_img(GILDE_MASTER_GRAY,
              "res/gfx/scr/gilde/button_gilde_gildenleiter_grau.jpg",
              False, (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    define_btn(GILDE_MASTER, "", GildeBtnHandler, btn_classMaster,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    i = (i + 1);
    define_btn(GILDE_REVOLT, "", GildeBtnHandler, btn_classRevolt,
               (GILDE_TOOLX + (i * GILDE_TOOLX)), GILDE_TOOLY);
    define_btn(GILDE_RAID, "", GildeBtnHandler, btn_classRaid,
               (GILDE_ATTACKX - 50), GILDE_TOOLY);
    define_img(GILDE_RAID_GRAY,
              "res/gfx/scr/gilde/button_gilde_raid_grey.jpg", False,
              (GILDE_ATTACKX - 50), GILDE_TOOLY);
    define_img(GILDE_RAID_OK,
              "res/gfx/scr/gilde/button_gilde_raid_check.jpg", False,
              (GILDE_ATTACKX - 50), GILDE_TOOLY);
    define_btn(GILDE_ATTACK, "", GildeBtnHandler, btn_classAttack,
               (GILDE_ATTACKX + 5), GILDE_TOOLY);
    define_btn(GILDE_DEFEND, "", GildeBtnHandler, btn_classDefend,
               (GILDE_DEFENDX + 5), GILDE_TOOLY);
    define_img(GILDE_ATTACK_GRAY,
              "res/gfx/scr/gilde/button_gilde_attack_grau.jpg", False,
              (GILDE_ATTACKX + 5), GILDE_TOOLY);
    define_img(GILDE_ATTACK_OK,
              "res/gfx/scr/gilde/button_gilde_attack_check.jpg", False,
              (GILDE_ATTACKX + 5), GILDE_TOOLY);
    define_img(GILDE_DEFEND_GRAY,
              "res/gfx/scr/gilde/button_gilde_defend_grau.jpg", False,
              (GILDE_DEFENDX + 5), GILDE_TOOLY);
    define_img(GILDE_DEFEND_OK,
              "res/gfx/scr/gilde/button_gilde_defend_check.jpg", False,
              (GILDE_DEFENDX + 5), GILDE_TOOLY);
    define_btn(GILDE_KATAPULT, "", GildeBtnHandler, btn_classCatapult0,
               (GILDE_ATTACKX - 105), GILDE_TOOLY);
    define_btn((GILDE_KATAPULT + 1), "", GildeBtnHandler,
               btn_classCatapult1, actor[GILDE_KATAPULT].x,
               actor[GILDE_KATAPULT].y);
    define_btn((GILDE_KATAPULT + 2), "", GildeBtnHandler,
               btn_classCatapult2, actor[GILDE_KATAPULT].x,
               actor[GILDE_KATAPULT].y);
    define_img(GILDE_KATAPULT_GRAY,
              "res/gfx/scr/gilde/button_gilde_catapult0_grau.png",
              False, actor[GILDE_KATAPULT].x, actor[GILDE_KATAPULT].y);
    define_img(GILDE_KATAPULT_OK,
              "res/gfx/scr/gilde/button_gilde_catapult1_idle.png", False,
              actor[GILDE_KATAPULT].x, actor[GILDE_KATAPULT].y);
    define_img((GILDE_KATAPULT_OK + 1),
              "res/gfx/scr/gilde/button_gilde_catapult2_idle.png",
              False, actor[GILDE_KATAPULT].x, actor[GILDE_KATAPULT].y);
    define_img((GILDE_KATAPULT_OK + 2),
              "res/gfx/scr/gilde/button_gilde_catapult3_idle.png",
              False, actor[GILDE_KATAPULT].x, actor[GILDE_KATAPULT].y);
    define_bunch(GILDE_KATAPULT, GILDE_KATAPULT, (GILDE_KATAPULT + 1),
                 (GILDE_KATAPULT + 2), GILDE_KATAPULT_GRAY,
                 GILDE_KATAPULT_OK, (GILDE_KATAPULT_OK + 1),
                 (GILDE_KATAPULT_OK + 2));
    DefineCnt(GILDE_ATTACK, GILDE_ATTACKLABEL_X, GILDE_TOOLY);
    DefineCnt(GILDE_DEFENCE, GILDE_ATTACKLABEL_X,
              (GILDE_TOOLY + GILDE_DEFENSELABEL_Y));
    define_lbl(LBL_GILDE_ATTACK, "", 0, 0, FontFormat_AttackLabel);
    define_lbl(LBL_GILDE_DEFENCE, "", 0, 0, FontFormat_AttackLabel);
    add_filter(LBL_GILDE_ATTACK, Filter_Shadow);
    add_filter(LBL_GILDE_DEFENCE, Filter_Shadow);
    MakePersistent(LBL_GILDE_ATTACK, LBL_GILDE_DEFENCE);
    _local2 = actor[GILDE_ATTACK];
    with (_local2) {
        addChild(actor[LBL_GILDE_ATTACK]);
        textLinkMakeClickable(getChildAt(0).parent);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
        add_event_listener(MouseEvent.CLICK, AttackLinkClick);
    };
    _local2 = actor[GILDE_DEFENCE];
    with (_local2) {
        addChild(actor[LBL_GILDE_DEFENCE]);
        textLinkMakeClickable(getChildAt(0).parent);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
        add_event_listener(MouseEvent.CLICK, DefenceLinkClick);
    };
    enable_popup(GILDE_INVITE, texts[TXT_POPUP_INVITE]);
    enable_popup(GILDE_INVITE_GRAY, texts[TXT_POPUP_INVITE]);
    enable_popup(GILDE_PROFILE, texts[TXT_POPUP_PROFILE]);
    enable_popup(GILDE_KICK, texts[TXT_POPUP_KICK]);
    enable_popup(GILDE_KICK_GRAY, texts[TXT_POPUP_KICK]);
    enable_popup(GILDE_PROMOTE, texts[TXT_POPUP_OFFIZIER]);
    enable_popup(GILDE_PROMOTE_GRAY, texts[TXT_POPUP_OFFIZIER]);
    enable_popup(GILDE_DEMOTE, texts[TXT_POPUP_OFFIZIER]);
    enable_popup(GILDE_MASTER, texts[TXT_POPUP_LEITER]);
    enable_popup(GILDE_MASTER_GRAY, texts[TXT_POPUP_LEITER]);
    enable_popup(GILDE_REVOLT, texts[TXT_POPUP_REVOLT]);
    define_bunch(GILDE_SET_MEMBER, GILDE_INVITE_GRAY, GILDE_PROFILE,
                 GILDE_KICK_GRAY, GILDE_PROMOTE_GRAY, GILDE_MASTER_GRAY);
    define_bunch(GILDE_SET_OFFICER, GILDE_INVITE, GILDE_PROFILE,
                 GILDE_KICK, GILDE_PROMOTE_GRAY, GILDE_MASTER_GRAY);
    define_bunch(GILDE_SET_MASTER, GILDE_INVITE, GILDE_PROFILE, GILDE_KICK,
                 GILDE_PROMOTE, GILDE_MASTER);
    define_bunch(GILDE_LISTBUTTONS, GILDE_SET_MEMBER, GILDE_SET_OFFICER,
                 GILDE_SET_MASTER);
    add_bunch(SCREEN_GILDEN, INP_GILDE_TEXT, GILDE_LIST,
              LBL['GILDE']['CHAT']_CAPTION, GILDE_CHAT_UP, GILDE_CHAT_DOWN)
    add_bunch(SCREEN_GILDEN, INP_GILDE_CHAT, GILDE_SCROLL_UP,
              GILDE_SCROLL_DOWN, GILDE_RANG, GILDE_ATTACK, GILDE_DEFENCE);
    define_lbl(LBL['GILDE']['CHAT']_CAPTION, texts[TXT_CHAT_CAPTION],
              GILDE_CHAT_X, (GILDE_CHAT_Y - GILDE_CHAT_CAPTION_Y));
    add_filter(LBL['GILDE']['CHAT']_CAPTION, Filter_Shadow);
    hide(LBL['GILDE']['CHAT']_CAPTION);
    DefineCnt(GILDE_LINK, 0, GILDE_RANG_Y);
    define_lbl(LBL_GILDE_LINK, texts[TXT_FORUM_LINK], 0, 0);
    add_filter(LBL_GILDE_LINK, Filter_HeavyShadow);
    MakePersistent(LBL_GILDE_LINK);
    _local2 = actor[GILDE_LINK];
    with (_local2) {
        addChild(actor[LBL_GILDE_LINK]);
        textLinkMakeClickable(getChildAt(0).parent);
        add_event_listener(MouseEvent.CLICK, OpenGuildLink);
        x = ((GILDE_LIST_SCROLLX - 30) - actor[LBL_GILDE_LINK].text_width);
        mouseChildren = False;
        useHandCursor = True;
        buttonMode = True;
    };
    define_btn(GILDE_CHAT_UP, "", GildeBtnHandler, btn_classArrowUp,
               GILDE_LIST_SCROLLX, (GILDE_CHAT_Y + GILDE_CHAT_UP_Y));
    define_btn(GILDE_CHAT_DOWN, "", GildeBtnHandler, btn_classArrowDown,
               GILDE_LIST_SCROLLX, (GILDE_CHAT_Y + GILDE_CHAT_DOWN_Y));
    define_bunch(GILDE_CHAT, LBL['GILDE']['CHAT']_CAPTION, GILDE_CHAT_UP,
                 GILDE_CHAT_DOWN, INP_GILDE_CHAT);
    i = 0;
    while (i < 40) {
        define_lbl((LBL['GILDE']['CHAT'] + i), "", GILDE_CHAT_X,
                  (GILDE_CHAT_Y + ((i - 35) * GILDE_CHAT_Y)));
        actor[(LBL['GILDE']['CHAT'] + i)].visible = (i >= 35);
        actor[(LBL['GILDE']['CHAT'] + i)].add_event_listener(
                                         MouseEvent.CLICK, clickChatLine);
        add_filter((LBL['GILDE']['CHAT'] + i), Filter_Shadow);
        add_bunch(SCREEN_GILDEN, (LBL['GILDE']['CHAT'] + i));
        add_bunch(GILDE_CHAT, (LBL['GILDE']['CHAT'] + i));
        i = (i + 1);
    };
    define_from_class(INP_GILDE_CHAT, ChatInputField, GILDE_CHAT_X,
                    GILDE_CHAT_FIELD_Y, 1, "chat");
    actor[INP_GILDE_CHAT].getChildAt(0).text = "";
    add_filter(INP_GILDE_CHAT, Filter_Shadow);
    actor[INP_GILDE_CHAT].add_event_listener(KeyboardEvent.KEY_DOWN,
                                             SendChatMsg);
    actor[INP_GILDE_CHAT].add_event_listener(KeyboardEvent.KEY_UP,
                                             AdvancedChatHandler);
    actor[INP_GILDE_CHAT].add_event_listener(FocusEvent.FOCUS_IN,
                                             ShowExtendedHistory);
    actor[INP_GILDE_CHAT].add_event_listener(FocusEvent.FOCUS_OUT,
                                             HideExtendedHistory);
    CleanupField(INP_GILDE_CHAT);
    lastChatLine = "";
    nextSuggestionTimer = new Timer((62 * 1000));
    suggestionAllowed = True;
    nextSuggestionTimer.add_event_listener(TimerEvent.TIMER,
                                           nextSuggestionAllow);
    define_click_area(CA_GILDE_DIALOG_BLOCK, C_EMPTY, None, 280, 100,
                    (RES_X - 280), (RES_Y - 100));
    _local2 = actor[CA_GILDE_DIALOG_BLOCK];
    with (_local2) {
        useHandCursor = False;
        buttonMode = False;
    };
    define_lbl(LBL_GILDE_DIALOG_TEXT_KICK, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (GILDE_TEXT2_X / 2)),
              (IF_WIN_Y + GILDE_TEXT_Y), FontFormat_Default);
    define_lbl(LBL_GILDE_DIALOG_TEXT_QUIT, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (GILDE_TEXT2_X / 2)),
              (IF_WIN_Y + GILDE_TEXT_Y), FontFormat_Default);
    define_lbl(LBL_GILDE_DIALOG_TEXT_MASTER, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (GILDE_TEXT2_X / 2)),
              (IF_WIN_Y + GILDE_TEXT_Y), FontFormat_Default);
    define_lbl(LBL_GILDE_DIALOG_TEXT_INVITE, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (GILDE_TEXT2_X / 2)),
              (IF_WIN_Y + GILDE_TEXT_Y), FontFormat_Default);
    define_lbl(LBL_GILDE_DIALOG_TEXT_REVOLT, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (GILDE_TEXT2_X / 2)),
              (IF_WIN_Y + GILDE_TEXT_Y), FontFormat_Default);
    define_lbl(LBL_GILDE_DIALOG_TEXT_RAID, "",
              ((IF_WIN_X + IF_WIN_WELCOME_X) - (GILDE_TEXT2_X / 2)),
              (IF_WIN_Y + GILDE_TEXT_Y), FontFormat_Default);
    _local2 = actor[LBL_GILDE_DIALOG_TEXT_KICK];
    with (_local2) {
        wordWrap = True;
        width = GILDE_TEXT2_X;
        text = texts[TXT_GILDE_KICK];
    };
    _local2 = actor[LBL_GILDE_DIALOG_TEXT_QUIT];
    with (_local2) {
        wordWrap = True;
        width = GILDE_TEXT2_X;
        text = texts[TXT_GILDE_QUIT];
    };
    _local2 = actor[LBL_GILDE_DIALOG_TEXT_MASTER];
    with (_local2) {
        wordWrap = True;
        width = GILDE_TEXT2_X;
        text = texts[TXT_GILDE_MASTER];
    };
    _local2 = actor[LBL_GILDE_DIALOG_TEXT_INVITE];
    with (_local2) {
        wordWrap = True;
        width = GILDE_TEXT2_X;
        text = texts[TXT_GILDE_INVITE];
    };
    _local2 = actor[LBL_GILDE_DIALOG_TEXT_REVOLT];
    with (_local2) {
        wordWrap = True;
        width = GILDE_TEXT2_X;
        text = texts[TXT_REVOLT_WARNING];
    };
    define_from_class(INP_GILDE_DIALOG_INVITE, text_input1, 0,
                    (IF_WIN_Y + GILDE_INP_Y), 2, "name");
    _local2 = actor[INP_GILDE_DIALOG_INVITE];
    with (_local2) {
        getChildAt(1).text = "";
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) - int((width / 2)));
    };
    define_btn(GILDE_DIALOG_CANCEL, texts[TXT_ABBRECHEN], GildeBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    define_btn(GILDE_DIALOG_OK_KICK, texts[TXT_OK], GildeBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    define_btn(GILDE_DIALOG_OK_MASTER, texts[TXT_OK], GildeBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    define_btn(GILDE_DIALOG_OK_INVITE, texts[TXT_OK], GildeBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    define_btn(GILDE_DIALOG_OK_REVOLT, texts[TXT_OK], GildeBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    define_btn(GILDE_DIALOG_OK_RAID, texts[TXT_OK], GildeBtnHandler,
               btn_classBasic, 0, (IF_WIN_Y + GILDE_OK_Y));
    _local2 = actor[GILDE_DIALOG_CANCEL];
    with (_local2) {
        x = ((IF_WIN_X + IF_WIN_WELCOME_X) + 10);
    };
    _local2 = actor[GILDE_DIALOG_OK_KICK];
    with (_local2) {
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int(width)) - 10);
    };
    _local2 = actor[GILDE_DIALOG_OK_MASTER];
    with (_local2) {
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int(width)) - 10);
    };
    _local2 = actor[GILDE_DIALOG_OK_INVITE];
    with (_local2) {
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int(width)) - 10);
    };
    _local2 = actor[GILDE_DIALOG_OK_REVOLT];
    with (_local2) {
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int(width)) - 10);
    };
    _local2 = actor[GILDE_DIALOG_OK_RAID];
    with (_local2) {
        x = (((IF_WIN_X + IF_WIN_WELCOME_X) - int(width)) - 10);
    };
    define_bunch(GILDE_DIALOG_KICK, CA_GILDE_DIALOG_BLOCK, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_GILDE_DIALOG_TEXT_KICK,
                 GILDE_DIALOG_OK_KICK, GILDE_DIALOG_CANCEL);
    define_bunch(GILDE_DIALOG_MASTER, CA_GILDE_DIALOG_BLOCK, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_GILDE_DIALOG_TEXT_MASTER,
                 GILDE_DIALOG_OK_MASTER, GILDE_DIALOG_CANCEL);
    define_bunch(GILDE_DIALOG_INVITE, CA_GILDE_DIALOG_BLOCK, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_GILDE_DIALOG_TEXT_INVITE,
                 INP_GILDE_DIALOG_INVITE, GILDE_DIALOG_OK_INVITE,
                 GILDE_DIALOG_CANCEL);
    define_bunch(GILDE_DIALOG_REVOLT, CA_GILDE_DIALOG_BLOCK, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_GILDE_DIALOG_TEXT_REVOLT,
                 GILDE_DIALOG_OK_REVOLT, GILDE_DIALOG_CANCEL);
    define_bunch(GILDE_DIALOG_RAID, CA_GILDE_DIALOG_BLOCK, IF_WINDOW,
                 LBL_WINDOW_TITLE, LBL_GILDE_DIALOG_TEXT_RAID, G
                 ILDE_DIALOG_OK_RAID, GILDE_DIALOG_CANCEL);
    actor[GILDE_DIALOG_CANCEL].add_event_listener(MouseEvent.CLICK,
                                                  PlayerGuildInviteCancel);
    actor[GILDE_DIALOG_OK_INVITE].add_event_listener(MouseEvent.CLICK,
                                                     PlayerGuildInviteOK);
    define_img(HUTMANN_BG,
              "res/gfx/scr/taverne/huetchenspieler/huetchenspieler.jpg",
              False, 280, 100);
    define_img(HUTFACE_IDLE,
              "res/gfx/scr/taverne/huetchenspieler/" +
              "huetchenspieler_neutral.jpg", False,
              (280 + HUTMANN_FACE_X), (100 + HUTMANN_FACE_Y));
    define_img(HUTFACE_HOVER,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_keinelust.jpg", False,
              (280 + HUTMANN_FACE_X), (100 + HUTMANN_FACE_Y));
    define_img(HUTFACE_WIN,
              "res/gfx/scr/taverne/huetchenspieler/" +
              "huetchenspieler_gewonnen.jpg", False,
              (280 + HUTMANN_FACE_X), (100 + HUTMANN_FACE_Y));
    define_img(HUTFACE_LOSE1,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_verloren.jpg", False,
              (280 + HUTMANN_FACE_X), (100 + HUTMANN_FACE_Y));
    define_img(HUTFACE_LOSE2,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_verloren2.jpg",
              False, (280 + HUTMANN_FACE_X), (100 + HUTMANN_FACE_Y));
    define_img(HUTFACE_LOSE3,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_verloren3.jpg", False,
              (280 + HUTMANN_FACE_X), (100 + HUTMANN_FACE_Y));
    define_img(HUTBECHER_1_IDLE,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher1_1.jpg", False,
              (280 + HUTMANN_BECHER1_X), (100 + HUTMANN_BECHER1_Y));
    define_img(HUTBECHER_1_HOVER,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher1_2.jpg", False,
              ((280 + HUTMANN_BECHER1_X) + HUTMANN_BECHER1_X2),
              ((100 + HUTMANN_BECHER1_Y) + HUTMANN_BECHER1_Y2));
    define_img(HUTBECHER_1_CLICK,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher1_3.jpg", False,
              ((280 + HUTMANN_BECHER1_X) + HUTMANN_BECHER1_X3),
              ((100 + HUTMANN_BECHER1_Y) + HUTMANN_BECHER1_Y3));
    define_bunch(HUTBECHER_1_HOVER, HUTBECHER_1_HOVER, HUTFACE_HOVER);
    define_click_area(CA_HUTBECHER_1, HUTBECHER_1_HOVER, ChooseCup,
                    (280 + HUTMANN_BECHER1_X), (100 + HUTMANN_BECHER1_Y),
                    HUTMANN_BECHER_X, HUTMANN_BECHER_Y);
    define_img(HUTBECHER_2_IDLE,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher2_1.jpg",
              False, (280 + HUTMANN_BECHER2_X), (100 + HUTMANN_BECHER2_Y));
    define_img(HUTBECHER_2_HOVER,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher2_2.jpg", False,
              ((280 + HUTMANN_BECHER2_X) + HUTMANN_BECHER2_X2),
              ((100 + HUTMANN_BECHER2_Y) + HUTMANN_BECHER2_Y2));
    define_img(HUTBECHER_2_CLICK,
              "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher2_3.jpg", False,
              ((280 + HUTMANN_BECHER2_X) + HUTMANN_BECHER2_X3),
              ((100 + HUTMANN_BECHER2_Y) + HUTMANN_BECHER2_Y3));
    define_bunch(HUTBECHER_2_HOVER, HUTBECHER_2_HOVER, HUTFACE_HOVER);
    define_click_area(CA_HUTBECHER_2, HUTBECHER_2_HOVER, ChooseCup,
                    (280 + HUTMANN_BECHER2_X), (100 + HUTMANN_BECHER2_Y),
                    HUTMANN_BECHER_X, HUTMANN_BECHER_Y);
    define_img(HUTBECHER_3_IDLE, "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher3_1.jpg", False,
              (280 + HUTMANN_BECHER3_X), (100 + HUTMANN_BECHER3_Y));
    define_img(HUTBECHER_3_HOVER, "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher3_2.jpg", False,
              ((280 + HUTMANN_BECHER3_X) + HUTMANN_BECHER3_X2),
              ((100 + HUTMANN_BECHER3_Y) + HUTMANN_BECHER3_Y2));
    define_img(HUTBECHER_3_CLICK, "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_becher3_3.jpg", False,
              ((280 + HUTMANN_BECHER3_X) + HUTMANN_BECHER3_X3),
              ((100 + HUTMANN_BECHER3_Y) + HUTMANN_BECHER3_Y3));
    define_bunch(HUTBECHER_3_HOVER, HUTBECHER_3_HOVER, HUTFACE_HOVER);
    define_click_area(CA_HUTBECHER_3, HUTBECHER_3_HOVER, ChooseCup,
                    (280 + HUTMANN_BECHER3_X), (100 + HUTMANN_BECHER3_Y),
                    HUTMANN_BECHER_X, HUTMANN_BECHER_Y);
    define_bunch(HUTMANN_BECHERCHOOSE, CA_HUTBECHER_1, CA_HUTBECHER_2,
                 CA_HUTBECHER_3, HUTFACE_IDLE);
    define_img(HUTKUGEL, "res/gfx/scr/taverne/huetchenspieler/"
              + "huetchenspieler_ball.png", False, 0, (100 + HUTKUGEL_Y));
    define_lbl(LBL_HUTMANN_TEXT, texts[TXT_HUTMANN_OFFER], 0,
              (100 + HUTMANN_TEXT_Y), FontFormat_Default);
    actor[LBL_HUTMANN_TEXT].x = (SCREEN_TITLE_X -
                                 (actor[LBL_HUTMANN_TEXT].text_width / 2));
    add_filter(LBL_HUTMANN_TEXT, Filter_Shadow);
    define_lbl(LBL_HUTMANN_GOLDBET, "", 0, HUTMANN_GOLD_Y,
              FontFormat_GuildMoney);
    add_filter(LBL_HUTMANN_GOLDBET, Filter_Shadow);
    define_lbl(LBL_HUTMANN_MUSHBET, "", 0,
              (HUTMANN_GOLD_Y + GILDE_MUSH_Y), FontFormat_GuildMoney);
    add_filter(LBL_HUTMANN_MUSHBET, Filter_Shadow);
    DefineCnt(HUTMANN_GOLDBET, 0, HUTMANN_GOLD_Y);
    DefineCnt(HUTMANN_MUSHBET, 0, (HUTMANN_GOLD_Y + GILDE_MUSH_Y));
    define_btn(HUTMANN_GOLDBET, "", HutBtnHandler, btn_classPlus,
               0, HUTMANN_GOLD_Y);
    _local2 = actor[HUTMANN_GOLDBET];
    with (_local2) {
        scaleX = 0.8;
        scaleY = 0.8;
    };
    enable_popup(HUTMANN_GOLDBET, texts[TXT_HUTMANN_GOLDBET]);
    define_img(HUTMANN_MUSHBET_DISABLED,
              "res/gfx/scr/gilde/plus_disabled.png", False, 0,
              (HUTMANN_GOLD_Y + GILDE_MUSH_Y));
    enable_popup(HUTMANN_MUSHBET_DISABLED, texts[TXT_MUSHBET_BOUGHT]);
    define_btn(HUTMANN_MUSHBET, "", HutBtnHandler, btn_classPlus, 0,
               (HUTMANN_GOLD_Y + GILDE_MUSH_Y));
    _local2 = actor[HUTMANN_MUSHBET];
    with (_local2) {
        scaleX = 0.8;
        scaleY = 0.8;
    };
    _local2 = actor[HUTMANN_MUSHBET_DISABLED];
    with (_local2) {
        scaleX = 0.8;
        scaleY = 0.8;
    };
    enable_popup(HUTMANN_MUSHBET, texts[TXT_HUTMANN_MUSHBET]);
    define_lbl(LBL_HUTMANN_GOLDBET2, "1", 0, HUTMANN_GOLD_Y,
              FontFormat_GuildMoney);
    add_filter(LBL_HUTMANN_GOLDBET2, Filter_Shadow);
    enable_popup(LBL_HUTMANN_GOLDBET2, texts[TXT_HUTMANN_GOLDBET]);
    define_lbl(LBL_HUTMANN_MUSHBET2, "1", 0,
              (HUTMANN_GOLD_Y + GILDE_MUSH_Y), FontFormat_GuildMoney);
    add_filter(LBL_HUTMANN_MUSHBET2, Filter_Shadow);
    enable_popup(LBL_HUTMANN_MUSHBET2, texts[TXT_HUTMANN_MUSHBET]);
    DefineCnt(HUTMANN_GOLDBET2, 0, HUTMANN_GOLD_Y);
    DefineCnt(HUTMANN_MUSHBET2, 0, (HUTMANN_GOLD_Y + GILDE_MUSH_Y));
    define_bunch(HUTMANN_PLACEBET, HUTMANN_MUSHBET_DISABLED,
                 HUTMANN_MUSHBET, LBL_HUTMANN_MUSHBET2, HUTMANN_MUSHBET2,
                 HUTMANN_GOLDBET, LBL_HUTMANN_GOLDBET2, HUTMANN_GOLDBET2,
                 HUTFACE_IDLE);
    define_lbl(LBL_HUTMANN_INSTR,
              texts[TXT_HUTMANN_INSTR]
              .split("#").join(((text_dir)=="right") ? "" : chr(13)),
              HUTMANN_INSTR_X, HUTMANN_INSTR_Y, FontFormat_DefaultLeft);
    add_filter(LBL_HUTMANN_INSTR, Filter_Shadow);
    define_bunch(SCREEN_HUTMANN, HUTMANN_BG, IF_OVL, IF_EXIT,
                 HUTFACE_HOVER, HUTFACE_WIN, HUTFACE_LOSE1, HUTFACE_LOSE2,
                 HUTFACE_LOSE3, HUTFACE_IDLE);
    define_btn(HUTMANN_OK, texts[TXT_HUTMANN_START], HutBtnHandler,
               btn_classLOGin, HUTMANN_OK_X, HUTMANN_OK_Y);
    define_btn(HUTMANN_BACK, texts[TXT_HUTMANN_BACK], interface_btn_handler,
               btn_classBack, HUTMANN_BACK_X, HUTMANN_BACK_Y);
    HutBtnRepeatTimer = new Timer(1000);
    DestroyHutBtnTimer = False;
    _local2 = actor[HUTMANN_GOLDBET];
    with (_local2) {
        add_event_listener(MouseEvent.MOUSE_DOWN, HutBtnDownHandler);
        add_event_listener(MouseEvent.MOUSE_UP, HutBtnUpHandler);
        add_event_listener(MouseEvent.MOUSE_OUT, HutBtnUpHandler);
    };
    _local2 = actor[HUTMANN_MUSHBET];
    with (_local2) {
        add_event_listener(MouseEvent.MOUSE_DOWN, HutBtnDownHandler);
        add_event_listener(MouseEvent.MOUSE_UP, HutBtnUpHandler);
        add_event_listener(MouseEvent.MOUSE_OUT, HutBtnUpHandler);
    };
    define_bunch(HUTMANN_WON, HUTFACE_WIN);
    define_bunch(HUTMANN_LOST, HUTFACE_LOSE1);
    add_bunch(SCREEN_HUTMANN, HUTBECHER_1_IDLE);
    add_bunch(SCREEN_HUTMANN, HUTBECHER_2_IDLE);
    add_bunch(SCREEN_HUTMANN, HUTBECHER_3_IDLE);
    add_bunch(SCREEN_HUTMANN, LBL_HUTMANN_TEXT, LBL_HUTMANN_GOLDBET,
              LBL_HUTMANN_MUSHBET, LBL_HUTMANN_GOLDBET2,
              LBL_HUTMANN_MUSHBET2, LBL_HUTMANN_INSTR, HUTMANN_BACK);
    add_bunch(SCREEN_HUTMANN, HUTMANN_GOLDBET, HUTMANN_MUSHBET,
              HUTMANN_GOLDBET2, HUTMANN_MUSHBET2, HUTMANN_GOLDBET,
              HUTMANN_MUSHBET_DISABLED, HUTMANN_MUSHBET);
    HutFaceResetTimer = new Timer(2000, 1);
    HutFaceResetTimer.add_event_listener(TimerEvent.TIMER, HutFaceReset);
    define_img(TAVERNE_BG, "res/gfx/scr/taverne/taverne.jpg",
              False, 280, 100);
    define_img(TAVERNE_BARKEEPER1,
              "res/gfx/scr/taverne/taverne_barkeeper1.jpg", False,
              (280 + TAVERNE_BARKEEPER_X), (100 + TAVERNE_BARKEEPER_Y));
    define_img(TAVERNE_BARKEEPER2,
              "res/gfx/scr/taverne/taverne_barkeeper2.jpg", False,
              (280 + TAVERNE_BARKEEPER_X), (100 + TAVERNE_BARKEEPER_Y));
    define_img(TAVERNE_BARKEEPER_HINT,
              "res/gfx/scr/taverne/exclamation.png",
              False, ((280 + TAVERNE_BARKEEPER_X) + 50),
              ((100 + TAVERNE_BARKEEPER_Y) - 215));
    define_img(TAVERNE_HUTMANN_BLINZELN,
              "res/gfx/scr/taverne/huetchenspieler_blink.jpg",
              False, (280 + TAVERNE_HUTAUGEN_X),
              (100 + TAVERNE_HUTAUGEN_Y));
    define_img(TAVERNE_HUTMANN_OVL,
              "res/gfx/scr/taverne/huetchenspieler_mouseover.jpg",
              False, (280 + TAVERNE_HUTAUGEN_X),
              (100 + TAVERNE_HUTAUGEN_Y));
    define_click_area(CA_TAVERNE_HUTMANN,
                    TAVERNE_HUTMANN_OVL, ShowHutmann,
                    (TAVERNE_HUT_X + 280), (TAVERNE_HUT_Y + 100),
                    TAVERNE_HUT_X, TAVERNE_HUT_Y);
    define_click_area(CA_TAVERNE_QUESTOFFER, TAVERNE_QUESTOVL,
                    ShowQuestOffer, (TAVERNE_QUEST_X + 280),
                    (TAVERNE_QUEST_Y + 100), TAVERNE_QUEST_X,
                    TAVERNE_QUEST_Y);
    define_click_area(CA_TAVERNE_TOILETTE, C_EMPTY, RequestToilet,
                    (280 + 470), (100 + 195), 36, 30);
    define_img(TAVERNE_KERZEN,
              "res/gfx/scr/taverne/taverne_kerzen.jpg", False,
              (280 + TAVERNE_KERZEN_X), (100 + TAVERNE_KERZEN_Y));
    define_img(TAVERNE_QUESTOVL1,
              "res/gfx/scr/taverne/taverne_orc_mouseover.jpg", False,
              ((TAVERNE_QUEST_X + 280) + TAVERNE_QUESTOVL1_X),
              ((TAVERNE_QUEST_Y + 100) + TAVERNE_QUESTOVL1_Y));
    define_img(TAVERNE_QUESTOVL2,
              "res/gfx/scr/taverne/taverne_bauer_mouseover.jpg", False,
              ((TAVERNE_QUEST_X + 280) + TAVERNE_QUESTOVL2_X),
              ((TAVERNE_QUEST_Y + 100) + TAVERNE_QUESTOVL2_Y));
    define_img(TAVERNE_QUESTOVL3,
              "res/gfx/scr/taverne/taverne_zauberin_mouseover.jpg",
              False, ((TAVERNE_QUEST_X + 280) + TAVERNE_QUESTOVL3_X),
              ((TAVERNE_QUEST_Y + 100) + TAVERNE_QUESTOVL3_Y));
    define_img(TAVERNE_QUESTOVL4,
              "res/gfx/scr/taverne/taverne_questgeber_mouseover.jpg",
              False, ((TAVERNE_QUEST_X + 280) + TAVERNE_QUESTOVL4_X),
              ((TAVERNE_QUEST_Y + 100) + TAVERNE_QUESTOVL4_Y));
    define_img(TAVERNE_QUESTOVL5,
              "res/gfx/scr/taverne/taverne_tourist_mouseover.jpg",
              False, ((TAVERNE_QUEST_X + 280) + TAVERNE_QUESTOVL5_X),
              ((TAVERNE_QUEST_Y + 100) + TAVERNE_QUESTOVL5_Y));
    define_img(TAVERNE_BAROVL,
              "res/gfx/scr/taverne/barkeeper_mouseover.jpg", False,
              TAVERNE_BAROVL_X, TAVERNE_BAROVL_Y);
    define_click_area(CA_TAVERNE_BAR, TAVERNE_BAROVL, ShowBeerOffer,
                    TAVERNE_BAR_X, TAVERNE_BAR_Y, TAVERNE_BAR_X,
                    TAVERNE_BAR_Y);
    define_img(TIMEBAR_BG, "res/gfx/if/adventurebar.png", False,
              TIMEBAR_X, TIMEBAR_Y);
    define_img(TIMEBAR_FILL, "res/gfx/scr/taverne/ausdauer.jpg", False,
              (TIMEBAR_X + 110), (TIMEBAR_Y + 44));
    DefineCnt(TIMEBAR_FILL, 0, (TIMEBAR_Y + 44));
    define_lbl(LBL_TIMEBAR_TEXT, "", 0, TIMEBAR_LABEL_Y, FontFormat_TimeBar)
    add_filter(LBL_TIMEBAR_TEXT, Filter_Shadow);
    enable_popup(TIMEBAR_BG, texts[TXT_TIMEBAR]);
    enable_popup(TIMEBAR_FILL, texts[TXT_TIMEBAR]);
    enable_popup(TIMEBAR_FILL, texts[TXT_TIMEBAR]);
    enable_popup(LBL_TIMEBAR_TEXT, texts[TXT_TIMEBAR]);
    define_bunch(SCREEN_TAVERNE, TAVERNE_BG, IF_OVL, TAVERNE_BARKEEPER1,
                 TAVERNE_BARKEEPER2, TAVERNE_HUTMANN_BLINZELN,
                 CA_TAVERNE_BAR);
    define_bunch(TAVERNE_CAS, CA_TAVERNE_QUESTOFFER, CA_TAVERNE_HUTMANN,
                 CA_TAVERNE_TOILETTE, CA_TAVERNE_BAR);
    define_img(BEERFEST,
              "res/gfx/scr/taverne/beerfest.png", False, 280, 100);
    actor[BEERFEST].mouse_enabled = False;
    define_bunch(BEERFEST, BEERFEST, TIMEBAR_BG, TIMEBAR_FILL,
                 TIMEBAR_FILL, LBL_TIMEBAR_TEXT, IF_OVL, IF_EXIT);
    i = 0;
    while (i < 4) {
        define_img((TV + i), (("res/gfx/scr/taverne/tv_animation/tv" +
                  str((i + 1))) + ".png"), False, (280 + 20), (100 + 20));
        hide((TV + i));
        add_bunch(SCREEN_TAVERNE, (TV + i));
        i = (i + 1);
    };
    define_click_area(CA_TV, C_EMPTY, request_tv, (280 + 20), (100 + 20),
                    280, 160);
    hide(CA_TV);
    add_bunch(SCREEN_TAVERNE, CA_TV);
    cursedDescr = "Fliegende";
    if (int((random.random() * 100)) == 0){
        cursedDescr = "Verfluchte";
    };
    enable_popup(CA_TV, POPUP_BEGIN_LINE,
                 texts[TXT_TV_HINT].split("|")[0].split("Fliegende")
                 .join(cursedDescr), POPUP_END_LINE, POPUP_BEGIN_LINE,
                 FontFormat_EpicItemQuote, texts[TXT_TV_HINT]
                 .split("|")[1].split("#").join(chr(13)), POPUP_END_LINE);
    i = 0;
    while (i < 4) {
        define_img((TAVERN_ADVENT + i),
                  (("res/gfx/scr/taverne/advent_wreath_"
                   + str((i + 1))) + ".jpg"), False, (280 + 337), 100);
        actor[(TAVERN_ADVENT + i)].mouse_enabled = False;
        i = (i + 1);
    };
    i = 0;
    while (i < 5) {
        define_img((SPECIAL_ACTION + i),
                  (("res/gfx/scr/taverne/event_ovl_" + str((i + 1)))
                   + ".png"), False, 280, 100);
        define_bunch((SPECIAL_ACTION + i), (SPECIAL_ACTION + i),
                     TIMEBAR_BG, TIMEBAR_FILL, TIMEBAR_FILL,
                     LBL_TIMEBAR_TEXT, IF_OVL, IF_EXIT);
        i = (i + 1);
    };
    i = 0;
    while (i < 5) {
        define_img((TAVERNE_QUEST1 + i),
                  (("res/gfx/scr/taverne/taverne_quest"
                   + str((i + 1))) + ".jpg"), False,
                    (280 + TAVERNE_QUEST_X), (100 + TAVERNE_QUEST_Y));
        add_bunch(SCREEN_TAVERNE, (TAVERNE_QUEST1 + i));
        i = (i + 1);
    };
    add_bunch(SCREEN_TAVERNE,
              TAVERNE_KERZEN, IF_EXIT, TIMEBAR_BG, TIMEBAR_FILL,
              TIMEBAR_FILL, LBL_TIMEBAR_TEXT);
    add_bunch(SCREEN_TAVERNE, CA_TAVERNE_QUESTOFFER, CA_TAVERNE_HUTMANN,
              CA_TAVERNE_TOILETTE);
    define_from_class(SHP_QO_BLACK_SQUARE, black_square_neutral,
                    QO_BLACK_SQUARE_X, QO_BLACK_SQUARE_Y);
    _local2 = actor[SHP_QO_BLACK_SQUARE];
    with (_local2) {
        width = QO_BLACK_SQUARE_X;
        height = QO_BLACK_SQUARE_Y;
        alpha = 0.6;
    };
    define_lbl(LBL_QO_CHOOSE, texts[TXT_QO_CHOOSE], (QO_BLACK_SQUARE_X
              + QO_CHOOSE_X), (QO_BLACK_SQUARE_Y + QO_CHOOSE_Y),
                FontFormat_Default);
    i = 0;
    while (i < 3) {
        define_lbl((LBL_QO_CHOICE1 + i), "TEST", 0, 0, FontFormat_Default);
        define_lbl((LBL_QO_CHOICE1_HL + i), "TEST", 0, 0,
                  FontFormat_Highlight);
        MakePersistent((LBL_QO_CHOICE1 + i), (LBL_QO_CHOICE1_HL + i));
        DefineCnt((QO_CHOICE1 + i), (QO_BLACK_SQUARE_X + QO_CHOOSE_X),
                  ((QO_BLACK_SQUARE_Y + QO_CHOOSE_Y) +
                   ((i + 1) * QO_CHOICES_Y)));
        _local2 = actor[(QO_CHOICE1 + i)];
        with (_local2) {
            addChild(actor[(LBL_QO_CHOICE1 + i)]);
            addChild(actor[(LBL_QO_CHOICE1_HL + i)]);
            add_event_listener(MouseEvent.CLICK, ChooseQuest);
            mouseChildren = False;
            useHandCursor = True;
            buttonMode = True;
        };
        i = (i + 1);
    };
    define_bunch(QUESTOFFER);
    define_lbl(LBL_QO_QUESTNAME, "QuestName", 0, (QO_BLACK_SQUARE_Y +
              QO_QUESTNAME_Y), FontFormat_Heading);
    define_lbl(LBL_QO_QUESTTEXT, "quest_text", (QO_BLACK_SQUARE_X
              + QO_QUESTTEXT_X), (QO_BLACK_SQUARE_Y + QO_QUESTTEXT_Y),
                FontFormat_DefaultLeft);
    actor[LBL_QO_QUESTTEXT].width = LBL_QO_TEXT_X;
    actor[LBL_QO_QUESTTEXT].wordWrap = True;
    actor[LBL_QO_QUESTTEXT].default_text_format.align = "right";
    define_lbl(LBL_QO_REWARD, texts[TXT_QO_REWARD],
              (QO_BLACK_SQUARE_X + QO_QUESTTEXT_X),
              (QO_BLACK_SQUARE_Y + QO_REWARD_Y), FontFormat_Default);
    DefineCnt(QO_REWARDGOLD, 0,
              ((QO_BLACK_SQUARE_Y + QO_REWARD_Y) + QO_REWARDS_Y));
    DefineCnt(QO_REWARDSILVER, 0,
              ((QO_BLACK_SQUARE_Y + QO_REWARD_Y) + QO_REWARDS_Y));
    define_lbl(LBL_QO_REWARDGOLD, "", 0,
              ((QO_BLACK_SQUARE_Y + QO_REWARD_Y) + QO_REWARDS_Y),
              FontFormat_Default);
    define_lbl(LBL_QO_REWARDSILVER, "", 0,
              ((QO_BLACK_SQUARE_Y + QO_REWARD_Y) + QO_REWARDS_Y),
              FontFormat_Default);
    define_lbl(LBL_QO_REWARDEXP, "",
              (QO_BLACK_SQUARE_X + QO_QUESTTEXT_X),
              ((QO_BLACK_SQUARE_Y + QO_REWARD_Y) + (QO_REWARDS_Y * 2)),
              FontFormat_Default);
    define_lbl(LBL_QO_TIME, "",
              (QO_BLACK_SQUARE_X + QO_QUESTTEXT_X),
              ((QO_BLACK_SQUARE_Y + QO_REWARD_Y) + (QO_REWARDS_Y * 3)),
              FontFormat_Default);
    define_btn(QO_START, texts[TXT_QO_START], RequestQuest, btn_classBasic,
               (QO_BLACK_SQUARE_X + QO_START_X),
               (QO_BLACK_SQUARE_Y + QO_RETURN_Y));
    define_btn(BO_BUY, texts[TXT_BO_BUY], BuyBeer, btn_classBasic,
               (QO_BLACK_SQUARE_X + QO_START_X),
               (QO_BLACK_SQUARE_Y + QO_RETURN_Y));
    define_btn(QO_RETURN, texts[TXT_QO_RETURN], ReturnQuest,
               btn_classBasic, (QO_BLACK_SQUARE_X + QO_START_X),
               (QO_BLACK_SQUARE_Y + QO_START_Y));
    define_lbl(LBL_QO_QUESTSTODAY, "", 0,
              (QO_BLACK_SQUARE_Y + QO_QUESTSTODAY_Y),
              FontFormat_Default);
    DefineCnt(QUEST_SLOT, ((QO_BLACK_SQUARE_X + QO_SLOT_X) + 20),
              (QO_BLACK_SQUARE_Y + QO_SLOT_Y));
    add_bunch(QUESTOFFER, SHP_QO_BLACK_SQUARE, LBL_QO_CHOOSE, QO_CHOICE1,
              QO_CHOICE2, QO_CHOICE3, LBL_QO_QUESTNAME, LBL_QO_QUESTTEXT);
    add_bunch(QUESTOFFER, LBL_QO_REWARD, LBL_QO_REWARDGOLD,
              LBL_QO_REWARDSILVER, QO_REWARDGOLD, QO_REWARDSILVER,
              LBL_QO_REWARDEXP, LBL_QO_TIME, QUEST_SLOT, QO_START,
              QO_RETURN, LBL_QO_QUESTSTODAY);
    i = 0;
    while (i < 5) {
        define_img((QO_PORTRAIT1 + i),
                  (("res/gfx/scr/taverne/portrait_questgeber_"
                   + str((i + 1))) + ".png"), False,
                    (QO_BLACK_SQUARE_X + QO_PORTRAIT_X),
                    (QO_BLACK_SQUARE_Y + QO_PORTRAIT_Y));
        add_bunch(QUESTOFFER, (QO_PORTRAIT1 + i));
        i = (i + 1);
    };
    define_img(BO_PORTRAIT_OK,
              "res/gfx/scr/taverne/portrait_barkeeper_2.png",
              False, (QO_BLACK_SQUARE_X + QO_PORTRAIT_X),
              (QO_BLACK_SQUARE_Y + QO_PORTRAIT_Y));
    define_img(BO_PORTRAIT_NO,
              "res/gfx/scr/taverne/portrait_barkeeper_3.png", False,
              (QO_BLACK_SQUARE_X + QO_PORTRAIT_X),
              (QO_BLACK_SQUARE_Y + QO_PORTRAIT_Y));
    define_img(BO_PORTRAIT_TH,
              "res/gfx/scr/taverne/portrait_barkeeper_1.png", False,
              (QO_BLACK_SQUARE_X + QO_PORTRAIT_X),
              (QO_BLACK_SQUARE_Y + QO_PORTRAIT_Y));
    define_bunch(BEEROFFER, SHP_QO_BLACK_SQUARE, LBL_QO_QUESTNAME,
                 LBL_QO_QUESTTEXT, LBL_QO_TIME, LBL_QO_REWARDEXP, BO_BUY,
                 BO_BUY, QO_RETURN, BO_PORTRAIT_OK, BO_PORTRAIT_NO,
                 BO_PORTRAIT_TH);
    TimeBarAniTimer = new Timer(20);
    TimeBarAniTimer.add_event_listener(TimerEvent.TIMER, TimeBarAniEvent);
    TimeBarAniTimer.start();
    timeBarAni = 0;
    define_bunch(SCREEN_TOILET);
    define_snd(SND_TOILET_FLUSHTRY, "res/sfx/toilet/flush_try.mp3", False);
    define_snd(SND_TOILET_FLUSH, "res/sfx/toilet/flush.mp3", False);
    define_snd(SND_TOILET_DROP, "res/sfx/toilet/drop.mp3", False);
    add_bunch(SCREEN_TOILET, SND_TOILET_FLUSHTRY, SND_TOILET_FLUSH,
              SND_TOILET_DROP);
    define_img(TOILET, "res/gfx/scr/taverne/toilet/toilet_bg.png", False,
              SCR_SHOP_BG_X, 100);
    define_img((TOILET + 1), "res/gfx/scr/taverne/toilet/tank_content.png",
              False, (SCR_SHOP_BG_X + 170), 190);
    define_img((TOILET + 2), "res/gfx/scr/taverne/toilet/toilet_ovl.png",
              False, SCR_SHOP_BG_X, 100);
    i = 0;
    while (i < 3) {
        add_bunch(SCREEN_TOILET, (TOILET + i));
        i = (i + 1);
    };
    define_img(TOILET_IDLE, "res/gfx/scr/taverne/toilet/bowl_idle.png",
              False, SCR_SHOP_BG_X, 100);
    define_img(TOILET_DROP, "res/gfx/scr/taverne/toilet/bowl_dropitem.png",
              False, SCR_SHOP_BG_X, 100);
    add_bunch(SCREEN_TOILET, TOILET_IDLE, TOILET_DROP);
    define_bunch(TOILET_OVERLAYS, TOILET_IDLE, TOILET_DROP);
    define_lbl(LBL_TOILET_AURA, "0", (SCR_SHOP_BG_X + 240), 430,
              FontFormat_ToiletAura);
    add_bunch(SCREEN_TOILET, LBL_TOILET_AURA);
    i = 0;
    while (i < 7) {
        define_img((TOILET_FLUSH + i),
                  ("res/gfx/scr/taverne/toilet/bowl_flush_" + str((i + 1)))
                  + ".png"), False, SCR_SHOP_BG_X, 100);
        hide((TOILET_FLUSH + i));
        add_bunch(SCREEN_TOILET, (TOILET_FLUSH + i));
        add_bunch(TOILET_OVERLAYS, (TOILET_FLUSH + i));
        i = (i + 1);
    };
    i = 0;
    while (i < 3) {
        define_img((TOILET_CHAIN + i),
                  (("res/gfx/scr/taverne/toilet/chain_"
                   + str((i + 1))) + ".png"), False, SCR_SHOP_BG_X, 100);
        hide((TOILET_CHAIN + i));
        add_bunch(SCREEN_TOILET, (TOILET_CHAIN + i));
        add_bunch(TOILET_OVERLAYS, (TOILET_CHAIN + i));
        i = (i + 1);
    };
    i = 0;
    while (i < 15) {
        add_bunch(SCREEN_TOILET, (CHAR_SLOT_1 + i));
        i = (i + 1);
    };
    define_click_area(CA_TOILET_TANK, C_EMPTY, None, (SCR_SHOP_BG_X + 170),
                    190, 156, 120);
    define_click_area(CA_TOILET_CHAIN, C_EMPTY, ToiletHandler,
                    (SCR_SHOP_BG_X + 320), 210, 36, 206);
    define_click_area(CA_TOILET_BOWL, C_EMPTY, None, (SCR_SHOP_BG_X + 120),
                    540, 260, 120);
    define_click_area(CA_TOILET_LID, C_EMPTY, None, (SCR_SHOP_BG_X + 180),
                    380, 135, 155);
    enable_popup(CA_TOILET_CHAIN, texts[(TXT_TOILET_HINT + 1)]);
    enable_popup(CA_TOILET_BOWL, texts[(TXT_TOILET_HINT + 2)]);
    enable_popup(CA_TOILET_LID, texts[(TXT_TOILET_HINT + 3)]);
    actor[CA_TOILET_TANK].useHandCursor = False;
    actor[CA_TOILET_BOWL].useHandCursor = False;
    add_bunch(SCREEN_TOILET, IF_OVL, CA_TOILET_LID, CA_TOILET_TANK,
              CA_TOILET_CHAIN, CA_TOILET_BOWL, IF_EXIT);
    toiletChainTimer = new Timer(50);
    toiletChainFrame = 0;
    toiletChainTimer.add_event_listener(TimerEvent.TIMER, toiletChainAni);
    i = 0;
    while (i < 6) {
        define_img((FIGHT_ONO + i), (("res/gfx/scr/fight/smash"
                  + str((i + 1))) + ".png"), False, 0, 0);
        i = (i + 1);
    };
    define_img(FIGHT_ARROW_SMASH, "res/gfx/scr/fight/arrowsmash.png",
              False, 0, 0);
    DefineCnt(FIGHT_ONO, 0, 0);
    define_lbl(LBL_FIGHT_PLAYERGUILD, "", 0, (OPPY + 5),
              FontFormat_ScreenTitle);
    define_lbl(LBL_FIGHT_OPPGUILD, "", 0, (OPPY + 5),
              FontFormat_ScreenTitle);
    add_filter(LBL_FIGHT_PLAYERGUILD, Filter_Shadow);
    add_filter(LBL_FIGHT_OPPGUILD, Filter_Shadow);
    define_bunch(OPPIMG);
    define_bunch(OPPIMG2);
    i = 0;
    while (i < 10) {
        define_img((OPPBACKGROUND + i), "", False, OPPX, OPPY);
        add_bunch(OPPIMG, (OPPBACKGROUND + i));
        define_img((OPPBACKGROUND2 + i), "", False, OPPX, OPPY);
        add_bunch(OPPIMG2, (OPPBACKGROUND2 + i));
        i = (i + 1);
    };
    k = 0;
    k = 0;
    while (k < 500) {
        i = k;
        if (param_censored){
            if ((((i >= 66)) and ((i <= 68)))){
                i = 69;
            };
            if (i == 73){
                i = 128;
            };
            if ((((i >= 117)) and ((i <= 118)))){
                i = 69;
            };
        };
        if (i >= 399){
            monsterChecksum = MD5((str(i) + "ScriptKiddieLovesToPeek"));
            define_img((OPPMONSTER + k),
                      (("res/gfx/scr/fight/monster/monster"
                       + monsterChecksum) + ".jpg"), False, OPPX, OPPY);
        } else {
            define_img((OPPMONSTER + k),
                      (("res/gfx/scr/fight/monster/monster"
                       + str((i + 1))) + ".jpg"), False, OPPX, OPPY);
        };
        k = (k + 1);
    };
    i = 0;
    while (i < 3) {
        ii = -7;
        while (ii < 100) {
            iii = 0;
            while (iii < 4) {
                define_snd(get_weapon_sound((i + 1), (ii + 1), iii),
                           get_weapon_sound_file((i + 1), (ii + 1), iii));
                iii = (iii + 1);
            };
            ii = (ii + 1);
        };
        i = (i + 1);
    };
    define_lbl(LBL_NAMERANK_CHAR, "", (FIGHT_CHARX + 310), OPPY,
              FontFormat_Default);
    add_filter(LBL_NAMERANK_CHAR, Filter_Shadow);
    define_lbl(LBL_NAMERANK_OPP, "", 0, OPPY, FontFormat_Default);
    add_filter(LBL_NAMERANK_OPP, Filter_Shadow);
    define_img(LIFEBAR_CHAR, "res/gfx/scr/fight/lifebar.png", False,
              FIGHT_CHARX, ((OPPY + 300) + LIFEBAR_Y));
    define_img(LIFEBAR_FILL_CHAR, "res/gfx/scr/fight/lifebar_red.png",
              False, (FIGHT_CHARX + 10), (((OPPY + 300) + 8) + LIFEBAR_Y));
    DefineCnt(LIFEBAR_OPP, OPPX, ((OPPY + 300) + LIFEBAR_Y));
    DefineCnt(LIFEBAR_FILL_OPP, (OPPX + 10), (((OPPY + 300) + 8)
              + LIFEBAR_Y));
    define_lbl(LBL_LIFEBAR_CHAR, "", 0, (((OPPY + 300) + 13) + LIFEBAR_Y),
              FontFormat_LifeBar);
    define_lbl(LBL_LIFEBAR_OPP, "", 0, (((OPPY + 300) + 13) + LIFEBAR_Y),
              FontFormat_LifeBar);
    define_img(FIGHT_CHAR_BORDER, "res/gfx/scr/fight/character_border.png",
              False, (FIGHT_CHARX - 10), (OPPY - 10));
    DefineCnt(FIGHT_OPP_BORDER, (OPPX - 10), (OPPY - 10));
    DefineCnt(BULLET_CHAR, 0, 0);
    SetCnt(BULLET_CHAR, ITM_OFFS);
    DefineCnt(BULLET_OPP, 0, 0);
    SetCnt(BULLET_OPP, ITM_OFFS);
    DefineCnt(WEAPON_CHAR, 0, 0);
    SetCnt(WEAPON_CHAR, ITM_OFFS);
    DefineCnt(SHIELD_CHAR, 0, 0);
    SetCnt(SHIELD_CHAR, ITM_OFFS);
    DefineCnt(WEAPON_OPP, 0, 0);
    SetCnt(WEAPON_OPP, ITM_OFFS);
    DefineCnt(SHIELD_OPP, 0, 0);
    SetCnt(SHIELD_OPP, ITM_OFFS);
    define_img(WEAPON_FIST, "res/gfx/itm/kampf_faust.png", False, 0, 0);
    define_img(WEAPON_STONEFIST, "res/gfx/itm/kampf_steinfaust.png",
              False, 0, 0);
    define_img(WEAPON_BONE, "res/gfx/itm/kampf_knochen.png", False, 0, 0);
    define_img(WEAPON_STICK, "res/gfx/itm/kampf_stock.png", False, 0, 0);
    define_img(WEAPON_CLAW, "res/gfx/itm/kampf_kralle1.png", False, 0, 0);
    define_img(WEAPON_CLAW2, "res/gfx/itm/kampf_kralle2.png", False, 0, 0);
    define_img(WEAPON_CLAW3, "res/gfx/itm/kampf_kralle3.png", False, 0, 0);
    define_img(WEAPON_CLAW4, "res/gfx/itm/kampf_kralle4.png", False, 0, 0);
    define_img(WEAPON_SWOOSH, "res/gfx/itm/kampf_swoosh1.png", False, 0, 0);
    define_img(WEAPON_SWOOSH2, "res/gfx/itm/kampf_swoosh2.png", False, 0, 0)
    define_img(WEAPON_SWOOSH3, "res/gfx/itm/kampf_swoosh3.png", False, 0, 0)
    define_img(WEAPON_SPLAT, "res/gfx/itm/kampf_splat1.png", False, 0, 0);
    define_img(WEAPON_SPLAT2, "res/gfx/itm/kampf_splat2.png", False, 0, 0);
    define_img(WEAPON_SPLAT3, "res/gfx/itm/kampf_splat3.png", False, 0, 0);
    define_img(WEAPON_FIRE, "res/gfx/itm/kampf_feuer1.png", False, 0, 0);
    define_img(WEAPON_FIRE2, "res/gfx/itm/kampf_feuer2.png", False, 0, 0);
    define_img(WEAPON_FIRE3, "res/gfx/itm/kampf_feuer3.png", False, 0, 0);
    define_lbl(LBL_DAMAGE_INDICATOR, "", 0, 0, FontFormat_Damage);
    add_filter(LBL_DAMAGE_INDICATOR, Filter_Shadow);
    define_btn(FIGHT_SKIP, texts[TXT_SKIP_FIGHT], SkipFight,
               btn_classBasic, 0, 0);
    define_btn(FIGHT_OK, texts[TXT_OK], interface_btn_handler,
               btn_classBasic, 0, 0);
    _local2 = actor[FIGHT_OK];
    with (_local2) {
        y = FIGHT_Y;
        x = (SCREEN_TITLE_X - int((width / 2)));
    };
    _local2 = actor[FIGHT_SKIP];
    with (_local2) {
        y = FIGHT_Y;
        x = (SCREEN_TITLE_X - int((width / 2)));
    };
    define_btn(BATTLE_SKIP, texts[TXT_SKIP_FIGHT], SkipFight,
               btn_classBasic, 0, 0);
    define_btn(BATTLE_SKIPONE, texts[TXT_GUILD_BATTLE_SKIP],
               SkipFight, btn_classBasic, 0, 0);
    _local2 = actor[BATTLE_SKIPONE];
    with (_local2) {
        y = FIGHT_Y;
        x = ((SCREEN_TITLE_X - width) - 5);
    };
    _local2 = actor[BATTLE_SKIP];
    with (_local2) {
        y = FIGHT_Y;
        x = (SCREEN_TITLE_X + 5);
    };
    define_lbl(LBL_FIGHT_SUMMARY, "", 0, FIGHT_SUMMARY_Y,
              FontFormat_Default);
    add_filter(LBL_FIGHT_SUMMARY, Filter_Shadow);
    define_img(GUILD_BATTLE_BG, "res/gfx/scr/fight/schlachtfeld.jpg",
              False, 280, 100);
    define_img(GUILD_RAID_BG, "res/gfx/scr/fight/raid.jpg", False,
              280, 100);
    define_bunch(SCREEN_FIGHT, BLACK_SQUARE, LBL_NAMERANK_CHAR,
                 LIFEBAR_CHAR, LIFEBAR_FILL_CHAR, LBL_LIFEBAR_CHAR,
                 LBL_NAMERANK_OPP, IF_EXIT);
    add_bunch(SCREEN_FIGHT, LIFEBAR_OPP, LIFEBAR_FILL_OPP, LBL_LIFEBAR_OPP,
              IF_OVL, FIGHT_SKIP, FIGHT_CHAR_BORDER, FIGHT_OPP_BORDER);
    define_img(FIGHT_BOX1, "res/gfx/scr/fight/box1.png", False,
              (FIGHT_CHAR_PROP_COLUMN_1_X + FIGHT_BOX1_X),
              (FIGHT_CHAR_PROP_Y + FIGHT_BOX1_Y));
    define_img(FIGHT_BOX2, "res/gfx/scr/fight/box2.png", False,
              (SCREEN_TITLE_X - 254), (FIGHT_CHAR_PROP_Y + FIGHT_BOX1_Y));
    DefineCnt(FIGHT_BOX3, (FIGHT_CHAR_PROP_COLUMN_3_X + FIGHT_BOX3_X),
              (FIGHT_CHAR_PROP_Y + FIGHT_BOX1_Y));
    DefineCnt(FIGHT_SLOT, (SCREEN_TITLE_X - 45), FIGHT_SLOT_Y);
    DefineCnt(FIGHT_REWARDGOLD, FIGHT_REWARDGOLD_X, FIGHT_REWARDGOLD_Y);
    DefineCnt(FIGHT_REWARDSILVER, FIGHT_REWARDGOLD_X, FIGHT_REWARDGOLD_Y);
    DefineCnt(FIGHT_REWARDMUSH, FIGHT_REWARDGOLD_X, FIGHT_REWARDMUSH_Y);
    define_lbl(LBL_FIGHT_REWARDGOLD, "", 0, FIGHT_REWARDGOLD_Y,
              FontFormat_Default);
    add_filter(LBL_FIGHT_REWARDGOLD, Filter_Shadow);
    define_lbl(LBL_FIGHT_REWARDSILVER, "", 0, FIGHT_REWARDGOLD_Y,
              FontFormat_Default);
    add_filter(LBL_FIGHT_REWARDSILVER, Filter_Shadow);
    define_lbl(LBL_FIGHT_REWARDMUSH, "", 0, FIGHT_REWARDMUSH_Y,
              FontFormat_Default);
    add_filter(LBL_FIGHT_REWARDMUSH, Filter_Shadow);
    define_lbl(LBL_FIGHT_REWARDEXP, "", FIGHT_REWARDEXP_X,
              FIGHT_REWARDGOLD_Y, FontFormat_Default);
    add_filter(LBL_FIGHT_REWARDEXP, Filter_Shadow);
    add_bunch(SCREEN_FIGHT, FIGHT_BOX1, FIGHT_BOX2, FIGHT_BOX3);
    define_bunch(FIGHT_REWARDS, FIGHT_SLOT, FIGHT_REWARDGOLD,
                 LBL_FIGHT_REWARDGOLD, FIGHT_REWARDSILVER,
                 LBL_FIGHT_REWARDSILVER, FIGHT_REWARDMUSH,
                 LBL_FIGHT_REWARDMUSH, LBL_FIGHT_REWARDEXP);
    define_lbl(LBL_HERO_OF_THE_DAY_TITLE,
              ((texts[TXT_HERO_OF_THE_DAY_TITLE])
               ? texts[TXT_HERO_OF_THE_DAY_TITLE] : ""), 0, 120,
                FontFormat_Heading);
    actor[LBL_HERO_OF_THE_DAY_TITLE].x = (SCREEN_TITLE_X
                      - (actor[LBL_HERO_OF_THE_DAY_TITLE].width / 2));
    define_lbl(LBL_HERO_OF_THE_DAY, "", 0, 160, FontFormat_Default);
    actor[LBL_HERO_OF_THE_DAY].default_text_format.align = "center";
    add_filter(LBL_HERO_OF_THE_DAY_TITLE, Filter_Shadow);
    add_filter(LBL_HERO_OF_THE_DAY, Filter_Shadow);
    define_bunch(HERO_OF_THE_DAY, LBL_HERO_OF_THE_DAY_TITLE,
                 LBL_HERO_OF_THE_DAY);
    i = 0;
    while (i < 5) {
        define_lbl((LBL_FIGHT_CHAR_STAERKE_CAPTION + i),
                  texts[(TXT_CHAR_STAERKE + i)],
                  FIGHT_CHAR_PROP_COLUMN_1_X,
                  (FIGHT_CHAR_PROP_Y + (i * FIGHT_CHAR_PROP_Y)),
                  FontFormat_Default);
        define_lbl((LBL_FIGHT_CHAR_STAERKE + i), "",
                  FIGHT_CHAR_PROP_COLUMN_2_X,
                  (FIGHT_CHAR_PROP_Y + (i * FIGHT_CHAR_PROP_Y)),
                  FontFormat_Attrib);
        define_lbl((LBL_FIGHT_OPP_STAERKE_CAPTION + i),
                  texts[(TXT_CHAR_STAERKE + i)],
                  FIGHT_CHAR_PROP_COLUMN_3_X, (FIGHT_CHAR_PROP_Y
                   + (i * FIGHT_CHAR_PROP_Y)), FontFormat_Default);
        define_lbl((LBL_FIGHT_OPP_STAERKE + i), "",
                  FIGHT_CHAR_PROP_COLUMN_4_X,
                  (FIGHT_CHAR_PROP_Y + (i * FIGHT_CHAR_PROP_Y)),
                  FontFormat_Attrib);
        add_filter((LBL_FIGHT_CHAR_STAERKE_CAPTION + i), Filter_Shadow);
        add_filter((LBL_FIGHT_CHAR_STAERKE + i), Filter_Shadow);
        add_filter((LBL_FIGHT_OPP_STAERKE_CAPTION + i), Filter_Shadow);
        add_filter((LBL_FIGHT_OPP_STAERKE + i), Filter_Shadow);
        add_bunch(SCREEN_FIGHT, (LBL_FIGHT_CHAR_STAERKE + i),
                  (LBL_FIGHT_CHAR_STAERKE_CAPTION + i),
                  (LBL_FIGHT_OPP_STAERKE + i),
                  (LBL_FIGHT_OPP_STAERKE_CAPTION + i));
        i = (i + 1);
    };
    define_img(FIGHT_MUSH, "res/gfx/scr/fight/bigmush.png", False, 0, 0);
    define_snd(SND_CATAPULT_LAUNCH, "res/sfx/catapult_launch.mp3");
    define_snd(SND_CATAPULT_HIT, "res/sfx/catapult_hit.mp3");
    i = 0;
    while (i < 3) {
        define_img((FIGHT_COPYCAT + i),
                  (("res/gfx/npc/copycat_" + str((i + 1))) + ".jpg"),
                  False, FIGHT_CHARX, OPPY);
        i = (i + 1);
    };
    define_img(BG_DEMO, "res/gfx/scr/demo/demo.png", False, 0, DEMO_Y);
    define_btn(DEMO_LOGOFF, texts[TXT_OK], RequestLOGout, btn_classBasic,
               DEMO_X, DEMO_Y);
    define_bunch(SCREEN_DEMO, BG_DEMO, IF_OVL, DEMO_LOGOFF, BLACK_SQUARE);
    define_from_class(SHP_OPTION_BLACK, black_square_neutral, OPTION_X,
                    OPTION_Y);
    _local2 = actor[SHP_OPTION_BLACK];
    with (_local2) {
        width = OPTION_X;
        height = OPTION_Y;
        alpha = 0.65;
    };
    define_lbl(LBL_OPTION_TITLE, texts[TXT_OPTION_TITLE], 0,
              (OPTION_Y + OPTION_Y0), FontFormat_ScreenTitle);
    add_filter(LBL_OPTION_TITLE, Filter_Shadow);
    define_lbl(LBL_OPTION_IMAGE, texts[TXT_CHARIMG],
              (OPTION_X + OPTION_IMAGE_X), (OPTION_Y + OPTION_Y1),
              FontFormat_Heading);
    add_filter(LBL_OPTION_IMAGE, Filter_Shadow);
    define_img(OPTION_IMAGEBORDER,
              "res/gfx/scr/option/character_border_small.png",
              False, (OPTION_X + OPTION_IMAGE_X), (OPTION_Y + OPTION_Y2));
    define_btn(OPTION_CHANGEIMG, texts[TXT_CHANGEIMG], OptionBtnHandler,
               btn_classBasic, (OPTION_X + OPTION_IMAGE_X),
               ((OPTION_Y + OPTION_Y5) - 2));
    define_lbl(LBL_OPTION_CHANGE, texts[TXT_CHANGE],
              (OPTION_X + OPTION_CHANGE_X), (OPTION_Y + OPTION_Y1),
              FontFormat_Heading);
    add_filter(LBL_OPTION_CHANGE, Filter_Shadow);
    define_btn(OPTION_CHANGE_NAME, texts[TXT_CHANGE_NAME],
               OptionBtnHandler, btn_classBasic,
               (OPTION_X + OPTION_CHANGE_X), (OPTION_Y + OPTION_Y2));
    define_btn(OPTION_RESEND, texts[TXT_RESEND_BTN1], OptionBtnHandler,
               btn_classBasic, (OPTION_X + OPTION_CHANGE_X),
               (OPTION_Y + OPTION_Y4));
    define_btn(OPTION_CHANGE_EMAIL, texts[TXT_CHANGE_EMAIL],
               OptionBtnHandler, btn_classBasic,
               (OPTION_X + OPTION_CHANGE_X), (OPTION_Y + OPTION_Y2));
    define_btn(OPTION_CHANGE_PASSWORD, texts[TXT_CHANGE_PASSWORD],
               OptionBtnHandler, btn_classBasic,
               (OPTION_X + OPTION_CHANGE_X), (OPTION_Y + OPTION_Y3));
    define_btn(OPTION_DELETE, texts[TXT_DELETE_ACCOUNT],
               OptionBtnHandler, btn_classBasic,
               (OPTION_X + OPTION_CHANGE_X), (OPTION_Y + OPTION_Y5));
    define_btn(OPTION_LUXURY, texts[TXT_LUXURY_BUTTON],
               OptionBtnHandler, btn_classBasic,
               (OPTION_X + OPTION_CHANGE_X), ((OPTION_Y + OPTION_Y5) - 2));
    define_img(LUXURY_SELLER, "res/gfx/scr/option/seller.jpg",
              False, 1100, 190);
    define_from_class(CB_LM_UNCHECKED, cb_unchecked, LM_X, LM_Y);
    actor[CB_LM_UNCHECKED].add_event_listener(MouseEvent.CLICK, CheckLM);
    define_from_class(CB_LM_CHECKED, cb_checked, LM_X, LM_Y);
    actor[CB_LM_CHECKED].add_event_listener(MouseEvent.CLICK, UncheckLM);
    define_lbl(LBL_LM, texts[TXT_LM], (LM_X + LM_X), (LM_Y + LM_Y),
              FontFormat_Default);
    add_filter(LBL_LM, Filter_Shadow);
    define_from_class(CB_CS_UNCHECKED, cb_unchecked, LM_X, (LM_Y - 50));
    actor[CB_CS_UNCHECKED].add_event_listener(MouseEvent.CLICK, CheckCS);
    define_from_class(CB_CS_CHECKED, cb_checked, LM_X, (LM_Y - 50));
    actor[CB_CS_CHECKED].add_event_listener(MouseEvent.CLICK, UncheckCS);
    define_lbl(LBL_CS, ((texts[TXT_CS]) ? texts[TXT_CS] : "Chat Sound"),
              (LM_X + LM_X), ((LM_Y + LM_Y) - 50), FontFormat_Default);
    add_filter(LBL_CS, Filter_Shadow);
    define_from_class(CB_COMPARE_UNCHECKED, cb_unchecked, (LM_X + 250),
                    (LM_Y - 50));
    actor[CB_COMPARE_UNCHECKED].add_event_listener(MouseEvent.CLICK,
                                                   CheckCompare);
    define_from_class(CB_COMPARE_CHECKED, cb_checked, (LM_X + 250),
                    (LM_Y - 50));
    actor[CB_COMPARE_CHECKED].add_event_listener(MouseEvent.CLICK,
                                                 UncheckCompare);
    define_lbl(LBL_COMPARE, texts[TXT_COMPARE], ((LM_X + LM_X) + 250),
              ((LM_Y + LM_Y) - 50), FontFormat_Default);
    add_filter(LBL_COMPARE, Filter_Shadow);
    define_from_class(CB_TV_UNCHECKED, cb_unchecked, (LM_X + 250), LM_Y);
    actor[CB_TV_UNCHECKED].add_event_listener(MouseEvent.CLICK, CheckTV);
    define_from_class(CB_TV_CHECKED, cb_checked, (LM_X + 250), LM_Y);
    actor[CB_TV_CHECKED].add_event_listener(MouseEvent.CLICK, UncheckTV);
    define_lbl(LBL_TV_CHECKBOX, texts[TXT_TV_DISABLE],
              ((LM_X + LM_X) + 250), (LM_Y + LM_Y), FontFormat_Default);
    add_filter(LBL_TV_CHECKBOX, Filter_Shadow);
    define_lbl(LBL_OPTION_DOCHANGE, "", (OPTION_X + OPTION_DOCHANGE_X),
              (OPTION_Y + OPTION_Y1), FontFormat_Heading);
    add_filter(LBL_OPTION_DOCHANGE, Filter_Shadow);
    define_lbl(LBL_OPTION_FIELD1, "", (OPTION_X + OPTION_DOCHANGE_LABEL_X),
              ((OPTION_Y + OPTION_Y2) + OPTION_TEXT_Y),
              FontFormat_DefaultLeft);
    _local2 = actor[LBL_OPTION_FIELD1];
    with (_local2) {
        wordWrap = True;
        width = 300;
    };
    define_lbl(LBL_OPTION_FIELD2, "", (OPTION_X + OPTION_DOCHANGE_LABEL_X),
              ((OPTION_Y + OPTION_Y3) + OPTION_TEXT_Y), FontFormat_Default)
    define_lbl(LBL_OPTION_FIELD3, "", (OPTION_X + OPTION_DOCHANGE_LABEL_X),
              ((OPTION_Y + OPTION_Y4) + OPTION_TEXT_Y), FontFormat_Default)
    add_filter(LBL_OPTION_FIELD1, Filter_Shadow);
    add_filter(LBL_OPTION_FIELD2, Filter_Shadow);
    add_filter(LBL_OPTION_FIELD3, Filter_Shadow);
    define_from_class(INP_OPTION_FIELD1, text_input1,
                    (OPTION_X + OPTION_DOCHANGE_FIELD_X),
                    (OPTION_Y + OPTION_Y2), 2, "name");
    define_from_class(INP_OPTION_FIELD2, text_input2,
                    (OPTION_X + OPTION_DOCHANGE_FIELD_X),
                    (OPTION_Y + OPTION_Y3), 2, "name");
    define_from_class(INP_OPTION_FIELD3, text_input1,
                    (OPTION_X + OPTION_DOCHANGE_FIELD_X),
                    (OPTION_Y + OPTION_Y4), 2, "name");
    actor[INP_OPTION_FIELD1].add_event_listener(KeyboardEvent.KEY_DOWN,
                                                OptionBtnHandler);
    actor[INP_OPTION_FIELD2].add_event_listener(KeyboardEvent.KEY_DOWN,
                                                OptionBtnHandler);
    actor[INP_OPTION_FIELD3].add_event_listener(KeyboardEvent.KEY_DOWN,
                                                OptionBtnHandler);
    actor[INP_OPTION_FIELD2].add_event_listener(KeyboardEvent.KEY_UP,
                                                gradePassword);
    actor[INP_OPTION_FIELD3].add_event_listener(KeyboardEvent.KEY_UP,
                                                gradePassword);
    DefineCnt(CHANGE_PASSWORD_SMILEY_SAD,
              ((OPTION_X + OPTION_DOCHANGE_X) - 50),
              (OPTION_Y + OPTION_Y5));
    DefineCnt(CHANGE_PASSWORD_SMILEY_NEUTRAL,
              ((OPTION_X + OPTION_DOCHANGE_X) - 50),
              (OPTION_Y + OPTION_Y5));
    DefineCnt(CHANGE_PASSWORD_SMILEY_HAPPY,
              ((OPTION_X + OPTION_DOCHANGE_X) - 50),
              (OPTION_Y + OPTION_Y5));
    enable_popup(CHANGE_PASSWORD_SMILEY_SAD,
                 texts[TXT_PASSWORD_SMILEY_SAD].split("#").join(chr(13)));
    enable_popup(CHANGE_PASSWORD_SMILEY_NEUTRAL,
                 texts[TXT_PASSWORD_SMILEY_NEUTRAL].split(
                                      "#").join(chr(13)));
    enable_popup(CHANGE_PASSWORD_SMILEY_HAPPY,
                 texts[TXT_PASSWORD_SMILEY_HAPPY].split("#").join(chr(13)))
    define_btn(OPTION_DOCHANGE, texts[TXT_DOCHANGE], OptionBtnHandler,
               btn_classBasic, (OPTION_X + OPTION_DOCHANGE_X),
               (OPTION_Y + OPTION_Y5));
    define_lbl(LBL_OPTION_VOLUME, "", 0, (OPTION_Y + OPTION_Y6),
              FontFormat_Default);
    add_filter(LBL_OPTION_VOLUME, Filter_Shadow);
    DefineSlider(SLDR_OPTION_VOLUME, 11,
                 ((OPTION_X + OPTION_VOLUME_X) + 250),
                 (OPTION_Y + OPTION_Y7), VolumeChange);
    define_snd(SND_TEST, "res/sfx/click.mp3");
    define_bunch(OPTION_DOCHANGE, LBL_OPTION_DOCHANGE, LBL_OPTION_FIELD1,
                 LBL_OPTION_FIELD2, LBL_OPTION_FIELD3, INP_OPTION_FIELD1,
                 INP_OPTION_FIELD2, INP_OPTION_FIELD3, OPTION_DOCHANGE);
    define_bunch(OPTION_DORESEND, LBL_OPTION_DOCHANGE, LBL_OPTION_FIELD1,
                 OPTION_DOCHANGE);
    define_lbl(LBL_OPTION_VER,
              ("v1.70" + (((get_file_version() == 0)) ? ""
               : ("." + str(get_file_version())))), 0,
                ((OPTION_Y + OPTION_VER_Y) + 110), FontFormat_Default);
    actor[LBL_OPTION_VER].x = (((OPTION_X + OPTION_VER_X) + 60)
                               - actor[LBL_OPTION_VER].text_width);
    add_filter(LBL_OPTION_VER, Filter_Shadow);
    define_bunch(SCREEN_OPTION, SHP_OPTION_BLACK, OPTION_IMAGEBORDER,
                 LBL_OPTION_TITLE, LBL_OPTION_IMAGE, OPTION_CHANGEIMG,
                 LBL_OPTION_CHANGE, OPTION_RESEND);
    add_bunch(SCREEN_OPTION, OPTION_CHANGE_EMAIL, OPTION_CHANGE_PASSWORD,
              OPTION_DELETE, LBL_OPTION_VOLUME, SLDR_OPTION_VOLUME,
              IF_EXIT, SND_TEST, LBL_OPTION_VER, CB_LM_UNCHECKED, LBL_LM);
    add_bunch(SCREEN_OPTION, CHANGE_PASSWORD_SMILEY_SAD,
              CHANGE_PASSWORD_SMILEY_NEUTRAL, CHANGE_PASSWORD_SMILEY_HAPPY,
              CB_CS_UNCHECKED, LBL_CS, CB_COMPARE_UNCHECKED, LBL_COMPARE,
              CB_TV_UNCHECKED, LBL_TV_CHECKBOX);
    Filter_Glow = [new GradientGlowFilter(0, 45, [16777026, 16777026],
                                          [0, 0.4], [0, 127], 16, 16, 1, 1,
                                          "outer")];
    i = 0;
    while (i < param_languages.length) {
        define_img((OPTION_FLAG + i),
                  ("res/gfx/if/flags/flag_" + param_languages[i] + ".png"),
                  False,
                  ((LM_X + (35 * i)) - ((lang_code)==param_languages[i])
                   ? 8 : 0),
                    (LM_Y + ((lang_code)==param_languages[i]) ? 53 : 60),
                    ((lang_code)==param_languages[i]) ? 0.9 : 0.6,
                    ((lang_code)==param_languages[i]) ? 0.9 : 0.6);
        if (lang_code == param_languages[i]){
            add_filter((OPTION_FLAG + i), Filter_Glow);
        };
        actor[(OPTION_FLAG + i)].add_event_listener(MouseEvent.CLICK,
                                                    ChooseLanguageIcon);
        add_bunch(SCREEN_OPTION, (OPTION_FLAG + i));
        enable_popup((OPTION_FLAG + i), param_language_names[i]);
        i = (i + 1);
    };
    optionMenuSelect = 0;
    define_lbl(LBL_HLMAINQUESTS_TITLE, texts[TXT_HL_MAINQUESTS_TITLE], 0,
              MQS_TITLE_Y, FontFormat_ScreenTitle);
    add_filter(LBL_HLMAINQUESTS_TITLE, Filter_Shadow);
    define_img(HLMQS_DISABLED, "res/gfx/scr/dungeons/unknown.png",
              False, 0, 0);
    define_img(HLMQS_COMPLETED, "res/gfx/scr/dungeons/done.png",
              False, 0, 0);
    define_img(HLMQS_TOWER_DISABLED, "res/gfx/scr/dungeons/unknown.png",
              False, 0, 0);
    define_img(HLMQS_TOWER_COMPLETED, "res/gfx/scr/dungeons/done_tower.png",
              False, 0, 0);
    define_bunch(SCREEN_HLMAINQUESTS, IF_OVL, IF_EXIT,
                 LBL_HLMAINQUESTS_TITLE, SND_MAINQUESTS_UNLOCK);
    i = 0;
    while (i < 5) {
        if (i == 4){
            DefineCnt((HLMQS_BUTTON + 4),
                      ((MQS_BUTTON_X + MQS_BUTTON_X) + 0),
                      ((MQS_BUTTON_Y + MQS_BUTTON_Y) - 170));
            define_img((HLMQS_BUTTON + 4),
                      "res/gfx/scr/dungeons/button_tower.jpg", False,
                      ((MQS_BUTTON_X + MQS_BUTTON_X) + 0),
                      ((MQS_BUTTON_Y + MQS_BUTTON_Y) - 170));
            DefineCnt((HLMQS_DISABLED + 4),
                      ((MQS_BUTTON_X + MQS_BUTTON_X) + 0),
                      ((MQS_BUTTON_Y + MQS_BUTTON_Y) - 170));
            DefineCnt((HLMQS_COMPLETED + 4),
                      ((MQS_BUTTON_X + MQS_BUTTON_X) + 0),
                      ((MQS_BUTTON_Y + MQS_BUTTON_Y) - 170));
        } else {
            DefineCnt((HLMQS_BUTTON + i),
                      (MQS_BUTTON_X + ((MQS_BUTTON_X * 2) * int((i % 2)))),
                      ((MQS_BUTTON_Y + 100) + (200 * int((i / 2)))));
            define_img((HLMQS_BUTTON + i),
                      (("res/gfx/scr/dungeons/button" + str((60 + i)))
                       + ".jpg"), False, (MQS_BUTTON_X +
                       ((MQS_BUTTON_X * 2) * int((i % 2)))),
                        ((MQS_BUTTON_Y + 100) + (200 * int((i / 2)))));
            DefineCnt((HLMQS_DISABLED + i),
                      (MQS_BUTTON_X + ((MQS_BUTTON_X * 2) * int((i % 2)))),
                      ((MQS_BUTTON_Y + 100) + (200 * int((i / 2)))));
            DefineCnt((HLMQS_COMPLETED + i),
                      (MQS_BUTTON_X + ((MQS_BUTTON_X * 2) * int((i % 2)))),
                      ((MQS_BUTTON_Y + 100) + (200 * int((i / 2)))));
        };
        add_bunch(SCREEN_HLMAINQUESTS, (HLMQS_BUTTON + i),
                  (HLMQS_DISABLED + i), (HLMQS_COMPLETED + i));
        enable_popup((HLMQS_DISABLED + i), POPUP_BEGIN_LINE,
                     texts[(TXT_HL_MAINQUESTS_NAME + i)].split("|")[0],
                     POPUP_END_LINE, POPUP_BEGIN_LINE,
                     FontFormat_EpicItemQuote,
                     texts[(TXT_HL_MAINQUESTS_NAME + i)].split("|")[1],
                     FontFormat_Popup, POPUP_END_LINE, POPUP_BEGIN_LINE,
                     texts[(TXT_DUNGEON_INFO + 1)], POPUP_END_LINE);
        enable_popup((HLMQS_COMPLETED + i), POPUP_BEGIN_LINE,
                     texts[(TXT_HL_MAINQUESTS_NAME + i)].split("|")[0],
                     POPUP_END_LINE, POPUP_BEGIN_LINE,
                     FontFormat_EpicItemQuote,
                     texts[(TXT_HL_MAINQUESTS_NAME + i)].split("|")[1],
                     FontFormat_Popup, POPUP_END_LINE, POPUP_BEGIN_LINE,
                     texts[(TXT_DUNGEON_INFO + 2)], POPUP_END_LINE);
        i = (i + 1);
    };
    define_lbl(LBL_MAINQUESTS_TITLE, texts[(TXT_DUNGEON_INFO + 4)], 0,
              MQS_TITLE_Y, FontFormat_ScreenTitle);
    add_filter(LBL_MAINQUESTS_TITLE, Filter_Shadow);
    define_snd(SND_MAINQUESTS_UNLOCK, "res/sfx/unlock.mp3", False);
    define_img(MQS_DISABLED,
              "res/gfx/scr/dungeons/unknown.png", False, 0, 0);
    define_img(MQS_COMPLETED,
              "res/gfx/scr/dungeons/done.png", False, 0, 0);
    define_bunch(SCREEN_MAINQUESTS, IF_OVL, IF_EXIT, LBL_MAINQUESTS_TITLE,
                 SND_MAINQUESTS_UNLOCK);
    i = 0;
    while (i < 9) {
        DefineCnt((MQS_BUTTON + i),
                  (MQS_BUTTON_X + (MQS_BUTTON_X * int((i % 3)))),
                  (MQS_BUTTON_Y + (MQS_BUTTON_Y * int((i / 3)))));
        define_img((MQS_BUTTON + i),
                  (("res/gfx/scr/dungeons/button" + str(51 + i)) + ".jpg"),
                  False, (MQS_BUTTON_X + (MQS_BUTTON_X * int((i % 3)))),
                  (MQS_BUTTON_Y + (MQS_BUTTON_Y * int((i / 3)))));
        DefineCnt((MQS_DISABLED + i),
                  (MQS_BUTTON_X + (MQS_BUTTON_X * int((i % 3)))),
                  (MQS_BUTTON_Y + (MQS_BUTTON_Y * int((i / 3)))));
        DefineCnt((MQS_COMPLETED + i),
                  (MQS_BUTTON_X + (MQS_BUTTON_X * int((i % 3)))),
                  (MQS_BUTTON_Y + (MQS_BUTTON_Y * int((i / 3)))));
        add_bunch(SCREEN_MAINQUESTS, (MQS_BUTTON + i), (MQS_DISABLED + i),
                  (MQS_COMPLETED + i));
        enable_popup((MQS_DISABLED + i), POPUP_BEGIN_LINE,
                     texts[(TXT_DUNGEON_NAME + i)].split("|")[0],
                     POPUP_END_LINE, POPUP_BEGIN_LINE,
                     FontFormat_EpicItemQuote,
                     texts[(TXT_DUNGEON_NAME + i)].split("|")[1],
                     FontFormat_Popup, POPUP_END_LINE, POPUP_BEGIN_LINE,
                     texts[(TXT_DUNGEON_INFO + 1)], POPUP_END_LINE);
        enable_popup((MQS_COMPLETED + i), POPUP_BEGIN_LINE,
                     texts[(TXT_DUNGEON_NAME + i)].split("|")[0],
                     POPUP_END_LINE, POPUP_BEGIN_LINE,
                     FontFormat_EpicItemQuote,
                     texts[(TXT_DUNGEON_NAME + i)].split("|")[1],
                     FontFormat_Popup, POPUP_END_LINE, POPUP_BEGIN_LINE,
                     texts[(TXT_DUNGEON_INFO + 2)], POPUP_END_LINE);
        i = (i + 1);
    };
    define_img(DUNGEON_CONGRATS, "res/gfx/scr/dungeons/congrats.jpg",
              False, 280, 100);
    define_lbl(LBL_DUNGEON_CONGRATS,
              ((texts[TXT_CONGRATS])
               ? texts[TXT_CONGRATS].split("#").join(chr(13))
               : ""), 1000, 600, FontFormat_Default);
    actor[LBL_DUNGEON_CONGRATS].wordWrap = True;
    actor[LBL_DUNGEON_CONGRATS].default_text_format.align = "right";
    add_filter(LBL_DUNGEON_CONGRATS, Filter_Shadow);
    define_bunch(DUNGEON_CONGRATS, DUNGEON_CONGRATS, LBL_DUNGEON_CONGRATS,
                 IF_OVL, IF_EXIT);
    define_from_class(SHP_MAINQUEST, black_square, MQ_SQUARE_X, MQ_SQUARE_Y);
    _local2 = actor[SHP_MAINQUEST];
    with (_local2) {
        width = MQ_SQUARE_X;
        height = MQ_SQUARE_Y;
        alpha = 0.6;
    };
    define_lbl(LBL_MAINQUEST_TITLE, "", 0, (MQ_SQUARE_Y + MQ_TITLE_Y),
              FontFormat_ScreenTitle);
    add_filter(LBL_MAINQUEST_TITLE, Filter_Shadow);
    define_lbl(LBL_MAINQUEST_TEXT, "", (MQ_SQUARE_X + MQ_TEXT_X),
              (MQ_SQUARE_Y + MQ_TEXT_Y), FontFormat_DefaultLeft);
    _local2 = actor[LBL_MAINQUEST_TEXT];
    with (_local2) {
        width = (MQ_SQUARE_X - (MQ_TEXT_X * 2));
        wordWrap = True;
    };
    add_filter(LBL_MAINQUEST_TEXT, Filter_Shadow);
    define_btn(MAINQUEST_START, "", RequestMainQuest, btn_classBasic, 0,
               ((MQ_SQUARE_Y + MQ_SQUARE_Y) - MQ_BUTTON_Y));
    _local2 = actor[MAINQUEST_START];
    with (_local2) {
        x = (((MQ_SQUARE_X + MQ_SQUARE_X) - MQ_TEXT_X) - width);
    };
    define_lbl(LBL_MAINQUEST_MUSHHINT, texts[TXT_MQ_MUSHHINT],
              (MQ_SQUARE_X + MQ_TEXT_X),
              ((MQ_SQUARE_Y + MQ_SQUARE_Y) - MQ_MUSHHINT_Y),
              FontFormat_DefaultLeft);
    _local2 = actor[LBL_MAINQUEST_MUSHHINT];
    with (_local2) {
        width = ((MQ_SQUARE_X - (MQ_TEXT_X * 3))
                 - actor[MAINQUEST_START].width);
        wordWrap = True;
    };
    add_filter(LBL_MAINQUEST_MUSHHINT, Filter_Shadow);
    DefineCnt(MAINQUEST_enemy, MAINQUEST_enemy_X, MAINQUEST_enemy_Y);
    DefineCnt(MAINQUEST_enemy_BORDER, (MAINQUEST_enemy_X - MQ_BORDER_X),
              (MAINQUEST_enemy_Y - MQ_BORDER_Y));
    define_bunch(SCREEN_MAINQUEST, SHP_MAINQUEST, IF_OVL,
                 LBL_MAINQUEST_TITLE, LBL_MAINQUEST_TEXT,
                 MAINQUEST_enemy_BORDER, MAINQUEST_enemy,
                 LBL_MAINQUEST_MUSHHINT, MAINQUEST_START, IF_EXIT);
    define_lbl(LBL_DISCONNECTED, texts[TXT_DISCONNECTED],
              ((DISCONNECTED_X - (DISCONNECTED_X / 2)) + 10),
              (DISCONNECTED_Y + 10), FontFormat_Error);
    _local2 = actor[LBL_DISCONNECTED];
    with (_local2) {
        wordWrap = True;
        width = (DISCONNECTED_X - 20);
    };
    add_filter(LBL_DISCONNECTED, Filter_Shadow);
    define_from_class(SHP_DISCONNECTED, black_square_neutral,
                    (DISCONNECTED_X - (DISCONNECTED_X / 2)),
                    DISCONNECTED_Y);
    _local2 = actor[SHP_DISCONNECTED];
    with (_local2) {
        width = DISCONNECTED_X;
        height = (actor[LBL_DISCONNECTED].textHeight + 20);
        alpha = 0.8;
    };
    define_bunch(SCREEN_DISCONNECTED, BLACK_SQUARE, SHP_DISCONNECTED,
                 LBL_DISCONNECTED);
    define_lbl(LBL_EMAIL_NAG, texts[TXT_EMAIL_NAG], EMAIL_NAG_X,
              EMAIL_NAG_Y, FontFormat_DefaultLeft);
    actor[LBL_EMAIL_NAG].width = EMAIL_NAG_TEXT_X;
    actor[LBL_EMAIL_NAG].wordWrap = True;
    add_filter(LBL_EMAIL_NAG, Filter_Shadow);
    define_lbl(LBL_EMAIL_RESEND, texts[TXT_EMAIL_RESEND], 0, 0,
              FontFormat_Default);
    add_filter(LBL_EMAIL_RESEND, Filter_Shadow);
    MakePersistent(LBL_EMAIL_RESEND);
    DefineCnt(EMAIL_RESEND, EMAIL_NAG_X, (EMAIL_NAG_Y + EMAIL_RESEND_Y));
    _local2 = actor[EMAIL_RESEND];
    with (_local2) {
        addChild(actor[LBL_EMAIL_RESEND]);
        textLinkMakeClickable(getChildAt(0).parent);
        mouseChildren = False;
        mouse_enabled = True;
        buttonMode = True;
        useHandCursor = True;
        add_event_listener(MouseEvent.CLICK, ResendConfirmationEmail);
    };
    define_btn(EMAIL_NAG, texts[TXT_OK], ShowCityScreen, btn_classBasic,
               ((IF_WIN_X + IF_WIN_WELCOME_X) + IF_WIN_X),
               (IF_WIN_Y + EMAIL_NAG_Y));
    define_bunch(SCREEN_EMAIL_NAG, IF_WINDOW, LBL_WINDOW_TITLE,
                 LBL_EMAIL_NAG, EMAIL_NAG, IF_EXIT);
    DefineCnt(POPUP_INFO);
    _local2 = actor[POPUP_INFO];
    with (_local2) {
    };
    add(POPUP_INFO);
    add(IF_MAIN);
    add(IF_BUTTONS);
    if (param_obj["login"]){
        show_login_screen(None, True);
    } else {
        show_build_character_screen();
    };
    '''
    pass
