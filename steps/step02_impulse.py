import math
import random
import matplotlib.pyplot as plt

SAMPLE_RATE = 100       # samples per second
DURATION = 10           # seconds
IMPULSE_TIME = 3.0      # when the impulse starts [s]
IMPULSE_HEIGHT = 8.0    # how tall it is
DECAY_TIME = 0.1        # how fast it fades [s]

signal = []
for i in range(SAMPLE_RATE * DURATION):
    t = i / SAMPLE_RATE
    value = random.gauss(0, 1)
    if t >= IMPULSE_TIME:
        value += IMPULSE_HEIGHT * math.exp(-(t - IMPULSE_TIME) / DECAY_TIME)
    signal.append(value)

time = [i / SAMPLE_RATE for i in range(len(signal))]

plt.plot(time, signal)
plt.xlabel("time [s]")
plt.ylabel("signal (arbitrary units)")
plt.show()