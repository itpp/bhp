import sys, socket, getopt, threading, subprocess

# define some global variables

listen				= False
command				= False
upload				= False
execute				= ""
target				= ""
upload_destination	= ""
port				= 0


def usage():
	print ("BHP Net Tool")
	print
	print("Usage: bhpnet.py -t target_host -p port")
	print("-l --listen						- listen on [host]:[port] for incoming connections")
	print("-e --execute=file_to_run			- execute the given file upon receiving a connction")
	print("-c --command						- initialize a command shell")
	print("-u --upload=upload_destination	- upon receiving connection upload a file and write to [destination]")
	print()
	print()
	print("Examples: ")
	print("bhpnet.py -t 192.168.1.1 -p 5555 -l -c")
	print("bhpnet.py -t 192.168.1.1 -p 5555 -l -u=/root/target.bin")
	print("bhpnet.py -t 192.168.1.1 -p 5555 -l -e=\"cat /etc/passwd\"")
	print("echo 'ABCDEFGH' | ./bhpnet.py -t 192.168.1.1 -p 135")
	sys.exit(0)

def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()