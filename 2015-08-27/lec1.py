import matplotlib.pyplot as plt


def plot_amdahl(serial_fraction, max_cores):
    x = range(1,max_cores+1)
    y = [1/(serial_fraction+(1-serial_fraction)/point) for point in x]
    plt.plot(x, y)
    plt.show()

plot_amdahl(0.1, 128)
