from src.utils.helpers import resource_path

ROOT = "src"
ROOT_ASSETS = "src/assets"

# --- Audios ---

SOUND_MUSIC = resource_path(relative_path=f"{ROOT_ASSETS}/sounds/game_music.wav")

SOUND_PLAYER_JUMP = resource_path(relative_path=f"{ROOT_ASSETS}/sounds/player_jump.mp3")

# --- Fonts ---

FONT_PRIMARY = resource_path(relative_path=f"{ROOT_ASSETS}/fonts/Pixeltype.ttf")

# --- Graphics ---

GRAPHIC_SKY = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/sky.png")
GRAPHIC_GROUND = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/ground.png")

GRAPHIC_PLAYER_STAND = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/player_stand.png")
GRAPHIC_PLAYER_WALK_1 = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/player_walk_1.png")
GRAPHIC_PLAYER_WALK_2 = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/player_walk_2.png")
GRAPHIC_PLAYER_JUMP = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/player_jump.png")
