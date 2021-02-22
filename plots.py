import tarfile
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen

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

def add_titlebox(ax, title):
    ax.text(.55, .8, title, horizontalalignment='center', transform=ax.transAxes, bbox=dict(facecolor='white', alpha=0.6), fontsize=12.5)
    return ax

def testThree():
    fpath = 'data/cal_housing.data'
    with open(fpath, mode='r') as archive:
        housing = np.loadtxt(archive,delimiter=',')
        #housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')

    y = housing[:,-1]
    pop, age = housing[:,[4,7]].T

    gridsize = (3, 2)
    fig = plt.figure(figsize=(12, 8))
    ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (2, 0))
    ax3 = plt.subplot2grid(gridsize, (2, 1))

    ax1.set_title('Home value as a function of home age & area population',fontsize=14)
    sctr = ax1.scatter(x=age, y=pop, c=y, cmap='RdYlGn')
    plt.colorbar(sctr, ax=ax1, format='$%d')
    ax1.set_yscale('log')
    ax1.set_ylabel('population')
    ax1.set_xlabel('age')
    ax2.hist(age, bins='auto')
    ax3.hist(pop, bins='auto', log=True)

    add_titlebox(ax2, 'Histogram: home age')
    add_titlebox(ax3, 'Histogram: area population (log scl.)')
    plt.show()

if __name__ == "__main__":

    #testOne()
    #testTwo()
    testThree()
