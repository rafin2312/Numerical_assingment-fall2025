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
# This is  FOR THE 2ND PERSON IN LIST TO PASTE INTO 



# This is  FOR THE 2ND PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 3RD PERSON IN LIST TO PASTE INTO 
def solve(self, r):
        """
        Solves using FTCS scheme: u_new = u + r * (u_i+1 - 2u_i + u_i-1)
        """
        # Calculate dt based on stability parameter r
        dt = r * (self.dx ** 2) / self.alpha
        nt = int(self.T / dt)

        u_curr = self.u.copy()
        history = [u_curr.copy()]  # Store for heatmap

        for n in range(nt):
            u_next = u_curr.copy()
            # Vectorized FTCS update (exclude boundaries)
            u_next[1:-1] = u_curr[1:-1] + r * (u_curr[2:] - 2 * u_curr[1:-1] + u_curr[:-2])


# This is  FOR THE 3RD PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 4TH PERSON IN LIST TO PASTE INTO 



# This is  FOR THE 4TH PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 5TH PERSON IN LIST TO PASTE INTO 
# --- MAIN EXECUTION ---

# 1. Setup Parameters
L = 1.0
alpha = 0.01
nx = 50
T = 0.5

print(f"--- Simulation Started ---")


# This is  FOR THE 5TH PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 6TH PERSON IN LIST TO PASTE INTO 
# 2. Run STABLE Case (r = 0.45)
solver_stable = HeatEquationFTCS(L, T, nx, alpha)
solver_stable.set_initial_conditions()
x, u_stable_final, history_stable, nt_s, dt_s = solver_stable.solve(r=0.45)

# 3. Run UNSTABLE Case (r = 0.51)
solver_unstable = HeatEquationFTCS(L, T, nx, alpha)
solver_unstable.set_initial_conditions()
_, u_unstable_final, _, nt_u, dt_u = solver_unstable.solve(r=0.51)


# This is  FOR THE 6TH PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 7TH PERSON IN LIST TO PASTE INTO 
# --- ACCURACY CHECK (MATCHING LATEX/README EXACTLY) ---
print("\n--- Accuracy Analysis (at t=0.5, r=0.45) ---")
u_exact = solver_stable.get_exact_solution(T)

# These specific indices correspond to x approx 0.24, 0.51, 0.76
indices = [12, 25, 37]

# Print Table Header
print(f"{'Position (x)':<15} {'Numerical':<15} {'Exact':<15} {'Error':<15}")
print("-" * 60)



# This is  FOR THE 7TH PERSON IN LIST TO PASTE INTO 


# This is  FOR THE 8TH PERSON IN LIST TO PASTE INTO 
for i in indices:
    pos = x[i]
    num_val = u_stable_final[i]
    ex_val = u_exact[i]
    err = abs(num_val - ex_val)
    # Formatting to 4 decimal places to match your report
    print(f"{pos:<15.2f} {num_val:<15.4f} {ex_val:<15.4f} {err:<15.4f}")
# This is  FOR THE 8TH PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 9TH PERSON IN LIST TO PASTE INTO 
# Plot 1: Comparison
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
steps_to_show = [0, nt_s // 5, nt_s // 2, nt_s]
for n in steps_to_show:
    plt.plot(x, history_stable[n], label=f't={n * dt_s:.3f}', linewidth=1.5)
plt.title(f'Stable Diffusion (r=0.45)')
plt.xlabel('Position (x)')
plt.ylabel('Temperature (u)')
plt.legend()
plt.grid(True, alpha=0.3)



# This is  FOR THE 9TH PERSON IN LIST TO PASTE INTO 

# This is  FOR THE 10TH PERSON IN LIST TO PASTE INTO 



# This is  FOR THE 10TH PERSON IN LIST TO PASTE INTO 
