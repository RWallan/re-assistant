import pytest

from re_assistant.collect.catalog import get_catalog


@pytest.mark.asyncio()
async def test_get_catalog():
    catalog = await get_catalog()

    assert catalog is not None
    assert len(catalog) > 0
