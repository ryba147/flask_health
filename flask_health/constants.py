import enum


class GenderEnum(enum.Enum):
    male = 'male'
    female = 'female'


class BloodTypeEnum(enum.Enum):
    O = 'O'
    A = 'A'
    B = 'B'
    AB = 'AB'


class RhesusFactorEnum(enum.Enum):
    positive = 'positive'
    negative = 'negative'


class HospitalTypeEnum(enum.Enum):
    private = 'private'
    government = 'government'
