def monoalphabetic_encrypt(text, key_map):
  encrypted_text = ""
  # 평문을 소문자로 변환하여 일관성을 유지
  text = text.lower()
  for char in text:
    # 알파벳인 경우에만 치환
    if 'a' <= char <= 'z':
      encrypted_text += key_map.get(char, char)
    else:
      # 알파벳이 아닌 문자는 그대로 유지 (공백, 구두점 등)
      encrypted_text += char
  return encrypted_text

def monoalphabetic_decrypt(encrypted_text, key_map):
  decrypted_text = ""
  # 복호화를 위해 키 맵의 키-값 순서를 반전
  reverse_key_map = {v: k for k, v in key_map.items()}

  for char in encrypted_text:
    # 알파벳인 경우에만 치환
    if 'a' <= char <= 'z':
      decrypted_text += reverse_key_map.get(char, char)
    else:
      # 알파벳이 아닌 문자는 그대로 유지
      decrypted_text += char
  return decrypted_text

# --- 사용 예시 ---

# 치환 맵 (키) 정의
# 'a'는 'x'로, 'b'는 'n'으로... 고정적으로 치환됩니다.
encryption_key = {
  'a': 'x', 'b': 'n', 'c': 'c', 'd': 'p', 'e': 'y',
  'f': 'v', 'g': 'z', 'h': 'q', 'i': 'j', 'k': 'm',
  'l': 'o', 'm': 'l', 'n': 'u', 'o': 'h', 'p': 'g',
  'q': 'w', 'r': 'f', 's': 'd', 't': 'r', 'u': 'i',
  'v': 's', 'w': 'a', 'x': 'b', 'y': 'k', 'z': 't',
}

# 평문
plain_text = "hello world"

# 암호화
encrypted_text = monoalphabetic_encrypt(plain_text, encryption_key)
print(f"평문: {plain_text}")
print(f"암호화된 텍스트: {encrypted_text}")

# 복호화
decrypted_text = monoalphabetic_decrypt(encrypted_text, encryption_key)
print(f"암호문: {encrypted_text}")
print(f"복호화된 텍스트: {decrypted_text}")
