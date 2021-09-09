import wordcloud
from wordcloud import WordCloud
from matplotlib import rc

print(wordcloud.__version__)

f = open("댓글.csv", encoding = "utf-8")
text = f.read()
print(text)
f.close()

rc('font', family = "NanumGothic")

wcloud = WordCloud("./data/D2Coding.ttf",
                   max_words=1000,
                   relative_scaling=0.2).generate(text)


import matplotlib.pyplot as plt

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()