import pytest
from IPYNBrenderer.youtube import render_Youtube_video
from IPYNBrenderer.custom_exception import InvalidURLException


class TestYTvideoRenderer:

    URL_test_good_data = [
        ("https://www.youtube.com/watch?v=dOKQeqGNJwY", 0),
        ("https://youtu.be/dOKQeqGNJwY", 0),
        ("https://youtu.be/dOKQeqGNJwY?t=5", 5),
    ]

    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=dOKQeqGNJwYasd"),
        ("https://www.youtube.com/watch?v=dOKQeqGNJwY&t"),
        ("https://www.youtube.com/watch?v=dOKQeqGNJwY&t==22s"),
        ("https://www.youtube.com/watch?v==dOKQeqGNJwY&t=2s"),
    ]
    
    @pytest.mark.parametrize("URL,response",URL_test_good_data)
    def test_render_YT_success(self,URL,response):
        assert render_Youtube_video(URL) == "success"
        
    @pytest.mark.parametrize("URL",URL_test_bad_data)
    def test_render_YT_failure(self,URL):
        with pytest.raises(InvalidURLException):
            render_Youtube_video(URL)
