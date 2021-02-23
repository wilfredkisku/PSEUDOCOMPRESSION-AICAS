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
    fig = plt.figure(figsize=(12, 8), dpi=400.0)
    ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (2, 0))
    ax3 = plt.subplot2grid(gridsize, (2, 1))

    ax1.set_title('Home value as a function of home age & area population',fontsize=14)
    sctr = ax1.scatter(x=age, y=pop, c=y, cmap='RdYlGn')
    plt.colorbar(sctr, ax=ax1, format='$%d')
    ax1.set_yscale('log')
    ax1.set_ylabel('population')
    ax1.set_xlabel('age')
    ax2.hist(age, bins='auto', facecolor='g')
    ax3.hist(pop, bins='auto', facecolor='r', log=True)

    add_titlebox(ax2, 'Histogram: home age')
    add_titlebox(ax3, 'Histogram: area population (log scl.)')
    plt.savefig('population.png')
    plt.show()

def testFour():
    t = np.arange(0.0, 1.0 + 0.01, 0.01)
    s = np.cos(2 * 2*np.pi * t)
    t[41:60] = np.nan

    plt.subplot(2, 1, 1)
    plt.plot(t, s, '-', lw=2)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('A sine wave with a gap of NaNs between 0.4 and 0.6')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    t[0] = np.nan
    t[-1] = np.nan
    plt.plot(t, s, '-', lw=2)
    plt.title('Also with NaN in first and last point')

    plt.xlabel('time (s)')
    plt.ylabel('more nans')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def testFive():
    np.random.seed(19680801)

    x = np.random.rand(10)
    y = np.random.rand(10)
    z = np.sqrt(x**2 + y**2)

    plt.subplot(321)
    plt.scatter(x, y, s=80, c=z, marker=">")

    plt.subplot(322)
    plt.scatter(x, y, s=80, c=z, marker=(5, 0))

    verts = np.array([[-1, -1], [1, -1], [1, 1], [-1, -1]])
    plt.subplot(323)
    plt.xlabel('this is the x label')
    plt.scatter(x, y, s=80, c=z, marker=verts)

    plt.subplot(324)
    plt.scatter(x, y, s=80, c=z, marker=(5, 1))

    plt.subplot(325)
    plt.scatter(x, y, s=80, c=z, marker='+')

    plt.subplot(326)
    plt.scatter(x, y, s=80, c=z, marker=(5, 2))

    plt.show()

if __name__ == "__main__":

    #testOne()
    #testTwo()
    #testThree()
    testFour()
    #testFive()
