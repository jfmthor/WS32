from machine import Pin
import network
import webrepl
import utime
import os
from WSLib.nethelp import GetConnection

ws_wifi = network.WLAN(network.STA_IF)
led = Pin(2, Pin.OUT)

if not ws_wifi.isconnected():
    ws_wifi.active(True)
    ws_wifi.connect('Boyz', '27854112Ca')
    while not ws_wifi.isconnected():
        led.value(0)
        utime.sleep_ms(500)
        led.value(1)
        utime.sleep_ms(500)
        pass
print('Local ip network:', ws_wifi.ifconfig())
led.value(1)

webrepl.start()

get = GetConnection()
get.ddns




