import repository
from graphics import*

# ------CITY------------------------------------------------------------------------------------------------------------

house = '#503B00'
house2 = '#3A2B00'
warehouse = '#3A3838'
warehouse2 = '#424040'
warehouse3 = '#504E4E'
warehouse4 = '#575555'
#tree = color_rgb(32, 96, 0)
tree = '#256000'
path = "gray"
castle = color_rgb(96, 96, 96)
male = '#0070C0'
female = 'pink'
# tree = "#006400"
tent1 = '#EEB500'
tent2 ='#960000'
tent3 = '#001642'
stonewell = '#424040'
waterwell = '#203764'
square ='#F2CB96'
wheat = '#FFC611'
bridge = '#604700'
bridge2 = '#423100'
invis_wall = ''
dirt = '#6F452D'

# ----------------------------------------------------------------------------------------------------------------------

castle_wall_1 = '#3A3838'
castle_wall_2 = '#5E5A5A'
castle_defense = '#262626'
castle_tower_1 = '#404040'
castle_tower_2 = '#534F4F'

castle_foundation = '#7B7B7B'
castle_smudge = '#6D6D6D'
thing = '#503B00'

castle_roof_1 = '#3A2B00'
castle_roof_2 = '#423100'
castle_roof_3 = '#503B00'
castle_roof_4 = '#543E00'
castle_roof_5 = '#604700'

tower_roof_1 = '#B00000'
tower_roof_2 = '#A40000'
tower_roof_3 = '#9A0000'
tower_roof_4 = '#860000'

# ----------------------------------------------------------------------------------------------------------------------

fr_house_ceilling1 = "#725747"
fr_house_ceilling2 = "#654D3F"
fr_house_ceilling3 = "#533E33"
fr_house_ceilling4 = "#3E2E26"
water1 = '#7C9CD6'
water2 = '#5F86CD'
water3 = '#3A68BC'
water4 = '#305496'
sand = '#F9CE6B'
stone= '#3A3838'
stripe= '#AEACAC'

# ----------FOREST------------------------------------------------------------------------------------------------------
waterL1 = '#3E6CC0'
waterL2 = '#3760AB'
waterL3 = '#305496'
FFstone_foundation = '#808080'
FFstone_walls = '#5B5959'
palm_tree = '#2B7000'
random_stone = '#3A3838'
cave_fr = '#3A3838'
bandit_tent1 = '#BF8F00'
bandit_tent2 = '#806000'
coal = 'black'

# ----------CAVE--------------------------------------------------------------------------------------------------------
cave_wall = '#180D08'
cave_floor = '#27160D'
cave_floor_2 = '#23130B'
void = '#000000'

cave_water1 = '#132F49'
cave_water2 = '#102940'
cave_water3 = '#0C2032'

dungeon_floor = '#3A3838'
dungeon_wall = '#1F1F1F'
dungeon_bricks_2E = '#2E2E2E'
dungeon_bricks_26 = '#262626'

red_46 = '#460000'
red_58 = '#580000'
white_light = '#A6A6A6'
white_dark = '#808080'
brown_32 = '#321C10'
brown_27 = '#27160D'

esmeralda_cave = '#203315'
ouro_cave = '#7A5A00'
rubi_cave = '#460000'

mineshaft1_cave = '#221814'
mineshaft2_cave = '#271C17'
mineshaft3_cave = '#2D211B'

# ----------MANSION-----------------------------------------------------------------------------------------------------
gate_1 = '#161616'
gate_2 = '#343232'
gate_3 = '#3A3838'

dirt_path = '#62463C'
road_mansion = '#858585'
roses = '#C00000'
violets = '#A274EE'
yellow_flower = '#FFCC67'
white_flower = '#F2F2F2'
grave_stone = '#454545'

labirinto = '#215600'

mansion_wall = '#2D201B'
mansion_floor = '#49362D'
mansion_wool1 = '#460000'
mansion_wool2 = '#580000'
mansion_stair1 = '#2D201B'
mansion_stair2 = '#372721'
mansion_stair3 = '#3E2D26'
mansion_stair4 = '#4E4C4C'
mansion_stair5 = '#444242'
mansion_stair6 = '#3A3838'
mansion_stair7 = '#32231E'
mansion_stair8 = '#343232'

shed1 = '#4C362E'
shed2 = '#412E27'
shed3 = '#382822'

mansion_bookcase = '#382822'
mansion_plates = '#BFBFBF'
mansion_dark_red = '#460000'
mansion_light_red = '#580000'
mansion_grey1 = '#262626'
mansion_grey2 = '#202020'
mansion_grey3 = '#303030'
mansion_piano1 = '#191919'
mansion_piano2 = '#1D1D1D'
mansion_notes1 = '#D9D9D9'
mansion_notes2 = '#BFBFBF'

# ----DESTROYED VILLAGE-------------------------------------------------------------------------------------------------
tree_dv = '#205500'
dv_dirt_path = '#503D32'#5D483B
background = '#256000'

wheat_1 = '#967200'
wheat_2 = '#9A7500'

water_1 = '#3E6CC0'
water_2 = '#3760AB'
water_3 = '#305496'
water_4 = '#2E508E'
water_5 = '#2D4E89'

wood_1 = '#2D201B'
wood_2 = '#382822'
wood_3 = '#412E27'

stone_base = '#3A3838'
stone_debris = '#2E2E2E'
stone_house_wall = '#1F1F1F'

pentagram = '#A60000'
lava_1 = '#FF3300' #vermelho
lava_2 = '#FF4401' #verde
lava_3 = '#FD6203' #azul
lava_4 = '#FF7B00' #roxo
lava_5 = '#FF8C01' #preto
lava_6 = '#FFAA01' #amarelo

# ----HELL--------------------------------------------------------------------------------------------------------------
background_hell = '#451100'
hell_rocks = '#360D00'

ground_hell_1 = '#4F1400'
ground_hell_2 = '#591700'
ground_hell_dungeon = '#360D00'
walls_hell_dungeon = '#2E0D00'


# repository.winsound.SND_ASYNC
# repository.winsound.SND_LOOP
# repository.winsound.SND_PURGE

def full_npc(x1, y1, x2, y2, name, gender, window):
    repository.crt_npc(x1, y1, x2, y2, gender, name, str(gender), True, window)
    repository.crt_npc_head(x1 + 12, y1 + 12, x2 - 12, y2 - 12, name + "_head", True, window)

# map city function
def city(b, window):
    global house, path, castle
    if b:
        repository.city_map = True
        repository.forest_map = False
        try:
            repository.forest_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_PURGE)
        except:
            pass
        repository.city_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_LOOP)
        # clearing the screen for new map:
        for e in repository.npcs:
            e.remove_obj()
        repository.npcs.clear()
        for e in repository.npcs_head:
            e.remove_obj()
        repository.npcs_head.clear()
        for e in repository.bcgrnd:
            e.remove_obj()
        repository.bcgrnd.clear()
        for e in repository.bcgrndC:
            e.remove_obj()
        repository.bcgrndC.clear()
        for e in repository.bcgrndI:
            e.remove_obj()
        repository.bcgrndI.clear()
        for e in repository.enemies:
            try:
                e.remove_obj()
            except:
                pass
        repository.enemies.clear()

        # city wall
        repository.crt_bcgrndC(-350, -75, -200, 2325, castle, "castle_wall_w", True, window)
        repository.crt_bcgrnd(-350, -75, -300, 2325, castle_wall_1, "castle_wall_decor1_w", True, window)
        repository.crt_bcgrnd(-300, -75, -250, -25, castle_wall_1, "castle_wall_decor2_w", True, window)
        repository.crt_bcgrnd(-250, -75, -200, 2225, castle_wall_1, "castle_wall_decor3_w", True, window)

        repository.crt_bcgrndC(-200, 2175, 550, 2275, castle, "castle_wall_s1", True, window)
        repository.crt_bcgrnd(-200, 2175, 550, 2225, castle_wall_1, "castle_wall_decor1_s1", True, window)
        repository.crt_bcgrnd(500, 2225, 550, 2275, castle_wall_1, "castle_wall_decor2_s1", True, window)

        repository.crt_bcgrndC(550, 2275, 700, 2325, invis_wall, "castle_wall_s1/s2", False, window)

        repository.crt_bcgrndC(700, 2175, 1700, 2275, castle, "castle_wall_s2", True, window)
        repository.crt_bcgrnd(700, 2175, 1600, 2225, castle_wall_1, "castle_wall_decor1_s2", True, window)
        repository.crt_bcgrnd(700, 2225, 750, 2275, castle_wall_1, "castle_wall_decor2_s2", True, window)
        repository.crt_bcgrnd(-300, 2275, 1700, 2325, castle_wall_1, "castle_wall_decor3_s", True, window)

        repository.crt_bcgrndC(1600, -75, 1750, 2175, castle, "castle_wall_e", True, window)
        repository.crt_bcgrnd(1600, -75, 1650, 2225, castle_wall_1, "castle_wall_decor1_e", True, window)
        repository.crt_bcgrnd(1650, -75, 1700, -25, castle_wall_1, "castle_wall_decor2_e", True, window)
        repository.crt_bcgrnd(1700, -75, 1750, 2325, castle_wall_1, "castle_wall_decor3_e", True, window)

        # houses
        repository.crt_bcgrndC(350, 175, 500, 475, house, "random_house_1", True, window)
        repository.crt_bcgrnd(400, 175, 450, 475, house2, "random_house_1,2", True, window)

        repository.crt_bcgrndC(0, 175, 150, 625, house, "random_house_2", True, window)
        repository.crt_bcgrnd(50, 175, 100, 625, house2, "random_house_2,2", True, window)

        repository.crt_bcgrndC(0, 775, 150, 1125, house, "random_house_3", True, window)
        repository.crt_bcgrnd(50, 775, 100, 1125, house2, "random_house_3,2", True, window)

        repository.crt_bcgrndC(350, 625, 500, 925, house, "random_house_4", True, window)
        repository.crt_bcgrnd(400, 625, 450, 925, house2, "random_house_4,2", True, window)

        repository.crt_bcgrndC(300, 1125, 500, 1375, house, "random_house_5", True, window)
        repository.crt_bcgrnd(350, 1125, 450, 1375, house2, "random_house_5,2", True, window)

        repository.crt_bcgrndC(50, 1425, 300, 1625, house, "random_house_6", True, window)
        repository.crt_bcgrnd(50, 1475, 300, 1575, house2, "random_house_6,2", True, window)

        repository.crt_bcgrndC(-150, 1825, 50, 2025, house, "random_house_7", True, window)
        repository.crt_bcgrnd(-150, 1875, 50, 1975, house2, "random_house_7,2", True, window)

        repository.crt_bcgrndC(200, 1825, 450, 2075, house, "random_house_8", True, window)
        repository.crt_bcgrnd(200, 1925, 450, 1975, house2, "random_house_8,2", True, window)

        repository.crt_bcgrndC(700, 125, 950, 325, house, "random_house_9", True, window)
        repository.crt_bcgrnd(700, 175, 950, 275, house2, "random_house_9,2", True, window)

        repository.crt_bcgrndC(1250, 225, 1450, 675, house, "random_house_10", True, window)
        repository.crt_bcgrnd(1300, 225, 1400, 675, house2, "random_house_10,2", True, window)

        repository.crt_bcgrndC(1200, 1925, 1550, 2125, house, "random_house_11", True, window)
        repository.crt_bcgrnd(1200, 1975, 1550, 2075, house2, "random_house_11,2", True, window)

        repository.crt_bcgrndC(1000, -25, 1250, 125, house, "random_house_12", True, window)
        repository.crt_bcgrnd(1000, 25, 1250, 75, house2, "random_house_12,2", True, window)

        # outside houses
        repository.crt_bcgrndC(-700, 1125, -500, 1475, house, "house_ext1", True, window)
        repository.crt_bcgrnd(-650, 1125, -550, 1475, house2, "house_ext1,1", True, window)

        repository.crt_bcgrndC(1950, 825, 2150, 1175, house, "house_ext2", True, window)
        repository.crt_bcgrnd(2000, 825, 2100, 1175, house2, "house_ext2,1", True, window)

        repository.crt_bcgrndC(1950, 225, 2150, 675, house, "house_ext3", True, window)
        repository.crt_bcgrnd(2000, 225, 2100, 675, house2, "house_ext3,1", True, window)

        repository.crt_bcgrndC(2250, 825, 2450, 1175, house, "house_ext4", True, window)
        repository.crt_bcgrnd(2300, 825, 2400, 1175, house2, "house_ext2,1", True, window)

        repository.crt_bcgrndC(2250, 225, 2450, 675, house, "house_ext5", True, window)
        repository.crt_bcgrnd(2300, 225, 2400, 675, house2, "house_ext3,1", True, window)

        # warehouse
        repository.crt_bcgrndC(750, 1175, 1100, 1925, warehouse, "warehouse1", True, window)
        repository.crt_bcgrnd(800, 1175, 1050, 1925, warehouse2, "warehouse2", True, window)
        repository.crt_bcgrnd(850, 1175, 1000, 1925, warehouse3, "warehouse3", True, window)
        repository.crt_bcgrnd(900, 1175, 950, 1925, warehouse4, "warehouse4", True, window)

        # plaza
        repository.crt_bcgrndC(800, 625, 950, 775, stonewell, "stone_well", True, window)
        repository.crt_bcgrnd(850, 675, 900, 725, waterwell, "water_well", True, window)

        repository.crt_bcgrnd(850, 475, 900, 575, path, "plaza1", False, window)
        repository.crt_bcgrnd(750, 575, 1000, 625, path, "plaza2", False, window)
        repository.crt_bcgrnd(750, 625, 800, 675, path, "plaza3,1", False, window)
        repository.crt_bcgrnd(700, 675, 800, 725, path, "plaza3,2", False, window)
        repository.crt_bcgrnd(750, 725, 800, 776, path, "plaza3,3", False, window)
        repository.crt_bcgrnd(951, 625, 1000, 675, path, "plaza4,1", False, window)
        repository.crt_bcgrnd(951, 675, 1050, 725, path, "plaza4,2", False, window)
        repository.crt_bcgrnd(951, 725, 1000, 776, path, "plaza4,3", False, window)
        repository.crt_bcgrnd(750, 776, 1000, 825, path, "plaza5", False, window)
        repository.crt_bcgrnd(850, 825, 900, 925, path, "plaza6", False, window)


        # checkpoint
        repository.crt_bcgrndC(700, 2375, 800, 2475, stonewell, "checkpoint", True, window)

        # tents
        repository.crt_bcgrndC(1150, 1175, 1250, 1325, tent1, "random_tent_1", True, window)
        repository.crt_bcgrndC(1151, 1225, 1250, 1275, stripe, "band_1_stripe", False, window)
        repository.crt_bcgrndC(1400, 1175, 1500, 1325, tent2, "random_tent_2", True, window)
        repository.crt_bcgrnd(1401, 1225, 1500, 1275, stripe, "band_2_stripe", False, window)
        repository.crt_bcgrndC(1400, 1425, 1500, 1675, tent3, "random_tent_3", True, window)
        repository.crt_bcgrndC(1401, 1475, 1500, 1525, stripe, "band_3_stripe", False, window)
        repository.crt_bcgrndC(1401, 1575, 1500, 1625, stripe, "band_4_stripe", False, window)

        # trees
        repository.crt_bcgrndC(1050, 2425, 1200, 2575, tree, "tree_ext1,1", False, window)
        repository.crt_bcgrndC(1100, 2475, 1150, 2525, house, "tree_ext1,2", False, window)
        repository.crt_bcgrndC(1500, 2475, 1650, 2625, tree, "tree_ext2,1", False, window)
        repository.crt_bcgrndC(1550, 2525, 1600, 2575, house, "tree_ext2,2", False, window)
        repository.crt_bcgrndC(1850, 2375, 2000, 2525, tree, "tree_ext3,1", False, window)
        repository.crt_bcgrndC(1900, 2425, 1950, 2475, house, "tree_ext3,2", False, window)
        repository.crt_bcgrndC(2000, 2075, 2150, 2225, tree, "tree_ext4,1", False, window)
        repository.crt_bcgrndC(2050, 2125, 2100, 2175, house, "tree_ext4,2", False, window)
        repository.crt_bcgrndC(1800, 1725, 1950, 1875, tree, "tree_ext5,1", False, window)
        repository.crt_bcgrndC(1850, 1775, 1900, 1825, house, "tree_ext5,2", False, window)
        repository.crt_bcgrndC(1900, 1375, 2050, 1525, tree, "tree_ext6,1", False, window)
        repository.crt_bcgrndC(1950, 1425, 2000, 1475, house, "tree_ext6,2", False, window)


        # water shallow
        repository.crt_bcgrndC(650, -125, 2650, -75, water1, "water1,1", False, window)
        repository.crt_bcgrndC(-150, -125, 500, -75, water1, "water2,1", False, window)
        repository.crt_bcgrndC(-350, -125, -200, -75, water1, "water3,1", False, window)
        repository.crt_bcgrndC(-400, -125, -350, 475, water1, "water4,1", False, window)
        repository.crt_bcgrndC(-1400, 475, -350, 525, water1, "water5,1", False, window)

        # noncollision objects

        # water deep
        repository.crt_bcgrnd(-1400, 425, -400, 475, water2, "water1,2", False, window)
        repository.crt_bcgrnd(-450, -125, -400, 425, water2, "water2,2", False, window)
        repository.crt_bcgrnd(-400, -175, 2650, -125, water2, "water3,2", False, window)

        repository.crt_bcgrnd(-450, -225, 2650, -175, water3, "water1,3", False, window)
        repository.crt_bcgrnd(-450, -175, -400, -125, water3, "water2,3", False, window)
        repository.crt_bcgrnd(-500, -175, -450, 375, water3, "water3,3", False, window)
        repository.crt_bcgrnd(-1400, 375, -450, 425, water3, "water4,3", False, window)

        repository.crt_bcgrnd(-1400, -1125, -500, 375, water4, "water1,4", False, window)
        repository.crt_bcgrnd(-500, -1125, -450, -175, water4, "water2,4", False, window)
        repository.crt_bcgrnd(-450, -1125, 2650, -225, water4, "water2,4", False, window)

        # castle----------------------------------------------------------------------------------------------------------------------------------

        repository.crt_bcgrnd(100, -1175, 1050, -525, castle_foundation, "castle_floor", False, window)
        repository.crt_bcgrnd(350, -1175, 400, -525, castle_roof_5, "castle_roof_1", False, window)
        repository.crt_bcgrnd(300, -1175, 350, -525, castle_roof_4, "castle_roof_2", False, window)
        repository.crt_bcgrnd(200, -1175, 300, -525, castle_roof_3, "castle_roof_3", False, window)
        repository.crt_bcgrnd(150, -1175, 200, -575, castle_roof_2, "castle_roof_4", False, window)
        repository.crt_bcgrnd(100, -1175, 150, -625, castle_roof_1, "castle_roof_5", False, window)
        repository.crt_bcgrnd(500, -825, 550, -775, castle_smudge, "castle_smudge_1", False, window)
        repository.crt_bcgrnd(400, -725, 450, -575, castle_smudge, "castle_smudge_2", False, window)
        repository.crt_bcgrnd(450, -625, 500, -575, castle_smudge, "castle_smudge_3", False, window)
        repository.crt_bcgrnd(500, -675, 550, -625, castle_smudge, "castle_smudge_4", False, window)
        repository.crt_bcgrnd(650, -775, 700, -725, castle_smudge, "castle_smudge_5", False, window)
        repository.crt_bcgrnd(650, -625, 700, -575, castle_smudge, "castle_smudge_6", False, window)
        repository.crt_bcgrnd(700, -725, 750, -675, castle_smudge, "castle_smudge_7", False, window)
        repository.crt_bcgrnd(800, -675, 850, -625, castle_smudge, "castle_smudge_8", False, window)
        repository.crt_bcgrnd(850, -775, 900, -725, castle_smudge, "castle_smudge_9", False, window)
        repository.crt_bcgrnd(900, -825, 950, -775, castle_smudge, "castle_smudge_10", False, window)
        repository.crt_bcgrnd(900, -725, 950, -675, castle_smudge, "castle_smudge_11", False, window)
        repository.crt_bcgrnd(850, -575, 900, -525, castle_smudge, "castle_smudge_12", False, window)
        repository.crt_bcgrnd(950, -875, 1000, -825, thing, "castle_thing_1", False, window)
        repository.crt_bcgrnd(950, -775, 1000, -725, thing, "castle_thing_2", False, window)
        repository.crt_bcgrnd(950, -675, 1000, -625, thing, "castle_thing_3", False, window)


        # -----------------------------------------------WALL MAIN---------------------------------------------------------------------------------------------------

        repository.crt_bcgrnd(200, -525, 950, -375, castle_wall_1, "castle_w_1,1", False, window)
        repository.crt_bcgrndC(200, -525, 950, -375, castle_wall_1, "castle_w_1,1", False, window)

        repository.crt_bcgrnd(900, -525, 950, -375, castle_defense, "castle_w_2,1", False, window)
        repository.crt_bcgrnd(800, -525, 850, -375, castle_defense, "castle_w_2,2", False, window)
        repository.crt_bcgrnd(700, -525, 750, -375, castle_defense, "castle_w_2,3", False, window)
        repository.crt_bcgrnd(600, -525, 650, -375, castle_defense, "castle_w_2,4", False, window)
        repository.crt_bcgrndC(600, -525, 650, -375, castle_defense, "castle_w_2,4", False, window)
        repository.crt_bcgrnd(500, -525, 550, -375, castle_defense, "castle_w_2,5", False, window)
        repository.crt_bcgrndC(500, -525, 550, -375, castle_defense, "castle_w_2,5", False, window)
        repository.crt_bcgrnd(400, -525, 450, -375, castle_defense, "castle_w_2,6", False, window)
        repository.crt_bcgrnd(300, -525, 350, -375, castle_defense, "castle_w_2,7", False, window)
        repository.crt_bcgrnd(200, -525, 250, -375, castle_defense, "castle_w_2,8", False, window)

        repository.crt_bcgrnd(200, -475, 950, -425, castle_wall_2, "castle_w_3,1", False, window)
        # -----------------------------------------------WALL LEFT---------------------------------------------------------------------------------------------------

        repository.crt_bcgrnd(-50, -625, 100, -1800, castle_wall_1, "castle_w_1,GDF1", False, window)

        repository.crt_bcgrnd(-50, -625, 100, -675, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(-50, -725, 100, -775, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(-50, -825, 100, -875, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(-50, -925, 100, -975, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(-50, -1025, 100, -1075, castle_defense, "castle_w_1,1", False, window)

        repository.crt_bcgrnd(0, -625, 50, -1800, castle_wall_2, "castle_w_1,GDF1", False, window)

        # -----------------------------------------------WALL RIGHT---------------------------------------------------------------------------------------------------

        repository.crt_bcgrnd(1050, -625, 1200, -1800, castle_wall_1, "castle_w_1,GDF1", False, window)

        repository.crt_bcgrnd(1050, -625, 1200, -675, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(1050, -725, 1200, -775, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(1050, -825, 1200, -875, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(1050, -925, 1200, -975, castle_defense, "castle_w_1,1", False, window)
        repository.crt_bcgrnd(1050, -1025, 1200, -1075, castle_defense, "castle_w_1,1", False, window)

        repository.crt_bcgrnd(1100, -625, 1150, -1800, castle_wall_2, "castle_w_1,GDF1", False, window)

        # -----------------------------------------------TORRE 1-------------------------------------------------------------------------------------
        repository.crt_bcgrnd(-50, -625, 150, -275, castle_tower_2, "castle_t_2,3", False, window)
        repository.crt_bcgrnd(-150, -525, 200, -375, castle_tower_2, "castle_t_1,3", False, window)
        # ==================HORIZONTAL
        repository.crt_bcgrnd(-150, -325, 200, -375, castle_tower_1, "castle_t_1,1", False, window)
        repository.crt_bcgrnd(-150, -425, 200, -475, castle_tower_1, "castle_t_1,2", False, window)
        repository.crt_bcgrnd(-150, -525, 200, -575, castle_tower_1, "castle_t_1,3", False, window)
        # ==================VERTICAL
        repository.crt_bcgrnd(100, -625, 150, -275, castle_tower_1, "castle_t_2,1", False, window)
        repository.crt_bcgrnd(00, -625, 50, -275, castle_tower_1, "castle_t_2,2", False, window)
        repository.crt_bcgrnd(-100, -625, -50, -275, castle_tower_1, "castle_t_2,3", False, window)
        # ===================TELHADO
        repository.crt_bcgrnd(-100, -575, 150, -525, tower_roof_1, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(-100, -575, -50, -325, tower_roof_1, "tower_roof_1,1", False, window)

        repository.crt_bcgrnd(-50, -525, 0, -325, tower_roof_2, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(-50, -525, 150, -475, tower_roof_2, "tower_roof_1,1", False, window)

        repository.crt_bcgrnd(0, -475, 50, -425, tower_roof_4, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(0, -475, 150, -325, tower_roof_4, "tower_roof_1,1", False, window)

        repository.crt_bcgrnd(0, -425, 50, -325, tower_roof_3, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(50, -425, 0, -325, tower_roof_3, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(50, -425, 100, -375, tower_roof_3, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(50, -475, 150, -425, tower_roof_3, "tower_roof_1,1", False, window)

        # ----------------------------------------------TORRE 2-----------------------------------------------------------------------------------------

        repository.crt_bcgrnd(950, -525, 1300, -375, castle_tower_2, "castle_t_2,3", False, window)
        repository.crt_bcgrnd(1050, -625, 1200, -275, castle_tower_2, "castle_t_1,3", False, window)
        # ==================HORIZONTAL
        repository.crt_bcgrnd(950, -325, 1300, -375, castle_tower_1, "castle_t_1,1", False, window)
        repository.crt_bcgrnd(950, -425, 1300, -475, castle_tower_1, "castle_t_1,2", False, window)
        repository.crt_bcgrnd(950, -525, 1300, -575, castle_tower_1, "castle_t_1,3", False, window)
        # ==================VERTICAL
        repository.crt_bcgrnd(1000, -625, 1050, -275, castle_tower_1, "castle_t_2,1", False, window)
        repository.crt_bcgrnd(1100, -625, 1150, -275, castle_tower_1, "castle_t_2,2", False, window)
        repository.crt_bcgrnd(1200, -625, 1250, -275, castle_tower_1, "castle_t_2,3", False, window)
        # ===================TELHADO
        repository.crt_bcgrnd(1000, -575, 1250, -525, tower_roof_1, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(1000, -575, 1050, -325, tower_roof_1, "tower_roof_1,1", False, window)

        repository.crt_bcgrnd(1050, -525, 1250, -325, tower_roof_2, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(1050, -525, 1050, -475, tower_roof_2, "tower_roof_1,1", False, window)

        repository.crt_bcgrnd(1100, -475, 1250, -325, tower_roof_4, "tower_roof_1,1", False, window)

        repository.crt_bcgrnd(1100, -425, 1150, -325, tower_roof_3, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(1150, -425, 1200, -375, tower_roof_3, "tower_roof_1,1", False, window)
        repository.crt_bcgrnd(1150, -475, 1250, -425, tower_roof_3, "tower_roof_1,1", False, window)

        # --------------------------------------------------------------------------------------------------------------------------------

        # bridge

        repository.crt_bcgrnd(500, -375, 650, -75, bridge, "bridge_1", False, window)
        repository.crt_bcgrndC(-200, -125, -150, -75, bridge, "bridge_2", False, window)
        repository.crt_bcgrnd(-250, -525, -150, -125, bridge, "bridge_3", False, window)
        repository.crt_bcgrnd(-350, -225, -250, -175, bridge, "bridge_4", False, window)
        repository.crt_bcgrnd(-350, -375, -250, -325, bridge, "bridge_5", False, window)
        repository.crt_bcgrnd(-350, -525, -250, -475, bridge, "bridge_6", False, window)

        repository.crt_bcgrnd(450, -375, 500, -325, bridge2, "bridge_square_1", False, window)
        repository.crt_bcgrnd(450, -275, 500, -225, bridge2, "bridge_square_2", False, window)
        repository.crt_bcgrnd(450, -175, 500, -125, bridge2, "bridge_square_3", False, window)
        repository.crt_bcgrnd(650, -375, 700, -325, bridge2, "bridge_square_4", False, window)
        repository.crt_bcgrnd(650, -275, 700, -225, bridge2, "bridge_square_5", False, window)
        repository.crt_bcgrnd(650, -175, 700, -125, bridge2, "bridge_square_6", False, window)
        repository.crt_bcgrndC(450, -375, 500, -325, bridge2, "bridge_square_1c", False, window)
        repository.crt_bcgrndC(450, -275, 500, -225, bridge2, "bridge_square_2c", False, window)
        repository.crt_bcgrndC(450, -175, 500, -125, bridge2, "bridge_square_3c", False, window)
        repository.crt_bcgrndC(650, -375, 700, -325, bridge2, "bridge_square_4c", False, window)
        repository.crt_bcgrndC(650, -275, 700, -225, bridge2, "bridge_square_5c", False, window)
        repository.crt_bcgrndC(650, -175, 700, -125, bridge2, "bridge_square_6c", False, window)

        repository.crt_bcgrndC(450, -325, 500, -275, invis_wall, "bridge_water_1", False, window)
        repository.crt_bcgrndC(450, -225, 500, -175, invis_wall, "bridge_water_2c", False, window)
        repository.crt_bcgrndC(650, -325, 500, -275, invis_wall, "bridge_water_3c", False, window)
        repository.crt_bcgrndC(650, -225, 700, -175, invis_wall, "bridge_water_4c", False, window)

        # repository.crt_bcgrnd(0, 0, 0, 0, type, False, window)

        # path

        repository.crt_bcgrnd(550, 125, 650, 375, path, "random_path_1", False, window)
        repository.crt_bcgrnd(551, 375, 700, 2275, path, "random_path_2", False, window)
        repository.crt_bcgrnd(-199, -75, 650, 125, path, "random_path_3", False, window)
        repository.crt_bcgrnd(-150, 125, -50, 1675, path, "random_path_4", False, window)
        repository.crt_bcgrnd(200, 125, 300, 1075, path, "random_path_5", False, window)
        repository.crt_bcgrnd(500, 375, 551, 425, path, "random_path_6", False, window)
        repository.crt_bcgrnd(150, 475, 200, 575, path, "random_path_7", False, window)
        repository.crt_bcgrnd(300, 525, 551, 575, path, "random_path_8", False, window)
        repository.crt_bcgrnd(500, 675, 551, 725, path, "random_path_9", False, window)
        repository.crt_bcgrnd(150, 925, 200, 1025, path, "random_path_10", False, window)
        repository.crt_bcgrnd(300, 975, 551, 1075, path, "random_path_11", False, window)
        repository.crt_bcgrnd(100, 1625, 150, 1675, path, "random_path_12", False, window)
        repository.crt_bcgrnd(-150, 1675, 551, 1775, path, "random_path_13", False, window)
        repository.crt_bcgrnd(-100, 1775, 0, 1825, path, "random_path_14", False, window)
        repository.crt_bcgrnd(200, 1775, 300, 1825, path, "random_path_15", False, window)
        repository.crt_bcgrnd(400, 1075, 450, 1125, path, "random_path_16", False, window)
        repository.crt_bcgrnd(850, 1075, 950, 1175, path, "random_path_17", False, window)
        repository.crt_bcgrnd(700, 925, 1200, 1075, path, "random_path_18", False, window)
        repository.crt_bcgrnd(1050, 375, 1200, 925, path, "random_path_19", False, window)
        repository.crt_bcgrnd(750, 325, 800, 375, path, "random_path_20", False, window)
        repository.crt_bcgrnd(700, 375, 1050, 475, path, "random_path_21", False, window)
        repository.crt_bcgrnd(1100, 125, 1200, 375, path, "random_path_22", False, window)
        repository.crt_bcgrnd(1200, 475, 1250, 525, path, "random_path_23", False, window)
        repository.crt_bcgrnd(1200, 975, 1400, 1075, path, "random_path_24", False, window)
        repository.crt_bcgrnd(1251, 1075, 1400, 1925, path, "random_path_25", False, window)
        repository.crt_bcgrnd(550, 2326, 700, 3025, path, "ext_path_1", False, window)
        repository.crt_bcgrnd(1950, 675, 2650, 825, path, "ext_path_2", False, window)

        # sand

        repository.crt_bcgrnd(650, -75, 1600, -25, sand, "sand_1", False, window)
        repository.crt_bcgrnd(650, -25, 750, 25, sand, "sand_2", False, window)
        repository.crt_bcgrnd(650, 25, 700, 75, sand, "sand_3", False, window)
        repository.crt_bcgrnd(950, -25, 1000, 25, sand, "sand_4", False, window)
        repository.crt_bcgrnd(1251, -25, 1300, 25, sand, "sand_5", False, window)
        repository.crt_bcgrnd(1350, -25, 1600, 25, sand, "sand_6", False, window)
        repository.crt_bcgrnd(1450, 25, 1600, 75, sand, "sand_7", False, window)
        repository.crt_bcgrnd(1500, 75, 1600, 125, sand, "sand_8", False, window)
        repository.crt_bcgrnd(1550, 125, 1600, 175, sand, "sand_9", False, window)
        repository.crt_bcgrnd(1750, -75, 2650, -25, sand, "sand_10", False, window)
        repository.crt_bcgrnd(1750, -25, 1900, 25, sand, "sand_11", False, window)
        repository.crt_bcgrnd(1750, 25, 1850, 75, sand, "sand_12", False, window)
        repository.crt_bcgrnd(1750, 75, 1800, 125, sand, "sand_13", False, window)
        repository.crt_bcgrnd(-1250, 525, -350, 575, sand, "sand_14", False, window)
        repository.crt_bcgrnd(-450, 575, -350, 625, sand, "sand_15", False, window)
        repository.crt_bcgrnd(-400, 625, -350, 675, sand, "sand_16", False, window)

        # wheat

        repository.crt_bcgrnd(-750, 625, -450, 1025, wheat, "wheat_1", False, window)
        repository.crt_bcgrnd(-750, 1575, -450, 2725, wheat, "wheat_2", False, window)

        # interactible objects

        # npcs
        # Jorge
        full_npc(600, 375, 650, 425, 'Jorge', male, window)

        # Roberta
        full_npc(550, 725, 600, 775, 'Roberta', female, window)

        # traders
        repository.crt_npc(1400, 1675, 1450, 1725, male, "Blacksmith:", "male_blacksmith", True, window)
        repository.crt_npc(1400, 1325, 1450, 1375, male, "Potions seller:", "male_potions_seller", True, window)
        repository.crt_npc(1200, 1325, 1250, 1375, male, "Goods trader:", "male_goods_trader", True, window)

        # Fisherman
        full_npc(-150, -75, -100, -25, 'Fisherman', male, window)

        # Guardsman
        full_npc(500, -375, 550, -325, 'Guardsman', male, window)

        # Priest
        full_npc(1150, 1525, 1200, 1575, 'Priest', male, window)

        # Lily
        full_npc(350, 75, 400, 125, 'Lily', female, window)

        # Grace
        full_npc(-100, 225, -50, 275, 'Grace', female, window)

        # Isabella
        full_npc(250, 775, 300, 825, 'Isabella', female, window)

        # Charlotte
        full_npc(1150, 775, 1200, 825, 'Charlotte', female, window)

        # Daisy
        full_npc(1150, 875, 1200, 925, 'Daisy', female, window)

        # Alex
        full_npc(1050, 125, 1100, 175, 'Alex', male, window)

        # Frederick
        full_npc(500, 775, 550, 825, 'Frederick', male, window)

        # Elliot
        full_npc(350, 1075, 400, 1125, 'Elliot', male, window)

        # Albert
        full_npc(200, 325, 250, 375, 'Albert', male, window)

        # Leon
        full_npc(300, 1775, 350, 1825, 'Leon', male, window)

        # Bobby
        full_npc(-150, 1325, -100, 1375, 'Bobby', male, window)

def forest(b, window):
    if b:
        repository.forest_map = True
        repository.city_map = False
        try:
            repository.city_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_PURGE)
        except:
            pass
        repository.forest_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_LOOP)
        # clearing the screen for new map:
        for e in repository.npcs:
            e.remove_obj()
        repository.npcs.clear()
        for e in repository.npcs_head:
            e.remove_obj()
        repository.npcs_head.clear()
        for e in repository.bcgrnd:
            e.remove_obj()
        repository.bcgrnd.clear()
        for e in repository.bcgrndC:
            e.remove_obj()
        repository.bcgrndC.clear()
        for e in repository.bcgrndI:
            e.remove_obj()
        repository.bcgrndI.clear()
        for e in repository.enemies:
            try:
                e.remove_obj()
            except:
                pass
        repository.enemies.clear()
        global house, path, castle, jorge
        # npcs-
        # repository.crt_npc(0, 0, 0, 0, type, True, window)
        repository.crt_npc(550, 725, 600, 775, 'pink', "Roberta", "female", True, window)

        # forest beach sand

        repository.crt_bcgrnd(1350, -875, 1950, -375, sand, "fr_sand1,1", False, window)
        repository.crt_bcgrnd(1400, -375, 2050, -275, sand, "fr_sand1,2", False, window)
        repository.crt_bcgrnd(1450, -275, 2100, -225, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1550, -225, 2200, -125, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1500, -925, 1550, -175, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1600, -175, 2200, -125, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1750, -125, 2200, -25, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1600, -325, 1750, -75, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1200, -825, 1350, -775, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1250, -775, 1350, -725, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1300, -725, 1350, -675, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1300, -575, 1350, -525, sand, "fr_sand1,3", False, window)
        repository.crt_bcgrnd(1700, -125, 1750, -25, sand, "fr_sand1,3", False, window)

        # path

        repository.crt_bcgrnd(450, -575, 1300, -475, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(1300, -525, 1350, -475, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(1350, -575, 1400, -525, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(450, -575, 550, 2075, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(550, 1975, 1350, 2075, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(1350, 1975, 1400, 2025, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(1400, 2025, 1450, 2075, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(1500, 1975, 1550, 2025, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(550, 425, 2200, 525, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(550, 375, 600, 575, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(550, -475, 600, -425, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(550, 1925, 600, 1975, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-750, -975, -400, -675, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-750, -975, -450, -625, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-400, -875, -350, -775, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-350, -875, -300, -825, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-750, -625, -600, -575, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-350, 1725, -200, 2075, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-450, 1825, -100, 1975, dirt, "fr_dirt", False, window)
        repository.crt_bcgrnd(-400, 1775, -150, 2025, dirt, "fr_dirt", False, window)

        # forest water

        # deep_water--------------------------------------------------------------------------

        repository.crt_bcgrnd(1950, -1975, 3000, -325, water4, "fr_water1,1", False, window)
        repository.crt_bcgrnd(2100, -325, 3000, -175, water4, "fr_water1,1", False, window)
        repository.crt_bcgrnd(1750, -1975, 3000, -825, water4, "fr_water1,1", False, window)

        # shallow_water_1--------------------------------------------------------------------------

        repository.crt_bcgrndC(1750, -1975, 1800, -825, water1, "fr_water1,1", False, window)
        repository.crt_bcgrndC(1800, -825, 1850, -675, water1, "fr_water1,2", False, window)
        repository.crt_bcgrndC(1850, -675, 1900, -525, water1, "fr_water1,3", False, window)
        repository.crt_bcgrndC(1900, -525, 1950, -425, water1, "fr_water1,4", False, window)
        repository.crt_bcgrndC(1950, -425, 2000, -325, water1, "fr_water1,5", False, window)
        repository.crt_bcgrndC(2000, -325, 2050, -275, water1, "fr_water1,6", False, window)
        repository.crt_bcgrndC(2050, -275, 2100, -225, water1, "fr_water1,7", False, window)
        repository.crt_bcgrndC(2100, -225, 2150, -175, water1, "fr_water1,8", False, window)
        repository.crt_bcgrndC(2150, -175, 2200, -125, water1, "fr_water1,9", False, window)
        repository.crt_bcgrndC(2200, -125, 3000, -75, water1, "fr_water1,10", False, window)

        # shallow_water_2--------------------------------------------------------------------------

        repository.crt_bcgrndC(1800, -1975, 1850, -825, water2, "fr_water1,1", False, window)
        repository.crt_bcgrndC(1850, -825, 1900, -675, water2, "fr_water1,2", False, window)
        repository.crt_bcgrndC(1900, -675, 1950, -525, water2, "fr_water1,3", False, window)
        repository.crt_bcgrndC(1950, -525, 2000, -425, water2, "fr_water1,4", False, window)
        repository.crt_bcgrndC(2000, -425, 2050, -325, water2, "fr_water1,5", False, window)
        repository.crt_bcgrndC(2050, -325, 2100, -275, water2, "fr_water1,6", False, window)
        repository.crt_bcgrndC(2100, -275, 2150, -225, water2, "fr_water1,7", False, window)
        repository.crt_bcgrndC(2150, -225, 2200, -175, water2, "fr_water1,8", False, window)
        repository.crt_bcgrndC(2200, -175, 3000, -125, water2, "fr_water1,10", False, window)

        # shallow_water_3--------------------------------------------------------------------------

        repository.crt_bcgrndC(1850, -1975, 1900, -825, water3, "fr_water1,1", False, window)
        repository.crt_bcgrndC(1900, -825, 1950, -675, water3, "fr_water1,2", False, window)
        repository.crt_bcgrndC(1950, -675, 2000, -525, water3, "fr_water1,3", False, window)
        repository.crt_bcgrndC(2000, -525, 2050, -425, water3, "fr_water1,4", False, window)
        repository.crt_bcgrndC(2050, -425, 2100, -325, water3, "fr_water1,5", False, window)
        repository.crt_bcgrndC(2100, -325, 2150, -275, water3, "fr_water1,6", False, window)
        repository.crt_bcgrndC(2150, -275, 2200, -225, water3, "fr_water1,7", False, window)
        repository.crt_bcgrndC(2200, -225, 3000, -175, water3, "fr_water1,10", False, window)

        # lake_water_1--------------------------------------------------------------------------

        repository.crt_bcgrndC(1100, 2575, 1150, 2625, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1150, 2525, 1200, 2575, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1200, 2475, 1250, 2525, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1250, 2425, 1300, 2475, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1300, 2375, 1400, 2425, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1400, 2325, 1450, 2375, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1450, 2275, 1500, 2325, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1500, 2225, 1600, 2275, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1600, 2175, 1700, 2225, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1700, 2125, 1750, 2175, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1750, 2075, 1900, 2125, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1900, 2025, 1950, 2075, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(2100, 2025, 2200, 2075, waterL1, "fr_waterL1,1", False, window)

        repository.crt_bcgrndC(1400, 2675, 1450, 2625, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1450, 2575, 1500, 2625, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1500, 2525, 1600, 2575, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1600, 2475, 1650, 2525, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1650, 2425, 1750, 2475, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1750, 2375, 1800, 2425, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1800, 2325, 1950, 2375, waterL1, "fr_waterL1,1", False, window)
        repository.crt_bcgrndC(1950, 2275, 2150, 2325, waterL1, "fr_waterL1,1", False, window)

        # lake_water_2--------------------------------------------------------------------------

        repository.crt_bcgrndC(1150, 2575, 1200, 2625, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1200, 2525, 1250, 2575, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1250, 2475, 1300, 2525, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1300, 2425, 1400, 2475, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1400, 2375, 1450, 2425, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1450, 2325, 1500, 2375, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1500, 2275, 1600, 2325, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1600, 2225, 1700, 2275, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1700, 2175, 1750, 2225, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1750, 2125, 1900, 2175, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1900, 2075, 2250, 2125, waterL2, "fr_waterL2,1", False, window)

        repository.crt_bcgrndC(1350, 2625, 1400, 2675, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1400, 2575, 1450, 2625, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1450, 2525, 1500, 2575, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1500, 2475, 1600, 2525, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1600, 2425, 1650, 2475, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1650, 2375, 1750, 2425, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1750, 2325, 1800, 2375, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1800, 2275, 1950, 2325, waterL2, "fr_waterL2,1", False, window)
        repository.crt_bcgrndC(1950, 2225, 2150, 2275, waterL2, "fr_waterL2,1", False, window)

        # lake_water_3--------------------------------------------------------------------------

        repository.crt_bcgrndC(1900, 2125, 2200, 2250, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1750, 2175, 2150, 2225, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1700, 2225, 1950, 2275, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1600, 2275, 1800, 2325, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1500, 2325, 1750, 2375, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1450, 2375, 1650, 2425, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1400, 2425, 1600, 2475, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1300, 2475, 1500, 2525, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1250, 2525, 1450, 2575, waterL3, "fr_waterL3,1", False, window)
        repository.crt_bcgrndC(1200, 2575, 1400, 2625, waterL3, "fr_waterL3,1", False, window)

        # forest tree==========================================================================================================

        repository.crt_bcgrndC(-1850, -2225, 1750, -975, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-1850, -975, -800, 3775, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-1000, 2725, 3300, 3775, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2250, -75, 3300, 3775, tree, "fr_tree_limit", False, window)
        # -----------------------------------------------------------------------------------------------------------------
        repository.crt_bcgrndC(1000, 2675, 1550, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1050, 2625, 1350, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1450, 2625, 1500, 2675, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(1650, 2675, 2250, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1800, 2625, 2250, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1850, 2575, 1900, 2625, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1950, 2575, 2000, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2000, 2475, 2250, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2050, 2425, 2100, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2100, 2325, 2150, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2150, 2175, 2250, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2200, 2125, 2250, 2675, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(2200, 525, 2250, 2075, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2150, 1675, 2200, 1975, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(2150, 975, 2200, 1575, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2100, 1075, 2150, 1475, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(2150, 675, 2200, 925, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(2200, 125, 2250, 525, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(2150, 225, 2200, 475, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(2200, -75, 2250, -25, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(1500, -1125, 1800, -925, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1550, -925, 1750, -875, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1050, -975, 1500, -875, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1100, -925, 1400, -825, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(1100, -925, 1400, -825, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(800, -975, 1400, -925, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-850, -975, 750, -925, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(200, -925, 650, -875, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(250, -875, 550, -825, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(-100, -925, 150, -875, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-500, -925, -200, -875, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(-800, -975, -750, 775, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, -975, -700, -825, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(-750, -675, -700, -525, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, -475, -700, 175, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-700, -375, -650, -225, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-700, -125, -650, 275, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-650, -75, -550, 225, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-700, -25, -500, 175, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, 225, -700, 325, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(-750, 375, -700, 575, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, 625, -700, 725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-800, 825, -750, 1575, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, 975, -700, 1275, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, 1375, -700, 1475, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(-800, 1925, -750, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, 1975, -700, 2475, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, 2525, -700, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-700, 2625, -650, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-650, 2675, -600, 2725, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(-550, 2675, 400, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-450, 2625, -150, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-100, 2625, 100, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(200, 2625, 300, 2675, tree, "fr_tree_limit", False, window)

        repository.crt_bcgrndC(450, 2675, 950, 2725, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(500, 2625, 900, 2675, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(550, 2575, 600, 2625, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(650, 2575, 850, 2625, tree, "fr_tree_limit", False, window)

        # palm tree

        repository.crt_bcgrndC(1700, -125, 1750, -75, palm_tree, "fr_palm_tree", False, window)
        repository.crt_bcgrndC(1750, -175, 1900, -125, palm_tree, "fr_palm_tree", False, window)
        repository.crt_bcgrndC(1800, -225, 1850, -75, palm_tree, "fr_palm_tree", False, window)
        repository.crt_bcgrndC(1850, -75, 1900, -25, palm_tree, "fr_palm_tree", False, window)
        repository.crt_bcgrndC(1900, -225, 1950, -175, palm_tree, "fr_palm_tree", False, window)
        repository.crt_bcgrndC(1750, -275, 1800, -225, palm_tree, "fr_palm_tree", False, window)

        # cave

        repository.crt_bcgrndC(-650, -1125, -500, -875, cave_fr, "fr_cave", False, window)
        repository.crt_bcgrndC(-700, -1225, -450, -925, cave_fr, "fr_cave", False, window)
        repository.crt_bcgrndC(-750, -1175, -400, -975, cave_fr, "fr_cave", False, window)

        repository.crt_bcgrndC(-750, -1175, -650, -1125, tree, "fr_tree_limit", False, window)
        repository.crt_bcgrndC(-750, -1225, -600, -1175, tree, "fr_tree_limit", False, window)

        # trees-------------------------------------------------------------------------------------------------------------------

        repository.crt_bcgrndC(1900, 1875, 2150, 2025, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1950, 1825, 2100, 2075, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1600, 975, 1750, 1225, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1550, 1025, 1800, 1175, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1150, 975, 1300, 1225, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1100, 1025, 1350, 1175, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(600, 75, 750, 325, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(550, 125, 800, 275, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(700, 625, 850, 875, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(650, 675, 900, 825, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1000, 625, 1200, 925, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(950, 675, 1250, 875, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1800, 725, 1950, 975, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1750, 775, 2000, 925, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(850, 1575, 1100, 1725, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(900, 1525, 1050, 1775, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1150, 2075, 1300, 2325, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1100, 2125, 1350, 2275, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(850, 2275, 1000, 2525, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(800, 2325, 1050, 2475, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(200, 1975, 400, 2275, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(150, 2025, 450, 2225, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(250, 2325, 400, 2575, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(200, 2375, 450, 2525, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(-350, 2325, -200, 2575, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(-400, 2375, -150, 2525, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(250, 1575, 400, 1825, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(200, 1625, 450, 1775, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(200, 1125, 400, 1425, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(150, 1175, 450, 1375, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(-300, 1175, -50, 1325, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(-250, 1125, -100, 1375, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(-600, 675, -350, 825, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(-550, 625, -400, 875, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(100, 725, 350, 875, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(150, 675, 300, 925, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(-250, 75, -50, 375, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(-300, 125, 0, 325, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(100, -175, 250, 75, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(50, -125, 300, 25, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(-250, -425, 0, -275, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(-200, -475, -50, -225, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(100, -475, 350, -325, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(150, -525, 300, -275, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(-50, -825, 100, -575, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(-100, -775, 150, -625, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(700, -475, 850, -225, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(650, -425, 900, -275, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1000, -75, 1150, 175, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(950, -25, 1200, 125, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1300, 175, 1600, 375, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1350, 125, 1550, 425, tree, "fr_tree", False, window)

        repository.crt_bcgrndC(1850, 175, 2100, 325, tree, "fr_tree", False, window)
        repository.crt_bcgrndC(1900, 125, 2050, 375, tree, "fr_tree", False, window)

        # tower-------------------------------------------------------------------------------------------------------------------

        repository.crt_bcgrnd(1450, 1375, 1900, 1775, FFstone_foundation, "fr_tower_foundation", False, window)

        repository.crt_bcgrndC(1450, 1375, 1550, 1425, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1450, 1375, 1500, 1625, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1450, 1725, 1500, 1775, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1650, 1725, 1750, 1775, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1800, 1725, 1900, 1775, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1850, 1575, 1900, 1775, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1850, 1375, 1900, 1525, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1650, 1375, 1800, 1425, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1550, 1475, 1600, 1525, FFstone_walls, "fr_stone_walls", False, window)

        repository.crt_bcgrndC(1500, 1225, 1550, 1275, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1250, 1525, 1300, 1575, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1350, 1725, 1400, 1775, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(1900, 1625, 1950, 1675, FFstone_walls, "fr_stone_walls", False, window)
        repository.crt_bcgrndC(2000, 1525, 2050, 1575, FFstone_walls, "fr_stone_walls", False, window)

        repository.crt_bcgrndC(1650, 1425, 1750, 1475, dirt, "fr_chest", False, window)

        # camp--------------------------------------------------------------------------------------------------------------------

        repository.crt_bcgrndC(-300, 1825, -250, 1975, fr_house_ceilling4, "fr_bonfire", False, window)
        repository.crt_bcgrndC(-350, 1875, -200, 1925, fr_house_ceilling4, "fr_bonfire", False, window)
        repository.crt_bcgrndC(-300, 1875, -250, 1925, coal, "fr_bonfire", False, window)

        repository.crt_bcgrndC(-600, 1625, -450, 1875, bandit_tent1, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-600, 1675, -450, 1825, bandit_tent2, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-600, 1725, -450, 1775, bandit_tent1, "fr_ccamp", False, window)

        repository.crt_bcgrndC(-600, 1925, -450, 2175, bandit_tent1, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-600, 1975, -450, 2125, bandit_tent2, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-600, 2025, -450, 2075, bandit_tent1, "fr_ccamp", False, window)

        repository.crt_bcgrndC(-100, 1625, 50, 1875, bandit_tent1, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-100, 1675, 50, 1825, bandit_tent2, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-100, 1725, 50, 1775, bandit_tent1, "fr_ccamp", False, window)

        repository.crt_bcgrndC(-100, 1925, 50, 2175, bandit_tent1, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-100, 1975, 50, 2125, bandit_tent2, "fr_ccamp", False, window)
        repository.crt_bcgrndC(-100, 2025, 50, 2075, bandit_tent1, "fr_ccamp", False, window)

        # stones

        repository.crt_bcgrndC(-500, 1475, -450, 1525, random_stone, "fr_stones", False, window)
        repository.crt_bcgrndC(-400, 1575, -350, 1625, random_stone, "fr_stones", False, window)
        repository.crt_bcgrndC(-150, 1425, -100, 1475, random_stone, "fr_stones", False, window)
        repository.crt_bcgrndC(0, 1525, 50, 1575, random_stone, "fr_stones", False, window)
        repository.crt_bcgrndC(-350, 2175, -300, 2225, random_stone, "fr_stones", False, window)
        repository.crt_bcgrndC(2150, -25, 2200, 25, random_stone, "fr_stones", False, window)
        repository.crt_bcgrndC(1800, -475, 1850, -425, random_stone, "fr_stones", False, window)

        # npc forest house

        repository.crt_bcgrndC(1450, -725, 1750, -325, fr_house_ceilling1, "fr_house1_celling2", True, window)
        repository.crt_bcgrndC(1450, -675, 1750, -375, fr_house_ceilling2, "fr_house1_celling3", False, window)
        repository.crt_bcgrndC(1450, -625, 1750, -425, fr_house_ceilling3, "fr_house1_celling4", False, window)
        repository.crt_bcgrndC(1450, -575, 1750, -475, fr_house_ceilling4, "fr_house1_celling4", False, window)

        # enemies
        # wild dogs 00-05
        if 0 <= repository.player_lvl < 5:
            repository.crt_enemy(1150, 275, 1200, 325, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(100, 575, 150, 625, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(350, 75, 400, 125, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(700, 25, 750, 75, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(900, 275, 950, 325, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(50, 225, 100, 275, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(350, 325, 400, 375, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(700, 975, 750, 1025, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(950, 1025, 1000, 1075, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(350, 925, 400, 975, '', "dog", 5, False, 100, 20, 10, 35, True, window)
        elif repository.player_lvl >= 5:
            repository.crt_enemy(1150, 275, 1200, 325, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(100, 575, 150, 625, '', "dog", 5, False, 100, 20, 10, 35, True, window)
            repository.crt_enemy(700, 975, 750, 1025, '', "dog", 5, False, 100, 20, 10, 35, True, window)

        # wolfs 05-10
        if 5 <= repository.player_lvl < 10:
            repository.crt_enemy(1400, 1075, 1450, 1125, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1100, 1325, 1150, 1375, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1350, 1325, 1400, 1375, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1150, 1725, 1200, 1775, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1050, 2025, 1100, 2075, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1450, 2125, 1500, 2175, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1700, 1975, 1750, 2025, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1750, 1725, 1800, 1775, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1550, 1675, 1600, 1725, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1950, 1275, 2000, 1325, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
        elif repository.player_lvl >= 10:
            repository.crt_enemy(1100, 1325, 1150, 1425, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1150, 1725, 1200, 1775, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1450, 2125, 1500, 2175, '', "wolf", 10, False, 200, 40, 10, 35, True, window)
            repository.crt_enemy(1750, 1725, 1800, 1775, '', "wolf", 10, False, 200, 40, 10, 35, True, window)

        # bandits 10-15
        if 10 <= repository.player_lvl < 15:
            repository.crt_enemy(-550, 1175, -500, 1225, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(0, 1325, 50, 1375, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-400, 1375, -350, 1425, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-200, 1575, -150, 1625, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(100, 1825, 150, 1875, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-250, 2125, -200, 2175, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-600, 2325, -550, 2375, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-550, 2475, -500, 2525, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-100, 2325, -50, 2375, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(50, 2425, 100, 2475, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
        elif repository.player_lvl >= 15:
            repository.crt_enemy(0, 1325, 50, 1375, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-200, 1575, -150, 1625, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(-250, 2125, -200, 2175, '', "bandit", 15, False, 300, 60, 10, 35, True, window)
            repository.crt_enemy(50, 2425, 100, 2475, '', "bandit", 15, False, 300, 60, 10, 35, True, window)

        # giant spiders 15-20
        if 15 <= repository.player_lvl < 20:
            repository.crt_enemy(-350, -775, -300, -725, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-200, -625, -150, -575, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-350, -525, -300, -475, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-550, -375, -500, -325, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-350, -325, -300, -275, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-650, -275, -600, -225, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-250, -175, -200, -125, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-500, -125, -450, -75, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-350, -125, -300, -75, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-100, -75, -50, -25, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
        elif repository.player_lvl >= 20:
            repository.crt_enemy(-200, -625, -150, -575, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-650, -275, -600, -225, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-500, -125, -450, -75, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            repository.crt_enemy(-100, -75, -50, -25, '', "g_spider_f", 20, False, 400, 80, 10, 35, True, window)
            try:
                if repository.inventory['Boss\'s spider heart'] == 1:
                    pass
            except:
                repository.crt_enemy(-600, -675, -500, -575, '', "boss_forest", 30, False, 600, 120, 15, 35, True, window)

def cave(b, window):
    if b:
        repository.forest_map = True
        repository.city_map = False
        try:
            repository.city_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_PURGE)
        except:
            pass
        repository.forest_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_LOOP)
        # clearing the screen for new map:
        for e in repository.npcs:
            e.remove_obj()
        repository.npcs.clear()
        for e in repository.npcs_head:
            e.remove_obj()
        repository.npcs_head.clear()
        for e in repository.bcgrnd:
            e.remove_obj()
        repository.bcgrnd.clear()
        for e in repository.bcgrndC:
            e.remove_obj()
        repository.bcgrndC.clear()
        for e in repository.bcgrndI:
            e.remove_obj()
        repository.bcgrndI.clear()
        for e in repository.enemies:
            try:
                e.remove_obj()
            except:
                pass
        repository.enemies.clear()
        global house, path, castle, jorge
        # npcs-
        # repository.crt_npc(0, 0, 0, 0, type, True, window)
        repository.crt_npc(550, 725, 600, 775, 'pink', "roberta:", "female", True, window)

        # cave floor

        repository.crt_bcgrnd(-850, -1025, 2350, 2825, cave_floor, "cv_floor_1", False, window)

        # dungeon

        repository.crt_bcgrnd(-850, 825, 600, 2775, dungeon_floor, "cv_dungeon_floor", False, window)

        repository.crt_bcgrndC(-850, 825, 600, 875, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(550, 825, 600, 2475, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(550, 2625, 600, 2775, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-800, 2725, 600, 2775, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-850, 825, -800, 2775, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(550, 2575, 600, 2725, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(350, 2275, 550, 2325, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(300, 2325, 350, 2525, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-650, 2525, 350, 2575, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-650, 2275, -600, 2525, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-650, 2275, 150, 2325, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(250, 2225, 300, 2275, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(350, 2175, 400, 2225, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-800, 1625, 400, 1675, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-650, 1175, -600, 1425, dungeon_wall, "cv_dungeon_wall", False, window)
        repository.crt_bcgrndC(-650, 1425, 550, 1475, dungeon_wall, "cv_dungeon_wall", False, window)

        # dungeon furniture

        repository.crt_bcgrnd(-150, 975, 200, 1325, red_46, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrnd(-50, 1025, 0, 1275, red_58, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrnd(-100, 1075, 150, 1125, red_58, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrnd(50, 1025, 100, 1275, red_58, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrnd(-100, 1175, 150, 1225, red_58, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrnd(-50, 1075, 100, 1225, red_46, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(300, 1025, 550, 1125, red_58, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(300, 1125, 550, 1225, red_46, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(500, 1125, 550, 1225, white_dark, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(500, 1025, 550, 1125, white_light, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(250, 1025, 300, 1225, brown_32, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(250, 1125, 300, 1225, brown_27, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(100, 875, 200, 925, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(250, 875, 250, 925, brown_27, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(500, 875, 550, 975, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(500, 1275, 550, 1375, brown_27, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC( -600, 2375, -550, 2475, brown_27, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(-600, 1925, 350, 2025, red_46, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-550, 1925, 300, 2025, brown_27, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(-550, 1825, -500, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-450, 1825, -400, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-350, 1825, -300, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-250, 1825, -200, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-150, 1825, -100, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-50, 1825, 0, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(50, 1825, 100, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(150, 1825, 200, 1875, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(250, 1825, 300, 1875, brown_27, "cv_dungeon_furniture", False, window)

        repository.crt_bcgrndC(250, 2075, 300, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(150, 2075, 200, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(50, 2075, 100, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-50, 2075, 0, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-150, 2075, -100, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-250, 2075, -200, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-350, 2075, -300, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-450, 2075, -400, 2125, brown_27, "cv_dungeon_furniture", False, window)
        repository.crt_bcgrndC(-550, 2075, -500, 2125, brown_27, "cv_dungeon_furniture", False, window)

        # dungeon rocks

        repository.crt_bcgrndC(-500, 875, -300, 925, dungeon_wall, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-450, 925, -400, 975, dungeon_wall, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-400, 925, -350, 975, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-450, 975, -400, 1025, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-500, 875, -400, 925, dungeon_bricks_2E, "cv_dungeon_rock", False, window)

        repository.crt_bcgrnd(-500, 1175, -550, 1225, dungeon_bricks_26, "cv_dungeon_rock", False, window)

        repository.crt_bcgrnd(-250, 925, -200, 975, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-250, 1075, -200, 1125, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-250, 1075, -200, 1125, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-250, 1525, -200, 1625, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-750, 925, -700, 975, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-550, 1025, -500, 1075, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-550, 1125, -500, 1175, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-500, 1175, -450, 1225, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-400, 1175, -350, 1225, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-250, 1275, -200, 1325, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-200, 1225, -150, 1275, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(300, 1025, 350, 1075, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(350, 1525, 400, 1575, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(400, 1575, 450, 1625, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(450, 1725, 500, 1775, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(400, 1775, 450, 1825, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(150, 1725, 200, 1775, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-100, 1725, -50, 1775, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-500, 1675, -450, 1725, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-750, 1725, -700, 1825, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-800, 1875, -750, 1925, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-700, 2025, -650, 2075, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-800, 2075, -750, 2125, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-650,  2125, -600, 2175, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-700, 2175, -650, 2225, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-500, 2125, -450, 2175, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-800, 2325, -750, 2375, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-750, 2375, -700, 2425, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-700, 1525, -650, 1575, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-750, 2625, -700, 2675, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-600, 2575, -550, 2625, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-450, 2625, -400, 2675, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-300, 2575, -250, 2625, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-350, 2625, -300, 2675, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(50, 2675, 100, 2725, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(150, 2575, 200, 2625, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(450, 2675, 500, 2725, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(450, 2125, 400, 2175, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(350, 2175, 400, 2225, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(250, 2225, 300, 2275, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(150, 2225, 200, 2275, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-150, 2175, -100, 2225, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-500, 2125, -450, 2175, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(200, 2375, 250, 2425, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(250, 2475, 300, 2525, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(150, 2475, 200, 2525, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(50, 2375, 100, 2425, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-100, 2375, -50, 2425, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-200, 2475, -150, 2525, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-350, 2325, -300, 2425, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-400, 2475, -350, 2525, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-500, 2375, -450, 2475, dungeon_bricks_26, "cv_dungeon_rock", False, window)


        repository.crt_bcgrnd(150, 1125, 200, 1175, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(50, 1075, 100, 1125, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-50, 975, 0, 1025, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-150, 1275, -100, 1325, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-100, 1325, -50, 1375, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-400, 1275, -350, 1375, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-700, 1225, -650, 1275, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-800, 1175, -750, 1225, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-750, 1375, -700, 1425, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-700, 1525, -650, 1575, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-600, 1525, -550, 1575, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-450, 1525, -400, 1575, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(-200, 1475, -150, 1525, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(200, 875, 250, 925, dungeon_bricks_2E, "cv_dungeon_rock", False, window)

        repository.crt_bcgrnd(500, 1875, 550, 2025, dungeon_bricks_2E, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(450, 1925, 500, 2075, dungeon_bricks_2E, "cv_dungeon_rock", False, window)

        repository.crt_bcgrnd(450, 1975, 500, 2025, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(500, 1925, 550, 2075, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(500, 2025, 550, 2125, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(400, 2025, 450, 2075, dungeon_bricks_26, "cv_dungeon_rock", False, window)


        repository.crt_bcgrnd(-50, 975, 0, 1025, dungeon_bricks_26, "cv_dungeon_rock", False, window)

        repository.crt_bcgrnd(450, 2375, 500, 2425, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(500, 2425, 550, 2475, dungeon_bricks_26, "cv_dungeon_rock", False, window)
        repository.crt_bcgrnd(450, 2675, 500, 2725, dungeon_bricks_2E, "cv_dungeon_rock", False, window)

        # mud

        repository.crt_bcgrnd(1700, 325, 1750, 375, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1750, 375, 1950, 475, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1800, 475, 1950, 575, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1950, 375, 2100, 825, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1850, 575, 1950, 675, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1900, 625, 2000, 725, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(2000, 825, 2050, 975, cave_floor_2, "cv_mud", False, window)

        repository.crt_bcgrnd(1650, 2425, 1700, 2475, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1800, 2175, 1850, 2225, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1900, 1325, 1950, 1375, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1200, 1325, 1250, 1375, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1050, 2525, 1100, 2575, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1150, 1875, 1200, 1925, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(950, 1425, 1000, 1475, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1300, 1675, 1350, 1725, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1750, 1075, 1800, 1125, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1700, 575, 1750, 625, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1050, 425, 1100, 475, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(950, 575, 1000, 625, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(550, 525, 600, 575, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(750, -625, 800, -575, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(550, -875, 600, -825, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1900, -425, 1950, -375, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(1850, -375, 1900, -325, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(-300, -725, -250, -675, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(-350, -525, -300, -475, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(-200, -375, -150, -325, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(0, -375, 50, -325, cave_floor_2, "cv_mud", False, window)
        repository.crt_bcgrnd(0, 75, 50, 125, cave_floor_2, "cv_mud", False, window)

        # mineshaft

        repository.crt_bcgrndC(900, 1225, 1400, 1375, mineshaft1_cave, "cv_mineshaft", False, window)
        repository.crt_bcgrndC(900, 1275, 1400, 1325, mineshaft2_cave, "cv_mineshaft", False, window)
        repository.crt_bcgrndC(900, 1325, 1400, 1375, mineshaft3_cave, "cv_mineshaft", False, window)

        repository.crt_bcgrndC(2100, 425, 2150, 675, mineshaft1_cave, "cv_mineshaft", False, window)
        repository.crt_bcgrndC(2050, 425, 2100, 675, mineshaft2_cave, "cv_mineshaft", False, window)

        # pedras e minérios

        repository.crt_bcgrndC(1700, -375, 1750, -325, rubi_cave, "cv_rubi", False, window)
        repository.crt_bcgrndC(1750, -325, 1800, -275, rubi_cave, "cv_rubi", False, window)

        repository.crt_bcgrndC(1750, -675, 1800, -625, rubi_cave, "cv_rubi", False, window)

        repository.crt_bcgrndC(-150, -175, -100, -125, esmeralda_cave, "cv_esmeralda", False, window)
        repository.crt_bcgrndC(-700, -575, -650, 525, esmeralda_cave, "cv_esmeralda", False, window)
        repository.crt_bcgrndC(-700, -575, -650, 525, esmeralda_cave, "cv_esmeralda", False, window)

        repository.crt_bcgrndC(1550, 1125, 1600, 1175, ouro_cave, "cv_ouro", False, window)
        repository.crt_bcgrndC(2000, 1175, 2050, 1225, ouro_cave, "cv_ouro", False, window)
        repository.crt_bcgrndC(2050, 875, 2100, 925, ouro_cave, "cv_ouro", False, window)

        repository.crt_bcgrndC(1950, 375, 2000, 425, ouro_cave, "cv_ouro", False, window)

        repository.crt_bcgrndC(1750, 325, 1800, 375, dungeon_bricks_2E, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(1750, 1525, 1800, 1575, dungeon_bricks_2E, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(1750, 1575, 1800, 1625, dungeon_wall, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(1350, 1775, 1400, 1825, dungeon_bricks_2E, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(1800, 2075, 1850, 2125, dungeon_wall, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(2150, 1975, 2200, 2025, dungeon_floor, "cv_skull", False, window)

        repository.crt_bcgrndC(1250, 2425, 1300, 2475, dungeon_wall, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(1300, 2475, 1350, 2525, dungeon_wall, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(1300, 2375, 1350, 2424, dungeon_bricks_2E, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(2150, -825, 2200, -775, dungeon_bricks_2E, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(500, 275, 550, 325, dungeon_bricks_2E, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(850, 375, 900, 425, dungeon_bricks_2E, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(1100, 575, 1150, 625, dungeon_bricks_2E, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(800, 325, 850, 375, dungeon_wall, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(400, 375, 450, 425, dungeon_wall, "cv_grey_stone", False, window)
        repository.crt_bcgrndC(650, 675, 700, 725, dungeon_wall, "cv_grey_stone", False, window)

        repository.crt_bcgrndC(750, -825, 800, -775, cave_wall, "cv_brown_stone", False, window)
        repository.crt_bcgrndC(800, -875, 850, -825, cave_wall, "cv_brown_stone", False, window)
        repository.crt_bcgrndC(850, -825, 900, -775, cave_wall, "cv_brown_stone", False, window)

        repository.crt_bcgrndC(1300, 25, 1350, 75, cave_wall, "cv_brown_stone", False, window)
        repository.crt_bcgrndC(1350, -25, 1400, 25, cave_wall, "cv_brown_stone", False, window)

        # water

        repository.crt_bcgrndC(0, 475, 150, 525, cave_water1, "cv_water", False, window)
        repository.crt_bcgrndC(-150, 425, 0, 775, cave_water1, "cv_water", False, window)
        repository.crt_bcgrndC(-250, 375, -150, 725, cave_water1, "cv_water", False, window)
        repository.crt_bcgrndC(-350, 325, -250, 675, cave_water1, "cv_water", False, window)
        repository.crt_bcgrndC(-550, 275, -350, 625, cave_water1, "cv_water", False, window)
        repository.crt_bcgrndC(-800, 175, -550, 525, cave_water1, "cv_water", False, window)
        repository.crt_bcgrndC(-1850, 125, -800, 525, cave_water1, "cv_water", False, window)

        repository.crt_bcgrndC(0, 525, 150, 775, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-150, 475, 0, 725, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-250, 425, -150, 675, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-350, 375, -250, 625, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-550, 325, -350, 525, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-450, 525, -350, 575, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-650, 275, -550, 475, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-800, 225, -650, 475, cave_water2, "cv_water", False, window)
        repository.crt_bcgrndC(-1850, 175, -800, 525, cave_water2, "cv_water", False, window)

        repository.crt_bcgrndC(0, 575, 100, 725, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-150, 525, 0, 675, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-250, 475, -150, 625, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-350, 425, -250, 575, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-550, 375, -350, 475, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-450, 475, -350, 525, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-650, 325, -550, 425, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-800, 275, -650, 425, cave_water3, "cv_water", False, window)
        repository.crt_bcgrndC(-1850, 225, -800, 425, cave_water3, "cv_water", False, window)

        # cave walls

        repository.crt_bcgrndC(1600, -325, 1650, -275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1650, -375, 1700, -225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1700, -325, 1750, -175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1750, -275, 1800, -225, cave_wall, "cv_wall", False, window)


        repository.crt_bcgrndC(-300, -1025, 1500, -975, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1500, -975, 1600, -925, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1600, -925, 1650, -725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1650, -725, 1800, -675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1800, -675, 1850, -525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1850, -525, 2000, -475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2000, -675, 2050, -525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2050, -825, 2100, -675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2100, -875, 2250, -825, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2250, -825, 2300, -375, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2200, -375, 2250, -325, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2150, -325, 2200, -25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2050, -25, 2150, 25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2000, 25, 2050, 75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1850, 75, 2000, 125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1800, 125, 1850, 175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1700, 175, 1800, 225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1650, 225, 1700, 275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1700, 275, 1800, 325, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1800, 325, 2000, 375, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2000, 375, 2150, 425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2150, 425, 2200, 675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2100, 675, 2150, 925, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2050, 925, 2100, 1225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2000, 1225, 2050, 1375, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1950, 1375, 2000, 1725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2000, 1725, 2150, 1775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2150, 1775, 2200, 1975, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2200, 1975, 2250, 2175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2250, 2175, 2300, 2425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2100, 2425, 2250, 2475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(2000, 2475, 2100, 2525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1900, 2525, 2000, 2575, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1750, 2575, 1900, 2625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1700, 2625, 1750, 2725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1300, 2725, 1700, 2775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1150, 2675, 1300, 2725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(900, 2625, 1150, 2675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(650, 2675, 900, 2725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(600, 2625, 650, 2675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(600, 2625, 650, 2675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(600, 2325, 650, 2475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(650, 2275, 850, 2325, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(850, 2025, 900, 2275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(850, 1725, 900, 1775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(900, 1775, 950, 2025, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(800, 1425, 850, 1725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(750, 1575, 800, 1625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(850, 1225, 900, 1425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(900, 1175, 1050, 1225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1050, 1225, 1200, 1275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1200, 1175, 1400, 1225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1400, 1225, 1500, 1275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1500, 1125, 1550, 1225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1550, 975, 1600, 1125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1500, 725, 1550, 975, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1450, 675, 1500, 725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1400, 625, 1450, 675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1250, 575, 1400, 625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1200, 625, 1250, 725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1250, 725, 1300, 875, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1200, 875, 1250, 925, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1050, 925, 1200, 975, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(700, 875, 1050, 925, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(600, 825, 700, 875, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(450, 775, 600, 825, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(400, 725, 450, 775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(350, 675, 400, 725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(300, 425, 350, 675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(250, 325, 300, 425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(250, 275, 300, 425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(300, 125, 350, 275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(350, 25, 400, 125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(400, -75, 450, 25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(450, -125, 500, -75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(500, -275, 550, -125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(450, -325, 500, -275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(400, -275, 450, -175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(350, -175, 400, -75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(300, -75, 350, -25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(250, -25, 300, 75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(200, 75, 250, 225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(150, 225, 200, 575, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(100, 575, 150, 775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-200, 775, 100, 825, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-400, 725, -200, 775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-450, 625, -400, 725, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-550, 575, -450, 625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-800, 525, -550, 575, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-1850, 475, -800, 525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-1850, 75, -800, 125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-800, 125, -650, 175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-650, 175, -550, 225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-550, 225, -500, 275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-500, 175, -450, 225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-450, 125, -400, 175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-500, -75, -450, 125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-450, -125, -400, -75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-400, -325, -350, -125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-450, -375, -400, -325, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-500, -425, -450, -375, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-600, -475, -500, -425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-700, -525, -600, -475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-750, -775, -700, -525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-700, -825, -650, -775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-650, -875, -550, -825, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-550, -925, -450, -875, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-450, -975, -300, -925, cave_wall, "cv_wall", False, window)

        repository.crt_bcgrndC(-100, -825, 400, -775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-150, -775, -100, -675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-100, -675, -50, -625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-50, -625, 50, -575, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(50, -575, 150, -525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(150, -525, 450, -475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(450, -575, 500, -525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(500, -675, 550, -575, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(450, -725, 500, -675, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(400, -775, 450, -725, cave_wall, "cv_wall", False, window)

        repository.crt_bcgrndC(1150, -825, 1400, -775, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1400, -775, 1450, -575, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1350, -575, 1400, -325, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1200, -325, 1350, -275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1050, -275, 1200, -225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1000, -225, 1050, -25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1050, -25, 1200, 25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1200, 25, 1250, 175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1250, 175, 1450, 225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1450, 225, 1500, 275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1150, 275, 1450, 325, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1100, 225, 1150, 275, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(950, 175, 1100, 225, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(900, 125, 950, 175, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(850, 75, 900, 125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(800, -25, 850, 75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(750, -75, 800, -25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(800, -375, 750, -75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(850, -475, 800, -375, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(850, -525, 1000, -475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1000, -575, 1100, -525, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1100, -775, 1150, -575, cave_wall, "cv_wall", False, window)

        repository.crt_bcgrndC(-200 , -25, -50,  75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-150, -125, 0, -25, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-100, -175, -50,  75, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(-150, -125,  -100, 125, cave_wall, "cv_wall", False, window)

        repository.crt_bcgrndC(1400, 1525, 1600, 2075, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1350, 1825, 1400, 2025, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1450, 1475, 1750, 1625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1550, 1425, 1750, 1625, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1650, 1375, 1750, 1425, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1750, 1625, 1800, 2075, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1600, 1875, 1850, 2125, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1600, 1375, 1800, 1475, cave_wall, "cv_wall", False, window)
        repository.crt_bcgrndC(1650, 1325, 1750, 1625, cave_wall, "cv_wall", False, window)


        # void

        repository.crt_bcgrnd(1650, -325, 1700, -275, void, "cv_void", False, window)
        repository.crt_bcgrnd(1700, -275, 1750, -225, void, "cv_void", False, window)


        repository.crt_bcgrnd(-1850, -2025, 3350, -1025, void, "cv_void", False, window)
        repository.crt_bcgrnd(-150, -25, -100, 75, void, "cv_void", False, window)
        repository.crt_bcgrnd(-100, -125, -50, -25, void, "cv_void", False, window)

        repository.crt_bcgrnd(1600, 1550, 1700, 2075, void, "cv_void", False, window)
        repository.crt_bcgrnd(1600, 1875, 1800, 2075, void, "cv_void", False, window)
        repository.crt_bcgrnd(1700, 1625, 1750, 2075, void, "cv_void", False, window)
        repository.crt_bcgrnd(1400, 1825, 1550, 2025, void, "cv_void", False, window)
        repository.crt_bcgrnd(1450, 1525, 1550, 2025, void, "cv_void", False, window)
        repository.crt_bcgrnd(1550, 1475, 1700, 2025, void, "cv_void", False, window)
        repository.crt_bcgrnd(1600, 1425, 1750, 1475, void, "cv_void", False, window)
        repository.crt_bcgrnd(1650, 1375, 1750, 1425, void, "cv_void", False, window)
        repository.crt_bcgrnd(-1850, 525, -850, 4625, void, "cv_void", False, window)
        repository.crt_bcgrnd(-900, 2775, 4350, 4825, void, "cv_void", False, window)
        repository.crt_bcgrnd(2300, -1975, 4350, 4825, void, "cv_void", False, window)
        repository.crt_bcgrnd(-1850, -2025, -850, 75, void, "cv_void", False, window)

        repository.crt_bcgrnd(-850, -1025, -300, -975, void, "cv_void", False, window)
        repository.crt_bcgrnd(-850, -1025, -400, -925, void, "cv_void", False, window)
        repository.crt_bcgrnd(-850, -925, -550, -875, void, "cv_void", False, window)
        repository.crt_bcgrnd(-850, -925, -600, -825, void, "cv_void", False, window)
        repository.crt_bcgrnd(-850, -925, -700, -775, void, "cv_void", False, window)
        repository.crt_bcgrnd(-850, -925, -750, 75, void, "cv_void", False, window)
        repository.crt_bcgrnd(-750, -525, -700, 75, void, "cv_void", False, window)
        repository.crt_bcgrnd(-700, -475, -650, 125, void, "cv_void", False, window)
        repository.crt_bcgrnd(-650, -425, -500, 175, void, "cv_void", False, window)
        repository.crt_bcgrnd(-650, 75, -500, 175, void, "cv_void", False, window)
        repository.crt_bcgrnd(-550, 125, -500, 225, void, "cv_void", False, window)
        repository.crt_bcgrnd(-550, 125, -450, 175, void, "cv_void", False, window)
        repository.crt_bcgrnd(-800, 75, -500, 125, void, "cv_void", False, window)
        repository.crt_bcgrnd(-700, -475, -600, -425, void, "cv_void", False, window)
        repository.crt_bcgrnd(-500, -325, -400, -125, void, "cv_void", False, window)
        repository.crt_bcgrnd(-550, -375, -450, -75, void, "cv_void", False, window)
        repository.crt_bcgrnd(-850, 625, -450, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(-800, 575, -550, 625, void, "cv_void", False, window)
        repository.crt_bcgrnd(-450, 725, -400, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(-450, 775, -200, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(-950, 525, -800, 825, void, "cv_void", False, window)

        repository.crt_bcgrnd(450, -275, 500, -125, void, "cv_void", False, window)
        repository.crt_bcgrnd(400, -175, 450, -75, void, "cv_void", False, window)
        repository.crt_bcgrnd(350, -75, 400, 25, void, "cv_void", False, window)
        repository.crt_bcgrnd(300, -25, 350, 125, void, "cv_void", False, window)
        repository.crt_bcgrnd(250, 75, 300, 275, void, "cv_void", False, window)
        repository.crt_bcgrnd(200, 225, 250, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(250, 425, 300, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(150, 575, 300, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(100, 775, 450, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(350, 725, 400, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(300, 675, 350, 825, void, "cv_void", False, window)
        repository.crt_bcgrnd(800, 1725, 850, 2275, void, "cv_void", False, window)

        repository.crt_bcgrnd(600, 875, 700, 2275, void, "cv_void", False, window)
        repository.crt_bcgrnd(600, 2275, 650, 2325, void, "cv_void", False, window)
        repository.crt_bcgrnd(700, 925, 800, 2275, void, "cv_void", False, window)
        repository.crt_bcgrnd(800, 1725, 800, 2275, void, "cv_void", False, window)
        repository.crt_bcgrnd(850, 1775, 900, 2025, void, "cv_void", False, window)
        repository.crt_bcgrnd(700, 925, 850, 1425, void, "cv_void", False, window)
        repository.crt_bcgrnd(700, 925, 900, 1225, void, "cv_void", False, window)
        repository.crt_bcgrnd(700, 925, 1050, 1175, void, "cv_void", False, window)
        repository.crt_bcgrnd(650, 975, 1550, 1125, void, "cv_void", False, window)
        repository.crt_bcgrnd(1050, 1125, 1200, 1225, void, "cv_void", False, window)
        repository.crt_bcgrnd(1200, 925, 1300, 1175, void, "cv_void", False, window)
        repository.crt_bcgrnd(1200, 925, 1500, 1175, void, "cv_void", False, window)
        repository.crt_bcgrnd(1450, 725, 1500, 1225, void, "cv_void", False, window)
        repository.crt_bcgrnd(1250, 625, 1400, 725, void, "cv_void", False, window)
        repository.crt_bcgrnd(1300, 675, 1450, 1175, void, "cv_void", False, window)
        repository.crt_bcgrnd(1400, 1175, 1500, 1225, void, "cv_void", False, window)
        repository.crt_bcgrnd(1250, 875, 1450, 1175, void, "cv_void", False, window)

        repository.crt_bcgrnd(1500, -1025, 2350, -975, void, "cv_void", False, window)
        repository.crt_bcgrnd(1600, -975, 2350, -925, void, "cv_void", False, window)
        repository.crt_bcgrnd(1650, -925, 2350, -875, void, "cv_void", False, window)
        repository.crt_bcgrnd(1650, -875, 2100, -825, void, "cv_void", False, window)
        repository.crt_bcgrnd(1800, -725, 2050, -675, void, "cv_void", False, window)
        repository.crt_bcgrnd(1850, -675, 2000, -525, void, "cv_void", False, window)
        repository.crt_bcgrnd(2250, -875, 2300, -825, void, "cv_void", False, window)
        repository.crt_bcgrnd(1650, -825, 2050, -725, void, "cv_void", False, window)

        repository.crt_bcgrnd(2300, -975, 2350, 2825, void, "cv_void", False, window)
        repository.crt_bcgrnd(2250, -375, 2300, 525, void, "cv_void", False, window)
        repository.crt_bcgrnd(2200, -325, 2300, 525, void, "cv_void", False, window)
        repository.crt_bcgrnd(2150, -25, 2200, 425, void, "cv_void", False, window)
        repository.crt_bcgrnd(2050, 25, 2150, 375, void, "cv_void", False, window)
        repository.crt_bcgrnd(2000, 75, 2150, 375, void, "cv_void", False, window)
        repository.crt_bcgrnd(1850, 125, 2000, 325, void, "cv_void", False, window)
        repository.crt_bcgrnd(1800, 175, 1850, 325, void, "cv_void", False, window)
        repository.crt_bcgrnd(1700, 225, 1800, 275, void, "cv_void", False, window)
        repository.crt_bcgrnd(1700, 225, 1800, 275, void, "cv_void", False, window)
        repository.crt_bcgrnd(2200, 475, 2350, 1975, void, "cv_void", False, window)
        repository.crt_bcgrnd(2250, 1975, 2350, 2175, void, "cv_void", False, window)

        repository.crt_bcgrnd(2150, 675, 2350, 1725, void, "cv_void", False, window)
        repository.crt_bcgrnd(2100, 925, 2350, 1725, void, "cv_void", False, window)
        repository.crt_bcgrnd(2050, 1225, 2350, 1725, void, "cv_void", False, window)
        repository.crt_bcgrnd(2000, 1375, 2350, 1725, void, "cv_void", False, window)
        repository.crt_bcgrnd(2150, 1725, 2200, 1775, void, "cv_void", False, window)

        repository.crt_bcgrnd(2250, 2425, 2350, 2825, void, "cv_void", False, window)
        repository.crt_bcgrnd(2100, 2475, 2350, 2825, void, "cv_void", False, window)
        repository.crt_bcgrnd(2000, 2525, 2350, 2825, void, "cv_void", False, window)
        repository.crt_bcgrnd(1900, 2575, 2350, 2825, void, "cv_void", False, window)
        repository.crt_bcgrnd(1750, 2625, 2350, 2825, void, "cv_void", False, window)
        repository.crt_bcgrnd(1700, 2725, 2350, 2825, void, "cv_void", False, window)

        repository.crt_bcgrnd(600, 2675, 650, 2725, void, "cv_void", False, window)
        repository.crt_bcgrnd(600, 2725, 1300, 2775, void, "cv_void", False, window)
        repository.crt_bcgrnd(900, 2675, 1150, 2725, void, "cv_void", False, window)

        repository.crt_bcgrnd(1150, -775, 1400, -575, void, "cv_void", False, window)
        repository.crt_bcgrnd(1100, -575, 1350, -525, void, "cv_void", False, window)
        repository.crt_bcgrnd(1000, -525, 1350, -325, void, "cv_void", False, window)
        repository.crt_bcgrnd(950, -475, 1200, -275, void, "cv_void", False, window)
        repository.crt_bcgrnd(850, -475, 1050, -225, void, "cv_void", False, window)
        repository.crt_bcgrnd(800, -375, 1000, -75, void, "cv_void", False, window)
        repository.crt_bcgrnd(800, -75, 1000, -25, void, "cv_void", False, window)
        repository.crt_bcgrnd(850, -25, 1050, 75, void, "cv_void", False, window)
        repository.crt_bcgrnd(900, 25, 1200, 125, void, "cv_void", False, window)
        repository.crt_bcgrnd(950, 125, 1200, 175, void, "cv_void", False, window)
        repository.crt_bcgrnd(1100, 175, 1250, 225, void, "cv_void", False, window)
        repository.crt_bcgrnd(1150, 225, 1450, 275, void, "cv_void", False, window)

        repository.crt_bcgrnd(-100, -775, 400, -675, void, "cv_void", False, window)
        repository.crt_bcgrnd(-50, -725, 450, -625, void, "cv_void", False, window)
        repository.crt_bcgrnd(50, -675, 500, -575, void, "cv_void", False, window)
        repository.crt_bcgrnd(150, -575, 450, -525, void, "cv_void", False, window)

def mansion(b, window):
    if b:
        repository.mansion_map = True
        repository.forest_map = False
        repository.city_map = False
        repository.cave_map = False
        try:
            repository.forest_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_PURGE)
        except:
            pass
        repository.city_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_LOOP)
        # clearing the screen for new map:
        for e in repository.npcs:
            e.remove_obj()
        repository.npcs.clear()
        for e in repository.npcs_head:
            e.remove_obj()
        repository.npcs_head.clear()
        for e in repository.bcgrnd:
            e.remove_obj()
        repository.bcgrnd.clear()
        for e in repository.bcgrndC:
            e.remove_obj()
        repository.bcgrndC.clear()
        for e in repository.bcgrndI:
            e.remove_obj()
        repository.bcgrndI.clear()
        for e in repository.enemies:
            try:
                e.remove_obj()
            except:
                pass
        repository.enemies.clear()

        # gate:
        repository.crt_bcgrndC(-2500, -2575, -1400, 4300, tree, "barrier_w_1", False, window)

        # map barrier w:
        repository.crt_bcgrndC(-2500, -2575, -1400, 4300, tree, "barrier_w_1", False, window)
        repository.crt_bcgrndC(-1400,  -2575, -1250, -525, tree, "barrier_w_2,1", False, window)
        repository.crt_bcgrndC(-1400, -225, -1000, 275, tree, "barrier_w_2,2", False, window)
        repository.crt_bcgrndC(-1400, 275, -1050, 325, tree, "barrier_w_2,3", False, window)
        repository.crt_bcgrndC(-1400, 325, -1100, 4000, tree, "barrier_w_2,4", False, window)
        repository.crt_bcgrndC(-1250, -2575, -1200, -2475, tree, "barrier_w_3,1", False, window)
        repository.crt_bcgrndC(-1200, -2575, -1150, -2525, tree, "barrier_w_3,2", False, window)
        repository.crt_bcgrndC(-1250, -2025, -1200, -1925, tree, "barrier_w_3,3", False, window)
        repository.crt_bcgrndC(-1200, -1975, -1150, -1925, tree, "barrier_w_3,4", False, window)
        repository.crt_bcgrndC(-1250, -1925, -1100, -725, tree, "barrier_w_3,5", False, window)
        repository.crt_bcgrndC(-1100, -1925, -1050, -1325, tree, "barrier_w_3,6", False, window)
        repository.crt_bcgrndC(-1050, -1825, -1000, -1425, tree, "barrier_w_3,7", False, window)
        repository.crt_bcgrndC(-1000, -1775, -950, -1575, tree, "barrier_w_3,8", False, window)
        repository.crt_bcgrndC(-1100, -1275, -1050, -825, tree, "barrier_w_3,9", False, window)
        repository.crt_bcgrndC(-1050, -1225, -1000, -875, tree, "barrier_w_3,10", False, window)
        repository.crt_bcgrndC(-1000, -1175, -950, -1025, tree, "barrier_w_3,11", False, window)
        repository.crt_bcgrndC(-1000, -975, -950, -925, tree, "barrier_w_3,12", False, window)
        repository.crt_bcgrndC(-1100, -775, -1050, -725, tree, "barrier_w_3,13", False, window)
        repository.crt_bcgrndC(-1250, -725, -1000, -525, tree, "barrier_w_3,14", False, window)
        repository.crt_bcgrndC(-1200, -525, -1100, -475, tree, "barrier_w_3,15", False, window)

        # map barrier s:
        repository.crt_bcgrnd(-1400, 3025, 2100, 4200, tree, "barrier_s_1,1", False, window)
        repository.crt_bcgrndC(2100, 3075, 2150, 3975, tree, "barrier_s_1,2", False, window)
        repository.crt_bcgrndC(2150, 3425, 2200, 3975, tree, "barrier_s_1,3", False, window)
        repository.crt_bcgrndC(2200, 3575, 2250, 3975, tree, "barrier_s_1,3", False, window)
        repository.crt_bcgrndC(-800, 2975, 2050, 3025, tree, "barrier_s_2", False, window)

        # map barrier n:
        repository.crt_bcgrndC(-2500,  -3575, 1950, -2575, tree, "barrier_n_1", False, window)
        repository.crt_bcgrndC(-800, -2575, -750, -2525, tree, "barrier_n_2,1", False, window)
        repository.crt_bcgrndC(-750, -2575, -700, -2475, tree, "barrier_n_2,2", False, window)
        repository.crt_bcgrndC(-700, -2575, -650,  -2425, tree, "barrier_n_2,3", False, window)
        repository.crt_bcgrndC(-650, -2575, 1950, -2375, tree, "barrier_n_2,4", False, window)
        repository.crt_bcgrndC(-600, -2375, -50, -2325, tree, "barrier_n_2,5", False, window)
        repository.crt_bcgrndC(-550, -2325, -150, -2275, tree, "barrier_n_2,6", False, window)
        repository.crt_bcgrndC(50, -2375, 400, -2325, tree, "barrier_n_2,7", False, window)
        repository.crt_bcgrndC(600, -2325, 800, -2275, tree, "barrier_n_2,8", False, window)
        repository.crt_bcgrndC(500, -2375, 1900, -2325, tree, "barrier_n_2,9", False, window)
        repository.crt_bcgrndC(1000, -2325, 1750, -2275, tree, "barrier_n_2,10", False, window)

        # map barrier e:
        repository.crt_bcgrnd(1950, -3300, 2750, -2275, water4, "water_barrier_e_4,1", False, window)
        repository.crt_bcgrnd(2050, -2275, 2750, -2025, water4, "water_barrier_e_4,1", False, window)
        repository.crt_bcgrnd(2250, -3225, 2750, 925, water4, "water_barrier_e_4,2", False, window)
        repository.crt_bcgrnd(2300, 925, 2750, 3925, water4, "water_barrier_e_4,3", False, window)
        repository.crt_bcgrnd(2650, -3625, 3750, 3925, water4, "water_barrier_e_4,3", False, window)

        repository.crt_bcgrndC(1900, -2475, 1950, -2375, water1, "water_barrier_e_1,1", False, window)
        repository.crt_bcgrndC(1950, -2375, 2000, -2275, water1, "water_barrier_e_1,2", False, window)
        repository.crt_bcgrndC(2000, -2275, 2050, -2225, water1, "water_barrier_e_1,3", False, window)
        repository.crt_bcgrndC(2050, -2225, 2100, -2025, water1, "water_barrier_e_1,4", False, window)
        repository.crt_bcgrndC(2100, -2025, 2150, -1675, water1, "water_barrier_e_1,5", False, window)
        repository.crt_bcgrndC(2150, -1675, 2200, -625, water1, "water_barrier_e_1,6", False, window)
        repository.crt_bcgrndC(2150, -625, 2200, -325, water1, "water_barrier_e_1,7", False, window)
        repository.crt_bcgrndC(2150, -325, 2200, 75, water1, "water_barrier_e_1,8", False, window)
        repository.crt_bcgrndC(2200, 75, 2250, 525, water1, "water_barrier_e_1,9", False, window)
        repository.crt_bcgrndC(2250, 525, 2300, 925, water1, "water_barrier_e_1,10", False, window)
        repository.crt_bcgrndC(2300, 925, 2350, 1525, water1, "water_barrier_e_1,11", False, window)
        repository.crt_bcgrndC(2250, 1525, 2300, 1925, water1, "water_barrier_e_1,12", False, window)
        repository.crt_bcgrndC(2200, 1925, 2250, 2325, water1, "water_barrier_e_1,13", False, window)
        repository.crt_bcgrndC(2250, 2325, 2300, 2725, water1, "water_barrier_e_1,14", False, window)
        repository.crt_bcgrndC(2200, 2725, 2250, 3525, water1, "water_barrier_e_1,15", False, window)
        repository.crt_bcgrndC(2250, 3525, 2300, 3925, water1, "water_barrier_e_1,16", False, window)

        repository.crt_bcgrnd(1950, -2475, 2000, -2375, water2, "water_barrier_e_2,1", False, window)
        repository.crt_bcgrnd(2000, -2375, 2050, -2275, water2, "water_barrier_e_2,2", False, window)
        repository.crt_bcgrnd(2050, -2275, 2100, -2225, water2, "water_barrier_e_2,3", False, window)
        repository.crt_bcgrnd(2100, -2225, 2150, -2025, water2, "water_barrier_e_2,4", False, window)
        repository.crt_bcgrnd(2150, -2025, 2200, -1675, water2, "water_barrier_e_2,err", False, window)
        repository.crt_bcgrnd(2200, -1675, 2250, -625, water2, "water_barrier_e_2,5", False, window)
        repository.crt_bcgrnd(2200, -625, 2300, -325, water2, "water_barrier_e_2,6", False, window)

        repository.crt_bcgrnd(2250, -625, 2300, -325, water3, "water_barrier_e_2,6", False, window)

        repository.crt_bcgrnd(2200, -325, 2250, 75, water2, "water_barrier_e_2,7", False, window)
        repository.crt_bcgrnd(2250, 75, 2300, 525, water2, "water_barrier_e_2,8", False, window)
        repository.crt_bcgrnd(2300, 525, 2350, 925, water2, "water_barrier_e_2,9", False, window)
        repository.crt_bcgrnd(2350,  925, 2400, 1525, water2, "water_barrier_e_2,10", False, window)
        repository.crt_bcgrnd(2300, 1525, 2350, 1925, water2, "water_barrier_e_2,11", False, window)
        repository.crt_bcgrnd(2250, 1925, 2300, 2325, water2, "water_barrier_e_2,12", False, window)
        repository.crt_bcgrnd(2300, 2325, 2350, 2725, water2, "water_barrier_e_2,13", False, window)
        repository.crt_bcgrnd(2250, 2725, 2300, 3525, water2, "water_barrier_e_2,14", False, window)
        repository.crt_bcgrnd(2300, 3525, 2350, 3925, water2, "water_barrier_e_2,14", False, window)

        repository.crt_bcgrnd(1950, -3300, 2000, -2475, water3, "water_barrier_e_3,1", False, window)
        repository.crt_bcgrnd(2000, -2475, 2050, -2375, water3, "water_barrier_e_3,2", False, window)
        repository.crt_bcgrnd(2050, -2375, 2100, -2275, water3, "water_barrier_e_3,3", False, window)
        repository.crt_bcgrnd(2100, -2275, 2150, -2225, water3, "water_barrier_e_3,4", False, window)
        repository.crt_bcgrnd(2150, -2225, 2200, -2025, water3, "water_barrier_e_3,5", False, window)
        repository.crt_bcgrnd(2200, -2025, 2250, -1675, water3, "water_barrier_e_3,6", False, window)
        repository.crt_bcgrnd(2250, -1675, 2300, -625, water3, "water_barrier_e_3,7", False, window)
        repository.crt_bcgrnd(2250, -325, 2300, 75, water3, "water_barrier_e_3,8", False, window)
        repository.crt_bcgrnd(2300, 75, 2350, 525, water3, "water_barrier_e_3,9", False, window)
        repository.crt_bcgrnd(2350, 525, 2400, 925, water3, "water_barrier_e_3,10", False, window)
        repository.crt_bcgrnd(2400, 925, 2450, 1525, water3, "water_barrier_e_3,11", False, window)
        repository.crt_bcgrnd(2350, 1525, 2400,  1925, water3, "water_barrier_e_3,11", False, window)
        repository.crt_bcgrnd(2300, 1925, 2350, 2325, water3, "water_barrier_e_3,12", False, window)
        repository.crt_bcgrnd(2350, 2325, 2400, 2725, water3, "water_barrier_e_3,13", False, window)
        repository.crt_bcgrnd(2300, 2725, 2350, 3525, water3, "water_barrier_e_3,14", False, window)
        repository.crt_bcgrnd(2350, 3525, 2400, 3925, water3, "water_barrier_e_3,15", False, window)

        # flores

        repository.crt_bcgrnd(-700, -1025, 300, -625, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(-700, -1025, 350, -675, tree, "flores_mansion", False, window)

        repository.crt_bcgrnd(-650, -1025, 300, -675, violets, "flores_mansion", False, window)

        repository.crt_bcgrnd(-650, -975, 300, -925, white_flower, "flores_mansion", False, window)
        repository.crt_bcgrnd(-650, -875, 300, -825, white_flower, "flores_mansion", False, window)
        repository.crt_bcgrnd(-650, -775, 300, -725, white_flower, "flores_mansion", False, window)

        repository.crt_bcgrnd(-600, -1025, -550, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(-500, -1025, -450, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(-400, -1025, -350, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(-300, -1025, -250, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(-200, -1025, -150, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(-100, -1025, -50, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(0, -1025, 50, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(100, -1025, 150, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(200, -1025, 250, -675, tree, "flores_mansion", False, window)

        #

        repository.crt_bcgrnd(950, -1025, 1950, -625, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(900, -1025, 1950, -675, tree, "flores_mansion", False, window)

        repository.crt_bcgrnd(950, -1025, 1900, -675, violets, "flores_mansion", False, window)

        repository.crt_bcgrnd(950, -975, 1900, -925, white_flower, "flores_mansion", False, window)
        repository.crt_bcgrnd(950, -875, 1900, -825, white_flower, "flores_mansion", False, window)
        repository.crt_bcgrnd(950, -775, 1900, -725, white_flower, "flores_mansion", False, window)

        repository.crt_bcgrnd(1000, -1025, 1050, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1100, -1025, 1150, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1200, -1025, 1250, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1300, -1025, 1350, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1400, -1025, 1450, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1500, -1025, 1550, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1600, -1025, 1650, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1700, -1025, 1750, -675, tree, "flores_mansion", False, window)
        repository.crt_bcgrnd(1800, -1025, 1850, -675, tree, "flores_mansion", False, window)

        # mansão escada

        repository.crt_bcgrndC(350, -1025, 400, -875, invis_wall, "mansion_stairs", False, window)
        repository.crt_bcgrndC(850, -1025, 900, -875, invis_wall, "mansion_stairs", False, window)

        repository.crt_bcgrnd(350, -1025, 900, -975, mansion_stair3, "mansion_stairs", False, window)
        repository.crt_bcgrnd(400, -1025, 850, -975, mansion_stair4, "mansion_stairs", False, window)
        repository.crt_bcgrnd(350, -975, 900, -925, mansion_stair2, "mansion_stairs", False, window)
        repository.crt_bcgrnd(400, -975, 850, -925, mansion_stair5, "mansion_stairs", False, window)
        repository.crt_bcgrnd(350, -925, 900, -875, mansion_stair1, "mansion_stairs", False, window)
        repository.crt_bcgrnd(400, -925, 850, -875, mansion_stair6, "mansion_stairs", False, window)

        # plantas na estrada

        repository.crt_bcgrnd(350, -875, 900, -825, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, -775, 900, -725, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, -675, 900, -625, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(300, -626, 350, -575, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(900, -625, 950, -575, tree, "platas_estrada", False, window)

        repository.crt_bcgrnd(250, -575, 300, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(150, -575, 200, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(50, -575, 100, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-50, -575, 0, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-150, -575, -100, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-250, -575, -200, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-350, -575, -300, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-450, -575, -400, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-550, -575, -500, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-650, -575, -600, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-750, -575, -700, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-850, -575, -800, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(-950, -575, -900, -175, tree, "platas_estrada", False, window)

        repository.crt_bcgrnd(950, -575, 1000, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1050, -575, 1100, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1150, -575, 1200, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1250, -575, 1300, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1350, -575, 1400, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1450, -575, 1500, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1550, -575, 1600, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1650, -575, 1700, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1750, -575, 1800, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1850, -575, 1900, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1950, -575, 2000, -175, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(2050, -575, 2100, -175, tree, "platas_estrada", False, window)

        repository.crt_bcgrnd(300, -175, 350, -125, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(900, -175, 950, -125, tree, "platas_estrada", False, window)

        repository.crt_bcgrnd(350, -125, 900, -75, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, -25, 900, 25, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, 75, 900, 125, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, 175, 900, 225, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, 275, 900, 325, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, 375, 950, 425, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(900, 225, 950, 425, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(350, 475, 900, 525, tree, "platas_estrada", False, window)

        repository.crt_bcgrnd(1350, 225, 1450, 425, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1450, 175, 1500, 475, tree, "platas_estrada", False, window)
        repository.crt_bcgrnd(1500, 125, 2100, 525, tree, "platas_estrada", False, window)

        # estrada

        repository.crt_bcgrnd(400, -875, 850, 575, road_mansion, "mansao_estrada", False, window)

        repository.crt_bcgrnd(450, 575, 800, 625, road_mansion, "mansao_estrada", False, window)
        repository.crt_bcgrnd(500, 475, 750, 675, road_mansion, "mansao_estrada", False, window)

        repository.crt_bcgrnd(350, -575, 900, -175, road_mansion, "mansao_estrada", False, window)

        repository.crt_bcgrnd(-1300, -525, 2150, -225, road_mansion, "mansao_estrada", False, window)

        repository.crt_bcgrndC(-1200, -525, -1100, -475, tree, "mansao_estrada_entrada", False, window)

        repository.crt_bcgrndC(-1400, -575, -1300, -175, void, "mansao_estrada_entrada", False, window)
        repository.crt_bcgrndC(-1400, -525, -1300, -225, mansion_stair6, "mansao_estrada_entrada", False, window)
        repository.crt_bcgrndC(-1350, -525, -1300, -225, mansion_stair8, "mansao_estrada_entrada", False, window)

        # shed

        repository.crt_bcgrnd(1600, 175, 1850, 225, white_flower, "mansao_flores", False, window)
        repository.crt_bcgrnd(1650, 175, 1700, 225, yellow_flower, "mansao_flores", False, window)
        repository.crt_bcgrnd(1750, 175, 1800, 225, yellow_flower, "mansao_flores", False, window)

        repository.crt_bcgrnd(1600, 425, 1850, 475, white_flower, "mansao_flores", False, window)
        repository.crt_bcgrnd(1650, 425, 1700, 475, yellow_flower, "mansao_flores", False, window)
        repository.crt_bcgrnd(1750, 425, 1800, 475, yellow_flower, "mansao_flores", False, window)

        repository.crt_bcgrndC(1850, 175, 2100, 475, shed1, "mansao_shed", False, window)
        repository.crt_bcgrndC(1900, 175, 2050, 475, shed2, "mansao_shed", False, window)
        repository.crt_bcgrndC(1950, 175, 2000, 475, shed3, "mansao_shed", False, window)

        # cemitério

        repository.crt_bcgrnd(-1150, -2175, -1100, -2025, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-1150, -2075, -1100, -2025, grave_stone, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(-1050, -2175, -1000, -2025, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-1050, -2075, -1000, -2025, grave_stone, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(-950, -2175, -900, -2025, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-950, -2075, -900, -2025, grave_stone, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(-850, -2175, -800, -2025, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-850, -2075, -800, -2025, grave_stone, "mansao_cemiterio", False, window)

        #

        repository.crt_bcgrnd(-1150, -2475, -1100, -2325, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-1150, -2475, -1100, -2425, grave_stone, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(-1050, -2475, -1000, -2325, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-1050, -2475, -1000, -2425, grave_stone, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(-950, -2475, -900, -2325, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-950, -2475, -900, -2425, grave_stone, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(-850, -2475, -800, -2325, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrndC(-850, -2475, -800, -2425, grave_stone, "mansao_cemiterio", False, window)

        # flores labirinto

        repository.crt_bcgrnd(950, 925, 1950, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(900, 975, 1950, 1325, tree, "flores_labirinto", False, window)

        repository.crt_bcgrnd(950, 975, 1900, 1325, roses, "flores_labirinto", False, window)

        repository.crt_bcgrnd(950, 1025, 1900, 1075, white_flower, "flores_labirinto", False, window)
        repository.crt_bcgrnd(950, 1125, 1900, 1175, white_flower, "flores_labirinto", False, window)
        repository.crt_bcgrnd(950, 1225, 1900, 1275, white_flower, "flores_labirinto", False, window)

        repository.crt_bcgrnd(1000, 975, 1050, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1100, 975, 1150, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1200, 975, 1250, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1300, 975, 1350, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1400, 975, 1450, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1500, 975, 1550, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1600, 975, 1650, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1700, 975, 1750, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(1800, 975, 1850, 1325, tree, "flores_labirinto", False, window)

        #

        repository.crt_bcgrnd(-700, 925, 300, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-700, 975, 350, 1325, tree, "flores_labirinto", False, window)

        repository.crt_bcgrnd(-650, 975, 300, 1325, roses, "flores_labirinto", False, window)

        repository.crt_bcgrnd(-650, 1025, 300, 1075, white_flower, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-650, 1125, 300, 1175, white_flower, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-650, 1225, 300, 1275, white_flower, "flores_labirinto", False, window)

        repository.crt_bcgrnd(-600, 975, -550, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-500, 975, -450, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-400, 975, -350, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-300, 975, -250, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-200, 975, -150, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(-100, 975, -50, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(0, 975, 50, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(100, 975, 150, 1325, tree, "flores_labirinto", False, window)
        repository.crt_bcgrnd(200, 975, 250, 1325, tree, "flores_labirinto", False, window)

        # arvores

        repository.crt_bcgrndC(-800, 1275, -750, 1325, tree, "arvores", False, window)
        repository.crt_bcgrndC(-850, 1225, -800, 1325, tree, "arvores", False, window)
        repository.crt_bcgrndC(-900, 1125, -850, 1325, tree, "arvores", False, window)
        repository.crt_bcgrndC(-950, 1025, -900, 1325, tree, "arvores", False, window)
        repository.crt_bcgrndC(-1000, 925, -950, 1325, tree, "arvores", False, window)
        repository.crt_bcgrndC(-1050, 875, -1000, 1325, tree, "arvores", False, window)
        repository.crt_bcgrndC(-1100, 475, -1050, 1325, tree, "arvores", False, window)

        repository.crt_bcgrndC(-1050, 575, -1000, 825, tree, "arvores", False, window)

        repository.crt_bcgrndC(-750, 625, -600, 875, tree, "arvores", False, window)
        repository.crt_bcgrndC(-800, 675, -550, 825, tree, "arvores", False, window)

        repository.crt_bcgrndC(-550, -25, -400, 225, tree, "arvores", False, window)
        repository.crt_bcgrndC(-600, 25, -350, 175, tree, "arvores", False, window)

        repository.crt_bcgrndC(-50, 225, 100, 475, tree, "arvores", False, window)
        repository.crt_bcgrndC(-100, 275, 150, 425, tree, "arvores", False, window)

        repository.crt_bcgrndC(250, 625, 400, 875, tree, "arvores", False, window)
        repository.crt_bcgrndC(200, 675, 450, 825, tree, "arvores", False, window)

        repository.crt_bcgrndC(1250, 625, 1400, 875, tree, "arvores", False, window)
        repository.crt_bcgrndC(1200, 675, 1450, 825, tree, "arvores", False, window)

        repository.crt_bcgrndC(1100, -75, 1250, 175, tree, "arvores", False, window)
        repository.crt_bcgrndC(1050, -25, 1300, 125, tree, "arvores", False, window)

        # estradas de terra

        repository.crt_bcgrnd(550, 675, 700, 1375, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrnd(500, 1275, 750, 1325, dirt_path, "mansao_cemiterio", False, window)

        repository.crt_bcgrnd(850, 225, 900, 425, dirt_path, "mansao_cemiterio", False, window)
        repository.crt_bcgrnd(900, 275, 1850, 375, dirt_path, "mansao_cemiterio", False, window)

        # labirinto

        repository.crt_bcgrndC(-1200, 1325, -850, 3025, tree, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-850, 1325, 550, 1375, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-850, 1325, -800, 3025, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(700, 1325, 2100, 1375, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(2050, 1375, 2100, 3025, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-800, 2975, 2100, 3025, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(450, 1475, 800, 1525, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(450, 1525, 500, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(100, 1625, 500, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(100, 1625, 150, 2425, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-50, 2375, 150, 2425, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-50, 2375, 0,  2875, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-700, 1475, 350, 1525, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-700, 1475, -650, 1675, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-550, 1625, 0, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-700, 1775, 100, 1825, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-800, 1925, 0, 1975, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-550, 2075, 100, 2125, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-700, 2075, -650, 2375, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-650, 2225, 0, 2275, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(-800, 2375, -150, 2425, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-700, 2525, -50, 2575, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-700, 2525, -650, 2725, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-650, 2675, -200, 2725, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-200, 2675, -150, 2875, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(-700, 2825, -150, 2875, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(100, 2525, 150, 2975, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(100, 2525, 300, 2575, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(250, 1775, 300, 2575, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(250, 1775, 550, 1825, labirinto, "labyrinth_wall", False, window)

        #

        repository.crt_bcgrndC(750, 1525, 800, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(800, 1625, 1150, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1100, 1675, 1150, 2425, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1150, 2375, 1300, 2425, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1250, 2425, 1300, 2875, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(700, 1775, 1000, 1825, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(950, 1825, 1000, 2575, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1000, 2525, 1150, 2575, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1100, 2575, 1150, 2975, labirinto, "labyrinth_wall", False, window)

        repository.crt_bcgrndC(900, 1475, 1950, 1525, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1900, 1525, 1950, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1250, 1625, 1800, 1675, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1150, 1775, 1950, 1825, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1250, 1925, 2050, 1975, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1150, 2075, 1800, 2125, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1900, 2075, 1950, 2375, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1250, 2225, 1900, 2275, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1400, 2375, 2050, 2425, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1300, 2525, 1950, 2575, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1900, 2575, 1950, 2725, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1400, 2675, 1950, 2725, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1400, 2675, 1450, 2875, labirinto, "labyrinth_wall", False, window)
        repository.crt_bcgrndC(1400, 2825, 1950, 2875, labirinto, "labyrinth_wall", False, window)

        # mansão

        repository.crt_bcgrnd(-700, -2275, 1950, -1025, mansion_floor, "mansion_floor", False, window)

        repository.crt_bcgrndC(-700, -2275, -650, -1075, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(-700, -1075, 550, -1025, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(700, -1075, 1950, -1025, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(1900, -2275, 1950, -1025, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(1900, -2275, 1950, -1025, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(-700, -2275, 1900, -2225, mansion_wall, "mansion_wall", False, window)

        repository.crt_bcgrndC(50, -1375, 100, -1075, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(50, -1625, 100, -1525, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(50, -1625, 550, -1575, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(700, -1625, 1900, -1575, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(1150, -1575, 1200, -1525, mansion_wall, "mansion_wall", False, window)
        repository.crt_bcgrndC(1150, -1375, 1200, -1075, mansion_wall, "mansion_wall", False, window)

        # escadas

        repository.crt_bcgrndC(350, -2075, 500, -2025, mansion_wall, "mansion_stairs", False, window)
        repository.crt_bcgrndC(500, -2075, 550, -1825, mansion_wall, "mansion_stairs", False, window)

        repository.crt_bcgrndC(700, -2075, 900, -2025, mansion_wall, "mansion_stairs", False, window)
        repository.crt_bcgrndC(700, -2075, 750, -1825, mansion_wall, "mansion_stairs", False, window)

        repository.crt_bcgrnd(550, -2075, 700, -2025, mansion_bookcase, "mansion_stairs", False, window)

        repository.crt_bcgrnd(550, -2025, 700, -1975, mansion_stair3, "mansion_stairs", False, window)

        repository.crt_bcgrnd(550, -1975, 700, -1925, mansion_bookcase, "mansion_stairs", False, window)

        repository.crt_bcgrnd(550, -1925, 700, -1875, mansion_stair3, "mansion_stairs", False, window)

        repository.crt_bcgrnd(550, -1875, 700, -1825, mansion_bookcase, "mansion_stairs", False, window)

        repository.crt_bcgrnd(550, -2175, 700, -2075, mansion_stair3, "mansion_stairs", False, window)

        repository.crt_bcgrnd(700, -2225, 750, -2075, mansion_stair3, "mansion_stairs", False, window)

        repository.crt_bcgrnd(750, -2225, 800, -2075, mansion_stair7, "mansion_stairs", False, window)

        repository.crt_bcgrnd(800, -2225, 850, -2075, mansion_stair3, "mansion_stairs", False, window)

        repository.crt_bcgrndC(850, -2225, 900, -2075, mansion_stair7, "mansion_stairs", False, window)

        repository.crt_bcgrndC(350, -2225, 400, -2075, mansion_stair7, "mansion_stairs", False, window)

        repository.crt_bcgrnd(400, -2225, 450, -2075, mansion_stair3, "mansion_stairs", False, window)

        repository.crt_bcgrnd(450, -2225, 500, -2075, mansion_stair7, "mansion_stairs", False, window)

        repository.crt_bcgrnd(500, -2225, 550, -2075, mansion_stair3, "mansion_stairs", False, window)

        # mansão tapete

        repository.crt_bcgrnd(150, -1525, 1100, -1125, mansion_light_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(150, -1525, 200, -1475, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(250, -1525, 300, -1375, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(150, -1425, 300, -1375, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(150, -1275, 300, -1225, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(250, -1225, 300, -1125, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(150, -1175, 200, -1125, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(350, -1525, 400, -1375, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(400, -1425, 550, -1375, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(500, -1375, 550, -1225, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(350, -1275, 550, -1225, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(350, -1275, 400, -1125, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(450, -1525, 800, -1475, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(600, -1475, 650, -1375, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(450, -1175, 800, -1125, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(600, -1275, 650, -1175, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(850, -1525, 900, -1375, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(700, -1425, 900, -1375, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(700, -1425, 750, -1225, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(750, -1275, 900, -1225, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(850, -1225, 900, -1125, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(950, -1525, 1000, -1375, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(1000, -1425, 1100, -1375, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(1050, -1525, 1100, -1475, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(950, -1275, 1100, -1225, mansion_dark_red, "mansion_tapete", False, window)
        repository.crt_bcgrnd(950, -1275, 1000, -1125, mansion_dark_red, "mansion_tapete", False, window)

        repository.crt_bcgrnd(1050, -1175, 1100, -1125, mansion_dark_red, "mansion_tapete", False, window)

        # mansão objetos

        repository.crt_bcgrndC(-500, -1675, -100, -1625, mansion_wall, "mansion_table", False, window)
        repository.crt_bcgrndC(-500, -1575, -100, -1525, mansion_wall, "mansion_table", False, window)
        repository.crt_bcgrndC(-500, -1475, -100, -1425, mansion_wall, "mansion_table", False, window)
        repository.crt_bcgrndC(-500, -1375, -100, -1325, mansion_wall, "mansion_table", False, window)
        repository.crt_bcgrndC(-350, -1825, -250, -1175, mansion_wall, "mansion_table", False, window)

        repository.crt_bcgrndC(-450, -1775, -150, -1225, mansion_dark_red, "mansion_table", False, window)

        repository.crt_bcgrndC(-450, -1725, -150, -1275, mansion_bookcase, "mansion_table", False, window)

        repository.crt_bcgrndC(-600, -2225, 50, -2175, mansion_bookcase, "mansion_bookcase", False, window)
        repository.crt_bcgrndC(-650, -2175, -600, -1825, mansion_bookcase, "mansion_bookcase", False, window)

        repository.crt_bcgrndC(1250, -1575, 1400, -1525, mansion_bookcase, "mansion_kitchen", False, window)
        repository.crt_bcgrndC(1350, -1425, 1750, -1275, mansion_bookcase, "mansion_kitchen", False, window)
        repository.crt_bcgrndC(1400, -1125, 1850, -1075, mansion_bookcase, "mansion_kitchen", False, window)

        repository.crt_bcgrndC(1200, -1325, 1250, -1125, mansion_grey1, "mansion_kitchen", False, window)

        repository.crt_bcgrndC(1850, -1525, 1900, -1125, mansion_grey1, "mansion_kitchen", False, window)
        repository.crt_bcgrndC(1800, -1225, 1850, -1175, mansion_grey1, "mansion_kitchen", False, window)

        repository.crt_bcgrndC(1850, -1425, 1900, -1225, mansion_grey2, "mansion_kitchen", False, window)

        repository.crt_bcgrndC(1800, -1475, 1850, -1225, mansion_grey3, "mansion_kitchen", False, window)

        repository.crt_bcgrndC(1500, -2125, 1550, -1925, mansion_piano1, "mansion_piano", False, window)
        repository.crt_bcgrndC(1500, -1925, 1550, -1975, mansion_notes2, "mansion_piano", False, window)

        repository.crt_bcgrndC(1550, -2125, 1650, -1925, mansion_piano2, "mansion_piano", False, window)
        repository.crt_bcgrndC(1650, -2075, 1700, -1925, mansion_piano2, "mansion_piano", False, window)
        repository.crt_bcgrndC(1550, -1925, 1700, -1975, mansion_notes1, "mansion_piano", False, window)

        repository.crt_bcgrndC(1550, -1825, 1650, -1775, mansion_piano1, "mansion_piano", False, window)

def village(b, window):
    if b:
        repository.mansion_map = True
        repository.forest_map = False
        repository.city_map = False
        repository.cave_map = False
        try:
            repository.forest_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_PURGE)
        except:
            pass
        repository.city_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_LOOP)
        # clearing the screen for new map:
        for e in repository.npcs:
            e.remove_obj()
        repository.npcs.clear()
        for e in repository.npcs_head:
            e.remove_obj()
        repository.npcs_head.clear()
        for e in repository.bcgrnd:
            e.remove_obj()
        repository.bcgrnd.clear()
        for e in repository.bcgrndC:
            e.remove_obj()
        repository.bcgrndC.clear()
        for e in repository.bcgrndI:
            e.remove_obj()
        repository.bcgrndI.clear()
        for e in repository.enemies:
            try:
                e.remove_obj()
            except:
                pass
        repository.enemies.clear()

        # background

        repository.crt_bcgrnd(-750, -1025, 2350, 2875, background, "barrier", False, window)

        # tree barriers
        repository.crt_bcgrndC(-550, -2025, 3150, -625, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2150, -2025, 3350, 4275, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(-500, 2875, 3350, 4275, tree_dv, "barrier", False, window)

        repository.crt_bcgrndC(-450, 2825, 2150, 2875, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(-600, -825, -550, -675, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(-400, 2775, -50, 2825, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(100, 2775, 350, 2825, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(-550, 2975, -500, 3175, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(400, 2775,  950, 2825, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1000, 2775, 2150, 2825, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1050, 2725, 1450, 2775, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1100, 2675, 1300, 2725, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1550, 2725, 1700, 2775, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1750, 2725, 2150, 2775, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1900, 2675, 2150, 2725, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2050, 2625, 2150, 2675, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2100, 2475, 2150, 2675, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2000, 2025, 2150, 2275, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2100, 1825, 2150, 2025, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2050, 1925, 2100, 1975, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2050, 1175, 2100, 1225, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2100, 1175, 2150, 1375, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2100, 175, 2150, 225, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1800, -625, 1900, -575, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1900, -625, 1950, -525, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1950, -625, 2000, -475, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2000, -625, 2050, -425, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2050, -625, 2100, -125, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(2100, -625, 2150, 75, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1350, -625, 1700, -575, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(550, -625, 1200, -575, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(700, -575, 1150, -525, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(-50, -625, 500, -575, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(50, -575, 350, -525, tree_dv, "barrier", False, window)
        repository.crt_bcgrndC(1950, 2075, 2000, 2225, tree_dv, "barrier", False, window)

        # water

        repository.crt_bcgrndC(-650, -2025, -600, -75, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-700, -75, -650, -25, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, -25, -700, 225, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-700, 225, -650, 375, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-650, 375, -600, 1425, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-600, 1425, -550, 2075, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-650, 2075, -600, 2525, water_1, "water_barrier", False, window)
        repository.crt_bcgrndC(-600, 2525, -550, 4575, water_1, "water_barrier", False, window)

        repository.crt_bcgrndC(-700, -2025, -650, -75, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, -75, -700, -25, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-800, -25, -750, 225, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, 225, -700, 375, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-700, 375, -650, 1425, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-650, 1425, -600, 2075, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-700, 2075, -650, 2525, water_2, "water_barrier", False, window)
        repository.crt_bcgrndC(-650, 2525, -600, 4575, water_2, "water_barrier", False, window)

        repository.crt_bcgrndC(-750, -2025, -700, -75, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-800, -75, -750, -25, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-850, -25, -800, 225, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-800, 225, -750, 375, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, 375, -700, 1425, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-700, 1425, -650, 2075, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, 2075, -700, 2525, water_3, "water_barrier", False, window)
        repository.crt_bcgrndC(-700, 2525, -650, 4575, water_3, "water_barrier", False, window)

        repository.crt_bcgrndC(-800, -2025, -750, -75, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-850, -75, -800, -25, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-900, -25, -850, 225, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-850, 225, -800, 375, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-800, 375, -750, 1425, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, 1425, -700, 2075, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-800, 2075, -750, 2525, water_4, "water_barrier", False, window)
        repository.crt_bcgrndC(-750, 2525, -700, 4575, water_4, "water_barrier", False, window)

        repository.crt_bcgrndC(-1850, -2025, -800, -75, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1900, -75, -850, -25, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1950, -25, -900, 225, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1900, 225, -850, 375, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1850, 375, -800, 1425, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1800, 1425, -750, 2075, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1850, 2075, -800, 2525, water_5, "water_barrier", False, window)
        repository.crt_bcgrndC(-1800, 2525, -750, 4575, water_5, "water_barrier", False, window)

        # trees

        repository.crt_bcgrndC(1800, 1675, 1950, 1925, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(1750, 1725, 2000, 1875, tree_dv, "tree", False, window)

        repository.crt_bcgrndC(1900, 1375, 2050, 1525, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(2050, 1475, 2100, 1525, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(1950, 1525, 2050, 1575, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(1850, 1375, 1900, 1425, tree_dv, "tree", False, window)

        repository.crt_bcgrndC(1150, 2475, 1200, 2575, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(1050, 2575, 1200, 2625, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(1100, 2525, 1150, 2575, wood_1, "tree", False, window)

        repository.crt_bcgrndC(200, 2025, 350, 2175, tree_dv, "tree", False, window)

        repository.crt_bcgrndC(-650, 25, -500, 175, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-700, 75, -550, 225, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-500, 75, -450, 125, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-650, 225, -600, 275, tree_dv, "tree", False, window)

        repository.crt_bcgrndC(-200, 225, -150, 325, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-250, 275, -200, 425, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-200, 325, -150, 375, wood_1, "tree", False, window)

        repository.crt_bcgrndC(-100, -275, 50, -75, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-150, -225, 100, -125, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-150, -225, 50, -75, tree_dv, "tree", False, window)
        repository.crt_bcgrndC(-100, -75, -50, -25, tree_dv, "tree", False, window)

        repository.crt_bcgrndC(1550, 2575, 1600, 2625, wood_1, "tree", False, window)

        # path

        repository.crt_bcgrnd(-150, 675, 0, 1275, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(-150, 675, -50, 1325, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(-150, 675, -100, 1375, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(-150, 1375, 0, 1775, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(-100, 1775, 0, 1825, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(0, 1625, 50, 1675, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(0, 1675, 200, 1775, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(100, 1625, 150, 1675, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(200, 1625, 700, 1775, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(200, 1775, 300, 1825, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(550, 1375, 700, 1775, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(550, 25, 700, 1325, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(600, 1325, 750, 1375, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(150, 325, 300, 825, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(150, 325, 250, 1075, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(250, 875, 300, 925, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(300, 525, 550, 575, dv_dirt_path, "path", False, window)
        #repository.crt_bcgrnd(500, 675, 550, 725, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(500, 375, 550, 425, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(700, 375, 1800, 525, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(1100, 125, 1200, 525, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(800, 325, 850, 375, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(1800, 375, 1850, 425, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(1850, 425, 1900, 475, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(1300, 525, 1450, 1225, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(700, 925, 950, 1075, dv_dirt_path, "path", False, window)
        repository.crt_bcgrnd(900, 1025, 950, 1175, dv_dirt_path, "path", False, window)

        # houses

        repository.crt_bcgrnd(750, 1175, 1100, 1925, stone_base, "stone_house", False, window)

        repository.crt_bcgrndC(750, 1725, 800, 1875, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(750, 1875, 1100, 1925, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(1050, 1225, 1100, 1925, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(1000, 1175, 1100, 1225, stone_house_wall, "stone_house", False, window)

        repository.crt_bcgrndC(750, 1575, 800, 1625, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(850, 1775, 900, 1825, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(950, 1825, 1000, 1875, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(950, 1525, 1000, 1575, stone_house_wall, "stone_house", False, window)
        repository.crt_bcgrndC(1000, 1775, 1050, 1825, stone_house_wall, "stone_house", False, window)

        repository.crt_bcgrnd(800, 1825, 850, 1875, stone_debris, "stone_house", False, window)
        repository.crt_bcgrnd(850, 1475, 900, 1525, stone_debris, "stone_house", False, window)
        repository.crt_bcgrnd(900, 1275, 950, 1325, stone_debris, "stone_house", False, window)
        repository.crt_bcgrnd(900, 1825, 950, 1875, stone_debris, "stone_house", False, window)
        repository.crt_bcgrnd(950, 1325, 1000, 1375, stone_debris, "stone_house", False, window)

        #

        repository.crt_bcgrndC(400, 1825, 500, 2025, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(400, 1875, 500, 1975, wood_1, "random_house", False, window)

        repository.crt_bcgrndC(150, 1825, 300, 2025, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(300, 1975, 500, 2025, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(150, 1875, 350, 1975, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(-150, 1825, -50, 2025, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(-50, 1975, 50, 2025, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(-150, 1875, -50, 1975, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(-50, 1925, 50, 1975, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(50, 1425, 100, 1625, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(50, 1475, 100, 1575, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(-350, 1425, -300, 1775, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(-200, 1675, -150, 1775, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(-300, 1475, -250, 1775, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(-250, 1675, -200, 1775, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(-350, 825, -300, 1175, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(-300, 825, -200, 875, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(-300, 825, -250, 925, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(-300, 1075, -250, 1175, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(0, 175, 50, 625, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(50, 175, 100, 275, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(350, 225, 400, 475, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(450, 325, 500, 475, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(400, 275, 450, 475, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(800, 125, 1000, 175, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(750, 275, 850, 325, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(800, 175, 1000, 275, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(950, 325, 1000, 375, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrnd(400, -225, 450, -125, stone_base, "stone_house", False, window)
        repository.crt_bcgrnd(450, -275, 500, -125, stone_base, "stone_house", False, window)
        repository.crt_bcgrnd(500, -275, 550, -75, stone_base, "stone_house", False, window)
        repository.crt_bcgrnd(550, -275, 600, -25, stone_base, "stone_house", False, window)
        repository.crt_bcgrnd(600, -375, 950, 25, stone_base, "stone_house", False, window)

        repository.crt_bcgrndC(450, -375, 850, -325, wood_3, "stone_house", False, window)
        repository.crt_bcgrndC(400, -325, 800, -275, wood_2, "stone_house", False, window)

        repository.crt_bcgrndC(500, -425, 950, -375, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(900, -375, 950, -25, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(350, -325, 400, -175, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(400, -275, 450, -225, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(450, -125, 500, -75, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(650, -225, 700, -175, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(700, -275, 750, -225, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(700, -175, 750, -125, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(950, 25, 1000, 75, wood_1, "stone_house", False, window)
        repository.crt_bcgrndC(1000, -225, 1050, -175, wood_1, "stone_house", False, window)

        #

        repository.crt_bcgrndC(1300, 1225, 1550, 1425, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(1200, 1375, 1300, 1425, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(1300, 1275, 1550, 1375, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(1250, 1325, 1300, 1375, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(1950, 225, 2150, 525, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(2100, 525, 2150, 675, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(2000, 225, 2100, 575, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(2050, 575, 2100, 625, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(1950, 975, 2150, 1175, wood_2, "random_house", False, window)
        repository.crt_bcgrndC(2100, 825, 2150, 1175, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(2000, 925, 2100, 1175, wood_1, "random_house", False, window)
        repository.crt_bcgrndC(2150, 875, 2100, 1175, wood_1, "random_house", False, window)

        #

        repository.crt_bcgrndC(0, 2575, 350, 2775, wood_2, "random_house", False, window)

        repository.crt_bcgrndC(0, 2625, 350, 2725, wood_1, "random_house", False, window)

        # wheat

        repository.crt_bcgrnd(400, 2375, 1000, 2775, wheat_1, "wheat", False, window)

        repository.crt_bcgrnd(-350, 2325, -50, 2775, wheat_1, "wheat", False, window)

        # pentagram

        repository.crt_bcgrnd(250, 875, 550, 1125, pentagram, "pentagram", False, window)

        repository.crt_bcgrnd(250, 825, 300, 925, dv_dirt_path, "path", False, window)

        repository.crt_bcgrnd(400, 825, 450, 875, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(300, 1175, 350, 1275, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(350, 1225, 400, 1375, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(500, 1175, 550, 1275, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(450, 1225, 500, 1375, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(400, 1375, 450, 1425, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(250, 1425, 600, 1475, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(550, 1375, 700, 1425, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(700, 1325, 750, 1375, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(750, 1275, 800, 1325, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(800, 1125, 850, 1275, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(550, 925, 600, 1175, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(0, 1125, 800, 1175, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(750, 1075, 800, 1175, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(850, 975, 900, 1125, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(800, 825, 850, 975, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(750, 725, 800, 825, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(700, 675, 750, 775, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(600, 625, 650, 725, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(600, 675, 700, 725, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(550, 625, 650, 675, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(300, 575, 550, 625, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(200, 625, 300, 675, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(100, 675, 250, 725, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(50, 725, 150, 775, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(50, 725, 100, 825, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(0, 825, 50, 975, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(-50, 975, 0, 1125, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(0, 1125, 50, 1275, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(50, 1275, 100, 1325, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(100, 1325, 150, 1375, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(150, 1375, 300, 1425, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(200, 875, 250, 1025, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(150, 975, 250, 1025, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(100, 1025, 150, 1075, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(50, 1075, 100, 1125, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(150, 775, 200, 875, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(250, 725, 300, 775, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(300, 775, 400, 825, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(450, 775, 550, 825, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(550, 725, 600, 775, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(700, 1025, 750, 1075, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(600, 975, 700, 1025, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(600, 875, 650, 1025, pentagram, "pentagram", False, window)
        repository.crt_bcgrnd(650, 775, 700, 875, pentagram, "pentagram", False, window)

        # lava

        repository.crt_bcgrndC(400, 875, 450, 925, lava_1, "lava_pentagram", False, window)
        repository.crt_bcgrndC(300, 925, 550, 1125, lava_1, "lava_pentagram", False, window)

        repository.crt_bcgrndC(350, 925, 500, 1125, lava_2, "lava_pentagram", False, window)
        repository.crt_bcgrndC(300, 1025, 550, 1075, lava_2, "lava_pentagram", False, window)

        repository.crt_bcgrndC(350, 925, 400, 1075, lava_3, "lava_pentagram", False, window)
        repository.crt_bcgrndC(350, 1025, 450, 1075, lava_3, "lava_pentagram", False, window)
        repository.crt_bcgrndC(300, 975, 550, 1025, lava_3, "lava_pentagram", False, window)
        repository.crt_bcgrndC(450, 1075, 500, 1125, lava_3, "lava_pentagram", False, window)

        repository.crt_bcgrndC(450, 975, 500, 1075, lava_4, "lava_pentagram", False, window)

        repository.crt_bcgrndC(400, 975, 450, 1025, lava_5, "lava_pentagram", False, window)
        repository.crt_bcgrndC(400, 1075, 450, 1125, lava_5, "lava_pentagram", False, window)

        repository.crt_bcgrndC(350, 975, 400, 1025, lava_6, "lava_pentagram", False, window)

        #

        repository.crt_bcgrndC(0, 725, 50, 825, lava_1, "lava", False, window)
        repository.crt_bcgrndC(50, 575, 100, 725, lava_1, "lava", False, window)
        repository.crt_bcgrndC(100, 625, 200, 675, lava_1, "lava", False, window)
        repository.crt_bcgrndC(100, 525, 150, 575, lava_1, "lava", False, window)
        repository.crt_bcgrndC(50, 375, 100, 525, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-100, 25, -50, 125, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-50, 125, 0, 175, lava_1, "lava", False, window)
        repository.crt_bcgrndC(350, -175, 400, -125, lava_1, "lava", False, window)
        repository.crt_bcgrndC(400, -125, 450, -75, lava_1, "lava", False, window)
        repository.crt_bcgrndC(500, -25, 550, 25, lava_1, "lava", False, window)
        repository.crt_bcgrndC(450, 25, 500, 125, lava_1, "lava", False, window)
        repository.crt_bcgrndC(400, 125, 450, 175, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-200, 475, -150, 525, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-450, 725, -400, 775, lava_1, "lava", False, window)
        repository.crt_bcgrndC(0, 1325, 100, 1375, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-50, 1375, 0, 1475, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-200, 1575, -150, 1625, lava_1, "lava", False, window)
        repository.crt_bcgrndC(-400, 1725, -350, 1775, lava_1, "lava", False, window)
        repository.crt_bcgrndC(50, 1925, 100, 1975, lava_1, "lava", False, window)
        repository.crt_bcgrndC(300, 1875, 350, 1925, lava_1, "lava", False, window)
        repository.crt_bcgrndC(400, 1825, 450, 1875, lava_1, "lava", False, window)
        repository.crt_bcgrndC(700, 1375, 800, 1425, lava_1, "lava", False, window)
        repository.crt_bcgrndC(800, 1425, 850, 1475, lava_1, "lava", False, window)
        repository.crt_bcgrndC(750, 1475, 800, 1525, lava_1, "lava", False, window)
        repository.crt_bcgrndC(900, 1025, 950, 1075 , lava_1, "lava", False, window)
        repository.crt_bcgrndC(950, 1075, 1000, 1125, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1000, 1125, 1050, 1275, lava_1, "lava", False, window)
        repository.crt_bcgrndC(750, 675, 850, 725, lava_1, "lava", False, window)
        repository.crt_bcgrndC(800, 675, 850, 825, lava_1, "lava", False, window)
        repository.crt_bcgrndC(850, 625, 900, 675, lava_1, "lava", False, window)
        repository.crt_bcgrndC(900, 575, 950, 625, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1000, 525, 1050, 575, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1050, 475, 1100, 525, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1100, 425, 1150, 475, lava_1, "lava", False, window)
        repository.crt_bcgrndC(850, 275, 900, 325, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1600, 225, 1650, 275, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1600, 425, 1650, 475, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1950, 625, 2000, 675, lava_1, "lava", False, window)
        repository.crt_bcgrndC(2100, 675, 2150, 725, lava_1, "lava", False, window)
        repository.crt_bcgrndC(2100, 775, 2150, 825, lava_1, "lava", False, window)
        repository.crt_bcgrndC(2050, 725, 2100, 775, lava_1, "lava", False, window)
        repository.crt_bcgrndC(2000, 775, 2050, 875, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1950, 875, 2000, 925, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1700, 925, 1750, 975, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1150, 1375, 1200, 1475, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1950, 1175, 2000, 1225, lava_1, "lava", False, window)
        repository.crt_bcgrndC(2000, 1225, 2050, 1275, lava_1, "lava", False, window)
        repository.crt_bcgrndC(2050, 1425, 2100, 1475, lava_1, "lava", False, window)
        repository.crt_bcgrndC(1700, 2025, 1750, 2075, lava_1, "lava", False, window)

        #

        repository.crt_bcgrndC(800, 675, 850, 725, lava_3, "lava", False, window)
        repository.crt_bcgrndC(950, 525, 1000, 575, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1050, 575, 1100, 625, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1150, 375, 1200, 425, lava_3, "lava", False, window)
        repository.crt_bcgrndC(950, 1025, 1000, 1075, lava_3, "lava", False, window)
        repository.crt_bcgrndC(750, 1325, 800, 1375, lava_3, "lava", False, window)
        repository.crt_bcgrndC(800, 1375, 850, 1425, lava_3, "lava", False, window)
        repository.crt_bcgrndC(800, 1525, 850, 1575, lava_3, "lava", False, window)
        repository.crt_bcgrndC(900, 225, 950, 275, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1650, 375, 1700, 425, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1950, 525, 2000, 575, lava_3, "lava", False, window)
        repository.crt_bcgrndC(2000, 725, 2050, 775, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1950, 825, 2000, 875, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1600, 975, 1650, 1025, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1650, 1025, 1700, 1075, lava_3, "lava", False, window)
        repository.crt_bcgrndC(2050, 1375, 2100, 1425, lava_3, "lava", False, window)
        repository.crt_bcgrndC(2100, 1475, 2150, 1525, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1200, 1325, 1250, 1375, lava_3, "lava", False, window)
        repository.crt_bcgrndC(1200, 1325, 1250, 1375, lava_3, "lava", False, window)
        repository.crt_bcgrndC(650, 1775, 700, 1825, lava_3, "lava", False, window)
        repository.crt_bcgrndC(250, 1825, 300, 1875, lava_3, "lava", False, window)
        repository.crt_bcgrndC(-100, 1825, -50, 1875, lava_3, "lava", False, window)
        repository.crt_bcgrndC(-100, 1475, -50, 1525, lava_3, "lava", False, window)
        repository.crt_bcgrndC(-300, 1425, -250, 1475, lava_3, "lava", False, window)
        repository.crt_bcgrndC(0, 1275, 50, 1325, lava_3, "lava", False, window)
        repository.crt_bcgrndC(50, 625, 100, 675, lava_3, "lava", False, window)
        repository.crt_bcgrndC(50, 425, 100, 475, lava_3, "lava", False, window)
        repository.crt_bcgrndC(100, 325, 150, 375, lava_3, "lava", False, window)
        repository.crt_bcgrndC(-150, 75, -100, 125, lava_3, "lava", False, window)
        repository.crt_bcgrndC(450, -25, 500, 25, lava_3, "lava", False, window)
        repository.crt_bcgrndC(400, 75, 450, 125, lava_3, "lava", False, window)

def hell(b, window):
    if b:
        repository.mansion_map = True
        repository.forest_map = False
        repository.city_map = False
        repository.cave_map = False
        try:
            repository.forest_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_PURGE)
        except:
            pass
        repository.city_soundtrack(repository.winsound.SND_ASYNC, repository.winsound.SND_LOOP)
        # clearing the screen for new map:
        for e in repository.npcs:
            e.remove_obj()
        repository.npcs.clear()
        for e in repository.npcs_head:
            e.remove_obj()
        repository.npcs_head.clear()
        for e in repository.bcgrnd:
            e.remove_obj()
        repository.bcgrnd.clear()
        for e in repository.bcgrndC:
            e.remove_obj()
        repository.bcgrndC.clear()
        for e in repository.bcgrndI:
            e.remove_obj()
        repository.bcgrndI.clear()
        for e in repository.enemies:
            try:
                e.remove_obj()
            except:
                pass
        repository.enemies.clear()

        # background

        repository.crt_bcgrnd(-2500, -3500, 4000, 4975, background_hell, "background", False, window)

        # map_limit

        repository.crt_bcgrndC(-2500, -1175, -1450, 4975, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-2500, 3925, 3900, 4975, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2950, -2575, 3900, 4975, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1150, -3500, 3900, -2575, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1150, -2625, 3050, -2575, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2950, -2475, 3000, -2575, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-2500, -3550, -1100, -2625, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-2500, -4500, -1450, -2175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-2500, -2175, -1500, -1825, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-2500, -1825, -1450, -1575, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-2500, -1575, -1500, -1175, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1200, -2575, -700, -2525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-300, -2575, 800, -2525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(900, -2575, 950, -2525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1000, -2575, 3000, -2525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2200, -2575, 2950, -2525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, -2525, 2950, -1975, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, -1625, 2950, -125, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, 25, 2950, 525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, 725, 2950, 1225, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, 1425, 2950, 2225, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, 2425, 2950, 2675, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, 2775, 2950, 3025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2900, 3225, 2950, 4500, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, -2375, 2900, -2125, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, -1525, 2900, -1275, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2750, -1325, 2900, -1275, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2850, -1075, 2900, -775, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2750, -1025, 2850, -925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2650, -975, 2850, -925, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2800, -575, 2900, -525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, -525, 2900, -475, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2850, 125, 2900, 375, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, 775, 2900, 1025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, 1125, 2900, 1175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, 1725, 2900, 2175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, 2525, 2900, 2625, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2700, 2825, 2850, 2875, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, 2825, 2900, 2925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2850, 3525, 2900, 4500, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2800, 1925, 2850, 2025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2750, 1975, 2800 ,2025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2700, 3625, 2750, 3675, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2650, 3675, 2850, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2650, 3775, 2700, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2600, 3825, 2650, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2500, 3875, 2600, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1550, 3975, 2350, 3925, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(1550, 3875, 2350, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1650, 3775, 1700, 3875, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1700, 3825, 1750, 3875, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1950, 3825, 2200, 3875, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2100, 3725, 2150, 3825, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(750, 3875, 1300, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(900, 3825, 950, 3875, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(500, 3875, 550, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-600, 3875, -200, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1000, 3825, -600, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1400, 3775, -1000, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1450, 2375, -1400, 3925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1400, 2975, -1350, 3375, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1350, 3025, -1300, 3175, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1400, 2425, -1250, 2475, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1400, 2425, -1350, 2675, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1400, 2425, -1300, 2525, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1450, 675, -1400, 2125, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1400, 875, -1350, 1475, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1350, 1125, -1250, 1375, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1250, 1175, -1150, 1325, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1150, 1225, -1100, 1325, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1100, 1275, -900, 1325, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1400, 1675, -1350, 1825, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1350, 1675, -1300, 1775, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1300, 1725, -1250, 1775, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1450, -1175, -1400, 425, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1400, -1025, -1350, 325, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1350, -325, -1300, 75, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1300, -275, -1250, 25, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1250, -175, -1200, 25, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1200, -175, -1150, -25, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1150, -125, -1000, -25, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-1000, -75, -900, -25, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-150, -2525, 150, -2475, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(0, -2475, 50, -2425, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(50, -2475, 100, -2275, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(350, -2525, 600, -2475, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(450, -2475, 500, -2275, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(450, -2475, 550, -2375, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(650, -2525, 700, -2425, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(700, -2525, 750, -2325, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(1100, -2525, 1200, -2475, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1400, -2525, 1900, -2475, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1600, -2475, 1650, -2375, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1600, -2475, 1700, -2425, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2250, -2525, 2950, -2475, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2500, -2475, 2950, -2425, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2600, 3725, 2650, 3775, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2400, 2625, 2450, 2675, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2400, 2725, 2450, 3175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2350, 2975, 2400, 3275, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2450, 2775, 2500, 3075, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2300, 3125, 2350, 3375, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2250, 3225, 2300, 3525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2150, 3375, 2300, 3525, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2200, 3275, 2250, 3575, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2650, 3375, 2700, 3425, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2600, 3375, 2650, 3425, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-950, 2425, -900, 2525, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-750, 1025, -650, 1075, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-650, 975, -500, 1125, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-600, 925, -400, 1075, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-550, 875, -300, 1025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-450, 825, -200, 975, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-400, 775, -350, 825, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-250, 775, -50, 925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-50, 775, 50, 875, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(0, 725, 300, 825, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(150, 675, 350, 775, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(350, 725, 550, 775, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-200, 625, -150, 675, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(0, 525, 50, 575, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-800, 225, -750, 175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-750, 175, -700, 125, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-650, 25, -600, 75, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-150, -425, -100, -375, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-100, -375, -50, -325, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(500, -275, 550, -225, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(800, -475, 850, -425, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-1050, -775, -1000, -725, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-900, -1275, -850, -1225, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-850, -1325, -800, -1275, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-800, -1275, -750, -1225, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-500, -1725, -450, -1675, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(100, -1875, 150, -1825, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(300, -1625, 350, -1575, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-850, -2075, -800, -2025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-650, -2175, -600, -2125, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(-150, -1875, -100, -1825, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-200, -1825, -50, -1625, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-250, -1625, -100, -1425, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-200, -1425, -50, -1325, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-150, -1375, 0, -1275, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(-100, -1325, 150, -1225, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(0, -1275, 200, -1175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(100, -1225, 300, -925, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(200, -925, 250, -875, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2350, -2275, 2300, -2225, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2500, -775, 2550, -625, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2450, -725, 2500, -575, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2500, -225, 2550, -175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2550, -175, 2600, -125, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2400, 125, 2450, 175, hell_rocks, "map_limit", False, window)

        repository.crt_bcgrndC(2350, 725, 2400, 975, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2300, 675, 2350, 1025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2250, 725, 2300, 1075, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2200, 875, 2300, 1075, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2150, 825, 2200, 1025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2100, 825, 2150, 1175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2050, 875, 2100, 1075, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(2000, 825, 2050, 1125, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1950, 775, 2000, 1025, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1900, 825, 1950, 1125, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1850, 975, 1900, 1175, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1800, 1075, 1850, 1225, hell_rocks, "map_limit", False, window)
        repository.crt_bcgrndC(1750, 1125, 1800, 1275, hell_rocks, "map_limit", False, window)

        # lava pools floor

        repository.crt_bcgrnd(-1400, 3525, -1200, 3675, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1400, 3525, -1300, 3725, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1200, 3475, -1000, 3625, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1000, 3525, -900, 3675, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-900, 3475, -800, 3625, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-800, 3525, -750, 3575, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(-1100, 3625, -1050, 3775, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1150, 3625, -1000, 3725, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(-750, 3425, -600, 3475, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-700, 3375, -650, 3525, ground_hell_1, "lava_pool", False, window)

        #

        repository.crt_bcgrnd(-150, -125, 100, 25, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-200, -75, 150, -25, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(50, -25, 200, 125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(100, 25, 350, 125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(100, 125, 500, 175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(150, 175, 450, 225, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(400, 25, 550, 125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(400, 25, 600, 75, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(500, -25, 550, 125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(300, 125, 450, 275, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(350, 75, 500, 175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(250, -25, 300, 25, ground_hell_1, "lava_pool", False, window)

        #

        repository.crt_bcgrnd(-350, -1075, -300, -1025, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-300, -1125, -150, -975, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-200, -1075, -50, -925, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-50, -1125, 150, -975, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(50, -975, 150, -925, ground_hell_1, "lava_pool", False, window)


        #lake------

        repository.crt_bcgrnd(-1200, -2525, -1150, -1925, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1250, -1925, -1200, -1575, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1300, -1575, -1250, -1375, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1350, -1375, -1300, -1275, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-1400, -1275, -1350, -1175, ground_hell_1, "lava_pool", False, window)

        #

        repository.crt_bcgrnd(1900, -1225, 2000, -1075, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2000, -1275, 2100, -1125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2100, -1325, 2200, -1175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2000, -1275, 2250, -1175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2150, -1175, 2200, -1125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1850, -1175, 1900, -1125, ground_hell_1, "lava_pool", False, window)

        #

        repository.crt_bcgrnd(2400, 2075, 2450, 2125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2450, 2025, 2600, 2175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2550, 2075, 2700, 2225, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2700, 1975, 2850, 2175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2750, 2175, 2850, 2225, ground_hell_1, "lava_pool", False, window)

        #pool----

        repository.crt_bcgrnd(-350, 1225, 1550, 3525, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(-450, 1275, -350, 3425, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-400, 3425, -350, 3525, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-500, 1475, -450, 3175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-550, 1725, -500, 2825, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-600, 1825, -550, 2575, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-750, 2025, -600, 2175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-800, 2075, -750, 2125, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(-300, 3525, 1500, 3575, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-250, 3575, 0, 3625, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(150, 3575, 1350, 3625, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(500, 3625, 1300, 3675, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(1550, 1325, 1650, 3475, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1650, 1625, 1700, 3425, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1550, 1275, 1600, 1325, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1700, 1825, 1750, 2625, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1700, 2975, 1750, 3275, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(1750, 1975, 1800, 2125, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1800, 2025, 1900, 2175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1900, 2075, 2000, 2225, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2000, 2125, 2050, 2175, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(1750, 2325, 1850, 2575, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1850, 2325, 1950, 2625, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1900, 2275, 2050, 2425, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(2050, 2325, 2100, 2375, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(1950, 2525, 2000, 2575, ground_hell_1, "lava_pool", False, window)

        repository.crt_bcgrnd(-200, 1175, 1500, 1225, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(-50, 1125, 1300, 1175, ground_hell_1, "lava_pool", False, window)
        repository.crt_bcgrnd(100, 1075, 950, 1225, ground_hell_1, "lava_pool", False, window)

        # pool----

        repository.crt_bcgrnd(0, 1775, 1300, 3125, ground_hell_2, "lava_pool", False, window)

        repository.crt_bcgrnd(1300, 2575, 1400, 2925, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(1300, 2925, 1350, 3025, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(1300, 1825, 1350, 2375, ground_hell_2, "lava_pool", False, window)

        repository.crt_bcgrnd(1000, 1625, 1250, 1775, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(650, 1575, 1000, 1775, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(-150, 1475, 650, 1775, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(250, 1425, 400, 1475, ground_hell_2, "lava_pool", False, window)

        repository.crt_bcgrnd(-150, 1775, 0,  2625, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(-100, 2625, 0, 2825, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(-150, 2825, -50, 2875, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(-50, 2875, 0, 3025, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(-200, 1575, -150, 1925, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(-250, 1725, -150, 1925, ground_hell_2, "lava_pool", False, window)

        repository.crt_bcgrnd(200, 3125, 350, 3175, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(350, 3125, 1150, 3225, ground_hell_2, "lava_pool", False, window)
        repository.crt_bcgrnd(600, 3225, 850, 3275, ground_hell_2, "lava_pool", False, window)

        # dungeon floor

        repository.crt_bcgrnd(650, -2075, 2500, -1475, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1450, -1475, 1700, -1425, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1500, -1475, 1650, -775, ground_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrnd(1400, -925, 1750, 225, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1350, -875, 1800, 375, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1300, -825, 1850, 325, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1250, -775, 1900, 275, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1200, -725, 1950, 225, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1150, -675, 2000, 175, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1100, -625, 2050, 125, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1050, -575, 2100, 75, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(1000, -525, 2150, 25, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(950, -475, 2200, -25, ground_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrnd(900, -425, 2250, -75, ground_hell_dungeon, "dungeon", False, window)

        # dungeon wall

        repository.crt_bcgrndC(650, -2075, 1000, -2025, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(950, -2025, 1000, -1825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(850, -1875, 1000, -1825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(800, -1925, 850, -1875, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(600, -1875, 800, -1825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(600, -2025, 650, -1825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(700, -1975, 800, -1925, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(600, -1725, 800, -1675, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(600, -1725, 650, -1525, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(650, -1525, 1150, -1475, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1100, -1925, 1150, -1475, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(800, -1675, 850, -1625, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(700, -1625, 800, -1575, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1000, -2125, 2500, -2075, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2500, -2075, 2550, -1525, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1750, -1525, 2500, -1475, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1150, -1475, 1450, -1425, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1400, -1625, 1450, -1425, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1150, -1975, 1550, -1925, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1250, -1775, 1300, -1575, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1300, -1825, 1650, -1775, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1650, -2075, 1700, -1825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1650, -2075, 1700, -1825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1450, -1675, 2400, -1625, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1800, -1925, 1850, -1625, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1850, -1975, 2400, -1925, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1950, -1825, 2500, -1775, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1700, -1475, 1750, -1425, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1450, -1425, 1500, -925, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1650, -1425, 1700, -925, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1500, -775, 1650, -725, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1400, -725, 1750, -425, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1350, -675, 1800, -625, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1300, -625, 1850, -575, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1250, -575, 1900, -525, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1200, -525, 1950, -475, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1150, -475, 2000, -425, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1100, -425, 1400, -75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1050, -325, 1100, -175, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1150, -75, 1200, -25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1200, -25, 1250, 25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1250, 25, 1300, 75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1300, 75, 1350, 125, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1350, 125, 1400, 175, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1400, 175, 1450, 225, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1450, -75, 1500, 175, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1650, -75, 1700, 175, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1700, 175, 1750, 225, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1750, 125, 1800, 175, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1800, 75, 1850, 125, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1850, 25, 1900, 75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1900, -25, 1950, 25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1950, -75, 2000, -25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2000, -425, 2050, -75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2050, -325, 2050, -75, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1400, -125, 1450, -75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1400, -425, 1450, -375, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1700, -425, 1750, -375, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1700, -125, 1750, -75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1750, -375, 1800, -125, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1400, -925, 1450, -875, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1350, -875, 1400, -825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1300, -825, 1350, -775, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1250, -775, 1300, -725, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1200, -725, 1250, -675, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1150, -675, 1200, -625, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1100, -625, 1150, -575, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1050, -575, 1100, -525, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1000, -525, 1050, -475, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(950, -475, 1000, -425, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(900, -425, 950, -75, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(950, -75, 1000, -25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1000, -25, 1050, 25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1050, 25, 1100, 75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1100, 75, 1150, 125, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1150, 125, 1200, 175, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1200, 175, 1250, 225, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1250, 225, 1300, 275, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1300, 275, 1350, 325, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1350, 325, 1800, 375, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(1800, 275, 1850, 325, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1850, 225, 1900, 275, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1900, 175, 1950, 225, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1950, 125, 2000, 175, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2000, 75, 2050, 125, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2050, 25, 2100, 75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2100, -25, 2150, 25, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2150, -75, 2200, -25, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(2200, -425, 2250, -75, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2050, -325, 2100, -175, walls_hell_dungeon, "dungeon", False, window)

        repository.crt_bcgrndC(2150, -475, 2200, -425, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2100, -525, 2150, -475, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2050, -575, 2100, -525, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(2000, -625, 2050, -575, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1950, -675, 2000, -625, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1900, -725, 1950, -675, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1850, -775, 1900, -725, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1800, -825, 1850, -775, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1750, -875, 1800, -825, walls_hell_dungeon, "dungeon", False, window)
        repository.crt_bcgrndC(1700, -925, 1750, -875, walls_hell_dungeon, "dungeon", False, window)

        # lava---------------------------------------------------

        repository.crt_bcgrndC(1500, -725, 1650, -675, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, -675, 1750, -625, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -625, 1800, -575, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1300, -575, 1850, -525, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1250, -525, 1900, -475, lava_1, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1200, -475, 1250, -425, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1150, -425, 1200, -325, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1100, -325, 1150, -175, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1150, -175, 1200, -75, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1200, -75, 1250, -25, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1250, -25, 1300, 25, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1300, 25, 1350, 75, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, 75, 1400, 125, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, 125, 1450, 175, lava_1, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1900, -475, 1950, -425, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1950, -425, 2000, -325, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(2000, -325, 2050, -175, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1950, -175, 2000, -75, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1900, -75, 1950, -25, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1850, -25, 1900, 25, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1800, 25, 1850, 75, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1750, 75, 1800, 125, lava_1, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1700, 125, 1750, 175, lava_1, "lava_dungeon", False, window)

        #

        repository.crt_bcgrndC(1500, -675, 1650, -625, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, -625, 1750, -575, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -575, 1800, -525, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1300, -525, 1850, -475, lava_3, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1300, -525, 1350, 25, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1250, -475, 1300, -25, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1200, -425, 1250, -75, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1150, -325, 1200, -175, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, 25, 1400, 75, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, 75, 1450, 125, lava_3, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1800, -525, 1850, 25, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1850, -475, 1900, -25, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1900, -425, 1950, -75, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1950, -325, 2000, -175, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1750, 25, 1800, 75, lava_3, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1700, 75, 1750, 125, lava_3, "lava_dungeon", False, window)

        #

        repository.crt_bcgrndC(1500, -625, 1650, -575, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, -575, 1750, -525, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -525, 1800, -475, lava_4, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1300, -475, 1350, -25, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1250, -425, 1300, -75, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1200, -325, 1250, -175, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -25, 1400, 25, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, 25, 1450, 75, lava_4, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1800, -475, 1850, -25, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1850, -425, 1900, -75, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1900, -325, 1950, -175, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1750, -25, 1800, 25, lava_4, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1700, 25, 1750, 75, lava_4, "lava_dungeon", False, window)

        #

        repository.crt_bcgrndC(1500, -575, 1650, -525, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, -525, 1750, -475, lava_5, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1350, -475, 1400, -425, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1300, -425, 1350, -75, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1250, -325, 1300, -175, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -75, 1400, -25, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, -25, 1450, 25, lava_5, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1750, -475, 1800, -425, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1800, -425, 1850, -75, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1850, -325, 1900, -175, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1750, -75, 1800, -25, lava_5, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1700, -25, 1750, 25, lava_5, "lava_dungeon", False, window)

        #

        repository.crt_bcgrndC(1500, -525, 1650, -475, lava_6, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1400, -475, 1450, -425, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -425, 1400, -375, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1300, -325, 1350, -175, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1350, -125, 1400, -75, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1400, -75, 1450, -25, lava_6, "lava_dungeon", False, window)

        repository.crt_bcgrndC(1700, -475, 1750, -425, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1750, -425, 1800, -375, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1800, -325, 1850, -175, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1750, -125, 1800, -75, lava_6, "lava_dungeon", False, window)
        repository.crt_bcgrndC(1700, -75, 1750, -25, lava_6, "lava_dungeon", False, window)

        # lava lake---------------------------------------------------

        repository.crt_bcgrndC(-1450, -2625, -1150, -2575, lava_1, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2625, -1200, -1925, lava_1, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2625, -1250, -1575, lava_1, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2625, -1300, -1375, lava_1, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2625, -1350, -1275, lava_1, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2625, -1400, -1175, lava_1, "lava_lake", False, window)

        repository.crt_bcgrndC(-1500, -2175, -1450, -1825, lava_1, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -1575, -1450, -1175, lava_1, "lava_lake", False, window)

        repository.crt_bcgrndC(-1300, -2425, -1250, -2225, lava_1, "lava_lake", False, window)

        #

        repository.crt_bcgrndC(-1250, -2625, -1200, -2525, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1300, -2525, -1250, -2425, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1350, -2425, -1300, -2225, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1300, -2225, -1250, -1925, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1350, -1925, -1300, -1575, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1400, -1575, -1350, -1375, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -1325, -1400, -1275, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -1375, -1400, -1325, lava_2, "lava_lake", False, window)

        repository.crt_bcgrndC(-1500, -1275, -1450, -1175, lava_2, "lava_lake", False, window)
        repository.crt_bcgrndC(-1350, -2575, -1250, -2525, lava_2, "lava_lake", False, window)

        #

        repository.crt_bcgrndC(-1300, -2625, -1250, -2575, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1400, -2575, -1350, -2525, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1350, -2525, -1300, -2425, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1400, -2425, -1350, -2225, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1350, -2225, -1300, -1925, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1400, -1925, -1350, -1575, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -1575, -1400, -1375, lava_3, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -1375, -1450, -1275, lava_3, "lava_lake", False, window)

        #

        repository.crt_bcgrndC(-1400, -2625, -1300, -2575, lava_4, "lava_lake", False, window)
        repository.crt_bcgrndC(-1400, -2525, -1350, -2425, lava_4, "lava_lake", False, window)
        repository.crt_bcgrndC(-1400, -2225, -1350, -1925, lava_4, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -1925, -1400, -1575, lava_4, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -1575, -1450,  -1375, lava_4, "lava_lake", False, window)

        #

        repository.crt_bcgrndC(-1450, -2625, -1400, -2425, lava_5, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2425, -1400, -2375, lava_5, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -2375, -1450, -2325, lava_5, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2325, -1400, -2275, lava_5, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -2275, -1450, -2225, lava_5, "lava_lake", False, window)
        repository.crt_bcgrndC(-1450, -2225, -1400, -1925, lava_5, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -1925, -1450, -1825, lava_5, "lava_lake", False, window)

        #

        repository.crt_bcgrndC(-1500, -2625, -1450, -2575, lava_6, "lava_lake", False, window)
        repository.crt_bcgrndC(-1500, -2225, -1450, -1975, lava_6, "lava_lake", False, window)

        # lava pools

        repository.crt_bcgrndC(100, -1125, 150, -1025, lava_1, "lava_pool", False, window)
        repository.crt_bcgrndC(50, -1075, 100, -975, lava_1, "lava_pool", False, window)
        repository.crt_bcgrndC(-50, -1075, 50, -1025, lava_1, "lava_pool", False, window)
        repository.crt_bcgrndC(-100, -1025, -50, -975, lava_1, "lava_pool", False, window)

        repository.crt_bcgrndC(-150, -1025, -100, -975, lava_3, "lava_pool", False, window)
        repository.crt_bcgrndC(-200, -1075, -150, -1025, lava_3, "lava_pool", False, window)

        repository.crt_bcgrndC(-200, -1025, -150, -975, lava_4, "lava_pool", False, window)
        repository.crt_bcgrndC(-250, -1075, -200, -1025, lava_4, "lava_pool", False, window)

        repository.crt_bcgrndC(-300, -1075, -250, -1025, lava_5, "lava_pool", False, window)

        #

        repository.crt_bcgrndC(2150, -1275, 2200, -1175, lava_1, "lava_pool", False, window)

        repository.crt_bcgrndC(2100, -1275, 2150, -1225, lava_3, "lava_pool", False, window)

        repository.crt_bcgrndC(2050, -1225, 2100, -1175, lava_4, "lava_pool", False, window)
        repository.crt_bcgrndC(1950, -1175, 2000, -1125, lava_4, "lava_pool", False, window)

        repository.crt_bcgrndC(2000, -1225, 2050, -1175, lava_5, "lava_pool", False, window)
        repository.crt_bcgrndC(1900, -1175, 1950, -1125, lava_5, "lava_pool", False, window)

        #

        repository.crt_bcgrndC(-150, -75, 100, -25, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(100, -25, 150, 125, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(200, 125, 400, 175, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(400, 75, 450, 125, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(500, 25, 550, 75, lava_2, "lava_pool", False, window)

        repository.crt_bcgrndC(-100, -75, -50, -25, lava_1, "lava_pool", False, window)
        repository.crt_bcgrndC(100, 25, 150, 75, lava_1, "lava_pool", False, window)

        repository.crt_bcgrndC(-50, -75, 0, -25, lava_3, "lava_pool", False, window)
        repository.crt_bcgrndC(250, 75, 300, 175, lava_3, "lava_pool", False, window)
        repository.crt_bcgrndC(350, 175, 400, 225, lava_3, "lava_pool", False, window)

        repository.crt_bcgrndC(450, 75, 500, 125, lava_4, "lava_pool", False, window)

        #

        repository.crt_bcgrndC(-1450, 3525, -1400, 3725, lava_2, "lava_pool", False, window)

        repository.crt_bcgrndC(-1450, 3625, -1400, 3725, lava_3, "lava_pool", False, window)
        repository.crt_bcgrndC(-1400, 3575, -1300, 3675, lava_3, "lava_pool", False, window)

        repository.crt_bcgrndC(-1350, 3575, -1300, 3625, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-1400, 3625, -1350, 3675, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-1250, 3575, -1200, 3625, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-1200, 3525, -1000, 3575, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-1000, 3575, -900, 3625, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-1100, 3675, -1050, 3725, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-900, 3525, -850, 3575, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(-700, 3425, -650, 3475, lava_2, "lava_pool", False, window)

        repository.crt_bcgrndC(-1150, 3525, -1050, 3575, lava_3, "lava_pool", False, window)

        repository.crt_bcgrndC(-1300, 3575, -1250, 3625, lava_4, "lava_pool", False, window)
        repository.crt_bcgrndC(-850, 3525, -800, 3575, lava_4, "lava_pool", False, window)

        #

        repository.crt_bcgrndC(2650, 2125, 2700, 2175, lava_1, "lava_pool", False, window)

        repository.crt_bcgrndC(2800, 2025, 2850, 2125, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(2750, 2075, 2800, 2175, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(2700, 2075, 2800, 2125, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(2600, 2125, 2650, 2175, lava_2, "lava_pool", False, window)
        repository.crt_bcgrndC(2550, 2075, 2600, 2125, lava_2, "lava_pool", False, window)

        repository.crt_bcgrndC(2550, 2125, 2600, 2175, lava_3, "lava_pool", False, window)
        repository.crt_bcgrndC(2500, 2075, 2550, 2125, lava_3, "lava_pool", False, window)

        repository.crt_bcgrndC(2450, 2075, 2500, 2125, lava_4, "lava_pool", False, window)
        repository.crt_bcgrndC(2750, 2025, 2800, 2075, lava_4, "lava_pool", False, window)

        # giant lava pool---------------------------------------------------

        repository.crt_bcgrndC(500, 1825, 900, 1875, lava_1, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(350, 1875, 1000, 2525, lava_1, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(350, 1875, 950, 2575, lava_1, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(300, 1925, 950, 2575, lava_1, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(250, 2075, 300, 2425, lava_1, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 2575, 800, 2625, lava_1, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1000, 1975, 1050, 2475, lava_1, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(350, 1925, 950, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(300, 2075, 1000, 2375, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 1875, 800, 2575, lava_2, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(400, 1975, 500, 2025, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(400, 1975, 450, 2075, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 1925, 650, 1975, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(700, 1925, 800, 1975, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(800, 1975, 900, 2125, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(900, 2075, 950, 2125, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(900, 2175, 950, 2375, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(800, 2425, 900, 2475, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(600, 2475, 700, 2525, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 2475, 550, 2525, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(400, 2375, 500, 2475, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(350, 2175, 400, 2275, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(350, 2075, 400, 2125, lava_3, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(400, 2075, 450, 2175, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(400, 2225, 450, 2275, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(450, 2375, 500, 2425, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 2425, 600, 2475, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(650, 2425, 700, 2475, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(750, 2425, 800, 2475, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(800, 2375, 850, 2425, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(850, 2125, 900, 2375, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(550, 1975, 800, 2025, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(550, 1975, 600, 2075, lava_4, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(450, 2075, 850, 2375, lava_5, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 2375, 650, 2425, lava_5, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(700, 2375, 750, 2425, lava_5, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(600, 2025, 750, 2075, lava_5, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(500, 2025, 550, 2075, lava_6, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(500, 2075, 600, 2125, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(500, 2075, 550, 2225, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(650, 2175, 700, 2275, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(750, 2125, 800, 2175, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(550, 2275, 600, 2325, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(600, 2225, 650, 2275, lava_4, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(600, 2275, 650, 2325, lava_5, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(500, 2125, 550, 2175, lava_6, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(650, 2275, 700, 2375, lava_6, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(600, 2175, 650, 2225, lava_6, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(950, 1875, 1000, 1925, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1000, 1775, 1050, 1875, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1100, 1725, 1150, 1775, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1150, 1675, 1300, 1725, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1200, 1625, 1250, 1675, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1100, 1625, 1150, 1675, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1300, 1625, 1400, 1675, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1250, 1575, 1300, 1625, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1300, 1475, 1350, 1525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1350, 1425, 1400, 1475, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1300, 1375, 1350, 1425, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1050, 1725, 1100, 1775, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1250, 1525, 1300, 1575, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1400, 1375, 1450, 1425, lava_4, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1450, 1325, 1500, 1375, lava_5, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(650, 1725, 700, 1825, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(750, 1725, 800, 1825, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(700, 1575, 750, 1725, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(700, 1575, 750, 1625, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(650, 1375, 700, 1575, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(650, 1375, 700, 1425, lava_1, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(650, 1325, 700, 1375, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(600, 1275, 650, 1375, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(700, 1225, 750, 1375, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(650, 1175, 700, 1225, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(650, 1125, 700, 1175, lava_4, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(350, 1775, 400, 1875, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(300, 1625, 350, 1775, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(200, 1725, 350, 1775, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(100, 1675, 200, 1725, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(50, 1625, 100, 1675, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(0, 1575, 50, 1625, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-50, 1525, 0, 1575, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-50, 1575, 0, 1625, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-100, 1475, -50, 1525, lava_3, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(150, 2025, 300, 2075, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(100, 1975, 150, 2075, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-50, 2075, 100, 2125, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-150, 2125, -50, 2175, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(0, 1925, 100, 1975, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-150, 1975, 0, 2025, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-100, 1975, -50, 2025, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-300, 1925, -150, 1975, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-400, 1975, -250, 2025, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-550, 2025, -400, 2075, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-450, 2025, -400, 2075, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-600, 2075, -550, 2125, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-650, 2075, -600, 2125, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-700, 2075, -650, 2125, lava_4, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-750, 2075, -700, 2125, lava_5, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(50, 2375, 300, 2425, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-100, 2325, 50, 2375, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-50, 2425, 100, 2475, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-200, 2475, -50, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-400, 2525, -200, 2575, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-350, 2525, -250, 2575, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-400, 2475, -350, 2525, lava_1, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-450, 2525, -400, 2575, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-500, 2525, -450, 2575, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-550, 2525, -500, 2575, lava_4, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(300, 2525, 350, 2625, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(300, 2575, 350, 2625, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(150, 2625, 300, 2675, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(200, 2625, 250, 2775, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(200, 2675, 250, 2725, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(100, 2675, 150, 2725, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(50, 2625, 100, 2675, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(50, 2725, 100, 2775, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(0, 2775, 50, 2825, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(0, 2725, 50, 2775, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-50, 2825, 0, 2875, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-250, 2875, -50, 2925, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-200, 2925, -150, 2975, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-200, 2875, -150, 2925, lava_1, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-350, 2925, -250, 2975, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-300, 2925, -250, 2975, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(-450, 2975, -350, 3025, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(-400, 2975, -350, 3025, lava_3, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(650, 2625, 700, 2725, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(700, 2725, 750, 2975, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(750, 2825, 800, 3125, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(750, 2825, 800, 2875, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(750, 2875, 800, 2925, lava_1, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(800, 3125, 850, 3175, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(750, 3175, 800, 3275, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(800, 3275, 850, 3475, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(800, 3325, 850, 3475, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(800, 3375, 850, 3475, lava_4, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(800, 3425, 850, 3475, lava_5, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(900, 2575, 950, 2825, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(900, 2675, 950, 2725, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(950, 2775, 1000, 2825, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1000, 2825, 1050, 2925, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(950, 2925, 1000, 3025, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1000, 3025, 1100, 3075, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1100, 3075, 1150, 3125, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1150, 3125, 1200, 3225, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1100, 3125, 1150, 3175, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1200, 3225, 1300, 3275, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1250, 3275, 1300, 3375, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1300, 3375, 1350, 3425, lava_4, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1300, 3425, 1350, 3475, lava_5, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(1000, 2375, 1050, 2475, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1050, 2425, 1150, 2475, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1100, 2475, 1200, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1200, 2525, 1450, 2575, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1400, 2475, 1650, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1600, 2425, 1650, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1600, 2425, 1700, 2475, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1700, 2375, 1950, 2425, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1700, 2375, 1750, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1750, 2475, 1850, 2525, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1950, 2325, 2000, 2375, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1250, 2525, 1300, 2575, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1500, 2475, 1550, 2525, lava_3, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1850, 2525, 1900, 2575, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1900, 2525, 1950, 2575, lava_4, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1450, 2475, 1500, 2525, lava_1, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1950, 2325, 2000, 2375, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(2000, 2325, 2050, 2375, lava_4, "giant_lava_pool", False, window)

        #

        repository.crt_bcgrndC(1050, 2275, 1200, 2375, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1150, 2225, 1250, 2275, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1250, 2175, 1400, 2225, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1300, 2125, 1400, 2225, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1350, 2175, 1400, 2225, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1400, 2075, 1550, 2125, lava_1, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1450, 2075, 1500, 2125, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1550, 2025, 1650, 2075, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1600, 1975, 1650, 2075, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1600, 1975, 1700, 2025, lava_2, "giant_lava_pool", False, window)
        repository.crt_bcgrndC(1700, 2025, 1800, 2075, lava_2, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1800, 2075, 1900, 2125, lava_3, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1900, 2125, 1950, 2175, lava_4, "giant_lava_pool", False, window)

        repository.crt_bcgrndC(1950, 2125, 2000, 2175, lava_5, "giant_lava_pool", False, window)

# change maps recipe
# elif dialog_option == "2":
#    forest(True, window)
#    for e in gui_text:
#        e.undraw()
#    for e in gui_background:
#        e.undraw()
#    character.char_on_screen(window, True)
#    repository.mov = True

# remove object interaction recipe
# if dialog_option == "1":
#    for e in gui_text:
#        e.undraw()
#    dialog('1.chupa chupa q é d uva', tempx2, tempy1, window)
#    i.remove_obj()
#    repository.npcs.remove(i)