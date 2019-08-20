import json

electrovannesHerbe = {
    2: "off",
    3: "off"
}

electrovannesPotager = {
    4: "off"
}


def stop_gpio():
    print('connecting to GPIO')
    print('Stopping GPIO')
    for electrovanne in electrovannesHerbe:
        electrovannesHerbe[electrovanne] = "off"
    for electrovanne in electrovannesPotager:
        electrovannesPotager[electrovanne] = "off"
    print('exiting GPIO')
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(2, GPIO.OUT,initial=GPIO.HIGH)
    # GPIO.setup(3, GPIO.OUT,initial=GPIO.HIGH)
    # GPIO.setup(4, GPIO.OUT,initial=GPIO.HIGH)
    # GPIO.output(2, GPIO.HIGH)
    # GPIO.output(3, GPIO.HIGH)
    
    # GPIO.output(4, GPIO.HIGH)
    # GPIO.cleanup() """
    print('-------------------------')
    return "stopped"

def startElectrovanneHerbe():
    print('connecting to GPIO')
    for electrovanne in electrovannesHerbe:
        print('connecting electrovanne ', str(electrovanne))
        print('starting electrovanne ', str(electrovanne))
        electrovannesHerbe[electrovanne] = "on"
    print('exiting GPIO')
    #GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
    #GPIO.output(electrovanne, GPIO.LOW)
    print('-------------------------')

def startElectrovannePotager():
    print('connecting to GPIO')
    for electrovanne in electrovannesPotager:
        print('connecting electrovanne ', str(electrovanne))
        print('starting electrovanne ', str(electrovanne))
        electrovannesPotager[electrovanne] = "on"
    print('exiting GPIO')
    #GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
    #GPIO.output(electrovanne, GPIO.LOW)
    print('-------------------------')

# def stop_electrovanne(number):
#     print('connecting to GPIO')
#     print('connecting electrovanne ', str(number))
#     #GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
#     print('stoping electrovanne ', str(number))
#     electrovannesMock[number] = "off"
#     #GPIO.output(electrovanne, GPIO.HIGH)
#     print('exiting GPIO')
#     print('-------------------------')

def get_status():
    print('returning GPIO status ')
    print('-------------------------')
    return {'herbe': str(electrovannesHerbe), 'potager': str(electrovannesPotager)}
