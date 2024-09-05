import csv
import time

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
    start_time = time.time()
    result = process_csv(config.sleep_data_file)
    print(f"Processamento sem multithreading concluído em {time.time() - start_time:.2f} segundos.")
