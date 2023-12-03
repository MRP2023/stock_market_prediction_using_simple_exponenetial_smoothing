from sktime.datasets import load_airline
from sktime.forecasting.exp_smoothing import ExponentialSmoothing

y = load_airline()


# Create an ExponentialSmoothing instance
model = ExponentialSmoothing(trend="add", seasonal="add", sp=12)

# Fit the model to the data
model.fit(y)

fh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

y_pred = model.predict(fh)