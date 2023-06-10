import time
import random

import config

from calc import Calc
from cell import Cell

def main():
    calc = Calc()
    cell = Cell()

    calc_cell = cell.get_cell()
    for i in range(config.GENERATION):
        print('Generation: ' + str(i))
        time.sleep(0.5)
        calc_cell = calc.next_cell(calc_cell)
        cell.cell_view(calc_cell)

main() if __name__ == '__main__' else None

