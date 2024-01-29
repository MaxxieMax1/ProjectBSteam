from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd
import utime
import machine
import time

led = Pin(25, Pin.OUT)
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)

adcpin = 4
sensor = machine.ADC(adcpin)

def schrijven(text):
    lcd.clear()
    lcd.putstr(text)
    utime.sleep(1)

# Wacht op gegevens van de verbinding
while True:
    data = input()

    print("Received '" + data + "'.")
    if data == "clear":
        lcd.clear()
    if data == 'start_scherm':
        schrijven("Welkom bij ons  steam project")
    elif data == 'ingelogd':
        schrijven("Welkom bij je   dashboard")
    elif data == 'games_library':
        schrijven("Kies een game!")
    elif data == 'login':
        schrijven("Login S.V.P")
    elif data == 'friends':
        schrijven("Wie is er online of offline?")
    # elif data == '2':
    #     # print("Temperature.")
    #     temperature = krijg_temperatuur()
    #     print(f"De temperatuur is {temperature} C")
    #     time.sleep(5)
