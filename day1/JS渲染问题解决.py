from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.taobao.com')
print(driver.page_source)