import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from random import randint
from scipy.optimize import curve_fit


class Opers:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def deltait(data):
        s, t = data.shape
        p = np.zeros((s, t))
        for j in range(t+1):
            p = data[:j] - np.mean(data[:j])
        return np.array(p)

    def mat_norm(self, med=None):
        ma = np.array(self.data)

        if med:
            ma_df = pd.DataFrame(ma)
            ma = Opers.deltait(ma_df)

        t1, t2 = ma.shape
        um = np.ones(t1)
        ze = np.zeros((t1, t2))
        ts = []

        for i in range(0, t1):
            um[i] = np.linalg.norm(ma[i, :])
            ze[i, :] = (ma[i, :] / um[i])

        for j in range(1, t1 - 1):
            med = t1 - j
            for k in range(0, med):
                t = np.dot(ze[k, :], ze[j + k, :])
                ts.append(t)

        return ze, ts


class GrafsIzra(Opers):

    def __init__(self, data):
        Opers.__init__(self, data)

    def fit_izra(self, model, density, color1, color2, title='', glog=None):
        x = self.data
        parameters = []

        if glog:
            mm = plt.hist(x, bins=np.arange(0, 2.0, 0.1), density=density, color=color1)
        else:
            mm = plt.hist(x, ec='k', bins=np.arange(0, 1.8, 0.1), density=density, color=color1)

        bins = mm[1][1:]
        medbins = [i - 0.05 for i in bins]
        freq = mm[0]

        if model == 'izrailev4':
            def izrailev(x, a, b, c):
                return ((x ** (a - 1)) / b) * np.exp(-x * c)
        elif model == 'izrailev6':
            def izrailev(x, a, b, c, d):
                return ((x ** (a - 1)) / b) * np.exp(-(d * x ** 2) - x * c)
        elif model == 'izrailev8':
            def izrailev(x, a, b, c, d, f):
                return ((x ** (a - 1)) / b) * np.exp(-(f * x ** 3) - (d * x ** 2) - x * c)
        elif model == 'izrailev10':
            def izrailev(x, a, b, c, d, f, g):
                return ((x ** (a - 1)) / b) * np.exp(-(g * x ** 4) - (f * x ** 3) - (d * x ** 2) - x * c)
        else:
            return 'Invalid Model'

        # Plotting the graph
        parametros, error = curve_fit(izrailev, medbins, freq)
        for par in parametros:
            parameters.append(par)

        xfit = np.arange(0, 2, 0.01)
        plt.plot(xfit, izrailev(xfit, *parametros), color=color2)
        if glog:
            plt.scatter(medbins, freq, s=18, c='black')
            plt.yscale('log')
            plt.xscale('log')
        plt.xlim(0.01, 1.8)
        plt.title(f'Izrailev {title} Profile')
        plt.show()

        # Analyzing the parameters
        return parameters, error


class GrafsVar(Opers):

    def __init__(self, data):
        Opers.__init__(self, data)

    @staticmethod
    def sohist(data, density, color, title=''):
        counts, bins = np.histogram(data, density=density)
        plt.hist(bins[:-1], bins, weights=counts, color=color)
        plt.title(title, fontsize=11, fontweight='bold', fontstyle='italic', fontfamily='serif')
        plt.show()

    def varii(self, color, vall=None, title=''):
        ze, _ = Opers(self.data).mat_norm()

        plt.plot(ze[vall, :], color=color)
        plt.title(title, fontsize=11, fontweight='bold', fontstyle='italic', fontfamily='serif')
        plt.show()

        return ze

    def grafs_a(self, color, title='', titlex='', titley='', titlez=''):
        df = self.data
        f = df.shape[0]
        i = randint(0, df.shape[0] - 1)
        diff = f - i
        m1 = df[i:f]
        x = np.linspace(1055, 1075, df.shape[1])
        y = np.linspace(0, 1000, diff)
        xx, yy = np.meshgrid(x, y)
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        surf = ax.plot_surface(xx, yy, m1, cmap=color, linewidth=0.3, antialiased=False)
        fig.colorbar(surf, shrink=False)

        plt.xticks([1060, 1065, 1070])
        plt.yticks([0, 250, 500, 750])
        plt.title(title, fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
        ax.set(xlabel=r"%s" % titlex, ylabel=r"%s" % titley, zlabel=r"%s" % titlez)
        plt.gcf().set_size_inches(12, 8)
        plt.show()

        return i

    @staticmethod
    def ht_map(a, cmap, title='', titlex='', titley=''):
        dft = pd.DataFrame(a)
        der = dft.corr()
        sns.heatmap(der, cmap=cmap, vmin=0, linecolor='red')
        plt.xticks([0, 100], [1060, 1064])
        plt.xlabel(titlex)
        plt.yticks([0, 100], [1060, 1064])
        plt.ylabel(titley)
        plt.title(title, fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
        plt.show()
