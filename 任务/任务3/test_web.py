import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def denglu():
    pass

def gongneng1():
    pass
def tuichu():
    driver.get('http://139.196.167.227/admin/home/')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/span').click()

if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("http://139.196.167.227/admin/login")
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('admin')
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/div/input').send_keys('admin123')
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[3]/div/div[1]/div/div/input').send_keys('8')
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/form/div[4]/div/button').click()



    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div/ul/li[5]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/li[5]/ul/li[2]/span').click()
    driver.implicitly_wait(3)
    #driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div/button[1]/span').click()

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/ul/li/ul/li[5]').click()
    # driver.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[1]/div/div/div/div[1]/div/i').click()
    # driver.implicitly_wait(1)
    # driver.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[1]/div/div/div/div[2]/ul[2]/li[4]').click()
    # driver.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[2]/div/div/div/textarea').send_keys("test")
    # driver.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/form/div/div[3]/div/div/div/textarea').send_keys("test_123456")
    # time.sleep(1)
    # driver.find_element(By.XPATH,'/html/body/div[16]/div[2]/div/div/div/div/div[2]/div/button').click()
    print(driver.find_element(By.XPATH,'//span[@class="ivu-page-total"]').text)




    #tuichu()
    time.sleep(3)