from game.components.powers.power import Power
from game.utils.constants import HEAVY_TYPE, HEAVI_IMG

class Heavy(Power):
    def __init__(self,rect):
        self.type = HEAVY_TYPE
        self.is_available = True
        super().__init__(HEAVI_IMG, self.type,rect)