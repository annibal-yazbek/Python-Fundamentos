# checando parâmetros de Sistema Operacional
import shutil
import psutil

cpuUse = psutil.cpu_percent(interval=1)
ramUse = psutil.virtual_memory().percent    
diskUse = psutil.disk_usage('/').percent
diskFree = shutil.disk_usage('/').free / (2**30)  # Convertendo para GB
diskTotal = shutil.disk_usage('/').total / (2**30)  # Convertendo para GB   
print(f"Uso de CPU: {cpuUse}%")
print(f"Uso de RAM: {ramUse}%")
print(f"Uso de Disco: {diskUse}%")          
print(f"Espaço livre em Disco: {diskFree:.2f} GB")
print(f"Espaço total em Disco: {diskTotal:.2f} GB")

