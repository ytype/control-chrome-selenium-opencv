from selenium import webdriver
from selcv import selcv
import time
sc = selcv('./chromedriver')
sc.driver_get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
sc.find_element_screen_shot('id','class','id_area')
sc.find_element_screen_shot('pw','class','pw_area')
sc.find_element_screen_shot('btn','xpath','//*[@id="log.login"]')

id_position = sc.find_element_by_tm('id')
pw_position = sc.find_element_by_tm('pw')
btn_position = sc.find_element_by_tm('btn')

print("id: ", id_position)
print("pw: ",pw_position)
print("btn: ",btn_position)

sc.click_paste_text(id_position,'userID')
time.sleep(1)
sc.click_paste_text(pw_position,'userPW')
time.sleep(1)
sc.click(btn_position)
