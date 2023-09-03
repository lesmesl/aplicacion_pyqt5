from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout

class Aplicacion_Gui(QWidget):

    def __init__(self):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        self.inicializar_GUI()

    def inicializar_GUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()