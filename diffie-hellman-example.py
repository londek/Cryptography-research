#!/usr/bin/env python3

from random import randint

p = 17
g = randint(2, p)

alice_secret = randint(8, 20)
alice_public = pow(g, alice_secret) % p

bob_secret = randint(8, 20)
bob_public = pow(g, bob_secret) % p

alice_shared_secret = pow(bob_public, alice_secret) % p
bob_shared_secret   = pow(alice_public, bob_secret) % p

print("prime p      = {0}".format(str(p)))
print("generator g  = {0}".format(str(g)))

print()
print("alice_secret = {0}".format(str(alice_secret)))
print("alice_public = {0}".format(str(alice_public)))

print()
print("bob_secret   = {0}".format(str(bob_secret)))
print("bob_public   = {0}".format(str(bob_public)))

print()
print("alice_shared = {0}".format(str(alice_shared_secret)))
print("bob_shared   = {0}".format(str(bob_shared_secret)))

print()
if alice_shared_secret == bob_shared_secret and alice_shared_secret != 0 and bob_shared_secret != 0:
	print("Successful communication? Yes")
else:
	print("Successful communication? No")