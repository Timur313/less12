import random


class PlayerCard():

    def __init__(self, base_num):
        self.player_nums = []
        self.base_num = base_num

        self.print_location = []

        self.n_col = 3
        self.n_row = 9
        self.n_lay = 5

    def __str__(self):
        print(f"player_nums = {self.player_nums}")

    def __eq__(self, item):
        return self.player_nums == item.player_nums

    def __ne__(self, item):
        return self.player_nums != item.player_nums

    def print_card(self):
        print("-"*26)

        for l, mass in enumerate(self.print_location):
            line = []
            for i in range(self.n_row):
                cell = "  "
                if i in mass:
                    ind = int(mass.index(i) + l * self.n_lay)
                    val = self.player_nums[ind]
                    if val is None:
                        cell = "--"
                    elif val < 10:
                        cell = f" {val}"
                    else:
                        cell = str(val)
                line.append(cell)
            print(" ".join(line))
        print("-"*26)


    def create_card(self):
        line9 = [i for i in range(0, self.n_row)]

        self.player_nums = random.sample(self.base_num, k=int(self.n_col * self.n_lay))

        for i in range(self.n_col):
            use_pos_lay = random.sample(line9, k=self.n_lay)
            use_pos_lay = sorted(use_pos_lay)
            self.print_location.append( use_pos_lay )


    def remove_num(self, val):
        if val in self.player_nums:
            i = self.player_nums.index(val)
            self.player_nums[i] = None
        else:
            raise("Вы не верно зачеркнули число! Игра окончена!")



