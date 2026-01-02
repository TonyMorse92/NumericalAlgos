import numpy as np

# Number of "darts"
N = 100000

# Number of "darts" landing in circle
in_circle = 0

# We need to pick random x coordinate and random y coordinate. 
# Add if in.
for i in range (N-1):
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)
    
    if(x**2 + y**2 <= 1):
        in_circle += 1
        
print(f"There were {in_circle} darts that landed in the circle.")

# Pi is approximately 4 * (in_circle / N)
pi_approx = 4 * ((in_circle)/(N))
print(f"Pi is approximately: {pi_approx}")
