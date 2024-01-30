from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd
import utime
import machine
import time
import neopixel

led = Pin(25, Pin.OUT)
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)
np = neopixel.NeoPixel(machine.Pin(13), 8)

adcpin = 4
sensor = machine.ADC(adcpin)

def schrijven(text):
    lcd.clear()
    lcd.putstr(text)
    utime.sleep(1)

def online():
    np[0] = [0, 255, 0]
    np[1] = [0, 255, 0]
    np[2] = [0, 255, 0]
    np[3] = [0, 255, 0]
    np[4] = [0, 255, 0]
    np[5] = [0, 255, 0]
    np[6] = [0, 255, 0]
    np[7] = [0, 255, 0]

    np.write()

def offline():
    np[0] = [255, 0, 0]
    np[1] = [255, 0, 0]
    np[2] = [255, 0, 0]
    np[3] = [255, 0, 0]
    np[4] = [255, 0, 0]
    np[5] = [255, 0, 0]
    np[6] = [255, 0, 0]
    np[7] = [255, 0, 0]

    np.write()

# Wacht op gegevens van de verbinding
while True:
    data = input()

    print("Received '" + data + "'.")
    if data == "clear":
        lcd.clear()
    if data == 'start_scherm':
        schrijven("Welkom bij ons  steam project")
        offline()
    elif data == 'ingelogd':
        schrijven("Welkom bij je   dashboard")
        online()
    elif data == 'games_library':
        schrijven("Kies een game!")
    elif data == 'login':
        schrijven("Login S.V.P")
        offline()
    elif data == 'friends':
        schrijven("Wie is er online of offline?")
    # elif data == '2':
    #     # print("Temperature.")
    #     temperature = krijg_temperatuur()
    #     print(f"De temperatuur is {temperature} C")
    #     time.sleep(5)
