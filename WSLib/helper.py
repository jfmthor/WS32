from machine import I2C, Pin, ADC
from WSLib.bme280 import BME280
from WSLib.bh1750 import BH1750
from WSLib.ina219 import INA219
from WSLib.at24c32n import AT24C32N
from WSLib.ds3231 import DS3231

i2c = I2C(scl=Pin(22), sda=Pin(21))
adc = ADC(Pin(34))
adc.atten(adc.ATTN_11DB)
adc.width(adc.WIDTH_12BIT)
VREF_12BIT = 0.9523809523809524


bme280Sensor = BME280(i2c)
bh1750Sensor = BH1750(i2c)
ina219Sensor = INA219(i2c)
at24c32 = AT24C32N(i2c)
Ds3231 = DS3231(i2c)



class GetUnixTime:
    def __init__(self):
      self.UnixTime = str(Ds3231.get_time(1))

class PowerData:
  
    def __init__(self,
                 Volts=ina219Sensor.readV(),
                 Current=ina219Sensor.readI()):
                   
      self.Volts = Volts
      self.Current = Current
      self.Power = Volts * Current
             
class MeteoData:
   
    def __init__(self,
                Lux=bh1750Sensor.luminance(BH1750.ONCE_HIRES_1),
                BaroPressure=bme280Sensor.pressure,
                AirTemperature=bme280Sensor.temp,
                Humidity=bme280Sensor.humidity,
                Uv=adc.read()):
     
      self.Lux = Lux
      self.BaroPressure = BaroPressure
      self.AirTemperature = AirTemperature
      self.Humidity = Humidity
      self.Ml8511 = (Uv * VREF_12BIT)/1000
      
    
    def map(self,x, in_min, in_max, out_min, out_max):
      return float((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
      
      
     
class StrData(MeteoData, PowerData, GetUnixTime):
  
    def __init__(self):
        GetUnixTime.__init__(self)
        PowerData.__init__(self)
        MeteoData.__init__(self)
        super().__init__()
        self.Lux = str(self.Lux)
        self.BaroPressure = str(self.BaroPressure)
        self.AirTemperature = str(self.AirTemperature)
        self.Humidity = str(self.Humidity)
        self.Volts = str(self.Volts)
        self.Current = str(self.Current)
        self.Power = str(self.Power)     
        self.UnixTime = str(self.UnixTime)
        self.UV = str(self.map(self.Ml8511, 0.99, 2.8, 0, 15))

class RTCtime:
        
    def updateTime(self):
      Ds3231.save_time(1)
      return Ds3231.get_time()
      
    def getTime(self):
      Ds3231.get_time()
      return Ds3231.get_time()
     
