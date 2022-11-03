from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome("C://Users//Joela//OneDrive//Escritorio//Codigo//Repositorios"
                          "//Mantenimiento_Pruebas_Software//Package//chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search = ("HP Pavilon azul")
search_input.send_keys(search)
search_input.submit()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div["
                                                                                    "1]/div[1]/div/span[1]/div["
                                                                                    "1]/div["
                                                                                    "3]/div/div/div/div/div/div/div"
                                                                                    "/div[2]/div/div/div["
                                                                                    "1]/h2/a/span")))
element.click()
amount = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "quantity")))
amount.send_keys("2")
add_to_cart = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
add_to_cart.click()
go_to_cart = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div["
                                                                                       "2]/div/div[1]/div[2]/div/div["
                                                                                       "1]/span/span/a")))
go_to_cart.click()

time.sleep(30)
driver.quit()
