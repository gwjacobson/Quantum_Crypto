import random
import sympy
import math
from math import gcd


#variables for public and private keys
primes = list(sympy.primerange(0,50))

p1 = random.choice(primes) #first prime
p2 = random.choice(primes) #second prime

n = p1*p2 #large prime for public key

phi = (p1 - 1)*(p2 - 1) #Euler's totient
print('phi: '+str(phi)+', n: '+str(n)+', p1: '+str(p1)+', p2:'+str(p2))

#find the exponent for the private key
#e is a coprime of phi
for e in range(2, phi):
	if gcd(phi, e) == 1:
		break

#this is the private key
for d in range(2,1000):
	if (d*e) % phi == 1:
		break

print('Your private key is: '+str(d))
print('Your public key is: '+str(n)+', '+str(e))

message = input('Enter your message: ') #user inputs message to encrypt
mess_int = int(message) #change message into int
print('Your message is: '+str(mess_int))

c = pow(mess_int, e, n) #encrypted message
print('The encrypted message is: '+str(c))

m = pow(c, d, n) #the decrypted message
print('The decrypted message is: '+str(m))