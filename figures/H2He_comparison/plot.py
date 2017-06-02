import numpy as np
import sys
sys.path.append('/home/hb407/reports/FirstYearReport/figures/')
from matplotlibParameters import * 
import os

matplotlibSetup()

fig =plt.figure(figsize=(7,3))
plt.gcf().subplots_adjust(bottom=0.28)

ax1 = fig.add_subplot(121)
ax1.set_ylim([-4,3.0])
ax1.set_xlim([29.999, 300.001])
plt.setp(ax1.get_yticklabels(), visible=True)
plt.setp(ax1.get_xticklabels())
ax1.set_xlabel(r'H - He Bond Length / $\mathrm{pm}$')
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$')

for f in os.listdir('./H2He_2p_sto-3g'):
    f = './H2He_2p_sto-3g/'+f
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')

ax2 = fig.add_subplot(122, sharey=ax1)
ax2.set_ylim([-4,3])
ax2.set_xlim([29.999, 300.001])
plt.setp(ax2.get_yticklabels(), visible=False)
plt.setp(ax2.get_xticklabels())
ax2.set_xlabel(r'H - He Bond Length / $\mathrm{pm}$')
ax2.plot([0],[0],c='r',label=r'RHF')
ax2.plot([0],[0],c='m',label=r'h-RHF')

for f in os.listdir('./H2He_sto-3g'):
    f = './H2He_sto-3g/'+f
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax2.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax2.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')

ax2.legend(loc='upper center', bbox_to_anchor=(-0.06, -0.22),
          fancybox=True, ncol=2, fontsize=matplotlib.rcParams['axes.labelsize'])

fig.subplots_adjust(wspace=0.1, hspace=0.)

fig.savefig('H2He_comparison.eps')
