
import machine
import time
try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

a = machine.Pin(16,machine.Pin.OUT)
b = machine.Pin(17,machine.Pin.OUT)
c = machine.Pin(18,machine.Pin.OUT)
d = machine.Pin(19,machine.Pin.OUT)
e = machine.Pin(21,machine.Pin.OUT)
f = machine.Pin(22,machine.Pin.OUT)
g = machine.Pin(23,machine.Pin.OUT)
inc_button = machine.Pin(34,machine.Pin.IN)
dec_button = machine.Pin(35,machine.Pin.IN)
reset_button = machine.Pin(36,machine.Pin.IN)

counter = 0



def web_page():
  
  html="""<html>
  <head> 
  <title>COUNTER</title> 
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html
  {
  font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;
  }
  p{
  font-size: 1.5rem;
  }
  .button{
  display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;
  }
  .button2{
  background-color: #4286f4;
  }
  .button3{
  background-color: #A569BD;
  }
  </style></head><body> 
  <h1>COUNTER</h1> 
  </strong></p><p><a href="/?counter0"><button class="button">Reset</button></a></p>
  <p><a href="/?counter1"><button class="button button2">Increment</button></a></p>
  <p><a href="/?counter2"><button class="button button3">Decrement</button></a></p>
  </body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while 1:
 conn, addr = s.accept()
 print('Got a connection from %s' % str(addr))
 request = conn.recv(1024)
 request = str(request)
 print('Content = %s' % request)
  
 count0 = request.find('/?counter0')
 countup = request.find('/?counter1')
 countdown = request.find('/?counter2')
  
 if(count0 == 6):
     print('Reset')
     counter = 0
     
 if(countup == 6):
     print('Increment')
     if(counter == 9):
         counter = -1
     counter = counter + 1
     
 if(countdown == 6):
     print('Decrement')
     if(counter == 0):
         counter = 10
     counter = counter - 1
     print(counter)
    
 if(counter == 0):
   a.value(1) 
   b.value(1) 
   c.value(1) 
   d.value(1) 
   e.value(1)
   f.value(1)
   g.value(0)
 elif(counter == 1):
   a.value(0)
   b.value(1)
   c.value(1)
   d.value(0)
   e.value(0)
   f.value(0)
   g.value(0)
 elif(counter == 2):
   a.value(1)
   b.value(1) 
   c.value(0)
   d.value(1)
   e.value(1)
   f.value(0)
   g.value(1)
 elif(counter == 3):
   a.value(1)
   b.value(1)
   c.value(1)
   d.value(1)

   e.value(0)
   f.value(0) 
   g.value(1)
 elif(counter == 4):
   a.value(0)
   b.value(1)
   c.value(1)
   d.value(0)

   e.value(0)
   f.value(1)
   g.value(1)
 elif(counter == 5):
   a.value(1)
   b.value(0)
   c.value(1)
   d.value(1)
   e.value(0)
   f.value(1)
   g.value(1)
 elif(counter == 6):
   a.value(1)
   b.value(0)
   c.value(1)
   d.value(1)
   e.value(1)
   f.value(1)
   g.value(1)
 elif(counter == 7):
   a.value(1)
   b.value(1)
   c.value(1)
   d.value(0)
   e.value(0)
   f.value(0)
   g.value(0)
 elif(counter == 8):
   a.value(1)
   b.value(1)
   c.value(1)
   d.value(1)
   e.value(1)
   f.value(1)
   g.value(1)
 elif(counter == 9):
   a.value(1)
   b.value(1)
   c.value(1)
   d.value(1)
   e.value(0)
   f.value(1)
   g.value(1)    
 
 response = web_page()

 conn.send('HTTP/1.1 200 OK\n')
 conn.send('Content-Type: text/html\n')
 conn.send('Connection: close\n\n')
 conn.sendall(response)
 conn.close()




