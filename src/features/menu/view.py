import pygame

from src.constants.game import SCREEN_H, SCREEN_W
from src.constants.paths import FONT_PRIMARY, GRAPHIC_PLAYER_STAND

_FONT_SIZE = 50
_COLOR_BG = (94, 129, 162)
_COLOR_TEXT = (111, 196, 169)
_TEXT_Y = 340


class MenuView:
    def __init__(self, screen: pygame.Surface) -> None:
        self._screen = screen

        font = pygame.font.Font(FONT_PRIMARY, _FONT_SIZE)

        player_stand_surface: pygame.Surface = pygame.transform.scale2x(pygame.image.load(GRAPHIC_PLAYER_STAND).convert_alpha())
        self._player_stand_surface = player_stand_surface
        self._player_stand_rect = player_stand_surface.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2))

        self._press_space_surface: pygame.Surface = font.render("Press Space to Start", False, _COLOR_TEXT)
        self._press_space_rect = self._press_space_surface.get_rect(center=(SCREEN_W // 2, _TEXT_Y))

    def render(self) -> None:
        self._screen.fill(_COLOR_BG)
        self._screen.blit(self._player_stand_surface, self._player_stand_rect)
        self._screen.blit(self._press_space_surface, self._press_space_rect)
