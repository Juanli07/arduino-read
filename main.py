from db import accessToDB
import serial, time

instance = accessToDB.accesSql('localhost', 'root', '', 'acdb')
instance.insertAC('G81', 25, 0)

line = serial.Serial('/dev/ttyACM0', 9600)

while True:
    read = str(line.readline())
    if(read):
        temp = float(read[4:9])
        state = int(read[2])
        instance.insertRegForHour('G81', state, state)




