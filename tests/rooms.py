from selenium.webdriver.common.by import By

def first_room(driver):
    # USERNAME
    username_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[1]')
    username_input.send_keys('admin')

    # PASSWORD
    password_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[1]/input[2]')

    password_p = driver.find_element(By.CSS_SELECTOR, '#root > main > div.flip-card > div > div.flip-card-back > p:nth-child(3)')

    pwd = password_p.get_attribute("textContent")

    password_input.send_keys(pwd)

    # LOGIN BUTTON CLICK
    login_btn = driver.find_element(By.TAG_NAME, 'button')
    login_btn.click()

    print("Első szoba kész!")

def second_room(driver):
    driver.implicitly_wait(5)
    gen_table_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button[1]')

    while(True):
        try:
            gen_table_btn.click()
        except:
            break
    
    test_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
    test_btn.click()

def third_room(driver):
    driver.implicitly_wait(5)
    tipp_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/input')
    tipp_btn = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/button')
    
    for i in range(0, 99):
        tipp_input.send_keys(i)
        tipp_btn.click()
        driver.implicitly_wait(5)
        result_h2 = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/h2')
        if '✅' in result_h2.get_attribute("textContent"):
            break
        tipp_input.clear()
    
    next_page_link = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/a')
    next_page_link.click()