import repository
from graphics import*
import maps
import interactions





#1950/1000
#1450/1000
#1050/650
# screen creationd
repository.choose_resolution()
background = color_rgb(46, 125, 2)
win = GraphWin("prototype-1", repository.resx, repository.resy, autoflush=False)
win.setBackground(background)
# player creation, initial map
player = repository.Character((repository.resx // 2) - 25, (repository.resy // 2) - 25, (repository.resx // 2) + 25, (repository.resy // 2) + 25, "black", win)
maps.city(True, win)
player.char_on_screen(win, True)

# menu background
tempx1 = ((repository.resx * 18) // 100)
tempy1 = ((repository.resy * 10) // 100)
tempx2 = repository.resx - ((repository.resx * 18) // 100)
tempy2 = repository.resy - ((repository.resy * 10) // 100)
menu_bc = repository.rectangle(tempx1, tempy1, tempx2, tempy2, color_rgb(223, 144, 65))
menu_bc.draw(win)
repository.gui_menu_bc.append(menu_bc)

# menu optionsa
repository.dialog("Tutorial", tempx1, tempx2, tempy1, tempy2, 1, repository.gui_text, win, 35)
repository.dialog("(dpress wasd to continue)", tempx1, tempx2, tempy1, tempy2, 2, repository.gui_text, win, 10)
repository.dialog(" You are an adventurer looking for treasure and making a name for yourself,", tempx1, tempx2, tempy1, tempy2, 3, repository.gui_text, win)
repository.dialog("on your travels you end up in Gatlinham, the capital of the kingdom.", tempx1, tempx2, tempy1, tempy2, 4, repository.gui_text, win)
repository.dialog("1.Go to the city gates to travel the land.", tempx1, tempx2, tempy1, tempy2, 6, repository.gui_text, win)
repository.dialog("2.Get quests and trade by speaking to npcs.", tempx1, tempx2, tempy1, tempy2, 7, repository.gui_text, win)
repository.dialog("3.Defeat enemies to gather resources for quests and upgrades.", tempx1, tempx2, tempy1, tempy2, 8, repository.gui_text, win)
repository.dialog("4.Comsplete quests to get money and defeat bosses to unlock new areas.", tempx1, tempx2, tempy1, tempy2, 9, repository.gui_text, win)
repository.dialog("5.The objective of the game is to kill the Dragon Lord who's terrorizing the Kingdom.", tempx1, tempx2, tempy1, tempy2, 10, repository.gui_text, win)
logo = Image(Point(repository.resx * 60 // 100, repository.resy * 58 // 100), 'sprites/castle.png')
logo.draw(win)
repository.gui_sprites.append(logo)
logo = Image(Point(repository.resx * 40 // 100, repository.resy * 53 // 100), 'sprites/dragon.png')
logo.draw(win)
repository.gui_sprites.append(logo)
logo = Image(Point(repository.resx * 50 // 100, repository.resy * 60 // 100), 'sprites/fighting-knight.png')
logo.draw(win)
repository.gui_sprites.append(logo)
repository.dialog("Esse jogo foi uma colaboração de:", tempx1, tempx2, tempy1, tempy2, 20, repository.gui_text, win)
repository.dialog("Davi Albuquerque Bitencourt", tempx1, tempx2, tempy1, tempy2, 21, repository.gui_text, win)
repository.dialog("Jaco Viado", tempx1, tempx2, tempy1, tempy2, 22, repository.gui_text, win)
repository.dialog("Davi inferior", tempx1, tempx2, tempy1, tempy2, 23, repository.gui_text, win)

# game running:
while True:
    interactions.inter(win, player)