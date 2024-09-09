import csv
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

import config
from process_row import process_row


# Função para processar um chunk do CSV
def process_chunk(chunk):
    result = []
    for row in chunk:
        result.append(process_row(row))
    return result


def process_csv_parallel(file_name: str, chunk_size: int = 150000):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pula o cabeçalho
        rows = list(reader)

        # Dividindo o arquivo em chunks
        chunks = [rows[i:i + chunk_size]
                  for i in range(0, len(rows), chunk_size)]

        result = []

        # Usando ProcessPoolExecutor para executar os chunks em paralelo
        with ProcessPoolExecutor() as executor:
            # Submetendo os chunks para processamento paralelo
            futures = [executor.submit(process_chunk, chunk)
                       for chunk in chunks]

            # Aguardando a conclusão das tarefas e coletando os resultados
            for future in as_completed(futures):
                result.extend(future.result())

    return result


if __name__ == "__main__":
    start_time = time.time()
    result = process_csv_parallel(config.sleep_data_file)
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"Processamento com paralelismo concluído em {
          int(minutes)} minutos e {seconds:.2f} segundos.")
