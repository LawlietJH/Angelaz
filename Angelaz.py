# -*- coding: UTF-8 -*-
# Python 2.7
# Angelaz
# By: LawlietJH
# v1.0.2



import threading
import time
import sys
import os

try:
	
	import requests

except:
	
	print "\n\n\t [+] Instalando Dependencias... Requests ",
	os.system("python -m pip install requests > Nul")
	print "OK"
	time.sleep(3)
	os.system("Cls")



#~ =====================================================================
#~ =====================================================================
#~ =====================================================================



def Robots(Pagina):
	
	Cadena = ""
	
	try:
		
		Req = requests.get(Pagina + '/robots.txt')
		http = Req.status_code
		
		if http == 200:
			
			if '<html>' in Req.text:
				
				return "\n\n\t [-] Robots.txt No Encontrado."
				
			else:
				
				Cadena += "\n\n\t [+] Robots.txt Encontrado."
				Cadena += "\n\n\n\n [~] Contenido de Robots.txt:\n\n"
				Cadena += "================================================\n\n\n"
				Cadena +=  Req.text + "\n\n"
				Cadena += "================================================\n\n"
				
				return Cadena
		
		else: return "\n\n\t [-] Robots.txt No encontrado."
		
	except: return "\n\n\t [-] Robots.txt No encontrado."



def Escanear(Pagina, Ruta):
	
	try:
		
		Ruta = Pagina + Ruta
		Req = requests.get(Ruta)
		http = Req.status_code
			
		if http == 200:   print "\n ---> [+]  Admin Panel Encontrado: " + Ruta,						# 200 - OK.						Pagina Encontrada.
		elif http == 301: print "\n [!] [301] Movido Permanentemente: " + Ruta,						# 301 - Moved Permanently.		Pagina Movida Permanentemente.
		elif http == 302: print "\n ---> [+]  Vulnerabilidad Potencial [EAR] Encontrada: " + Ruta,	# 302 - Found.					Pagina Redireccionada.
		elif http == 401: print "\n [!] [401] Acceso No Autorizado: " + Ruta,						# 401 - Unauthorized.			Pagina No Autorizada.
		elif http == 403: print "\n [!] [403] Acceso Prohibido: " + Ruta,							# 403 - Forbidden.				Pagina Restringida.
		elif http == 404: print "\n      [-]  " + Ruta,												# 404 - Not Found.				Pagina No Encontrada.
		elif http == 410: print "\n [!] [410] Ya No Existe: " + Ruta,								# 410 - Gone.					Pagina Que Existia y No Volvera.
		elif http == 500: print "\n [!] [500] Internal Server Error: " + Ruta,						# 500 - Internal Server Error.
		else: print "\n [!] [" + str(http) + "] " + Ruta,
	
	except KeyboardInterrupt: exit(1)
	except Exception as e:
		
		if str(type(e).__name__) == "ConnectionError": print "\n   X  [!]  " + Ruta + "\t <--- Error De Coneccion.",
		else: print "\n  X   [!]  " + Ruta + "\t <--- " + str(type(e).__name__),



def Argumentos():
	
	global Pagina
	
	Args = sys.argv
	
	if len(Args) == 3:
		
		if Args[1] == "-P":
			
			Pagina = Args[2]
			
			return True
		
	elif len(Args) == 1:
		
		return True
	
	else: return False



Pagina = None

Rutas = [
'account.html', 'account.php', 'adm.html', 'adm.php', 'adm/', 'adm/admloginuser.php', 'adm/index.html', 'adm/index.php', 'adm_auth.php', 'admin',
'admin-login.html', 'admin-login.php', 'admin.html', 'admin.php', 'admin/', 'admin/account.html', 'admin/account.html', 'admin/account.php', 'admin/account.php', 'admin/admin-login.html',
'admin/admin-login.php', 'admin/admin.html', 'admin/admin.php', 'admin/adminLogin.html', 'admin/adminLogin.html', 'admin/adminLogin.php', 'admin/admin_login.html', 'admin/admin_login.php', 'admin/controlpanel.html', 'admin/controlpanel.php',
'admin/cp.html', 'admin/cp.php', 'admin/home.html', 'admin/home.php', 'admin/index.html', 'admin/index.php', 'admin/login.html', 'admin/login.php', 'admin2.php', 'admin2/index.php',
'admin2/login.php', 'adminLogin.html', 'adminLogin.php', 'adminLogin/', 'admin_area/', 'admin_area/admin.html', 'admin_area/admin.php', 'admin_area/index.html', 'admin_area/index.php', 'admin_area/login.html',
'admin_area/login.php', 'admin_login.html', 'admin_login.php', 'adminarea/', 'adminarea/admin.html', 'adminarea/admin.php', 'adminarea/index.html', 'adminarea/index.php', 'adminarea/login.html', 'adminarea/login.php',
'admincontrol.html', 'admincontrol.php', 'admincontrol/login.html', 'admincontrol/login.php', 'admincp/index.asp', 'admincp/index.html', 'admincp/login.asp', 'administrator.html', 'administrator.php', 'administrator/',
'administrator/account.html', 'administrator/account.php', 'administrator/index.html', 'administrator/index.php', 'administrator/login.html', 'administrator/login.php', 'administratorlogin.php', 'administratorlogin/', 'adminpanel.html', 'adminpanel.php',
'admloginuser.php', 'affiliate.php', 'bb-admin/', 'bb-admin/admin.html', 'bb-admin/admin.php', 'bb-admin/index.html','bb-admin/index.php', 'bb-admin/login.html', 'bb-admin/login.php', 'controlpanel.html',
'controlpanel.php', 'cp.html', 'cp.php', 'home.html', 'home.php', 'instadmin/', 'joomla/administrator', 'login.html','login.php', 'memberadmin.php',
'memberadmin/', 'modelsearch/admin.html', 'modelsearch/admin.php', 'modelsearch/index.html', 'modelsearch/index.php','modelsearch/login.html', 'modelsearch/login.php', 'moderator.html', 'moderator.php', 'moderator/',
'moderator/admin.html', 'moderator/admin.php', 'moderator/login.html', 'moderator/login.php', 'nsw/admin/login.php', 'pages/admin/admin-login.html', 'pages/admin/admin-login.php', 'panel-administracion/', 'panel-administracion/admin.html', 'panel-administracion/admin.php',
'panel-administracion/index.html', 'panel-administracion/index.php', 'panel-administracion/login.html', 'panel-administracion/login.php', 'rcjakar/admin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'siteadmin/login.php', 'user.html', 'user.php',
'webadmin.html', 'webadmin.php', 'webadmin/', 'webadmin/admin.html', 'webadmin/admin.php', 'webadmin/index.html', 'webadmin/index.php', 'webadmin/login.html', 'webadmin/login.php', 'wp-login.php'
]



if __name__ == "__main__":
	
	xD = Argumentos()
	
	os.system("Cls")
	
	if Pagina == None: Pagina = "http://" + raw_input("\n\n\n\t [~] URL: ").replace("https://","").replace("http://","").split("/")[0]
	else:
		
		Pagina = "http://" + Pagina.replace("https://","").replace("http://","").split("/")[0]
		
		print("\n\n\t URL: " + Pagina)
	
	print Robots(Pagina)
	
	print "\n\n Buscando Admin Panels... \n\n"
	
	for Ruta in Rutas:
		
		time.sleep(.01)
		threading.Thread(target=Escanear, args=(Pagina, "/"+Ruta, )).start()


