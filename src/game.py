import pygame

from src.configs.default_config import DefaultConfig
from src.constants.game import GROUND_Y, SCREEN_H, SCREEN_W
from src.constants.paths import GRAPHIC_GROUND, GRAPHIC_SKY, SOUND_MUSIC
from src.features.menu.view import MenuView
from src.features.player.model import PlayerModel

_FPS = 60
_MUSIC_VOLUME = 0.1


class Game:
    TITLE = "Python Pygame Boilerplate"

    def __init__(self, config: DefaultConfig) -> None:
        pygame.init()

        self._config = config
        self._game_started: bool = False
        self._running: bool = True

        pygame.display.set_caption(self.TITLE)
        self._screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self._clock = pygame.time.Clock()
        self._player_single_group: pygame.sprite.GroupSingle = pygame.sprite.GroupSingle()

        self._load_assets()
        self._menu = MenuView(self._screen)
        self._setup()

    # --- Properties ---

    @property
    def screen(self) -> pygame.Surface:
        return self._screen

    @property
    def game_started(self) -> bool:
        return self._game_started

    @property
    def config(self) -> DefaultConfig:
        return self._config

    @property
    def player_single_group(self) -> pygame.sprite.GroupSingle:
        return self._player_single_group

    @property
    def player(self) -> PlayerModel | None:
        sprites = self._player_single_group.sprites()
        return sprites[0] if sprites else None

    @property
    def clock(self) -> pygame.time.Clock:
        return self._clock

    # --- Init helpers ---

    def _load_assets(self) -> None:
        self._bg_music = pygame.mixer.Sound(SOUND_MUSIC)
        self._sky_surface = pygame.image.load(GRAPHIC_SKY).convert()
        self._ground_surface = pygame.image.load(GRAPHIC_GROUND).convert()

    def _setup(self) -> None:
        self._bg_music.set_volume(_MUSIC_VOLUME)
        self._player_single_group.add(PlayerModel())

    # --- Game loop ---

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if not self._game_started and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._game_started = True
                self._bg_music.play(loops=-1)

    def _render_game(self) -> None:
        self._screen.blit(self._sky_surface, (0, 0))
        self._screen.blit(self._ground_surface, (0, GROUND_Y))
        self._player_single_group.draw(surface=self._screen)
        self._player_single_group.update()

        if self._config.DEBUG:
            pygame.display.set_caption(f"{self.TITLE} - {int(self._clock.get_fps())} fps")

    def game_loop(self) -> None:
        while self._running:
            self._handle_events()

            if self._game_started:
                self._render_game()
            else:
                self._menu.render()

            pygame.display.update()
            self._clock.tick(_FPS)

        pygame.quit()
