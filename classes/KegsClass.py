import random


class Kegs():

    def __init__(self):
        self.this_val = None
        self.base_num = self.get_linespace()
        self.remm_num = self.base_num

    def get_linespace(self):
        i0, i1 = 1, 90
        return [i for i in range(i0, i1+1)]

    def get_random_num(self):
        self.this_val = random.choice(self.remm_num)
        self.remm_num.remove(self.this_val)

    def print_num(self):
        n_ost = len(self.remm_num)
        print(f"Новый бочонок: {self.this_val} (осталось {n_ost})")

    def __str__(self):
        print(f"this_val = {self.this_val}; remm_num = {self.remm_num}")

    def __eq__(self, item):
        return self.this_val == item.this_val

    def __ne__(self, item):
        return self.this_val != item.this_val