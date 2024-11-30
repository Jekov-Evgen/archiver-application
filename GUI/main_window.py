from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox
from GUI.style.style_Qt import CONST_MAIN_WINDOW

def pop_up_window(title : str, text : str):
    window = QMessageBox()
    window.setWindowIcon(QIcon(r"image\icon.webp"))
    window.setWindowTitle(title)
    window.setText(text)
    window.exec()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Архиватор файлов")
        self.setFixedSize(350, 250)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        greetings = QLabel(text="Вам надо выбрать файлы для архивации")
        file_selection = QPushButton(text="Выбрать файлы")
        
        control_UI.addWidget(greetings, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(file_selection)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def dialog_box(self):
        try:
            file_path = QFileDialog.getOpenFileNames(self, "Выбор файлов")
        except:
            pop_up_window("Ошибка", "Произошла ошибка при поучении пути файлов")
        
        