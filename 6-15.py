import time
from selenium import webdriver
from lxml import etree

class taobao():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        #链接是在淘宝搜索上选好筛选参数的链接
        self.driver.get("https://s.taobao.com/search?q=%E6%98%BE%E7%A4%BA%E5%99%A8&type=p&tmhkh5=&spm=a21wu.241046-cn.a2227oh.d100&from=sea_1_searchbutton&catId=100&cps=yes&ppath=21433%3A386520869%3B21433%3A79937%3B21433%3A78225%3B21433%3A134082108%3B21433%3A25515396%3B21433%3A11079864%3B21433%3A80111%3B29029%3A78185%3B29029%3A3231227%3B29656%3A80020%3B122216344%3A79352303&fs=1&baoyou=1&user_type=1&filter=reserve_price%5B500%2C1300%5D")
        print("初始页面",type(self.driver))
        time.sleep(1)
        self.driver.find_element_by_class_name("h").click()  #点击登录按钮进入登录页
        self.driver.find_element_by_class_name('login-switch').click() #点击右上角二维码切换到账号密码登录
        """
            使用支付宝账密登录淘宝更为轻松
        """
        self.driver.find_element_by_class_name('alipay-login').click() #点击支付宝登录
        time.sleep(1)
        self.driver.find_element_by_xpath("//li[@data-status='show_login']").click()
        time.sleep(1)
        #直接输入账户名容易被网站标识为机器，而每次输入一个数字更符合人类打字速度
        for num in '账号':
            self.driver.find_element_by_id('J-input-user').send_keys(num) #输入账号
            time.sleep(0.2)

        self.driver.find_element_by_id('password_rsainput').send_keys('密码') #输入密码
        time.sleep(1)
        self.driver.find_element_by_id('J-login-btn').click() #提交登录信息
        #进入下一阶段，获取所有商品的id 例：J_Itemlist_Pic_521901618079，只需要匹配J_Itemlist_Pic_即可


        img_url = self.driver.find_elements_by_xpath("//img[contains(@id,'J_Itemlist_Pic_')]")
        i = 0
        for img in img_url:
            print("img:",img,"type:",type(img))
            handle = self.driver.current_window_handle #定位当前页面句柄
            img.click()
            handles = self.driver.window_handles  #获取所有页面句柄
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:
                    # 切换到新打开的窗口B
                    current_window = self.driver.switch_to.window(newhandle)
                    # print(current_window)
            # 在新打开的窗口B中操作
                    Promises = self.driver.find_element_by_class_name('tb-serPromise')
            #         Promises = self.driver.find_element_by_xpath("//ul[@class='tb-serPromise']")

                    print(self.driver)

                    # for Promise in Promises:
                    print(Promises)
                    # 关闭当前窗口B
                    current_window.close()
                    # 切换回窗口A
                    self.driver.switch_to.window(handles[0])
                    i+=1

        print(i)


if __name__ == '__main__':
    taobao = taobao()
    taobao.login()
