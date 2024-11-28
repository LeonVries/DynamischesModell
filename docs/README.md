```markdown
# Market Simulation Project Documentation

## Overview

This project implements a market simulation model featuring companies with configurable pricing strategies. The simulation allows experimentation with various market conditions, company strategies, and demand dynamics. The goal is to understand the impact of pricing decisions on profit, demand, and competition over time.

---

## Features

- **Dynamic Market Simulation**: Models demand variation and competitive dynamics.
- **Configurable Strategies**: Supports `OptimizerStrategy` (aggressive pricing) and `FollowerStrategy` (conservative pricing).
- **Visual Analysis**: Outputs demand, profit, and pricing trends.
- **Extensible Framework**: Easily add new strategies or customize simulation settings.

---

## Installation

### Prerequisites

- Python >= 3.8

### Dependencies

The following libraries are required:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/market-simulation.git
   cd market-simulation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install the package:
   ```bash
   pip install .
   ```

---

## Project Structure

```
market-simulation/
├── src/
│   ├── models/
│   │   ├── company.py
│   │   ├── config.py
│   │   ├── strategies.py
│   ├── simulation/
│   │   ├── market_simulation.py
│   ├── utils/
│       ├── visualization.py
│   ├── main.py
├── tests/
├── docs/
│   ├── README.md
│   ├── examples.md
├── setup.py
```

### Key Components

#### `models/config.py`

Defines the `SimulationConfig` class for managing simulation parameters:

- `base_market_demand`
- `demand_variation`
- `simulation_periods`
- `price_elasticity`
- `fixed_cost_increase_rate`

#### `models/company.py`

Implements the `Company` class:

- Represents a company with configurable fixed and variable costs.
- Calculates demand, profit, and optimal pricing.
- Supports price updates based on chosen strategies.

#### `models/strategies.py`

Contains strategy implementations:

1. `OptimizerStrategy`: Uses profit optimization to calculate optimal pricing.
2. `FollowerStrategy`: Adjusts pricing based on competitor’s price.

#### `simulation/market_simulation.py`

Manages the simulation process:

- Handles demand generation.
- Updates pricing and tracks performance over time.
- Stores results for visualization.

#### `utils/visualization.py`

Generates plots to visualize simulation outcomes:

- Pricing trends.
- Demand and profit analysis.

---

## Example Usage

```python
from src.models.config import SimulationConfig
from src.models.company import Company
from src.models.strategies import OptimizerStrategy, FollowerStrategy
from src.simulation.market_simulation import MarketSimulation

def main():
    # Simulation Configuration
    config = SimulationConfig(
        base_market_demand=10000,
        demand_variation=2000,
        simulation_periods=50,
        price_elasticity=0.05,
        random_seed=42
    )

    # Define Companies
    companies = [
        Company(
            name='Company A',
            fixed_costs=55000,
            variable_cost_per_unit=50,
            initial_price=100,
            reaction_speed=0.19,
            pricing_strategy=FollowerStrategy(),
            config=config
        ),
        Company(
            name='Company B',
            fixed_costs=30000,
            variable_cost_per_unit=30,
            initial_price=100,
            reaction_speed=0.2,
            pricing_strategy=OptimizerStrategy(),
            config=config
        )
    ]

    # Run Simulation
    simulation = MarketSimulation(companies, config)
    simulation.run_and_visualize(save_path='results')

if __name__ == "__main__":
    main()
```

---

## Results

### Example Visualization



### Output Data

Simulation outputs are saved as:

1. CSV: `results/market_simulation_results.csv`
2. Plot: `results/market_simulation_plot.png`

---

## Extending the Framework

### Adding a New Strategy

1. Create a new strategy class in `models/strategies.py`.
2. Inherit from `PricingStrategy`.
3. Implement the `calculate_optimal_price` method.

Example:

```python
class AggressiveStrategy(PricingStrategy):
    def calculate_optimal_price(self, company, competitor, total_market_demand):
        return competitor.price * 1.1
```

4. Update `main.py` to use the new strategy.

---

## Testing

Tests are located in the `tests/` directory. Run tests with:

```bash
pytest
```

---

## Future Enhancements

- Implement additional pricing strategies (e.g., dynamic pricing).
- Extend visualization options (e.g., heatmaps for profitability).
- Add real-time market feedback loops.

---

## Authors

[Your Name]\
Email: [mail@leondevries.de](mailto\:mail@leondevries.de)

---

## License

This project is licensed under the MIT License.

```

