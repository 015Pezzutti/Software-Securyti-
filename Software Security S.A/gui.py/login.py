from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox # type: ignore
from services.authentication import authenticate_user # type: ignore

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login - Sistema de Gerenciamento')
        self.setFixedSize(300, 150)
        layout = QVBoxLayout()

        self.username_label = QLabel('Usuário:')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Senha:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if authenticate_user(username, password):
            from gui.dashboard import DashboardWindow # type: ignore
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Erro', 'Usuário ou senha inválidos')
