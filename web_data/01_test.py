from urllib.request import urlopen
from bs4 import BeautifulSoup

# 01. 우리가 가져올 url
# 02. 내가 원하는 정보의 위치(span, id)
# uel :
# tag : span , is , : KOSPIZ_now

# html 코드를 요청해서 가져온다.

url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)

#구체적인 html 확인하고 , 구조화하기
soup = BeautifulSoup(page, "html.parser")
KOSPI = soup.find("span", id ="KOSPI_now")
KOSPI200 = soup.find("span", id ="KPI200_now")
KOSDAQ = soup.find("span", id="KOSDAQ_now")

RANK = soup.find("ul", id="popularItemList")


print("코스피 현재 지수는: ", KOSPI.text)
print("코스피200 현재 지수는: ", KOSPI200.text)
print("코스닥 현재 지수는: ", KOSDAQ.text)

print("랭킹" , RANK.text) 

