import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# 송신자
password = '1234mysupersecret'
salt = os.urandom(16)
it = 120
print('Password: ', password)
print('Salt: ', salt.hex())

# 송신자 키생섬
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256(),
  length=32,
  salt=salt,
  iterations=1_200_000,
)
key = kdf.derive(password.encode())
print('Generated key: ', key.hex())

# 수신자 키생성
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256(),
  length=32,
  salt=salt,
  iterations=1_200_000,
)
kdf.verify(password.encode(), key)
print('Generated key: ', key.hex())