# Sistema Inteligente de Otimização de Rotas com Monitoramento do Motorista

## 📋 Descrição

Este projeto implementa um sistema inteligente que combina **otimização de rotas** com **detecção de fadiga do motorista** para melhorar a segurança e eficiência no transporte. O sistema utiliza algoritmos genéticos para otimizar rotas e monitora indicadores de fadiga em tempo real.

## 🚀 Funcionalidades

- **Detecção de Fadiga**: Monitora indicadores como horas dirigindo, taxa de piscar de olhos e ajustes no volante
- **Otimização de Rotas**: Utiliza algoritmo genético para encontrar a melhor rota considerando tráfego e fadiga
- **Recomendação de Paradas**: Sugere pontos de descanso baseados no nível de fadiga
- **Visualização**: Gera gráficos de evolução da fadiga e mapas das rotas otimizadas
- **Análise em Tempo Real**: Simula situações reais de direção e ajusta rotas dinamicamente

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **NumPy** - Cálculos matemáticos
- **Pandas** - Manipulação de dados
- **Matplotlib** - Visualizações
- **DEAP** - Algoritmos genéticos
- **Folium** - Mapas interativos

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/logistica-inteligente.git
cd logistica-inteligente
```

2. **Crie um ambiente virtual:**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual:**
```bash
# No Windows:
.venv\Scripts\activate

# No macOS/Linux:
source .venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. **Ative o ambiente virtual:**
```bash
source .venv/bin/activate
```

2. **Execute o programa:**
```bash
python app.py
```

## 📊 Exemplo de Saída

```
Sistema Inteligente de Otimização de Rotas com Monitoramento do Motorista
======================================================================

Carregando dados...

[1] Demonstração do Detector de Fadiga
--------------------------------------------------
Simulação de fadiga ao longo de 10 horas de direção:
Fadiga inicial: 0.20 (nível baixo)
Fadiga após 5 horas: 0.59
Fadiga após 10 horas: 0.86 (nível crítico)
Imagem da simulação salva em 'outputs/fatigue_simulation.png'

[2] Demonstração da Otimização de Rota
--------------------------------------------------
Executando algoritmo genético para otimização de rota...
gen     nevals  avg                             min                        
0       50      [496.35  59.53]     [396.26  49.52]
1       43      [460.54  55.95]     [376.64  47.56]
...
Rota otimizada: [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]
Visualização da rota salva em 'outputs/route_visualization.png'
Pontos de parada recomendados: [0, 3]

[3] Análise de uma situação completa
--------------------------------------------------
Status do motorista às 14:30 após 4.5 horas dirigindo:
Nível de fadiga: alto (0.63)
ALERTA: Recomendado fazer uma pausa!
Rota recalculada considerando necessidade de descanso.
Nova visualização salva em 'outputs/route_visualization.png'

Demonstração concluída!
```

## 📁 Estrutura do Projeto

```
logistica-inteligente/
├── app.py                          # Arquivo principal
├── models/
│   ├── route_optimizer.py          # Otimizador de rotas
│   └── fatigue_detector.py         # Detector de fadiga
├── utils/
│   └── data_loader.py              # Carregador de dados
├── data/
│   ├── locations.csv               # Coordenadas dos pontos
│   ├── traffic_data.csv            # Dados de tráfego
│   ├── driver_data.csv             # Dados do motorista
│   ├── clientes.json               # Dados dos clientes
│   └── rotas.json                  # Dados das rotas
├── outputs/                        # Imagens geradas
├── requirements.txt                # Dependências
└── README.md                       # Este arquivo
```

## 🔧 Configuração

### Personalizando os Dados

1. **Localizações**: Edite `data/locations.csv` para adicionar novos pontos
2. **Tráfego**: Modifique `data/traffic_data.csv` para ajustar fatores de tráfego
3. **Motorista**: Altere `data/driver_data.csv` para simular diferentes estados

### Parâmetros do Algoritmo Genético

No arquivo `models/route_optimizer.py`, você pode ajustar:
- `generations`: Número de gerações (padrão: 50)
- `population_size`: Tamanho da população (padrão: 50)
- `cxpb`: Probabilidade de crossover (padrão: 0.7)
- `mutpb`: Probabilidade de mutação (padrão: 0.2)

## 📈 Resultados

O sistema gera duas visualizações principais:

1. **`outputs/fatigue_simulation.png`**: Gráfico da evolução da fadiga ao longo do tempo
2. **`outputs/route_visualization.png`**: Mapa da rota otimizada com pontos de parada

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request


## 👨‍💻 Autor

**Seu Nome**
- GitHub: [gabrieldeoliveira72](https://github.com/gabrieldeoliveira72)



