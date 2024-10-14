import subprocess

# Ejecutar el script Automatizacion.py
try:
    print("Ejecutando Automatizacion.py...")
    subprocess.run(["python", "Automatizacion.py"], check=True)
    print("Automatizacion.py ejecutado con éxito.")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar Automatizacion.py: {e}")
    exit(1)

# Ejecutar el script Actualizacion.py
try:
    print("Ejecutando Actualizacion.py...")
    subprocess.run(["python", "Actualizacion.py"], check=True)
    print("Actualizacion.py ejecutado con éxito.")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar Actualizacion.py: {e}")
    exit(1)

# Ejecutar el script Update_Automation.py
try:
    print("Ejecutando Update_Automation.py...")
    subprocess.run(["python", "Update_Automation.py"], check=True)
    print("Update_Automation.py ejecutado con éxito.")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar Update_Automation.py: {e}")
    exit(1)

print("Secuencia de scripts completada.")
