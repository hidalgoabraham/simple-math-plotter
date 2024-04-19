import numpy as np
import matplotlib.pyplot as plt
import mplcursors


# Define n values for the plot
n = np.linspace(-100, 100, 201)  # Adjust range and number of points

# Calculate x1 values
x1 = np.sinc(n / 10)  # Normalized Cardinal Sine


# Configure the plot
plt.title("Normalized Cardinal Sine Function")
plt.xlabel("n")
plt.ylabel("sinc[n]")
# var = plt.plot(n, x1, ".", label="sinc[n]")
plt.plot(n, x1, ".", label="sinc[n]")


plt.grid(True)
plt.legend()

# labels = []
# for i in range(len(n)):
#     labels.append(f"sinc[n]={str(round(x1[i], 3))}" + f"\nn={str(round(n[i], 3))}")
# mplcursors.cursor(var, hover=True).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.index)]))

mplcursors.cursor(hover=True)

# Show the plot
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Define function parameters
# t_start = 0  # Start time
# t_end = 5  # End time
# f = 2  # Frequency (Hz)
# pulse_width = 2  # Pulse width (seconds)

# # Create time vector
# t = np.linspace(t_start, t_end, 1000)  # 1000 time steps

# # Create sine wave
# sine_wave = np.sin(2 * np.pi * f * t)


# # Create unit step function (using Heaviside function)
# def unit_step(t, pulse_width, t_start):
#     return np.heaviside(t - t_start, 1) - np.heaviside(t - (t_start + pulse_width), 1)


# # Create unit step signal for the pulse duration
# unit_step_signal = unit_step(t, pulse_width, t_start)

# # Calculate sine pulse (sine wave multiplied by unit step)
# sine_pulse = sine_wave * unit_step_signal

# # Plot the results
# plt.plot(t, sine_wave, label="Sine wave")
# plt.plot(t, unit_step_signal, label="Unit step")
# plt.plot(t, sine_pulse, label="Sine pulse")

# # Customize the plot
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")
# plt.title("Sine Pulse Function")
# plt.grid(True)
# plt.legend()
# plt.show()
