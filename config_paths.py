import sys
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

def get_eccang_paths():
    """Load and return ECCANG-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("ECCANG"))
    return {k: Path(v) for k, v in paths.items()}

def get_tp_paths():
    """Load and return TP-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("TP"))
    return {k: Path(v) for k, v in paths.items()}

def get_refresh_paths():
    """Load and return REFRESH-related paths from the config file."""
    paths = dict(config.items("Common"))
    paths.update(config.items("REFRESH"))
    return {k: Path(v) for k, v in paths.items()}
