from dataclasses import dataclass, field
from typing import Dict, Any
from math import sqrt
import pygame
from shared import cartesian_to_pygame

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


@dataclass
class Entity(object):
    mass: float
    position: R2
    velocity: R2 = field(default_factory=R2)
    render_params: Dict[str, Any] = field(default_factory=dict)

    def g(self, witness, G: float) -> R2:
        r = witness.position - self.position
        return r * (-G*self.mass/abs(r)**3)

    def render(self, screen) -> None:
        pygame.draw.circle(
            screen,
            pygame.Color(self.render_params['color']),
            cartesian_to_pygame(
                self.position.x,
                self.position.y
            ),
            radius=self.render_params['radius']
        )