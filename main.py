import sys

from PyQt5.QtWidgets import QApplication

from view.HomeController import Home


def main():
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()