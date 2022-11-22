from componentClass.componentType import ComponentType

class Component(object):
    def __init__(self, type: ComponentType, count: int, items: list) -> None:
        self.type = type
        self.count = count
        self.items = items

    def GetMaterialList(self) -> dict:
        materials = {}
        for i in range(self.count):
            for item in self.items:
                for j in range(item.count):
                    for material in item.materials:
                        for k in range(material.count):
                            if material.GetName() not in materials:
                                materials[material.GetName()] = 1
                            else:
                                materials[material.GetName()]+=1
        return materials
