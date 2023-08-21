from bitcoin import random_key, privtopub, pubtoaddr

#Caesar cipher
def encrypt_private_key(private_key):
	encrypted_key = []
	for index, char in enumerate(private_key):
		if (index + 1) % 3 == 0:
			encrypted_key.append(chr(ord(char) + 3))
		else:
			encrypted_key.append(char)
	return ''.join(encrypted_key)

private_key = random_key()
public_key = privtopub(private_key)
address = pubtoaddr(public_key)

encrypted_private_key = encrypt_private_key(private_key)

print("Private key: ", private_key)
print("Encrypted private key: ", encrypted_private_key)
print("Public key:", public_key)
print("Bitcoin address: ", address)