import variables as var

petId = var.PET_ID#123
petName = var.PET_NAME#"Dog123"
categoryId = var.CATEGORY_ID#1
categoryName = var.CATEGORY_NAME#"Dogs"

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