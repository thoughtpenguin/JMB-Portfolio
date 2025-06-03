import requests
import pytest

BASE_URL = 'https://openlibrary.org'


class TestOpenLibrary:
    @pytest.fixture
    def request_bringing_the_shovel_down(self):
        params = {
           'title' : 'bringing the shovel down'
        }
        response = requests.get(BASE_URL+'/search.json', params)
        return response.json()
    
    def test_search_bringing_the_shovel_down(self, request_bringing_the_shovel_down):
       assert request_bringing_the_shovel_down['numFound'] == 1
       return
    def test_search_bringing_the_shovel_down_docs(self, request_bringing_the_shovel_down):
        assert len(request_bringing_the_shovel_down['docs']) == 1
        return
    
