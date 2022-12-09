from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome("C://Users//Joela//OneDrive//Escritorio//Codigo//Repositorios"
                          "//Mantenimiento_Pruebas_Software//Package//chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/ingenieriaweb/Proyecto-IngenieriaWeb/Inicio.php")
try:
    equipos = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[5]/a")))
    time.sleep(2)
    equipos.click()
    time.sleep(1)
except:
    print("La pagina web no cargo correctamente")
finally:
    print("La pagina web cargo correctamente en menos de 5 segundos")
    time.sleep(3)
    driver.quit()

