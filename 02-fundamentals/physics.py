'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def free_fall_time(height):
    """
    Tato funkce vypočítá čas, který trvá volný pád z určité výšky na Zemi.
    :param height: Výška v metrech
    :return: Čas volného pádu v sekundách
    """
    time = (2 * height / EARTH_GRAVITY) ** 0.5
    return time

def lunar_free_fall_time(height):
    """
    Tato funkce vypočítá čas volného pádu z určité výšky na Měsíci.
    :param height: Výška v metrech
    :return: Čas volného pádu na Měsíci v sekundách
    """
    time = (2 * height / MOON_GRAVITY) ** 0.5
    return time

def time_to_travel_light_years(distance):
    """
    Tato funkce vypočítá čas, který by trval cestování světelným rokem (light-year) při rychlosti světla ve vakuu.
    :param distance: Vzdálenost v metrech
    :return: Čas cestování v sekundách
    """
    time = distance / SPEED_OF_LIGHT
    return time

def time_to_travel_sound_distance(distance):
    """
    Tato funkce vypočítá čas, který by trval cestování určitou vzdáleností rychlostí zvuku při teplotě 20 °C v suchém vzduchu.
    :param distance: Vzdálenost v metrech
    :return: Čas cestování v sekundách
    """
    time = distance / SPEED_OF_SOUND
    return time