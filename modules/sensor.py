# modules/sensor.py

import random

def get_sensor_data():
    motion = random.choice([True, False])
    light_level = random.uniform(0, 1)
    return motion, light_level
