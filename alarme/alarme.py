from playsound import playsound 
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarme(segundos):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < segundos:
        time.sleep(1)
        time_elapsed += 1

        time_left = segundos - time_elapsed
        minutos_left = time_left // 60
        segundos_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}O alarme irá disparar em: {minutos_left:02d}:{segundos_left:02d}")

    playsound("alarme.mp3")

minutos = int(input ("Quantos minutos devo aguardar? "))
segundos = int(input ("Quantos segundos devo aguardar? "))
total_segundos = minutos * 60 + segundos
alarme(total_segundos)