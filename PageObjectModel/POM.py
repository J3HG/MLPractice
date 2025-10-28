from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class POM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Locators ---
    mexicoLocator = (By.XPATH, "//a[@id='MX']")
    searchingBarLocator = (By.XPATH, "//input[@class='nav-search-input']")
    newBtnLocator = (By.XPATH, "//span[contains(text(), 'Nuevo')]")
    masTardeBtnLocator = (By.XPATH, "//span[contains(text(), 'Más tarde')]")
    cookieBtnLocator = (By.XPATH, "//button[contains(., 'Aceptar') or contains(., 'cookies') or contains(., 'Entendido')]")
    bannerLocator = (By.XPATH, "//div[contains(@class, 'cookie-consent-banner')]")
    overlayLocator = (By.CSS_SELECTOR, ".andes-modal__overlay, .ui-overlay, .modal-overlay")
    dropdownTriggerLocator = (By.XPATH, "//div[@id=':Rlilie:']") #andes-dropdown__display-values
    mayorPrecioLocator = (By.XPATH, "//li//span[contains(text(), 'Mayor precio')]")
    titulosLocator = (By.XPATH, "//a[@class='poly-component__title']")
    preciosLocator = (By.XPATH, "//div[@class='poly-price__current']")

    def mexicoBtn(self):
        return self.wait.until(EC.element_to_be_clickable(self.mexicoLocator))

    def buscarPlay(self):
        return self.wait.until(EC.visibility_of_element_located(self.searchingBarLocator))

    def masTardeBtn(self):
        try:
            masTBtn = self.wait.until(EC.element_to_be_clickable(self.masTardeBtnLocator))
            masTBtn.click()
        except:
            pass

    def newBtn(self):
        return self.wait.until(EC.element_to_be_clickable(self.newBtnLocator))

    def cerrar_cookies(self):
        try:
            # Esperando a que desaparezca el overlay
            try:
                self.wait.until(EC.invisibility_of_element_located(self.overlayLocator))
            except:
                pass  # Por si no había overlay

            # Encontrando el botón de "Aceptar cookies"
            cookieBtn = self.wait.until(EC.element_to_be_clickable(self.cookieBtnLocator))

            # Ejecutar clic vía JavaScript
            self.driver.execute_script("arguments[0].click();", cookieBtn)
            #Comprobación en la consola
            print(" Banner de cookies cerrado correctamente.")
        except Exception as e:
            #Comprobación en la consola
            print("No se encontró banner de cookies o ya estaba cerrado:", e)

    def ordenar_por_mayor_precio(self):
        #Se abre el dropdown list y se seleccionar la opción de "Mayor precio", sin embargo se coloca en un try catch para evitar errores en la selección de las opcionescl
        try:
            dropdown_trigger = self.wait.until(EC.element_to_be_clickable(self.dropdownTriggerLocator))
            dropdown_trigger.click()

            mayor_precio_opcion = self.wait.until(EC.element_to_be_clickable(self.mayorPrecioLocator))
            mayor_precio_opcion.click()

            print("Filtro aplicado: 'Mayor precio'")
        except Exception as e:
            print("No se pudo aplicar el filtro 'Mayor precio':", e)

    def getTitles(self):
        """Devuelve todos los títulos y precios de productos visibles en la página."""
        try:
            # Esperar hasta que al menos un título esté presente
            titles = self.wait.until(
                EC.presence_of_all_elements_located(POM.titulosLocator)
            )

            # Esperar hasta que al menos un precio esté presente
            prices = self.wait.until(
                EC.presence_of_all_elements_located(POM.preciosLocator)
            )

            print(f"🟢 Se encontraron {len(titles)} títulos y {len(prices)} precios.")
            return titles, prices

        except Exception as e:
            print("⚠️ No se pudieron obtener los títulos o precios:", e)
            return [], []





