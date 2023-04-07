import time
import random

from lifegame_rule import LifeGameRule

CELL_NUM = 64
ALIVE = 1
DEAD = 0

GENERATION = 2

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

def calc_next_cell(cell, rule):
    next_cell = [[0] * CELL_NUM for i in range(CELL_NUM)]
    out_of_range = 0

    for j in range(len(cell)):
        for i in range(len(cell)):
            center = cell[j][i]
            if j <= 0 and i <= 0 or j >= CELL_NUM -1 and i >= CELL_NUM -1 or \
                j <= 0 and i >= CELL_NUM - 1 or j >= CELL_NUM -1 and i <= CELL_NUM - 1 or \
                j <= 0 or i <= 0 or j >= CELL_NUM - 1 or i >= CELL_NUM - 1:
                cell_sum = out_of_cell_calc(j, i)
            else:
                cell_sum = around_cell_calc(cell, j, i)

            next_cell[j][i] = rule.is_alive_or_dead(center, cell_sum)
        print()

    return next_cell

def main():
    cell = cell_initialize()
    rule = LifeGameRule() 
    for i in range(GENERATION):
        print('Generation: ' + str(i))
        time.sleep(0.5)
        cell = calc_next_cell(cell, rule)
        cell_view(cell)

main() if __name__ == '__main__' else None

