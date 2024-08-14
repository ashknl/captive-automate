

def login_to_captive_portal(portal_address:str) -> None:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time

    service = webdriver.FirefoxService()
    driver = webdriver.Firefox(service=service)
    driver.get(portal_address)

    username_elem = driver.find_element(By.ID,"ft_un")
    password_elem = driver.find_element(By.ID,"ft_pd")
    submit_btn = driver.find_element(By.XPATH,"/html/body/div/form/div[3]/button")

    username_elem.send_keys("ashutoshnayak23")
    password_elem.send_keys("2023cw20df324")

    submit_btn.click()
    time.sleep(2)
    driver.quit()