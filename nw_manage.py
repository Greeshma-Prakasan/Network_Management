import os
from rich.console import Console

console = Console()

def interface_menu():
    interface = os.popen("ls /sys/class/net").read()
    console.print(interface,style="bold blue")

def assign_ip():
    interface_menu()
    ip = input("\tEnter the ip : ")
    inter = input("\tEnter the interface name from above menu list : ")
    ip_assign = os.popen(f"sudo ip address add {ip} dev {inter}").read()
    console.print(ip_assign,style="bold blue")
    console.print("\tSuccessfully Assigned",style="bold red") 


def delete_ip():
	interface_menu()
	ip = input("Enter the ip : ")
	inter = input("Enter the interface name from above list : ")
	del_ip = os.popen(f"sudo ip address del {ip} dev {inter}").read()
	console.print(f"{del_ip}\n\tSuccessfully Deleted",style="bold red") 

def display_ip():
	interface_menu()
	inter = input("Enter the interface name from above list : ")
	show_ip = os.popen(f"sudo ip -4 a show {inter}").read()
	console.print(show_ip,style="bold blue")
	
def display_interface():
	show_inter = os.popen(f"sudo ip l").read()
	console.print(show_inter,style="bold blue")

def config_route():
	interface_menu()
	ip = input("Enter the ip : ")
	inter = input("Enter the interface name : ")
	console.print(os.popen(f"sudo ip r add {ip} dev {inter}").read(),style="bold blue") 
	console.print("\tSuccessfully Configured",style="bold blue")
	

def turn_On_Off_interface():
	while True:
		interface_menu()
		print("\t.............Menu for turn/off interface.............")
		console.print("\t1.Turn on interface",style="bold blue")
		console.print("\t2.Turn off interface",style="bold blue")
		console.print("\t3.Exit",style="bold blue")
		ch = int(input("\tEnter the choice"))
		if ch == 1:
			inter_name = input("\tEnter the interface name from the above menu list :")
			cmd = f"sudo ip link set dev {inter_name} up" 
			on = os.popen(cmd).read()
			print("................Turn on interface................")
			print(os.popen("ip a").read())
			console.print("\tSuccessfully turned on the interface",style="bold blue")
		
		elif ch == 2:
			inter_name = input("Enter the interface name :")
			cmd = f"sudo ip link set dev {inter_name} down" 
			down = os.popen(cmd).read()
			print(".................Turn off interface........................")
			print(os.popen("ip a").read())
			console.print("\tSuccessfully turned off the interface",style="bold red")
		elif ch == 3:
			break
		else:
			console.print("\tInvalid choice",style="bold red")

def add_arp_entry():
	interface_menu()
	ip = input("Enter the ip address to add :")
	inter_name = input("Enter the interface name :")
	cmd =f"sudo ip n add {ip} lladdr 00:45:78:52:ed:55 dev {inter_name} nud permanent" 
	arp = os.popen(cmd).read()
	print(".................Adding ARP entry.......................")
	print(os.popen("ip n show").read())
	console.print("\tSuccesffuly added the arp entry",style="bold blue")

def delete_arp_entry():
	interface_menu()
	ip = input("Enter the ip address to delete :")
	inter_name = input("Enter the interface name :")
	cmd =f"sudo ip n flush {ip} dev {inter_name} nud permanent" 
	arp = os.popen(cmd).read()
	print("........................Deleting ARP entry....................")
	print(os.popen("ip n show").read())
	console.print("\tSuccessfully deleted the arp entry",style="bold red")

def restart_network():
	cmd = "sudo systemctl status  networking" 
	re_net = os.popen(cmd).read()
	print(".................Restarting network................")
	console.print(re_net,style="bold blue")

def change_hostname():
	cmd = "sudo hostname shanususanabraham" 
	change_host = os.popen(cmd).read()
	change_host_det = os.popen("hostnamectl status").read()
	print(".................Changing Host name..............")
	console.print(change_host_det,style="bold blue")

def new_dns_entry():
	dns = os.popen("sudo cat >> /etc/resolv.conf").read() 
	print(".................Adding DNS entry................")
	console.print(dns,style="bold blue")
