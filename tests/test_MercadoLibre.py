import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from PageObjectModel.POM import POM
import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setUpDriver")
class Test_MercadoLibre:
    def test_MercadoLibreMX(self):
        object = POM(self.driver)
        #Presionando el botón de la bandera de México
        object.mexicoBtn().click()
        #Presionando el botón para quitar un Pop Up
        object.masTardeBtn()
        #Presionando el botón para cerrar el banner de las cookies
        object.cerrar_cookies()

    def test_BuscarPlay(self):
        object = POM(self.driver)
        #Escribiendo en la barra de búsqueda
        object.buscarPlay().send_keys("playstation5")
        #Presionando enter para buscar
        object.buscarPlay().send_keys(Keys.ENTER)
        #Filtrando por la categoría "Nuevo"
        object.newBtn().click()
        #Ordenando de mayor a menor precio
        object.ordenar_por_mayor_precio()

    def test_printingValues(self):
        object = POM(self.driver)

        #Asignando a variables los valores de títulos y precios
        titles, prices = object.getTitles()

        #Asegurándome de que no cause un error si no llegara a encontrar alguno
        if not titles or not prices:
            print("No se encontraron productos o precios para imprimir.")
        else:
            print(f"Se encontraron {len(titles)} productos:")
            #Asegurando que solamente se muestren los primeros 5 productos
            for title, price in zip(titles[:5], prices[:5]):
                print(f"{title.text} — {price.text}")