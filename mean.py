from typing import List
import time
import numpy as np
import random as rand
import matplotlib.pyplot as plt

def plot_hist(x: List[float]) -> None:
	plt.hist(timing, bins=25)
	plt.title("Hist with 25 bins.")
	plt.show()

def my_mean(x: List[int]) -> None:
	return sum(x)/len(x)

num_runs = 1000

timing = num_runs * [0]

for i in range(num_runs):
	test_array = rand.choices(range(1000), k=1000000)
	start = time.perf_counter()
	my_mean(test_array)
	end = time.perf_counter()
	time_taken = end - start
	timing[i] = time_taken


print(f"On average, it took {my_mean(timing):.8f} seconds.")



plot_hist(timing)

