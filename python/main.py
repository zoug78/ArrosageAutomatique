#   Script Lancement Arrosage Jardin
#   3 variables necessaires :
#       - Choix de la zone (1 : Herbe, 2 : potager+bambou)
#       - durée en secondes
#   exemple : lancement de la partie herbe pendant 5min --> python3 main.py 1 300

import RPi.GPIO as GPIO
import time
import sys
import tqdm

def checkVariables():
  if len(sys.argv) < 3:
    print("variable(s) d'entree(s) manquante(s)")
    sys.exit()

def launch(electrovannes,action):
  for electrovanne in electrovannes:
    GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
    if action == "launch":
      print("Lancement de l'electrovanne " + str(electrovanne) + "...")
      GPIO.output(electrovanne, GPIO.LOW)
      print("Electrovanne " + str(electrovanne) + " lancee")
      
    else:
      print("Arret de l'electrovanne " + str(electrovanne) + "...")
      GPIO.output(electrovanne, GPIO.HIGH)
      print("Electrovanne " + str(electrovanne) + " coupee")


def main():
  checkVariables()
  duree=int(sys.argv[2])
  if sys.argv[1]=="1":
    type="herbe"
    electrovannes=[2,3]
  else:
    type="potager"
    electrovannes=[4]

  print("""
------------------------------------------------
         Activation de l'arrosage

       - Lancement de l'arrosage partie : """ + type + """
       - Duree : """ + str(duree) + """
------------------------------------------------
""")

  print("Activation en mode 'BCM'")
  GPIO.setmode(GPIO.BCM)

  launch(electrovannes,"launch")

  for i in tqdm.tqdm(range(duree)):
    time.sleep(1)

  launch(electrovannes,"stop")

  print("Remise a zero des entrees/sorties")
  GPIO.cleanup()

main()
