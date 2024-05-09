import pytest

from re_assistant.utils import fetch_html_content


@pytest.mark.asyncio()
async def test_fetch_html_content():
    content = await fetch_html_content('https://www.google.com.br')

    assert content is not None
    assert isinstance(content, str)
    assert '<!doctype html>' in content
