import socket
import sys
import datetime
import os

#dom's network
'''
HOST = "192.168.2.91"
PORT = 10000
'''

#yamez network
#HOST = "192.168.86.41"
HOST = "10.0.0.167"
PORT = 80

SAVE_FILE = "eng.data"

def await_client_data(s):
	connection, address = s.accept()

	with connection:
		while True:
			data = connection.recv(1024)
			if not data:
				break

			return data

	return b"None"

def save_data(data):
	print("SAVING:", data)

	with open(SAVE_FILE, "a") as f:
		f.write(data + "\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	print("CONNECTED TO %s:%d" % (HOST, PORT))
	s.bind((HOST, PORT))
	s.listen(5)

	while True:
		data = await_client_data(s)
		print("RECIEVED", data)

		decoded = data.decode("utf-8").strip()
		if decoded != "None":
			things = decoded.split(',')

			command = things[0]
			if command == "close":
				sys.exit(0);

			if len(things) >= 3:
				save_data("time:" + str(datetime.datetime.now()) + " " + things[1] + " " + things[2])
