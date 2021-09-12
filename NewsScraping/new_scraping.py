from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
# 출력해보면 어디까지 추출했는지 확인 가능
# print(articles)

# [엑셀에 스크래핑한 내용 저장] 워크북, 워크시트 생성
wb = Workbook()
ws = wb.active
ws.title = "articles"

for article in articles:
    # 'li' 태그의 하위에서 다시 찾기
    # ('div.news_wrap.api_ani_send' 이하로 위에 select 함수 경로로 옮겨도 실행 가능)
    title = article.select_one('div.news_wrap.api_ani_send > div.news_area > a').text
    url = article.select_one('div.news_wrap.api_ani_send > div.news_area > a')['href']
    comp = article.select_one('div.news_wrap.api_ani_send > div.news_area > div.news_info > div.info_group > a').text.split(" ")[0].replace('언론사', '')

    ws.append([title, url, comp]) # 엑셀 파일에 저장할 내용 추가

driver.quit()
wb.save(filename='article.xlsx')