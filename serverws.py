from db import accessToDB
import socket, json, time, os, datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

access = accessToDB.accesSql("localhost", "root", "", "acdb")
my_socket = socket.socket()
my_socket.bind(('0.0.0.0', 8000))
my_socket.listen(5)
print("[*] socket online in {}".format(socket.gethostname()))

try:
    while True:
        con, addr =my_socket.accept()
        print('[*] New connection established from {}'.format(addr))
        resp = con.recv(1024).decode()
        data = json.loads(resp)
        if(data):
            con.send('[ * ] Information received'.encode())
            for row in data:
                access.insertRegForHour(row[0], row[1], row[3], row[4])
                print(" {}, {}, {}, {}, {}".format(row[0], row[1], row[2], row[3], row[4]))
except KeyboardInterrupt:
    print('\nSaliendo..')
finally:
    time.sleep(5)
    os.system ("clear")