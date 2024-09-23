from Data import Data_excel  # Importa la función de lectura de Excel
from configExcel import file_path  # Importa el archivo de configuración


# Función para consultar datos de una fila y columna específica
def get_data_from_excel(data_dict, row_index, col_index):
    if row_index not in data_dict:
        print(f"No se encontraron datos para la fila {row_index}")
        return None

    row_data = data_dict[row_index]  # Obtener los datos de la fila

    if col_index >= len(
        row_data
    ):  # Verificar si la columna solicitada existe en la fila
        print(f"No se encontraron datos para la columna {col_index}")
        return None

    return row_data[col_index]  # Retorna el valor de la columna especificada


# Leer los datos del Excel
file_path2 = file_path  # Obtener el file_path desde el archivo de configuración
data = Data_excel(file_path2)

# Variables para la fila y columna a consultar
row_index = 3  # Cambia el índice de la fila según sea necesario (comienza en 2 si la primera fila tiene encabezados)
col_indices = {"campo1": 0, "campo2": 1}

# Exportar las variables en un diccionario
variables = {
    name: get_data_from_excel(data, row_index, idx) for name, idx in col_indices.items()
}

# Puedes agregar más variables dinámicamente si es necesario
# variables['nueva_variable'] = get_data_from_excel(data, row_index, new_idx)

# Exportar el diccionario de variables
if __name__ == "__main__":
    import json

    print(json.dumps(variables, indent=4))  # Verifica el contenido de variables
