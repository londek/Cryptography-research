#!/usr/bin/env python3

from random import randint

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29]

def generate_prime():
	return primes[randint(0, len(primes))]

def gcd(a, b):
	small = 0
	gcd = 1
	if a > b:
		small = b
	else:
		small = a
	for i in range(2, small + 1):
		if a%i==0 and y%i==0:
			gcd = i
	return gcd

def generate_e(phi):
	for i in range(2, phi):
		if gcd(i, phi) == 1:
			return i
	raise Exception("Could not generate e from phi") 


p = generate_prime()
q = generate_prime()

N = p*q
phi = (p-1)*(q-1)
