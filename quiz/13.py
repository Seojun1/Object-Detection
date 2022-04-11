from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel, QVBoxLayout, QFileDialog
import sys

# cnt GUI에 나타내기 (미충족)
class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.group_box = QGroupBox('그룹 1')
        self.group_box2 = QGroupBox('그룹 2')

        self.button1 = QPushButton('open_file')
        self.button1.clicked.connect(self.button1_click)

        self.pixmap_label = QLabel(self)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.pixmap_label)

        self.group_box.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)

        self.setLayout(self.main_layout)

    def button1_click(self):
        # getOpenFileName의 속성들 : self, 창 제목, 초기 이미지 폴더 지정, 필터링(선택 가능한 파일 확장자 지정)
        path, _ = QFileDialog.getOpenFileName(self, '제목', '..', 'Image File (*.png, *.jpg)') # path, _ 둘 다 변수임
        if path == '':
            print('취소')
        else:
            print('PATH : ', path)
            self.img = ''
            self.img = str(path)
            # print(self.img)
            pixmap = QPixmap(self.img)  # Pixmap은 잠깐쓰기 때문에 self 안붙여도됨
            self.pixmap_label.setPixmap(pixmap)  # 이미지 적용

if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())