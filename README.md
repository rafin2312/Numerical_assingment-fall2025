# Assignment: Numerical Solution of Heat Equation (Explicit FTCS)

**Topic:** D1 - Heat Equation (Explicit FTCS)  
**Course:** CSE261 - Numerical Methods  

## Problem Statement
We need to solve the one-dimensional transient heat conduction equation:

$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

Subject to the boundary conditions $u(0,t) = u(L,t) = 0$ and initial condition $u(x,0) = \sin(\pi x)$.

* Implement **Explicit Finite Difference Scheme (FTCS)**.
* Analyze **Stability** by varying the parameter $r$.
* Visualize **Diffusion** and **Instability**.

## Theory

### Explicit FTCS Scheme
The Forward Time Centered Space (FTCS) method discretizes the domain into a grid. The update formula is:

$$u_i^{n+1} = u_i^n + r (u_{i+1}^n - 2u_i^n + u_{i-1}^n)$$

Where $r$ is the stability parameter (Fourier number):

$$r = \frac{\alpha \Delta t}{(\Delta x)^2}$$

* **Easy to implement.**
* **Accuracy:** $O(\Delta t, \Delta x^2)$.
* **Conditional Stability:** Requires strictly $r \le 0.5$.

## Analysis

### Stability
* **Stable Case ($r \le 0.5$):** The solution decays smoothly as expected physically.
    * *Example:* For $r=0.45$, the temperature profile remains smooth.
* **Unstable Case ($r > 0.5$):** Numerical errors amplify exponentially.
    * *Example:* For $r=0.51$, oscillations (zig-zags) appear immediately and the solution explodes.

### Graphical Results
The graphs below demonstrate the difference between the stable and unstable regimes.

![Solution Comparison](solution_comparison.png)

## Conclusion
* The **Explicit FTCS** method is simple but has a strict stability constraint.
* If the time step $\Delta t$ is too large (making $r > 0.5$), the method fails catastrophically.
* For practical simulations, one must ensure the stability condition is met or use Implicit methods (like Crank-Nicolson).
