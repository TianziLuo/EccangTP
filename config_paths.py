import sys
from pathlib import Path
import configparser

if getattr(sys, "frozen", False):  # exe 打包环境
    _base_path = Path(sys.executable).parent
else:  # 开发环境
    _base_path = Path(__file__).parent

_config_path = _base_path / "dv_config.ini"

config = configparser.ConfigParser()
config.optionxform = str  # 保持 key 原样
read_files = config.read(_config_path, encoding="utf-8")

if not read_files:
    raise FileNotFoundError(f"找不到配置文件: {_config_path}")

def get_eccang_paths():
    paths = dict(config.items("Common"))
    paths.update(config.items("ECCANG"))
    return {k: Path(v) for k, v in paths.items()}

def get_tp_paths():
    paths = dict(config.items("Common"))
    paths.update(config.items("TP"))
    return {k: Path(v) for k, v in paths.items()}

def get_refresh_paths():
    paths = dict(config.items("Common"))
    paths.update(config.items("REFRESH"))
    return {k: Path(v) for k, v in paths.items()}
