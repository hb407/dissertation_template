import numpy as np
import sys
sys.path.append('/home/hb407/reports/FirstYearReport/figures/')
from matplotlibParameters import * 
import os

matplotlibSetup()

fig =plt.figure(figsize=(7,3))
plt.gcf().subplots_adjust(bottom=0.28)

ax1 = fig.add_subplot(131)
ax1.set_ylim([-3,1.0])
ax1.set_xlim([49,401])
plt.setp(ax1.get_yticklabels(), visible=True)
plt.setp(ax1.get_xticklabels())
ax1.set_xlabel(r'Bond Length / pm')
ax1.set_ylabel(r'Energy / $\mathrm{E_{h}}$')
ax1.set_title(r'$Z = 1.00\ \mathrm{a.u.}$')

for f in os.listdir('./z1-00'):
    f = './z1-00/'+f
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax1.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')

ax2 = fig.add_subplot(132, sharey=ax1)
ax2.set_ylim([-3,1.0])
ax2.set_xlim([49,401])
plt.setp(ax2.get_yticklabels(), visible=False)
plt.setp(ax2.get_xticklabels())
ax2.set_xlabel(r'Bond Length / pm')
ax2.set_title(r'$Z = 1.25\ \mathrm{a.u.}$')
ax2.plot([0],[0],c='r',label=r'RHF')
ax2.plot([0],[0],c='m',label=r'h-RHF')

for f in os.listdir('./z1-25'):
    f = './z1-25/'+f
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax2.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax2.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')

ax3 = fig.add_subplot(133, sharey=ax1)
ax3.set_ylim([-3,1.0])
ax3.set_xlim([49,401])
plt.setp(ax3.get_yticklabels(), visible=False)
plt.setp(ax3.get_xticklabels())
ax3.set_xlabel(r'Bond Length / pm')
ax3.set_title(r'$Z = 2.00\ \mathrm{a.u.}$')

for f in os.listdir('./z2-00'):
    f = './z2-00/'+f
    if 'real' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax3.plot(data[:,0].T,data[:,1].T,c='r')
    if 'holo' in f:
        data = np.genfromtxt(f)
        if data.size>0:
            ax3.plot(data[:,0].T,data[:,1].T,c='m',linestyle='-')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22),
          fancybox=True, ncol=2, fontsize=10)

fig.subplots_adjust(wspace=0.15, hspace=0.)

fig.savefig('HZ_r_vary.eps')
