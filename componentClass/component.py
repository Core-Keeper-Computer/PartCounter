from componentType import ComponentType

class Component(object):
    def __init__(self, type: ComponentType, count: int, items: list) -> None:
        self.type = type
        self.count = count
        self.items = items

    def __str__(self) -> str:
        materials = {}
        for item in self.items:
            for material in item.materials:
                if material.GetName() not in materials:
                    materials[material.GetName()] = 1
                else:
                    materials[material.GetName()]+=1
                
        return materials
