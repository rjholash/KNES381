import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# generate some example data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# create a smoothed line with a moving average filter
window_size = 5
weights = np.repeat(1.0, window_size) / window_size
smoothed = np.convolve(y, weights, 'valid')

# calculate the 95% confidence interval using t-distribution
n = len(y)
m = np.mean(y)
s = np.std(y, ddof=1)
t = stats.t.ppf(0.975, n-1)
ci = t * s / np.sqrt(n)
offset = 0.2
# need to calculate an offset of the smooth line
# 100 data points divided by the window size of 5 = 20  20/100 = .2

# plot the data and smoothed line with confidence interval
plt.plot(x, y, 'o', alpha=0.5)
<<<<<<< HEAD
plt.plot((x[window_size-1:]-.12), (smoothed -.0))
# The bracketed x and smoothed values above with the -.12 and -.0 correction
=======
plt.plot((x[window_size-1:]-offset), (smoothed -.0))
# The bracketed x and smoothed values above with the -.1 and -.0 correction
>>>>>>> e966f22 (added offset variable to correct for right shifted smooth and confidence interval)
# are included to left shift the smoothing line to compensate for the 
# moving average needed to describe the smoothed line
# this is also used below to shift the confidence interval plot
plt.fill_between((x[window_size-1:]-offset), smoothed - ci, smoothed + ci, alpha=0.2)
plt.show()
