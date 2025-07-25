
from Simulation.RocketPy.monte_carlo_analysis import MonteCarloDispersion
import sys



# Lancer l'analyse Monte Carlo après la fermeture de la fenêtre (ou via un bouton dans l'UI)
mc_analysis = MonteCarloDispersion(num_simulations=20)
mc_analysis.run_monte_carlo()
mc_analysis.plot_dispersion()