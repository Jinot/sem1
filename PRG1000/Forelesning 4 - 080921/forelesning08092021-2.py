#Oppgave 3 oppgavesett 1, med if-elif-else, tester < og starter med
#laveste karakterkategori

#Kandidatens poengsum som inndata fra bruker
poengsum=int(input('Oppgi kandidatens poengsum: '))

#Tilordning av karakter ved nøsta if, "forenkla" elif-struktur
if poengsum<40:
    karakter='F'
elif poengsum<46:
    karakter='E'
elif poengsum<58:
    karakter='D'
elif poengsum<77:
    karakter='C'
elif poengsum<92:
    karakter='B'
else:
    karakter='A'

#Skriver ut resultatet
print('Ved poengsum',poengsum,' får kandidaten karakteren ',karakter)
