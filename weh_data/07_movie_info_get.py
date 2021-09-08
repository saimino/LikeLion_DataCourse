from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

list_movie_all = []
tit_data_all = soup.find_all('dt', class_='tit')
for i in tit_data_all:
    one = i.find("a").text
    list_movie_all.append(one)
print(list_movie_all)


#평점

score_one