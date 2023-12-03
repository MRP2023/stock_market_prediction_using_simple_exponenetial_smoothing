
#####Formula Math of Double Explonation

def exponential_smoothing(data, alpha):
    # Initialize the forecast with the first data point
    forecast = [data[0]]

    # Perform exponential smoothing for the rest of the data
    for t in range(1, len(data)):
        forecast_t = alpha * data[t] + (1 - alpha) * forecast[t - 1]
        forecast.append(forecast_t)

    return forecast


# Example usage
historical_data = [100, 110, 120, 130, 140]
smoothing_alpha = 0.2

forecasted_values = exponential_smoothing(historical_data, smoothing_alpha)

for t, forecast in enumerate(forecasted_values):
    print(f"Month {t + 1} Forecast: {forecast:.2f}")
    
    
    
    
