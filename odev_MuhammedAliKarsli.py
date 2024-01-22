import matplotlib
import matplotlib.pylab as plt
import math as m
import numpy as np   #fffffurkan

# parametreler

v = 30
g = 9.8
t = np.arange(0.0, 5.0, 0.05)
theta = []

for i in range(10):
    ekle = (i)*m.pi/36
    theta.append(m.pi/6 + ekle)

# =========================================

def konum(aci, zaman, v, g):
    x = v*zaman*m.cos(aci)
    y = v*zaman*m.sin(aci) - (1/2)*g*zaman*zaman

    return x,y


fig, ax = plt.subplots()
i=0
for aci in theta: # her bir aci icin
    
    # bu aci icin olusturulacak listeleri sifirla
    listx = []
    listy = []

    # zaman vektorundeki her bir zaman icin
    for zaman in t:
        #koordinatlari hesapla
        x,y = konum(aci,zaman,v,g)
        if(y<0):
            y=0

        #listeye ekle
        listx.append(x)
        listy.append(y)
                         
    #grafige ekleme
    ax.plot(listx,listy,label="{}°".format(30+5*i))
    i += 1
    #plt.gca().legend() 

# her bir atisin grafigini ekle
ax = plt.gca()

ax.set_xlim([0, 100])
ax.set_ylim([0, 50])
plt.xlabel("Mesafe")
plt.ylabel("Yukseklik")
plt.title("Balistik Atis Grafigi")

plt.gca().legend()    #bu satir gerekli! yeri çok fark etmedi
plt.show() # Bir gorselde goster

print("en uzaga giden kirmizi, 45 derecelik aci")