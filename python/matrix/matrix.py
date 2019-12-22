import unittest

class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        row_len = len(rows)
        col_len = len(rows[0].split(' '))


        self.matrix = [[0 for i in range(col_len)]for j in range(row_len)]

        for i, row in enumerate(rows):
        	values = row.split(' ')
        	for j, value in enumerate(values):
        		self.matrix[i][j] = int(value)

        print(self.matrix)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        ans = []
        for row in range(len(self.matrix)):
        	ans.append(self.matrix[row][index-1])
        return ans



#matrix = Matrix("1 2\n10 20")
matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
print(matrix.row(2))
print(matrix.column(3))