import requests
import bs4
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


def can_connect():
    baidu_request = requests.get("http://www.baidu.com")
    if baidu_request.status_code == 200:
        baidu_request.encoding = "utf-8"
        baidu_request_bsObj = bs4.BeautifulSoup(baidu_request.text, "html.parser")
        baidu_input = baidu_request_bsObj.find(value="百度一下")
        if baidu_input == None:
            return False
        return True

    return False


json_str = json.load(open("conf.json"))

username_str = json_str["username_str"]
password_str = json_str["password_str"]

# can_connect = True


def login():
    driver = None
    try:
        options = Options()
        options.headless = True
        # binary = FirefoxBinary("/usr/bin/firefox")
        driver = webdriver.Firefox(options=options)  # firefox_binary=binary,
        driver.get(
            "https://net.hitsz.edu.cn/srun_portal_pc?ac_id=1&theme=basic4"
        )  # 你的校园网登陆地址

        # Create a WebDriverWait instance
        wait = WebDriverWait(driver, 10)

        local_user_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-account"))
        )
        local_user_button.click()
        print("Clicked local user login button")

        username_input = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        print("Found login form elements")

        # Enter credentials
        username_input.clear()
        username_input.send_keys(username_str)
        password_input.send_keys(password_str)
        print("Input user info")

        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-account")))
        login_button.click()
        print("Clicked login button")

        time.sleep(3)
        if can_connect():
            print("Connect successful")
        else:
            print("Connected failed, wait a second and try again")
    except Exception as e:
        print(f"Error during login: {e}")
    finally:
        if driver:
            driver.quit()  # Make sure to close the browser
