from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\dell\Desktop\chromedriver.exe')

driver.get("http://www.facebook.com")

driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys("nivithakumar1308@gmail.com")

driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys("nivi1308")

driver.find_element_by_xpath("//button[contains(@value,'1')]").click()
