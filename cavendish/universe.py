import pygame
from entity import Entity, R2
from typing import List
from functools import reduce


class Universe:
    __active: bool
    __screen: pygame.Surface
    __clock: pygame.time.Clock

    G: float
    entities: List[Entity]

    def __init__(self, *entities, G=6.67430e-17) -> None:
        self.__screen = pygame.display.set_mode((640, 480))
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption('Cavendish Spatial Physics Engine')
        
        self.G = G
        self.entities = []
        for entity in entities:
            self.entities.append(entity)

    def execute(self) -> None:
        self.__active = True
        while self.__active:
            self.process(self.__clock.tick(60))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__active = False

    def process(self, delta) -> None:
        self.__screen.fill(pygame.Color(0, 0, 0))
        for entity in self.entities:
            # a = sum(e.position for e in self.entities if e != entity)
            a = reduce(
                lambda v1, v2: v1 + v2,
                (e.g(entity, self.G) for e in self.entities if e != entity)
            )
            if a == 0:
                a = R2(0, 0)
            entity.velocity += a*delta
            entity.position += entity.velocity*delta
            entity.render(self.__screen)
        pygame.display.update()