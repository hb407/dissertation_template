import numpy as np
import sys
sys.path.append('/home/hb407/reports/FirstYearReport/figures/')
from matplotlibParameters import * 
import os
import warnings

warnings.filterwarnings('error')
matplotlibSetup()

fig =plt.figure(figsize=(6.5,3.5))
plt.gcf().subplots_adjust(bottom=0.15)

ax1 = fig.add_subplot(121)
ax1.set_ylim([-1.3,2.2])
ax1.set_xlim([50,400])
plt.setp(ax1.get_yticklabels(), visible=True)
plt.setp(ax1.get_xticklabels())
ax1.set_xlabel(r'Bond Length / pm')
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$')

ax2 = fig.add_subplot(122)
ax2.set_ylim([-1.3,2.2])
ax2.set_xlim([50,400])
plt.setp(ax2.get_yticklabels(), visible=False)
plt.setp(ax2.get_xticklabels())
ax2.set_xlabel(r'Bond Length / pm')

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

    if 'real_all_RHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax2.plot(data[:,0].T,data[:,1].T,c='r',linestyle='-')
        except UserWarning:
            os.remove(f)
    if 'holo_all_RHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax2.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')
        except UserWarning:
            os.remove(f)
    if 'real_all_UHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax2.plot(data[:,0].T,data[:,1].T,c='b',linestyle='-')
        except UserWarning:
            os.remove(f)
    if 'holo_all_UHF' in f:
        try:
            data = np.genfromtxt(f)
            if data.size>0:
                ax2.plot(data[:,0].T,data[:,1].T,c='c',linestyle='-')
        except UserWarning:
            os.remove(f)
ax2.plot([0],[0],c='r',label=r'RHF')
ax2.plot([0],[0],c='m',label=r'h-RHF')
ax2.plot([0],[0],c='b',label=r'UHF')
ax2.plot([0],[0],c='c',label=r'h-UHF')

ax2.legend(loc='upper right', bbox_to_anchor=(0.97, 0.97),
          fancybox=True, ncol=2, fontsize=matplotlib.rcParams['axes.labelsize'])

fig.subplots_adjust(wspace=0.15, hspace=0.)
fig.savefig('H2_3-21g.eps')
