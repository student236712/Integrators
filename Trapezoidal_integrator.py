import numpy as np
import parser


# Created for integrating functions of one variable - x
class TrapezoidalIntegrator:
    def __init__(self, integration_points):
        self.integration_points = integration_points

    def integrate(self, function_to_integrate, left_integration_limes, right_integration_limes):
        a = left_integration_limes
        b = right_integration_limes
        delta_x = (b - a) / self.integration_points
        arr = np.linspace(a, b, num=self.integration_points)
        st = parser.expr(function_to_integrate)
        code = st.compile('Trapezoidal_integrator.py')
        x_sum = 0
        for i in range(len(arr)):
            x = arr[i]
            if i == 0 or i == len(arr) - 1:
                x_sum += eval(code)
            else:
                x_sum += 2 * eval(code)
        return x_sum * delta_x / 2


if __name__ == '__main__':
    t_i = TrapezoidalIntegrator(integration_points=2000000)
    print(t_i.integrate("2*x+40", 2, 10))
