from db import accessToDB
import socket, json, time, os

access = accessToDB.accesSql("localhost", "root", "", "acdb")
my_socket = socket.socket()
my_socket.bind(('0.0.0.0', 8000))
my_socket.listen(5)
print("[*] socket online in {}".format(socket.gethostname()))

try:
    while True:
        con, addr =my_socket.accept()
        print('[*] New connection established from {}'.format(addr))
        date = con.recv(1024).decode()
        data = access.selectRegforhour(date)
        send_data = json.dumps(data)

        if(con.send(send_data.encode())):
            print('[*] {}'.format(con.recv(1024).decode()))
            con.close()
        else:
            print('[!] Error sending data')

except KeyboardInterrupt:
    print('\nSaliendo..')
finally:
    time.sleep(5)
    os.system ("clear")