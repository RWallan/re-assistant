import pytest

from re_assistant.utils import fetch_html_content, load_pickle, save_to_pickle


@pytest.mark.asyncio()
async def test_fetch_html_content():
    content = await fetch_html_content('https://www.google.com.br')

    assert content is not None
    assert isinstance(content, str)
    assert '<!doctype html>' in content


def test_save_obj_to_pickle(tmp_path):
    d = tmp_path

    obj = {1: 'a', 2: 'b'}

    path = save_to_pickle(obj, path=d / 'test_obj.pkl')

    assert len(list(tmp_path.iterdir())) == 1
    assert path == str(d / 'test_obj.pkl')


def test_load_pkl_obj(tmp_path):
    d = tmp_path

    obj = {1: 'a', 2: 'b'}

    _ = save_to_pickle(obj, path=d / 'test_obj.pkl')
    result = load_pickle(path=d / 'test_obj.pkl')

    assert result == obj
