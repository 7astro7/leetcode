
import numpy as np

class MakePascal:

    def get_triangle(self, num_rows: int = 30):
        pascal = list([] for i in range(num_rows))
        for row in range(num_rows):
            for col in range(row + 1):
                choose = np.math.comb(row, col)
                pascal[row].append(choose)
        return pascal

if __name__ == "__main__":
    MakePascal()
