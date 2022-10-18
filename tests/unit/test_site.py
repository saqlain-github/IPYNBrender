import pytest
from IPYNBrenderer.site import is_valid

URL_test_data = [
    ("https://pytorch.org",True),
    ("https:/pytorch.org",False),
    ("https://pytorch.or",False),
    ("https://pytorch.org",True),
]

@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid(URL,response):
    assert is_valid(URL) == response