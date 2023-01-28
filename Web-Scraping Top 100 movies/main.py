import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
names = soup.find_all(name="h3", class_="title")

movie_list = [item.getText() for item in names]
movie_list = movie_list[::-1]

with open("myFile.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")


    