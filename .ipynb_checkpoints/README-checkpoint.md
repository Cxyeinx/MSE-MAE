# Mean Squared Error (MSE)

In Statistics MSE is the average of squares of error. 

A error is meant by the difference between the real y value and the predicted/estimated y value. 

$$ 
error = (Y_i - \widehat{Y}_i)
$$

$$
MSE = \frac{1}{n} \sum^{n}_{i=1}{(Y_i - \widehat{Y}_i)^2}
$$

where

$n$ = Number of observations

$Y_i$ = Real Value

$\widehat{Y}_i$ = Predicted Value

## Why just Square of the error?
Well.... Because we want the error to be absolute, or else the average of the error might be disturbed by positive and negitive values. We do take the square as we want a single minima-point.