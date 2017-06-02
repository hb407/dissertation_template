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

f_list = os.listdir('./')

fig =plt.figure()
gs = gridspec.GridSpec(1,1)
ax = fig.add_subplot(gs[0])
ax.set_ylim([-3,0.5])
ax.set_xlim([50,300])
ax.set_xlabel(r'Bond Length / pm',fontsize=18)
ax.set_ylabel(r'Energy / $E_{h}$',fontsize=18)
ax.set_title(r'$Z = 1.00\ \mathrm{a.u.}$',fontsize=18)

ax.plot([0],[0],c='r',label=r'RHF')
ax.plot([0],[0],c='m',label=r'h-RHF')
for f in f_list:
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')
ax.legend(loc='upper right')

fig.savefig('HZ_z1-00.eps')
