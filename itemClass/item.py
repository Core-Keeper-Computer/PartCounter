from itemType import ItemType

class Item(object):
    def __init__(self, type: ItemType, count: int, materials: list) -> None:
        self.type = type
        self.count = count
        self.materials = materials

    def __str__(self):
        # return "{0} {1}".format(self.street, self.number)
        pass