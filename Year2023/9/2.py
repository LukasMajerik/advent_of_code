# https://adventofcode.com/2023/day/9#part2

import os

FILENAME = "data.txt"
# FILENAME = "data_test.txt"

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split("\n")

data_processed = []
for row in data:
    row = row.split()
    data_processed.append([int(e) for e in row])

print(data_processed)


testing_row = data_processed[2]
print(testing_row)


class NextValuePredict:
    def __init__(self, row):
        self.row = row
        self.matrix = [row]

    def __repr__(self):
        return str(self.matrix)

    def print_me(self):
        print("NextValuePredict:")
        for e in self.matrix:
            print(e)

    def _is_predict_matrix_finished(self, row):
        for e in row:
            if e != 0:
                return False
        return True

    def _find_nxt_row(self, row):
        res = []
        for k in range(len(row) - 1):
            # print(k, row[k + 1], row[k])
            res.append(row[k + 1] - row[k])

        return res

    def build_val_matrix(self):
        row = self.matrix[0]
        while not self._is_predict_matrix_finished(row):
            row = self._find_nxt_row(row)
            self.matrix.append(row)

    def pred_nxt_val(self):
        self.build_val_matrix()

        last_idx_matrx = len(self.matrix) - 1
        curr_row = self.matrix[last_idx_matrx]
        curr_row.insert(0, 0)

        for i in range(last_idx_matrx, 0, -1):
            curr_row = self.matrix[i]
            prev_row = self.matrix[i - 1]
            prev_row.insert(0, -curr_row[0] + prev_row[0])

        return self._get_predicted_val()

    def _get_predicted_val(self):
        return self.matrix[0][0]


extrap_values = 0
# nvp = NextValuePredict(testing_row)
# print(nvp.pred_nxt_val())
# nvp.print_me()

for e in data_processed:
    print(e)
    nvp = NextValuePredict(e)
    nxt_val_ = nvp.pred_nxt_val()
    nvp.print_me()
    print(nxt_val_)
    extrap_values += nxt_val_
    print("sum:", extrap_values)

print(extrap_values)
