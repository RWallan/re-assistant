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

    def strip_not_em_pattern(content):
        return (
            content.replace(r'</em>', '')
            .replace('<em>', '')
            .split('<br/>')[:-1]
        )

    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )
        return {}

    topics = page_content.find_all('p')[1].find_all('em')

    if not topics:
        topics = str(page_content.find_all('p')[1])
        topics = strip_not_em_pattern(topics)
        infos = {
            key: value for key, value in [topic.split(':') for topic in topics]
        }
    elif len(topics) == 1:
        topics = (
            str(topics[0])
            .replace(r'</em>', '')
            .replace('<em>', '')
            .split('<br/>')[:-1]
        )

        infos = {
            key: value for key, value in [topic.split(':') for topic in topics]
        }
    else:
        infos = {
            key.strip(): value.strip()
            for key, value in [topic.text.split(':') for topic in topics]
        }

    if not infos:
        logger.error('Não foi possível buscar os itens do personagem.')

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
    """Aplica o pipeline para buscar todas as informações do peronsagem.

    Returns:
        dict: Dados do personagem contendo: perfil, titulos, biografia.
    """

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
    char_name = url.strip('/').split('/')[-1].replace('-', ' ').title()
    data = {
        'link': url,
        'name': char_name,
    }

    logger.info(f'Buscando informações do personagem: {char_name}')
    data.update(get_basic_info(soup))
    data.update(get_titles_info(soup))
    data.update(get_biography_info(soup))

    return data
