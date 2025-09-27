import numpy as np
from deap import base, creator, tools, algorithms
import random
import matplotlib.pyplot as plt

class RouteOptimizer:
    def __init__(self, locations, traffic_data=None, driver_state=None):
        self.locations = locations
        self.traffic_data = traffic_data or {}
        self.driver_state = driver_state or {"fatigue_level": 0}
        self.setup_genetic_algorithm()
        
    def setup_genetic_algorithm(self):
        if not hasattr(creator, "FitnessMin"):
            creator.create("FitnessMin", base.Fitness, weights=(-1.0, -0.5))
        if not hasattr(creator, "Individual"):
            creator.create("Individual", list, fitness=creator.FitnessMin)
        
        self.toolbox = base.Toolbox()
        self.toolbox.register("indices", random.sample, range(1, len(self.locations)), len(self.locations)-1)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.indices)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", self.evaluate_route)
        self.toolbox.register("mate", self._custom_crossover)
        self.toolbox.register("mutate", self._custom_mutation)
        self.toolbox.register("select", tools.selTournament, tournsize=3)
    
    def calculate_distance(self, point1, point2):
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def evaluate_route(self, individual):
        route = [0] + individual + [0]
        
        total_distance = 0
        fatigue_impact = 0
        
        for i in range(len(route) - 1):
            from_loc = self.locations[route[i]]
            to_loc = self.locations[route[i+1]]
            
            segment_distance = self.calculate_distance(from_loc, to_loc)
            
            segment_key = f"{route[i]}-{route[i+1]}"
            traffic_factor = self.traffic_data.get(segment_key, 1.0)
            
            adjusted_distance = segment_distance * traffic_factor
            
            current_fatigue = self.driver_state.get("fatigue_level", 0) + (adjusted_distance * 0.1)
            fatigue_impact += current_fatigue
            
            total_distance += adjusted_distance
        
        return total_distance, fatigue_impact
    
    def _custom_crossover(self, ind1, ind2):
        """Crossover simples que troca segmentos das rotas"""
        if len(ind1) < 2 or len(ind2) < 2:
            return ind1, ind2
        
        point = random.randint(1, min(len(ind1), len(ind2)) - 1)
        
        new_ind1 = creator.Individual(ind1[:point] + ind2[point:])
        new_ind2 = creator.Individual(ind2[:point] + ind1[point:])
        
        return new_ind1, new_ind2
    
    def _custom_mutation(self, individual):
        """Mutação que troca duas posições aleatórias"""
        if len(individual) < 2:
            return individual,
        
        pos1, pos2 = random.sample(range(len(individual)), 2)
        
        individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
        
        return individual,
    
    def optimize(self, generations=50, population_size=50):
        pop = self.toolbox.population(n=population_size)
        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", np.mean, axis=0)
        stats.register("min", np.min, axis=0)
        
        pop, logbook = algorithms.eaSimple(pop, self.toolbox, 
                                           cxpb=0.7, mutpb=0.2, 
                                           ngen=generations, 
                                           stats=stats, halloffame=hof, 
                                           verbose=True)
        
        best_route = [0] + list(hof[0]) + [0]
        return best_route, logbook
        
    def visualize_route(self, route):
        route_x = [self.locations[i][0] for i in route]
        route_y = [self.locations[i][1] for i in route]
        
        plt.figure(figsize=(10, 6))
        plt.scatter([loc[0] for loc in self.locations], [loc[1] for loc in self.locations], c='blue')
        plt.plot(route_x, route_y, 'r-')
        plt.scatter(self.locations[0][0], self.locations[0][1], c='green', s=100, marker='s')
        
        rest_stops = self.recommend_rest_stops(route)
        if rest_stops:
            rest_x = [self.locations[i][0] for i in rest_stops]
            rest_y = [self.locations[i][1] for i in rest_stops]
            plt.scatter(rest_x, rest_y, c='orange', s=80, marker='^')
            
        plt.title('Rota Otimizada com Pontos de Parada')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        
        import os
        os.makedirs('outputs', exist_ok=True)
        
        plt.savefig('outputs/route_visualization.png')
        plt.close()
        
    def recommend_rest_stops(self, route):
        rest_stops = []
        accumulated_fatigue = 0
        
        for i in range(len(route) - 1):
            from_loc = self.locations[route[i]]
            to_loc = self.locations[route[i+1]]
            
            segment_distance = self.calculate_distance(from_loc, to_loc)
            accumulated_fatigue += segment_distance * 0.1
            
            if accumulated_fatigue > 1.5:
                rest_stops.append(route[i])
                accumulated_fatigue = 0
                
        return rest_stops
