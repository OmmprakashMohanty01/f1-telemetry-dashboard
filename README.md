# F1 Telemetry Dashboard 🏎️📊

A comprehensive data analytics tool that fetches, processes, and visualizes Formula 1 race telemetry. This project demonstrates proficiency in interacting with external APIs, handling complex JSON data, and building modular Python applications.

## 🚀 Features

- **Live Data Ingestion (`redbull_api_client.py`)**: Connects to F1 telemetry APIs to retrieve real-time and historical race data.
- **Lap Delta Analysis (`lap_delta_calculator.py`)**: Computes sector-by-sector time differences to evaluate driver performance visually.
- **Tire Strategy Modeler (`tire_strategy.py`)**: Analyzes tire degradation patterns to predict optimal pit window strategies.

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Key Libraries:** `requests`, `logging`, `json`
- **Architecture:** Object-Oriented API Client Design

## 💻 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OmmprakashMohanty01/f1-telemetry-dashboard.git
   cd f1-telemetry-dashboard
   ```
2. **Install dependencies (if applicable):**
   ```bash
   pip install requests
   ```
3. **Execute the analysis:**
   *(Run the relevant script, e.g., to test the API client)*
   ```bash
   python3 redbull_api_client.py
   ```