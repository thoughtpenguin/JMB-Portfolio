import requests
import pytest
from helpers.APIHelper import LoadSchema, ValidateJsonWithSchema

#region Constants

BASE_URL = "https://whoa.onrender.com/whoas"
RANDOM_WHOA_RESPONSE_SCHEMA_NAME = "keanu_reeves_whoa_random_response"

#endregion

#region Fixtures

@pytest.fixture
def random_whoa():
    path = "/random"
    url = BASE_URL + path
    response = requests.get(url)
    return response.json()

@pytest.fixture
def random_whoa_response_schema():
    return LoadSchema(RANDOM_WHOA_RESPONSE_SCHEMA_NAME)

#endregion

#region Tests

class TestKeanuReevesWoah:
    def test_random_whoa(self, random_whoa, random_whoa_response_schema):
        assert random_whoa
        assert ValidateJsonWithSchema(random_whoa, random_whoa_response_schema)
        return

#endregion