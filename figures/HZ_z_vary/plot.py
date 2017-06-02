import numpy as np
import sys
sys.path.append('/home/hb407/reports/FirstYearReport/figures/')
from matplotlibParameters import * 
import os

matplotlibSetup()

fig =plt.figure(figsize=(5.3,3.2))
plt.gcf().subplots_adjust(left=0.12,bottom=0.15,right=0.75)

ax1 = fig.add_subplot(111)
ax1.set_ylim([-3,3.0])
ax1.set_xlim([-1.0001,2.0001])
plt.setp(ax1.get_yticklabels(), visible=True)
plt.setp(ax1.get_xticklabels())
ax1.set_xlabel(r'$Z\ /\ \mathrm{a.u.}$')
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$')

for f in os.listdir('./'):
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='r',linestyle='-')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')
ax1.plot([0],[0],c='r',label=r'RHF')
ax1.plot([0],[0],c='m',label=r'h-RHF')

ax1.legend(loc='upper right', bbox_to_anchor=(1.35, 0.61),
          fancybox=True, ncol=1, fontsize=matplotlib.rcParams['axes.labelsize'])

fig.savefig('HZ_z_vary.eps')
