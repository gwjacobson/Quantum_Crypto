# Quantum_Crypto

Recreation of four different cryptography algorithms to research the differences in performance and security. All four of these will be able to encrypt and decrypt a simple message for testing purposes. Slides for each algorithm included.

-RSA: First, took a look at the popular RSA algorithm from a classical sense to compare to the other three which are quantum computing algorithms. RSA involves a public and private key where the public key is known and a private key is sent between the two parties in order to encrpyt and decrypt the message. A hacker would have trouble cracking this classically because it would involve the factoring or very large prime numbers, which is compututaionally hard for classical computers.

-BB84: This was the first quantum key distribution algorithm implemented. QKD involved using a quantum channel to securely send polarizations where an eavesdropper can be detected by quantum mechanical effects such as non-cloning thereom and measurements. Two parties share a string of bits and make measurements on those bits using a certain basis. When they measure the same bits, they use that as a quantum key. If the error rate is too great, we assume there is an eavesdropper and start the process over. This key can then be used to encrypt messages and send them across any public channel.

-B92

-Ekert
