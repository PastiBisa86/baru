from selenium import webdriver
import time
import pickle
import os
import json

login_url='https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2F'
index_url='https://shopee.co.id/'
target_url='https://shopee.co.id/shop/20601737'
class Connect:
    def __init__(self):
        self.status=0
        self.login_method=1 # 0模擬登入 1免登入
        self.browser=webdriver.Chrome(executable_path='./chromedriver.exe')
    def set_cookies(self):
        self.browser.get(index_url)
        time.sleep(3)
        if self.browser.find_element("xpath",'//*[@id="main"]/div/header/div[1]/nav/ul/a[3]'):
            self.browser.find_element("xpath",'//*[@id="main"]/div/header/div[1]/nav/ul/a[3]').click()
        print("Tunggu 20 Detik")
        
   #     while self.browser.find_element("xpath",'//*[@id="main"]/div/header/div[1]/nav/ul/a[3]'):
    #        time.sleep(1)
        time.sleep(50)
        cookie=self.browser.get_cookies()
        with open('cookies.json','w') as f:
            f.write(json.dumps(cookie))
    def get_cookies(self):
        with open('cookies.json','r') as f:
            data=json.loads(f.read())
        for c in data:
            self.browser.add_cookie(c)
        self.browser.refresh()
        
    def login(self):
        if self.login_method==0:
            self.browser.get(login_url)
        elif self.login_method==1:
            
            if not os.path.exists('cookies.json'):
                self.set_cookies()
            else:
                self.browser.get(target_url)
                self.get_cookies()
    def day_check(self):
        self.browser.get('https://shopee.co.id/shopee-coins')
        time.sleep(3)
        self.browser.find_element("xpath",'//*[@id="main"]/div/div[2]/div/main/section[1]/div[1]/div/section/div[2]/button').click()
    def enter_conncert(self):
        self.login()
        self.browser.refresh()
        self.status =2
if __name__ == '__main__':
    connect=Connect()
    connect.enter_conncert()
    connect.day_check()
    time.sleep(50)
    
 
 
 
 
