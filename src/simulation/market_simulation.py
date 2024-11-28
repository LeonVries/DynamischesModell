import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Callable
from ..models.company import Company
from ..models.config import SimulationConfig
from ..utils.visualization import plot_simulation_results

class MarketSimulation:
    """Enhanced Market Simulation with more flexible design"""
    def __init__(
        self, 
        companies: List[Company], 
        config: SimulationConfig,
        random_generator: Callable = np.random.normal
    ):
        self.companies = companies
        self.config = config
        self.random_generator = random_generator
        self.market_history = []
        
        # Set random seed if provided
        if config.random_seed is not None:
            np.random.seed(config.random_seed)
    
    def run_simulation(self) -> pd.DataFrame:
        """Execute market simulation with enhanced flexibility"""
        for period in range(self.config.simulation_periods):
            # Generate market demand with variation
            total_market_demand = max(
                0, 
                self.random_generator(
                    self.config.base_market_demand, 
                    self.config.demand_variation
                )
            )
            
            period_data = {'Period': period}
            
            for company in self.companies:
                competitor = next(c for c in self.companies if c != company)
                
                # Calculate demand and profit
                quantity = company.calculate_demand(
                    company.price, 
                    competitor.price, 
                    total_market_demand, 
                    self.config.price_elasticity
                )
                profit = company.calculate_profit(company.price, quantity)
                
                # Store period data
                period_data.update({
                    f'{company.name} Price': company.price,
                    f'{company.name} Quantity': quantity,
                    f'{company.name} Profit': profit,
                    f'{company.name} Total Cost': company.calculate_total_cost(quantity)
                })
                
                # Optimize or follow pricing strategy
                optimal_price = company.pricing_strategy.calculate_optimal_price(
                    company, competitor, total_market_demand
                )
                company.update_price(optimal_price)
                
                # Update fixed costs
                company.update_fixed_costs()
            
            self.market_history.append(period_data)
        
        return pd.DataFrame(self.market_history)
    
    def run_and_visualize(self, save_path: str = None):
        """
        Run simulation and visualize results
        
        Args:
            save_path (str, optional): Path to save results CSV and plot
        """
        results = self.run_simulation()
        
        # Visualize results
        plot_simulation_results(self.companies, results)
        
        # Save results if path provided
        if save_path:
            results.to_csv(f'{save_path}/market_simulation_results.csv', index=False)
            plt.savefig(f'{save_path}/market_simulation_plot.png')