from dataclasses import dataclass
from typing import Optional

@dataclass
class SimulationConfig:
    """
    Centralized configuration for market simulation parameters.
    Allows easy modification and extension of simulation settings.
    """
    base_market_demand: float
    demand_variation: float
    simulation_periods: int
    price_elasticity: float
    fixed_cost_increase_rate: float = 0.01
    random_seed: Optional[int] = None

    def validate(self):
        """
        Validate configuration parameters to ensure simulation integrity.
        
        Raises:
            ValueError: If any parameter is invalid
        """
        if self.base_market_demand <= 0:
            raise ValueError("Base market demand must be positive")
        
        if self.simulation_periods <= 0:
            raise ValueError("Simulation periods must be greater than zero")
        
        if not (0 < self.price_elasticity < 1):
            raise ValueError("Price elasticity must be between 0 and 1")