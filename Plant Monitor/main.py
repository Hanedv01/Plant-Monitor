import dht
import machine
import time
import math as m
from lib.mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import lib.keys as k

downTime = 60
client = MQTTClient(k.AIO_CLIENT_ID, k.AIO_SERVER, k.AIO_PORT, k.AIO_USER, k.AIO_KEY)
client.connect()

tempSensor = dht.DHT11(machine.Pin(28))     # DHT11 Constructor 
lightSensor = machine.ADC(machine.Pin(26))  # Photoresistance Initializer

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
    wifiConnection.disconnect()
    print("Disconnected from Adafruit IO.")
