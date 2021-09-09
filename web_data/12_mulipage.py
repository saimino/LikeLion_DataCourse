from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

## 1~5페이지 가져오기
## 댓글 1페이지의 댓글 전체 가져오기-10개
url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=19079&target='

full_comment = []
for i in range(1, 50, 1):
    page_url = url + f"&page={i}"
    page = urlopen(page_url)
    soup = BeautifulSoup(page, "html.parser")
    eval_box = soup.find_all("td", class_="title")
    time.sleep(0.5)
    # comments = []
    for comment in eval_box:
        each_comment = (list(comment.children)[6]).strip()
        # comments.append(each_comment)
        full_comment.append(each_comment)
        print(each_comment)

print(full_comment)

dict_dat = {"영화댓글": full_comment}
dat = pd.DataFrame(dict_dat)
dat.to_csv("댓글.csv", index=False)