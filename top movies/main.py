import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name='h3',class_="title")
movie = []
for mov in movies:
    movie.insert(0,mov.text)



with open(file='movies.txt',mode='w',encoding='utf-8') as file:
    for each_movie in movie:
        file.write(f"{each_movie}\n")