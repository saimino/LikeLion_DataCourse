from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

list=list(soup.find("table", class_="list_netizen").find("td",class_="title").children)
# comment=list[6].replace("\n","")
# comment=comment.replace("\t","") / 공백없애기는 여러가지 방법이있는데
# comment=comment.replace('\r','').replace('\t','').replace('\n', '') / 한번에 replace
comment = list[6].strip() # strip으로 공백만 다없애기
print(comment)