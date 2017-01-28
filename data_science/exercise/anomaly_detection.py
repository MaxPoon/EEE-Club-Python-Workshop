import matplotlib.pyplot as plt
import numpy as np
from math import pi, sqrt, exp

#part4: change the threshold to separate the outliers and the rest
threshold = 0.5
data = np.load('dataset.npy')
y = np.zeros((len(data), 1))
data = np.hstack([data,y])

# part1: calculate the mean and std for each column
#mean = ...
#std = ...

def gaussian(x, mean, std):
	denom = sqrt(2*pi*std*std)
	num = exp(-(x-mean)**2/(2*std*std))
	return num/denom

def predict(data, mean, std, threshold):
	# part2: for each row, change the last element to 1 
	# if the gaussian probability is smaller than the threshold
	

def plot(data):
	# part3: plot the detected anomalies and the rest points
	# on the same graph using different colours
	

predict(data, mean, std, threshold)
plot(data)