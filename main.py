from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi
import os


class MonApplication(QMainWindow):
    def __init__(self):
        super(MonApplication, self).__init__()
        
        self.setWindowTitle("Page de connexion")
        self.setWindowIcon()
        
        # Créer un widget central
        self.windowContent = QWidget()
        self.setCentralWidget(self.windowContent)

        loadUi(localPath + "/interface/KSP.ui", self.windowContent)


localPath = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__': 
    os.system("cls")
    app = QApplication([]) 
    fenetre = MonApplication()
    fenetre.show() 
    app.exec_()