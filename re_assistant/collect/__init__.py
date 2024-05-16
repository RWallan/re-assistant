import asyncio
from pathlib import Path

from loguru import logger
from tqdm import tqdm

from re_assistant.utils import load_pickle, save_to_pickle

from .catalog import get_catalog
from .info import get_char_infos

ROOT = Path(__file__).cwd()


@logger.catch()
async def create_char_database():
    database_dir = ROOT / 'data/database'
    database_dir.mkdir(parents=True, exist_ok=True)

    _catalog_file = database_dir / 're_assistant_catalog.pkl'
    if not _catalog_file.exists():
        logger.info('Buscando catálogo...')
        catalog = await get_catalog()
        catalog_file = save_to_pickle(catalog, _catalog_file)
        logger.info(f'Catálogo salvo em {catalog_file}')
    else:
        catalog = load_pickle(_catalog_file)

    tasks = [get_char_infos(url) for url in catalog]  # pyright: ignore

    data = [
        await task
        for task in tqdm(
            asyncio.as_completed(tasks),
            desc='Processando tarefas concluídas',
            total=len(tasks),
        )
    ]

    logger.info(f'Tasks completas: {len(tasks)}.')
    database_file = save_to_pickle(
        data, database_dir / 're_assistant_data.pkl'
    )

    return database_file
