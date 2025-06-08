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
DOC_EXPECTED_KEYS = {
    'author_key' : list,
    'author_name' : list,
    'ebook_access' : str,
    'edition_count' : int,
    'first_publish_year' : int,
    'has_fulltext' : bool,
    'key' : str,
    'language' : list,
    'public_scan_b' : bool,
    'title' : str
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
@pytest.fixture
def search_bringing_the_shovel_down_docs(search_bringing_the_shovel_down:dict):
    return search_bringing_the_shovel_down['docs']

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
            assert isinstance(search_bringing_the_shovel_down[key], SEARCH_EXPECTED_KEYS[key])
        return
    def test_search_result_doc_fields(self, search_bringing_the_shovel_down_docs:list[dict]):
        #Confirm each doc has expected fields
        for doc in search_bringing_the_shovel_down_docs:
            docKeys = doc.keys()
            for key in DOC_EXPECTED_KEYS:
                assert key in docKeys
    def test_search_result_doc_field_types(self, search_bringing_the_shovel_down_docs:list[dict]):
        #Confirm each field in each doc is of the expected type.
        for doc in search_bringing_the_shovel_down_docs:
            for key in doc:
                type = DOC_EXPECTED_KEYS[key]
                assert isinstance(doc[key], type)
        return


