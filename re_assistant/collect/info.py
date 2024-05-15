from loguru import logger


def get_basic_info(soup):
    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )

    topics = page_content.find_all('p')[1].find_all('em')

    if not topics:
        logger.error('Não foi possível encontrar os tópicos dos personagens.')

    infos = {
        key.strip(): value.strip()
        for key, value in [topic.text.split(':') for topic in topics]
    }

    return infos


def get_titles_info(soup):
    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )
        return None

    items = page_content.find_all('li')

    titles = {'titles': [item.text for item in items]}

    return titles


def get_biography_info(soup):
    page_content = soup.find('div', class_='td-page-content')
    if not page_content:
        logger.error(
            "Não foi possível encontrar a div com a classe 'td-page-content'"
        )

        return None

    content = []
    for tag in page_content.find('h4').next_siblings:
        if tag.name == 'h4':
            break
        else:
            content.append(tag.text)

    return {'biography': r"\n".join(content)}
