# Mean Absolute Error


import numpy as np


def mae(y_real, y_predicted):
	mae = []
	for real, predicted in zip(y_real, y_predicted):
		mae.append(abs(real - predicted))

	mae = sum(mae) / len(mae)
	return mae

y_real = np.array([10, 13, 14, 9, 17])
y_predicted = np.array([9, 14, 12, 10, 15])


print(mae(y_real, y_predicted))
