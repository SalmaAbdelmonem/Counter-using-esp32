import machine
import time


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

while 1:
  if(reset_button.value()==1 and inc_button.value()==0 and dec_button.value() == 0) :
     counter = 0
     print(counter)
     time.sleep(0.5)
  elif(inc_button.value()==1 and reset_button.value()==0 and dec_button.value() == 0):
     if(counter == 9):
         counter = -1
     counter = counter + 1
     print(counter)
     time.sleep(0.5)
  elif(dec_button.value() == 1 and reset_button.value()==0 and inc_button.value()==0): 
     if(counter == 0):
         counter = 10
     counter = counter - 1
     print(counter)
     time.sleep(0.5)
  else:
    counter = counter
  
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
   





