from src.models.config import SimulationConfig
from src.models.company import Company
from src.models.strategies import OptimizerStrategy, FollowerStrategy
from src.simulation.market_simulation import MarketSimulation

def main():
    # Configuration
    config = SimulationConfig(
        base_market_demand=10000,
        demand_variation=2000,
        simulation_periods=50,
        price_elasticity=0.05,
        random_seed=42  # For reproducibility
    )
    
    # Companies with different strategies
    companies = [
        Company(
            name='Unternehmen A',
            fixed_costs=55000,
            variable_cost_per_unit=50,
            initial_price=100,
            reaction_speed=0.19,
            pricing_strategy=FollowerStrategy(),
            config=config
        ),
        Company(
            name='Unternehmen B',
            fixed_costs=30000,
            variable_cost_per_unit=30,
            initial_price=100,
            reaction_speed=0.2,
            pricing_strategy=OptimizerStrategy(),
            config=config
        )
    ]
    
    # Run simulation
    simulation = MarketSimulation(companies, config)
    simulation.run_and_visualize(save_path='data/simulation_results')

if __name__ == "__main__":
    main()