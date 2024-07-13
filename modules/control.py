# modules/control.py

from time import sleep
from iot.config.settings import LUMINOSITY_THRESHOLD
from iot.modules.sensor import get_sensor_data
from iot.modules.data_logger import log_data
from iot.modules.cloud import send_data_to_cloud


def control_light():
    while True:
        motion, light_level = get_sensor_data()
        log_data(motion, light_level)
        send_data_to_cloud(motion, light_level)

        if motion:
            print("Movimento detectado!")
            if light_level < LUMINOSITY_THRESHOLD:
                print("Luz acesa (simulada).")
            else:
                print("Ambiente já está claro (simulado).")
        else:
            print("Sem movimento, luz apagada (simulada).")

        sleep(1)
