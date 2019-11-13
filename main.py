from db import accessToDB
import serial, time, json, socket, datetime
from datetime import date

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

instance = accessToDB.accesSql('localhost', 'root', '', 'acdb')
instance.insertAC('G81', 25, 0)

line = serial.Serial('/dev/ttyACM0', 9600)
today = date.today()
print(today)
try:    
    while True:
        read = str(line.readline())
        if(read):
            temp = float(read[4:9])
            state = int(read[2])
            instance.insertRegForHour('G81', temp, state, state)
            print("[* ] DATOS INSERTADOS")
            print("[ *] ID_AC = {}, Temperatura : {}, Estado(on/of): {}, sensor de movimiento: {}".format("G81", temp, state, state))

            send_data = json.dumps(instance.selectRegforhour(today), default=myconverter)
            my_socket = socket.socket()

            my_socket.connect(('192.168.0.16', 8000))
            if(my_socket.send(send_data.encode())):
                print('[*] {}'.format(my_socket.recv(1024).decode()))
                my_socket.close()
            else:
                print('[!] Error sending data')
            
except KeyboardInterrupt:
    print('\nSaliendo...')
    



