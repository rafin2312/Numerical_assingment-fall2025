import numpy as np
import matplotlib.pyplot as plt

class HeatEquationFTCS:
    def __init__(self, L=1.0, T=0.5, nx=50, alpha=0.01):
        """
        Initializes the solver.
        Parameters match the Group Alpha1 Report exactly.
        """
        self.L = L
        self.T = T
        self.nx = nx
        self.dx = L / (nx - 1)
        self.alpha = alpha
        self.x = np.linspace(0, L, nx)
        self.u = np.zeros(nx)
