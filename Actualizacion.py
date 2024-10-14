import os
import re
import time
import importlib.util
from configExcel import URL


def copy_and_modify_file(src_file, dest_file):
    if os.path.exists(src_file):
        with open(src_file, "r", encoding="utf-8") as file:
            content = file.readlines()

        updated_content = []  # Inicializa como lista
        campo_counter = 1  # Contador para los campos, empieza en 1

        for line in content:
            if (
                line.strip().startswith("from selenium.webdriver.common.by import By")
                or line.strip().startswith("driver = webdriver.Chrome()")
                or line.strip().startswith("driver.quit()")
                or line.strip().startswith("from selenium import webdriver")
                or line.strip().startswith("driver.get(URL)")
            ):
                continue

            # Modificar las líneas que contienen send_keys para usar las variables
            if ".send_keys(" in line:
                css_selector = re.search(
                    r"driver\.find_element\(By\.CSS_SELECTOR,\s*'(.*?)'\)", line
                )

                if css_selector:
                    selector = css_selector.group(1)

                    # Usar el contador para nombrar la variable
                    variable_name = (
                        f"campo{campo_counter}"  # Asegura que empiece desde campo1
                    )

                    # Reemplazo usando la variable
                    replacement = f'driver.find_element(By.CSS_SELECTOR, \'{selector}\').send_keys(variables.get("{variable_name}", ""))'

                    # Aplicar la sustitución correctamente
                    line = re.sub(
                        r"driver\.find_element\(By\.CSS_SELECTOR,\s*'(.*?)'\)\.send_keys\(.*\)",
                        replacement,
                        line,
                    )

                    campo_counter += (
                        1  # Incrementar el contador solo si se procesó una línea
                    )

            # Agregar la línea modificada a updated_content
            updated_content.append(line)

        # Escribir el contenido modificado en el archivo de destino
        with open(dest_file, "w", encoding="utf-8") as file:
            file.write("# -*- coding: utf-8 -*-\n")
            file.write("from configExcel import URL\n")
            file.write("from selenium import webdriver\n")
            file.write("from selenium.webdriver.common.by import By\n")
            file.write(
                "from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException\n"
            )
            file.write("import importlib.util\n")
            file.write("import time\n\n")
            file.write("# Cargar el módulo DataArray dinámicamente\n")
            file.write(
                'spec = importlib.util.spec_from_file_location("DataArray", "DataArray.py")\n'
            )
            file.write("data_array = importlib.util.module_from_spec(spec)\n")
            file.write("spec.loader.exec_module(data_array)\n\n")
            file.write(
                "# Obtener todas las variables definidas en el módulo DataArray\n"
            )
            file.write("variables = data_array.variables\n\n")
            file.write("# Inicializar el WebDriver\n")
            file.write("driver = webdriver.Chrome()\n")
            file.write(
                "driver.implicitly_wait(10)  # Espera implícita de 10 segundos para que los elementos estén disponibles\n"
            )
            file.write("driver.get(URL)\n")
            file.write("driver.maximize_window()\n")
            file.write("# Espera a que la página cargue completamente\n")
            file.write("time.sleep(10)\n\n")
            file.write("# Usar los nombres de campo directamente desde variables\n")
            file.write("try:\n")

            for line in updated_content:
                file.write("    " + line)  # Indentar las líneas

            file.write("except NoSuchElementException:\n")
            file.write('    print("Error: No se encontró uno de los campos.")\n')
            file.write("except ElementNotInteractableException:\n")
            file.write('    print("Error: El elemento no es interactuable.")\n')
            file.write("except TimeoutException:\n")
            file.write(
                """
                print("Error: Tiempo de espera excedido para encontrar el elemento.")\n\n"""
            )
            file.write("# Finalizar el WebDriver\n")
            file.write("time.sleep(30)\n")
            file.write("driver.quit()\n")

        print(f"'{src_file}' ha sido copiado y modificado en '{dest_file}'.")
    else:
        print(f"El archivo '{src_file}' no existe.")


if __name__ == "__main__":
    src_file = "IA_Automation.py"
    dest_file = "Update_Automation.py"
    copy_and_modify_file(src_file, dest_file)
