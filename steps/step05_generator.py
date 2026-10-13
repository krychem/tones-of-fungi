import math
import random
import matplotlib.pyplot as plt

SAMPLE_RATE = 100
DURATION = 20
N_IMPULSES = 4
IMPULSE_HEIGHT = 8.0
DECAY_TIME = 0.5
DRIFT_AMPLITUDE = 3.0   # how far the baseline wanders
DRIFT_PERIOD = 15.0     # seconds for one full wave

def generate_samples():
    impulse_times = []
    for _ in range(N_IMPULSES):
        impulse_times.append(random.uniform(1, DURATION - 3))

    for i in range(SAMPLE_RATE * DURATION):
        t = i / SAMPLE_RATE
        value = random.gauss(0, 1)
        value += DRIFT_AMPLITUDE * math.sin(2 * math.pi * t / DRIFT_PERIOD)
        for start in impulse_times:
            if t >= start:
                value += IMPULSE_HEIGHT * math.exp(-(t - start) / DECAY_TIME)
        yield t, value


time = []
signal = []
for t, value in generate_samples():
    time.append(t)
    signal.append(value)

plt.plot(time, signal)
plt.xlabel("time [s]")
plt.ylabel("signal (arbitrary units)")
plt.show()