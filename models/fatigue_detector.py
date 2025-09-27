import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class FatigueDetector:
    def __init__(self):
        self.fatigue_thresholds = {
            'low': 0.3,
            'medium': 0.6,
            'high': 0.8
        }
    
    def detect_fatigue(self, driver_data):
        """
        Detecta nível de fadiga baseado em diferentes indicadores
        driver_data: dicionário com informações como horas_dirigindo, piscar_olhos, etc.
        """
        driving_hours = min(driver_data.get('driving_hours', 0) / 8, 1.0)
        blink_rate = driver_data.get('blink_rate', 0.5)
        steering_adjustments = driver_data.get('steering_adjustments', 0.5)
        time_of_day = self._time_factor(driver_data.get('current_time'))
        
        fatigue_score = (
            driving_hours * 0.4 +
            blink_rate * 0.25 +
            steering_adjustments * 0.25 +
            time_of_day * 0.1
        )
        
        fatigue_level = self._get_fatigue_level(fatigue_score)
        
        return {
            'fatigue_score': fatigue_score,
            'fatigue_level': fatigue_level,
            'needs_rest': fatigue_score > self.fatigue_thresholds['medium'],
            'critical': fatigue_score > self.fatigue_thresholds['high']
        }
    
    def _time_factor(self, current_time=None):
        """Calcula fator de fadiga baseado na hora do dia (maior durante a madrugada)"""
        if current_time is None:
            current_time = datetime.now()
        elif isinstance(current_time, str):
            try:
                current_time = datetime.strptime(current_time, "%H:%M")
            except ValueError:
                current_time = datetime.now()
            
        hour = current_time.hour
        
        if 2 <= hour < 5:
            return 1.0
        elif 13 <= hour < 15:
            return 0.7
        elif (8 <= hour < 11) or (16 <= hour < 18):
            return 0.2
        else:
            return 0.5
    
    def _get_fatigue_level(self, score):
        """Converte score numérico para nível categórico de fadiga"""
        if score < self.fatigue_thresholds['low']:
            return "baixo"
        elif score < self.fatigue_thresholds['medium']:
            return "moderado"
        elif score < self.fatigue_thresholds['high']:
            return "alto"
        else:
            return "crítico"
    
    def simulate_fatigue_over_time(self, hours=10, starting_time="08:00"):
        """Simula a evolução da fadiga ao longo de uma jornada"""
        start_time = datetime.strptime(starting_time, "%H:%M")
        times = [(start_time + timedelta(minutes=30*i)).strftime("%H:%M") for i in range(hours*2)]
        
        fatigue_scores = []
        for i, time_str in enumerate(times):
            hours_driven = i/2
            blink_rate = min(0.3 + (hours_driven * 0.05), 0.9)
            steering = min(0.3 + (hours_driven * 0.06), 0.95)
            
            driver_data = {
                'driving_hours': hours_driven,
                'blink_rate': blink_rate,
                'steering_adjustments': steering,
                'current_time': time_str
            }
            
            result = self.detect_fatigue(driver_data)
            fatigue_scores.append(result['fatigue_score'])
        
        plt.figure(figsize=(10, 5))
        plt.plot(times[::2], fatigue_scores[::2], 'o-', label='Nível de Fadiga')
        plt.axhline(y=self.fatigue_thresholds['low'], color='g', linestyle='-', label='Baixo')
        plt.axhline(y=self.fatigue_thresholds['medium'], color='y', linestyle='-', label='Moderado')
        plt.axhline(y=self.fatigue_thresholds['high'], color='r', linestyle='-', label='Crítico')
        
        plt.title('Simulação de Fadiga Durante a Jornada')
        plt.xlabel('Hora do Dia')
        plt.ylabel('Nível de Fadiga')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        import os
        os.makedirs('outputs', exist_ok=True)
        
        plt.savefig('outputs/fatigue_simulation.png')
        plt.close()
        
        return fatigue_scores
