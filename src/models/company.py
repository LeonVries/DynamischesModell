import numpy as np
from typing import TYPE_CHECKING
from .strategies import PricingStrategy

if TYPE_CHECKING:
    from .config import SimulationConfig

class Company:
    """Enhanced Company class with more flexible design"""
    def __init__(
        self, 
        name: str, 
        fixed_costs: float, 
        variable_cost_per_unit: float,
        initial_price: float, 
        reaction_speed: float,
        pricing_strategy: PricingStrategy,
        config: 'SimulationConfig'
    ):
        self.name = name
        self.fixed_costs = fixed_costs
        self.variable_cost_per_unit = variable_cost_per_unit
        self.price = initial_price
        self.reaction_speed = reaction_speed
        self.pricing_strategy = pricing_strategy
        self.config = config
    
    def calculate_demand(
        self, 
        own_price: float, 
        competitor_price: float, 
        total_market_demand: float, 
        alpha: float
    ) -> float:
        """Calculate market demand using logit model"""
        numerator = np.exp(-alpha * own_price)
        denominator = numerator + np.exp(-alpha * competitor_price)
        market_share = numerator / denominator
        return total_market_demand * market_share
    
    def calculate_total_cost(self, quantity: float) -> float:
        """Calculate total costs including fixed and variable costs"""
        variable_costs = self.variable_cost_per_unit * quantity
        return self.fixed_costs + variable_costs

    def calculate_profit(self, price: float, quantity: float) -> float:
        """Calculate company's profit"""
        revenue = price * quantity
        total_cost = self.calculate_total_cost(quantity)
        return revenue - total_cost

    def update_price(self, optimal_price: float):
        """Update price with reaction speed consideration"""
        self.price += self.reaction_speed * (optimal_price - self.price)
    
    def update_fixed_costs(self):
        """Increase fixed costs gradually"""
        self.fixed_costs *= (1 + self.config.fixed_cost_increase_rate)