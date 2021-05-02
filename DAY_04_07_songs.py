# DAY_04_07_songs

import requests
import re

def show_songs(code, page):
    url ='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'

    # S_PAGENUMBER:2
    # S_MB_CD:W0726200
    # S_HNAB_GBN:I
    # hanmb_nm:G-DRAGON
    # payload = dict(S_PAGENUMBER=1, S_MB_CD='W0726200') # data parameter 전달을 위한 dictionary
    payload = dict(S_PAGENUMBER=page, S_MB_CD=code) # data parameter 전달을 위한 dictionary

    recvd =requests.post(url,payload)

    # print(recvd)
    # print(recvd.text)
    tbody = re.findall(r'<tbody>(.+?)</tbody>',recvd.text,re.DOTALL)

    list = re.findall(r'<tr>(.+?)</tr>', tbody[0] ,re.DOTALL)

    if not list:
        return False

    for td in list:
        # td = re.sub(r'<img src="/images/common/(NO_, )control.gif" border="0" alt="" />',
        #             '',
        #             td)
        td = re.sub(r' <img .+? />', '', td)
        td = re.sub(r'<br/>', ', ',td)

        items = re.findall(r'<td>(.+?)</td>',td,re.DOTALL)
        items = [i.strip() for i in items] # 공백제거

        print(items, sep='\n')

    return True
#
# page =1
# while show_songs('10003665', page):
#     print('='*30, page)
#     page += 1

def save_img():
    url='https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
    recvd = requests.get(url)

    f = open('Data/google.jpg', 'wb')
    f.write(recvd.content)
    f.close()
save_img()














