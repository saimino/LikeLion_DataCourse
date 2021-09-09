from bs4 import BeautifulSoup
from urllib.request import urlopen

# url 정보
# tag, id, class 정보

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 제목 - 하나 성공
tit_data = soup.find("dt", class_="tit").find("a").text
print(tit_data)

# 제목 - 하나 성공
# tit_all_data = soup.find_all("dt", class_="tit")
#
# list_all = []
# for one in tit_all_data:
#     title_one = one.find("a").text
#     list_all.append(title_one)
# print(len(list_all), list_all)

## 평점 점수 가져오기
##
# score_all = soup.find_all("span", class_='num')
# print(score_all[1].text)


score_all = soup.find_all("div", class_='star_t1')
score_all_all =[]
for i in score_all:
    score_all_all.append(i.find("span",class_='num').text)

print(score_all_all)

# 예매율 정보 가져와보기
rate_tmp = soup.find_all("dl", class_='info_exp')
# print( score_all[2].find("span", class_='num').text )

rate_all_all = []
for one in rate_tmp:
    one_rate = one.find("span", class_='num').text
    # print(one_score)
    rate_all_all.append(one_rate)

print(rate_all_all)