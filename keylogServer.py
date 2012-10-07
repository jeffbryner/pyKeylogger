import socket
import sys
from optparse import OptionParser


def printable():
    #regular string.printable includes \n \t, etc which is a pain to escape.
    return ''.join([chr(byte) for byte in range(256) \
                    if len(repr(chr(byte))) == 3 or byte == ord('\\')])

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", dest='server', default='0.0.0.0', help="IP address to listen on")
    parser.add_option("-p", dest='port', default=6666,type='int', help="port number")
    (options,args) = parser.parse_args()

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((options.server, options.port))
    
    while True:
        data, addr = sock.recvfrom(1) # buffer size
        if data in printable():
            sys.stdout.write("%s"% (data))
        else:
            sys.stdout.write("chr(%s)"% (ord(data)))
        sys.stdout.flush()