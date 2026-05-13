from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pygame
import pytest

from src.configs.default_config import DefaultConfig
from src.features.player.model import PlayerModel
from src.game import Game


@pytest.fixture(scope="function")
def mock_assets() -> Generator[None, None, None]:
    real_surface: pygame.Surface = pygame.Surface((50, 50))
    mock_image: MagicMock = MagicMock()
    mock_image.convert.return_value = real_surface
    mock_image.convert_alpha.return_value = real_surface
    mock_sound_instance: MagicMock = MagicMock()
    mock_font_instance: MagicMock = MagicMock()
    mock_font_instance.render.return_value = real_surface
    with (
        patch("pygame.image.load", return_value=mock_image),
        patch("pygame.mixer.Sound", return_value=mock_sound_instance),
        patch("pygame.font.Font", return_value=mock_font_instance),
        patch("pygame.transform.scale2x", return_value=real_surface),
    ):
        yield


@pytest.fixture(scope="function")
def game(mock_assets: None) -> Game:
    return Game(DefaultConfig())


class TestGameTitle:
    @pytest.mark.unit
    def test_title_is_string(self) -> None:
        assert isinstance(Game.TITLE, str)

    @pytest.mark.unit
    def test_title_value(self) -> None:
        assert Game.TITLE == "Python Pygame Boilerplate"


class TestGameInit:
    @pytest.mark.unit
    def test_initial_game_started_is_false(self, game: Game) -> None:
        assert game.game_started is False

    @pytest.mark.unit
    def test_config_is_stored(self, game: Game) -> None:
        assert isinstance(game.config, DefaultConfig)

    @pytest.mark.unit
    def test_screen_is_surface(self, game: Game) -> None:
        assert isinstance(game.screen, pygame.Surface)

    @pytest.mark.unit
    def test_screen_width(self, game: Game) -> None:
        assert game.screen.get_width() == 800

    @pytest.mark.unit
    def test_screen_height(self, game: Game) -> None:
        assert game.screen.get_height() == 400

    @pytest.mark.unit
    def test_clock_is_clock(self, game: Game) -> None:
        assert isinstance(game.clock, pygame.time.Clock)

    @pytest.mark.unit
    def test_player_group_is_group_single(self, game: Game) -> None:
        assert isinstance(game.player_single_group, pygame.sprite.GroupSingle)


class TestGameProperties:
    @pytest.mark.unit
    def test_game_started_property_is_false(self, game: Game) -> None:
        assert game.game_started is False

    @pytest.mark.unit
    def test_player_property_returns_player_model(self, game: Game) -> None:
        assert isinstance(game.player, PlayerModel)

    @pytest.mark.unit
    def test_player_property_returns_none_when_group_empty(self, game: Game) -> None:
        game.player_single_group.empty()
        assert game.player is None

    @pytest.mark.unit
    def test_config_property_returns_config(self, game: Game) -> None:
        assert isinstance(game.config, DefaultConfig)

    @pytest.mark.unit
    def test_screen_property_returns_surface(self, game: Game) -> None:
        assert isinstance(game.screen, pygame.Surface)

    @pytest.mark.unit
    def test_clock_property_returns_clock(self, game: Game) -> None:
        assert isinstance(game.clock, pygame.time.Clock)

    @pytest.mark.unit
    def test_player_single_group_property(self, game: Game) -> None:
        assert isinstance(game.player_single_group, pygame.sprite.GroupSingle)


class TestGameHandleEvents:
    @pytest.mark.unit
    def test_space_keydown_starts_game(self, game: Game) -> None:
        event: pygame.event.Event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_SPACE})
        with patch("pygame.event.get", return_value=[event]):
            game._handle_events()
        assert game.game_started is True

    @pytest.mark.unit
    def test_space_key_ignored_when_game_already_started(self, game: Game) -> None:
        game._game_started = True
        event: pygame.event.Event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_SPACE})
        with patch("pygame.event.get", return_value=[event]):
            game._handle_events()
        assert game.game_started is True

    @pytest.mark.unit
    def test_quit_event_sets_running_false(self, game: Game) -> None:
        quit_event: pygame.event.Event = pygame.event.Event(pygame.QUIT)
        with patch("pygame.event.get", return_value=[quit_event]):
            game._handle_events()
        assert game._running is False

    @pytest.mark.unit
    def test_no_events_does_not_change_state(self, game: Game) -> None:
        with patch("pygame.event.get", return_value=[]):
            game._handle_events()
        assert game.game_started is False

    @pytest.mark.unit
    def test_space_starts_music(self, game: Game) -> None:
        event: pygame.event.Event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_SPACE})
        with patch("pygame.event.get", return_value=[event]):
            game._handle_events()
        game._bg_music.play.assert_called_once_with(loops=-1)
