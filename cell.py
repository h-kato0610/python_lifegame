import config

import random

class Cell():
    def __init__(self):
        self.cell_num = config.CELL_NUM
        self.dead = config.DEAD
        self.alive = config.ALIVE
        self.min = 0
        self.max = 2
        self.cell = [[0] * self.cell_num for i in range(self.cell_num)]
        
        for j in range(len(self.cell)):
            for i in range(len(self.cell)):
                rand_num = int(random.uniform(self.min, self.max))
                self.cell[j][i] = rand_num

    def get_cell(self):
        return self.cell

    def cell_view(self, in_cell):
        for j in range(len(in_cell)):
            for i in range(len(in_cell)):
                if in_cell[j][i] == self.alive:
                    print('■', end='')
                else:
                    print('□', end='')
            print('') 
