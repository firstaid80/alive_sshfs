import os
import socket


mediabrain = '10.0.0.19'

if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((mediabrain,22)) == 0:
	if not os.path.ismount("/media/mediabrain"):
		os.system("sshfs -o allow_other peter@10.0.0.19:/media/peter/ /media/mediabrain/")
