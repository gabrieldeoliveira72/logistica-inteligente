import pandas as pd
import numpy as np

def load_locations(filepath='data/locations.csv'):
    """Carrega as coordenadas de localizações a partir de um CSV"""
    try:
        df = pd.read_csv(filepath)
        locations = [(row['x'], row['y']) for _, row in df.iterrows()]
        return locations
    except FileNotFoundError:
        print(f"Arquivo {filepath} não encontrado. Gerando localizações aleatórias.")
        # Gera 10 localizações aleatórias em um espaço 2D 100x100
        np.random.seed(42)  # Para reprodutibilidade
        return [(50, 50)] + [(int(x), int(y)) for x, y in np.random.rand(10, 2) * 100]

def load_traffic_data(filepath='data/traffic_data.csv'):
    """Carrega dados de tráfego de um CSV"""
    try:
        df = pd.read_csv(filepath)
        traffic_data = {f"{row['from_id']}-{row['to_id']}": row['traffic_factor'] for _, row in df.iterrows()}
        return traffic_data
    except FileNotFoundError:
        print(f"Arquivo {filepath} não encontrado. Usando dados de tráfego padrão.")
        # Retorna alguns dados de tráfego padrão
        return {
            "0-1": 1.2, "1-2": 1.0, "2-3": 1.5, "3-4": 1.3,
            "4-5": 1.1, "5-6": 1.8, "6-7": 1.4, "7-8": 1.0,
            "8-9": 1.2, "9-10": 1.6
        }

def load_driver_data(filepath='data/driver_data.csv'):
    """Carrega dados do motorista de um CSV"""
    try:
        df = pd.read_csv(filepath)
        # Pega o último registro como o estado atual do motorista
        last_row = df.iloc[-1]
        driver_data = {
            "driving_hours": last_row['driving_hours'],
            "blink_rate": last_row['blink_rate'],
            "steering_adjustments": last_row['steering_adjustments'],
            "current_fatigue": last_row['current_fatigue'],
            "current_time": last_row['timestamp'].split()[1][:5]  # Extrai apenas o horário
        }
        return driver_data
    except (FileNotFoundError, IndexError):
        print(f"Arquivo {filepath} não encontrado ou vazio. Usando dados padrão do motorista.")
        return {
            "driving_hours": 4.5,
            "blink_rate": 0.5,
            "steering_adjustments": 0.6,
            "current_fatigue": 0.45,
            "current_time": "14:30"
        }
