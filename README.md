# 🚚 Logística Inteligente

> **Sistema Python que combina algoritmos genéticos para otimização de rotas de entrega com monitoramento em tempo real do nível de fadiga do motorista — melhorando segurança e eficiência operacional no transporte.**

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.20+-013243?style=flat&logo=numpy&logoColor=white)
![DEAP](https://img.shields.io/badge/DEAP-Algoritmos_Genéticos-green?style=flat)
![Folium](https://img.shields.io/badge/Folium-Mapas_Interativos-77B829?style=flat)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizações-11557C?style=flat)
![Status](https://img.shields.io/badge/Status-Funcional-brightgreen?style=flat)

---

## 🎯 Problema Resolvido

Empresas de logística sofrem com dois problemas críticos e interligados: **rotas ineficientes** que desperdiçam combustível e tempo, e **acidentes causados por fadiga do motorista** — responsável por 30% dos acidentes graves de trânsito segundo o DENATRAN. Este sistema resolve ambos simultaneamente: otimiza a rota *e* monitora o estado do motorista, sugerindo paradas antes que a fadiga se torne perigosa.

---

## 🏗️ Arquitetura

```
┌──────────────────────────────────────────────────────────┐
│                    ENTRADAS DE DADOS                      │
│  utils/data_loader.py                                     │
│  Localidades  |  Dados de Tráfego  |  Dados do Motorista  │
└──────────┬───────────────┬──────────────────────────────┘
           │               │
           ▼               ▼
┌─────────────────┐  ┌───────────────────────────────────┐
│  OTIMIZADOR     │  │  DETECTOR DE FADIGA                │
│  DE ROTAS       │  │  models/fatigue_detector.py        │
│  models/        │  │                                    │
│  route_         │  │  Indicadores:                      │
│  optimizer.py   │  │  - Horas ao volante                │
│                 │  │  - Taxa de piscar de olhos         │
│  Algoritmo      │  │  - Correções no volante            │
│  Genético       │  │  → Score de fadiga (0.0–1.0)       │
│  (DEAP)         │  └─────────────┬─────────────────────┘
└────────┬────────┘                │
         │         ┌───────────────┘
         └─────────▼
┌──────────────────────────────────────────────────────────┐
│                   ENGINE PRINCIPAL (app.py)               │
│  Rota Ótima + Fadiga → Recomendação de Paradas           │
└──────────────────────┬───────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────┐
│                     SAÍDAS (outputs/)                     │
│  Gráfico de evolução da fadiga  |  Mapa de rota (HTML)   │
│  Matplotlib                     |  Folium                 │
└──────────────────────────────────────────────────────────┘
```

### Decisões Técnicas

| Decisão | Escolha | Justificativa |
|---|---|---|
| Otimização de rotas | **Algoritmo Genético (DEAP)** | Superior ao brute-force para problemas NP-difíceis como TSP |
| Modelo de fadiga | **Score composto multiindicador** | Mais robusto que monitorar apenas horas ao volante |
| Visualização de rotas | **Folium** | Mapas interativos em HTML, sem dependência de servidor |
| Processamento numérico | **NumPy + Pandas** | Performance em operações matriciais para cálculo de distâncias |
| Estrutura modular | `models/` + `utils/` separados | Facilita substituição de modelos sem alterar lógica principal |

---

## 📁 Estrutura do Projeto

```
logistica-inteligente/
├── models/
│   ├── __init__.py
│   ├── fatigue_detector.py     # Modelo de detecção e simulação de fadiga
│   └── route_optimizer.py      # Algoritmo genético para otimização de rotas
├── utils/
│   └── data_loader.py          # Carregamento de localidades, tráfego e motoristas
├── data/                       # Dados de entrada (localidades, grafos de rotas)
├── outputs/                    # Gráficos e mapas gerados automaticamente
├── app.py                      # Ponto de entrada principal
├── requirements.txt
└── README.md
```

---

## ⚙️ Pré-requisitos

- **Python 3.8+** (desenvolvido com Python 3.13)
- **pip** para gerenciamento de pacotes

---

## 🚀 Como Rodar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/gabrieldeoliveira72/logistica-inteligente.git
cd logistica-inteligente
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# macOS/Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o sistema

```bash
python app.py
```

---

## 📊 Exemplo de Saída

```
Sistema Inteligente de Otimização de Rotas com Monitoramento do Motorista
======================================================================

Carregando dados...

[1] Demonstração do Detector de Fadiga
--------------------------------------------------
Simulação de fadiga ao longo de 10 horas de direção:
  Fadiga inicial:        0.05 (nível baixo — seguro)
  Fadiga após 5 horas:   0.52 (nível moderado — atenção)
  Fadiga após 10 horas:  0.91 (nível crítico — PARAR!)
  → Imagem salva em: outputs/fatigue_simulation.png

[2] Otimização de Rotas com Algoritmo Genético
--------------------------------------------------
  Número de pontos de entrega: 12
  Distância sem otimização:    347.4 km
  Distância otimizada:         218.6 km
  Redução:                     37.1%
  → Mapa interativo salvo em: outputs/route_map.html

[3] Integração: Rota Adaptada ao Estado do Motorista
--------------------------------------------------
  Km rodados: 180 km  |  Fadiga detectada: 0.61
  ⚠️  ALERTA: Recomenda-se pausa de 20 minutos.
  → Ponto de descanso sugerido: Posto BR km 214
```

---

## 📦 Dependências

| Pacote | Versão | Uso |
|---|---|---|
| `numpy` | ≥ 1.20.0 | Cálculos de distância e matrizes |
| `pandas` | ≥ 1.4.0 | Manipulação de dados dos motoristas |
| `matplotlib` | ≥ 3.5.0 | Gráficos de evolução de fadiga |
| `deap` | ≥ 1.3.1 | Framework para algoritmos genéticos |
| `folium` | ≥ 0.12.0 | Mapas interativos em HTML |

---

## 🔮 Melhorias Futuras

- [ ] **API REST** — Expor o sistema via FastAPI para integração com sistemas de frota existentes
- [ ] **Dados reais de GPS** — Integração com telemetria de veículos (OBD-II ou APIs de frota)
- [ ] **Monitoramento por câmera** — Detecção de fadiga via visão computacional (OpenCV + MediaPipe)
- [ ] **Dashboard web em tempo real** — Painel com mapa ao vivo e alertas por WebSocket
- [ ] **Multi-veículo** — Otimização simultânea de frotas com múltiplos motoristas (CVRP)
- [ ] **Dados de tráfego real** — Integração com Google Maps API ou OSRM para tráfego em tempo real
- [ ] **Testes unitários** — Cobertura dos modelos `fatigue_detector` e `route_optimizer`
- [ ] **Containerização** — Dockerfile para execução padronizada em qualquer ambiente

---

## 👨‍💻 Autor

**Gabriel de Oliveira**
[![GitHub](https://img.shields.io/badge/GitHub-gabrieldeoliveira72-181717?style=flat&logo=github)](https://github.com/gabrieldeoliveira72)
