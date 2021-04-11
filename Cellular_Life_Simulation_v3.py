#!/usr/bin/env python3.8.2
# This is a placeholder, feel free to delete everything
# and start from scratch we won't be (too) mad (:
import copy

# --- Read program input from stdin


# birth_conditions_line = "3\n1,2,3,4\n2,2\n3x2\nx__\nxxx\n8\n0,5\n5,0\n" # __x___|xx_xx_|xx_xx_|x___xx|x_x_x_|x__x__\n #####exemple
# birth_conditions_line = "3\n2,3\n1,1\n6x6\n______\n______\n__xx__\n__xx__\n______\n______\n1\n1,1\n6,6\n" #############1
# birth_conditions_line = "3\n2,3\n1,1\n6x6\n______\n__x___\n__x___\n__x___\n______\n______\n5\n1,1\n5,5\n" #_____|_____|_xxx_|_____|_____ #################2
# birth_conditions_line = "3\n1,2,3,4\n1392,-5\n4x2\nxx_x\n_xxx\n40\n1407,-10\n1382,-20\n" #__________________________|______________xx__________|____________xx__x_________|xxx_____xxx______x________|x_x_xx_x_xxx_____x________|__xxxxxx______x_xx________|x_________x_xxxx__________|x_xxxxxxx_x_xx_x_xxx______|xx_x______x_xxxxx_x_x__x__|xx__xxxxxxxx_x____x___xxx_|__xx_______x_xxxxx_xxx__x_ ##################3
birth_conditions_line = "3,5,7\n1,3,5,8\n1,1\n16x12\n_xx__xx__xx__xx_\n_x_xx__x_x____xx\n________________\n_xx__xx__xx__xx_\n_x_xx__x_x_____x\n_xx_____x___x__x\n_xx___x___x____x\n________________\n_xx_____x___x__x\n_x_xx__x_xx_x_x_\n______xxxxx__xx_\nxxx__xx____x___x\n80\n-2,-5\n18,18\n" # _____________________|__________xx_________|__________xxx__x_____|________xx_x___xx____|__________xxx____x___|_______x_xx____x_____|______x_x_x_xx_______|________x_xx_x_x_____|___x___xx__x_xx______|_________x__xx_x_____|_____x____x__x_______|_____________xxxx____|_______x_x_x___x_x___|_________xxxxxx_x____|_______x_xx__xxx_x___|______x_____xxxx_____|______________xxx____|________x____xx_x_x__|_______xx_x____x__x__|________xx_____x_x___|________x__xxxxxx____|________xx__xx_x_____|_____________x_x_____|_____________________ ##############4

# birth_conditions_line = input()
# ... parse other lines based on the challenge instructions
infos = {}
birth_conditions_line_computed = birth_conditions_line.split("\n")
del birth_conditions_line_computed[-1]
if ',' in birth_conditions_line_computed[0]:
    infos["naissance"] = list(map(int, list(dict.fromkeys(birth_conditions_line_computed[0].split(',')))))
else:
    infos["naissance"] = list(map(int,birth_conditions_line_computed[0]))
if ',' in birth_conditions_line_computed[1]:
    infos["survie"] = list(map(int, list(dict.fromkeys(birth_conditions_line_computed[1].split(',')))))
else:
    infos["survie"] = list(map(int,birth_conditions_line_computed[1]))
infos["coordonnees_haut_gauche"] = list(map(int, birth_conditions_line_computed[2].split(',')))
infos["taille_univers"] = list(map(int,birth_conditions_line_computed[3].split('x')))
infos["grille"] = list(map(list,birth_conditions_line_computed[4:-3]))
infos["generation"] = int(birth_conditions_line_computed[-3])
infos["premiere_coordonnees"] = list(map(int, birth_conditions_line_computed[-2].split(',')))
infos["deuxieme_coordonnees"] = list(map(int, birth_conditions_line_computed[-1].split(',')))

def initGrid(list_to_init):
    #create blank rectangle around initial list
    list_to_init.insert(0, ['_']*(len(list_to_init[0])))
    for k in range(len(list_to_init)):
            list_to_init[k].insert(0, '_')
            list_to_init[k].insert(len(list_to_init[0]) + 1, '_')
    list_to_init.insert(len(list_to_init)+1, ['_']*(len(list_to_init[0])))
    return list_to_init

def computeNextStep(list_to_compute):
    computed_list = copy.deepcopy(list_to_compute)

    for j in range(1,len(list_to_compute)-1):
        for i in range(1,len(list_to_compute[0])-1):
            if list_to_compute[j][i] == '_':
                if getNeighbours(list_to_compute, i, j) in infos["naissance"]:
                    computed_list[j][i] = 'x'
            else:
                if getNeighbours(list_to_compute, i, j) not in infos["survie"]:
                    computed_list[j][i] = '_'
    
    return initGrid(computed_list)
                

def getNeighbours(list_to_compute, i, j): 
    #count how many neighbours around
    count = 0
    for k in range(-1,2):
        if list_to_compute[j-1][i+k] == 'x':
            count += 1
        if list_to_compute[j+1][i+k] == 'x':
            count += 1
    if list_to_compute[j][i-1] == 'x':
        count += 1
    if list_to_compute[j][i+1] == 'x':
        count += 1
    return count

def getRectangle(a, b, list_to_compute, start_position, position_initial_grid):
    top_line = a[1] if a[1] > b[1] else b[1]
    last_line = b[1] if a[1] > b[1] else a[1]
    min_column = a[0] if a[0] < b[0] else b[0]
    max_column = b[0] if a[0] < b[0] else a[0]

    list_to_compute[:]
    print(len(list_to_compute[0]), len(list_to_compute))
    # print(position_initial_grid + 2 - start_position[1] - a[0], position_initial_grid + 2 - start_position[0] - top_line)
    # for _ in range(position_initial_grid + 2 - start_position[1] - a[0]):
    #     list_to_compute.pop(0)
    #     list_to_compute.pop()
    # for _ in range(position_initial_grid + 2 - start_position[0] - top_line):
    #     for line in list_to_compute:
    #         line.pop(0)
    #         line.pop()
    # print(len(list_to_compute[0]), len(list_to_compute))
    # for _ in range(top_line, start_position[1] + len())

    

    # # print(top_line ,last_line, min_column, max_column)
    

    
    # while len(list_to_compute) -1 != top_line - last_line:
    #     list_to_compute.pop()

    # while len(list_to_compute[0]) -1 != max_column - min_column:
    #     for line in list_to_compute:
    #         line.pop()

    return list_to_compute

def printReadable(list_to_compute):
    final_list = ""
    for line in list_to_compute:
        final_list += ''.join(line) + '|'
    return final_list[:-1]

if __name__ == '__main__':
    # for line in infos["grille"]:
    #     print(line)
    # print()
    initialized_grid = initGrid(infos["grille"])
    for i in range(infos["generation"]+1):
        # print(i)
        initialized_grid = computeNextStep(initialized_grid)
    # for line in initialized_grid:
    #     print(line)
    # print()
    
    computed_list = getRectangle(infos["premiere_coordonnees"], infos["deuxieme_coordonnees"], initialized_grid, infos["coordonnees_haut_gauche"], infos["generation"])
    for line in computed_list:
        print(line)
    print()
    output = printReadable(computed_list)
    print(output)
    