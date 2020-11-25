from Rectangular_integrator import RectangularIntegrator
from Trapezoidal_integrator import TrapezoidalIntegrator
import numpy as np
import matplotlib.pyplot as plt

function_to_integrate = "np.sqrt(1-x*x)*4"
expected_value = np.pi
expected_value_name = "PI VALUE"

left_integration_limes = 0
right_integration_limes = 1

r_i = RectangularIntegrator()
t_i = TrapezoidalIntegrator()

test_points = np.arange(10, 400, 5)

rectangular_integrator_results = []
trapezoidal_integrator_results = []

t_x_counter = 0
r_x_counter = 0

for test_point in test_points:
    r_x = r_i.integrate(function_to_integrate, left_integration_limes, right_integration_limes, test_point)
    t_x = t_i.integrate(function_to_integrate, left_integration_limes, right_integration_limes, test_point)
    rectangular_integrator_results.append(r_x)
    trapezoidal_integrator_results.append(t_x)

    if np.isclose(t_x, expected_value, 0.005) and t_x_counter == 0:
        plt.vlines(x=test_point, ymin=0, ymax=expected_value + 0.1,
                   label=f'First convergence trapezoidal {test_point}', color="g")
        t_x_counter += 1
    if np.isclose(r_x, expected_value, 0.005) and r_x_counter == 0:
        plt.vlines(x=test_point, ymin=0, ymax=expected_value + 0.1,
                   label=f"First convergence rectangular {test_point}", color='m')
        r_x_counter += 1

plt.plot(test_points, rectangular_integrator_results, label="Rectangular values")
plt.plot(test_points, trapezoidal_integrator_results, label="Trapezoidal values")
plt.hlines(y=expected_value, xmin=test_points[0], xmax=test_points[-1], linestyles="--", color="k",
           label=expected_value_name)
plt.xlim(test_points[0], test_points[-1])
plt.ylim(min(min(trapezoidal_integrator_results), min(rectangular_integrator_results)))
plt.legend()
plt.xlabel("Integration steps done")
plt.ylabel("Integration result")
plt.title(
    f"Comparison for function = {function_to_integrate},a="
    f"{left_integration_limes},b={right_integration_limes}")
plt.savefig("Integrators_comparison.png")
plt.show()
