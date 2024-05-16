import os
import binascii

# Générer une clé secrète aléatoire
secret_key = binascii.hexlify(os.urandom(24)).decode()
print(secret_key)