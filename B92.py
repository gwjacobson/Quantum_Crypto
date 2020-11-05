from qiskit import *
from numpy import pi
import random
import string

#implementation of B92 QKD protocol

bits = [0,1] #classical bits alice can choose

a = [] #initialize alices bit string
for i in range(0,8): #choose random bit string
    curr_bit = random.choice(bits)
    a.append(curr_bit)

print("Alice's String: "+str(a))

qc = QuantumCircuit(8) #create 8 quibit circuit for 8 bits
for qubit in range(8): #apply basis on each qubit
    if a[qubit] == 1: #diagonal basis on 1 bit
        qc.h(qubit)
    else: #computational basis on 0 bit
        continue

a_prime = [] #initial Bobs bit string
for i in range(8):
    curr_bit = random.choice(bits)
    a_prime.append(curr_bit)

print("Bob's String: "+str(a_prime))

