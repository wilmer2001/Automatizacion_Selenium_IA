from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import spacy
import traceback
from selenium.common.exceptions import TimeoutException
from configExcel import URL

# Cargar el modelo de lenguaje para clasificación de campos
nlp = spacy.load("en_core_web_sm")


# Función para generar el selector del campo
def generate_selector(element):
    # Primero, busca el nombre
    element_name = element.get_attribute("name")
    if element_name:
        return f'[name="{element_name}"]'

    # Luego, busca el ID
    element_id = element.get_attribute("id")
    if element_id:
        return f"#{element_id}"

    # Después, busca la clase
    element_class = element.get_attribute("class")
    if element_class:
        class_selector = ".".join(element_class.split())
        return f".{class_selector}"

    # Genera el XPath si no se puede obtener el selector CSS
    return driver.execute_script(
        """  
        function getElementXPath(element) {
            var path = [];
            while (element.nodeType === Node.ELEMENT_NODE) {
                var selector = element.nodeName.toLowerCase();
                if (element.id) {
                    selector += '#' + element.id;
                    path.unshift(selector);
                    break;
                } else {
                    var sibling = element;
                    var nth = 1;
                    while (sibling = sibling.previousSibling) {
                        if (sibling.nodeType === Node.ELEMENT_NODE && sibling.nodeName.toLowerCase() === selector) {
                            nth++;
                        }
                    }
                    selector += ':nth-of-type(' + nth + ')';
                }
                path.unshift(selector);
                element = element.parentNode;
            }
            return path.length ? '/' + path.join('/') : null;
        }
        return getElementXPath(arguments[0]);
    """,
        element,
    )


# Función para crear el script de automatización
def create_automation_script(selectors):
    if not selectors:
        print("No hay selectores para guardar.")
        return

    script = """from selenium import webdriver\n"""
    script += """from configExcel import URL\n"""
    script += """from selenium.webdriver.common.by import By\n\n"""
    script += """driver = webdriver.Chrome()\n"""
    script += """driver.get(URL)\n\n"""

    for selector, element_type in selectors:
        if element_type == "input":
            script += f"driver.find_element(By.CSS_SELECTOR, '{selector}').send_keys('Valor a ingresar')\n"
        elif element_type in ["button", "a", "select", "img", "div"]:
            script += f"driver.find_element(By.CSS_SELECTOR, '{selector}').click()\n"
        else:
            script += f"driver.find_element(By.CSS_SELECTOR, '{selector}').click()\n"  # Otros elementos

    script += """\ndriver.quit()"""

    try:
        # Guardar el script en un archivo
        with open("IA_Automation.py", "w") as f:
            f.write(script)
        print("El script de automatización ha sido generado en 'IA_Automation.py'")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")


# Inicializa Selenium y abre la página web con tiempos de espera
driver = webdriver.Chrome()

# Espera explícita para la página completa antes de interactuar
wait = WebDriverWait(driver, 40)

driver.get(URL)


def asignacion_selector(list_selector, inp_selectors, inp_existing_selectors):

    try:
        for list_item in list_selector:
            input_fields = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, list_item))
            )
            for field in input_fields:
                selector = generate_selector(field)
                # Verifica si el selector ya existe
                if selector not in existing_selectors:
                    inp_selectors.append((selector, list_item))
                    inp_existing_selectors.add(
                        selector
                    )  # Agrega el nuevo selector al conjunto
                    print(f"Selector generado para el campo de entrada: {selector}")
                else:
                    print(f"Selector ya existente, no se genera: {selector}")
    except TimeoutException as e:
        print("Timeout al buscar campos de entrada de texto:", e)


try:
    selectors = []
    existing_selectors = set()  # Conjunto para almacenar selectores únicos
    list_selector = ["input", "button", "select", "a", "img", "div[onclick], div[role]"]
    # Encuentra y procesa campos de entrada (text inputs)
    asignacion_selector(list_selector, selectors, existing_selectors)
    # Crear el script de automatización con los selectores
    create_automation_script(selectors)

except Exception as e:
    print(f"Error al procesar la página: {e}")
    print(traceback.format_exc())

# Cierra el navegador
driver.quit()
