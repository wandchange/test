import time
from selenium import webdriver
# 等待模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
  步骤：
        1.爬取拉钩网所有的php职位详情页链接
        2.进一步爬取详情页的职位信息
        3.保存为csv文件
  要求：
        1、能做到输入职位，城市，等等筛选条件，不拘泥于只能爬取固定的城市与职位
        2、
"""
# https://www.lagou.com/jobs/list_PHP?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&xl
# =%E5%A4%A7%E4%B8%93&city=%E5%B9%BF%E5%B7%9E#filterBox
def is_element_exist(css):
    x = driver.find_elements_by_css_selector(css)
    if len(x) == 0:
        print("元素未找到{}".format(css))
        return False
    elif len(x) == 1:
        return True
    else:
        print("找到{0}个元素：{1}".format(len(x),css))
        return False

driver = webdriver.Firefox()
driver.get("https://www.lagou.com/jobs/list_PHP?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&xl=%E5%A4%A7%E4%B8%93&city=%E5%B9%BF%E5%B7%9E#filterBox")
# print("初始页面",type(driver))
wait = WebDriverWait(driver, 3)  # 等待3秒
n = 0
position_link_list = []
"""
<span hidefocus="hidefocus" action="next" class="pager_next ">下一页
<strong class="pager_lgthen "></strong></span>

<span hidefocus="hidefocus" action="next" class="pager_next pager_next_disabled">下一页
<strong class="pager_lgthen pager_lgthen_dis"></strong></span>
下一页在最后一页时会变灰色，同时class【pager_next pager_next_disabled】出现，可以选择它作为状态，即灰色时不再翻页，获取所有职位详情页链接完成
"""
while True:
    if is_element_exist("pager_next pager_next_disabled"):
        print("======获取所有职位详情页链接完成!======")
        break
    # print(driver.current_url)
    position_link = driver.find_elements_by_xpath("//*[@class='position_link']")
    for link in position_link:
        href = link.get_attribute("href")
        print(href)
        position_link_list.append(href)
        n+=1
    time.sleep(0.5)

    driver.find_element_by_class_name('pager_next').click()  # 点击下一页


print(n)
print(position_link_list)


