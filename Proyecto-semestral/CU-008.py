from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C://Users//Joela//OneDrive//Escritorio//Codigo//Repositorios"
                          "//Mantenimiento_Pruebas_Software//Package//chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://localhost/ingenieriaweb/Proyecto-IngenieriaWeb/Inicio.php")
try:
    usuario = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[6]")))
    acceso = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[6]/ul/li[2]/a")))
    movimiento = ActionChains(driver)
    time.sleep(2)
    movimiento.move_to_element(usuario).move_to_element(acceso).click().perform()
    time.sleep(1)
    nombre = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[1]")))
    time.sleep(1)
    nombre.send_keys("Joel")
    contraseña = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[2]")))
    time.sleep(1)
    contraseña.send_keys("1234")
    iniciar_sesion = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form/input[3]")))
    time.sleep(1)
    iniciar_sesion.click()
    time.sleep(1)
    resultados = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/ul/li[2]/a")))
    resultados.click()
    time.sleep(1)
    grupo = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[1]")))
    grupo.send_keys("D")
    time.sleep(1)
    equipo1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[2]")))
    equipo1.send_keys("Argentina")
    time.sleep(1)
    goles1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[3]")))
    goles1.send_keys("2")
    time.sleep(1)
    equipo2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[4]")))
    equipo2.send_keys("Brasil")
    time.sleep(1)
    goles2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[5]")))
    goles2.send_keys("1")
    time.sleep(1)
    estadio = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[6]")))
    estadio.send_keys("Al bufe")
    time.sleep(1)
    fecha = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[7]")))
    fecha.send_keys("11/06/2022")
    time.sleep(1)
    hora = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[8]")))
    hora.click()
    hora.send_keys("12:00P.M.")

    time.sleep(1)
    registrar_resultados = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/input[9]")))
    registrar_resultados.click()
    time.sleep(8)


except:
    print("La pagina web no cargo correctamente")
finally:
    print("La pagina web cargo correctamente en menos de 5 segundos")
    time.sleep(3)
    driver.quit()

