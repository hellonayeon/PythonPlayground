from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
print(articles)

for article in articles:
    # 'li' 태그의 하위에서 다시 찾기
    # ('div.news_wrap.api_ani_send' 이하로 위에 select 함수 경로로 옮겨도 실행 가능)
    title = article.select_one('div.news_wrap.api_ani_send > div.news_area > a').text
    url = article.select_one('div.news_wrap.api_ani_send > div.news_area > a')['href']
    comp = article.select_one('div.news_wrap.api_ani_send > div.news_area > div.news_info > div.info_group > a').text.split(" ")[0].replace('언론사', '')

    print(title, url, comp)

driver.quit()