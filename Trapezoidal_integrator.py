import numpy as np
import parser


# Created for integrating functions of one variable - x
class TrapezoidalIntegrator:

    def integrate(self, function_to_integrate, left_integration_limes, right_integration_limes, integration_points):
        a = left_integration_limes
        b = right_integration_limes
        delta_x = (b - a) / integration_points
        arr = np.linspace(a, b, num=integration_points)
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
    t_i = TrapezoidalIntegrator()
    print(t_i.integrate("4*np.sqrt(1-x*x)", 0, 1, 100000))
