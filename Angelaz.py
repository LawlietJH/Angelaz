# -*- coding: UTF-8 -*-
# Python 2.7
#        █████╗ ███╗   ██╗ ██████╗ ███████╗██╗      █████╗ ███████╗
#       ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ██╔══██╗╚══███╔╝
#       ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ███████║  ███╔╝ 
#       ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ██╔══██║ ███╔╝  
#       ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║███████╗
#       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.0.7
# Python 2.7

import threading
import time
import sys
import os



#~ =====================================================================
#~ =====================================================================
#~ =====================================================================



Version = "v.1.0.7"

# Banners: http://patorjk.com/software/taag/

Banner = u"""
           █████╗ ███╗   ██╗ ██████╗ ███████╗██╗      █████╗ ███████╗
          ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ██╔══██╗╚══███╔╝
          ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ███████║  ███╔╝ 
          ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ██╔══██║ ███╔╝  
          ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║███████╗
          ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
"""
# Fuente: ANSI Shadow - http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Angelaz

Autor = u"""
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
# Fuente: Calvin S - http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH



def Dat():
	
	#~ os.system("Cls && Title Angelaz.py                "+\
			#~ "By: LawlietJH                "+Version+"    ")
	print("\n\n" + Banner)
	print("\n\n" + Autor)
	print("\n{:^80}".format(Version))
	
	#~ try:
		#~ time.sleep(2)
	#~ except:
		#~ Dat()



try:
	import requests
except:
	Dat()
	print("\n\n\t [+] Instalando Dependencias... Requests "),
	os.system("python -m pip install requests > Nul")
	try:
		import requests
		print("OK")
		time.sleep(3)
		os.system("Cls")
	except:
		print("\n\n\t [+] No Se Pudo Instalar 'requests'... Instalalo manualmente.\n\n\t python -m pip install requests")
		sys.exit(1)



#~ =====================================================================
#~ =====================================================================
#~ =====================================================================



def Argumentos():
	
	global Pagina, Robot, Lista, Fast
	
	Args = sys.argv
	
	if len(Args) == 6:
		
		if Args[1] == "-R" and Args[2] == "-P" and Args[4] == "-L":
			
			Lista = Args[5]
			Pagina = Args[3]
			Robot = True
			return True
			
		elif Args[1] == "-R" and Args[2] == "-L" and Args[4] == "-P":
			
			Lista = Args[3]
			Pagina = Args[5]
			Robot = True
			return True
			
		elif Args[1] == "-P" and Args[3] == "-R" and Args[4] == "-L":
			
			Lista = Args[5]
			Pagina = Args[2]
			Robot = True
			return True
			
		elif Args[1] == "-P" and Args[3] == "-L" and Args[5] == "-R":
			
			Lista = Args[4]
			Pagina = Args[2]
			Robot = True
			return True
			
		elif Args[1] == "-L" and Args[3] == "-R" and Args[4] == "-P":
			
			Lista = Args[2]
			Pagina = Args[5]
			Robot = True
			return True
			
		elif Args[1] == "-L" and Args[3] == "-P" and Args[5] == "-R":
			
			Lista = Args[2]
			Pagina = Args[4]
			Robot = True
			return True
			
		else: return False
		
	if len(Args) == 5:
		
		if Args[1] == "-P" and Args[3] == "-L":
			
			Lista = Args[4]
			Pagina = Args[2]
			Robot = False
			return True
		
		elif Args[1] == "-L" and Args[3] == "-P":
			
			Lista = Args[2]
			Pagina = Args[4]
			Robot = False
			return True
			
		else: return False
		
	if len(Args) == 4:
		
		if Args[1] == "-P" and Args[3] == "-R":
			
			Pagina = Args[2]
			Robot = True
			return True
		
		elif Args[1] == "-R" and Args[2] == "-P":
			
			Pagina = Args[3]
			Robot = True
			return True
			
		else: return False
		
	if len(Args) == 3:
		
		if Args[1] == "-P":
			
			Pagina = Args[2]
			Robot = False
			return True
			
		elif Args[1] == "-L":
			
			Lista = Args[2]
			Robot = False
			return True
			
		else: return False
		
	elif len(Args) == 2:
		
		if Args[1] == "-R":
			
			Robot = True
			return True
			
		
		if Args[1] == "-h" or Args[1] == "--help":
			
			os.system("Cls")
			Dat()
			print("\n" + Modo_De_Uso)
			sys.exit(1)
			
		else: return False
		
	elif len(Args) == 1: return True
	
	else: return False



#========================================================================



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
			
		if http == 200:   print("\n ---> [+]  Admin Panel Encontrado: " + Ruta),					# 200 - OK.						Pagina Encontrada.
		elif http == 301: print("\n [!] [301] Movido Permanentemente: " + Ruta),					# 301 - Moved Permanently.		Pagina Movida Permanentemente.
		elif http == 302: print("\n ---> [+]  Vulnerabilidad Potencial [EAR] Encontrada: " + Ruta),	# 302 - Found.					Pagina Redireccionada.
		elif http == 401: print("\n [!] [401] Acceso No Autorizado: " + Ruta),						# 401 - Unauthorized.			Pagina No Autorizada.
		elif http == 403: print("\n [!] [403] Acceso Prohibido: " + Ruta),							# 403 - Forbidden.				Pagina Restringida.
		elif http == 404: print("\n      [-]  " + Ruta),											# 404 - Not Found.				Pagina No Encontrada.
		elif http == 410: print("\n [!] [410] Ya No Existe: " + Ruta),								# 410 - Gone.					Pagina Que Existia y No Volvera.
		elif http == 500: print("\n [!] [500] Internal Server Error: " + Ruta),						# 500 - Internal Server Error.
		else: print ("\n [!] [" + str(http) + "] " + Ruta),
	
	except KeyboardInterrupt: exit(1)
	except Exception as e:
		
		if str(type(e).__name__) == "ConnectionError": print("\n   X  [!]  " + Ruta + u" <--- Error De Conección."),
		else: print("\n   X  [!]  " + Ruta + " <--- " + str(type(e).__name__)),



#========================================================================



Pagina = None
Robot = None
Lista = None
Fast = True

RutasFast = [
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

Rutas = []

Modo_De_Uso = """ [+] Modo De Uso:\n\n\n Angelaz.py [-P Pagina.com][-L Rutas.txt][-R] | [-h|--help]


  -h, --help            Muestra este Mensaje y Sale del Script.
  
  -P PAGINA.COM         Pagina a Escanear.
  
  -L LISTA.TXT          Archivo con la Lista de Rutas.txt.

  -R                    Indica Si Se Desea Buscart El Archivo Robots.txt.


  [+] Ejemplos:
    
  > Angelaz.py                      Corre El Script y Pide La Informacion
                                    Necesaria De Forma Interna.
  
  > Angelaz.py -h                   Muestra El Mensaje de Ayuda.
  
  > Angelaz.py -P Pagina.com        Realiza Escaneo a La Pagina Usando 
                                    Las Rutas En Lista Interna.
                                                
  > Angelaz.py -P xD.com -L Rutas.txt -R  Realiza Escaneo a La Pagina Usando 
                                          Las Rutas Del Archivo de Rutas.txt
                                          y Busca El Archivo Robots.txt.

"""

#========================================================================



if __name__ == "__main__":
	
	xD = Argumentos()
	
	if xD == False:
		
		os.system("Cls")
		Dat()
		print("\n" + Modo_De_Uso)
		sys.exit(1)
	
	os.system("Cls")
	
	if Lista != None:
		
		if os.path.exists(Lista):
			
			with open(Lista, "r") as Lis:
				
				Rutas = []
				
				print("\n\n\n [~] Cargando Rutas...")
				
				for x in Lis:
					
					if x.startswith("/"): x = x[1:]
					
					Rutas.append(x.replace("\n",""))
				
				print("\n\n\t [~] " + str(len(Rutas)) + " Rutas Cargadas")
				
				time.sleep(1)
		
		else:
			os.system("Cls")
			Dat()
			print("\n\t [!] El Archivo " + Lista + " No Existe.\n\n")
			print("\n" + Modo_De_Uso)
			sys.exit(0)
		
	if Pagina == None: Pagina = "http://" + raw_input("\n\n\n\t [~] URL: ").replace("https://","").replace("http://","").split("/")[0]
	else:
		
		Pagina = "http://" + Pagina.replace("https://","").replace("http://","").split("/")[0]
		print("\n\n\n [+] URL: " + Pagina)
	
	if Robot == None or Robot == False:
		
		if raw_input("\n\n\n\t [~] Buscar Robots.txt [S/N]: ").lower() in ["s","si","y","yes"]:
			
			print("\n\n [+] Buscando Robots.txt ...")
			print(Robots(Pagina))
		
	elif Robot == True:
		
		print("\n\n [+] Buscando Robots.txt ...")
		print(Robots(Pagina))
	
	print("\n\n [+] Buscando Admin Panels... \n\n")
	
	if Fast: Rutas = RutasFast
	
	for Ruta in Rutas:
		
		time.sleep(.01)
		threading.Thread(target=Escanear, args=(Pagina, "/"+Ruta, )).start()


