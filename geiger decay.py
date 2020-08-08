
import numpy as np
import datetime as dt
import winsound
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time
plt.style.use("ggplot")
fig = plt.figure()
ax=fig.add_subplot(1,1,1)
T=[]
Nuclei=[]

N=80                                # number of nucleons
L=0.005                             # decay constant (L)* 10^6 s
def animate(i,T,Nuclei,L):
    global N
    T.append(dt.datetime.now().strftime('%M:%S.%f')[:-6])
    Nuclei.append(N)
    Nd=0 #decayed particles
    for n in range(N+1):
        r= random.random()
        if (r<L):
            Nd=Nd+1
            winsound.Beep(800,100)  #BEEP sound after every decay
    N=N-Nd
    time.sleep(0.2)
    ax.clear()
    ax.plot(T,Nuclei)
    ax.set_xlabel("system Time")
    ax.set_ylabel("# of Nuclei")
    start, end = ax.get_xlim()
    stepsize=abs((end-start)/10)
    ax.xaxis.set_ticks(np.arange(start, end, stepsize))
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title("virtual GM counter")
ani = animation.FuncAnimation(fig, animate, fargs=(T,Nuclei,L), interval=100)  #live plot
plt.show()
