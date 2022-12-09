from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("C://Users//Joela//OneDrive//Escritorio//Codigo//Repositorios"
                          "//Mantenimiento_Pruebas_Software//Package//chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/sitios/Proyecto-IngenieriaWeb/Inicio.php")
try:
    resultados = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[3]/a")))
    time.sleep(2)
    resultados.click()
    dia = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/select")))
    dia_seleccion = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/select/option[21]")))
    dia.click()
    dia_seleccion.click()
    time.sleep(2)
    mes = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/select")))
    mes_seleccion = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/select/option[2]")))
    mes.click()
    mes_seleccion.click()
    time.sleep(2)
    buscar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/form/input")))
    buscar.click()
    time.sleep(2)
except:
    print("La pagina web no cargo correctamente")
finally:
    print("La pagina web cargo correctamente en menos de 5 segundos")
    time.sleep(3)
    driver.quit()

