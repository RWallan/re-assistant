import pytest
from bs4 import BeautifulSoup

from re_assistant.collect.config import settings
from re_assistant.collect.info import (
    get_basic_info,
    get_biography_info,
    get_titles_info,
)
from re_assistant.utils import fetch_html_content


@pytest.mark.asyncio()
async def test_basic_info():
    expected = {
        'Ano de nascimento': '1974 (24 anos em 1998)',
        'Tipo sanguíneo': 'AB',
        'Altura': 'Desconhecida.',
        'Peso': 'Desconhecido.',
    }

    headers = {
        key.replace('_', '-'): value
        for key, value in settings.headers.model_dump().items()
    }

    html_content = await fetch_html_content(
        'https://www.residentevildatabase.com/personagens/ada-wong/', headers
    )
    if not html_content:
        raise Exception('Conteúdo não encontrado')

    soup = BeautifulSoup(html_content, 'html.parser')

    infos = get_basic_info(soup)

    assert infos == expected


@pytest.mark.asyncio()
async def test_titles_info():
    expected = {
        'titles': [
            'Biohazard / Resident Evil 2 (1998)',
            'Biohazard / Resident Evil 4 (2005)',
            'Biohazard / Resident Evil: The Umbrella Chronicles (2007)',
            'Biohazard / Resident Evil: The Darkside Chronicles (2009)',
            'Biohazard / Resident Evil: Operation Raccoon City (2012)',
            'Biohazard / Resident Evil: Damnation (2012)',
            'Biohazard / Resident Evil 6 (2012)',
            'Biohazard RE:2 / Resident Evil 2 (2019)',
            'Biohazard RE:4 / Resident Evil 4 (2023)',
        ]
    }

    headers = {
        key.replace('_', '-'): value
        for key, value in settings.headers.model_dump().items()
    }

    html_content = await fetch_html_content(
        'https://www.residentevildatabase.com/personagens/ada-wong/', headers
    )
    if not html_content:
        raise Exception('Conteúdo não encontrado')

    soup = BeautifulSoup(html_content, 'html.parser')

    infos = get_titles_info(soup)

    assert infos == expected


def test_get_biography():
    html = (
        "<div class = 'td-page-content'><h4>Title 1</h4><p>paragraph</p>"
        '<p>paragraph with <a href="https://google.com.br">link</a></p>'
        '<p>another paragraph</p><h4>Title 2</h4><p>paragraph 2</p></div>'
    )

    expected = {
        'biography': r'paragraph\nparagraph with link\nanother paragraph'
    }

    soup = BeautifulSoup(html, 'html.parser')

    bio = get_biography_info(soup)

    assert bio == expected
