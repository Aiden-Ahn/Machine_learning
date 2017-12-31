import urllib.request
from bs4 import BeautifulSoup

search_text = input("검색어를 입력하세요 : ").encode("utf-8")
search_text = str(search_text)[2:-1].replace('\\x', '%')


# list_url = "http://search.hani.co.kr/Search?command=query&keyword="+search_text+"&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.12.29&pageseq="



def fetch_list_url():
    params = []
    for i in range(20):

        list_url = "http://search.hani.co.kr/Search?command=query&keyword=" + search_text + "&media=news&sort=d&period=all&datefrom=2000.01.01&dateto=2017.12.29&pageseq=" + str(
            i)
        url = urllib.request.Request(list_url)
        res = urllib.request.urlopen(url).read().decode("utf-8")

        # print(res)  # 위의 두가지 작업을 거치면 위의 url 의 html 문서를 res 변수에 담을수 있게 된다.

        soup = BeautifulSoup(res, "html.parser")

        for link in soup.find_all('dt'):
            for i in link:  # dt 테그 밑에 있는 a 테그를 가져오려고
                params.append(i.get('href'))  # for loop문을 돌려줌

    return params


def fetch_list_url2():
    params3 = []
    list_url = fetch_list_url()

    for i in range(len(list_url)):
        url = urllib.request.Request(list_url[i])
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser")

        params1 = []
        params2 = []

        for link1, link2 in zip(soup.find_all('p', class_="date-time"), soup.find_all('div', class_="text")):
            params1.append(link1.get_text())
            params2.append(link2.get_text())

        for i1, i2 in zip(params1, params2):
            params3.append(i1.strip())
            params3.append(i2.strip())

    return params3


f = open('d:\\data\\mydata3.txt', 'w', encoding='UTF-8')
f.writelines(fetch_list_url2())
f.close()

from wordcloud import WordCloud, STOPWORDS  # 워드 클라우딩 모듈
import matplotlib.pyplot as plt  # 시각화 모듈
from os import path  # 텍스트 파일을 불러오기 위한 open, path 하기 위해 os 임포트
import re

d = path.dirname("d://data//")  # 텍스트 파일이 있는 상위 디렉토리를 path로 지정
text = open(path.join(d, "mydata3.txt"), mode="r",
            encoding="UTF-8").read()  # 텍스트파일을 open 하는데 reading만 되게 (mode="r"), UTF-8 방식으로 불러옴(UTF-8)

text = re.sub("있다", '', text)
text = re.sub("있는", '', text)
text = re.sub("하지만", '', text)
text = re.sub("것이다", '', text)
text = re.sub("대한", '', text)
text = re.sub("통해", '', text)
text = re.sub("함께", '', text)
text = re.sub("인공지능", '', text)
text = re.sub("hani", '', text)
text = re.sub("한다", '', text)
text = re.sub("하는", '', text)
text = re.sub("위해", '', text)
text = re.sub("co", '', text)
text = re.sub("kr", '', text)
text = re.sub("위한", '', text)
text = re.sub("했다", '', text)
text = re.sub("같은", '', text)
text = re.sub("것은", '', text)
text = re.sub("그는", '', text)
text = re.sub("어떤", '', text)
text = re.sub("다른", '', text)
text = re.sub("새로운", '', text)
text = re.sub("많은", '', text)
text = re.sub("이런", '', text)
text = re.sub("다양한", '', text)
text = re.sub("제공", '', text)
text = re.sub("모든", '', text)
text = re.sub("등을", '', text)
text = re.sub("어떻게", '', text)
text = re.sub("이를", '', text)
text = re.sub("아니라", '', text)

wordcloud = WordCloud(font_path='C://Windows//Fonts//YTTE08.TTF',  # 폰트 위치(거의 기본적으로 C://Windows//Fonts 안에 들어있습니다)
                      stopwords=STOPWORDS, background_color='white',  # STOPWORDS 옵션은 공백/줄바꾸기 기준으로 단어를 추출해 냅니다
                      width=1000,  # background_color는 워드클라우드 배경색을 나타냅니다. 'black'으로하면 검은색이 됩니다.
                      height=800,  # width와 height는 워드클라우드의 크기를 지정해 줍니다.
                      colormap='PuRd').generate(text)  # colormap은 워드 색깔을 지정해주는데 첨부한 색감표를 사용하시면 됩니다. generate() 메소드는

# 워드 클라우드를 생성합니다

plt.figure(figsize=(13, 13))  # matplotlib의 pyplot을 figsize로 생성합니다

plt.imshow(wordcloud)  # 워드 클라우드 이미지를 pyplot에 띄웁니다

plt.axis("off")  # pyplot에 x, y축 표시를 없앱니다.

plt.show()




