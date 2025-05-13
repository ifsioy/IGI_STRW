import numpy as np

class WorkingWithNumpy:
    def __init__(self):
        self.matrix = None
        self.arr = None


    def set_rand_matrix(self, n, m):
        self.matrix = np.random.randint(-10, 10, size=(n, m))

    def to_array(self):
        self.arr = self.matrix.flatten()

    def get_matrix(self):
        return self.matrix

    def get_arr(self):
        return self.arr

    def get_mean(self):
        return self.arr.mean()

    def get_median(self):
        return self.arr.median()

    def get_var(self):
        return self.arr.var()

    def get_std(self):
        return self.arr.std()

    def get_corrcoef(self, odd, even):
        min_len = min(len(odd), len(even))
        odd = odd[:min_len]
        even = even[:min_len]

        return np.corrcoef(odd, even)[0,1]


def task5():
    trp = WorkingWithNumpy()
    trp.set_rand_matrix(5, 5)
    matrix = trp.get_matrix()
    print(matrix)

    trp.to_array()
    arr = trp.get_arr()

    odd = [v for arr in matrix for v in arr if v % 2 == 1]
    even = [v for arr in matrix for v in arr if v % 2 == 0]
    print('num of odd  - ', len(odd),'\todd - ', odd)
    print('num of even - ', len(even),'\teven - ', even)

    odd = [arr[i] for i in range(0, len(arr), 2)]
    even = [arr[i] for i in range(1, len(arr), 2)]

    print('corrcoef')
    print(trp.get_corrcoef(odd, even))