from WSLib.helper import StrData
import socket

class GetConnection(StrData):
    
    def __init__(self):
        StrData.__init__(self)
        
    def pushData(self,Apikey,NodeName):
        HeadUrl = "http://emoncms.org/input/post?node={:s}&json=".format(NodeName)
        PowerDataPayload = "Voltage:{0:s},Current:{1:s},Power:{2:s},".format(self.Volts, self.Current, self.Power)
        MeteoDataPayload = "Temperature:{0:s},Humidity:{1:s},Pressure:{2:s},Lux:{3:s},UVindex:{4:s}".format(self.AirTemperature, self.Humidity, self.BaroPressure, self.Lux, self.UV)
        EndURL = "&time={0:s}&apikey={1:s}" .format(self.UnixTime, Apikey)
        return self.getHttp(HeadUrl + "{" + PowerDataPayload + MeteoDataPayload + "}" + EndURL)
    
    @property    
    def ddns(self):
        token = "9e7b546f-798b-4e4d-bdc4-8b71c76827ef"
        domain = "ws32"
        return self.getHttp("https://www.duckdns.org/update?domains=" + domain + "&token=" + token)
        
    def getHttp(self, url):
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        while True:
            data = s.recv(100)
            if data:
              #print(str(data, 'utf8'), end='')
              print(url)
            else:
              break
        s.close()
        
       

  
    






