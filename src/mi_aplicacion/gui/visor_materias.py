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
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        #Creamos la caja de materias
        self.caja_materias = QGroupBox("Materia")
        distr_caja_materias = QGridLayout()
        self.caja_materias.setLayout(distr_caja_materias)

        #Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setLayout(distr_caja_botones)
        
        #Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_materias)
        self.distr_vertical.addWidget(self.caja_botones)

        #Definimos el distribuidor principal de la ventana.
        self.setLayout(self.distr_vertical)

        #Hacemos la ventana visible
        self.show()