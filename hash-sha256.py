from cryptography.hazmat.primitives import hashes

message = "hash test. 해시함수 테스트... "
print("Message: ", message) 

# SHA1 해시 계산
digest = hashes.Hash(hashes.SHA1())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA1 해시: ", hash_value.hex())

# SHA256 해시 계산
digest = hashes.Hash(hashes.SHA256())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA256 해시: ", hash_value.hex())

# SHA512 해시 계산
digest = hashes.Hash(hashes.SHA512())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA512 해시: ", hash_value.hex())

# SHA3_512 해시 계산
digest = hashes.Hash(hashes.SHA3_512())
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("SHA3_512 해시: ", hash_value.hex())

# Blake2b 해시 계산
digest = hashes.Hash(hashes.BLAKE2b(64))
digest.update(message.encode('utf-8'))
hash_value = digest.finalize() 
print("BLAKE2b 해시: ", hash_value.hex())