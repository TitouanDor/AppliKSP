import math

def excentricite(apoapse : int, periapse : int): 
    """
    Fonction renvoyant l'excentricité d'une ellipse

    arguments :
        apoapse : le point de l'orbite d'un objet céleste où la distance est maximale par rapport au foyer de l'orbite (en metre)
        periapse : le point de l'orbite d'un objet céleste où la distance est minimal par rapport au foyer de l'orbite (en metre)

    variables locales :
        poly1 : premier polynome de l'équation
        poly2 : deuxième polynome de l'équation
    """
    poly1 = apoapse/periapse
    poly2 = poly1 + 1
    return 1 - (2/poly2)

def demi_grand_axe(e : float, apoapse = None, periapse = None):
    assert(type(e) == float), f"TypeError e must be float not {str(type(e))}"
    """
    fonction renvoyant la longeur du demi-grand axe de l'ellipse nommé a (en metre)

    arguments :
        e : excentricité de l'ellipse
        apoapse : le point de l'orbite d'un objet céleste où la distance est maximale par rapport au foyer de l'orbite (en metre)
        periapse : le point de l'orbite d'un objet céleste où la distance est minimal par rapport au foyer de l'orbite (en metre)
    """
    if (periapse != None): return periapse/(1-e)
    
    elif (apoapse != None): return apoapse/(1+e)

def periode(a : int) -> float:
    """
    fonction renvoyant le temps (en annee) que met un objet à faire le tour d'une ellipse

    argument :
        a : le demi-grand axe de l'ellipse (en metre)

    variables locales :
        poly1 : premier polynome de l'équation
        poly2 : deuxième polynome de l'équation
        poly3 : troisième polynome de l'équation
    """
    poly1 = 4*math.pi**2
    poly2 = a**3
    poly3 = (6.673015/(10**11))*(1.7565459*(10**28))
    return math.sqrt(poly2/(poly3/poly1))/9203545

def pos_astre(T : float, periode : float) -> float:
    """
    retourne l'angle entre l'astre de départ et l'astre viser (°)

    arguments :
        T : temps pour aller retour d'une elipse (annee)
        periode : temps d'une revolution de l'astre viser (annee)

    variable locale:
        angle : anlge entre la position initial de l'astre viser et sa position final
    """
    angle = ((T/2)*360)/periode
    return 180 - angle

def periode_entre_pos(T1 : float, T2 : float) -> float:
    """
    retourne le temps entre deux meme position entre deux planete (j)

    arguments :
        T1 : periode de revolution du premier astre (j)
        T2 : periode de revolution du second astre (j)

    variables locales:
        num : numerateur d'une division
        denom : denominateur d'une divison
    
    """
    num = T1*T2
    denom = abs(T1 - T2)
    return num/denom

def moyenne(x, y) -> float: return (x + y)/2

def airEllipse(demiPetitAxe : float, demiGrandAxe : int):
    """
    retourne l'air d'une ellipse'

    arguments :
        demiPetitAxe : demiPetitAxe de l'ellipse du transphère
        demiGrandAxe : demiGrandAxe de l'ellipse du transphère
    """
    return math.pi*demiGrandAxe*demiPetitAxe

def axeEllipse(e : float, apoapside : float):
    """
    fonction renvoyant la longeur du demi-grand axe de l'ellipse nommé a (en metre)

    arguments :
        e : excentricité de l'ellipse
        apoapse : le point de l'orbite d'un objet céleste où la distance est maximale par rapport au foyer de l'orbite (en metre)
    
    variable local :
        DGA : le demi grand axes de l'ellipse (en metre)
        DPA : le demi petit axes de l'ellipse (en metre)
    """

    DGA = apoapside/(1 + e)
    DPA = DGA*math.sqrt(1 - e**2)
    return (DGA, DPA)

def calculVitesse(GA,PA):
    """
    
    """

    air = airEllipse(PA, GA)
    per = periode(GA)*426*24*60*60 #seconde
    vitesse = air/per #m²/s




