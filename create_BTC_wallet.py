from bitcoin import random_key, privtopub, pubtoaddr

private_key = random_key()
public_key = privtopub(private_key)
address = pubtoaddr(public_key)

print("Private key: ", private_key)
print("Public key:", public_key)
print("Bitcoin address: ", address)