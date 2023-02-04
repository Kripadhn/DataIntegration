import numpy as np

class KalmanFilter:
    def __init__(self, process_noise, measurement_noise):
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        self.posterior = np.zeros(2)
        self.covariance = np.eye(2)
        
    def estimate(self, measurement):
        prediction = self.posterior
        prediction_covariance = self.covariance + self.process_noise
        
        # Kalman gain
        gain = prediction_covariance.dot(np.linalg.inv(prediction_covariance + self.measurement_noise))
        
        self.posterior = prediction + gain.dot(measurement - prediction)
        self.covariance = (np.eye(2) - gain).dot(prediction_covariance)
        
        return self.posterior
