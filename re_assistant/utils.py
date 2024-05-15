from http import HTTPStatus

import httpx
from loguru import logger


async def fetch_html_content(url, headers=None):
    async with httpx.AsyncClient(
        follow_redirects=True, timeout=None
    ) as client:
        response = await client.get(url, headers=headers)

    if response.status_code != HTTPStatus.OK:
        logger.error(f'Não foi possível fazer o fetch da url: {url}')
        return None

    return response.text
