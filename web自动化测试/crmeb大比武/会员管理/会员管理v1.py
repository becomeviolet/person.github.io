import time
from selenium.webdriver.support.select import Select
from selenium import webdriver

from selenium.webdriver.common.by import By






if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get("http://139.9.209.241:8080/woniusales/")
    driver.maximize_window()

    driver.find_element(By.ID, '''username''').send_keys('''admin''')
    driver.find_element(By.ID, '''password''').send_keys('''admin123''')
    driver.find_element(By.ID, '''verifycode''').send_keys('''0000''')
    time.sleep(1)
    driver.find_element(By.XPATH, '''/html/body/div[4]/div/form/div[6]/button''').click()
    time.sleep(2)
    text1 = driver.find_element(By.XPATH, '''/html/body/div[2]/div/div[2]/ul[2]/li[1]/a''').text
    assert "管理员" in text1
    time.sleep(1)

    driver.find_element(By.XPATH, '''//*[@id="navbar"]/ul[1]/li[5]/a''').click()
    time.sleep(1)
    driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
    driver.find_element(By.ID, '''customername''').clear()
    driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
    Select1 = Select(driver.find_element(By.ID, '''childsex'''))
    Select1.select_by_visible_text('''女''')

    driver.find_element(By.ID, '''childdate''').click()
    driver.find_element(By.XPATH, '''/html/body/div[6]/div[3]/table/tbody/tr[3]/td[5]''').click()
    driver.find_element(By.ID, '''creditkids''').clear()
    driver.find_element(By.ID, '''creditkids''').send_keys('''85''')
    driver.find_element(By.ID, '''creditcloth''').clear()
    driver.find_element(By.ID, '''creditcloth''').send_keys('''85''')
    driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[1]''').click()
    # 已经有的信息
    try:
        # js1 = '''document.querySelector("body > div.bootbox.modal.fade.mydialog.in > div > div > div.modal-footer > button").click()'''
        # driver.execute_script(js1)
        # driver.execute_script(js1)
        time.sleep(2)
        driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
    except:
        print("重复添加")
    time.sleep(1)

    driver.find_element(By.ID, '''customerphone''').clear()
    driver.find_element(By.ID, '''customerphone''').send_keys('''19914665037''')
    time.sleep(1)
    driver.find_element(By.ID, '''customername''').clear()
    driver.find_element(By.ID, '''customername''').send_keys('''test_hzt''')
    time.sleep(1)
    driver.find_element(By.XPATH, '''/html/body/div[4]/div[1]/form[2]/div[2]/button[3]''').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '''//*[@id="customerlist"]/tr[1]/td[11]/a''').click()
    driver.find_element(By.XPATH, '''//*[@id="editBtn"]''').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '''/html/body/div[7]/div/div/div[3]/button''').click()
    time.sleep(2)
