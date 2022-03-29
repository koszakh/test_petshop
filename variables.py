import random

PETSHOP_URL = "https://petstore3.swagger.io/api/v3"
JSON_NAME = "pet.json"

CATEGORIES = {1: "Dogs", 2: "Cats", 3: "Parrots"}
PET_NAMES = {1: ["Sparkie", "Tucker", "Max"], 2: ["Oliver", "Garfield", "Felix"], 3: ["Polly", "Jackie", "Toby"]}

CATEGORY_ID = random.choice(list(CATEGORIES.keys()))
CATEGORY_NAME = CATEGORIES[CATEGORY_ID]
PET_ID = random.randint(1, 10000)
PET_NAME = random.choice(PET_NAMES[CATEGORY_ID])