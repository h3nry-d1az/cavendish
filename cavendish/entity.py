from typing import Tuple, List
from random import randrange
import pygame

from .r2 import R2
from .shared import cartesian_to_pygame


class Entity(object):
    __trace: List[Tuple[int, int]]

    mass: float
    position: R2
    velocity: R2
    color: Tuple[int, int, int]

    def __init__(
        self,
        mass: float,
        position: R2,
        velocity: R2 = None
    ) -> None:
        self.__trace = []
        self.mass = mass
        self.position = position
        self.velocity = velocity if velocity else R2.Zero()
        self.color = (
            randrange(256),
            randrange(256),
            randrange(256)
        )


    def g(self, witness, G: float) -> R2:
        r = witness.position - self.position
        if (norm := abs(r)) < 5e2:
            norm = 5e2
        return r * (-G*self.mass/norm**3)

    def render(self, screen, camera: R2, scaling: float) -> None:
        self.__trace.append((self.position.x, self.position.y))

        if len(self.__trace) > 100:
            self.__trace.pop(0)

        for point in self.__trace:
            pygame.draw.circle(
                screen,
                self.color,
                cartesian_to_pygame(
                    point[0] - camera.x,
                    point[1] - camera.y,
                    scaling
                ),
                1
            )

        pygame.draw.circle(
            screen,
            pygame.Color(self.color),
            cartesian_to_pygame(
                self.position.x - camera.x,
                self.position.y - camera.y,
                scaling
            ),
            radius=self.mass*scaling
        )
        pygame.draw.circle(
            screen,
            pygame.Color(255, 255, 255),
            cartesian_to_pygame(
                self.position.x - camera.x,
                self.position.y - camera.y,
                scaling
            ),
            radius=(self.mass + 1)*scaling,
            width=int(scaling)
        )