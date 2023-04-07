import config

from lifegame_rule import LifeGameRule

class Calc():
    def __init__(self):
        self.cell_num = config.CELL_NUM
        self.dead = config.DEAD
        self.alive = config.ALIVE

    def out_of_cell_calc(self, j, i):
        """CELL外のセルは死亡とする"""
        out_of_cell = {'min': 0, 'max': self.cell_num}

        if j < out_of_cell['min']:
            return self.dead
        elif j > out_of_cell['max']:
            return self.dead
        elif i < out_of_cell['min']:
            return self.dead
        elif i > out_of_cell['max']:
            return self.dead
        elif j < out_of_cell['min'] and i < out_of_cell['min']:
            return self.dead
        elif j < out_of_cell['max'] and i < out_of_cell['max']:
            return self.dead
        elif j < out_of_cell['max'] and i < out_of_cell['min']:
            return self.dead
        elif j < out_of_cell['min'] and i < out_of_cell['max']:
            return self.dead

    def around_cell_calc(self, cell, j, i):
        """"中央から周辺8個のセルが生きているか死んでいるかを調べる"""
        return  cell[j - 1][i] + cell[j + 1][i] + \
                cell[j][i - 1] + cell[j][i + 1] + \
                cell[j - 1][i - 1] + cell[j + 1][i + 1] + \
                cell[j - 1][i + 1] + cell[j + 1][i - 1]

    def next_cell(self, cell):
        rule = LifeGameRule()
        next_cell = [[0] * self.cell_num for i in range(self.cell_num)]
        out_of_range = 0
        for j in range(len(cell)):
            for i in range(len(cell)):
                center = cell[j][i]
                if j <= 0 and i <= 0 or j >= self.cell_num -1 and i >= self.cell_num -1 or \
                    j <= 0 and i >= self.cell_num - 1 or j >= self.cell_num -1 and i <= self.cell_num - 1 or \
                    j <= 0 or i <= 0 or j >= self.cell_num - 1 or i >= self.cell_num - 1:
                    cell_sum = self.out_of_cell_calc(j, i)
                else:
                    cell_sum = self.around_cell_calc(cell, j, i)

                next_cell[j][i] = rule.is_alive_or_dead(center, cell_sum)
            print()

        return next_cell