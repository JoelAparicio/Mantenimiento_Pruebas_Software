from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("C://Users//Joela//OneDrive//Escritorio//Codigo//Repositorios//Mantenimiento_Pruebas_Software//Package//chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

time.sleep(100)
driver.close()