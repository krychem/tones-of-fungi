import math
import random
import matplotlib.pyplot as plt

SAMPLE_RATE = 100
DURATION = 20
N_IMPULSES = 4
IMPULSE_HEIGHT = 8.0
DECAY_TIME = 0.5

random.seed(1)  # same result every run; remove it later

impulse_times = []
for _ in range(N_IMPULSES):
    impulse_times.append(random.uniform(1, DURATION - 3))
impulse_times.sort()
print(impulse_times)

signal = []
for i in range(SAMPLE_RATE * DURATION):
    t = i / SAMPLE_RATE
    value = random.gauss(0, 1)
    for start in impulse_times:
        if t >= start:
            value += IMPULSE_HEIGHT * math.exp(-(t - start) / DECAY_TIME)
    signal.append(value)

time = [i / SAMPLE_RATE for i in range(len(signal))]

plt.plot(time, signal)
plt.xlabel("time [s]")
plt.ylabel("signal (arbitrary units)")
plt.show()