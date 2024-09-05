import math


def __countdown(n):
    while n > 0:
        n -= 1
    return n


def process_row(row: list[str]):
    # Processa apenas as colunas "HeartRate" e "RespirationRate"
    try:
        heart_rate = int(row[2])  # Coluna "HeartRate"
        respiration_rate = float(row[3])  # Coluna "RespirationRate"

    except ValueError:
        return 0
    return __countdown(heart_rate**2 + 0.3*respiration_rate + 1)
