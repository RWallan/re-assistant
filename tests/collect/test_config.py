from pathlib import Path

import toml

from re_assistant.collect.config import Settings

ROOT = Path(__file__).parent.parent.parent


def test_settings():
    print(ROOT)
    with open(
        ROOT / 're_assistant' / 'collect' / 'config.toml',
        'r',
        encoding='utf-8',
    ) as file:
        expected = toml.load(file)

    settings = Settings().model_dump()  # pyright: ignore

    assert settings == expected
