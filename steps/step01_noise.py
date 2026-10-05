import random
import matplotlib.pyplot as plt

SAMPLE_RATE = 100   # samples per second
DURATION = 10       # seconds

signal = []
for i in range(SAMPLE_RATE * DURATION):
    signal.append(random.gauss(0, 1))

time = [i / SAMPLE_RATE for i in range(len(signal))]

plt.plot(time, signal)
plt.xlabel("time [s]")
plt.ylabel("signal (arbitrary units)")
plt.show()