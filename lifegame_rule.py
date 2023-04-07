import config

class LifeGameRule():
    def __init__(self):
        self.dead = config.DEAD
        self.alive = config.ALIVE

        self.lifegame_rule = {
            # 誕生 死んでるセルに隣接する生きたセルが3つあれば、次の世代が誕生する
            'birth': self.alive, 
            # 生存 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する
            'survive': self.alive, 
            # 過疎 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する
            'depopulation': self.dead,
            # 過密 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する
            'overcrowding': self.dead, 
        }

    def is_alive_or_dead(self, current_cell, around_cell):
        if current_cell == self.dead:
            if around_cell == 3:
                return self.lifegame_rule['birth']

        if current_cell == self.alive:
            if around_cell == 2 or around_cell == 3:
                return self.lifegame_rule['survive']
            elif around_cell <= 1:
                return self.lifegame_rule['depopulation']
            elif around_cell >= 4:
                return self.lifegame_rule['overcrowding']

        return self.dead