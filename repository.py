from graphics import*
import time
import random
import winsound

# variables
npcs = []
npcs_head = []
bcgrnd = []
bcgrndC = []
bcgrndI = []
characters = []
enemies = []
resx = 0
resy = 0
player_spd = 1
gui_menu_bc = []
gui_text = []
gui_background = []
gui_sprites = []
gui_sprites_enemies = []
inventory = {'gold': 0, 'armor lvl': 0, 'sword lvl': 0, 'mana potions': 0, 'health potions 25%': 0, 'health potions 50%': 0, 'health potions 75%': 0, 'iron': 0, 'silver': 0, 'steel': 0, 'mithril': 0, 'obsidian': 0}
is_alive = True
intro = True
mov = True
fled = False
city_map = True
forest_map = False
return_to_city = False
player_lvl = (inventory['armor lvl'] + inventory['sword lvl']) // 2
default_m = 25
enemy_spd = 1
try:
    save = open("save.txt", "r")
    items = save.read()
    inventory = eval(items)
except:
    pass


def option_box(x, window):
    rect = Rectangle(Point(25 + x, 100), Point(125 + x, 150))
    rect.setFill("black")
    rect.draw(window)
    cormouse = x
    return rect, cormouse

def option_1(mouse):
    compx_m_op1 = mouse.getX() > 25 and mouse.getX() < 125
    compy_m_op1 = mouse.getY() > 100 and mouse.getY() < 150
    if compx_m_op1 and compy_m_op1:
        return True

def option_2(mouse):
    compx_m_op2 = mouse.getX() > 150 and mouse.getX() < 250
    compy_m_op2 = mouse.getY() > 100 and mouse.getY() < 150
    if compx_m_op2 and compy_m_op2:
        return True

def option_3(mouse):
    compx_m_op3 = mouse.getX() > 275 and mouse.getX() < 375
    compy_m_op3 = mouse.getY() > 100 and mouse.getY() < 150
    if compx_m_op3 and compy_m_op3:
        return True


def choose_resolution():
    global resx, resy
    x1 = 400
    y1 = 400
    win = GraphWin("Resolution", x1, y1)
    win.setBackground("white")
    text = Text(Point(x1 / 2, y1 / 5) , 'choose your resolution:')
    text.setFill("black")
    text.draw(win)
    text = Text(Point(x1 / 2, y1 * 45 //100), 'Controls:')
    text.setFill("black")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(x1 / 2, y1 * 55 // 100), '\"WASD\" to move;')
    text.setFill("black")
    text.setSize(10)
    text.draw(win)
    text = Text(Point(x1 / 2, y1 * 60 // 100), '\"Space-bar, Enter\", to interact;')
    text.setFill("black")
    text.setSize(10)
    text.draw(win)
    text = Text(Point(x1 / 2, y1 * 65 // 100), '\"1-10\" to choose options displayed;')
    text.setFill("black")
    text.setSize(10)
    text.draw(win)
    text = Text(Point(x1 / 2, y1 * 70 // 100), '\"Esc\" for main menu/save/inventory.')
    text.setFill("black")
    text.setSize(10)
    text.draw(win)
    text = Text(Point(x1 / 2, y1 * 80 // 100), 'This game does NOT use the mouse!')
    text.setFill("black")
    text.setSize(15)
    text.draw(win)

    option_box(0, win)
    text = Text(Point(75, 125) , '1366x768p')
    text.setFill("white")
    text.draw(win)
    option_box(125, win)
    text = Text(Point(200, 125) , '1920x1080p')
    text.setFill("white")
    text.draw(win)
    option_box(250, win)
    text = Text(Point(325, 125) , '2560x1440p')
    text.setFill("white")
    text.draw(win)


    temp = 1
    while temp:
        mouse_click = win.getMouse()
        if option_1(mouse_click):
            temp = 0
            win.close()
            resx = 1350
            resy = 700
        elif option_2(mouse_click):
            temp = 0
            win.close()
            resx = 1550
            resy = 800
        elif option_3(mouse_click):
            temp = 0
            win.close()
            resx = 1950
            resy = 1000


def city_soundtrack(flaga, flagb):
    winsound.PlaySound('soundtracks/city_soundtrack.wav', flaga | flagb)

def forest_soundtrack(flaga, flagb):
    winsound.PlaySound('soundtracks/forest_soundtrack.wav', flaga | flagb)

def combat1_soundtrack(flaga, flagb):
    winsound.PlaySound('soundtracks/combat1.wav', flaga | flagb)

def combat2_soundtrack(flaga, flagb):
    winsound.PlaySound('soundtracks/combat2.wav', flaga | flagb)

def combat3_soundtrack(flaga, flagb):
    winsound.PlaySound('soundtracks/combat3.wav', flaga | flagb)



# function to create rectangles
def rectangle(x1, y1, x2, y2, color):
    rect = Rectangle(Point(x1, y1), Point(x2, y2))
    rect.setFill(color)
    return rect


# display text function
def text(x, y, size, color, window, log):
    text = Text(Point(x, y), log)
    text.undraw()
    text = Text(Point(x, y), log)
    text.setFill(color)
    text.setSize(size)
    text.draw(window)

# class- object on scene
class Object_scene:

    def __init__(self, x1, y1, x2, y2, color, name, width, window):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.obj_name = name
        self.window = window
        self.temp = rectangle(x1, y1, x2, y2, color)
        self.width = width
        # remove outline:
        if self.width == False:
            self.temp.setWidth(0)
        self.temp.draw(window)
        if self.obj_name == 'wolf':
            self.temp_sprite = Image(Point((x1 + x2) // 2, (y1 + y2) // 2), 'sprites/wolf_map.png')
            self.temp_sprite.draw(window)

    # movement function of an object:
    # right
    def char_move_right(self, ammount):
        self.x1 -= default_m * ammount
        self.x2 -= default_m * ammount
        self.temp.move(-default_m * ammount, 0)
        try:
            self.temp_sprite.move(-default_m * ammount, 0)
        except:
            pass

    # left
    def char_move_left(self, ammount):
        self.x1 += default_m * ammount
        self.x2 += default_m * ammount
        self.temp.move(+default_m * ammount, 0)
        try:
            self.temp_sprite.move(+default_m * ammount, 0)
        except:
            pass

    # up
    def char_move_up(self, ammount):
        self.y1 += default_m * ammount
        self.y2 += default_m * ammount
        self.temp.move(0, +default_m * ammount)
        try:
            self.temp_sprite.move(0, +default_m * ammount)
        except:
            pass

    # down
    def char_move_down(self, ammount):
        self.y1 -= default_m * ammount
        self.y2 -= default_m * ammount
        self.temp.move(0, -default_m * ammount)
        try:
            self.temp_sprite.move(0, -default_m * ammount)
        except:
            pass

    # function to remove created object
    def remove_obj(self):
        self.temp.undraw()


# types of objects functions(used for map creation):
# npcs
def crt_npc(x1, y1, x2, y2, color, name, gender, width, window):
    global npcs
    obj = Object_scene(x1, y1, x2, y2, color, name, width, window)
    obj.npc_gender = gender
    npcs.append(obj)

# npc heads
def crt_npc_head(x1, y1, x2, y2, name, width, window, color = ''):
    global npcs_head
    obj = Object_scene(x1, y1, x2, y2, color, name, width, window)
    npcs_head.append(obj)

# enemies
def crt_enemy(x1, y1, x2, y2, color, name, lvl, counter, life, damage, crit_chance, charge_chance, width, window):
    global enemies
    obj = Object_scene(x1, y1, x2, y2, color, name, width, window)
    obj.life = life
    obj.damage = damage
    obj.crit_chance = crit_chance
    obj.charge_chance = charge_chance
    obj.lvl = lvl
    obj.counter = counter
    obj.prey_fled = True
    enemies.append(obj)

# background
def crt_bcgrnd(x1, y1, x2, y2, color, name, width, window):
    global bcgrnd
    obj = Object_scene(x1, y1, x2, y2, color, name, width, window)
    bcgrnd.append(obj)

# background collidables
def crt_bcgrndC(x1, y1, x2, y2, color, name, width, window):
    global bcgrndC
    obj = Object_scene(x1, y1, x2, y2, color, name, width, window)
    bcgrndC.append(obj)

# background interactibles
def crt_bcgrndI( x1, y1, x2, y2, color, name, width, window):
    global bcgrndI
    obj = Object_scene(x1, y1, x2, y2, color, name, width, window)
    bcgrndI.append(obj)

# player create
class Character:
    def __init__(self, x1, y1, x2, y2, color, window):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.life = 100 + (inventory['armor lvl'] * 20)
        self.life_total = self.life
        self.crit_chance = 100
        self.window = window
        self.temp = rectangle(x1, y1, x2, y2, color).draw(window)


    def char_loose_life(self, ammount):
        self.life -= ammount

    # updates the screen to show the player:
    def char_on_screen(self,  window, b):
        self.temp.undraw()
        self.temp.draw(window)



# dialog function
def dialog(speech, x1, x2, y1, y2, number, gui_text, window, font_size = 13):
    global resx, resy
    speech = speech
    if y2 - y1 > resy // 2:
        intro_text = Text(Point(x1 + ((x2 - x1) // 2), y1 + (((y2 - y1) * 2) // 100) * (number * 2)), speech)
    else:
        intro_text = Text(Point(x1 + ((x2 - x1) // 2), y1 + (((y2 - y1) * 4) // 100) * (number * 2)), speech)
    intro_text.setFill("Black")
    intro_text.setSize(font_size)
    intro_text.draw(window)
    gui_text.append(intro_text)

# damage taken animation
def damagetaken(window):
    global gui_sprites
    for e in gui_sprites_enemies:
        e.undraw()
        window.update()
        time.sleep(0.1)
        e.draw(window)
        for a in gui_background:
            a.undraw()
            a.draw(window)
        for i in gui_text:
            i.undraw()
            i.draw(window)
        window.update()
        time.sleep(0.1)
        e.undraw()
        window.update()
        time.sleep(0.1)
        e.draw(window)
    for e in gui_background:
        e.undraw()
        e.draw(window)
    for e in gui_text:
        e.undraw()
        e.draw(window)
    window.update()
    time.sleep(0.1)

# combat
def combat(i, character, window):
    global mov, gui_sprites, gui_background, is_alive, city_map, forest_map

    chance_music = random.randint(1, 3)
    if city_map:
        city_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
    elif forest_map:
        forest_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)

    if chance_music == 1:
        combat1_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
    elif chance_music == 2:
        combat2_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
    elif chance_music == 3:
        combat3_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)

    damage_lvl = inventory['sword lvl']
    player_lvl = (inventory['armor lvl'] + inventory['sword lvl']) // 2
    player_life = int((character.life * 100) // character.life_total)
    enemy_t = i.life
    enemy_life = ((i.life * 100) // enemy_t)
    #character.life = player_lvl * 80
    if i.obj_name == 'wolf':
        wolf_sprite = Image(Point(resx // 2, resy // 2), 'sprites/wolf_combat.png')
        wolf_sprite.draw(window)
        gui_sprites_enemies.append(wolf_sprite)

    # gui battle box creation
    tempx1 = 0
    tempy1 = resy - ((resy * 35) // 100)
    tempx2 = resx
    tempy2 = resy
    text_box = rectangle(tempx1, tempy1, tempx2, tempy2, "white")
    text_box.draw(window)
    gui_background.append(text_box)

    # to choose dialog:
    temp = True
    enemy_charge = False
    stunned = False
    no_intro_dialog = False
    player_crit = False
    enemy_crit = False
    has_charged = False
    enemy_attack = False
    guard = False
    enemy_dmg_tkn = False
    m_consumed_hrgn = 5
    m_consumed_hs = 1
    m_consumed_stun = 5
    m_consumed_ss = 10
    p_lvl_hrgn = 0
    p_lvl_hs = 40
    p_lvl_stun = 60
    p_lvl_ss = 70
    enraged = 30
    timer_er = 0
    timer_gd = 0
    while temp:
        # kill
        if player_life > 1:
            if enemy_dmg_tkn:
                damagetaken(window)
                enemy_dmg_tkn = False
            enemy_life = ((i.life * 100) // enemy_t)
            if enemy_life < 1:
                if chance_music == 1:
                    combat1_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                elif chance_music == 2:
                    combat2_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                elif chance_music == 3:
                    combat3_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)

                if city_map:
                    city_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
                elif forest_map:
                    forest_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)

                for e in gui_text:
                    e.undraw()
                gui_text.clear()
                for e in gui_sprites_enemies:
                    e.undraw()
                n = 0
                if player_life < 1:
                    dialog('The angel of death granted you with max health after the battle!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                    character.life = 100 + (inventory['armor lvl'] * 20)
                    character.life_total = character.life
                    n+= 1
                dialog('The enemy was defeated!', tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                dialog('1.press enter/escape/space-bar to continue', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                if i.obj_name == "wolf":
                    inventory['wolf\'s teeth'] += 1
                if i.obj_name == "boss_forest":
                    inventory['Boss\'s spider heart'] = 1

                # close interaction
                temp1 = True
                while temp1:
                    dialog_option = window.getKey()
                    if dialog_option == "Escape" or dialog_option == "Return" or dialog_option == "Space" or dialog_option == "1":
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        for e in gui_background:
                            e.undraw()
                        i.temp_sprite.undraw()
                        gui_text.clear()
                        gui_background.clear()
                        gui_sprites_enemies.clear()
                        i.remove_obj()
                        enemies.remove(i)
                        mov = True
                        temp = temp1 = False
            else:
                #time.sleep(0.3)
                player_life = int((character.life * 100) // character.life_total)
                enemy_life = ((i.life * 100) // enemy_t)
                if timer_er > 0:
                    timer_er -= 1
                    character.crit_chance = enraged
                else:
                    character.crit_chance = 5
                if timer_gd > 0:
                    timer_gd -= 1
                    pass
                else:
                    guard = False
                if not no_intro_dialog:
                    countered = False
                    n = 0
                    for e in gui_text:
                        e.undraw()
                    gui_text.clear()
                    if player_crit:
                        dialog('You delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                        n += 1
                    elif enemy_crit:
                        dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                        n += 1
                    if enemy_attack:
                        enemy_attack = False
                        if has_charged:
                            has_charged = False
                            if enemy_crit:
                                dialog('The enemy delivered :' + str(int((((i.damage * 2) + i.damage / 2) * 1.5) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                            else:
                                dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                            n += 1
                        else:
                            if enemy_crit:
                                dialog('The enemy delivered :' + str(int((i.damage * 1.5) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                            else:
                                dialog('The enemy delivered :' + str(int((i.damage) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                            n += 1

                    player_life = int((character.life * 100) // character.life_total)
                    dialog('enemy\'s life: ' + str(enemy_life) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                    dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                    if not guard:
                        dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                    else:
                        n -= 1
                    dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)

                    if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                        dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)
                    elif not character.life < character.life_total:
                        n -= 1
                    if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                        dialog('5.Heavy strike (+20% damage strike)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                        dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                        dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)

            dialog_option = window.getKey()
            # first dialog option
            if dialog_option == "1":
                # enemy is able to counter an attack while it charges
                if i.counter and enemy_charge and not stunned:
                    no_intro_dialog = True
                    enemy_charge = False
                    countered = True
                    chance = random.randint(1, 100)
                    n = 0
                    for e in gui_text:
                        e.undraw()
                    gui_text.clear()
                    if chance > i.crit_chance:
                        character.life -= ((i.damage * 2) + i.damage // 2)
                    else:
                        dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 3, gui_text, window)
                        character.life -= int(((i.damage * 2) + i.damage // 2) * 1.5)
                        n += 1
                    if enemy_crit:
                        dialog('The enemy delivered :' + str(int((((i.damage * 2) + i.damage / 2) * 1.5) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        n += 1
                    else:
                        dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        n += 1

                    player_life = int((character.life * 100) // character.life_total)
                    dialog('enemy\'s life: ' + str(enemy_life) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                    dialog('The enemy counters your move!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                    dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                    if not guard:
                        dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                    else:
                        n -= 1
                    dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                    if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                        dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                    elif not character.life < character.life_total:
                        n -= 1
                    if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                        dialog('5.Heavy strike (+20% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                        dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                        dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)



                # normal player attack if no counter
                elif not enemy_charge:
                    no_intro_dialog = False
                    chance = random.randint(1, 100)
                    enemy_dmg_tkn = True
                    if chance > character.crit_chance:
                        player_crit = False
                        i.life -= 20 + 4 * damage_lvl
                    else:
                        player_crit = True
                        i.life -= (20 + 4 * damage_lvl) * 2

                    # attack enemy not stunned
                    if not stunned:
                        # is enemy charging
                        if enemy_charge:
                            enemy_attack = True
                            has_charged = True
                            enemy_charge = False
                            no_intro_dialog = False
                            chance = random.randint(1, 100)
                            if chance > i.crit_chance:
                                enemy_crit = False
                                character.life -= ((i.damage * 2) + i.damage // 2)
                            else:
                                if not player_crit:
                                    enemy_crit = True
                                    character.life -= int(((i.damage * 2) + i.damage // 2) * 1.5)
                                else:
                                    enemy_crit = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)

                        # enemy did not charge
                        elif not enemy_charge:
                            # chance of charge
                            if not countered:
                                chance = random.randint(1, 100)
                            else:
                                chance = 101
                            # normal taken damage
                            if chance > i.charge_chance:
                                enemy_attack = True
                                no_intro_dialog = False
                                chance = random.randint(1, 100)
                                if chance > i.crit_chance:
                                    enemy_crit = False
                                    character.life -= i.damage
                                else:
                                    if not player_crit:
                                        enemy_crit = True
                                        character.life -= (i.damage * 1.5)
                                    else:
                                        enemy_crit = False
                                        character.life -= i.damage

                            # enemy charges, no damage taken
                            else:
                                for e in gui_text:
                                    e.undraw()
                                gui_text.clear()
                                n = 0
                                if player_crit:
                                    dialog('You delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 3, gui_text, window)
                                    n += 1

                                player_life = int((character.life * 100) // character.life_total)
                                dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                                dialog('The enemy is charging an attack!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                                dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                                if not guard:
                                    dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                                else:
                                    n -= 1
                                dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                                if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                                    dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                                elif not character.life < character.life_total:
                                    n -= 1
                                if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                                    dialog('5.Heavy strike (+20% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                                if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                                    dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                                if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                                    dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)
                                enemy_charge = True
                                no_intro_dialog = True


                    # attack enemy stunned
                    else:
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        n = 0
                        if player_crit:
                            dialog('You delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n += 1

                        player_life = int((character.life * 100) // character.life_total)
                        dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                        dialog('The enemy recovered!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                        dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        if not guard:
                            dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                        if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                            dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                        elif not character.life < character.life_total:
                            n -= 1
                        if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                            dialog('5.Heavy strike (+20% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)
                        no_intro_dialog = True
                        stunned = False

            # guard
            if dialog_option == "2" and not guard:
                for e in gui_text:
                    e.undraw()
                gui_text.clear()
                guard = True
                timer_gd = 1
                if enemy_charge == True:

                    player_life = int((character.life * 100) // character.life_total)
                    dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                    dialog('The enemy is stunned!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                    dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3, gui_text, window)
                    dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 4, gui_text, window)
                    n = 0
                    if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                        dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 5, gui_text, window)
                    elif not character.life < character.life_total:
                        n -= 1
                    if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                        dialog('5.Heavy strike (+20% damage strike)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                        dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                    if inventory[ 'mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                        dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)

                    no_intro_dialog = True
                    enemy_charge = False
                    stunned = True
                else:
                    n = 0
                    chance = random.randint(1, 10)
                    if chance < 2:
                        stunned = True
                        dialog('The enemy is stunned!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                    else:
                        dialog('You failed to stun the enemy but block the attack!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)

                    player_life = int((character.life * 100) // character.life_total)
                    dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                    dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3, gui_text, window)
                    dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 4, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                        dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 5, gui_text, window)
                    elif not character.life < character.life_total:
                        n -= 1
                    if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                        dialog('5.Heavy strike (+20% damage strike)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                        dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                    if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                        dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                    no_intro_dialog = True

            # flee combat
            elif dialog_option == "3":
                # guaranteed fled
                if player_lvl >= i.lvl:
                    if chance_music == 1:
                        combat1_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                    elif chance_music == 2:
                        combat2_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                    elif chance_music == 3:
                        combat3_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)

                    if city_map:
                        city_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
                    elif forest_map:
                        forest_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)

                    for e in gui_text:
                        e.undraw()
                    gui_text.clear()
                    for e in gui_background:
                        e.undraw()
                    for e in gui_sprites_enemies:
                        e.undraw()
                    gui_sprites_enemies.clear()

                    mov = True
                    temp = False
                    i.prey_fled = True
                # 50% chance to flee
                elif player_lvl >= i.lvl // 2 and player_lvl < i.lvl:
                    chance = random.randint(1, 10)
                    if chance < i.lvl // 2:
                        if chance_music == 1:
                            combat1_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                        elif chance_music == 2:
                            combat2_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                        elif chance_music == 3:
                            combat3_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)

                        if city_map:
                            city_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
                        elif forest_map:
                            forest_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        for e in gui_background:
                            e.undraw()
                        for e in gui_sprites_enemies:
                            e.undraw()
                        gui_sprites_enemies.clear()

                        mov = True
                        temp = False
                        i.prey_fled = True
                    else:
                        no_intro_dialog = True
                        chance = random.randint(1, 100)
                        if chance > i.crit_chance:
                            enemy_crit = False
                            if enemy_charge:
                                has_charged = True
                                enemy_charge = False
                                character.life -= ((i.damage * 2) + i.damage // 2)
                                enemy_attack = True
                            else:
                                character.life -= i.damage
                                enemy_attack = True
                        else:
                            if not player_crit:
                                enemy_crit = True
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= int(((i.damage * 2) + i.damage // 2) * 1.5)
                                else:
                                    character.life -= int(i.damage * 1.5)
                            else:
                                enemy_crit = False
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                else:
                                    character.life -= i.damage

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        n = 0
                        if enemy_crit:
                            dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n += 1
                        if enemy_attack:
                            enemy_attack = False
                            if has_charged:
                                has_charged = False
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int((((i.damage * 2) + i.damage / 2) * 1.5) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            else:
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(i.damage * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int(i.damage * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1

                        player_life = int((character.life * 100) // character.life_total)
                        dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                        dialog('Escape failed!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                        dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        if not guard:
                            dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                        if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                            dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                        elif not character.life < character.life_total:
                            n -= 1
                        if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                            dialog('5.Heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)

                # 20% chance to flee
                else:
                    chance = random.randint(1, 10)
                    if chance <= 2:
                        if chance_music == 1:
                            combat1_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                        elif chance_music == 2:
                            combat2_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
                        elif chance_music == 3:
                            combat3_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)

                        if city_map:
                            city_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
                        elif forest_map:
                            forest_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        for e in gui_background:
                            e.undraw()
                        for e in gui_sprites_enemies:
                            e.undraw()
                        gui_sprites_enemies.clear()

                        mov = True
                        temp = False
                        i.prey_fled = True
                    else:
                        no_intro_dialog = True
                        chance = random.randint(1, 100)
                        if chance > i.crit_chance:
                            enemy_crit = False
                            if enemy_charge:
                                has_charged = True
                                enemy_charge = False
                                character.life -= ((i.damage * 2) + i.damage // 2)
                                enemy_attack = True
                            else:
                                character.life -= i.damage
                                enemy_attack = True
                        else:
                            if not player_crit:
                                enemy_crit = True
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= int(((i.damage * 2) + i.damage // 2) * 1.5)
                                else:
                                    character.life -= int(i.damage * 1.5)
                            else:
                                enemy_crit = False
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                else:
                                    character.life -= i.damage

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        n = 0
                        if enemy_crit:
                            dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n += 1
                        if enemy_attack:
                            enemy_attack = False
                            if has_charged:
                                has_charged = False
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int((i.damage * 2) + i.damage / 2 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            else:
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(i.damage * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int(i.damage * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1

                        player_life = int((character.life * 100) // character.life_total)
                        dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                        dialog('Escape failed!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                        dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        if not guard:
                            dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                        if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                            dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                        elif not character.life < character.life_total:
                            n -= 1
                        if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                            dialog('5.Heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)

            # Health regen
            elif dialog_option == "4":
                if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        no_intro_dialog = True
                        tempx = inventory['mana potions']
                        tempx -= m_consumed_hrgn
                        inventory['mana potions'] = tempx

                        character.life += character.life_total * 0.3

                        chance = random.randint(1, 100)
                        if chance > i.crit_chance:
                            enemy_crit = False
                            if enemy_charge:
                                has_charged = True
                                enemy_charge = False
                                character.life -= ((i.damage * 2) + i.damage // 2)
                                damage_taken = ((i.damage * 2) + i.damage // 2)
                                enemy_attack = True
                            else:
                                character.life -= i.damage
                                damage_taken = i.damage
                                enemy_attack = True
                        else:
                            if not player_crit:
                                enemy_crit = True
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2) * 1.5
                                    damage_taken = ((i.damage * 2) + i.damage // 2) * 1.5
                                else:
                                    character.life -= i.damage * 1.5
                                    damage_taken = i.damage * 1.5
                            else:
                                enemy_crit = False
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                    damage_taken = ((i.damage * 2) + i.damage // 2)
                                else:
                                    character.life -= i.damage
                                    damage_taken = i.damage

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        n = 0
                        if enemy_crit:
                            dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n += 1
                        if enemy_attack:
                            enemy_attack = False
                            if has_charged:
                                has_charged = False
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int((i.damage * 2) + i.damage / 2 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            else:
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(i.damage * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int(i.damage * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1

                        if character.life > character.life_total:
                            character.life = character.life_total
                        player_life = int((character.life * 100) // character.life_total)
                        dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                        if int(character.life_total * 0.3 - damage_taken) > 0:
                            dialog('You regen ' + str(int(character.life_total * 0.3 - damage_taken)) + ' health points!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        if not guard:
                            dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                        if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                            dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                        elif not character.life < character.life_total:
                            n -= 1
                        if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                            dialog('5.Heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)


                else:
                    no_intro_dialog = False

            # heavy strike
            elif dialog_option == "5":
                if inventory['mana potions'] >= m_consumed_hs:
                    if player_lvl >= p_lvl_hs:

                        chance = random.randint(1, 100)
                        if chance > i.crit_chance:
                            enemy_crit = False
                            if enemy_charge:
                                has_charged = True
                                enemy_charge = False
                                character.life -= ((i.damage * 2) + i.damage // 2)
                                damage_taken = ((i.damage * 2) + i.damage // 2)
                                enemy_attack = True
                            else:
                                character.life -= i.damage
                                damage_taken = i.damage
                                enemy_attack = True
                        else:
                            if not player_crit:
                                enemy_crit = True
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2) * 1.5
                                    damage_taken = ((i.damage * 2) + i.damage // 2) * 1.5
                                else:
                                    character.life -= i.damage * 1.5
                                    damage_taken = i.damage * 1.5
                            else:
                                enemy_crit = False
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                    damage_taken = ((i.damage * 2) + i.damage // 2)
                                else:
                                    character.life -= i.damage
                                    damage_taken = i.damage

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        no_intro_dialog = True
                        tempx = inventory['mana potions']
                        tempx -= m_consumed_hs
                        inventory['mana potions'] = tempx
                        chance = random.randint(1, 100)
                        enemy_dmg_tkn = True
                        if chance > character.crit_chance:
                            player_crit = False
                            i.life -= int((16 + 4 * damage_lvl) + (16 + 4 * damage_lvl) * 0.25)
                        else:
                            player_crit = True
                            i.life -= int(((16 + 4 * damage_lvl) + (16 + 4 * damage_lvl) * 0.25) * 2)

                        if not stunned:
                            chance = random.randint(1, 100)
                            if chance > i.crit_chance:
                                enemy_crit = False
                                if enemy_charge:
                                    has_charged = True
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                    damage_taken = ((i.damage * 2) + i.damage // 2)
                                    enemy_attack = True
                                else:
                                    character.life -= i.damage
                                    damage_taken = i.damage
                                    enemy_attack = True
                            else:
                                if not player_crit:
                                    enemy_crit = True
                                    if enemy_charge:
                                        enemy_charge = False
                                        character.life -= (((i.damage * 2) + i.damage // 2) * 1.5)
                                        damage_taken = (((i.damage * 2) + i.damage // 2) * 1.5)
                                    else:
                                        character.life -= (i.damage * 1.5)
                                        damage_taken = (i.damage * 1.5)
                                else:
                                    enemy_crit = False
                                    if enemy_charge:
                                        enemy_charge = False
                                        character.life -= ((i.damage * 2) + i.damage // 2)
                                        damage_taken = ((i.damage * 2) + i.damage // 2)
                                    else:
                                        character.life -= i.damage
                                        damage_taken = i.damage

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        n = 0
                        if player_crit:
                            dialog('You delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n += 1
                        elif enemy_crit:
                            dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n += 1
                        if enemy_attack:
                            enemy_attack = False
                            if has_charged:
                                has_charged = False
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int((i.damage * 2) + i.damage / 2 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            else:
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(i.damage * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int(i.damage * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1

                        player_life = int((character.life * 100) // character.life_total)
                        dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                        dialog('You do a heavy strike!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                        dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        if not guard:
                            dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                        if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                            dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                        elif not character.life < character.life_total:
                            n -= 1
                        if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                            dialog('5.Heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)

                else:
                    no_intro_dialog = False

            # stun spell
            elif dialog_option == "6":
                if inventory['mana potions'] >= m_consumed_stun:
                    if player_lvl >= p_lvl_stun:
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        no_intro_dialog = True
                        tempx = inventory['mana potions']
                        tempx -= m_consumed_stun
                        inventory['mana potions'] = tempx
                        chance = random.randint(1, 100)
                        if chance <= 45:
                            n = 0
                            player_life = int((character.life * 100) // character.life_total)
                            stunned = True
                            dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                            dialog('The enemy was successfully stunned!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3, gui_text, window)
                            if not guard:
                                dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                            else:
                                n -= 1
                            dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5, gui_text, window)
                            if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                                dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6, gui_text, window)
                            elif not character.life < character.life_total:
                                n -= 1
                            dialog('5.Heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)
                        else:
                            chance = random.randint(1, 100)
                            if chance > i.crit_chance:
                                enemy_crit = False
                                if enemy_charge:
                                    has_charged = True
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                    damage_taken = ((i.damage * 2) + i.damage // 2)
                                    enemy_attack = True
                                else:
                                    character.life -= i.damage
                                    damage_taken = i.damage
                                    enemy_attack = True
                            else:
                                if not player_crit:
                                    enemy_crit = True
                                    if enemy_charge:
                                        enemy_charge = False
                                        character.life -= (((i.damage * 2) + i.damage // 2) * 1.5)
                                        damage_taken = (((i.damage * 2) + i.damage // 2) * 1.5)
                                    else:
                                        character.life -= (i.damage * 1.5)
                                        damage_taken = (i.damage * 1.5)
                                else:
                                    enemy_crit = False
                                    if enemy_charge:
                                        enemy_charge = False
                                        character.life -= ((i.damage * 2) + i.damage // 2)
                                        damage_taken = ((i.damage * 2) + i.damage // 2)
                                    else:
                                        character.life -= i.damage
                                        damage_taken = i.damage

                            n = 0
                            if enemy_crit:
                                dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                                n += 1
                            if enemy_crit:
                                dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            else:
                                dialog('The enemy delivered :' + str(int((i.damage * 2) + i.damage / 2 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            player_life = int((character.life * 100) // character.life_total)
                            dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str(player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                            dialog('You failed to stun the enemy!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                            dialog('1.attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                            if not guard:
                                dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                            else:
                                n -= 1
                            dialog('3.flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)
                            if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                                dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                            elif not character.life < character.life_total:
                                n -= 1
                            dialog('5.heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                            dialog('6.stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)

                else:
                    no_intro_dialog = False

            # enrage
            elif dialog_option == "7":
                pass
                if inventory['mana potions'] >= m_consumed_ss:
                    if player_lvl >= p_lvl_ss and timer_er == 0:
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        no_intro_dialog = True
                        tempx = inventory['mana potions']
                        tempx -= m_consumed_ss
                        inventory['mana potions'] = tempx
                        timer_er = 5

                        chance = random.randint(1, 100)
                        if chance > i.crit_chance:
                            enemy_crit = False
                            if enemy_charge:
                                has_charged = True
                                enemy_charge = False
                                character.life -= ((i.damage * 2) + i.damage // 2)
                                enemy_attack = True
                            else:
                                character.life -= i.damage
                                enemy_attack = True
                        else:
                            if not player_crit:
                                enemy_crit = True
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= int(((i.damage * 2) + i.damage // 2) * 1.5)
                                else:
                                    character.life -= int(i.damage * 1.5)
                            else:
                                enemy_crit = False
                                if enemy_charge:
                                    enemy_charge = False
                                    character.life -= ((i.damage * 2) + i.damage // 2)
                                else:
                                    character.life -= i.damage

                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        if enemy_crit:
                            dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                            n = 1
                        else:
                            n = 0
                        n = 0
                        if player_crit:
                            dialog('You delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2, gui_text,
                                   window)
                            n += 1
                        elif enemy_crit:
                            dialog('The enemy delivered a critical strike!', tempx1, tempx2, tempy1, tempy2, 2,
                                   gui_text, window)
                            n += 1
                        if enemy_attack:
                            enemy_attack = False
                            if has_charged:
                                has_charged = False
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(((i.damage * 2) + i.damage / 2) * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int((i.damage * 2) + i.damage / 2 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1
                            else:
                                if enemy_crit:
                                    dialog('The enemy delivered :' + str(int(i.damage * 1.5 * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                else:
                                    dialog('The enemy delivered :' + str(int(i.damage * 100 / character.life_total)) + ' damage!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                                n += 1

                        player_life = int((character.life * 100) // character.life_total)
                        dialog('enemy\'s life: ' + str((i.life * 100) // enemy_t) + ' / your life: ' + str( player_life) + ' / mana potions: ' + str(inventory['mana potions']), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                        dialog('You can feel the anger!', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
                        dialog('1.Attack', tempx1, tempx2, tempy1, tempy2, 3 + n, gui_text, window)
                        if not guard:
                            dialog('2.Guard (blocks an attack & 10% stunning chance)', tempx1, tempx2, tempy1, tempy2, 4 + n, gui_text, window)
                        else:
                            n -= 1
                        dialog('3.Flee', tempx1, tempx2, tempy1, tempy2, 5 + n, gui_text, window)

                        if inventory['mana potions'] >= m_consumed_hrgn and player_lvl >= p_lvl_hrgn and character.life < character.life_total:
                            dialog('4.Health (+30% health regen)', tempx1, tempx2, tempy1, tempy2, 6 + n, gui_text, window)
                        elif not character.life < character.life_total:
                            n -= 1
                        if inventory['mana potions'] >= m_consumed_hs and player_lvl >= p_lvl_hs:
                            dialog('5.Heavy strike (+25% damage strike)', tempx1, tempx2, tempy1, tempy2, 7 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_stun and player_lvl >= p_lvl_stun:
                            dialog('6.Stun spell (45% success rate)', tempx1, tempx2, tempy1, tempy2, 8 + n, gui_text, window)
                        if inventory['mana potions'] >= m_consumed_ss and player_lvl >= p_lvl_ss and character.crit_chance != enraged:
                            dialog('7.Enrage (30% crit chance for 5 turns)', tempx1, tempx2, tempy1, tempy2, 9 + n, gui_text, window)
                    else:
                        no_intro_dialog = False

        # player death
        else:
            if chance_music == 1:
                combat1_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
            elif chance_music == 2:
                combat2_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)
            elif chance_music == 3:
                combat3_soundtrack(winsound.SND_ASYNC, winsound.SND_PURGE)

            if city_map:
                city_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)
            elif forest_map:
                forest_soundtrack(winsound.SND_ASYNC, winsound.SND_LOOP)

            for e in gui_text:
                e.undraw()
            gui_text.clear()
            if inventory['armor lvl'] > 1 and inventory['sword lvl'] > 1:
                inventory['armor lvl'] -= 1
                inventory['sword lvl'] -= 1
                dialog('Your sword and armor lost a lvl!', tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                character.life = 100 + (inventory['armor lvl'] * 20)
                character.life_total = character.life
                n = 1
            else:
                character.life = 100 + (inventory['armor lvl'] * 20)
                n = 0
            dialog('You died!', tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
            dialog('Press Escape/Return/Space-bar to continue', tempx1, tempx2, tempy1, tempy2, 2 + n, gui_text, window)
            dialog_option = window.getKey()

            # first dialog option
            if dialog_option == "Escape" or dialog_option == "Return" or dialog_option == "Space":
                for e in gui_text:
                    e.undraw()
                gui_text.clear()
                for e in gui_background:
                    e.undraw()
                for e in gui_sprites_enemies:
                    e.undraw()
                i.temp_sprite.undraw()

                mov = True
                temp = False
                is_alive = False


# map movement function
def movement(window, character):
    global mov, inventory, intro, bcgrnd, bcgrndC, bcgrndI, npcs, npcs_head, is_alive, player_lvl, fled, default_m, player_spd, enemy_spd, return_to_city
    player_life = int((character.life * 100) // character.life_total)
    if player_life > 100:
        character.life = character.life_total
        player_life = int((character.life * 100) // character.life_total)
    player_lvl = (inventory['armor lvl'] + inventory['sword lvl']) // 2

    key = (window.getKey()).lower()
    if mov:
        # to go up
        intro = False
        player_sm_mvw = False
        player_sm_mva = False
        player_sm_mvs = False
        player_sm_mvd = False
        tempw = 0
        tempa = 0
        temps = 0
        tempd = 0
        for e in bcgrndC:
            # collison equations w:
            x = character.x1 >= e.x1 - default_m and character.x2 <= e.x2 + default_m
            y = (character.y1 - ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
            y2 = (character.y1 - ((e.y2 - e.y1) // 2)) - default_m == (e.y2 + e.y1) // 2
            if x:
                if player_spd == 2 and y:
                    tempw = 1
                elif player_spd == 2 and y2:
                    player_sm_mvw = True
                elif player_spd == 1 and y:
                    tempw = 1
            # collison equations a:
            y = character.y1 >= e.y1 - default_m and character.y2 <= e.y2 + default_m
            x = (character.x1 - ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
            x2 = (character.x1 - ((e.x2 - e.x1) // 2)) - default_m == (e.x2 + e.x1) // 2
            if y:
                if player_spd == 2 and x:
                    tempa = 1
                elif player_spd == 2 and x2:
                    player_sm_mva = True
                elif player_spd == 1 and x:
                    tempa = 1
            # collison equations s:
            x = character.x1 >= e.x1 - default_m and character.x2 <= e.x2 + default_m
            y = (character.y2 + ((e.y2 - e.y1) // 2))== (e.y2 + e.y1) // 2
            y2 = (character.y2 + ((e.y2 - e.y1) // 2)) + default_m == (e.y2 + e.y1) // 2
            if x:
                if player_spd == 2 and y:
                    temps = 1
                elif player_spd == 2 and y2:
                    player_sm_mvs = True
                elif player_spd == 1 and y:
                    temps = 1
            # collison equations d:
            y = character.y1 >= e.y1 - default_m and character.y2 <= e.y2 + default_m
            x = (character.x2 + ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
            x2 = (character.x2 + ((e.x2 - e.x1) // 2)) + default_m == (e.x2 + e.x1) // 2
            if y:
                if player_spd == 2 and x:
                    tempd = 1
                elif player_spd == 2 and x2:
                    player_sm_mvd = True
                elif player_spd == 1 and x:
                    tempd = 1
        for e in npcs:
            # collison equations w:
            x = character.x1 >= e.x1 - default_m and character.x2 <= e.x2 + default_m
            y = (character.y1 - ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
            y2 = (character.y1 - ((e.y2 - e.y1) // 2)) - default_m == (e.y2 + e.y1) // 2
            if x:
                if player_spd == 2 and y:
                    tempw = 1
                elif player_spd == 2 and y2:
                    player_sm_mvw = True
                elif player_spd == 1 and y:
                    tempw = 1
            # collison equations a:
            y = character.y1 >= e.y1 - default_m and character.y2 <= e.y2 + default_m
            x = (character.x1 - ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
            x2 = (character.x1 - ((e.x2 - e.x1) // 2)) - default_m == (e.x2 + e.x1) // 2
            if y:
                if player_spd == 2 and x:
                    tempa = 1
                elif player_spd == 2 and x2:
                    player_sm_mva = True
                elif player_spd == 1 and x:
                    tempa = 1
            # collison equations s:
            x = character.x1 >= e.x1 - default_m and character.x2 <= e.x2 + default_m
            y = (character.y2 + ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
            y2 = (character.y2 + ((e.y2 - e.y1) // 2)) + default_m == (e.y2 + e.y1) // 2
            if x:
                if player_spd == 2 and y:
                    temps = 1
                elif player_spd == 2 and y2:
                    player_sm_mvs = True
                elif player_spd == 1 and y:
                    temps = 1
            # collison equations d:
            y = character.y1 >= e.y1 - default_m and character.y2 <= e.y2 + default_m
            x = (character.x2 + ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
            x2 = (character.x2 + ((e.x2 - e.x1) // 2)) + default_m == (e.x2 + e.x1) // 2
            if y:
                if player_spd == 2 and x:
                    tempd = 1
                elif player_spd == 2 and x2:
                    player_sm_mvd = True
                elif player_spd == 1 and x:
                    tempd = 1
        for e in enemies:
            # collison equations w:
            x = character.x1 >= e.x1 - default_m and character.x2 <= e.x2 + default_m
            y = (character.y1 - ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
            y2 = (character.y1 - ((e.y2 - e.y1) // 2)) - default_m == (e.y2 + e.y1) // 2
            if x:
                if player_spd == 2 and y:
                    tempw = 1
                elif player_spd == 2 and y2:
                    player_sm_mvw = True
                elif player_spd == 1 and y:
                    tempw = 1
            # collison equations a:
            y = character.y1 >= e.y1 - default_m and character.y2 <= e.y2 + default_m
            x = (character.x1 - ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
            x2 = (character.x1 - ((e.x2 - e.x1) // 2)) - default_m == (e.x2 + e.x1) // 2
            if y:
                if player_spd == 2 and x:
                    tempa = 1
                elif player_spd == 2 and x2:
                    player_sm_mva = True
                elif player_spd == 1 and x:
                    tempa = 1
            # collison equations s:
            x = character.x1 >= e.x1 - default_m and character.x2 <= e.x2 + default_m
            y = (character.y2 + ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
            y2 = (character.y2 + ((e.y2 - e.y1) // 2)) + default_m == (e.y2 + e.y1) // 2
            if x:
                if player_spd == 2 and y:
                    temps = 1
                elif player_spd == 2 and y2:
                    player_sm_mvs = True
                elif player_spd == 1 and y:
                    temps = 1
            # collison equations d:
            y = character.y1 >= e.y1 - default_m and character.y2 <= e.y2 + default_m
            x = (character.x2 + ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
            x2 = (character.x2 + ((e.x2 - e.x1) // 2)) + default_m == (e.x2 + e.x1) // 2
            if y:
                if player_spd == 2 and x:
                    tempd = 1
                elif player_spd == 2 and x2:
                    player_sm_mvd = True
                elif player_spd == 1 and x:
                    tempd = 1

        # if no collision, movement:
        if tempw == 0 and key == "w":
            for e in bcgrndC:
                if player_sm_mvw:
                    Object_scene.char_move_up(e, 1)
                else:
                    Object_scene.char_move_up(e, player_spd)
            for e in bcgrnd:
                if player_sm_mvw:
                    Object_scene.char_move_up(e, 1)
                else:
                    Object_scene.char_move_up(e, player_spd)
            for e in bcgrndI:
                if player_sm_mvw:
                    Object_scene.char_move_up(e, 1)
                else:
                    Object_scene.char_move_up(e, player_spd)
            for e in npcs:
                if player_sm_mvw:
                    Object_scene.char_move_up(e, 1)
                else:
                    Object_scene.char_move_up(e, player_spd)
            for e in npcs_head:
                if player_sm_mvw:
                    Object_scene.char_move_up(e, 1)
                else:
                    Object_scene.char_move_up(e, player_spd)
            for e in enemies:
                if player_sm_mvw:
                    Object_scene.char_move_up(e, 1)
                else:
                    Object_scene.char_move_up(e, player_spd)
            character.char_on_screen(window, True)

        # if no collision, movement:
        if tempa == 0 and key == "a":
            for e in bcgrndC:
                if player_sm_mva:
                    Object_scene.char_move_left(e, 1)
                else:
                    Object_scene.char_move_left(e, player_spd)
            for e in bcgrnd:
                if player_sm_mva:
                    Object_scene.char_move_left(e, 1)
                else:
                    Object_scene.char_move_left(e, player_spd)
            for e in bcgrndI:
                if player_sm_mva:
                    Object_scene.char_move_left(e, 1)
                else:
                    Object_scene.char_move_left(e, player_spd)
            for e in npcs:
                if player_sm_mva:
                    Object_scene.char_move_left(e, 1)
                else:
                    Object_scene.char_move_left(e, player_spd)
            for e in npcs_head:
                if player_sm_mva:
                    Object_scene.char_move_left(e, 1)
                else:
                    Object_scene.char_move_left(e, player_spd)
            for e in enemies:
                if player_sm_mva:
                    Object_scene.char_move_left(e, 1)
                else:
                    Object_scene.char_move_left(e, player_spd)
            character.char_on_screen(window, True)

        # if no collision, movement:
        if temps == 0 and key == "s":
            for e in bcgrndC:
                if player_sm_mvs:
                    Object_scene.char_move_down(e, 1)
                else:
                    Object_scene.char_move_down(e, player_spd)
            for e in bcgrnd:
                if player_sm_mvs:
                    Object_scene.char_move_down(e, 1)
                else:
                    Object_scene.char_move_down(e, player_spd)
            for e in bcgrndI:
                if player_sm_mvs:
                    Object_scene.char_move_down(e, 1)
                else:
                    Object_scene.char_move_down(e, player_spd)
            for e in npcs:
                if player_sm_mvs:
                    Object_scene.char_move_down(e, 1)
                else:
                    Object_scene.char_move_down(e, player_spd)
            for e in npcs_head:
                if player_sm_mvs:
                    Object_scene.char_move_down(e, 1)
                else:
                    Object_scene.char_move_down(e, player_spd)
            for e in enemies:
                if player_sm_mvs:
                    Object_scene.char_move_down(e, 1)
                else:
                    Object_scene.char_move_down(e, player_spd)
            character.char_on_screen(window, True)

        # if no collision, movement:
        if tempd == 0 and key == "d":
            for e in bcgrndC:
                if player_sm_mvd:
                    Object_scene.char_move_right(e, 1)
                else:
                    Object_scene.char_move_right(e, player_spd)
            for e in bcgrnd:
                if player_sm_mvd:
                    Object_scene.char_move_right(e, 1)
                else:
                    Object_scene.char_move_right(e, player_spd)
            for e in bcgrndI:
                if player_sm_mvd:
                    Object_scene.char_move_right(e, 1)
                else:
                    Object_scene.char_move_right(e, player_spd)
            for e in npcs:
                if player_sm_mvd:
                    Object_scene.char_move_right(e, 1)
                else:
                    Object_scene.char_move_right(e, player_spd)
            for e in npcs_head:
                if player_sm_mvd:
                    Object_scene.char_move_right(e, 1)
                else:
                    Object_scene.char_move_right(e, player_spd)
            for e in enemies:
                if player_sm_mvd:
                    Object_scene.char_move_right(e, 1)
                else:
                    Object_scene.char_move_right(e, player_spd)
            character.char_on_screen(window, True)

        elif key == "shift_l":
            if player_spd == 1:
                player_spd = 2
                for i in enemies:
                    i.prey_fled = True
            else:
                player_spd = 1
                for i in enemies:
                    i.prey_fled = True

        elif key == "p":
            character.life -= (character.life_total * 70 // 100)

        # open menu
        elif key == "escape":
            if intro == False:
                mov = False

                # menu background
                tempx1 = ((resx * 40) // 100)
                tempy1 = ((resy * 15) // 100)
                tempx2 = resx - ((resx * 40) // 100)
                tempy2 = resy - ((resy * 15) // 100)
                menu_bc = rectangle(tempx1, tempy1, tempx2, tempy2, "white")
                menu_bc.draw(window)
                gui_menu_bc.append(menu_bc)

                # menu options
                dialog("Health: " + str(player_life) + " / Gold: " + str(inventory['gold']) + " / LVL: " + str(player_lvl), tempx1, tempx2, tempy1, tempy2, 1, gui_text, window)
                dialog("1.close menu", tempx1, tempx2, tempy1, tempy2, 2, gui_text, window)
                dialog("2.Return to city", tempx1, tempx2, tempy1, tempy2, 4, gui_text, window)
                dialog("3.Health potion 25%", tempx1, tempx2, tempy1, tempy2, 5, gui_text, window)
                dialog("4.Health potion 50%", tempx1, tempx2, tempy1, tempy2, 6, gui_text, window)
                dialog("5.Health potion 75%", tempx1, tempx2, tempy1, tempy2, 7, gui_text, window)
                dialog("6.open inventory", tempx1, tempx2, tempy1, tempy2, 8, gui_text, window)
                dialog("7.save inventory", tempx1, tempx2, tempy1, tempy2, 9.5, gui_text, window)
                dialog("8.load inventory", tempx1, tempx2, tempy1, tempy2, 10.5, gui_text, window)
                dialog("9.close game", tempx1, tempx2, tempy1, tempy2, 11.5, gui_text, window)

                temp = True
                while temp:
                    key = window.getKey()
                    if key == "9":
                        window.close()

                    elif key == "6":
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        menu_bc.undraw()

                        # menu inv_background
                        tempx1 = ((resx * 30) // 100)
                        tempy1 = ((resy * 15) // 100)
                        tempx2 = resx - ((resx * 30) // 100)
                        tempy2 = resy - ((resy * 15) // 100)
                        menu_bc = rectangle(tempx1, tempy1, tempx2, tempy2, "white")
                        menu_bc.draw(window)
                        gui_menu_bc.append(menu_bc)

                        n = 1
                        x1 = (tempx1 * 80) // 100
                        x2 = (tempx2 * 80) // 100
                        for e, i in inventory.items():
                            dialog(str(e) + " : " + str(i), x1, x2, tempy1, tempy2, n, gui_text, window)
                            n += 1
                            if n == 25:
                                x1 = (tempx1 * 120) // 100
                                x2 = (tempx2 * 120) // 100
                                n = 1

                        # close menu
                        temp = True
                        while temp:
                            key = window.getKey()
                            if key == "Escape" or key == "Return":
                                menu_bc.undraw()
                                mov = True
                                temp = False
                                for e in gui_text:
                                    e.undraw()
                                gui_text.clear()

                    elif key == "7":
                        save = open("save.txt", "w+")
                        save.write(str(inventory))

                        # close menu
                        menu_bc.undraw()
                        mov = True
                        temp = False
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()

                    elif key == "8":
                        try:
                            save = open("save.txt", "r")
                            items = save.read()
                            inventory = eval(items)
                        except:
                            pass

                        # close menu
                        menu_bc.undraw()
                        mov = True
                        temp = False
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()

                    elif key == "1" or key == "Escape" or key == "Return":
                        #close menu
                        menu_bc.undraw()
                        mov = True
                        temp = False
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()

                    elif key == "2":
                        menu_bc.undraw()
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        return_to_city = True
                        mov = True
                        temp = False

                    elif key == "3":
                        menu_bc.undraw()
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        character.life += character.life_total * 0.25
                        temp = False
                        mov = True

                    elif key == "4":
                        menu_bc.undraw()
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        character.life += character.life_total * 0.5
                        mov = True
                        temp = False

                    elif key == "4":
                        menu_bc.undraw()
                        for e in gui_text:
                            e.undraw()
                        gui_text.clear()
                        character.life += character.life_total * 0.75
                        mov = True
                        temp = False


        # enemy movement
        stop = 0
        temp = 1
        tempw = 0
        tempa = 0
        temps = 0
        tempd = 0
        enemy_sm_mvw = False
        enemy_sm_mva = False
        enemy_sm_mvs = False
        enemy_sm_mvd = False
        for i in enemies:
            chance_movement = random.randint(1, 20 )

            # player collision
            # "w"
            pxw = i.x1 >= character.x1 - default_m and i.x2 <= character.x2 + default_m
            pyw = (i.y1 - ((character.y2 - character.y1) // 2)) == (character.y2 + character.y1) // 2
            pyw2 = (i.y1 - ((character.y2 - character.y1) // 2)) - default_m == (character.y2 + character.y1) // 2
            # "a"
            pya = i.y1 >= character.y1 - default_m and i.y2 <= character.y2 + default_m
            pxa = (i.x1 - ((character.x2 - character.x1) // 2)) == (character.x2 + character.x1) // 2
            pxa2 = (i.x1 - ((character.x2 - character.x1) // 2)) - default_m == (character.x2 + character.x1) // 2
            # "s"
            pxs = i.x1 >= character.x1 - default_m and i.x2 <= character.x2 + default_m
            pys = (i.y2 + ((character.y2 - character.y1) // 2)) == (character.y2 + character.y1) // 2
            pys2 = (i.y2 + ((character.y2 - character.y1) // 2)) + default_m == (character.y2 + character.y1) // 2
            # "d"
            pyd = i.y1 >= character.y1 -default_m and i.y2 <= character.y2 + default_m
            pxd = (i.x2 + ((character.x2 - character.x1) // 2)) == (character.x2 + character.x1) // 2
            pxd2 = (i.x2 + ((character.x2 - character.x1) // 2)) + default_m == (character.x2 + character.x1) // 2

            if (pxw and pyw) or (pxa and pya) or (pxs and pys) or (pxd and pyd):
                mov = False
                combat(i, character, window)
                stop = 1
                break

            for e in bcgrndC:
                # collison equations w:
                x = i.x1 >= e.x1 - default_m and i.x2 <= e.x2 + default_m
                y = (i.y1 - ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
                y2 = (i.y1 - ((e.y2 - e.y1) // 2)) - default_m == (e.y2 + e.y1) // 2
                if x:
                    if enemy_spd == 2 and y:
                        tempw = 1
                    elif enemy_spd == 2 and y2:
                        enemy_sm_mvw = True
                    elif enemy_spd == 1 and y:
                        tempw = 1
                # collison equations a:
                y = i.y1 >= e.y1 - default_m and i.y2 <= e.y2 + default_m
                x = (i.x1 - ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
                x2 = (i.x1 - ((e.x2 - e.x1) // 2)) - default_m == (e.x2 + e.x1) // 2
                if y:
                    if enemy_spd == 2 and x:
                        tempa = 1
                    elif enemy_spd == 2 and x2:
                        enemy_sm_mva = True
                    elif enemy_spd == 1 and x:
                        tempa = 1
                # collison equations s:
                x = i.x1 >= e.x1 - default_m and i.x2 <= e.x2 + default_m
                y = (i.y2 + ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
                y2 = (i.y2 + ((e.y2 - e.y1) // 2)) + default_m == (e.y2 + e.y1) // 2
                if x:
                    if enemy_spd == 2 and y:
                        temps = 1
                    elif enemy_spd == 2 and y2:
                        enemy_sm_mvs = True
                    elif enemy_spd == 1 and y:
                        temps = 1
                # collison equations d:
                y = i.y1 >= e.y1 - default_m and i.y2 <= e.y2 + default_m
                x = (i.x2 + ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
                x2 = (i.x2 + ((e.x2 - e.x1) // 2)) + default_m == (e.x2 + e.x1) // 2
                if y:
                    if enemy_spd == 2 and x:
                        tempd = 1
                    elif enemy_spd == 2 and x2:
                        enemy_sm_mvd = True
                    elif enemy_spd == 1 and x:
                        tempd = 1

            for e in enemies:
                if e != i:
                    # collison equations w:
                    x = i.x1 >= e.x1 - default_m and i.x2 <= e.x2 + default_m
                    y = (i.y1 - ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
                    y2 = (i.y1 - ((e.y2 - e.y1) // 2)) - default_m == (e.y2 + e.y1) // 2
                    if x:
                        if enemy_spd == 2 and y:
                            tempw = 1
                        elif enemy_spd == 2 and y2:
                            enemy_sm_mvw = True
                        elif enemy_spd == 1 and y:
                            tempw = 1
                    # collison equations a:
                    y = i.y1 >= e.y1 - default_m and i.y2 <= e.y2 + default_m
                    x = (i.x1 - ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
                    x2 = (i.x1 - ((e.x2 - e.x1) // 2)) - default_m == (e.x2 + e.x1) // 2
                    if y:
                        if enemy_spd == 2 and x:
                            tempa = 1
                        elif enemy_spd == 2 and x2:
                            enemy_sm_mva = True
                        elif enemy_spd == 1 and x:
                            tempa = 1
                    # collison equations s:
                    x = i.x1 >= e.x1 - default_m and i.x2 <= e.x2 + default_m
                    y = (i.y2 + ((e.y2 - e.y1) // 2)) == (e.y2 + e.y1) // 2
                    y2 = (i.y2 + ((e.y2 - e.y1) // 2)) + default_m == (e.y2 + e.y1) // 2
                    if x:
                        if enemy_spd == 2 and y:
                            temps = 1
                        elif enemy_spd == 2 and y2:
                            enemy_sm_mvs = True
                        elif enemy_spd == 1 and y:
                            temps = 1
                    # collison equations d:
                    y = i.y1 >= e.y1 - default_m and i.y2 <= e.y2 + default_m
                    x = (i.x2 + ((e.x2 - e.x1) // 2)) == (e.x2 + e.x1) // 2
                    x2 = (i.x2 + ((e.x2 - e.x1) // 2)) + default_m == (e.x2 + e.x1) // 2
                    if y:
                        if enemy_spd == 2 and x:
                            tempd = 1
                        elif enemy_spd == 2 and x2:
                            enemy_sm_mvd = True
                        elif enemy_spd == 1 and x:
                            tempd = 1

            # player near check
            length = (character.x2 - character.x1)
            height = (character.y2 - character.y1)
            pdy_u = (i.y1) <= (character.y1 + (height * 4)) and (i.y2) - default_m > character.y2
            pdx_l = (i.x1) <= (character.x1 + (length * 4)) and (i.x2) - default_m > character.x2
            pdy_d = (i.y2) >= (character.y1 - (height * 4)) and (i.y1) + default_m < character.y1
            pdx_r = (i.x2) >= (character.x2 - (length * 4)) and (i.x1) + default_m < character.x1

            if (pxw and pdy_u) or (pya and pdx_l) or (pxw and pdy_d) or (pyd and pdx_r) or (pdy_u and pdx_l) or (pdy_u and pdx_r) or (pdy_d and pdx_l) or (pdy_d and pdx_r):
                enemy_spd = 2
                temp = 1
                if not stop and not i.prey_fled:
                    chance = random.randint(1, 10)
                    if chance < 8:
                        if tempw == 0:
                            if pdy_u and pyw2:
                                Object_scene.char_move_down(i, 1)
                            elif pxw and pdy_u:
                                Object_scene.char_move_down(i, 2)
                        if tempa == 0:
                            if pya and pxa2:
                                Object_scene.char_move_right(i, 1)
                            elif pya and pdx_l:
                                Object_scene.char_move_right(i, 2)
                        if temps == 0:
                            if pxw and pys2:
                                Object_scene.char_move_up(i, 1)
                            elif pxw and pdy_d:
                                Object_scene.char_move_up(i, 2)
                        if tempd == 0:
                            if pyd and pxd2:
                                Object_scene.char_move_left(i, 1)
                            if pyd and pdx_r:
                                Object_scene.char_move_left(i, 2)
                        if pdy_u and pdx_l:
                            chance = random.randint(1, 2)
                            if chance == 1:
                                if tempw == 0:
                                    if enemy_sm_mvs:
                                        Object_scene.char_move_down(i, 1)
                                    else:
                                        Object_scene.char_move_down(i, 2)
                                elif tempa == 0:
                                    if enemy_sm_mvd:
                                        Object_scene.char_move_right(i, 1)
                                    else:
                                        Object_scene.char_move_right(i, 2)
                            else:
                                if tempa == 0:
                                    if enemy_sm_mvd:
                                        Object_scene.char_move_right(i, 1)
                                    else:
                                        Object_scene.char_move_right(i, 2)
                                elif tempw == 0:
                                    if enemy_sm_mvs:
                                        Object_scene.char_move_down(i, 1)
                                    else:
                                        Object_scene.char_move_down(i, 2)
                        if pdy_u and pdx_r:
                            chance = random.randint(1, 2)
                            if chance == 1:
                                if tempw == 0:
                                    if enemy_sm_mvs:
                                        Object_scene.char_move_down(i, 1)
                                    else:
                                        Object_scene.char_move_down(i, 2)
                                elif tempd == 0:
                                    if enemy_sm_mva:
                                        Object_scene.char_move_left(i, 1)
                                    else:
                                        Object_scene.char_move_left(i, 2)
                            else:
                                if tempd == 0:
                                    if enemy_sm_mva:
                                        Object_scene.char_move_left(i, 1)
                                    else:
                                        Object_scene.char_move_left(i, 2)
                                elif tempw == 0:
                                    if enemy_sm_mvs:
                                        Object_scene.char_move_down(i, 1)
                                    else:
                                        Object_scene.char_move_down(i, 2)
                        if pdy_d and pdx_l:
                            chance = random.randint(1, 2)
                            if chance == 1:
                                if temps == 0:
                                    if enemy_sm_mvw:
                                        Object_scene.char_move_up(i, 1)
                                    else:
                                        Object_scene.char_move_up(i, 2)
                                elif tempa == 0:
                                    if enemy_sm_mvd:
                                        Object_scene.char_move_right(i, 1)
                                    else:
                                        Object_scene.char_move_right(i, 2)
                            else:
                                if tempa == 0:
                                    if enemy_sm_mvd:
                                        Object_scene.char_move_right(i, 1)
                                    else:
                                        Object_scene.char_move_right(i, 2)
                                elif temps == 0:
                                    if enemy_sm_mvw:
                                        Object_scene.char_move_up(i, 1)
                                    else:
                                        Object_scene.char_move_up(i, 2)
                        if pdy_d and pdx_r:
                            chance = random.randint(1, 2)
                            if chance == 1:
                                if temps == 0:
                                    if enemy_sm_mvw:
                                        Object_scene.char_move_up(i, 1)
                                    else:
                                        Object_scene.char_move_up(i, 2)
                                elif tempd == 0:
                                    if enemy_sm_mva:
                                        Object_scene.char_move_left(i, 1)
                                    else:
                                        Object_scene.char_move_left(i, 2)
                            else:
                                if tempd == 0:
                                    if enemy_sm_mva:
                                        Object_scene.char_move_left(i, 1)
                                    else:
                                        Object_scene.char_move_left(i, 2)
                                elif temps == 0:
                                    if enemy_sm_mvw:
                                        Object_scene.char_move_up(i, 1)
                                    else:
                                        Object_scene.char_move_up(i, 2)
                else:
                    i.prey_fled = False
            else:
                enemy_spd = 1
                temp = 0

            # if no collision, movement:
            if temp == 0:
                if tempw == 0:
                    if chance_movement == 1:
                        Object_scene.char_move_down(i, 1)

                if tempa == 0:
                    if chance_movement == 2:
                        Object_scene.char_move_right(i, 1)

                if temps == 0:
                    if chance_movement == 3:
                        Object_scene.char_move_up(i, 1)

                if tempd == 0:
                    if chance_movement == 4:
                        Object_scene.char_move_left(i, 1)

            # player collision
            # "w"
            pxw = i.x1 >= character.x1 and i.x2 <= character.x2
            pyw = (i.y1 - ((character.y2 - character.y1) // 2)) == (character.y2 + character.y1) // 2
            # "a"
            pya = i.y1 >= character.y1 and i.y2 <= character.y2
            pxa = (i.x1 - ((character.x2 - character.x1) // 2)) == (character.x2 + character.x1) // 2
            # "s"
            pxs = i.x1 >= character.x1 and i.x2 <= character.x2
            pys = (i.y2 + ((character.y2 - character.y1) // 2)) == (character.y2 + character.y1) // 2
            # "d"
            pyd = i.y1 >= character.y1 and i.y2 <= character.y2
            pxd = (i.x2 + ((character.x2 - character.x1) // 2)) == (character.x2 + character.x1) // 2

            if (pxw and pyw) or (pxa and pya) or (pxs and pys) or (pxd and pyd):
                mov = False
                combat(i, character, window)
                break





    # returns pressed key
    return key


