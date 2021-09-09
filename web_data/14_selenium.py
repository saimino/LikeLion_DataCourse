from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
# url = "http://browse.auction.co.kr/search?keyword=%EA%B0%80%EB%B0%A9&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EA%B0%80%EB%B0%A9&acode=SRP_SU_0100&arraycategory=&encKeyword=%EA%B0%80%EB%B0%A9"
# page = urlopen(url)
# soup = BeautifulSoup(page, 'lxml')
# print(soup.title)

driver = webdriver.Chrome('./data/chromedriver')