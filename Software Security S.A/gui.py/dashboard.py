from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton # type: ignore

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dashboard - Sistema de Gerenciamento')
        self.setFixedSize(800, 600)
        
        layout = QVBoxLayout()
        
        self.welcome_label = QLabel('Bem-vindo ao sistema de gerenciamento')
        layout.addWidget(self.welcome_label)

        self.manage_cameras_button = QPushButton('Gerenciar Câmeras')
        self.manage_alarms_button = QPushButton('Gerenciar Alarmes')
        self.manage_fence_button = QPushButton('Gerenciar Cerca Elétrica')
        self.manage_access_control_button = QPushButton('Controle de Acesso Facial')

        layout.addWidget(self.manage_cameras_button)
        layout.addWidget(self.manage_alarms_button)
        layout.addWidget(self.manage_fence_button)
        layout.addWidget(self.manage_access_control_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

