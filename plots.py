import numpy as np
import matplotlib.pyplot as plt

def testOne():
    #np.random.seed(444)

    #fig, _= plt.subplots()
    #print(type(fig))

    #one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
    #print((one_tick.axes))

    rng = np.arange(50)
    rnd = np.random.randint(0,10, size=(3, rng.size))

    #print(rng)
    #print(rnd)

    yrs = 1950 + rng

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
    ax.set_title('Combined debt growth over time')
    ax.legend(loc='upper left')
    ax.set_ylabel('Total debt')
    ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
    fig.tight_layout()
    plt.show()

def testTwo():
    x = np.random.randint(low=1,  high =11, size = 500)
    y = x + np.random.randint(1,5,size=x.size)

    data = np.column_stack((x,y))
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,figsize=(8,4))
    ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
    ax1.set_title('Scatter: $x$ versus $y$')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')

    ax2.hist(data, bins=np.arange(data.min(), data.max()),label=('x', 'y'))
    ax2.legend(loc=(0.65, 0.8))
    ax2.set_title('Frequencies of $x$ and $y$')
    ax2.yaxis.tick_right()
    plt.show()

if __name__ == "__main__":

    #testOne()
    testTwo()
