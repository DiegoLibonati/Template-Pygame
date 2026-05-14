# Python Pygame Boilerplate

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Python Pygame Boilerplate** is a starting point for building games with Pygame.

Solves the problem of repeating the same setup and architecture decisions every time a new game project is started: environment config, logging, asset path resolution, build pipeline, and test infrastructure are already in place.

What it includes:

- **Pygame** — game loop, sprite system, input, audio, and rendering
- **Environment-based config** — `DefaultConfig` hierarchy with `development`, `production`, and `testing` variants selected via `ENVIRONMENT` env var
- **Structured logging** — `setup_logger()` ready to use across any module
- **Asset path resolution** — `resource_path()` works both in development and inside a PyInstaller bundle
- **PyInstaller build** — `app.spec` bundles `src/assets/` and `.env` into a standalone executable
- **Ruff** — linting and formatting with pre-commit integration
- **pytest** — configured with markers, `pytest-env`, coverage, and headless Pygame support

How to use it:

1. Clone the repository
2. Replace the game logic inside `src/features/`, `src/game.py`, and `src/assets/` with your own
3. Update `ENV_NAME` and the project name in `pyproject.toml`
4. Keep the config, logging, utils, and build setup as-is or extend them as needed

## Technologies used

1. Python >= 3.11

## Libraries used

The dependencies are declared in `pyproject.toml` and split across four groups, one per workflow (runtime, development, testing, build), so each environment installs only what it needs. The `requirements*.txt` files are thin wrappers that delegate to those groups via `-e .[group]`.

#### Runtime (`[project.dependencies]`)

```
pygame==2.6.1
python-dotenv==1.2.2
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`[project.optional-dependencies]` build)

```
pyinstaller==6.16.0
```

## Getting Started

With Python 3.11+ installed, follow these steps to set up the project locally and launch the game.

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .`
6. Execute: `pip install -e ".[dev]"`
7. Execute: `pip install -e ".[test]"`
8. Copy the example env file so the app can load its configuration:
   - Windows: `copy .env.example.dev .env`
   - Linux/Mac: `cp .env.example.dev .env`
9. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

If you plan to contribute or extend the project, install the pre-commit hooks so linting and formatting run automatically on every commit.

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The project loads environment variables from a `.env` file at the repository root. Use `.env.example.dev` as a base for development and `.env.example.prod` as a base for production.

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.
2. `ENV_NAME`: A custom environment variable for template demonstration purposes.

```
ENVIRONMENT=development
ENV_NAME=template_value
```

## Project Structure

Now that the project is installed and configured, here is how the codebase is organized. The layout follows a **feature-based architecture**, with `src/` holding all application code and `tests/` mirroring its structure.

```
python-pygame-boilerplate/
├── src/
│   ├── features/
│   │   ├── player/
│   │   │   ├── __init__.py
│   │   │   └── model.py
│   │   └── menu/
│   │       ├── __init__.py
│   │       └── view.py
│   ├── configs/
│   │   ├── __init__.py
│   │   ├── default_config.py
│   │   ├── development_config.py
│   │   ├── production_config.py
│   │   ├── testing_config.py
│   │   └── logger_config.py
│   ├── constants/
│   │   ├── __init__.py
│   │   ├── game.py
│   │   └── paths.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── assets/
│   │   ├── fonts/
│   │   ├── graphics/
│   │   └── sounds/
│   ├── __init__.py
│   ├── __main__.py
│   └── game.py
├── tests/
│   ├── test_features/
│   │   ├── test_player/
│   │   │   ├── __init__.py
│   │   │   └── test_model.py
│   │   └── test_menu/
│   │       ├── __init__.py
│   │       └── test_view.py
│   ├── test_configs/
│   │   ├── __init__.py
│   │   ├── test_default_config.py
│   │   ├── test_development_config.py
│   │   ├── test_logger_config.py
│   │   ├── test_production_config.py
│   │   └── test_testing_config.py
│   ├── test_constants/
│   │   ├── __init__.py
│   │   └── test_paths.py
│   ├── test_utils/
│   │   ├── __init__.py
│   │   └── test_helpers.py
│   ├── __init__.py
│   ├── conftest.py
│   └── test_game.py
├── app.py
├── pyproject.toml
├── requirements.txt
├── requirements.dev.txt
├── requirements.test.txt
├── requirements.build.txt
├── app.spec
├── build.bat
├── build.sh
├── .env
├── .env.example.dev
├── .env.example.prod
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── LICENSE
└── README.md
```

1. `src` -> Root directory of the source code. Contains the full application logic following a **feature-based architecture** pattern.
2. `features` -> Each subfolder is a self-contained feature. `player/` holds the sprite model; `menu/` holds the intro screen view. Add new features here (e.g. `enemy/`, `hud/`).
3. `configs` -> Contains all **configuration classes** organized by environment (development, production, testing). Includes logging setup and application settings.
4. `constants` -> Holds **static values**: world geometry (`game.py`) and asset paths (`paths.py`), centralized for use across the entire application.
5. `utils` -> Contains **shared utilities**. `helpers.py` provides `resource_path()` to resolve asset paths both in development and inside a PyInstaller bundle.
6. `assets` -> Static game files: **graphics** (sprites, backgrounds), **sounds** (music, effects), and **fonts**.
7. `game.py` -> The **main game orchestrator**. Handles the game loop, event processing, and delegates rendering to the appropriate feature (menu or gameplay).
8. `tests/` -> Contains **tests** organized to mirror the `src/` structure.
9. `conftest.py` -> Defines **pytest fixtures** for application setup and tests data.
10. `app.py` -> The **application entry point**. Loads the environment, selects the config class, and launches the game.
11. `pyproject.toml` -> **Unified project configuration** for pytest, ruff, and project metadata.
12. `requirements.txt` -> Thin wrapper — installs the package with its **runtime dependencies** via `-e .`.
13. `requirements.dev.txt` -> Thin wrapper — installs the **dev extras** via `-e .[dev]`.
14. `requirements.test.txt` -> Thin wrapper — installs the **test extras** via `-e .[test]`.
15. `requirements.build.txt` -> Thin wrapper — installs the **build extras** via `-e .[build]`.
16. `app.spec` -> **PyInstaller configuration** for generating standalone executables. Bundles `src/assets/` and `.env.example.prod` into the binary.
17. `.python-version` -> Declares the **minimum Python version** (`3.11`) for pyenv and compatible tooling (e.g. `uv`) to auto-select the correct interpreter.

## Architecture & Design Patterns

The structure above is shaped by a few deliberate design decisions. This section explains the layering and the patterns used inside each layer.

### Feature-based Architecture

The project follows a **feature-based architecture** where each game concept lives in its own folder under `src/features/`. Shared infrastructure (configs, constants, utils) stays at the `src/` level. The main orchestrator (`src/game.py`) wires features together and owns the game loop.

```
┌─────────────────────────────┐
│         Entry Point         │  app.py
├─────────────────────────────┤
│       Game Orchestrator     │  src/game.py
├──────────────┬──────────────┤
│   feature/   │   feature/   │  src/features/player/  src/features/menu/
│    player    │     menu     │  (add more features here)
├──────────────┴──────────────┤
│     Configs / Constants     │  src/configs/  src/constants/
├─────────────────────────────┤
│           Utils             │  src/utils/
└─────────────────────────────┘
```

---

### Design Patterns Used

#### 1. Environment-based Configuration (Strategy Pattern)
Configuration is selected at runtime based on the `ENVIRONMENT` variable. All config classes inherit from `DefaultConfig`, and `app.py` uses a `CONFIG_MAP` dictionary to pick the right class without conditionals.

```python
# app.py
CONFIG_MAP = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
config = CONFIG_MAP.get(environment, ProductionConfig)()
```

This makes it trivial to add a new environment by defining a new class and registering it in the map.

---

#### 2. Game Loop Pattern
`Game` implements the standard **game loop**: process input → update state → render → repeat at a fixed frame rate. The loop is split into focused private methods to keep each responsibility isolated. Rendering is delegated to the appropriate feature.

```python
def game_loop(self) -> None:
    while self._running:
        self._handle_events()   # input
        if self._game_started:
            self._render_game() # update + render (player feature)
        else:
            self._menu.render() # render (menu feature)
        pygame.display.update()
        self._clock.tick(_FPS)
```

---

#### 3. Sprite Pattern (Pygame)
Game entities extend `pygame.sprite.Sprite` and are managed through **sprite groups** (`GroupSingle`, `Group`). The group handles drawing and updating all sprites with a single call, decoupling the game loop from individual entity logic.

```python
self._player_single_group.draw(surface=self._screen)
self._player_single_group.update()
```

---

#### 4. Template Method Pattern
`PlayerModel.update()` defines a fixed sequence of steps, each delegated to a private method. Subclasses or future entities can override individual steps without altering the overall update order.

```python
def update(self) -> None:
    keys = pygame.key.get_pressed()
    self._input(keys)
    self._apply_gravity()
    self._animate(keys)
    self._clamp_position()
```

---

#### 5. State Machine (Intro / In-Game)
`Game` uses a simple boolean state (`_game_started`) to switch between the two game states. Each state delegates rendering to its feature (`MenuView` or the player group), making it straightforward to add new states (e.g., pause, game over) in the future.

---

#### 6. Centralized Asset Paths (Constants Module)
All file paths are defined once in `src/constants/paths.py` using `resource_path()`, which resolves them correctly both during development and inside a PyInstaller bundle. No path string is ever duplicated across the codebase.

```python
# src/constants/paths.py
GRAPHIC_PLAYER_WALK_1 = resource_path("src/assets/graphics/player_walk_1.png")
```

## Testing

With the codebase understood, you can run the test suite at any time to validate changes. Tests live under `tests/` and mirror the `src/` layout.

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .`
6. Execute: `pip install -e ".[test]"`
7. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Beyond running tests, you should also check the runtime dependencies for known vulnerabilities using **pip-audit** before shipping any release.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e ".[dev]"`
4. Execute: `pip-audit -r requirements.txt`

## Build

Once tests pass and dependencies are clean, you can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Production

For a desktop game built with Pygame, "production" means generating a standalone executable that end users can run without Python installed. The checklist below ties together the previous sections (Testing, Security Audit, Build) into a single release flow.

### Checklist

1. **Configure the production environment** — copy `.env.example.prod` to `.env` and set `ENVIRONMENT=production`

```bash
cp .env.example.prod .env
```

2. **Run the [security audit](#security-audit)** — check dependencies for known vulnerabilities

```bash
pip install -e ".[dev]"
pip-audit -r requirements.txt
```

3. **Run the [test suite](#testing)** — make sure nothing is broken before building

```bash
pip install -e ".[test]"
pytest
```

4. **[Build](#build) the executable** — generates a standalone binary in `dist/`

```bash
pip install -e ".[build]"

# Windows
build.bat          # or: pyinstaller app.spec

# Linux / Mac
./build.sh         # or: pyinstaller app.spec
```

5. **Distribute** — the output inside `dist/` is self-contained. Assets and `.env` are bundled into the executable by `app.spec`, so no extra files are needed.

> Runtime configuration should come from OS environment variables, not from a baked-in `.env`; the bundled `.env` (sourced from `.env.example.prod`) only ships safe defaults.

> There is no server, Docker, or reverse proxy involved — a Pygame game is a desktop application, not a web service.

## Known Issues

None at the moment.

## Portfolio link

[`https://www.diegolibonati.com.ar/#/project/python-pygame-boilerplate`](https://www.diegolibonati.com.ar/#/project/python-pygame-boilerplate)
