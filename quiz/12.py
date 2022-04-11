from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel, QVBoxLayout
import sys

# cnt GUI에 나타내기 (미충족)

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.group_box = QGroupBox('그룹 1')
        self.group_box2 = QGroupBox('그룹 2')

        self.button1 = QPushButton('-')
        self.button2 = QPushButton('+')

        self.button2.clicked.connect(self.btn_plus)
        self.button1.clicked.connect(self.btn_minus)

        self.cnt = 0
        self.text_label = QLabel(self)
        self.text_label.setText(str(self.cnt))

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label)

        self.group_box.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)

        self.setLayout(self.main_layout)

    def btn_plus(self):
        self.cnt += 1
        print(self.cnt)
    def btn_minus(self):
        self.cnt -= 1
        print(self.cnt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())