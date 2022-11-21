from materialClass.material import Material
from materialClass.materialType import MaterialType

class Holz(Material):
    def __init__(self, count: int):
        super().__init__(MaterialType.Holz, count)

class Kupferbarren(Material):
    def __init__(self, count: int):
        super().__init__(MaterialType.Kupferbarren, count)

class Eisenbarren(Material):
    def __init__(self, count: int):
        super().__init__(MaterialType.Eisenbarren, count)

class Goldbarren(Material):
    def __init__(self, count: int):
        super().__init__(MaterialType.Goldbarren, count)