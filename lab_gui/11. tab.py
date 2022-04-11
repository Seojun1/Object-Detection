from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QVBoxLayout, QGridLayout, QLabel
import sys


class ClassificationAIButton(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('버튼 1')
        self.button2 = QPushButton('버튼 2')
        self.button3 = QPushButton('버튼 3')

        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)
        self.button3.clicked.connect(self.button3_click)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.button1, 0, 0, 1, 2)
        self.main_layout.addWidget(self.button2, 1, 0, 1, 1)
        self.main_layout.addWidget(self.button3, 1, 1, 1, 1)

        self.setLayout(self.main_layout)


    def button1_click(self):
        self.button1.setEnabled(False)
        self.button1.setText('버튼 1 클릭')


    def button2_click(self):
        self.button2.setEnabled(False)
        self.button2.setText('버튼 2 클릭')


    def button3_click(self):
        self.button3.setEnabled(False)
        self.button3.setText('버튼 3 클릭')


class ClassificationAIText(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_label = QLabel(self)
        self.text_label.setText('Text')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.text_label)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.vbox_layout, 0, 0, 1, 1)

        self.setLayout(self.main_layout)


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        button1_tab = QPushButton('버튼 1')
        button2_tab = QPushButton('버튼 2')


        button = ClassificationAIButton()
        text = ClassificationAIText()

        tabs = QTabWidget()
        tabs.addTab(button, '버튼')
        tabs.addTab(text, '텍스트')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())