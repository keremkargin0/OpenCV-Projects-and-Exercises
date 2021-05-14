import cv2
import numpy as np

# Reading Handwritten Digits

digits = cv2.imread("digits.png", cv2.IMREAD_GRAYSCALE)
test_digits = cv2.imread("test_digits.png", cv2.IMREAD_GRAYSCALE)

# Splitting Digits as Vertical

rows = np.vsplit(digits, 50)
cells = []

# Splitting Digits as Horizontal and Creating Cells

for row in rows:
    row_cells = np.hsplit(row, 50)
    for cell in row_cells:
        cell = cell.flatten()
        cells.append(cell)
cells = np.array(cells, dtype=np.float32)

k = np.arange(10)
cells_labels = np.repeat(k, 250)


test_digits = np.vsplit(test_digits, 50)
test_cells = []
for d in test_digits:
    d = d.flatten()
    test_cells.append(d)
test_cells = np.array(test_cells, dtype=np.float32)

# Using KNN Algorithm
# The algorithm is labeling correctly for each handwritten digit.
# The algorithm doesn't work multiple arrays. So we should use one single arrays.

knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)
ret, result, neighbours, dist = knn.findNearest(test_cells, k=3)


print(result)
