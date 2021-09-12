from wordcloud import WordCloud
import csv
from PIL import Image
import numpy as np

# 데이터 클렌징: 원하는 데이터를 얻기 위해서 불필요한 데이터를 제거해주는 작업

talk_content = ''
with open('kakaotalk.csv', 'r', encoding='utf-8') as file:
    lines = list(csv.reader(file)) # csv reader 함수의 리턴형은  'csv.reader', 따라서 'list()' 함수로 리스트형 생성
    for line in lines[1:]:
        # 대화 '내용(Message)' 부분만 추출
        # 페이스톡 시작종료 제외
        talk_content += line[2].replace('ㅎ', '').replace('페이스톡', '').replace(':', '').replace('[0-9]', '')

# print(talk_content)

# [Word Cloud Customize] 글자 색상 변경하기
# hsl(341, 100%, 85%) hsl(220, 100%, 80%) 사이값에서 색상 변경
def get_color(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(220,341),100, np.random.randint(80,85)))


mask = np.array(Image.open('cloud.png')) # 워드클라우드 모양 변경
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", mask=mask, color_func = get_color)
wc.generate(talk_content)
wc.to_file("word_cloud.png")



# [시스템에 저장된 사용 가능한 폰트 검색]
# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)


