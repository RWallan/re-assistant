"""Reune métodos úteis para diferentes partes do projeto."""
import pickle
from http import HTTPStatus
from pathlib import Path

import httpx
from loguru import logger


async def fetch_html_content(url, headers=None):
    """Executa um fetch em um html.

    Returns:
        str | None: Retorna o elemento html.
    """
    async with httpx.AsyncClient(
        follow_redirects=True, timeout=None
    ) as client:
        response = await client.get(url, headers=headers)

    if response.status_code != HTTPStatus.OK:
        logger.error(f'Não foi possível fazer o fetch da url: {url}')
        return None

    return response.text


def save_to_pickle(obj, path):
    """Salva um objeto em formato pickle."""
    _path = Path(path)
    with open(_path, 'wb') as file:
        pickle.dump(obj, file, -1)

    return str(_path)


def load_pickle(path):
    """Carrega um arquivo pickle em um objeto."""
    _path = Path(path)
    with open(_path, 'rb') as file:
        obj = pickle.load(file)

    return obj
