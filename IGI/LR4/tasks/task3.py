import math
import matplotlib.pyplot as plt
from statistics import mean, median, mode, stdev, variance

from input_handler import input_float


class BaseSeries:
    _count = 0  # Статический атрибут для подсчета экземпляров

    def __init__(self, x, eps):
        self.x = x
        self.eps = eps
        self.terms = []
        self.max_iter = 500
        BaseSeries._count += 1

    def calculate(self):
        raise NotImplementedError("Subclasses must implement this method")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not (-1 < value < 1):
            raise ValueError("x must be in (-1, 1)")
        self._x = value

    @staticmethod
    def get_count():
        return BaseSeries._count

    def __str__(self):
        return f"Series with x={self.x}, eps={self.eps}"

class LnSeries(BaseSeries):
    def calculate(self):
        sum_result = 0.0
        self.terms = []
        for n in range(1, self.max_iter + 1):
            term = -(self.x ** n) / n
            sum_result += term
            self.terms.append(term)
            if abs(term) < self.eps:
                return sum_result, n
        return sum_result, self.max_iter

class LnSeriesWithStatistics(LnSeries):
    pass

class Plotter:
    @staticmethod
    def plot_series(x_range, eps):
        series_values = []
        math_values = []
        valid_x = []
        for x in x_range:
            x /= 1000
            try:
                ln_series = LnSeriesWithStatistics(x, eps)
                sum_result, _ = ln_series.calculate()
                series_values.append(sum_result)
                math_values.append(math.log(1 - x))
                valid_x.append(x)
            except ValueError:
                print(f"Skipping x={x} as it is out of range (-1, 1)")

        plt.figure()
        plt.plot(valid_x, series_values, 'b-', label='Series Approximation')
        plt.plot(valid_x, math_values, 'r--', label='Math Function')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Comparison of Series Approximation and Math Function')
        plt.legend()
        plt.grid(True)
        plt.annotate(f'Precision ε = {eps}', xy=(0.5, 0.02), xycoords='axes fraction', ha='center')
        plt.savefig('comparison_plot.png')
        plt.show()

class task3:
    def __init__(self):
        pass

    def run(self):
        try:
            x = input_float('Input x: ')
            eps = input_float('Input eps: ')
            ln_series = LnSeriesWithStatistics(x, eps)
            sum_result, n = ln_series.calculate()
            math_fx = math.log(1 - x)

            print('x = ', x)
            print('n = ', n)
            print('f(x) = ', sum_result)
            print('math f(x) = ', math_fx)
            print('eps = ', eps)

            plotter = Plotter()
            plotter.plot_series(range(0, 1000), eps)

        except ValueError as e:
            print(e)
