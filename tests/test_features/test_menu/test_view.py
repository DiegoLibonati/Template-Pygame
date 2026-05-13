from unittest.mock import MagicMock, patch

import pygame
import pytest

from src.constants.game import SCREEN_H, SCREEN_W
from src.features.menu.view import MenuView


@pytest.fixture(scope="function")
def mock_assets() -> None:
    real_surface: pygame.Surface = pygame.Surface((50, 50))
    mock_image: MagicMock = MagicMock()
    mock_image.convert_alpha.return_value = real_surface
    mock_font_instance: MagicMock = MagicMock()
    mock_font_instance.render.return_value = real_surface
    with (
        patch("pygame.image.load", return_value=mock_image),
        patch("pygame.font.Font", return_value=mock_font_instance),
        patch("pygame.transform.scale2x", return_value=real_surface),
    ):
        yield


@pytest.fixture(scope="function")
def screen() -> pygame.Surface:
    return pygame.Surface((SCREEN_W, SCREEN_H))


@pytest.fixture(scope="function")
def menu_view(mock_assets: None, screen: pygame.Surface) -> MenuView:
    return MenuView(screen)


class TestMenuViewInit:
    @pytest.mark.unit
    def test_screen_is_stored(self, menu_view: MenuView, screen: pygame.Surface) -> None:
        assert menu_view._screen is screen

    @pytest.mark.unit
    def test_player_stand_surface_is_surface(self, menu_view: MenuView) -> None:
        assert isinstance(menu_view._player_stand_surface, pygame.Surface)

    @pytest.mark.unit
    def test_player_stand_rect_is_centered(self, menu_view: MenuView) -> None:
        assert menu_view._player_stand_rect.centerx == SCREEN_W // 2
        assert menu_view._player_stand_rect.centery == SCREEN_H // 2

    @pytest.mark.unit
    def test_press_space_surface_is_surface(self, menu_view: MenuView) -> None:
        assert isinstance(menu_view._press_space_surface, pygame.Surface)

    @pytest.mark.unit
    def test_press_space_rect_is_centered_x(self, menu_view: MenuView) -> None:
        assert menu_view._press_space_rect.centerx == SCREEN_W // 2


class TestMenuViewRender:
    @pytest.mark.unit
    def test_render_does_not_raise(self, menu_view: MenuView) -> None:
        menu_view.render()

    @pytest.mark.unit
    def test_render_fills_screen(self, menu_view: MenuView, screen: pygame.Surface) -> None:
        menu_view.render()
        assert screen.get_at((0, 0)) == (94, 129, 162, 255)
