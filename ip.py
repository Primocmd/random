import requests,re,os,time
from time import sleep as sp
import json
from bs4 import BeautifulSoup as parser

def clear():
	os.system('clear')
def line():
	print (51*'-')
def logo():
	logo =('''
______  ______  _______  _______  _______
|   __ \|   __ \|_     _||   |   ||       |
|    __/|      < _|   |_ |       ||   -   |
|___|   |___|__||_______||__|_|__||_______|
P          R          I          M          O
---------------------------------------------------
[   IP UNBLOCKER   ]
[   FREE TO USE    ]	
---------------------------------------------------''')
	print(logo)

class iAmIPClass:
	def __init__(self):
		self.ip_check_url = "http://ip-api.com/json/"
		self.ip_unblock_url= 'https://updraftplus.com/unblock-ip-address/'
	def iAmMenu(self):
		clear();logo()
		print(" [•] IP UNBLOCKER")
		line()
		print(' [1] UNBLOCK MANUALLY \n [2] UNBLOCK NET IP AUTO')
		line()
		m = input(' [•] Choose: ')
		if m in ['1','01']:self.manual()
		else:self.iAmIPChecker()
	def manual(self):
		clear();logo()
		print(' [•] UNBLOCK DEV IP ')
		print(' [•] GO TO DEVICE SETTINGS/ABOUT DEVICE ')
		print(' [•] Copy your device ip address from About ')
		line ()
		ip = input(' [•] Paste your device IP here : ')
		line()
		self.iAmIPUnblocker(ip)
	def iAmIPChecker(self):
		clear();logo()
		print(" [•] Use Flight Mode 5 Seconds Before Start .")
		input(" [•] PRESS ENTER TO START ...")
		sp(2)
		print(" [•] Detecting YourIP Address ...")
		try:
			getting_network_ip = requests.get(self.ip_check_url).json()
			ip = getting_network_ip["query"]
			print(f" [•] Your Public IP Address : {ip}")
			self.iAmIPUnblocker(str(ip))
		except requests.exceptions.ConnectionError:
			print(' [•] Check Your Internet Failed to detect ip ')
		except KeyError:
			print(' [•] Please Change your network !! ..')
		except Exception as e:
			print(e)
				#open("/sdcard/iprespo.txt","w").write(r)
	def iAmIPUnblocker(self,x):
		print(" [•] Trying To Unblock Your IP Address ...")
		try:
			r2 = requests.get(self.ip_unblock_url).text
		except requests.exceptions.ConnectionError:
			print(' [•] Check Your Internet Faild To Unblock Your IP Adddresss ')
		data={}
		ud_unblock_ip = x
		nonce= re.search('name="nonce" value="(.*?)"',r2).group(1)
		data.update(
			{
'ud_unblock_ip':ud_unblock_ip,
'nonce':nonce,
			}
			)
		try:
			po = requests.post(self.ip_unblock_url,data=data).text
		except requests.exceptions.ConnectionError:
			print(' [•] Check Your Internet Faild To Unblock Your IP Adddresss ')
		if "Your IP has been successfully unblocked" in po:
			print(" [•] IP Unblocked SuccessFully ")
			line()
			exit()
		elif "This IP address has been recently unblocked. If it has become blocked again, then you must raise a manual support request." in po:
			exit(" [•] IP Address already unblocked ")
		else:
			pass
			#rint(" [•] We are failed to unblock your IP Address")

if __name__=="__main__":
		iAmIPClass().iAmMenu()
		