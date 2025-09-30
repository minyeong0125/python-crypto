import base64
import os
from cryptography.hazmat.primitives import poly1305
from cryptography.exceptions import InvalidSignature

# Poly1305 CMAC 생성 (송신자)
key = os.urandom(32) 
message = 'Message, 메시지인증코드테스트'
p = poly1305.Poly1305(key)
p.update(message.encode('utf-8'))
signature = p.finalize()
print('Key(base64): ',base64.b64encode(key).decode())
print('Key(hex): ', key.hex())
print('Message: ', message)
print('Signatrue: ',signature.hex())

# 송신자->수신자 (message, signatrue) 전송

# Poly1305 MAC 검증 (수신자) 
key1 = key
try:
  p = poly1305.Poly1305(key)
  p.update(message.encode('utf-8'))
  p.verify(signature)
  print("검증 성공")
except InvalidSignature:
  print("검증 실패: 서명이 유효하지 않습니다.")
