import socket,time,subprocess,os,sys
# creating socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# binding socket
# address 
myaddress=("127.0.0.1",8889) 
try :
    s.bind(myaddress) # local binding 
    os_type=sys.platform
    os_data=s.recvfrom(10)
    print("sending os details to client ")
    s.sendto(os_type.encode('ascii'), os_data[1])

    while True:
        # receiving data 
        data=s.recvfrom(100)
        # extracing data 
        cmd=data[0].decode('ascii')
        # checking command existance 
        status=os.system(cmd + ' &>/dev/null')
        if status == 0 :
            print("command found ")
            print(subprocess.getoutput(cmd))
            # sending respose to client 
            rply=cmd+" execution done check result on server side"
            time.sleep(1)
            s.sendto(rply.encode('ascii'), data[1])
        else :
            print("Command not found ")
            rply=cmd+" execution Not done "
            time.sleep(1)
            s.sendto(rply.encode('ascii'), data[1])

except : 
    print("socket binding failed ..")
    time.sleep(1)
    print("check your Port number ")


s.close() # closing socket 