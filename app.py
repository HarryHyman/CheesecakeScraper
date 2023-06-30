import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.janespatisserie.com/2019/05/30/no-bake-lemon-cheesecake/").text

soup = BeautifulSoup(site, "html.parser")

recipe = soup.find(class_="wprm-recipe")

recipe_text = recipe.get_text(separator="")

print(recipe_text)
