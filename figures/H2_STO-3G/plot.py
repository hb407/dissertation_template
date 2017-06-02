import numpy as np
import sys
sys.path.append('/home/hb407/reports/FirstYearReport/figures/')
from matplotlibParameters import * 
import os
import warnings

warnings.filterwarnings('error')
matplotlibSetup()

fig =plt.figure(figsize=(6.,3.5))
plt.gcf().subplots_adjust(bottom=0.15)

ax1 = fig.add_subplot(111)
ax1.set_ylim([-1.2,0.2])
ax1.set_xlim([50,400])
plt.setp(ax1.get_yticklabels(), visible=True)
plt.setp(ax1.get_xticklabels())
ax1.set_xlabel(r'Bond Length / pm')
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$')

for f in os.listdir('./'):
    if 'real_RHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax1.plot(data[:,0].T,data[:,1].T,c='r',linestyle='-')
        except UserWarning:
            os.remove(f)
    if 'holo_RHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax1.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')
        except UserWarning:
            os.remove(f)
    if 'real_UHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax1.plot(data[:,0].T,data[:,1].T,c='b',linestyle='-')
        except UserWarning:
            os.remove(f)
    if 'holo_UHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax1.plot(data[:,0].T,data[:,1].T,c='c',linestyle='-')
        except UserWarning:
            os.remove(f)
ax1.plot([0],[0],c='r',label=r'RHF')
ax1.plot([0],[0],c='m',label=r'h-RHF')
ax1.plot([0],[0],c='b',label=r'UHF')
ax1.plot([0],[0],c='c',label=r'h-UHF')

ax1.legend(loc='upper right', bbox_to_anchor=(0.97, 0.97),
          fancybox=True, ncol=2, fontsize=matplotlib.rcParams['axes.labelsize'])

fig.savefig('H2_sto-3g.eps')
