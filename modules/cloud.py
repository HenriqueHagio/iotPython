# modules/cloud.py
from datetime import datetime

import requests
from iot.config.settings import CLOUD_ENDPOINT

def send_data_to_cloud(motion, light_level):
    data = {
        "timestamp": datetime.now().isoformat(),
        "motion": motion,
        "light_level": light_level
    }
    response = requests.post(CLOUD_ENDPOINT, json=data)
    if response.status_code == 200:
        print("Dados enviados para a nuvem com sucesso.")
    else:
        print("Falha ao enviar dados para a nuvem.")
