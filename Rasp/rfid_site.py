from mfrc522 import SimpleMFRC522
import webbrowser
import time

reader = SimpleMFRC522()

print("Aproxime a tag...")

try:
    while True:
        id, text = reader.read()
        print("ID lido:", id)

        # Se a tag é a correta, abre o site
        if id == 1234567890:   # <-- troque pelo ID da sua tag
            print("Abrindo site...")
            webbrowser.open("https://www.google.com")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Finalizado")
