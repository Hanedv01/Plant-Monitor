import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor

# Wireless network
WIFI_SSID = 'Enter your WiFi SSID'
WIFI_PASS = 'Enter your WiFi password'

## Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
#The following two fields are found under the yellow key button in adafruit
AIO_USER = "Enter your username"
AIO_KEY = "Enter your key"
#These fields are found under each feed but should have the form "Username/feeds/Feed name"
AIO_TEMPERATURE_FEED = "Enter your address to the temperature feed"
AIO_HUMIDITY_FEED = "Enter your address to the humidity feed"
AIO_LIGHT_FEED = "Enter your address to the light feed"