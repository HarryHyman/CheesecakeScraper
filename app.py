import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.janespatisserie.com/2019/05/30/no-bake-lemon-cheesecake/").text

soup = BeautifulSoup(site, "html.parser")

# recipe = soup.find(class_="wprm-recipe")
# recipe_text = recipe.get_text(separator="")

ingredients = soup.find(class_="wprm-recipe-ingredients-container")
ingredients_text = ingredients.get_text(separator="")

instructions = soup.find(class_="wprm-recipe-instructions-container")
instructions_text = instructions.get_text(separator="\n")

notes = soup.find(class_="wprm-recipe-notes-container")
notes_text = notes.get_text(separator="")

print("*** INGREDIENTS ***")
print(ingredients_text)

print("*** INSTRUCTIONS ***")
print(instructions_text)

print("*** NOTES ***")
print(notes_text)
