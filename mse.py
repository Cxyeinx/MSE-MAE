# Mean Squared Error


import numpy as np


def mse(y_real, y_predicted):
	mse = []
	for real, fake in zip(y_real, y_predicted):
		mse.append((real - fake) ** 2)

	mse = sum(mse) / len(mse)

	return mse


y_real = np.array([10, 13, 14, 9, 17])
y_predicted = np.array([9, 14, 12, 10, 15])


print(mse(y_real, y_predicted))