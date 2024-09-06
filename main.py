from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
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
        p = self.comboBoxAstreCible.currentText()
        return p if p in astre else False

    def getComboBoxAstreDepartChanged(self):
        p = self.comboBoxAstreDepart.currentText() 
        print("---",p,"---")
        return p if p in astre else False
    
    def verifBonAstreCentral(self):
        mess = "Destination Impossible\nles deux astres \nn'orbitentpas sur \nle même astre"
        astreDepart = self.getComboBoxAstreDepartChanged()
        astreCible = self.getComboBoxAstreCibleChanged()
        if (astreCible != False) and (astreDepart != False):
            AstreD = dicoAstre[astreDepart]
            AstreC = dicoAstre[astreCible]
            if (AstreD.centre == AstreC.centre) :
                self.labelImpossible.setText("")
                angleInterAstre(AstreD, AstreC)

            elif(AstreC.centre == astreDepart) or (AstreD.centre == astreCible):
                self.labelImpossible.setText("")
                self.output.setText("Pour Lune de la Planète pas besoin d'angle")
            
            else: self.labelImpossible.setText(mess)

        else: 
            self.labelImpossible.setText("Veillez bien \nchoisir deux astres")
            self.output.setText("")
        
    
#####Fonction#####

def angleInterAstre(AstreD, AstreC):

    moyenneAstreD = fonctionCalcul.moyenne(AstreD.apo, AstreD.peri)
    moyenneAstreC = fonctionCalcul.moyenne(AstreC.apo, AstreC.peri)

    periapseOrbite = min(moyenneAstreD, moyenneAstreC)
    apoapseOrbite = max(moyenneAstreD, moyenneAstreC)

    excentriciteOrbite = fonctionCalcul.excentricite(apoapseOrbite, periapseOrbite)

    demiGrandAxeOrbite = fonctionCalcul.demi_grand_axe(excentriciteOrbite, apoapseOrbite, periapseOrbite)

    periodeOrbite = fonctionCalcul.periode(demiGrandAxeOrbite)

    angleEntreAstre = fonctionCalcul.pos_astre(periodeOrbite, AstreC.revo)
    fenetre.output.setText(str(round(angleEntreAstre, 2)) + "°")




#####Programme#####
localPath = os.path.dirname(os.path.abspath(__file__))
astre = ["Moho", "Eve", "Gilly", "Kerbin", "Mune", "Minmus", "Duna", "Ike", "Dres", "Jool", "Laythe", "Vall", "Tylo", "Bob", "Pol", "Eeloo"]

dicoAstre = {
    "Moho" : Astre(6315765981, 4210510628, "Kerbol", 0.23977770170405147),
    "Eve" : Astre(9931011387, 9734357701, "Kerbol", 0.6132301719266214),
    "Gilly" : Astre(48825000, 14175000, "Eve", 0.04048717070944184),
    "Kerbin" : Astre(13599840256, 13599840256, "Kerbol", 1.0000528169014085),
    "Mune" : Astre(12000000, 12000000, "Kerbin", 0.01433946270213876),
    "Minmus" : Astre(47000000, 47000000, "Kerbin", 0.11553724352286558),
    "Duna" : Astre(21783189163, 19669121365, "Kerbol", 1.8806566249347938),
    "Ike" : Astre(3296000, 3104000, "Duna", 0.007061733828899321),
    "Dres" : Astre(46761053692, 34917642714, "Kerbol", 5.204384645061728),
    "Jool" : Astre(72212238387, 65334882253, "Kerbol", 11.373495696400626),
    "Laythe" : Astre(27184000, 27184000, "Jool", 0.0049605503390714656),
    "Vall" : Astre(43152000, 43152000, "Jool", 0.009921155016518867),
    "Tylo" : Astre(68500000 ,68500000, "Jool", 0.02160292775169536),
    "Bob" : Astre(158697500, 98302500, "Jool", 0.05880789753955833),
    "Pol" : Astre(210624207, 149155794, "Jool", 0.09668704355764215),
    "Eeloo" : Astre(113549713200, 66687926800, "Kerbol", 17.061121109372284),
    }


if __name__ == '__main__': 
    os.system("cls")
    app = QApplication([]) 
    fenetre = MonApplication()
    fenetre.show() 
    app.exec_()