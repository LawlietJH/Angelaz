# -*- coding: UTF-8 -*-
# Python 2.7
#        █████╗ ███╗   ██╗ ██████╗ ███████╗██╗      █████╗ ███████╗
#       ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ██╔══██╗╚══███╔╝
#       ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ███████║  ███╔╝ 
#       ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ██╔══██║ ███╔╝  
#       ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║███████╗
#       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.0.9
# Python 2.7

import threading
import time
import sys
import os



#~ =====================================================================
#~ =====================================================================
#~ =====================================================================



Version = "v.1.0.9"

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
				Cadena += "\n\n\n [~] Contenido de Robots.txt:\n\n"
				Cadena += "================================================\n\n\n"
				Cadena +=  Req.text + "\n\n"
				Cadena += "================================================\n\n"
				
				return Cadena
		
		elif http == 404 and not "www." in Pagina: return Robots(Pagina.replace("http://","http://www."))
		
		else: return "\n\n\t [-] Robots.txt No encontrado."
		
	except: return "\n\n\t [-] Robots.txt No encontrado."



def Escanear(Pagina, Ruta):
	
	try:
		
		Ruta = Pagina + Ruta
		Req = requests.get(Ruta)
		http = Req.status_code
			
		if http == 200:   print("\n ---> [+]  Admin Panel Encontrado: " + Ruta),	# 200 - OK.						Pagina Encontrada.
		elif http == 301: print("\n [!] [301] Movido Permanentemente: " + Ruta),	# 301 - Moved Permanently.		Pagina Movida Permanentemente.
		elif http == 302: print("\n ---> [+]  Vulnerabilidad [EAR]: " + Ruta),		# 302 - Found.					Pagina Redireccionada.
		elif http == 401: print("\n [!] [401] Acceso No Autorizado: " + Ruta),		# 401 - Unauthorized.			Pagina No Autorizada.
		elif http == 403: print("\n [!] [403] Acceso Prohibido: " + Ruta),			# 403 - Forbidden.				Pagina Restringida.
		elif http == 404: print("\n      [-]  " + Ruta),							# 404 - Not Found.				Pagina No Encontrada.
		elif http == 410: print("\n [!] [410] Ya No Existe: " + Ruta),				# 410 - Gone.					Pagina Que Existia y No Volvera.
		elif http == 500: print("\n [!] [500] Internal Server Error: " + Ruta),		# 500 - Internal Server Error.
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

# 140 Rutas.
RutasFast = [
 'account.html', 'account.php', 'adm.html', 'adm.php', 'adm/', 'adm/admloginuser.php', 'adm/index.html', 'adm/index.php', 'adm_auth.php', 'admin', 'admin-login.html', 'admin-login.php', 'admin.html', 'admin.php', 'admin/', 'admin/account.html', 'admin/account.html', 'admin/account.php', 'admin/account.php', 'admin/admin-login.html',
 'admin/admin-login.php', 'admin/admin.html', 'admin/admin.php', 'admin/adminLogin.html', 'admin/adminLogin.html', 'admin/adminLogin.php', 'admin/admin_login.html', 'admin/admin_login.php', 'admin/controlpanel.html', 'admin/controlpanel.php', 'admin/cp.html', 'admin/cp.php', 'admin/home.html', 'admin/home.php', 'admin/index.html', 'admin/index.php', 'admin/login.html', 'admin/login.php', 'admin2.php', 'admin2/index.php',
 'admin2/login.php', 'adminLogin.html', 'adminLogin.php', 'adminLogin/', 'admin_area/', 'admin_area/admin.html', 'admin_area/admin.php', 'admin_area/index.html', 'admin_area/index.php', 'admin_area/login.html', 'admin_area/login.php', 'admin_login.html', 'admin_login.php', 'adminarea/', 'adminarea/admin.html', 'adminarea/admin.php', 'adminarea/index.html', 'adminarea/index.php', 'adminarea/login.html', 'adminarea/login.php',
 'admincontrol.html', 'admincontrol.php', 'admincontrol/login.html', 'admincontrol/login.php', 'admincp/index.asp', 'admincp/index.html', 'admincp/login.asp', 'administrator.html', 'administrator.php', 'administrator/', 'administrator/account.html', 'administrator/account.php', 'administrator/index.html', 'administrator/index.php', 'administrator/login.html', 'administrator/login.php', 'administratorlogin.php', 'administratorlogin/', 'adminpanel.html', 'adminpanel.php',
 'admloginuser.php', 'affiliate.php', 'bb-admin/', 'bb-admin/admin.html', 'bb-admin/admin.php', 'bb-admin/index.html','bb-admin/index.php', 'bb-admin/login.html', 'bb-admin/login.php', 'controlpanel.html', 'controlpanel.php', 'cp.html', 'cp.php', 'home.html', 'home.php', 'instadmin/', 'joomla/administrator', 'login.html','login.php', 'memberadmin.php',
 'memberadmin/', 'modelsearch/admin.html', 'modelsearch/admin.php', 'modelsearch/index.html', 'modelsearch/index.php','modelsearch/login.html', 'modelsearch/login.php', 'moderator.html', 'moderator.php', 'moderator/', 'moderator/admin.html', 'moderator/admin.php', 'moderator/login.html', 'moderator/login.php', 'nsw/admin/login.php', 'pages/admin/admin-login.html', 'pages/admin/admin-login.php', 'panel-administracion/', 'panel-administracion/admin.html', 'panel-administracion/admin.php',
 'panel-administracion/index.html', 'panel-administracion/index.php', 'panel-administracion/login.html', 'panel-administracion/login.php', 'rcjakar/admin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'siteadmin/login.php', 'user.html', 'user.php', 'webadmin.html', 'webadmin.php', 'webadmin/', 'webadmin/admin.html', 'webadmin/admin.php', 'webadmin/index.html', 'webadmin/index.php', 'webadmin/login.html', 'webadmin/login.php', 'wp-login.php'
]

# 483 Rutas.
RutasFull = [
 '/ADMIN/', '/ADMIN/login.html', '/ADMIN/login.php', '/ADMON/', '/Admin/', '/Admin/private/', '/AdminTools/', '/AdminWeb/', '/Database_Administration/', '/Indy_admin/', '/LiveUser_Admin/', '/Lotus_Domino_Admin/', '/Server.asp', '/Server.html', '/Server.php', '/Server/', '/ServerAdministrator/', '/Super-Admin/', '/SysAdmin/', '/SysAdmin2/',
 '/UserLogin/', '/WebAdmin/', '/_adm/', '/_adm_/', '/_admin/', '/_admin_/', '/_administrator/', '/_administrator_/', '/acceso.asp', '/acceso.php', '/access.php', '/access/', '/account.asp', '/account.html', '/account.php', '/account/', '/acct_login/', '/adm.asp', '/adm.html', '/adm.php',
 '/adm/', '/adm/admloginuser.asp', '/adm/admloginuser.php', '/adm/index.asp', '/adm/index.html', '/adm/index.php', '/adm2/', '/adm_auth.asp', '/adm_auth.php', '/admin', '/admin-login.asp', '/admin-login.html', '/admin-login.php', '/admin-login.php/', '/admin.asp', '/admin.html', '/admin.php', '/admin/', '/admin/AdminDashboard.php', '/admin/AdminHome.php',
 '/admin/CPhome.php', '/admin/ManageAdmin.php', '/admin/account.asp', '/admin/account.html', '/admin/account.php', '/admin/add-room.php', '/admin/add-slider.php', '/admin/add.php', '/admin/add_banner.php/', '/admin/add_gallery_image.php', '/admin/add_testimonials.php', '/admin/addblog.php', '/admin/adm.php', '/admin/admin-home.php', '/admin/admin-login.asp', '/admin/admin-login.html', '/admin/admin-login.php', '/admin/admin.asp', '/admin/admin.html', '/admin/admin.php',
 '/admin/admin/', '/admin/adminLogin.asp', '/admin/adminLogin.html', '/admin/adminLogin.php', '/admin/admin_index.php', '/admin/admin_login.asp', '/admin/admin_login.html', '/admin/admin_login.php', '/admin/admin_management.php', '/admin/admin_users.php', '/admin/adminarea.php', '/admin/adminview.php', '/admin/banner.php', '/admin/banners_report.php', '/admin/category.php', '/admin/change_gallery.php', '/admin/checklogin.php', '/admin/configration.php', '/admin/control_pages/admin_home.php', '/admin/controlpanel.asp',
 '/admin/controlpanel.html', '/admin/controlpanel.php', '/admin/cp.asp', '/admin/cp.html', '/admin/cp.php', '/admin/cpanel.php', '/admin/dash.php', '/admin/dashboard.php', '/admin/dashboard/index.php', '/admin/dashbord.php', '/admin/default.php', '/admin/enter.php', '/admin/event.php', '/admin/form.php', '/admin/gallery.php', '/admin/headline.php', '/admin/home.asp', '/admin/home.html', '/admin/home.php', '/admin/index-digital.php',
 '/admin/index.asp', '/admin/index.html', '/admin/index.php', '/admin/index_ref.php', '/admin/initialadmin.php', '/admin/leads.php','/admin/list_gallery.php', '/admin/log.php', '/admin/login', '/admin/login-home.php', '/admin/login.asp', '/admin/login.html', '/admin/login.php', '/admin/login_success.php', '/admin/loginsuccess.php', '/admin/main.php/', '/admin/main_page.php', '/admin/manageImages.php', '/admin/manage_team.php', '/admin/member_home.php',
 '/admin/moderator.php', '/admin/my_account.php', '/admin/myaccount.php', '/admin/overview.php', '/admin/page_management.php', '/admin/pages/home_admin.php', '/admin/product.php', '/admin/products.php', '/admin/save.php', '/admin/slider.php', '/admin/specializations.php', '/admin/uhome.html', '/admin/upload.php', '/admin/userpage.php', '/admin/viewblog.php', '/admin/viewmembers.php', '/admin/voucher.php', '/admin/welcome.php', '/admin/welcomepage.php', '/admin1.asp',
 '/admin1.html', '/admin1.php', '/admin1/', '/admin2.asp', '/admin2.html', '/admin2.php', '/admin2/', '/admin2/index.asp', '/admin2/index.php', '/admin2/index/', '/admin2/login.asp', '/admin2/login.php', '/admin3/', '/admin4/', '/admin4_account/', '/admin4_colon/', '/admin5/', '/adminLogin.asp', '/adminLogin.html', '/adminLogin.php',
 '/adminLogin/', '/admin_area/', '/admin_area/admin.asp', '/admin_area/admin.html', '/admin_area/admin.php', '/admin_area/index.asp', '/admin_area/index.html', '/admin_area/index.php', '/admin_area/login.asp', '/admin_area/login.html', '/admin_area/login.php', '/admin_home.php', '/admin_login.asp', '/admin_login.html', '/admin_login.php', '/admin_login.php]', '/admin_main.html', '/admin_tool/', '/adminarea/', '/adminarea/admin.asp',
 '/adminarea/admin.html', '/adminarea/admin.php', '/adminarea/index.asp', '/adminarea/index.html', '/adminarea/index.php', '/adminarea/login.asp', '/adminarea/login.html', '/adminarea/login.php', '/admincontrol.asp', '/admincontrol.html', '/admincontrol.php', '/admincontrol.php/', '/admincontrol/login.asp', '/admincontrol/login.html', '/admincontrol/login.php', '/admincp/index.asp', '/admincp/index.html', '/admincp/login.asp', '/administer/', '/administr8.asp',
 '/administr8.html', '/administr8.php', '/administr8/', '/administracion.php', '/administrador/', '/administratie/', '/administration.html', '/administration.php', '/administration/', '/administrator', '/administrator.asp', '/administrator.html', '/administrator.php', '/administrator/', '/administrator/account.asp', '/administrator/account.html', '/administrator/account.php', '/administrator/index.asp', '/administrator/index.html', '/administrator/index.php',
 '/administrator/login.asp', '/administrator/login.html', '/administrator/login.php', '/administratoraccounts/', '/administratorlogin.asp', '/administratorlogin.php', '/administratorlogin/', '/administrators/', '/administrivia/', '/adminpanel.asp', '/adminpanel.html', '/adminpanel.php', '/adminpanel/', '/adminpro/', '/admins.asp', '/admins.html', '/admins.php', '/admins/', '/admloginuser.asp', '/admloginuser.php',
 '/admon/', '/affiliate.asp', '/affiliate.php', '/auth/', '/auth/login/', '/authorize.php', '/autologin/', '/banneradmin/', '/base/admin/', '/bb-admin/', '/bb-admin/admin.asp', '/bb-admin/admin.html', '/bb-admin/admin.php', '/bb-admin/index.asp', '/bb-admin/index.html', '/bb-admin/index.php', '/bb-admin/login.asp', '/bb-admin/login.html', '/bb-admin/login.php', '/bbadmin/',
 '/bigadmin/', '/blogindex/', '/cPanel/', '/cadmins/', '/ccms/', '/ccms/index.php', '/ccms/login.php', '/ccp14admin/', '/cms/', '/cms/_admin/logon.php', '/cms/admin/', '/cms/login/', '/cmsadmin/', '/configuration/', '/configure/', '/controlpanel.asp', '/controlpanel.html', '/controlpanel.php', '/controlpanel/', '/cp.asp',
 '/cp.html', '/cp.php', '/cpanel/', '/cpanel_file/', '/customer_login/', '/database_administration/', '/db/admin.php', '/dir-login/', '/directadmin/', '/edit.php', '/editor/', '/evmsadmin/', '/ezsqliteadmin/', '/fileadmin.asp', '/fileadmin.html', '/fileadmin.php', '/fileadmin/', '/formslogin/', '/forum/admin', '/globes_admin/',
 '/home.asp', '/home.html', '/home.php', '/hpwebjetadmin/', '/include/admin.php', '/includes/login.php', '/instadmin/', '/interactive/admin.php', '/irc-macadmin/', '/joomla/administrator', '/links/login.php', '/login-redirect/', '/login-us/', '/login.asp', '/login.html', '/login.php', '/login/', '/login/login.php', '/login1/', '/login_db/',
 '/loginflat/', '/logins/', '/logo_sysadmin/', '/logon/', '/macadmin/', '/mag/admin/', '/maintenance/', '/manage_admin.php', '/manager/', '/manager/ispmgr/', '/manuallogin/', '/memberadmin.asp', '/memberadmin.php', '/memberadmin/', '/members/', '/memlogin/', '/meta_login/', '/modelsearch/admin.asp', '/modelsearch/admin.html', '/modelsearch/admin.php',
 '/modelsearch/index.asp', '/modelsearch/index.html', '/modelsearch/index.php', '/modelsearch/login.asp', '/modelsearch/login.html', '/modelsearch/login.php', '/moderator.asp', '/moderator.html', '/moderator.php', '/moderator.php/', '/moderator/', '/moderator/admin.asp', '/moderator/admin.html', '/moderator/admin.php', '/moderator/login.asp', '/moderator/login.html', '/moderator/login.php', '/myadmin/', '/navSiteAdmin/', '/newsadmin/',
 '/nsw/admin/login.php', '/openvpnadmin/', '/pages/admin/admin-login.asp', '/pages/admin/admin-login.html', '/pages/admin/admin-login.php', '/panel-administracion/', '/panel-administracion/admin.asp', '/panel-administracion/admin.html', '/panel-administracion/admin.php', '/panel-administracion/index.asp', '/panel-administracion/index.html', '/panel-administracion/index.php', '/panel-administracion/login.asp', '/panel-administracion/login.html', '/panel-administracion/login.php', '/panel.php', '/panel/', '/panelc/', '/paneldecontrol/', '/pgadmin/',
 '/phpSQLiteAdmin/', '/phpldapadmin/', '/phpmyadmin/', '/phppgadmin/', '/platz_login/', '/pma/', '/power_user/', '/project-admins/', '/pureadmin/', '/radmind-1/', '/radmind/', '/rcLogin/', '/rcjakar/admin/login.php', '/server/', '/server_admin_small/', '/showlogin/', '/simpleLogin/', '/site/admin/', '/site_admin/login.php', '/siteadmin/',
 '/siteadmin/index.asp', '/siteadmin/index.php', '/siteadmin/login.asp', '/siteadmin/login.html', '/siteadmin/login.php', '/smblogin/', '/sql-admin/', '/ss_vms_admin_sm/', '/sshadmin/', '/staradmin/', '/sub-login/', '/support_login/', '/sys-admin/', '/sysadmin.asp', '/sysadmin.html', '/sysadmin.php', '/sysadmin/', '/sysadmins/', '/system-administration/', '/system_administration/',
 '/typo3/', '/ur-admin.asp', '/ur-admin.html', '/ur-admin.php', '/ur-admin/', '/user.asp', '/user.html', '/user.php', '/useradmin/', '/usuario/', '/usuarios/', '/usuarios//', '/usuarios/login.php', '/utility_login/', '/vadmind/', '/vmailadmin/', '/webadmin.asp', '/webadmin.html', '/webadmin.php', '/webadmin/',
 '/webadmin/admin.asp', '/webadmin/admin.html', '/webadmin/admin.php', '/webadmin/index.asp', '/webadmin/index.html', '/webadmin/index.php', '/webadmin/login.asp', '/webadmin/login.html', '/webadmin/login.php', '/webmaster/', '/websvn/', '/wizmysqladmin/', '/wp-admin/', '/wp-login.php', '/wp-login/', '/wplogin/', '/xlogin/', '/yonetici.asp', '/yonetici.html', '/yonetici.php',
 '/yonetim.asp', '/yonetim.html', '/yonetim.php'
]

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
	
	Chk = Pagina
	while True:
		
		if Chk == None: Pagina = "http://" + raw_input("\n\n\n\t [~] URL: ").replace("https://","").replace("http://","").split("/")[0]
		else:
			Pagina = "http://" + Pagina.replace("https://","").replace("http://","").split("/")[0]
			print("\n\n\n [+] URL: " + Pagina)
			
		try: requests.get(Pagina)
		except requests.exceptions.ConnectionError:
			print(u"\n\n [!] Error De Conexión Con La Página:\n\n\n\t" + Pagina)
			print(u"\n\n [!] La Página No Existe    o    No Tienes Conexión A Internet.")
			time.sleep(4)
			os.system("Cls")
			continue
			
		break
	
	if Robot == None or Robot == False:
		
		if raw_input("\n\n\n\t [~] Buscar Robots.txt [S/N]: ").lower() in ["s","si","y","yes"]:
			
			print("\n\n\n [+] Buscando Robots.txt ...")
			print(Robots(Pagina))
		
	elif Robot == True:
		
		print("\n\n\n [+] Buscando Robots.txt ...")
		print(Robots(Pagina))
	
	if Fast: EscaneoTipo = u"Escaneo Rápido " + str(len(RutasFast)) + " Rutas."; Rutas = RutasFast
	else:    EscaneoTipo = "Escaneo Completo" + str(len(RutasFull)) + " Rutas."; Rutas = RutasFull
	
	print("\n\n\n [+] Buscando Admin Panels... " + EscaneoTipo + "\n\n")
	
	for Ruta in Rutas:
		
		time.sleep(.01)
		threading.Thread(target=Escanear, args=(Pagina, "/"+Ruta, )).start()


