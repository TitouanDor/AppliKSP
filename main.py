from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi
import os
from classAstre import Astre
import fonctionCalcul

#####Classe#####
class MonApplication(QMainWindow):
    def __init__(self):
        super(MonApplication, self).__init__()
        
        self.setWindowTitle("KSP trajectories")
        self.setWindowIcon(QIcon("interface/logo.png"))
        loadUi(localPath + "/interface/KSP.ui", self)
        for e in astre:
            self.comboBoxAstreCible.addItem(e)
            self.comboBoxAstreDepart.addItem(e)

        self.comboBoxAstreCible.currentIndexChanged.connect(self.getComboBoxAstreCibleChanged)
        self.comboBoxAstreDepart.currentIndexChanged.connect(self.getComboBoxAstreDepartChanged)
        self.pushButtonCalculer.clicked.connect(self.verifBonAstreCentral)


    def getComboBoxAstreCibleChanged(self):
        return self.comboBoxAstreCible.currentText()

    def getComboBoxAstreDepartChanged(self):
        return self.comboBoxAstreDepart.currentText()
    
    def verifBonAstreCentral(self):
        mess = "Destination Impossible\nles deux astres n'orbitent\npas sur le même astre"
        astreDepart = self.getComboBoxAstreDepartChanged()
        astreCible = self.getComboBoxAstreCibleChanged()
        AstreD = dicoAstre[astreDepart]
        AstreC = dicoAstre[astreCible]
        if (AstreD.centre == AstreC.centre) or (AstreC.centre == astreDepart) or (AstreD.centre == astreCible):
            self.labelImpossible.setText("")
            print(" Ok\n", astreDepart, "->", astreCible)
        else: self.labelImpossible.setText(mess)
        
    
#####Fonction#####
def verif_exen(dic : dict, L = []) ->list:
    for obj in dic.values(): L.append(fonctionCalcul.excentricite(obj.apo, obj.peri))
    return L





#####Programme#####
localPath = os.path.dirname(os.path.abspath(__file__))
astre = ["Moho", "Eve", "Gilly", "Kerbin", "Mune", "Minmus", "Duna", "Ike", "Dres", "Jool", "Laythe", "Vall", "Tylo", "Bob", "Pol", "Eeloo"]

#region Astre
dicoAstre = {
    "Moho" : Astre(6315765981, 4210510628, "Kerbol"),
    "Eve" : Astre(9931011387, 9734357701, "Kerbol"),
    "Gilly" : Astre(48825000, 14175000, "Eve"),
    "Kerbin" : Astre(13599840256, 13599840256, "Kerbol"),
    "Mune" : Astre(12000000, 12000000, "Kerbin"),
    "Minmus" : Astre(47000000, 47000000, "Kerbin"),
    "Duna" : Astre(21783189163, 19669121365, "Kerbol"),
    "Ike" : Astre(3296000, 3104000, "Duna"),
    "Dres" : Astre(46761053692, 34917642714, "Kerbol"),
    "Jool" : Astre(72212238387, 65334882253, "Kerbol"),
    "Laythe" : Astre(27184000, 27184000, "Jool"),
    "Vall" : Astre(43152000, 43152000, "Jool"),
    "Tylo" : Astre(68500000 ,68500000, "Jool"),
    "Bob" : Astre(158697500, 98302500, "Jool"),
    "Pol" : Astre(210624207, 149155794, "Jool"),
    "Eeloo" : Astre(113549713200, 66687926800, "Kerbol"),
    }
#endregion


if __name__ == '__main__': 
    os.system("cls")
    app = QApplication([]) 
    fenetre = MonApplication()
    fenetre.show() 
    app.exec_()