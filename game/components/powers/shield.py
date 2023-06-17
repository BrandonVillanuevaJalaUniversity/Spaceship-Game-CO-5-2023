from game.components.powers.power import Power
from game.utils.constants import SHIELD_TYPE, SHIELD

class Shiel(Power):
    def __init__(self,rect):
        super().__init__(SHIELD, SHIELD_TYPE,rect)