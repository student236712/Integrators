import numpy as np
import parser


# Created for integrating functions of one variable - x
class RectangularIntegrator:
    def __init__(self, integration_points):
        self.integration_points = integration_points

    def integrate(self, function_to_integrate, left_integration_limes, right_integration_limes):
        a = left_integration_limes
        b = right_integration_limes
        width = (b - a) / self.integration_points
        arr = np.linspace(a, b, num=self.integration_points)
        st = parser.expr(function_to_integrate)
        code = st.compile('Rectangular_integrator.py')
        x_sum = 0
        for x in arr:
            x_sum += width * eval(code)

        return x_sum


if __name__ == '__main__':
    t_i = RectangularIntegrator(integration_points=2000000)
    print(t_i.integrate("2*x+40", 2, 10))
