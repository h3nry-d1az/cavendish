from dataclasses import dataclass
from math import sqrt


@dataclass
class R2(object):
    x: float = 0.
    y: float = 0.

    def __add__(self, other):
        assert isinstance(other, R2)
        return R2(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return self + other*(-1)

    def __mul__(self, other):
        assert isinstance(other, int) or isinstance(other, float)
        return R2(other*self.x, other*self.y)

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    @classmethod
    def Zero(cls, *_, **__):
        return cls(0, 0)