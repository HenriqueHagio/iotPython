# modules/data_logger.py

import csv
import os
from datetime import datetime


def log_data(motion, light_level):
    file_path = 'data/sensor_data.csv'

    # Verifica se o arquivo já existe
    file_exists = os.path.isfile(file_path)

    # Abre o arquivo no modo de anexação
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)

        # Escreve o cabeçalho se o arquivo for criado pela primeira vez
        if not file_exists:
            writer.writerow(['timestamp', 'motion', 'light_level'])

        # Escreve os dados dos sensores
        writer.writerow([datetime.now(), motion, light_level])
