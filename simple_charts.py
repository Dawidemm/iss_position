import matplotlib.pyplot as plt

def simple_2d_charts(x, y, xlabel, ylabel):
    fig = plt.figure()
    fig.set_size_inches(9, 7)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()
    return None