def print_multiplication_table():
  cell_width = 5
  separator_line = '-' * ((cell_width + 1) * 10 - 1)

  # 헤더 행을 출력합니다.
  print(separator_line)
  print(f'{"X":^{cell_width}}', end=' ')
  for i in range(1, 10):
    print(f'{i:^{cell_width}}', end=' ')
  print()
  print(separator_line)

  # 테이블 본문을 출력합니다.
  for i in range(1, 10):
    print(f'{i:^{cell_width}}', end=' ')
    for j in range(1, 10):
      result = i * j
      print(f'{result:^{cell_width}}', end=' ')
    print()

  # 하단 구분선을 출력합니다.
  print(separator_line)
# 함수 호출
print_multiplication_table()