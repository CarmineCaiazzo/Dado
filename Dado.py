#Programma Python per simulazione di un dado a 6 faccie.

import random 

def LancioDado():
	return random.randint(1,6)


print ("Lancia un dado di 6 faccie: ")
print ("|----------------------------|")

print ("Il Numero uscito dal lancio del dado è: " + str(LancioDado()))




