import nw_manage as nw
from rich.console import Console
console = Console()

def menu():
    console.print("1.Assign IP",style="bold yellow")
    console.print("2.Delete IP",style="bold yellow")
    console.print("3.Display IP",style="bold yellow")
    console.print("4.Dispaly all interfaces",style="bold yellow")
    console.print("5.Configure routing",style="bold yellow")
    console.print("6.Turn On/Off interface",style="bold yellow")
    console.print("7.Add ARP entry",style="bold yellow")
    console.print("8.Delete ARP Entry",style="bold yellow")
    console.print("9.Restart Network",style="bold yellow")
    console.print("10.Change Hostname",style="bold yellow")
    console.print("11.Add DNS server entry",style="bold yellow")
    console.print("12.Exit",style="bold yellow")
    
while True:
	menu()
	c = int(input("Enter your choice : "))
	if c == 1:
		nw.assign_ip()
	elif c == 2:
		nw.delete_ip()
	elif c == 3:
		nw.display_ip()
	elif c == 4:
		nw.display_interface()
	elif c == 5:
		nw.config_route()
	elif c == 6:
		nw.turn_On_Off_interface()
	elif c == 7:
		nw.add_arp_entry()
	elif c == 8:
		nw.delete_arp_entry()
	elif c == 9:
		nw.restart_network()
	elif c == 10:
		nw.change_hostname()
	elif c == 11:
		nw.new_dns_entry()
	elif c == 12:
		break
	else:
		console.print("Wrong choice",style="bold yellow")
