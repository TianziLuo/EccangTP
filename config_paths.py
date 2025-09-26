import sys
import os
from pathlib import Path
import configparser

# Determine the base path depending on the runtime environment
if getattr(sys, "frozen", False):  # Running in packaged .exe environment
    _base_path = Path(sys.executable).parent
else:  # Running in development environment
    _base_path = Path(__file__).parent

# Path to the configuration file
_config_path = _base_path / "ET_config.ini"

config = configparser.ConfigParser()
config.optionxform = str  # Preserve the original case of keys
read_files = config.read(_config_path, encoding="utf-8")

if not read_files:
    raise FileNotFoundError(f"Configuration file not found: {_config_path}")


def _expand_and_default(section_dict: dict) -> dict:
    """Expand ~ in paths and apply defaults if needed."""
    result = {}
    for k, v in section_dict.items():
        expanded = os.path.expanduser(v)
        result[k] = Path(expanded).resolve()

    # 如果没写 downloads，就补上默认的 ~/Downloads
    if "downloads" not in result:
        home = Path.home()
        result["downloads"] = (home / "Downloads").resolve()

    return result


def get_eccang_paths():
    """Load and return ECCANG-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("ECCANG"))
    return _expand_and_default(paths)


def get_tp_paths():
    """Load and return TP-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("TP"))
    return _expand_and_default(paths)


def get_refresh_paths():
    """Load and return REFRESH-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("REFRESH"))
    return _expand_and_default(paths)


def get_diary_paths():
    """Load and return DIARY-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("DIARY"))
    return _expand_and_default(paths)