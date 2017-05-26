import numpy as np
import matplotlib.pyplot as plt
qmax=95.0
circuito=np.genfromtxt("CircuitoRC.txt")
t=circuito[:,0]
y=circuito[:,1]
I=100  #dado que la corriente no ha sido dada, se tiene que asumir una.
mi_t=np.linspace(0,300)

def mi_modelo(t,q,r,c):
    y=q*(1-np.exp(-t/r*c)) 
    return(y)


def likelihood(y_obs, y_model):
    chi_squared = (1.0/(40000)*2.0)*sum((y_obs-y_model)**2)
    return np.exp(-chi_squared)


r_walk = np.empty((0))
c_walk = np.empty((0))
likehoo_walk=np.empty((0))


r_walk = np.append(r_walk, np.random.random())
c_walk = np.append(c_walk, np.random.random())
y_init = mi_modelo(t,10*r_walk[0]*c_walk[0]*I  ,r_walk[0], c_walk[0])

#

likehood_walk = np.append(likehoo_walk, likelihood(y, y_init))



n_iterations = 2000 
for i in range(n_iterations):
    r_prime = np.random.normal(r_walk[i], 0.1) 
    c_prime = np.random.normal(c_walk[i], 0.1)

    y_init = mi_modelo(t,10*r_walk[i]*c_walk[i]*I , r_walk[i], c_walk[i])
    y_prime = mi_modelo(t,10*r_prime*c_prime*I ,r_prime, c_prime)
    
    likehood_prime = likelihood(y, y_prime)
    l_init = likelihood(y, y_init)
    
    
    alpha = likehood_prime/l_init
    
    if(alpha>=1.0):
        r_walk  = np.append(r_walk,r_prime)
        c_walk  = np.append(c_walk,c_prime)
        likehood_walk = np.append(likehood_walk, likehood_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            r_walk = np.append(r_walk,r_prime)
            c_walk = np.append(c_walk,c_prime)
            likehood_walk = np.append(likehood_walk, likehood_prime)
        else:
            r_walk = np.append(r_walk,r_walk[i])
            c_walk = np.append(c_walk,c_walk[i])
            likehood_walk = np.append(likehood_walk, l_init)






count, bins, ignored =plt.hist(c_walk, 20, normed=True)
plt.xlabel("Posibles numeros para la capacitancia")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('hist1.png', bbox_inches='tight')
plt.clf()

count1, bins1, ignored1 =plt.hist(r_walk, 20, normed=True)
plt.xlabel("Posibles numeros para la resistencia")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('hist2.png', bbox_inches='tight')
plt.clf()

max_likelihood_id = np.argmax(likehood_walk)
best_r = r_walk[max_likelihood_id]
best_c = c_walk[max_likelihood_id]
sc=str(best_c)
sr=str(best_r)

Qmax =   10*best_r*best_c*I         
best_y = mi_modelo(mi_t,  Qmax ,best_r,best_c)

plt.scatter(t,y)
plt.plot(mi_t, best_y,c="red")
plt.text(5,120,"R=" +sr[:8])
plt.text(5,115,"C=" +sc[:8])
plt.text(5,110,"Qmax=" +sc[:8])
plt.xlabel("tiempo (Seg)")
plt.ylabel("Carga (Coulombs)")
plt.savefig('circuito.png', bbox_inches='tight')
plt.clf()

plt.scatter(r_walk, likehood_walk)
plt.xlabel("Caminata en Resistencia")
plt.ylabel("likelihood")
plt.savefig('caminata_r.png', bbox_inches='tight')
plt.clf()

plt.scatter(c_walk, likehood_walk)
plt.xlabel("Caminata en Capacitancia")
plt.ylabel("likelihood")
plt.savefig('caminata_c.png', bbox_inches='tight')
