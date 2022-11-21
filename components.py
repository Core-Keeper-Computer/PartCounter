from componentClass.component import Component
from componentClass.componentType import ComponentType
from items import *

class OneBitVolladdierer(Component):
    def __init__(self, count: int):
        super().__init__(ComponentType.OneBitVolladdierer, count, [Querschluss(14), Kabel(8), Stab(3), Schaltkreis(6), Generator(1)])