import requests
import pytest
from helpers.APIHelper import LoadSchema, ValidateJsonWithSchema

#region Constants

BASE_URL = "https://whoa.onrender.com/whoas"
ORDERED_URL = BASE_URL + "/ordered"
RANDOM_URL = BASE_URL + "/random"

RANDOM_WHOA_RESPONSE_SCHEMA_NAME = "keanu_reeves_whoa_random_response"

#endregion

#region Fixtures

@pytest.fixture
def random_whoa():
    response = requests.get(RANDOM_URL)
    return response.json()

@pytest.fixture
def five_random_whoas():
    query = { "results" : 5 }
    response = requests.get(RANDOM_URL, params=query)
    return response.json()

@pytest.fixture
def all_movies():
    path = "/movies"
    url = BASE_URL + path
    response = requests.get(url)
    return response.json()

@pytest.fixture
def random_whoa_response_schema():
    return LoadSchema(RANDOM_WHOA_RESPONSE_SCHEMA_NAME)

#endregion

def getWhoaByIndex(index:int):
    response = requests.get(ORDERED_URL + "/" + str(index))
    return response.json()
def getRandomWhoaFiltered(query):
    response = requests.get(RANDOM_URL, params=query)
    return response.json()

#region Tests

class TestKeanuReevesWhoa:
    def test_random_whoa(self, random_whoa, random_whoa_response_schema):
        assert random_whoa
        assert ValidateJsonWithSchema(random_whoa, random_whoa_response_schema)
        return
    def test_five_random_whoas(self, five_random_whoas, random_whoa_response_schema):
        assert five_random_whoas
        assert ValidateJsonWithSchema(five_random_whoas, random_whoa_response_schema)
        return
    def test_whoa_retrieval(self, random_whoa:dict, all_movies, random_whoa_response_schema):
        assert random_whoa
        assert all_movies
        targetMovie = random_whoa[0]["movie"]
        whoaIndex = random_whoa[0]["current_whoa_in_movie"]-1
        for movie in all_movies:
            if movie == targetMovie:
                break
            # Avoid double adding by skipping director's cut movies (they count as the same movie as the original).
            if "(The Director's Cut)" in movie:
                continue
            response = getRandomWhoaFiltered({ "movie" : movie })
            whoaIndex += response[0]["total_whoas_in_movie"]
        ordered_whoa = getWhoaByIndex(whoaIndex)
        assert ordered_whoa == random_whoa[0]
        return

#endregion