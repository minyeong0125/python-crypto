def caesar_cipher_encrypt(text, key):
  encrypted_text = ""
  for char in text:
    if 'a' <= char <= 'z':
      start = ord('a')
      encrypted_char_code = (ord(char) - start + key) % 26 + start
      encrypted_text += chr(encrypted_char_code)
    elif 'A' <= char <= 'Z':
      start = ord('A')
      encrypted_char_code = (ord(char) - start + key) % 26 + start
      encrypted_text += chr(encrypted_char_code)
    else:
      encrypted_text += char
  return encrypted_text

def caesar_cipher_decrypt(text, key):
  decrypted_text = ""
  for char in text:
    if 'a' <= char <= 'z':
      start = ord('a')
      decrypted_char_code = (ord(char) - start - key) % 26 + start
      decrypted_text += chr(decrypted_char_code)
    elif 'A' <= char <= 'Z':
      start = ord('A')
      decrypted_char_code = (ord(char) - start - key) % 26 + start
      decrypted_text += chr(decrypted_char_code)
    else:
      decrypted_text += char
  return decrypted_text

plain_text = "Hello, Caesar Cipher!"
encryption_key = 6 

#암호화
cipher_text = caesar_cipher_encrypt(plain_text, encryption_key)
print(f"평문: {plain_text}")
print(f"암호화된 텍스트: {cipher_text}")

# 복호화
decrypted_text = caesar_cipher_decrypt(cipher_text, encryption_key)
print(f"복호화된 텍스트: {decrypted_text}")

# 다른 키로 시도해보기
print("\n--- 다른 키로 암호화 시도 ---")
plain_text_2 = "Python"
encryption_key_2 = 10

cipher_text_2 = caesar_cipher_encrypt(plain_text_2, encryption_key_2)
print(f"평문: {plain_text_2}")
print(f"암호화된 텍스트: {cipher_text_2}")

decrypted_text_2 = caesar_cipher_decrypt(cipher_text_2, encryption_key_2)
print(f"복호화된 텍스트: {decrypted_text_2}")
