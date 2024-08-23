import sys
from PyQt5.QtWidgets import QApplication # type: ignore
from gui.login import LoginWindow # type: ignore

def main():
    app = QApplication(sys.argv)
    
    # Carregar estilo
    with open("gui/styles.qss", "r") as style_file:
        app.setStyleSheet(style_file.read())

    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
