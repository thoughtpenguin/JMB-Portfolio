import requests
import pytest

BASE_URL = 'https://openlibrary.org'
SEARCH_URL = BASE_URL + '/search.json'
SEARCH_EXPECTED_KEYS = {
    'numFound' : int,
    'start' : int,
    'numFoundExact' : bool,
    'num_found' : int,
    'documentation_url' : str,
    'q' : str,
    'docs' : list
}

@pytest.fixture
def search_bringing_the_shovel_down():
    params = {
        'title' : 'bringing the shovel down'
    
    }
    response = requests.get(SEARCH_URL, params)
    return response.json()
@pytest.fixture
def search_ross_gay():
    params = {
        'author' : 'Ross Gay'
    }
    response = requests.get(SEARCH_URL, params)
    return response.json()

class TestOpenLibrary:
    
    def test_search_result_fields(self, search_bringing_the_shovel_down:dict):
       # Confirm return object has expected fields.
       responseKeys = search_bringing_the_shovel_down.keys()
       expectedResultKeys = SEARCH_EXPECTED_KEYS.keys()
       for key in expectedResultKeys:
           assert key in responseKeys
       return
    def test_search_result_field_types(self, search_bringing_the_shovel_down:dict):
        # Confirm return object fields have expected types.
        expectedResultKeys = SEARCH_EXPECTED_KEYS.keys()
        for key in expectedResultKeys:
            assert type(search_bringing_the_shovel_down[key]) == SEARCH_EXPECTED_KEYS[key]
        return
    
