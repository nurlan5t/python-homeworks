from bs4 import BeautifulSoup
import requests

response = requests.get('http://www.cinema.kg/')
response_text = response.text
html = BeautifulSoup(response_text, 'lxml')

trs = html.find('body').find('div', id="afishaContents").find_all('tbody')
movies = trs[2].find_all('tr', class_="tRow tooltips")

def get_movies():
    for movie in movies:
        movie = movie.find_all('td')[1].text
        print(movie)
get_movies()

