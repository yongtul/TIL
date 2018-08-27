# https://finance.naver.com/sise/ 에 요청을 보내서, 응답을 받아온다.

import requests
import bs4

#requests.get(url)

url = "https://finance.naver.com/sise/"
response = requests.get(url)

# print(response.text)

html = bs4.BeautifulSoup(response.text, "html.parser")    # 검색하기 좋게 예쁘게 만든다
                                           # BeautifulSoup 이 정제를 함.
#print(html)

kospi = html.select_one('#KOSPI_now')

print(kospi.text)
