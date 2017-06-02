import numpy as np
import sys
sys.path.append('/home/hb407/reports/FirstYearReport/figures/')
from matplotlibParameters import * 
import os

matplotlibSetup()

fig =plt.figure(figsize=(6.25,4.25))
gs = gridspec.GridSpec(2,1, height_ratios=[5,1])
plt.gcf().subplots_adjust(bottom=0.12)
fig.subplots_adjust(hspace=0.13)

ax1 = fig.add_subplot(gs[0])
ax1.set_ylim([-75.1,-73.9])
#ax1.set_yticks(np.arange(-7.9,-6.9,0.1))
ax1.set_xlim([50,290])
plt.setp(ax1.get_yticklabels(), visible=True)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$')
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.9, box.height])

ax2 = fig.add_subplot(gs[1], sharex=ax1)
ax2.set_ylim([-0,6])
ax2.set_xlim([50,290])
ax2.set_yticks(np.arange(0.0,7,2.0))
ax2.set_xticks(np.arange(50,300,25))
plt.setp(ax2.get_yticklabels())
plt.setp(ax2.get_xticklabels(), visible=True)
ax2.set_xlabel(r'O-H Bond Length / pm')
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.9, box.height])

fileList = os.listdir('./')
print fileList
fileList.sort()
print fileList
for f in fileList:
    if 'real_RHF' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo_RHF' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')
    if 'NOCI.dat' in f:
        data = np.genfromtxt(f)
        for i in range(1,7):
            ax1.plot(data[:,0].T,data[:,i],c='g')
    if 'FCI.dat' in f:
        data = np.genfromtxt(f)
        print data.shape
        for i in range(1,2):
            ax1.plot(data[::10,0].T,data[::10,i],ls='None',marker='x',c='k')
    if 'ERROR.dat' in f:
        data = np.genfromtxt(f)
        ax2.plot(data[::5,0].T,data[::5,1],c='b')

ax1.plot([0],[0],c='r',linewidth=1,label=r'RHF')
ax1.plot([0],[0],c='m',linewidth=1,label=r'h-RHF')
ax1.plot([0],[0],c='g',linewidth=1,label=r'NOCI')
ax1.plot([0],[0],c='k',linestyle='None', marker='x',label=r'FCI')
ax1.legend(loc='upper right', bbox_to_anchor=(1.24, 0.6),
          fancybox=True, ncol=1, fontsize=10)
ax2.text(225,3,r'$E_0^{\mathrm{NOCI}} - E_0^{\mathrm{FCI}} / \mathrm{mE_{h}}$',fontsize=9)


fig.savefig('H2O_sto-3g_NOCI_RHF.eps')
