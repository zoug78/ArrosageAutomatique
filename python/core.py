#   Script Lancement Arrosage Jardin
#   3 variables necessaires :
#       - Choix de la zone (1 : Herbe, 2 : potager+bambou)
#       - duree en secondes
#   exemple : lancement de la partie herbe pendant 5min --> python3 main.py 1 300

import RPi.GPIO as GPIO
import time
import sys
import threading
import tqdm
import logging


def launch(electrovannes,action):
  for electrovanne in electrovannes:
    GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
    if action == "launch":
      logging.warning("Lancement de l'electrovanne " + str(electrovanne) + "...")
      GPIO.output(electrovanne, GPIO.LOW)
      logging.warning("Electrovanne " + str(electrovanne) + " lancee")
      
    else:
      logging.warning("Arret de l'electrovanne " + str(electrovanne) + "...")
      GPIO.output(electrovanne, GPIO.HIGH)
      logging.warning("Electrovanne " + str(electrovanne) + " coupee")

def stop_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(3, GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(4, GPIO.OUT,initial=GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)
    GPIO.cleanup()
    return "stopped"

def timer(duree):
    time.sleep(duree)
    stop_gpio()

def main(action,mode,temps):
  try:
      logging.basicConfig(filename='/var/log/arrosage/arrosage.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
      duree=temps
      if action == "off":
          return stop_gpio()
      if mode=="herbe":
        electrovannes=[2,3]
      elif mode=="potager":
        electrovannes=[4]
      else:
        return "bad mode"

      logging.warning("""
    ------------------------------------------------
             Activation de l'arrosage

           - Lancement de l'arrosage partie : """ + mode + """
           - Duree : """ + str(duree) + """
    ------------------------------------------------
    """)

      logging.warning("Activation en mode 'BCM'")
      GPIO.setmode(GPIO.BCM)

      launch(electrovannes,"launch")
      threading.Thread(target=timer, args=(duree,)).start()
      return "well done"

  except Exception as e:
    print("error : " , str(e))
    GPIO.cleanup()
    logging.warning("Error : " , str(e))

