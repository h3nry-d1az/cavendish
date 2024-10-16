from typing import List
from functools import reduce
import tkinter as tk
import pygame

from .entity import Entity, R2
from .shared import pygame_to_cartesian


class Universe:
    __active: bool
    __screen: pygame.Surface
    __clock: pygame.time.Clock
    __font: pygame.font.Font

    __language: str
    __settings: bool

    __panel: tk.Tk

    camera: R2
    scaling: float = 1
    G: float
    entities: List[Entity]

    def __init__(self, *entities, G=6.67430, language='English', settings=True) -> None:
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.init()
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.Font(size=22)
        self.camera = R2.Zero()
        match language:
            case 'English':
                pygame.display.set_caption('Cavendish: Yet another gravitational physics simulator')
            case 'Español':
                pygame.display.set_caption('Cavendish: Otro simulador más de físicas gravitatorias')

        pygame.display.set_icon(pygame.image.load('./assets/favicon-main.ico'))

        if settings:
            self.__panel = tk.Tk()
            self.__panel.title('Settings panel')
            self.__panel.geometry('256x256+154+175')
            self.__panel.resizable(False, False)
            self.__panel.iconbitmap('./assets/favicon.ico')

        self.G = G
        self.entities = []
        for entity in entities:
            self.entities.append(entity)

        self.__language = language
        self.__settings = settings

    def execute(self) -> None:
        self.__active = True
        while self.__active:
            self.process(self.__clock.tick(60))
            if self.__settings:
                self.__panel.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__active = False

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            self.camera.x -= int(100/self.scaling)
                        case pygame.K_RIGHT:
                            self.camera.x += int(100/self.scaling)
                        case pygame.K_UP:
                            self.camera.y += int(100/self.scaling)
                        case pygame.K_DOWN:
                            self.camera.y -= int(100/self.scaling)
                        
                        case pygame.K_PLUS:
                            if self.scaling >= 1:
                                self.scaling += 0.5
                            else:
                                self.scaling *= 2

                        case pygame.K_MINUS:
                            if self.scaling >= 1:
                                self.scaling -= 0.5
                            else:
                                self.scaling /= 2

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame_to_cartesian(*pygame.mouse.get_pos(), self.scaling)
                    position = R2(mouse[0], mouse[1]) + self.camera
                    match pygame.mouse.get_pressed():
                        case (False, False, True):
                            for entity in self.entities:
                                if abs(entity.position - position) <= entity.mass:
                                    self.entities.remove(entity)
                        case _:
                            self.entities.append(Entity(10, position))

    def process(self, delta) -> None:
        self.__screen.fill(pygame.Color(0, 0, 0))

        for entity in self.entities:
            try:
                a = reduce(
                    lambda v1, v2: v1 + v2,
                    (e.g(entity, self.G) for e in self.entities if e != entity)
                )
            except TypeError:
                a = R2.Zero()

            entity.velocity += a*delta
            entity.position += entity.velocity*delta
            entity.render(self.__screen, self.camera, self.scaling)

        text_camera_position = self.__font.render(f'({self.camera.x}, {self.camera.y})', True, (255, 255, 255))
        text_scaling = self.__font.render(f'{self.scaling*100:.2f}%', True, (255, 255, 255))
        text_fps = self.__font.render(f'{self.__clock.get_fps():.2f}', True, (255, 255, 255))

        self.__screen.blit(text_camera_position, (10, 10))
        self.__screen.blit(text_scaling, (575, 10))
        self.__screen.blit(text_fps, (10, 450))

        pygame.display.update()