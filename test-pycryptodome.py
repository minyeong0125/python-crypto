from Crypto.Hash import SHA256

hash_object = SHA256.new(data=b"First")
#hash_object.update(b"Second")
##hash_object.update(b"Third")
print(hash_object.digest())
print(hash_object.hexdigest())