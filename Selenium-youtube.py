from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\dell\Desktop\chromedriver.exe')

driver.get("http://www.youtube.com")

driver.find_element_by_xpath("//input[contains(@id,'search')]").send_keys('Taare gin')

driver.find_element_by_xpath("//button[contains(@id,'search-icon-legacy')]").click()

driver.find_element_by_xpath("//a[contains(@id,'video-title')]").click()
