import lib.wifiConnection as wifi # Contains functions to connect/disconnect from WiFi 

try:
    ip = wifi.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")
