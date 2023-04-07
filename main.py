import time
import random

import sys

CELL_NUM = 64
ALIVE = 1
DEAD = 0

GENERATION = 20

def lifegame_rule(current_cell, around_cell):
    LifeGameRule = {
        # 誕生 死んでるセルに隣接する生きたセルが3つあれば、次の世代が誕生する
        'birth': ALIVE, 
        # 生存 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する
        'survive': ALIVE, 
        # 過疎 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する
        # 過密 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する
        'depopulation_overcrowding': DEAD, 
    }

    if current_cell == DEAD:
        if around_cell == 3:
            return LifeGameRule['birth']
    if current_cell == ALIVE:
        if around_cell == 2 or around_cell == 3:
            return LifeGameRule['survive']

    return LifeGameRule['depopulation_overcrowding']

def cell_initialize():
    cell = [[0] * CELL_NUM for i in range(CELL_NUM)]

    for j in range(len(cell)):
        for i in range(len(cell)):
            rand_num = int(random.uniform(DEAD, ALIVE + 1))
            cell[j][i] = rand_num

    return cell

def cell_view(cell):
    for j in range(len(cell)):
        for i in range(len(cell)):
            if cell[j][i] == ALIVE:
                print('■', end='')
            else:
                print('□', end='')
        print('')

def out_of_cell_calc(j, i):
    """CELL外のセルは死亡とする"""
    out_of_cell = {'min': 0, 'max': CELL_NUM}

    if j < out_of_cell['min']:
        return DEAD
    elif j > out_of_cell['max']:
        return DEAD
    elif i < out_of_cell['min']:
        return DEAD
    elif i > out_of_cell['max']:
        return DEAD
    elif j < out_of_cell['min'] and i < out_of_cell['min']:
        return DEAD
    elif j < out_of_cell['max'] and i < out_of_cell['max']:
        return DEAD
    elif j < out_of_cell['max'] and i < out_of_cell['min']:
        return DEAD
    elif j < out_of_cell['min'] and i < out_of_cell['max']:
        return DEAD

def around_cell_calc(cell, j, i):
    """"中央から周辺8個のセルが生きているか死んでいるかを調べる"""
    return  cell[j - 1][i] + cell[j + 1][i] + \
            cell[j][i - 1] + cell[j][i + 1] + \
            cell[j - 1][i - 1] + cell[j + 1][i + 1] + \
            cell[j - 1][i + 1] + cell[j + 1][i - 1]

def calc_next_cell(cell):
    next_cell = [[0] * CELL_NUM for i in range(CELL_NUM)]
    out_of_range = 0

    for j in range(len(cell)):
        for i in range(len(cell)):
            center = cell[j][i]
            if j <= 0 and i <= 0 or j >= CELL_NUM -1 and i >= CELL_NUM -1 or \
                j <= 0 and i >= CELL_NUM - 1 or j >= CELL_NUM -1 and i <= CELL_NUM - 1 or \
                j <= 0 or i <= 0 or j >= CELL_NUM - 1 or i >= CELL_NUM - 1:
                cell_sum = center + out_of_cell_calc(j, i)
            else:
                cell_sum = center + around_cell_calc(cell, j, i)

            next_cell[j][i] = lifegame_rule(center, cell_sum)

    return next_cell

def main():
    cell = cell_initialize()
    
    for i in range(GENERATION):
        print('Generation: ' + str(i))
        time.sleep(0.5)
        cell = calc_next_cell(cell)
        cell_view(cell)

main() if __name__ == '__main__' else None

