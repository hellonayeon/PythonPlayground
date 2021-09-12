from bs4 import BeautifulSoup
from selenium import webdriver
import dload
import time

# selenium: 브라우저 자동 제어 패키지
# BeautifulSoup: 브라우저가 보고있는 것들 중에서, 내가 원하는 것을 솎아내는 패키지

driver = webdriver.Chrome('./chromedriver')
driver.get('https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EA%B3%A0%EC%96%91%EC%9D%B4')
time.sleep(5) # 5초동안 페이지 로딩 기다리기

# HTML을 BeautifulSoup 패키지를 통해 파싱하기 용이한 상태로 변경
# 'soup' 변수 안에는 '파싱하기 용이한 HTML'이 담긴 상태
# 'soup' 에서 코딩에 필요한 정보 추출
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# select, select_one
thumbnails = soup.select('#imgList > div > a > img')
fnum = 1
for thumbnail in thumbnails:
    url = thumbnail['src']
    dload.save(url, f'./images/{fnum}.jpg')
    fnum += 1

driver.quit() # 끝나면 닫아주기