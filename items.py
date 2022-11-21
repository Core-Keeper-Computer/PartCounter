from itemClass.item import Item
from itemClass.itemType import ItemType
from materials import *

class Generator(Item):
    def __init__(self, count: int):
        super().__init__(ItemType.Generator, count, [Eisenbarren(5), Kupferbarren(10), Goldbarren(1)])

class Stab(Item):
    def __init__(self, count: int):
        super().__init__(ItemType.Stab, count, [Holz(1), Kupferbarren(2)])

class Kabel(Item):
    def __init__(self, count: int):
        super().__init__(ItemType.Kabel, count, [Kupferbarren(1)])

class Querschluss(Item):
    def __init__(self, count: int):
        super().__init__(ItemType.Querschluss, count, [Kupferbarren(1)])

class Verzögerer(Item):
    def __init__(self, count: int):
        super().__init__(ItemType.Verzögerer, count, [Kupferbarren(1), Eisenbarren(1)])

class Schaltkreis(Item):
    def __init__(self, count: int):
        super().__init__(ItemType.Schaltkreis, count, [Kupferbarren(1), Eisenbarren(1)])