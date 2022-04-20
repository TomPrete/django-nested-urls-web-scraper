import requests as req
from bs4 import BeautifulSoup

for i in range(1,10):
    response = req.get(f'http://localhost:8000/movies/{i}')
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        movie = soup.find('h2').text
        print(movie)
    else:
        print('Resource not found')
