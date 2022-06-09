#This is a basic program to find the ip address of the system or any webserver.
#It is a simple program using socket.
#socket is a library used for connections with nodes.It is used for networking.
import socket as sc #Importing socket to program
print("Which IP address do you want to gather?")
print("1.My_Host_System\t\t2.Webserver_In_The_Internet")
userselection=input("[+] " )
if(userselection=='1' or userselection=='My_Host_System'):
    Hostname=sc.gethostname() #socket.gethostname() Helps to get the name of the running host.
    print("The Host Name Of Your Pc Is \n [+]" + Hostname)
    ipaddr=sc.gethostbyname(Hostname)#socket.gethostbyname() Helps to get ip Of host inside the constructor
    print("The Ip Address Of Your Host Is \n [+]" + ipaddr)

elif(userselection=='2' or userselection=='Webserver_In_The_Internet'):
    url=input("Enter The URL Of The Website \n [+]")
    web_ip=sc.gethostbyname(url)
    print("The IP Address Is \n [+]" + web_ip)

else:
    print("Enter An Correct Command")