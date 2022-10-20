from enum import Enum


class Choice(Enum):
    @classmethod
    def choice(cls):
        return [(c.value, c.name) for c in cls]


    @classmethod
    def repr(cls):
        return {c.name: {'id': c.value, 'name':c.name} for c in cls}

    @classmethod
    def list(cls):
        return [c.value for c in cls]

    def __str__(self):
        return self.value


class CityChoice(str, Choice):
    ALMATY = 'Almaty'
    ASTANA = 'ASTANA'
    KOKSHETAU ='KOKSHETAU'
    AKTAU = 'AKTAU'
    ATYRAU = 'ATYRAU'
    ORAL = 'ORAL'
    SHYMKENT = 'SHYMKENT'


class STATUSChoice(str, Choice):
    FLEW_OUT = 'FLEW_OUT'
    LANDED = 'LANDED'
    LANDING = 'LANDING'
    DETAIND = 'DETAIND'


