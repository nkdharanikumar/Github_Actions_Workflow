import pytest
from app import TinyURL

@pytest.fixture
def tiny():
    return TinyURL()

def test_shorten_url(tiny):
    code = tiny.shorten_url("https://google.com")
    assert len(code) == 6

def test_retrieve_url(tiny):
    code = tiny.shorten_url("https://google.com")
    assert tiny.get_original_url(code) == "https://google.com"

def test_invalid_code(tiny):
    assert tiny.get_original_url("abc123") is None

def test_delete_url(tiny):
    code = tiny.shorten_url("https://google.com")
    assert tiny.delete_url(code) is True

def test_delete_invalid_url(tiny):
    assert tiny.delete_url("wrong") is False

def test_count_after_insert(tiny):
    tiny.shorten_url("https://google.com")
    assert tiny.total_urls() == 1

def test_count_after_multiple_insert(tiny):
    tiny.shorten_url("https://google.com")
    tiny.shorten_url("https://github.com")
    assert tiny.total_urls() == 2

def test_count_after_delete(tiny):
    code = tiny.shorten_url("https://google.com")
    tiny.delete_url(code)
    assert tiny.total_urls() == 0

def test_unique_codes(tiny):
    code1 = tiny.shorten_url("https://google.com")
    code2 = tiny.shorten_url("https://github.com")
    assert code1 != code2

def test_code_length(tiny):
    code = tiny.shorten_url("https://google.com")
    assert len(code) == 6