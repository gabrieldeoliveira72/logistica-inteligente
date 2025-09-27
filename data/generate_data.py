import os
import json

# Cria a pasta data caso não exista
os.makedirs('data', exist_ok=True)

# Dados simulados de exemplo
clientes = [
    {"id": 1, "nome": "Cliente A", "lat": -23.5505, "lon": -46.6333},
    {"id": 2, "nome": "Cliente B", "lat": -23.5489, "lon": -46.6388},
    {"id": 3, "nome": "Cliente C", "lat": -23.5505, "lon": -46.6290},
    {"id": 4, "nome": "Cliente D", "lat": -23.5587, "lon": -46.6358},
    {"id": 5, "nome": "Cliente E", "lat": -23.5465, "lon": -46.6401},
]

rotas = [
    {"origem": 1, "destino": 2, "distancia": 5.2},
    {"origem": 2, "destino": 3, "distancia": 7.8},
    {"origem": 3, "destino": 4, "distancia": 3.5},
    {"origem": 4, "destino": 5, "distancia": 6.2},
    {"origem": 5, "destino": 1, "distancia": 8.1}
]

# Salvar dados de clientes como JSON
with open('data/clientes.json', 'w') as f:
    json.dump(clientes, f, indent=4)
    print("Arquivo clientes.json criado com sucesso!")

# Salvar dados de rotas como JSON
with open('data/rotas.json', 'w') as f:
    json.dump(rotas, f, indent=4)
    print("Arquivo rotas.json criado com sucesso!")

# Criar os arquivos CSV para o projeto
# Arquivo locations.csv
with open('data/locations.csv', 'w') as f:
    f.write("id,name,x,y\n")
    f.write("0,Depósito,50,50\n")
    f.write("1,Cliente A,20,30\n")
    f.write("2,Cliente B,35,15\n")
    f.write("3,Cliente C,70,40\n")
    f.write("4,Cliente D,85,70\n")
    f.write("5,Cliente E,65,25\n")
    f.write("6,Cliente F,25,60\n")
    f.write("7,Cliente G,45,80\n")
    f.write("8,Cliente H,90,45\n")
    f.write("9,Cliente I,10,75\n")
    f.write("10,Cliente J,60,55\n")
    print("Arquivo locations.csv criado com sucesso!")

# Arquivo traffic_data.csv
with open('data/traffic_data.csv', 'w') as f:
    f.write("segment_id,from_id,to_id,traffic_factor,time_of_day\n")
    f.write("1,0,1,1.2,morning\n")
    f.write("2,0,2,1.0,morning\n")
    f.write("3,1,3,1.5,afternoon\n")
    f.write("4,2,4,1.3,afternoon\n")
    f.write("5,3,5,1.1,evening\n")
    f.write("6,4,6,1.8,evening\n")
    f.write("7,5,7,1.4,night\n")
    f.write("8,6,8,1.0,night\n")
    f.write("9,7,9,1.2,morning\n")
    f.write("10,8,10,1.6,afternoon\n")
    print("Arquivo traffic_data.csv criado com sucesso!")

# Arquivo driver_data.csv
with open('data/driver_data.csv', 'w') as f:
    f.write("id,timestamp,driving_hours,blink_rate,steering_adjustments,current_fatigue\n")
    f.write("1,2023-09-26 08:00:00,0.0,0.2,0.1,0.1\n")
    f.write("1,2023-09-26 10:30:00,2.5,0.3,0.25,0.25\n")
    f.write("1,2023-09-26 12:45:00,4.75,0.5,0.4,0.45\n")
    f.write("1,2023-09-26 14:30:00,6.5,0.65,0.7,0.6\n")
    f.write("1,2023-09-26 16:15:00,8.25,0.75,0.8,0.75\n")
    f.write("1,2023-09-26 18:00:00,10.0,0.85,0.9,0.9\n")
    print("Arquivo driver_data.csv criado com sucesso!")

print("Todos os dados foram gerados com sucesso!")
