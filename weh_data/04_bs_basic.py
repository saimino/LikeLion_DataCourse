from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"


page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''
page1 = page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
soup1 = BeautifulSoup(page1, 'lxml')
# print( soup1.title )

#

soup = BeautifulSoup(page, 'lxml')
# print(soup.title)
# print(soup.body)
# print(soup.div)
# print(soup.img)
# print(soup.a)
# print(soup.a.text)
# print(soup.div.a.text)


# ## find ; 특정 id,class 를 통해 가져오기
# ## find_all ; 모든 특정 태그 정보 가져오기
# print(soup.find("p", id = "p4"))
# print(soup.find_all('p'))
# print(soup.find("a", href = "https://www.naver.com/"))
# print(soup.find_all('a'))
# print(soup.div.find("p", id="p4"))
# # print(soup.find_all("p",class = "p3")  )

print(soup.find_all("a",href=True))
##################################################
print("\n\n\n")
soup1 = BeautifulSoup(page1, 'lxml')
# print( soup1.title )

one_info = soup1.find_all("div")
# print(len(one_info) )
# print()

wanted_info = soup1.find_all('div')[3]
print(wanted_info)
print()
last_info_multi = wanted_info.find_all('p', class_="p3")
print(last_info_multi)
print()
# #
# list1 = []
# f = open("info_test.csv", 'w')
# for one in last_info_multi:
#     # list1.append(one)
#     f.write(str(one.text))
#     print(one.text)

print(list(wanted_info.children)[-2])