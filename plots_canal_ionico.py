import numpy as np
import matplotlib.pyplot as plt


datos=np.genfromtxt("Canal_ionico.txt")
datos2=np.genfromtxt("Canal_ionico1.txt")
parametros=np.genfromtxt("datos.txt")
x=datos[:,0]
y=datos[:,1]

x1=datos2[:,0]
y1=datos2[:,1]


p1=parametros[:,0]
p2=parametros[:,1]
r=parametros[:,2]

p11=parametros[:,3]
p21=parametros[:,4]
r1=parametros[:,5]

count, bins, ignored =plt.hist(p1, 20, normed=True)
plt.xlabel("Posibles numeros para la coordenada x caso 1")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('p1.png', bbox_inches='tight')
plt.clf()

count, bins, ignored =plt.hist(p2, 20, normed=True)
plt.xlabel("Posibles numeros para la coordenada y caso 1")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('p2.png', bbox_inches='tight')
plt.clf()

count, bins, ignored =plt.hist(p11, 20, normed=True)
plt.xlabel("Posibles numeros para la coordenada x caso 2")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('p11.png', bbox_inches='tight')
plt.clf()

count, bins, ignored =plt.hist(p21, 20, normed=True)
plt.xlabel("Posibles numeros para la coordenada y caso 2")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('p21.png', bbox_inches='tight')
plt.clf()



count, bins, ignored =plt.hist(r, 20, normed=True)
plt.xlabel("Posibles numeros para el radio caso 1")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('r.png', bbox_inches='tight')
plt.clf()


count, bins, ignored =plt.hist(r1, 20, normed=True)
plt.xlabel("Posibles numeros para el radio caso 2")
plt.ylabel("Probabilidad de ser correcto")
plt.savefig('r1.png', bbox_inches='tight')
plt.clf()

fig=plt.figure(1)
ax=fig.add_subplot(2,1,1)
plt.axis('equal')
plt.title('Membranas')
plt.ylabel('y (Ångström)')
circ=plt.Circle((p1[3999], p2[3999]), radius=(r[3999]), color='g', fill=False)
plt.scatter(x,y)
sp1,sp2,sr=str(p1[3999]),str(p2[3999]),str(r[3999])
plt.text(20,10,s="parámetros:x="+sp1[:4]+" y:"+sp2[:4]+" r:"+sr[:4])
ax.add_patch(circ)

ax1=fig.add_subplot(2,1,2)
plt.axis('equal')
plt.xlabel('x (Ångström)')
plt.ylabel('y (Ångström)')
circ1=plt.Circle((p11[3999], p21[3999]), radius=(r1[3999]), color='r', fill=False)
plt.scatter(x1,y1)
sp1,sp2,sr=str(p11[3999]),str(p21[3999]),str(r1[3999])
plt.text(20,10,s="parámetros:x="+sp1[:4]+" y:"+sp2[:4]+" r:"+sr[:4])
ax1.add_patch(circ1)

plt.savefig('membrana.png', bbox_inches='tight')


  




 





