'''
蓝桥杯试题爬虫
'''

from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
import time
from lxml import etree
import re
from PIL import Image



#
# def Get_Opener():
#     # 创建一个cookiejar对象
#     cookiejar=CookieJar()
#     # 使用cookiejar创建一个httpcookieprocessor对象
#     handle=request.HTTPCookieProcessor(cookiejar)
#     # 使用handle创建一个opener
#     opener=request.build_opener(handle)
#
#     return opener




def Get_Url():
    url="http://lx.lanqiao.cn/problem.page?gpid="
    for i in range(412,413):
        Save_Data(url+"T{0}".format(i))



def Login():
    url="http://dasai.lanqiao.cn/pages/account/login_other.html?backurl=http%3A//lx.lanqiao.cn/lqloginfinished.page%3Fredir%3D/problem.page"
    header = {
        "User - Agent": "Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181 Safari / 537.36",
    }

    driver = webdriver.Firefox()

    driver.get(url)
    #
    #
    # handles = driver.window_handles
    # driver.switch_to_window(handles[1])

    driver.find_element_by_name('login').send_keys("18877423546")
    driver.find_element_by_name('pwd').send_keys("cjy1995309")
    time.sleep(6)
    driver.find_element_by_xpath("//*[@class='sub mt10']").click()

    # print(driver.page_source)
    time.sleep(5)
    # driver.find_element_by_xpath("//a[@href='/problemsets.page']").click()

    url1 = "http://lx.lanqiao.cn/problem.page?gpid="
    # now_handle = driver.current_window_handle
    for i in range(1, 496):
        Save_Data(url1 + "T{0}".format(i),i,driver)
        time.sleep(3)


def Save_Data(url,i,driver):
    print(i)
    driver.get(url)

    handles = driver.window_handles
    driver.switch_to_window(handles[0])

    html=driver.page_source

    driver.set_window_size(1200, 900)
    driver.execute_script("""
           (function () {
               var y = 0;
               var step = 100;
               window.scroll(0, 0);

               function f() {
                   if (y < document.body.scrollHeight) {
                       y += step;
                       window.scroll(0, y);
                       setTimeout(f, 100);
                   } else {
                       window.scroll(0, 0);
                       document.title += "scroll-done";
                   }
               }

               setTimeout(f, 1000);
           })();
       """)

    for i in range(30):
        if "scroll-done" in driver.title:
            break
        time.sleep(5)
    driver.save_screenshot('../data/{0}.png'.format(i))



    # soup = BeautifulSoup(html, 'lxml')
    #
    # print("--------")
    # img = soup.find_all("div", class_="des")
    # re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    # re_br= re.compile('<br\s*?/?>')  # 处理换行
    # # 处理&lt
    # re_lt=re.compile('&lt;')
    # re_gt = re.compile('&gt;')
    # re_amp = re.compile('&amp;')
    # re_left = re.compile("\[")
    # re_right = re.compile(']')
    #
    # s = re_h.sub('', str(img))
    # s=re_br.sub('', s)
    # s=re_lt.sub('<',s)
    # s = re_gt.sub('>', s)
    # s = re_amp.sub('&', s)
    # s = re_left.sub('', s)
    # s = re_right.sub('', s)
    # print(s)
    # with open("./data/{0}.txt".format(i),"w",encoding='utf-8') as f:
    #     f.write(s)
    # time.sleep(1)
    # element = driver.find_element_by_xpath("//div[@class='problem']")


    # left = element.location['x']
    # top = element.location['y']
    # right = element.location['x'] + element.size['width']
    # bottom = element.location['y'] + element.size['height']
    #
    # im = Image.open('../data/{0}.png'.format(i))
    # im = im.crop((left, top, right, bottom))
    # im.save('../data/{0}.png'.format(i))






if __name__ == '__main__':
    Login()












































