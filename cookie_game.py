

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

site = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome()
driver.get(site)

count = 1

def countinous_clicks():
    while count < 4:
        cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

        action_chain = ActionChains(driver)
        #Performs right click on the element
        action_chain.context_click(cookie).perform()


def option_to_click(num):
    if num == 8:
        courser = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
        courser.click()
    elif num == 7:
        grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
        grandma.click()
    elif num == 6:
        factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
        factory.click()


while count < 4:
    # countinous_clicks()

    num_of_options = driver.find_elements(By.CLASS_NAME, "grayed")


    if len(num_of_options) < 9:
        option_to_click(len(num_of_options))

    cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

    action_chain = ActionChains(driver)
    #Performs right click on the element
    action_chain.context_click(cookie).perform()
    
    # time.sleep(5)
    
    








