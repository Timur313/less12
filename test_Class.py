from classes.PlayerCardClass import PlayerCard
from classes.KegsClass import Kegs

class TestKegs():

    def setup(self):
        self.obj = Kegs()

    def test_get_linespace_v1(self):
        assert isinstance(self.obj.base_num, list)

    def test_get_linespace_v2(self):
        assert len(self.obj.base_num) == 90

    def test_get_random_num_v1(self):
        #old_mass = self.obj.remm_num
        old_mass = list(self.obj.remm_num).copy()
        self.obj.get_random_num()
        assert self.obj.this_val in old_mass

    def test_get_random_num_v2(self):
        n1 = len(self.obj.remm_num)
        self.obj.get_random_num()
        n2 = len(self.obj.remm_num)
        assert n1 == n2+1



class TestPlayerCard():

    def setup(self):
        self.kegs = Kegs()
        self.obj = PlayerCard(self.kegs.base_num)


    def test_create_card(self):
        self.obj.create_card()

        n = self.obj.n_col * self.obj.n_lay
        assert len(self.obj.player_nums) == n

    def test_remove_num(self):
        val = 50
        try:
            self.obj.remove_num(val)
        except:
            if val in self.obj.player_nums:
                assert False
            else:
                assert True
        else:
            if val in self.obj.player_nums:
                assert True
            else:
                assert False


