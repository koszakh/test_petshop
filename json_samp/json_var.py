import json

petId = 123
petName = "Dog123"
categoryId = 1
categoryName = "Dogs"

dct = {
  "id": petId,
  "name": petName,
  "category": {
    "id": categoryId,
    "name": categoryName
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

json_str = json.dumps(dct, indent=True)
print(json_str, type(json_str))