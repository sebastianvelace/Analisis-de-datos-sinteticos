import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle('Ventana básica PyQt5')
    win.setGeometry(100, 100, 400, 250)  # x, y, width, height
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
