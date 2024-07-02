import dht
import machine
import time
import math as m
from lib.mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import lib.wifiConnection as wifi # Contains functions to connect/disconnect from WiFi
import lib.keys as k              # Contains all keys

downTime = 60*5
client = MQTTClient(k.AIO_CLIENT_ID, k.AIO_SERVER, k.AIO_PORT, k.AIO_USER, k.AIO_KEY)
client.connect()

tempSensor = dht.DHT11(machine.Pin(28))            # DHT11 Constructor 
lightSensor = machine.ADC(machine.Pin(26))         # Photoresistance Initializer
redLED  =  machine.Pin(2, mode=machine.Pin.OUT)    # Pin for red LED
greenLED = machine.Pin(3, mode=machine.Pin.OUT)    # Pin for green LED

redLED.value(0)
greenLED.value(0)
"""
while True:
    redLED.value(1)
    greenLED.value(0)
    print("RED")
    time.sleep(1)
    redLED.value(0)
    greenLED.value(1)
    print("GREEN")
    time.sleep(1)
"""


try:
    while True:
        try:
            # Perform measurements
            tempSensor.measure()
            temperature = tempSensor.temperature()
            humidity = tempSensor.humidity()

            lightData = lightSensor.read_u16()
            light = round(100 - 10*m.log(lightData), 1)    # Arbitrary units

            # Do something with the data
            print(f"The temperature is {temperature} degrees Celsius, the humidity is {humidity} % and the light is {light}.")

            client.publish(topic=k.AIO_TEMPERATURE_FEED, msg=str(temperature))
            client.publish(topic=k.AIO_HUMIDITY_FEED, msg=str(humidity))
            client.publish(topic=k.AIO_LIGHT_FEED, msg=str(light))
            
        except Exception as error:
            print("Exception occurred", error)
        time.sleep(downTime)
finally:
    client.disconnect()
    client = None
    wifi.disconnect()
    print("Disconnected from Adafruit IO.")
