import lib.keys as k              # Contain all keys used here
import lib.wifiConnection as wifi # Contains functions to connect/disconnect from WiFi 
from lib.mqtt import MQTTClient

try:
    ip = wifi.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

#client = MQTTClient(k.AIO_CLIENT_ID, k.AIO_SERVER, k.AIO_PORT, k.AIO_USER, k.AIO_KEY)
#client.connect()