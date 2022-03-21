from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QFileDialog
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('open_file')
        self.button1.clicked.connect(self.button1_click)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.hbox_layout, 0, 0, 1, 1)

        self.setLayout(self.main_layout)

    def button1_click(self):
                # getOpenFileName의 속성들 : self, 창 제목, 초기 이미지 폴더 지정, 필터링(선택 가능한 파일 확장자 지정)
        path, _ = QFileDialog.getOpenFileName(self, '제목', '.', 'Image File (*.*)') # path, _ 둘 다 변수임
        if path == '':
            print('취소')
        else:
            print('PATH : ', path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())