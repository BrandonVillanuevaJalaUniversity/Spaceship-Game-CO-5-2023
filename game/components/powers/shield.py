from game.components.powers.power import Power
from game.utils.constants import SHIELD_TYPE, PLAYER_ONE_HEART3

class Shiel(Power):
    def __init__(self,rect):
        self.type = SHIELD_TYPE
        self.is_available = True
        super().__init__(PLAYER_ONE_HEART3, self.type,rect)