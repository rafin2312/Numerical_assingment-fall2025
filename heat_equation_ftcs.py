import numpy as np
import matplotlib.pyplot as plt
class HeatEquationFTCS:
    def __init__(self, L=1.0, T=0.5, nx=50, alpha=0.01):
        self.L = L
        self.T = T
        self.nx = nx
        self.dx = L / (nx - 1)
        self.alpha = alpha
        self.x = np.linspace(0, L, nx)
        self.u = np.zeros(nx)

def set_initial_conditions(self):
        """Sets Initial Condition: u(x,0) = sin(pi * x)"""
        self.u = np.sin(np.pi * self.x)

def get_exact_solution(self, t):
        """Calculates exact solution: u = e^(-pi^2 * alpha * t) * sin(pi * x)"""
        decay = np.exp(-np.pi ** 2 * self.alpha * t)
        return decay * np.sin(np.pi * self.x)

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

#Boundary Conditions: u(0,t) = u(L,t) = 0
            u_next[0] = 0
            u_next[-1] = 0

            u_curr = u_next
            history.append(u_curr.copy())

        return self.x, u_curr, np.array(history), nt, dt

# --- MAIN EXECUTION ---

# 1. Setup Parameters

L = 1.0
alpha = 0.01
nx = 50
T = 0.5

print(f"--- Simulation Started ---")

# 2. Run STABLE Case (r = 0.45)

solver_stable = HeatEquationFTCS(L, T, nx, alpha)
solver_stable.set_initial_conditions()
x, u_stable_final, history_stable, nt_s, dt_s = solver_stable.solve(r=0.45)

# 3. Run UNSTABLE Case (r = 0.51)

solver_unstable = HeatEquationFTCS(L, T, nx, alpha)
solver_unstable.set_initial_conditions()
_, u_unstable_final, _, nt_u, dt_u = solver_unstable.solve(r=0.51)

# --- ACCURACY CHECK (MATCHING LATEX/README EXACTLY) ---

print("\n--- Accuracy Analysis (at t=0.5, r=0.45) ---")
u_exact = solver_stable.get_exact_solution(T)

# These specific indices correspond to x approx 0.24, 0.51, 0.76
indices = [12, 25, 37]

# Print Table Header

print(f"{'Position (x)':<15} {'Numerical':<15} {'Exact':<15} {'Error':<15}")
print("-" * 60)

for i in indices:
    pos = x[i]
    num_val = u_stable_final[i]
    ex_val = u_exact[i]
    err = abs(num_val - ex_val)
    # Formatting to 4 decimal places to match your report
    print(f"{pos:<15.2f} {num_val:<15.4f} {ex_val:<15.4f} {err:<15.4f}")
    
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

plt.subplot(1, 2, 2)

# Simulate instability visually
u_temp = np.sin(np.pi * x)
for n in range(60):  # Run enough steps to show explosion
    if n % 20 == 0:
        plt.plot(x, u_temp, label=f'Step {n}')
    u_new = u_temp.copy()
    u_new[1:-1] = u_temp[1:-1] + 0.51 * (u_temp[2:] - 2 * u_temp[1:-1] + u_temp[:-2])
    u_new[0] = 0;
    u_new[-1] = 0
    u_temp = u_new

plt.title(f'Instability (r=0.51)')
plt.xlabel('Position (x)')
plt.ylim(-2, 2)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig('solution_comparison.png', dpi=300)
print("\nGenerated: solution_comparison.png")

# Plot 2: Heatmap

plt.figure(figsize=(8, 6))
plt.imshow(history_stable, aspect='auto', extent=[0, L, T, 0], cmap='hot')
cb = plt.colorbar()
cb.set_label('Temperature (u)')
plt.title('2D Temperature Evolution (Stable Case)')
plt.xlabel('Position (x)')
plt.ylabel('Time (t)')
plt.tight_layout()
plt.savefig('resized_heatmap.png', dpi=300)
print("Generated: resized_heatmap.png")
plt.show()
