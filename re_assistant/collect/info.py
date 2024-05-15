"""
Busca informações relacionadas aos personagens do Resident Evil.

As informações contemplam:

- Perfil
- Títulos que participou
- Biografia
"""

from bs4 import BeautifulSoup
from loguru import logger

from re_assistant.collect.config import settings
from re_assistant.utils import fetch_html_content


def get_basic_info(soup):
    """Busca informações de perfil do personagem.

    Returns:
        dict: Informações de perfil.
    """
    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )
        return {}

    topics = page_content.find_all('p')[1].find_all('em')

    if not topics:
        logger.error('Não foi possível encontrar os tópicos dos personagens.')

    infos = {
        key.strip(): value.strip()
        for key, value in [topic.text.split(':') for topic in topics]
    }

    return infos


def get_titles_info(soup):
    """Busca quais os titulos das séries o personagem participou.

    Returns:
        dict: Séries que o personagem participou.
    """
    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )
        return {}

    items = page_content.find_all('li')

    titles = {'titles': [item.text for item in items]}

    return titles


def get_biography_info(soup):
    """Busca a biografia o personagem.

    Returns:
        dict: Biografia do personagem.

    """
    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )

        return {}

    content = []
    for tag in page_content.find('h4').next_siblings:
        if tag.name == 'h4':
            break
        else:
            content.append(tag.text)

    return {'biography': r'\n'.join(content)}


async def get_char_infos(url):
    headers = {
        key.replace('_', '-'): value
        for key, value in settings.headers.model_dump().items()
    }
    html_content = await fetch_html_content(url, headers)
    if not html_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    data = {
        'link': url,
        'name': url.strip('/').split('/')[-1].replace('-', '').title(),
    }

    data.update(get_basic_info(soup))
    data.update(get_titles_info(soup))
    data.update(get_biography_info(soup))

    return data
