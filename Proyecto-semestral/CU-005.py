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
    usuario = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[6]")))
    acceso = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[6]/ul/li[2]/a")))
    movimiento = ActionChains(driver)
    time.sleep(2)
    movimiento.move_to_element(usuario).move_to_element(acceso).click().perform()
    time.sleep(2)
    nombre = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[1]")))
    time.sleep(2)
    nombre.send_keys("Joel")
    contraseña = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[2]")))
    time.sleep(2)
    contraseña.send_keys("123456")
    equipos = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[2]/a")))
    time.sleep(2)
    equipos.click()
    time.sleep(2)
    seleccion_equipo = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/a")))
    seleccion_equipo.location_once_scrolled_into_view
    time.sleep(2)
    seleccion_equipo.click()
    favorito = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/a")))
    favorito.click()
    time.sleep(2)
except:
    print("La pagina web no cargo correctamente")
finally:
    print("La pagina web cargo correctamente en menos de 5 segundos")
    time.sleep(3)
    driver.quit()

