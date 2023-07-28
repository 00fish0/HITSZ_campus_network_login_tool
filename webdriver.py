import requests
import bs4
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

def can_connect():
    baidu_request = requests.get("http://www.baidu.com")
    if (baidu_request.status_code == 200):
        baidu_request.encoding = 'utf-8'
        baidu_request_bsObj = bs4.BeautifulSoup(baidu_request.text, 'html.parser')
        baidu_input = baidu_request_bsObj.find(value="百度一下")
        if (baidu_input == None):
            return False
        return True

    return False

json_str = json.load(open('conf.json'))

username_str = json_str['username_str']
password_str = json_str['password_str']

# can_connect = True

def login():
    try:
        options = Options()
        options.headless = True
        #binary = FirefoxBinary("/usr/bin/firefox")
        driver = webdriver.Firefox(#firefox_binary=binary,
                                   options=options,
                                   executable_path="/home/ices/Documents/login/geckodriver")
        driver.get("http://10.248.98.2/") # 你的校园网登陆地址
        time.sleep(3)
        username_input = driver.find_element_by_id("username") # 校园网登陆用户名的输入控件ID, 浏览器上右键查看网页源代码查询
        password_input = driver.find_element_by_id("password") # 校园网登陆密码的输入控件ID, 浏览器上右键查看网页源代码查询
        print('Searching connect')
        login_button = driver.find_element_by_id("login") # 校园网登陆连接的点击控件ID, 浏览器上右键查看网页源代码查询
        print('Find connect successfully')
        username_input.send_keys(username_str)
        password_input.send_keys(password_str)
        print('Input user info')
        login_button.click()
        time.sleep(3)
        if can_connect():
            print('Connect')
        else:
            print('Connected failed, wait a second and try again')
    except Exception as e:
        print(e)
        print(u"登陆函数异常")
    finally:
        pass


