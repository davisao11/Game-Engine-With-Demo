from graphics import *
import repository
import maps
quest1_jorge = quest2_jorge = quest3_jorge = quest4_jorge = quest5_jorge = 2

def buy_option(i, dialog_option_1, value, item, dialog_option, no_money, tempx1, tempx2, tempy1, tempy2, window):
    if dialog_option == dialog_option_1 and not no_money:
        temp_ammount = True
        temp_has_gold = True
        has_bought = False
        quantity = 0
        while temp_ammount:
            for e in repository.gui_text:
                e.undraw()
            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
            if quantity * value <= repository.inventory['gold']:
                repository.dialog('How many?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                temp_has_gold = True
            else:
                repository.dialog('Not enough gold.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                temp_has_gold = False
            repository.dialog(str(quantity), tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
            key = window.getKey()
            if quantity >= 0:
                if key == "w" or key == "Up":
                    quantity += 1
                elif key == "d" or key == "Right":
                    quantity += 10
                elif key == "Return" and temp_has_gold:
                    temp_ammount = False
                    has_bought = True
            if quantity >= 1:
                if key == "s" or key == "Down":
                    quantity -= 1
            if quantity >= 10:
                if key == "a" or key == "Left":
                    quantity -= 10

            if key == "Escape":
                temp_ammount = False

        if has_bought:
            if repository.inventory['gold'] >= quantity * value:
                repository.inventory['gold'] -= quantity * value
            for e in repository.gui_text:
                e.undraw()
            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
            repository.dialog('You bought ' + str(quantity) + ' ' + item, tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
            temp1 = 0
            try:
                temp1 = repository.inventory[item]
                del repository.inventory[item]
            except:
                pass
            repository.inventory[item] = temp1 + quantity

        # close the dialog
        temp1 = True
        while temp1:
            if key != "Escape":
                key = window.getKey()
            if key == "Escape" or key == "Return":
                for e in repository.gui_text:
                    e.undraw()
                for e in repository.gui_background:
                    e.undraw()
                for e in repository.gui_sprites:
                    e.undraw()
                repository.mov = True
                temp = temp1 = False
                return temp
    else:
        temp = True
        return temp

def sell_option(i, dialog_option_1, value, item, amount, dialog_option, tempx1, tempx2, tempy1, tempy2, window):
    if dialog_option == dialog_option_1 and amount != 0:
        temp_ammount = True
        temp_has_item = True
        quantity = 0
        while temp_ammount:
            for e in repository.gui_text:
                e.undraw()
            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
            if amount - quantity > 0:
                repository.dialog('How many?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                temp_has_item = True
            else:
                repository.dialog('Those are all you have.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                temp_has_item = False
            repository.dialog(str(quantity), tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
            repository.dialog('Gold: ' + str(quantity * value), tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
            key = window.getKey()
            if quantity >= 0 and temp_has_item:
                if key == "w" or key == "Up":
                    quantity += 1
                elif key == "d" or key == "Right":
                    quantity += 10
                elif key == "Return":
                    temp_ammount = False
            if quantity >= 1:
                if key == "s" or key == "Down":
                    quantity -= 1
            if quantity >= 10:
                if key == "a" or key == "Left":
                    quantity -= 10

            if key == "Escape":
                temp_ammount = False

        repository.inventory[item] -= quantity
        repository.inventory['gold'] += quantity * value
        for e in repository.gui_text:
            e.undraw()
        repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
        repository.dialog('You sold ' + str(quantity) + ' ' + '(' + item + ')', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)

        # close the dialog
        temp1 = True
        while temp1:
            if key != "Escape":
                key = window.getKey()
            if key == "Escape" or key == "Return":
                for e in repository.gui_text:
                    e.undraw()
                for e in repository.gui_background:
                    e.undraw()
                for e in repository.gui_sprites:
                    e.undraw()
                repository.mov = True
                temp = temp1 = False
                return temp
    else:
        temp = True
        return temp



def receive_quest(required_item, required_ammount, quest_status, tempx1, tempx2, tempy1, tempy2, window):
    # quest completed = 1
    # quest not completed = 0
    # quest accepted = 3
    # quest not accepted = 2
    try:
        quest_requirement = repository.inventory[required_item] >= required_ammount
    except:
        quest_requirement = False

    if quest_status == 3:
        if quest_requirement:
            repository.dialog('2.Here\'s what you asked for. (-' + str(required_ammount) + ' ' + required_item + ')', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
            quest_status = 1
            return quest_status
        else:
            repository.dialog('2.I still need ' + str(required_ammount) + ' ' + required_item, tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)

    elif quest_status == 2:
        repository.dialog('2.Do you have a quest for me?', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
        return quest_status


def deliver_quest(key, i, quest_completed, required_item, required_ammount, quest_reward, tempx1, tempx2, tempy1, tempy2, window):
    if key == "2" and quest_completed == 1:
        for e in repository.gui_text:
            e.undraw()

        repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
        repository.dialog('Thank you so much, here have this as a reward.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
        repository.dialog('The villager hands you ' + str(quest_reward) + ' gold coins.', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)
        repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 5, repository.gui_text, window)
        repository.inventory['gold'] += quest_reward
        repository.inventory[required_item] -= required_ammount
        quest_completed = 4

        # close the dialog
        temp1 = True
        while temp1:
            key = window.getKey()
            if key == "Escape" or key == "Return":
                temp1 = False
                temp = True
                return quest_completed

    else:
        temp = False
        return temp


# interaction function
def inter(window, character):
    global quest1_jorge

    if repository.is_alive == False:
        character.life = 100 + (repository.inventory['armor lvl'] * 20)
        maps.city(True, window)
        repository.is_alive = True

    if repository.return_to_city:
        repository.return_to_city = False
        maps.city(True, window)

    while repository.intro:
        key = (window.getKey()).lower()
        if key == "w" or key == "a" or key == "s" or key == "d" or key == "escape":
            for e in repository.gui_text:
                e.undraw()
            for e in repository.gui_menu_bc:
                e.undraw()
            for e in repository.gui_sprites:
                e.undraw()
            repository.gui_text.clear()
            repository.gui_menu_bc.clear()
            repository.gui_sprites.clear()
            repository.intro = False
            character.life = 100 + (repository.inventory['armor lvl'] * 20)


    # npc interaction
    if repository.movement(window, character) == "return":

        # npcs
        for i in repository.npcs:
            # collision equations:
            # "w" up
            xw = character.x1 >= i.x1 - repository.default_m and character.x2 <= i.x2 + repository.default_m
            yw = ((character.y2 + character.y1) // 2) - (((character.y2 - character.y1) // 2) + ((i.y2 - i.y1) // 2)) == (i.y2 + i.y1) // 2

            # "a" left
            ya = character.y1 >= i.y1 - repository.default_m and character.y2 <= i.y2 + repository.default_m
            xa = ((character.x2 + character.x1) // 2) - (((character.x2 - character.x1) // 2) + ((i.x2 - i.x1) // 2)) == (i.x2 + i.x1) // 2

            # "s" down
            xs = character.x1 >= i.x1 - repository.default_m and character.x2 <= i.x2 + repository.default_m
            ys = ((character.y2 + character.y1) // 2) + (((character.y2 - character.y1) // 2) + ((i.y2 - i.y1) // 2)) == (i.y2 + i.y1) // 2

            # "d" right
            yd = character.y1 >= i.y1 - repository.default_m and character.y2 <= i.y2 + repository.default_m
            xd = ((character.x2 + character.x1) // 2) + (((character.x2 - character.x1) // 2) + ((i.x2 - i.x1) // 2)) == (i.x2 + i.x1) // 2

            # collision check:
            if (xw and yw) or (ya and xa) or (xs and ys) or (yd and xd):
                # stop player movement
                repository.mov = False

                if i.npc_gender == "male":
                    sprite = Image(Point(repository.resx // 2, repository.resy // 2), 'sprites/npc_male.png')
                    sprite.draw(window)
                    repository.gui_sprites.append(sprite)

                if i.npc_gender == "female":
                    sprite = Image(Point(repository.resx // 2, (repository.resy // 2) + (repository.resy // 10)), 'sprites/npc_female.png')
                    sprite.draw(window)
                    repository.gui_sprites.append(sprite)

                if i.npc_gender == "male_blacksmith":
                    sprite = Image(Point(repository.resx // 2, (repository.resy // 2) + (repository.resy // 10)), 'sprites/npc_blacksmith.png')
                    sprite.draw(window)
                    repository.gui_sprites.append(sprite)

                if i.npc_gender == "male_potions_seller":
                    sprite = Image(Point(repository.resx // 2, (repository.resy * 0.4) + (repository.resy // 10)), 'sprites/npc_potions_seller.png')
                    sprite.draw(window)
                    repository.gui_sprites.append(sprite)

                if i.npc_gender == "male_goods_trader":
                    sprite = Image(Point(repository.resx // 2, (repository.resy // 2) + (repository.resy // 10)), 'sprites/npc_goods_trader.png')
                    sprite.draw(window)
                    repository.gui_sprites.append(sprite)

                # gui text box creation
                tempx1 = 0
                tempy1 = repository.resy - ((repository.resy * 35) // 100)
                tempx2 = repository.resx
                tempy2 = repository.resy
                text_box = repository.rectangle(tempx1, tempy1, tempx2, tempy2, "white")
                text_box.draw(window)
                repository.gui_background.append(text_box)

                # dialog if npc is "jorge"
                if i.obj_name == "Jorge":

                    repository.dialog(i.obj_name + " :", tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                    repository.dialog('What is it?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                    repository.dialog('1.Tell me about yourself.', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                    if repository.player_lvl <= 20 and not quest1_jorge == 4:
                        quest1_jorge = receive_quest('wolf\'s teeth', 1, quest1_jorge, tempx1, tempx2, tempy1, tempy2, window)
                    elif 20 < repository.player_lvl <= 40 and not quest2_jorge == 4:
                        quest2_jorge = receive_quest('wolf\'s teeth', 1, quest2_jorge, tempx1, tempx2, tempy1, tempy2, window)
                    elif 40 < repository.player_lvl <= 60 and not quest3_jorge == 4:
                        quest3_jorge = receive_quest('wolf\'s teeth', 1, quest3_jorge, tempx1, tempx2, tempy1, tempy2, window)
                    elif 60 < repository.player_lvl <= 80 and not quest4_jorge == 4:
                        quest4_jorge = receive_quest('wolf\'s teeth', 1, quest4_jorge, tempx1, tempx2, tempy1, tempy2, window)
                    elif 80 < repository.player_lvl and not quest5_jorge == 4:
                        quest5_jorge = receive_quest('wolf\'s teeth', 1, quest5_jorge, tempx1, tempx2, tempy1, tempy2, window)

                    temp_intro = True
                    while temp_intro:
                        key = window.getKey()
                        if key == "1":
                            for e in repository.gui_text:
                                e.undraw()
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('My name is Jorge.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)

                            # close the dialog
                            temp1 = True
                            while temp1:
                                key = window.getKey()
                                if key == "Escape" or key == "Return" or temp_intro == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp1 = temp_intro = False

                        if repository.player_lvl < 20:
                            temp_exit = deliver_quest(key, i, quest1_jorge, 'wolf\'s teeth', 1, 15, tempx1, tempx2, tempy1, tempy2, window)
                            if key == "2" and quest1_jorge == 2:
                                for e in repository.gui_text:
                                    e.undraw()
                                quest1_jorge = 3
                                repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                repository.dialog('I need 1 wolf\'s teeth.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)

                                # close the dialog
                                temp1 = True
                                while temp1 and temp_intro:
                                    key = window.getKey()
                                    if key == "Escape" or key == "Return":
                                        for e in repository.gui_text:
                                            e.undraw()
                                        for e in repository.gui_background:
                                            e.undraw()
                                        for e in repository.gui_sprites:
                                            e.undraw()
                                        repository.mov = True
                                        temp1 = temp_intro = False

                        elif 20 < repository.player_lvl <= 40:
                            temp_exit = deliver_quest(key, i, quest2_jorge, 'wolf\'s teeth', 1, 15, tempx1, tempx2, tempy1, tempy2, window)
                            if key == "2" and quest2_jorge == 2:
                                for e in repository.gui_text:
                                    e.undraw()
                                quest2_jorge = 3
                                repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                repository.dialog('I need 20 wolf\'s teeth.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)

                                # close the dialog
                                temp1 = True
                                while temp1 and temp_intro:
                                    key = window.getKey()
                                    if key == "Escape" or key == "Return":
                                        for e in repository.gui_text:
                                            e.undraw()
                                        for e in repository.gui_background:
                                            e.undraw()
                                        for e in repository.gui_sprites:
                                            e.undraw()
                                        repository.mov = True
                                        temp1 = temp_intro = False

                        elif 40 < repository.player_lvl <= 60:
                            temp_exit = deliver_quest(key, i, quest3_jorge, 'wolf\'s teeth', 1, 15, tempx1, tempx2, tempy1, tempy2, window)
                            if key == "2" and quest3_jorge == 2:
                                for e in repository.gui_text:
                                    e.undraw()
                                quest3_jorge = 3
                                repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                repository.dialog('I need 40 wolf\'s teeth.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)

                                # close the dialog
                                temp1 = True
                                while temp1 and temp_intro:
                                    key = window.getKey()
                                    if key == "Escape" or key == "Return":
                                        for e in repository.gui_text:
                                            e.undraw()
                                        for e in repository.gui_background:
                                            e.undraw()
                                        for e in repository.gui_sprites:
                                            e.undraw()
                                        repository.mov = True
                                        temp1 = temp_intro = False

                        elif 60 < repository.player_lvl <= 80:
                            temp_exit = deliver_quest(key, i, quest4_jorge, 'wolf\'s teeth', 1, 15, tempx1, tempx2, tempy1, tempy2, window)
                            if key == "2" and quest4_jorge == 2:
                                for e in repository.gui_text:
                                    e.undraw()
                                quest4_jorge = 3
                                repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                repository.dialog('I need 60 wolf\'s teeth.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)

                                # close the dialog
                                temp1 = True
                                while temp1 and temp_intro:
                                    key = window.getKey()
                                    if key == "Escape" or key == "Return":
                                        for e in repository.gui_text:
                                            e.undraw()
                                        for e in repository.gui_background:
                                            e.undraw()
                                        for e in repository.gui_sprites:
                                            e.undraw()
                                        repository.mov = True
                                        temp1 = temp_intro = False

                        elif 80 < repository.player_lvl:
                            temp_exit = deliver_quest(key, i, quest5_jorge, 'wolf\'s teeth', 1, 15, tempx1, tempx2, tempy1, tempy2, window)
                            if key == "2" and quest5_jorge == 2:
                                for e in repository.gui_text:
                                    e.undraw()
                                quest5_jorge = 3
                                repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                repository.dialog('I need 80 wolf\'s teeth.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)

                                # close the dialog
                                temp1 = True
                                while temp1 and temp_intro:
                                    key = window.getKey()
                                    if key == "Escape" or key == "Return":
                                        for e in repository.gui_text:
                                            e.undraw()
                                        for e in repository.gui_background:
                                            e.undraw()
                                        for e in repository.gui_sprites:
                                            e.undraw()
                                        repository.mov = True
                                        temp1 = temp_intro = False


                        # close the dialog
                        if key == "Escape" or temp_exit:
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp_intro = False

                # dialog if npc is "jorge"
                elif i.obj_name == "Lily":

                    repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text,
                                      window)
                    repository.dialog('What is it?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text,
                                      window)
                    repository.dialog('1.Tell me about yourself.', tempx1, tempx2, tempy1, tempy2, 3.5,
                                      repository.gui_text, window)
                    if repository.player_lvl < 20:
                        quest1_lily = receive_quest('wolf\'s teeth', 1, quest1_jorge, tempx1, tempx2,
                                                     tempy1, tempy2, window)

                    temp_intro = True
                    while temp_intro:
                        key = window.getKey()
                        if key == "1":
                            for e in repository.gui_text:
                                e.undraw()
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('My name is Lily.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)

                            # close the dialog
                            temp1 = True
                            while temp1:
                                key = window.getKey()
                                if key == "Escape" or key == "Return" or temp_intro == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp1 = temp_intro = False

                        if repository.player_lvl < 20:
                            temp_exit = deliver_quest(key, i, quest1_lily, 'wolf\'s teeth', 1, 15, tempx1, tempx2, tempy1, tempy2, window)
                            if key == "2" and quest1_lily == 2:
                                for e in repository.gui_text:
                                    e.undraw()
                                quest1_jorge = 3
                                repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                repository.dialog('I need 1 wolf\'s teeth.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, window)

                                # close the dialog
                                temp1 = True
                                while temp1 and temp_intro:
                                    key = window.getKey()
                                    if key == "Escape" or key == "Return":
                                        for e in repository.gui_text:
                                            e.undraw()
                                        for e in repository.gui_background:
                                            e.undraw()
                                        for e in repository.gui_sprites:
                                            e.undraw()
                                        repository.mov = True
                                        temp1 = temp_intro = False

                        # close the dialog
                        if key == "Escape" or temp_exit:
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp_intro = False

                # dialog if npc is "roberto"
                elif i.obj_name == "Roberta":
                    repository.dialog('1.ir para floresta', tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                    repository.dialog('2.ir para cidade', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)

                    # to choose dialog:
                    temp = True
                    while temp:
                        dialog_option = repository.movement(window, character)
                        if dialog_option == "1":
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp = False
                            maps.forest(True, window)

                        # second dialog option
                        elif dialog_option == "2":
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp = False
                            maps.city(True, window)

                        # close the dialog
                        elif dialog_option == "escape":
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp = False

                elif i.obj_name == "Blacksmith":
                    repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                    repository.dialog('What is it?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                    repository.dialog('1.Tell me about yourself.', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                    repository.dialog('2.I\'d like to upgrade my gear.', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)

                    temp_intro = True
                    while temp_intro:
                        key = window.getKey()

                        if key == "1":
                            for e in repository.gui_text:
                                e.undraw()
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('I\'m the blacksmith.', tempx1, tempx2, tempy1, tempy2, 2.5, repository.gui_text, window)

                            # close the dialog
                            temp1 = True
                            while temp1:
                                key = window.getKey()
                                if key == "Escape" or key == "Return" or temp_intro == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp1 = temp_intro = False

                        elif key == "2":
                            for e in repository.gui_text:
                                e.undraw()
                            not_enough_swd = False
                            not_enough_arm = False
                            sword_cr_ir = armor_cr_ir = 0
                            sword_cr_sv = armor_cr_sv = 0
                            sword_cr_st = armor_cr_st = 0
                            sword_cr_mt = armor_cr_mt = 0
                            sword_cr_ob = armor_cr_ob = 0

                            if repository.inventory['sword lvl'] == 0:
                                sword_cr_ir = 1
                            if repository.inventory['sword lvl'] <= 20:
                                for e in range(0, repository.inventory['sword lvl']):
                                    sword_cr_ir += 5
                            if 40 >= repository.inventory['sword lvl'] > 20:
                                for e in range(0, repository.inventory['sword lvl'] - 20):
                                    sword_cr_ir += 5
                                    sword_cr_sv += 5
                            if 60 >= repository.inventory['sword lvl'] > 40:
                                sword_cr_ir = 0
                                for e in range(0, repository.inventory['sword lvl'] - 40):
                                    sword_cr_sv += 5
                                    sword_cr_st += 5
                            if 80 >= repository.inventory['sword lvl'] > 60:
                                sword_cr_sv = 0
                                for e in range(0, repository.inventory['sword lvl'] - 60):
                                    sword_cr_st += 5
                                    sword_cr_mt += 5
                            if 100 > repository.inventory['sword lvl'] > 80:
                                sword_cr_st = 0
                                for e in range(0, repository.inventory['sword lvl'] - 80):
                                    sword_cr_mt += 5
                                    sword_cr_ob += 5

                            # armor requirements
                            if repository.inventory['armor lvl'] == 0:
                                armor_cr_ir = 1
                            if repository.inventory['armor lvl'] <= 20:
                                for e in range(0, repository.inventory['armor lvl']):
                                    armor_cr_ir += 5
                            if 40 >= repository.inventory['armor lvl'] > 20:
                                for e in range(0, repository.inventory['armor lvl'] - 20):
                                    armor_cr_ir += 10
                                    armor_cr_sv += 5
                            if 60 >= repository.inventory['armor lvl'] > 40:
                                armor_cr_ir = 0
                                for e in range(0, repository.inventory['armor lvl'] - 40):
                                    armor_cr_sv += 10
                                    armor_cr_st += 5
                            if 80 >= repository.inventory['armor lvl'] > 60:
                                armor_cr_sv = 0
                                for e in range(0, repository.inventory['armor lvl'] - 60):
                                    armor_cr_st += 10
                                    armor_cr_mt += 5
                            if 100 > repository.inventory['armor lvl'] > 80:
                                armor_cr_st = 0
                                for e in range(0, repository.inventory['armor lvl'] - 80):
                                    armor_cr_mt += 10
                                    armor_cr_ob += 5

                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('What would you like to upgrade?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                            if repository.inventory['sword lvl'] >= 100:
                                repository.dialog('1.sword upgrade (max LvL)', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                                not_enough_swd = True
                            elif repository.inventory['silver'] < sword_cr_sv or repository.inventory['iron'] < sword_cr_ir or repository.inventory['steel'] < sword_cr_st or repository.inventory['mithril'] < sword_cr_mt or repository.inventory['obsidian'] < sword_cr_ob:
                                repository.dialog('1.sword upgrade (not enough materials)', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                                not_enough_swd = True
                            else:
                                repository.dialog('1.sword upgrade', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                            repository.dialog('(iron: ' + str(sword_cr_ir) + '\\' + str(repository.inventory['iron']) + ', silver: ' + str(sword_cr_sv) + '\\' + str(repository.inventory['silver']) + ', steel: ' + str(sword_cr_st) + '\\' + str(repository.inventory['steel']) + ', mithril: ' + str(sword_cr_mt) + '\\' + str(repository.inventory['mithril']) + ', obsidian: ' + str(sword_cr_ob) + '\\' + str(repository.inventory['obsidian']) + ')', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)

                            if repository.inventory['armor lvl'] >= 100:
                                repository.dialog('2.armor upgrade (max LvL)', tempx1, tempx2, tempy1, tempy2, 6, repository.gui_text, window)
                                not_enough_arm = True
                            elif repository.inventory['silver'] < armor_cr_sv or repository.inventory['iron'] < armor_cr_ir or repository.inventory['steel'] < armor_cr_st or repository.inventory['mithril'] < armor_cr_mt or repository.inventory['obsidian'] < armor_cr_ob:
                                repository.dialog('2.Armor upgrade (not enough materials)', tempx1, tempx2,tempy1, tempy2, 6, repository.gui_text, window)
                                not_enough_arm = True
                            else:
                                repository.dialog('2.armor upgrade', tempx1, tempx2, tempy1, tempy2, 6, repository.gui_text, window)
                            repository.dialog('(iron: ' + str(armor_cr_ir) + '\\' + str(repository.inventory['iron']) + ', silver: ' + str(armor_cr_sv) + '\\' + str(repository.inventory['silver']) + ', steel: ' + str(armor_cr_st) + '\\' + str(repository.inventory['steel']) + ', mithril: ' + str(armor_cr_mt) + '\\' + str(repository.inventory['mithril']) + ', obsidian: ' + str(armor_cr_ob) + '\\' + str(repository.inventory['obsidian']) + ')', tempx1, tempx2, tempy1, tempy2, 7, repository.gui_text, window)

                            # to choose dialog:
                            temp4 = True
                            while temp4:
                                key = window.getKey()
                                if key == "1" and not not_enough_swd:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                    repository.dialog('Here you go.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                    repository.dialog('Sword LvL + 1.', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                                    repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                                    repository.inventory['sword lvl'] += 1
                                    repository.inventory['iron'] -= sword_cr_ir
                                    repository.inventory['silver'] -= sword_cr_sv
                                    repository.inventory['steel'] -= sword_cr_st
                                    repository.inventory['mithril'] -= sword_cr_mt
                                    repository.inventory['obsidian'] -= sword_cr_ob

                                    temp4_1 = True
                                    while temp4_1:
                                        key = window.getKey()
                                        # close the dialog
                                        if key == "Escape" or key == "Return" or key == "space":
                                            for e in repository.gui_text:
                                                e.undraw()
                                            for e in repository.gui_background:
                                                e.undraw()
                                            for e in repository.gui_sprites:
                                                e.undraw()
                                            repository.mov = True
                                            temp4_1 = temp4 = temp_intro = False

                                elif key == "2" and not not_enough_arm:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                                    repository.dialog('Here you go.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                                    repository.dialog('Armor LvL + 1.', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                                    repository.dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                                    repository.inventory['armor lvl'] += 1
                                    repository.inventory['iron'] -= armor_cr_ir
                                    repository.inventory['silver'] -= armor_cr_sv
                                    repository.inventory['steel'] -= armor_cr_st
                                    repository.inventory['mithril'] -= armor_cr_mt
                                    repository.inventory['obsidian'] -= armor_cr_ob

                                    temp4_1 = True
                                    while temp4_1:
                                        key = window.getKey()
                                        # close the dialog
                                        if key == "Escape" or key == "Return" or key == "space":
                                            for e in repository.gui_text:
                                                e.undraw()
                                            for e in repository.gui_background:
                                                e.undraw()
                                            for e in repository.gui_sprites:
                                                e.undraw()
                                            repository.mov = True
                                            temp4_1 = temp4 = temp_intro = False

                                # close the dialog
                                elif key == "Escape" or key == "Return" or key == "space":
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp4 = temp_intro = False

                        # close the dialog
                        elif key == "Escape" or key == "Return" or temp_intro == False:
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp_intro = False

                elif i.obj_name == "Potions seller":
                    repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                    repository.dialog('What is it?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                    repository.dialog('1.Tell me about yourself.', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                    repository.dialog('2.What have you got for sale?', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)

                    temp_intro = True
                    while temp_intro:
                        key = window.getKey()

                        if key == "1":
                            for e in repository.gui_text:
                                e.undraw()
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('I\'m the Potions seller.', tempx1, tempx2, tempy1, tempy2, 2.5, repository.gui_text, window)

                            # close the dialog
                            temp1 = True
                            while temp1:
                                key = window.getKey()
                                if key == "Escape" or key == "Return" or temp_intro == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp1 = temp_intro = False

                        elif key == "2":
                            no_money = False
                            # items prices lvls
                            if repository.player_lvl <= 10:
                                value_health_25 = 15
                                value_health_50 = 30
                                value_health_75 = 45
                                value_mana = 15
                            elif 10 < repository.player_lvl <= 20:
                                value_health_25 = 120
                                value_health_50 = 240
                                value_health_75 = 360
                                value_mana = 120
                            elif 20 < repository.player_lvl <= 30:
                                value_health_25 = 225
                                value_health_50 = 450
                                value_health_75 = 675
                                value_mana = 225
                            elif 30 < repository.player_lvl <= 40:
                                value_health_25 = 315
                                value_health_50 = 630
                                value_health_75 = 945
                                value_mana = 315
                            elif 40 < repository.player_lvl <= 50:
                                value_health_25 = 450
                                value_health_50 = 900
                                value_health_75 = 1350
                                value_mana = 450
                            elif 50 < repository.player_lvl <= 60:
                                value_health_25 = 600
                                value_health_50 = 1200
                                value_health_75 = 1800
                                value_mana = 600
                            elif 60 < repository.player_lvl <= 70:
                                value_health_25 = 750
                                value_health_50 = 1500
                                value_health_75 = 2250
                                value_mana = 750
                            elif 70 < repository.player_lvl <= 80:
                                value_health_25 = 1050
                                value_health_50 = 2100
                                value_health_75 = 3150
                                value_mana = 1050
                            elif 80 < repository.player_lvl <= 90:
                                value_health_25 = 1500
                                value_health_50 = 3000
                                value_health_75 = 4500
                                value_mana = 1500
                            elif 90 < repository.player_lvl <= 100:
                                value_health_25 = 1950
                                value_health_50 = 3900
                                value_health_75 = 5850
                                value_mana = 1950

                            for e in repository.gui_text:
                                e.undraw()
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('What would you like to buy?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                            # health 25%
                            if repository.inventory['gold'] >= value_health_25:
                                repository.dialog('1.Health potions 25% (' + str(value_health_25) + ' gold each)', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                            else:
                                no_money = True
                                repository.dialog('1.Health potions 25% (not enough gold)', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                            # health 50%
                            if repository.inventory['gold'] >= value_health_50:
                                repository.dialog('2.Health potions 50% (' + str(value_health_50) + ' gold each)', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                            else:
                                no_money = True
                                repository.dialog('2.Health potions 50% (not enough gold)', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                            # health 75%
                            if repository.inventory['gold'] >= value_health_75:
                                repository.dialog('3.Health potions 75% (' + str(value_health_75) + ' gold each)', tempx1, tempx2, tempy1, tempy2, 5.5, repository.gui_text, window)
                            else:
                                no_money = True
                                repository.dialog('3.Health potions 75% (not enough gold)', tempx1, tempx2, tempy1, tempy2, 5.5, repository.gui_text, window)
                            # mana
                            if repository.inventory['gold'] >= value_mana:
                                repository.dialog('4.Mana potions (' + str(value_mana) + 'gold each)', tempx1, tempx2, tempy1, tempy2, 6.5, repository.gui_text, window)
                            else:
                                no_money = True
                                repository.dialog('4.Mana potions (not enough gold)', tempx1, tempx2, tempy1, tempy2, 6.5, repository.gui_text, window)

                            # to choose dialog:s
                            temp2 = True
                            while temp2:
                                key = window.getKey()
                                # first dialog option
                                if temp2:
                                    temp2 = buy_option(i, "1", value_health_25, 'health potions 25%', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # second dialog option
                                if temp2:
                                    temp2 = buy_option(i, "2", value_health_50, 'health potions 50%', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # third dialog option
                                if temp2:
                                    temp2 = buy_option(i, "3", value_health_75, 'health potions 75%', key, no_money, tempx1,  tempx2, tempy1, tempy2, window)

                                # fourth dialog option
                                if temp2:
                                    temp2 = buy_option(i, "4", value_mana, 'mana potions', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # close the dialog
                                if key == "Escape" or key == "Return" or temp2 == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp2 = temp_intro = False
                        # close the dialog
                        if key == "Escape" or key == "Return" or temp_intro == False:
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp1 = temp_intro = False

                elif i.obj_name == "Goods trader":
                    repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                    repository.dialog('What is it?', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                    repository.dialog('1.Tell me about yourself.', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                    repository.dialog('2.What have you got for sale?', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                    repository.dialog('3.I\'d like to sell some things.', tempx1, tempx2, tempy1, tempy2, 5.5, repository.gui_text, window)

                    temp_intro = True
                    while temp_intro:
                        key = window.getKey()
                        if key == "1":
                            for e in repository.gui_text:
                                e.undraw()
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('I\'m the Goods buyer.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)

                            # close the dialog
                            temp1 = True
                            while temp1:
                                key = window.getKey()
                                if key == "Escape" or key == "Return" or temp_intro == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp1 = temp_intro = False

                        # def buy_option(i, dialog_option_1, value, item, dialog_option, no_money, tempx1, tempx2, tempy1, tempy2, window):
                        elif key == "2":
                            for e in repository.gui_text:
                                e.undraw()
                            no_money = False
                            repository.dialog(i.obj_name, tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, window)
                            repository.dialog('What would you like to buy?.', tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, window)
                            if repository.inventory['gold'] > 10:
                                repository.dialog('1.Iron. (10 gold each)', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                            else:
                                repository.dialog('1.Iron. (not enough gold)', tempx1, tempx2, tempy1, tempy2, 3.5, repository.gui_text, window)
                                no_money = True
                            if repository.inventory['gold'] > 25:
                                repository.dialog('2.Silver. (25 gold each)', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                            else:
                                repository.dialog('2.Silver. (not enough gold)', tempx1, tempx2, tempy1, tempy2, 4.5, repository.gui_text, window)
                                no_money = True
                            if repository.inventory['gold'] > 50:
                                repository.dialog('3.Steel. (50 gold each)', tempx1, tempx2, tempy1, tempy2, 5.5, repository.gui_text, window)
                            else:
                                repository.dialog('3.Steel. (not enough gold)', tempx1, tempx2, tempy1, tempy2, 5.5, repository.gui_text, window)
                                no_money = True
                            if repository.inventory['gold'] > 100:
                                repository.dialog('4.Mithril. (100 gold each)', tempx1, tempx2, tempy1, tempy2, 6.5, repository.gui_text, window)
                            else:
                                repository.dialog('4.Mithril. (not enough gold)', tempx1, tempx2, tempy1, tempy2, 6.5, repository.gui_text, window)
                                no_money = True
                            if repository.inventory['gold'] > 200:
                                repository.dialog('5.Obsidian. (200 gold each)', tempx1, tempx2, tempy1, tempy2, 7.5, repository.gui_text, window)
                            else:
                                repository.dialog('5.Obsidian. (not enough gold)', tempx1, tempx2, tempy1, tempy2, 7.5, repository.gui_text, window)
                                no_money = True

                            # to choose dialog:s
                            temp2 = True
                            while temp2:
                                key = window.getKey()
                                # first dialog option
                                if temp2:
                                    temp2 = buy_option(i, "1", 10, 'iron', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # second dialog option
                                if temp2:
                                    temp2 = buy_option(i, "2", 25, 'silver', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # third dialog option
                                if temp2:
                                    temp2 = buy_option(i, "3", 50, 'steel', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # fourth dialog option
                                if temp2:
                                    temp2 = buy_option(i, "4", 100, 'mithril', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # fourth dialog option
                                if temp2:
                                    temp2 = buy_option(i, "5", 200, 'obsidian', key, no_money, tempx1, tempx2, tempy1, tempy2, window)

                                # close the dialog
                                if key == "Escape" or key == "Return" or temp2 == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp2 = temp_intro = False


                            # close the dialog
                            temp1 = True
                            while temp1:
                                key = window.getKey()
                                if key == "Escape" or key == "Return" or temp_intro == False:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp1 = temp_intro = False

                        elif key == "3":
                            for e in repository.gui_text:
                                e.undraw()
                            repository.gui_text.clear()
                            for e in repository.gui_background:
                                e.undraw()

                            # menu inv_background
                            tempx1 = ((repository.resx * 30) // 100)
                            tempy1 = ((repository.resy * 15) // 100)
                            tempx2 = repository.resx - ((repository.resx * 30) // 100)
                            tempy2 = repository.resy - ((repository.resy * 15) // 100)
                            inventory_bc = repository.rectangle(tempx1, tempy1, tempx2, tempy2, "white")
                            inventory_bc.draw(window)
                            repository.gui_background.append(inventory_bc)

                            # inventory
                            n = 1
                            x1 = (tempx1 * 80) // 100
                            x2 = (tempx2 * 80) // 100
                            item_temp = []
                            amount_temp = []
                            for e, a in repository.inventory.items():
                                if e != 'armor lvl' and e != 'sword lvl' and e != 'gold':
                                    repository.dialog(str(n) + "." + str(e) + " : " + str(a), x1, x2, tempy1, tempy2, n, repository.gui_text, window)
                                    item_temp.append(e)
                                    amount_temp.append(a)
                                    n += 1
                                    if n == 25:
                                        x1 = (tempx1 * 120) // 100
                                        x2 = (tempx2 * 120) // 100
                                        n = 1
                            temp3 = True
                            while temp3:
                                n = 1
                                key = window.getKey()
                                for item, amount in zip(item_temp, amount_temp):
                                    if temp3:
                                        temp3 = sell_option(i, str(n), 5, item, amount, key, tempx1, tempx2, tempy1, tempy2, window)
                                    n += 1
                                    # close the dialog
                                if key == "Escape" or key == "Return" or not temp3:
                                    for e in repository.gui_text:
                                        e.undraw()
                                    for e in repository.gui_background:
                                        e.undraw()
                                    for e in repository.gui_sprites:
                                        e.undraw()
                                    repository.mov = True
                                    temp3 = temp_intro = False

                        # close the dialog
                        if key == "Escape" or key == "Return" or temp_intro == False:
                            for e in repository.gui_text:
                                e.undraw()
                            for e in repository.gui_background:
                                e.undraw()
                            for e in repository.gui_sprites:
                                e.undraw()
                            repository.mov = True
                            temp1 = temp_intro = False