from typing import List, Tuple

# 키 스퀘어 만들기
def generate_key_square(key: str) -> List[List[str]]:
    key = key.upper().replace('J', 'I')
    seen = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    # 나머지 알파벳 채우기
    for code in range(ord('A'), ord('Z') + 1):
        ch = chr(code)
        if ch == 'J':  # J는 I와 합침
            continue
        if ch not in seen:
            seen.append(ch)
    # 5x5 매트릭스 만들기
    square = [seen[i*5:(i+1)*5] for i in range(5)]
    return square

# 문자 위치 찾기
def find_position(square: List[List[str]], ch: str) -> Tuple[int,int]:
    ch = 'I' if ch == 'J' else ch
    for r in range(5):
        for c in range(5):
            if square[r][c] == ch:
                return r, c
    raise ValueError(f"{ch} 문자를 키 스퀘어에서 찾을 수 없음")

# 평문 전처리 (짝 만들기)
def preprocess_plaintext(text: str, pad_char: str = 'X') -> List[Tuple[str,str]]:
    letters = [ch.upper() for ch in text if ch.isalpha()]
    letters = [ 'I' if ch == 'J' else ch for ch in letters ]
    digraphs = []
    i = 0
    while i < len(letters):
        a = letters[i]
        if i+1 < len(letters):
            b = letters[i+1]
            if a == b:  # 같은 글자면 X 끼워넣기
                digraphs.append((a, pad_char))
                i += 1
            else:
                digraphs.append((a, b))
                i += 2
        else:  # 홀수면 마지막에 X 추가
            digraphs.append((a, pad_char))
            i += 1
    return digraphs

# 쌍 암호화
def encrypt_pair(square, a, b):
    ra, ca = find_position(square, a)
    rb, cb = find_position(square, b)
    if ra == rb:  # 같은 행
        return (square[ra][(ca+1)%5], square[rb][(cb+1)%5])
    elif ca == cb:  # 같은 열
        return (square[(ra+1)%5][ca], square[(rb+1)%5][cb])
    else:  # 직사각형
        return (square[ra][cb], square[rb][ca])

# 쌍 복호화
def decrypt_pair(square, a, b):
    ra, ca = find_position(square, a)
    rb, cb = find_position(square, b)
    if ra == rb:  # 같은 행
        return (square[ra][(ca-1)%5], square[rb][(cb-1)%5])
    elif ca == cb:  # 같은 열
        return (square[(ra-1)%5][ca], square[(rb-1)%5][cb])
    else:  # 직사각형
        return (square[ra][cb], square[rb][ca])

# 전체 암호화
def encrypt(plain: str, key: str, pad_char='X') -> str:
    square = generate_key_square(key)
    digraphs = preprocess_plaintext(plain, pad_char)
    cipher_pairs = [encrypt_pair(square, a, b) for a, b in digraphs]
    return ''.join(a+b for a,b in cipher_pairs)

# 전체 복호화
def decrypt(cipher: str, key: str) -> str:
    square = generate_key_square(key)
    cipher = ''.join(ch.upper() for ch in cipher if ch.isalpha())
    pairs = [(cipher[i], cipher[i+1]) for i in range(0, len(cipher), 2)]
    plain_pairs = [decrypt_pair(square, a, b) for a,b in pairs]
    return ''.join(a+b for a,b in plain_pairs)

# 실행 예시
if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = "HELLO WORLD"
    print("키:", key)
    print("평문:", plaintext)

    cipher = encrypt(plaintext, key)
    print("암호문:", cipher)

    decrypted = decrypt(cipher, key)
    print("복호화 결과:", decrypted)
