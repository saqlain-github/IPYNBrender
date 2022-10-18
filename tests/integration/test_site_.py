import pytest
from IPYNBrenderer.site import render_site
from IPYNBrenderer.custom_exception import InvalidURLException


class TestRenderSite:
    
    URL_test_good_data = [
        ("https://pytorch.org","success"),
        ("https://pytorch.org","success"),
    ]
    
    URL_test_bad_data = [
    ("https:/pytorch.org"),
    ("https://pytorch.or"),
    ]
        
    @pytest.mark.parametrize("URL,response",URL_test_good_data)
    def test_render_site_success(self, URL, response):
        assert render_site(URL) == response
        
    @pytest.mark.parametrize("URL",URL_test_bad_data)
    def test_render_site_failure(self, URL):
        with pytest.raises(InvalidURLException):
            render_site(URL)