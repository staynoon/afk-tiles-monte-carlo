import random
import numpy as np

class Tiles:
    def __init__(self,keynum,tile_cost):
        self.cost = tile_cost
        self.key = keynum
        self.current_keys = keynum
        self.floor = 0

    def flip(self):

        self.current_keys = self.key
        self.floor = 0

        self.board()


    def board(self):

        reward_position = random.randint(1,36)

        if self.current_keys < self.cost:
            return
        else:
            if int(self.current_keys/self.cost) < reward_position:
                return
            else:
                self.floor += 1
                self.current_keys -= reward_position * self.cost
                self.board()

    def monte_carlo(self,runs):
        floor_count = np.zeros(runs).astype(int)
        for lv1 in range(runs):
            self.flip()
            floor_count[lv1] = self.floor

        return floor_count