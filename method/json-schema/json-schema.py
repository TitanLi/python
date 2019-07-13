from jsonschema import validate
schema = {
    "type": "object",
    "properties": {
        "price": {
            "type": "number"
        },
        "name": {
            "type": "string"
        },
    },
}

# 檢驗JSON Type
validate({"name": "Eggs", "price": 34.99}, schema)