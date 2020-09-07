import random
import sympy


#create the public and private keys. Public key can be sent to anyone
#wanting to send a message or seen by others. The private key is used to
#decrypt the message. Returns a private key.
def KeyDef(n, phi, e):
	k = 0 #value to make private key an int
	for i in range(1, 100): #finding value of k
		if ((i*phi+1)/e) % 1 == 0:
			k = i
			break
		else:
			continue
	return ((k*phi+1)/e) #private key

#Encrypt a inputted message. The message comes in as an int and will be made into
#an encrypted using n and e. It will return the encrypted message, c.
def Encrypt(m, n, e):
	return (m**e) % n

#Decrypt a message, c, using d and n. This will return a decrypted
#message.
def Decrypt(c, d, n):
	return (c**d) % n

#variables for public and private keys
primes = list(sympy.primerange(0,1000000))

p1 = random.choice(primes) #first prime
p2 = random.choice(primes) #second prime

n = p1*p2 #large prime for public key

phi = (p1 - 1)*(p2 - 1) #Euler's totient

e = 0 #exponent for encrypt and decrypt
for i in range(1, 100): #smallest number where phi/e and phi don't share factor
	a = phi
	b = phi/i
	if i % 2 != 0:
		if a % i == b % i == 0:
			continue
		else:
			e = i
			break
	else:
		continue

d = KeyDef(n, phi, e) #find private key

print('Your private key is: '+str(d))
print('Your public key is: '+str(n)+', '+str(e))

message = input('Enter your message: ') #user inputs message to encrypt
print('Your message is: '+message)

mess_int = int(message) #change message into int

c = Encrypt(mess_int, n, e) #encrypted message
print('The encrypted message is: '+str(c))

m = Decrypt(c, d, n) #the decrypted message
m = int(round(m))
print('The decrypted message is: '+str(m))