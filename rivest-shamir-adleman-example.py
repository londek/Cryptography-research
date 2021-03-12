#!/usr/bin/env python3

from random import randint

# Mathematically:
# p = prime
# q = prime different from p

# n = pq
# phi = φ(n) = n-1 = (p*q)-1 = (p-1)(q-1)       since we are working on primes

# e = coprime of phi
# d = d ≡ e^−1 (mod phi) or de ≡ 1 mod phi 


# We are working on small numbers here - just to show the concept
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29]

def generate_prime():
	return primes[randint(0, len(primes)-1)]

def gcd(a, b):
	small = 0
	gcd = 1
	if a > b:
		small = b
	else:
		small = a
	for i in range(2, small + 1):
		if a%i==0 and b%i==0:
			gcd = i
	return gcd

def modular_inverse(a, c):
	b = 1
	while a * b % c != 1:
		b += 1
	return b

def generate_e(phi):
	for i in range(2, phi):
		if gcd(i, phi) == 1:
			return i
	raise Exception("Could not generate e from phi") 

def decrypt(c, d, n):
	return pow(c, d) % n

def encrypt(m, e, n):
	return pow(m, e) % n

p = generate_prime()
q = generate_prime()

# Ensure q is different from p
while q == p:
	q = generate_prime()

n = p*q
# Since p, q are primes, phi of pq is (p-1)(q-1)
phi = (p-1)*(q-1)

# Public key
e = generate_e(phi)

# Private key
d = modular_inverse(e, phi)

# Ensure 1 < chosen_msg < n
# So we don't have to split message to blocks (Our message will be exactly one block)
chosen_msg = randint(1, n-1)
c = encrypt(chosen_msg, e, n)
m = decrypt(c, d, n)


print()
print("PRIMES:")
print("p = {0}".format(str(p)))
print("q = {0}".format(str(q)))

print()
print("PRIVATE KEY:")
print("n = {0}".format(str(n)))
print("e = {0}".format(str(e)))

print()
print("PUBLIC KEY:")
print("n = {0}".format(str(n)))
print("d = {0}".format(str(d)))

print()
print("TEST ENC/DEC:")
print("Chosen message = {0}".format(str(chosen_msg)))
print("c              = {0}".format(str(c)))
print("m              = {0}".format(str(m)))

print()
if chosen_msg == m:
	print("Successful decryption/encryption? Yes")
else:
	print("Successful decryption/encryption? No")