import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

from models.route_optimizer import RouteOptimizer
from models.fatigue_detector import FatigueDetector
from utils.data_loader import load_locations, load_traffic_data, load_driver_data

def main():
    print("Sistema Inteligente de Otimização de Rotas com Monitoramento do Motorista")
    print("=" * 70)
    
    os.makedirs('outputs', exist_ok=True)
    
    print("\nCarregando dados...")
    locations = load_locations()
    traffic_data = load_traffic_data()
    driver_data = load_driver_data()
    
    print("\n[1] Demonstração do Detector de Fadiga")
    print("-" * 50)
    
    fatigue_detector = FatigueDetector()
    fatigue_scores = fatigue_detector.simulate_fatigue_over_time(hours=10, starting_time="06:00")
    
    print("Simulação de fadiga ao longo de 10 horas de direção:")
    print(f"Fadiga inicial: {fatigue_scores[0]:.2f} (nível baixo)")
    print(f"Fadiga após 5 horas: {fatigue_scores[10]:.2f}")
    print(f"Fadiga após 10 horas: {fatigue_scores[-1]:.2f} (nível crítico)")
    print(f"Imagem da simulação salva em 'outputs/fatigue_simulation.png'")
    
    print("\n[2] Demonstração da Otimização de Rota")
    print("-" * 50)
    
    current_driver_state = {"fatigue_level": driver_data["current_fatigue"]}
    
    optimizer = RouteOptimizer(locations, traffic_data, current_driver_state)
    
    print("Executando algoritmo genético para otimização de rota...")
    best_route, _ = optimizer.optimize(generations=30, population_size=50)
    
    print(f"Rota otimizada: {best_route}")
    optimizer.visualize_route(best_route)
    print(f"Visualização da rota salva em 'outputs/route_visualization.png'")
    
    rest_stops = optimizer.recommend_rest_stops(best_route)
    if rest_stops:
        print(f"Pontos de parada recomendados: {rest_stops}")
    
    print("\n[3] Análise de uma situação completa")
    print("-" * 50)
    
    current_time = "14:30"
    hours_driven = 4.5
    
    driver_status = {
        'driving_hours': hours_driven,
        'blink_rate': 0.65,
        'steering_adjustments': 0.7,
        'current_time': current_time
    }
    
    fatigue_result = fatigue_detector.detect_fatigue(driver_status)
    
    print(f"Status do motorista às {current_time} após {hours_driven} horas dirigindo:")
    print(f"Nível de fadiga: {fatigue_result['fatigue_level']} ({fatigue_result['fatigue_score']:.2f})")
    
    if fatigue_result['needs_rest']:
        print("ALERTA: Recomendado fazer uma pausa!")
        
        driver_state = {"fatigue_level": fatigue_result['fatigue_score']}
        new_optimizer = RouteOptimizer(locations, traffic_data, driver_state)
        new_route, _ = new_optimizer.optimize()
        
        print("Rota recalculada considerando necessidade de descanso.")
        new_optimizer.visualize_route(new_route)
        print("Nova visualização salva em 'outputs/route_visualization.png'")
    else:
        print("Motorista em condições adequadas para continuar.")
    
    print("\nDemonstração concluída!")

if __name__ == "__main__":
    main()
