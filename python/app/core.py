#   Script Lancement Arrosage Jardin
#   3 variables necessaires :
#       - Choix de la zone (1 : Herbe, 2 : potager+bambou)
#       - duree en secondes
#   exemple : lancement de la partie herbe pendant 5min --> python3 main.py 1 300

# import RPi.GPIO as GPIO
import time
import sys
import threading
import tqdm
import logging
from . import gpio

def stop_gpio():
    gpio.stop_gpio()
    return "stopped"

def timer(duree):
    time.sleep(duree)
    stop_gpio()

def main(action,mode,temps):
  try:
      duree=temps
      if action == "off":
          return stop_gpio()
      if mode=="herbe":
        gpio.startElectrovanneHerbe()
      elif mode=="potager":
        gpio.startElectrovannePotager()
      else:
        return "bad mode"

      logging.info("""
    ------------------------------------------------
             Activation de l'arrosage

           - Lancement de l'arrosage partie : """ + mode + """
           - Duree : """ + str(duree) + """
    ------------------------------------------------
    """)

      threading.Thread(target=timer, args=(duree,)).start()
      return "well done"

  except Exception as e:
    print("error : " , str(e))
    stop_gpio
    logging.error("Error : " , str(e))

def getStatus():
    return gpio.get_status()