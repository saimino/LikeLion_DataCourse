from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

print(soup.title)

soup_ul_li = soup.find("ul", class_='lst_detail_t1').find_all("li")
print( len(soup_ul_li) )

### 상영작/예정작 제목만 뽑기
soup_ul_li = soup.find("ul", class_='lst_detail_t1').find_all("li")
print( len(soup_ul_li) )
# print( soup_ul_li[122].find("dt", class_="tit").a.text )

### 평점
print( "평점",soup_ul_li[4].find("span", class_="num").text )

### 참여명수
print( "참여명수",soup_ul_li[122].find("em").text )

### 예매율
# print( soup_ul_li[122].find("dl", class_="info_exp").span.text )

## 개요
txt = soup_ul_li[0].find("span", class_="link_txt").text
txt_last = txt.replace("\n", "")
txt_last = txt_last.replace("\t", "")
txt_last = txt_last.replace("\r", "")
print( txt_last )
print( len(txt_last))
dat_dict = {

}