import os
import json
from jsonschema import validate, ValidationError

def LoadSchema(schemaName):
    cwd = os.getcwd()
    path = os.path.join(cwd, "APITests", "schemas", schemaName+ ".json")
    with open(path, "r") as file:
        schema = json.load(file)
    return schema
def ValidateJsonWithSchema(json, schema):
    try:
        validate(instance=json, schema=schema)
        return True
    except ValidationError as e:
        print(e)
        return False
    return False