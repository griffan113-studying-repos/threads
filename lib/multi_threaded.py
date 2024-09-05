import csv
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Process, Pool
import config
from process_row import process_row

# Função para processar um chunk do CSV
def process_chunk(rows):
    result = []
    for row in rows:
        result.append(process_row(row))
    return result

def process_csv_parallel(file_name: str, chunk_size: int = 150000):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pula o cabeçalho
        rows = list(reader)

    # Dividindo o arquivo em chunks
    chunks = [rows[i:i + chunk_size] for i in range(0, len(rows), chunk_size)]

    result = []
    # Usando o pool de processos para paralelizar o processamento
    # with ProcessPoolExecutor() as executor:
    #     futures = [executor.submit(process_chunk, chunk) for chunk in chunks]
    #     for future in as_completed(futures):
    #         result.extend(future.result())

    with Pool() as pool:
        for chunk in chunks:
          result = pool.map(process_chunk, chunk)

    return result

if __name__ == "__main__":
    start_time = time.time()
    result = process_csv_parallel(config.sleep_data_file)
    print(f"Processamento com paralelismo concluído em {time.time() - start_time:.2f} segundos.")
