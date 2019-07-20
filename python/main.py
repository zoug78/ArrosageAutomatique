#   Script Lancement Arrosage Jardin
#   3 variables necessaires :
#       - Choix de la zone (1 : Herbe, 2 : potager+bambou)
#       - duree en secondes
#   exemple : lancement de la partie herbe pendant 5min --> python3 main.py 1 300

import RPi.GPIO as GPIO
import time
import sys
import tqdm
import logging

def checkVariables():
  if len(sys.argv) < 3:
    print("variable(s) d'entree(s) manquante(s)")
    logging.error("variable(s) d'entree(s) manquante(s)")
    sys.exit()

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


def main():
  try:
      logging.basicConfig(filename='/var/log/arrosage/arrosage.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
      checkVariables()
      duree=int(sys.argv[2])
      if sys.argv[1]=="1":
        type="herbe"
        electrovannes=[2,3]
      else:
        type="potager"
        electrovannes=[4]

      logging.warning("""
    ------------------------------------------------
             Activation de l'arrosage

           - Lancement de l'arrosage partie : """ + type + """
           - Duree : """ + str(duree) + """
    ------------------------------------------------
    """)

      logging.warning("Activation en mode 'BCM'")
      GPIO.setmode(GPIO.BCM)

      launch(electrovannes,"launch")

      for i in tqdm.tqdm(range(duree)):
        time.sleep(1)

      launch(electrovannes,"stop")

      logging.warning("Remise a zero des entrees/sorties")
      GPIO.cleanup()
  except Exception as e:
    print("error : " + e)
    GPIO.cleanup()
    logging.warning("Error : " + e)

if __name__ == '__main__':
    main()
