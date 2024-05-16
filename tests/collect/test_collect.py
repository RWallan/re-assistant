from pathlib import Path

import pytest

from re_assistant.collect import create_char_database


@pytest.mark.asyncio()
async def test_create_char_database_without_catalog():
    database_file = await create_char_database()

    assert Path(database_file).exists()
