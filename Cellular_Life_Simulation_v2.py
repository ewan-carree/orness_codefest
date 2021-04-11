#!/usr/bin/env python3.8.2
# This is a placeholder, feel free to delete everything
# and start from scratch we won't be (too) mad (:
import copy

# --- Read program input from stdin
# birth_conditions_line = "3\n1,2,3,4\n1392,-5\n4x2\nxx_x\n_xxx\n40\n1407,-10\n1382,-20\n" #__________________________|______________xx__________|____________xx__x_________|xxx_____xxx______x________|x_x_xx_x_xxx_____x________|__xxxxxx______x_xx________|x_________x_xxxx__________|x_xxxxxxx_x_xx_x_xxx______|xx_x______x_xxxxx_x_x__x__|xx__xxxxxxxx_x____x___xxx_|__xx_______x_xxxxx_xxx__x_

# birth_conditions_line = "3\n1,2,3,4\n2,2\n3x2\nx__\nxxx\n8\n0,5\n5,0\n" # __x___|xx_xx_|xx_xx_|x___xx|x_x_x_|x__x__\n

birth_conditions_line = "3\n2,3\n1,1\n6x6\n______\n__x___\n__x___\n__x___\n______\n______\n5\n1,1\n5,5\n" #_____|_____|_xxx_|_____|_____

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


def initGrid(a, b, grid, start):
    top_line = a[1] if a[1] > b[1] else b[1]
    last_line = b[1] if a[1] > b[1] else a[1]
    first_column = a[0] if a[0] < b[0] else b[0]
    end_column = b[0] if a[0] < b[0] else a[0]

    decalage_x = decalage_y = 0
    if not first_column <= start[0] + len(grid[0]) <= end_column:
        if start[0] + len(grid[0]) < first_column:
            decalage_x = abs(first_column) - abs(start[0])
            first_column = start[0] + len(grid[0])
        elif start[0] + len(grid[0]) > end_column:
            decalage_x = abs(end_column) - abs(start[0])
            end_column = start[0] + len(grid[0])
        else:
            print("error")

    if not last_line <= start[1] + len(grid) <= top_line:
        if start[1] + len(grid) < last_line:
            decalage_y = abs(last_line) - abs(start[1])
            last_line = start[1] + len(grid)
        elif start[1] + len(grid) > top_line:
            decalage_y = abs(top_line) - abs(start[1])
            top_line = start[1] + len(grid)
        else:
            print("error")

    decalage = (decalage_x, decalage_y)
    print("decalage" + str(decalage))

    rectangle = (top_line, last_line, first_column, end_column)

    # print(first_column, end_column, top_line, last_line) 
    # end_column -= first_column
    # first_column = 0
    # top_line -= last_line
    # last_line = 0
    # print(first_column, end_column, top_line, last_line) 
    
    blank_grid = []
    for _ in range(last_line, top_line):
        line = []
        for _ in range(first_column, end_column):
            line.append('_')
        blank_grid.append(line)
    for line in blank_grid:
        print(line)
    print(str(len(blank_grid[0])) + "x" + str(len(blank_grid)))
    print()

    return blank_grid, decalage, rectangle

def fillGrid(blank_grid, grid, start, rectangle):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == 'x':
                blank_grid[j][i + start[0] - rectangle[2]] = 'x'#################################
    for line in blank_grid:
        print(line)
    print(str(len(blank_grid[0])) + "x" + str(len(blank_grid)))
    print()

    #create blank rectangle around initial list
    blank_grid.insert(0, ['_']*(len(blank_grid[0])))
    for k in range(len(blank_grid)):
            blank_grid[k].insert(0, '_')
            blank_grid[k].insert(len(blank_grid[0]) + 1, '_')
    blank_grid.insert(len(blank_grid)+1, ['_']*(len(blank_grid[0])))
    for line in blank_grid:
        print(line)
    print(str(len(blank_grid[0])) + "x" + str(len(blank_grid)))
    print()
    return blank_grid

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
    return computed_list
                

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

def getRectangle(a, b, list_to_compute, decalage):
    # print(decalage)
    top_line = a[1] if a[1] > b[1] else b[1]
    last_line = b[1] if a[1] > b[1] else a[1]
    min_column = a[0] if a[0] < b[0] else b[0]
    max_column = b[0] if a[0] < b[0] else a[0]

    # for line in list_to_compute:
    #     print(line)
    # print()

    list_to_compute.pop()
    list_to_compute.pop(0)
    for line in list_to_compute:
        line.pop()
        line.pop(0)

    # for line in list_to_compute:
    #     print(line)
    # print()

    # print(decalage)

    x = decalage[0]
    y = decalage[1]

    if y > 0:
        while y != 0:
            y -= 1
            list_to_compute.pop()
    elif y < 0:
        while y != 0:
            y += 1
            list_to_compute.pop(0)
    
    if x > 0:
        while x != 0:
            x -= 1
            for line in list_to_compute:
                line.pop(0)
    elif x < 0:
        while x != 0:
            x += 1
            for line in list_to_compute:
                line.pop()
    else:
        return list_to_compute 

    # for line in list_to_compute:
    #     print(line)
    # print()
    # print(len(list_to_compute), len(list_to_compute[0]))
    # print(top_line, last_line, min_column, max_column)

    computed_list = []
    for j in range(abs(last_line) - abs(top_line) + 1):
        # print(j)
        computed_list.append(list_to_compute[j])
        # for line in computed_list:
        #     print(line)
        # print()
    # for line in computed_list:
    #     line[min_column:max_column]
    # for j in range(top_line - last_line + 1):
    #     for i in range(max_column - min_column + 1):
    #         pass

    return computed_list

def printReadable(list_to_compute):
    final_list = ""
    for line in list_to_compute:
        final_list += ''.join(line) + '|'
    return final_list[:-1]

if __name__ == '__main__':
    blank_grid, decalage, rectangle = initGrid(infos["premiere_coordonnees"], infos["deuxieme_coordonnees"], infos["grille"], infos["coordonnees_haut_gauche"])
    filled_grid = fillGrid(blank_grid, infos["grille"], infos["coordonnees_haut_gauche"], rectangle)
    for i in range(infos["generation"]):
        filled_grid = computeNextStep(filled_grid)
        for line in filled_grid:
            print(line)
        print()

    grid = getRectangle(infos["premiere_coordonnees"], infos["deuxieme_coordonnees"], filled_grid, decalage)
    # for line in grid:
    #     print(line)
    # print()

    output = printReadable(grid)

    print(output)