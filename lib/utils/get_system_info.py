import platform
import os


def get_system_info():
    print(f"ℹ️ Processando os dados utilizando as seguintes especificações:")
    print(f"🖥️ OS: {platform.platform()}")
    print(f"💽 Processador: {platform.processor() or "N/A"}")
    print(f"⚙️ Quantidade de núcleos: {os.cpu_count()}")
    print(f"⚙️ Arquitetura: {platform.machine()}")
