from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 코스피 정보 가져오기
kospi_info = soup.find("em", id="now_value")
print(kospi_info.text)

# 거래량 천주 정보 가져오기
deal_info = soup.find("td", id='quant')
print("거래량 : ", deal_info.text)

# 장중최고
max_info = soup.find("td", id='high_value')
print("장중최고 : ", max_info.text)

# 52주 최고
max52_info = soup.find("td")
print("52주최고 : ", max52_info.text)

tmp_index = soup.find("table", class_="table_kos_index")
tmp_52week = tmp_index.find_all("tr")[2].find("td")
print("52주 최고 : ", tmp_52week.text)

# 시황뉴스 - ul
tmp_news = soup.find("ul", class_="sise_report")
# print(len(tmp_news))
# print(tmp_news)


tmp_li_all = tmp_news.find_all("span", class_="tit")

news = []
for one in tmp_li_all:
    # print(one.text)
    news.append(one.text)


dat = pd.DataFrame( {"시황뉴스" : news})
print(dat)
dat.to_csv("news.csv")
dat.to_excel("news_excel.xlsx")

# print(news)