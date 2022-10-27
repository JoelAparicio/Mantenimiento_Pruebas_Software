package Selenium_Pack;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class primera_prueba {
	public static void main (String[] args)throws InterruptedException {
		System.setProperty("webdriver.chrome.driver","C:\\Users\\Joela\\OneDrive\\Escritorio\\Codigo\\Repositorios\\Mantenimiento_Pruebas_Software\\Package\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("https://www.amazon.com/");
		driver.findElement(By.id("twotabsearchtextbox")).click();
		((WebElement) driver) .sendKeys("Laptop");
		//inserta tu código aquí
		Thread.sleep(5000);
		driver.quit();
		}
}
