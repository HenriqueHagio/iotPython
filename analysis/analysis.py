# analysis/analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_data():
    df = pd.read_csv('data/sensor_data.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='light_level', data=df, label='Light Level')
    sns.scatterplot(x='timestamp', y='motion', data=df, label='Motion')

    plt.title('Sensor Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Sensor Values')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    analyze_data()
