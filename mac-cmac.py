import base64
import os
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.exceptions import InvalidSignature

# CMAC 생성 (송신자)
key = os.urandom(16) 
message = 'Message, 메시지인증코드테스트'
c = cmac.CMAC(algorithms.AES(key))
c.update(message.encode('utf-8'))
signature = c.finalize()
print('Key(base64): ',base64.b64encode(key).decode())
print('Key(hex): ', key.hex())
print('Message: ', message)
print('Signatrue: ',signature.hex())

# 송신자->수신자 (message, signatrue) 전송

# CMAC 검증 (수신자) 
key1 = key
try:
  c = cmac.CMAC(algorithms.AES(key))
  c.update(message.encode('utf-8'))
  c.verify(signature)
  print("검증 성공")
except InvalidSignature:
  print("검증 실패: 서명이 유효하지 않습니다.")
