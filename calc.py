import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt
class Calculator(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
  def initUI(self):
    self.setWindowTitle('간단한 계산기')
    # 메인 레이아웃 (수직)
    main_layout = QVBoxLayout()

    # 수식 입력 레이아웃 (수평)
    equation_layout = QHBoxLayout()
    self.equation_label = QLabel('수식 입력:')
    self.equation_input = QLineEdit(self)
    self.equation_input.setPlaceholderText('예: 10 + 5')

    # 라벨과 입력창을 수평으로 배치
    equation_layout.addWidget(self.equation_label)
    equation_layout.addWidget(self.equation_input)

    # 계산 결과 레이아웃 (수평)
    result_layout = QHBoxLayout()
    self.result_label_title = QLabel('계산 결과:')
    self.result_label = QLabel('')
    self.result_label.setStyleSheet("font-size: 16px; font-weight: bold; color: blue;")

    # '결과' 라벨을 왼쪽 정렬하고, 남은 공간을 확장하여 빈 공간을 없앱니다.
    self.result_label.setAlignment(Qt.AlignLeft)

    # 라벨과 결과값을 수평으로 배치
    result_layout.addWidget(self.result_label_title)
    result_layout.addWidget(self.result_label)
    result_layout.addStretch()  # 이 부분이 핵심입니다.
    # main_layout에 수평 레이아웃들을 추가
    main_layout.addLayout(equation_layout)
    main_layout.addLayout(result_layout)
    self.setLayout(main_layout)
    # 시그널 연결:
    self.equation_input.returnPressed.connect(self.calculate)
  def calculate(self):
    try:
      equation = self.equation_input.text()
      if not equation.strip():
        self.result_label.setText('오류: 수식을 입력하세요.')
        return

      result = eval(equation)

      self.result_label.setText(f'{equation} = {result}')
    except (SyntaxError, NameError, ZeroDivisionError) as e:
      self.result_label.setText(f'오류: {e}')
    except Exception as e:
      self.result_label.setText(f'알 수 없는 오류: {e}')
if __name__ == '__main__':
  app = QApplication(sys.argv)
  calculator = Calculator()
  calculator.show()
  sys.exit(app.exec_())
