from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi
import os


class MonApplication(QMainWindow):
    def __init__(self):
        super(MonApplication, self).__init__()
        
        self.setWindowTitle("KSP trajectories")
        self.setWindowIcon(QIcon("interface/logo.png"))
        loadUi(localPath + "/interface/KSP.ui", self)
        self.comboBoxAstreCible.addItem("Moho")
        self.comboBoxAstreCible.addItem("Eve")
        self.comboBoxAstreCible.addItem("Kerbin")
        self.comboBoxAstreCible.addItem("Duna")
        self.comboBoxAstreCible.addItem("Dres")
        self.comboBoxAstreCible.addItem("Jool")
        self.comboBoxAstreCible.addItem("Eeloo")
        self.comboBoxAstreCible.currentIndexChanged.connect(self.getComboBoxAstreCibleChanged)

        self.comboBoxAstreDepart.addItem("Moho")
        self.comboBoxAstreDepart.addItem("Eve")
        self.comboBoxAstreDepart.addItem("Kerbin")
        self.comboBoxAstreDepart.addItem("Duna")
        self.comboBoxAstreDepart.addItem("Dres")
        self.comboBoxAstreDepart.addItem("Jool")
        self.comboBoxAstreDepart.addItem("Eeloo")
        self.comboBoxAstreDepart.currentIndexChanged.connect(self.getComboBoxAstreDepartChanged)



    def getComboBoxAstreCibleChanged(self):
        selected_item = self.comboBoxAstreCible.currentText()
        print(f"Sélection Astre Cible: {selected_item}")
        return selected_item

    def getComboBoxAstreDepartChanged(self):
        selected_item = self.comboBoxAstreDepart.currentText()
        print(f"Sélection Astre Départ: {selected_item}")
        return selected_item

localPath = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__': 
    os.system("cls")
    app = QApplication([]) 
    fenetre = MonApplication()
    fenetre.show() 
    app.exec_()