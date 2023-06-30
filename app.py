import requests
from bs4 import BeautifulSoup

site = requests.get("https://www.janespatisserie.com/2019/05/30/no-bake-lemon-cheesecake/").text

soup = BeautifulSoup(html_content, "html.parser")

recipe = soup.find(class="wprm-recipe")

print(recipe)
