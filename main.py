from db import accessToDB
import serial, time

instance = accessToDB.accesSql('localhost', 'root', '', 'acdb')
instance.insertAC('G81', 25, 0)

line = serial.Serial('/dev/ttyACM0', 9600)
try:    
    while True:
        read = str(line.readline())
        if(read):
            temp = float(read[4:9])
            state = int(read[2])
            instance.insertRegForHour('G81', temp, state, state)
            print("[* ] DATOS INSERTADOS")
            print("[ *] ID_AC = {}, Temperatura : {}, Estado(on/of): {}, sensor de movimiento: {}".format("G81", temp, state, estate))
            
except KeyboardInterrupt:
    print('\nSaliendo...')
    



