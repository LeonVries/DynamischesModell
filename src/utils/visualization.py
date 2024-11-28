import matplotlib.pyplot as plt
import pandas as pd
from typing import List
from ..models.company import Company

def plot_simulation_results(companies: List[Company], results: pd.DataFrame):
    """
    Visualize simulation results with multiple subplots
    
    Args:
        companies (List[Company]): List of companies in simulation
        results (pd.DataFrame): Simulation results dataframe
    """
    plt.figure(figsize=(16, 12))
    
    plot_configs = [
        ('Preisentwicklung', 'Price', 'Preis (€)'),
        ('Nachfrageentwicklung', 'Quantity', 'Menge (Einheiten)'),
        ('Gewinnentwicklung', 'Profit', 'Gewinn (€)'),
        ('Kostenentwicklung', 'Total Cost', 'Gesamtkosten (€)')
    ]
    
    for idx, (title, metric, ylabel) in enumerate(plot_configs, 1):
        plt.subplot(2, 2, idx)
        for company in companies:
            plt.plot(results[f'{company.name} {metric}'], label=company.name)
        plt.title(title)
        plt.xlabel('Periode')
        plt.ylabel(ylabel)
        plt.legend()
    
    plt.tight_layout()
    plt.show()