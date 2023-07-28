import webdriver

if webdriver.can_connect() == False:
    webdriver.login()

else:
    print('Connected')
