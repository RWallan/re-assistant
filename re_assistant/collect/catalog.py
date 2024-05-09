from bs4 import BeautifulSoup
from loguru import logger

from re_assistant.collect.config import settings
from re_assistant.utils import fetch_html_content


async def get_catalog():
    headers = {
        key.replace('_', '-'): value
        for key, value in settings.headers.model_dump().items()
    }

    content = await fetch_html_content(settings.catalog_url, headers)
    if not content:
        return None

    soup = BeautifulSoup(content, 'html.parser')

    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )
        return None

    links = page_content.find_all('a')  # pyright: ignore

    return [link['href'] for link in links]
