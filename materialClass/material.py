from materialClass.materialType import MaterialType

class Material(object):
    def __init__(self, type: MaterialType, count: int) -> None:
        self.type = type
        self.count = count

    def GetName(self)->str:
        return MaterialType(self.type).name