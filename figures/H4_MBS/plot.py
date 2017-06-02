import numpy as np
import matplotlib
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

rc('font', **{'family': 'serif', 'serif': ['Libertine']})
rc('text', usetex=True)
matplotlib.rcParams['xtick.labelsize'] = 18
matplotlib.rcParams['ytick.labelsize'] = 18

labelsize=10

fig =plt.figure(figsize=(7,5.))
plt.gcf().subplots_adjust(left=0.12,bottom=0.15,right=0.8)

ax1 = fig.add_subplot(111)
ax1.set_ylim([-2,-0.77777775])
ax1.set_xlim([1.058235,6])#10.58235])
plt.setp(ax1.get_yticklabels(), visible=True, fontsize=labelsize)
plt.setp(ax1.get_xticklabels(), fontsize=labelsize)
ax1.set_xlabel(r'Bond Length / $\mathrm{pm}$',fontsize=labelsize)
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$',fontsize=labelsize)

for f in os.listdir('./'):
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='r',linestyle='-', linewidth=0.5)
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-',linewidth=0.5)
ax1.plot([0],[0],c='r',label=r'RHF',linewidth=0.5)
ax1.plot([0],[0],c='m',label=r'h-RHF',linewidth=0.5)

ax1.legend(loc='upper right', bbox_to_anchor=(1.25, 0.61),
          fancybox=True, ncol=1, fontsize=labelsize)

fig.savefig('H4_MBS.eps')
