import csv
import time
from utils.get_system_info import get_system_info

import config
from process_row import process_row


def process_csv(file_name: str):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pula o cabeçalho
        result = []
        for row in reader:
            result.append(process_row(row))

    return result


if __name__ == "__main__":
    get_system_info()

    start_time = time.time()
    result = process_csv(config.sleep_data_file)
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"Processamento com paralelismo concluído em {
          int(minutes)} minutos e {seconds:.2f} segundos.")
