from typing import List
from functools import reduce
import tkinter as tk
from tkinter import ttk
from sys import exit
import pygame

from .entity import Entity, R2
from .shared import pygame_to_cartesian


text =\
{
    "English":\
    {
        "MAIN_WINDOW_TITLE": "Cavendish: Yet another gravitational physics simulator",
        "SETTINGS_WINDOW_TITLE": "Settings panel",

        "G_VALUE": "Value of G:",
        "COLLISIONS": "Collisions enabled:",
        "MAX_FPS": "Maximum FPS:",

        "ENTITY_MASS": "Entity mass:",
        "ENTITY_TRAIL_LENGTH": "Entity trail length:",

        "SHOW_FPS": "Show FPS:",
        "SHOW_CAMERA_POSITION": "Show camera position:",
        "SHOW_ZOOM": "Show camera zoom:",
    },
    "Español":\
    {
        "MAIN_WINDOW_TITLE": "Cavendish: Otro simulador más de físicas gravitatorias",
        "SETTINGS_WINDOW_TITLE": "Panel de configuración",

        "G_VALUE": "Valor de G:",
        "COLLISIONS": "Colisiones activadas:",
        "MAX_FPS": "FPS máximos:",

        "ENTITY_MASS": "Masa del cuerpo:",
        "ENTITY_TRAIL_LENGTH": "Longitud del rastro:",

        "SHOW_FPS": "Mostrar FPS:",
        "SHOW_CAMERA_POSITION": "Mostrar posición de la cámara:",
        "SHOW_ZOOM": "Mostrar zoom de la cámara:",
    }
}

class Universe:
    __active: bool
    __screen: pygame.Surface
    __clock: pygame.time.Clock
    __font: pygame.font.Font

    __language: str
    __settings: bool

    __panel: tk.Tk
    g_value: tk.StringVar
    collisions: tk.BooleanVar
    max_fps: tk.StringVar
    entity_mass: tk.StringVar
    entity_trail_length: tk.StringVar
    show_fps: tk.BooleanVar
    show_camera_position: tk.BooleanVar
    show_zoom: tk.BooleanVar

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
        pygame.display.set_caption(text[language]["MAIN_WINDOW_TITLE"])

        pygame.display.set_icon(pygame.image.load('./assets/favicon-main.ico'))

        if settings:
            def __on_settings_window_close(*_) -> None:
                self.__settings = False
            self.__panel = tk.Tk()
            self.__panel.bind('<Destroy>', __on_settings_window_close)
            self.__panel.title(text[language]["SETTINGS_WINDOW_TITLE"])
            self.__panel.geometry('256x265+154+175')
            self.__panel.resizable(False, False)
            self.__panel.iconbitmap('./assets/favicon.ico')
            self.__panel.columnconfigure(0, weight=3)
            self.__panel.columnconfigure(1, weight=1)

            #=======================================
            # Engine settings
            #=======================================
            self.g_value = tk.StringVar(value=str(G))
            tk.Label(text=text[language]["G_VALUE"], font=("Times New Roman", 12))\
              .grid(column=0, row=1, sticky=tk.W, padx=5, pady=2.5)
            ttk.Entry(font=("Consolas", 12), width=5, textvariable=self.g_value).grid(column=1, row=1, sticky=tk.E, padx=5, pady=2.5)

            self.collisions = tk.BooleanVar(value=False)
            tk.Label(text=text[language]["COLLISIONS"], font=("Times New Roman", 12))\
              .grid(column=0, row=2, sticky=tk.W, padx=5, pady=2.5)
            ttk.Checkbutton(variable=self.collisions).grid(column=1, row=2, sticky=tk.E, padx=5, pady=2.5)

            self.max_fps = tk.StringVar(value="60")
            tk.Label(text=text[language]["MAX_FPS"], font=("Times New Roman", 12))\
              .grid(column=0, row=3, sticky=tk.W, padx=5, pady=2.5)
            ttk.Entry(font=("Consolas", 12), width=5, textvariable=self.max_fps).grid(column=1, row=3, sticky=tk.E, padx=5, pady=2.5)

            ttk.Separator(orient="horizontal").grid(row=4, columnspan=2, pady=2.5, ipadx=100)

            #=======================================
            # Entity settings
            #=======================================
            self.entity_mass = tk.StringVar(value="10")
            tk.Label(text=text[language]["ENTITY_MASS"], font=("Times New Roman", 12))\
              .grid(column=0, row=5, sticky=tk.W, padx=5, pady=2.5)
            ttk.Entry(font=("Consolas", 12), width=5, textvariable=self.entity_mass).grid(column=1, row=5, sticky=tk.E, padx=5, pady=2.5)

            self.entity_trail_length = tk.StringVar(value="100")
            tk.Label(text=text[language]["ENTITY_TRAIL_LENGTH"], font=("Times New Roman", 12))\
              .grid(column=0, row=6, sticky=tk.W, padx=5, pady=2.5)
            ttk.Entry(font=("Consolas", 12), width=5, textvariable=self.entity_trail_length).grid(column=1, row=6, sticky=tk.E, padx=5, pady=2.5)

            ttk.Separator(orient="horizontal").grid(row=7, columnspan=2, pady=2.5, ipadx=100)

            #=======================================
            # Rendering settings
            #=======================================
            self.show_fps = tk.BooleanVar(value=True)
            tk.Label(text=text[language]["SHOW_FPS"], font=("Times New Roman", 12))\
              .grid(column=0, row=8, sticky=tk.W, padx=5, pady=2.5)
            ttk.Checkbutton(variable=self.show_fps).grid(column=1, row=8, sticky=tk.E, padx=5, pady=2.5)

            self.show_camera_position = tk.BooleanVar(value=True)
            tk.Label(text=text[language]["SHOW_CAMERA_POSITION"], font=("Times New Roman", 12))\
              .grid(column=0, row=9, sticky=tk.W, padx=5, pady=2.5)
            ttk.Checkbutton(variable=self.show_camera_position).grid(column=1, row=9, sticky=tk.E, padx=5, pady=2.5)

            self.show_zoom = tk.BooleanVar(value=True)
            tk.Label(text=text[language]["SHOW_ZOOM"], font=("Times New Roman", 12))\
              .grid(column=0, row=10, sticky=tk.W, padx=5, pady=2.5)
            ttk.Checkbutton(variable=self.show_zoom).grid(column=1, row=10, sticky=tk.E, padx=5, pady=2.5)


        self.G = G
        self.entities = []
        for entity in entities:
            self.entities.append(entity)

        self.__language = language
        self.__settings = settings

    def execute(self) -> None:
        self.__active = True
        while True:
            if not self.__settings:
                self.process(self.__clock.tick(60))
            else:
                try:
                    fps = int(self.max_fps.get())
                    self.process(self.__clock.tick(fps))
                except ValueError:
                    self.process(self.__clock.tick(60))

            if self.__settings:
                self.__panel.update()
                try:
                    new_G = float(self.g_value.get())
                    self.G = new_G
                except ValueError:
                    pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

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

                        case pygame.K_SPACE:
                            self.__active = not self.__active

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame_to_cartesian(*pygame.mouse.get_pos(), self.scaling)
                    position = R2(mouse[0], mouse[1]) + self.camera
                    match pygame.mouse.get_pressed():
                        case (False, False, True):
                            for entity in self.entities:
                                if abs(entity.position - position) <= entity.mass:
                                    self.entities.remove(entity)
                        case _:
                            if not self.__settings:
                                self.entities.append(Entity(10, position))
                            else:
                                try:
                                    mass = float(self.entity_mass.get())
                                except ValueError:
                                    mass = 10
                                self.entities.append(Entity(mass, position))

    def process(self, delta: float) -> None:
        self.__screen.fill(pygame.Color(0, 0, 0))

        for entity in self.entities:
            if self.__active:
                try:
                    a = reduce(
                        lambda v1, v2: v1 + v2,
                        (e.g(entity, self.G) for e in self.entities if e != entity)
                    )
                except TypeError:
                    a = R2.Zero()

                acceleration_step = a*delta
                entity.velocity += acceleration_step

                if not self.__settings:
                    entity.position += entity.velocity*delta
                else:
                    if not self.collisions.get():
                        entity.position += entity.velocity*delta
                    else:
                        movement_vector = R2()
                        horizontal_component = True
                        vertical_component = True
                        for to_check_entity in self.entities:
                            if entity == to_check_entity:
                                continue
                            if abs(to_check_entity.position\
                                - (entity.position + R2(entity.velocity.x*delta, 0)))\
                             < (to_check_entity.mass + entity.mass):
                                horizontal_component = False
                            if abs(to_check_entity.position\
                                - (entity.position + R2(0, entity.velocity.y*delta)))\
                             < (to_check_entity.mass + entity.mass):
                                vertical_component = False
                        if horizontal_component:
                            movement_vector.x = entity.velocity.x*delta
                        else:
                            entity.velocity.x -= acceleration_step.x
                        if vertical_component:
                            movement_vector.y = entity.velocity.y*delta
                        else:
                            entity.velocity.y -= acceleration_step.y
                        entity.position += movement_vector

            if not self.__settings:
                entity.render(self.__screen, self.camera, self.scaling, self.__active, 100)
            else:
                try:
                    trail_length = int(self.entity_trail_length.get())
                    entity.render(self.__screen, self.camera, self.scaling, self.__active, trail_length*self.__clock.get_fps()/60)
                except ValueError:
                    entity.render(self.__screen, self.camera, self.scaling, self.__active, 100*self.__clock.get_fps()/60)

        text_camera_position = self.__font.render(f'({self.camera.x}, {self.camera.y})', True, (255, 255, 255))
        text_scaling = self.__font.render(f'{self.scaling*100:.2f}%', True, (255, 255, 255))
        text_fps = self.__font.render(f'{self.__clock.get_fps():.2f}', True, (255, 255, 255))

        if not self.__settings:
            self.__screen.blit(text_camera_position, (10, 10))
            self.__screen.blit(text_scaling, (575, 10))
            self.__screen.blit(text_fps, (10, 450))
        else:
            if self.show_camera_position.get():
                self.__screen.blit(text_camera_position, (10, 10))
            if self.show_zoom.get():
                self.__screen.blit(text_scaling, (575, 10))
            if self.show_fps.get():
                self.__screen.blit(text_fps, (10, 450))

        pygame.display.update()