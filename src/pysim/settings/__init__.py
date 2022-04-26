from typing import Any
from .hierarchy import HierarchicalSettings
from .dictionary import DictionarySettings



_default_settings = DictionarySettings({
    'show_fps': False,
    'max_fps': 60,
})


_runtime_settings = DictionarySettings()


_settings = HierarchicalSettings([
    _runtime_settings,
    _default_settings,
])


def setting(key : str) -> Any:
    return _settings[key]


def set_setting(key : str, value : Any) -> None:
    _runtime_settings[key] = value
