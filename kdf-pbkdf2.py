import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Salts should be randomly generated
salt = os.urandom(16)
password = '1234mysupersecretkey'
print('Salt: ', salt.hex())
print('Password: ', password)

# derive
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256(),
  length=32,
  salt=salt,
  iterations=1_200_000,
)
key = kdf.derive(password.encode())
print('Generated key: ', key.hex())

# verify
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256(),
  length=32,
  salt=salt,
  iterations=1_200_000,
)
kdf.verify(password.encode(), key)
print('key verified. 검증 성공')