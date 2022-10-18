import pytest 
from IPYNBrenderer.youtube import get_time_info
from IPYNBrenderer.custom_exception import InvalidURLException


good_URL_data = [
    ("https://www.youtube.com/watch?v=dOKQeqGNJwY",0),
    ("https://youtu.be/dOKQeqGNJwY",0),
    ("https://youtu.be/dOKQeqGNJwY?t=5",5)
]

bad_URL_data = [
    ("https://www.youtube.com/watch?v=dOKQeqGNJwYasd"),
    ("https://www.youtube.com/watch?v=dOKQeqGNJwY&t"),
    ("https://www.youtube.com/watch?v=dOKQeqGNJwY&t==22s"),
    ("https://www.youtube.com/watch?v==dOKQeqGNJwY&t=2s"),
]

@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response
    
@pytest.mark.parametrize("URL",bad_URL_data)
def test_get_time_info_false(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)