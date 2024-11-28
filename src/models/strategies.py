from abc import ABC, abstractmethod
from scipy.optimize import minimize_scalar
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .company import Company

class PricingStrategy(ABC):
    """Abstract base class for different pricing strategies"""
    
    @abstractmethod
    def calculate_optimal_price(
        self, 
        company: 'Company', 
        competitor: 'Company', 
        total_market_demand: float
    ) -> float:
        """Calculate optimal pricing strategy"""
        pass

class OptimizerStrategy(PricingStrategy):
    """Aggressive pricing strategy that actively optimizes prices"""
    
    def calculate_optimal_price(
        self, 
        company: 'Company', 
        competitor: 'Company', 
        total_market_demand: float
    ) -> float:
        def negative_profit(price):
            quantity = company.calculate_demand(
                price, 
                competitor.price, 
                total_market_demand, 
                company.config.price_elasticity
            )
            return -company.calculate_profit(price, quantity)
        
        # Intelligent price bounds
        min_price = company.variable_cost_per_unit * 1.1
        max_price = min(200, competitor.price * 1.5)
        
        result = minimize_scalar(
            negative_profit,
            bounds=(min_price, max_price),
            method='bounded'
        )
        
        return result.x

class FollowerStrategy(PricingStrategy):
    """Conservative pricing strategy that follows market leader"""
    
    def calculate_optimal_price(
        self, 
        company: 'Company', 
        competitor: 'Company', 
        total_market_demand: float
    ) -> float:
        # Slightly undercut competitor with conservative adjustment
        return competitor.price * 0.97