# -*- coding: UTF-8 -*-
# Python 2.7 y 3.X
# Windows
#
#        █████╗ ███╗   ██╗ ██████╗ ███████╗██╗      █████╗ ███████╗
#       ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ██╔══██╗╚══███╔╝
#       ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ███████║  ███╔╝ 
#       ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ██╔══██║ ███╔╝  
#       ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║███████╗
#       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
#                                                         By: LawlietJH
#                                                               v1.2.1

import threading
import time
import sys
import os



#~ =====================================================================
#~ =====================================================================
#~ =====================================================================

PythonVer = str(sys.version.split(" ")[0].split(".")[0])
Version = "v.1.2.1"

# Banners: http://patorjk.com/software/taag/

Banner = u"""
           █████╗ ███╗   ██╗ ██████╗ ███████╗██╗      █████╗ ███████╗
          ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     ██╔══██╗╚══███╔╝
          ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     ███████║  ███╔╝ 
          ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ██╔══██║ ███╔╝  
          ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║███████╗
          ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝"""
# Fuente: ANSI Shadow - http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Angelaz

Autor = u"""\
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
	if PythonVer == "2": print("\n\n\t [+] Instalando Dependencias... Requests "),
	if PythonVer == "3": print("\n\n\t [+] Instalando Dependencias... Requests ",)
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
	
	global Pagina, Robot, Lista, FullScan, TipoRuta
	
	Args = sys.argv
	
	#~ if len(Args) == 8:
		
		#~ # Angelaz.py -P xD.com -T PHP -L Paths.txt -R
		#~ if   (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 #~ and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 #~ and (Args[5].lower() == "-l" or Args[5].lower() == "--lista")\
		 #~ and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			#~ TipoRuta = Args[4].replace('"',"")
				
			#~ if  TipoRuta.lower() == "php"\
			 #~ or TipoRuta.lower() == "asp"\
			 #~ or TipoRuta.lower() == "html"\
			 #~ or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 #~ or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 #~ or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 #~ or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 #~ or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 #~ or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				#~ Pagina = Args[2]
				#~ Lista = Args[6]
				#~ Robot = True
				#~ return True
			
			#~ else: return False
		
		#~ else: return False
		
	if len(Args) == 7:
		
		# Angelaz.py -P xD.com -L Paths.txt -T PHP
		if   (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				Lista = Args[4]
				Robot = False
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -T PHP -L Paths.txt	
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-l" or Args[5].lower() == "--lista"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				Lista = Args[6]
				Robot = False
				return True
			
			else: return False
			
		# Angelaz.py -L Paths.txt -P xD.com -T PHP
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				Lista = Args[2]
				Robot = False
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -P xD.com -L Paths.txt
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-l" or Args[5].lower() == "--lista"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				Lista = Args[6]
				Robot = False
				return True
			
			else: return False
			
		# Angelaz.py -L Paths.txt -T PHP -P xD.com
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				Lista = Args[2]
				Robot = False
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -L Paths.txt -P xD.com
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				Lista = Args[4]
				Robot = False
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -T PHP -R -C
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-c" or Args[6].lower() == "--completo"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -T PHP -C -R
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-c" or Args[5].lower() == "--completo")\
		 and (Args[6].lower() == "-r" or Args[6].lower() == "--robots"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -R -T PHP -C
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-c" or Args[6].lower() == "--completo"):
			
			TipoRuta = Args[5].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -C -T PHP -R
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-r" or Args[6].lower() == "--robots"):
			
			TipoRuta = Args[5].replace('"',"")
			
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -R -C -T PHP
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -P xD.com -C -R -T PHP
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -P xD.com -R -C
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-c" or Args[6].lower() == "--completo"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -P xD.com -C -R
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-c" or Args[5].lower() == "--completo")\
		 and (Args[6].lower() == "-r" or Args[6].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -R -P xD.com -C
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-c" or Args[6].lower() == "--completo"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[5]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -C -P xD.com -R
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-r" or Args[6].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[5]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -R -C -P xD.com
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -T PHP -C -R -P xD.com
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -R -P xD.com -T PHP -C
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-c" or Args[6].lower() == "--completo"):
			
			TipoRuta = Args[5].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[3]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -R -P xD.com -C -T PHP 
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[3]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -R -T PHP -P xD.com -C
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-c" or Args[6].lower() == "--completo"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[5]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -R -C -P xD.com -T PHP
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-c" or Args[2].lower() == "--completo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -R -T PHP -C -P xD.com
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -R -C -T PHP -P xD.com
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-c" or Args[2].lower() == "--completo")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -C -P xD.com -T PHP -R
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-r" or Args[6].lower() == "--robots"):
			
			TipoRuta = Args[5].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[3]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -C -P xD.com -R -T PHP 
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[3]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -C -T PHP -P xD.com -R
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-r" or Args[6].lower() == "--robots"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[5]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -C -R -P xD.com -T PHP
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-r" or Args[2].lower() == "--robots")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo"):
			
			TipoRuta = Args[6].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -C -T PHP -R -P xD.com
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		# Angelaz.py -C -R -T PHP -P xD.com
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-r" or Args[2].lower() == "--robots")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[6]
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		else: return False
		
	elif len(Args) == 6:
		
		if   (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-l" or Args[4].lower() == "--lista"):
			
			Lista = Args[5]
			Pagina = Args[3]
			Robot = True
			return True
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-l" or Args[2].lower() == "--lista")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina"):
			
			Lista = Args[3]
			Pagina = Args[5]
			Robot = True
			return True
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-l" or Args[4].lower() == "--lista"):
			
			Lista = Args[5]
			Pagina = Args[2]
			Robot = True
			return True
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots"):
			
			Lista = Args[4]
			Pagina = Args[2]
			Robot = True
			return True
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina"):
			
			Lista = Args[2]
			Pagina = Args[5]
			Robot = True
			return True
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots"):
			
			Lista = Args[2]
			Pagina = Args[4]
			Robot = True
			return True
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Lista = Args[4]
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-c" or Args[5].lower() == "--completo"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				FullScan = True
				Robot = False
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Lista = Args[2]
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-c" or Args[5].lower() == "--completo"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = False
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo"):
			
			TipoRuta = Args[5].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Lista = Args[2]
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo"):
			
			TipoRuta = Args[5].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo"):
			
			TipoRuta = Args[5].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				FullScan = True
				Robot = False
				return True
			
			else: return False
			
		else: return False
		
	elif len(Args) == 5:
		
		if   (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista"):
			
			Lista = Args[4]
			Pagina = Args[2]
			Robot = False
			return True
		
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina"):
			
			Lista = Args[2]
			Pagina = Args[4]
			Robot = False
			return True
		
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo"):
			
			Pagina = Args[2]
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots"):
			
			Pagina = Args[2]
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo"):
			
			Pagina = Args[3]
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots"):
			
			Pagina = Args[3]
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-c" or Args[2].lower() == "--completo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina"):
			
			Pagina = Args[4]
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-r" or Args[2].lower() == "--robots")\
		 and  Args[3].lower() == "-p":
			
			Pagina = Args[4]
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-c" or Args[4].lower() == "--completo"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-r" or Args[4].lower() == "--robots"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-c" or Args[2].lower() == "--completo")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-r" or Args[2].lower() == "--robots")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				FullScan = True
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[4]
				Robot = False
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Pagina = Args[2]
				Robot = False
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Lista = Args[4]
				Robot = False
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo"):
			
			TipoRuta = Args[4].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				
				Lista = Args[2]
				Robot = False
				return True
			
			else: return False
			
		else: return False
		
	elif len(Args) == 4:
		
		if   (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots"):
			
			Pagina = Args[2]
			FullScan = False
			Robot = True
			return True
		
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina"):
			
			Pagina = Args[3]
			FullScan = False
			Robot = True
			return True
			
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo"):
			
			Pagina = Args[2]
			FullScan = True
			Robot = False
			return True
		
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina"):
			
			Pagina = Args[3]
			FullScan = True
			Robot = False
			return True
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots"):
			
			Lista = Args[2]
			Robot = True
			return True
		
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-l" or Args[2].lower() == "--lista"):
			
			Lista = Args[3]
			Robot = True
			return True
		
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				  
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				  
				Robot = True
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-c" or Args[3].lower() == "--completo"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				  
				FullScan = True
				Robot = False
				return True
			
			else: return False
			
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo"):
			
			TipoRuta = Args[3].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				  
				FullScan = True
				Robot = False
				return True
			
			else: return False
			
		else: return False
		
	elif len(Args) == 3:
		
		if (Args[1].lower() == "-p" or Args[1].lower() == "--pagina"):
			
			Pagina = Args[2]
			Robot = False
			return True
			
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista"):
			
			Lista = Args[2]
			Robot = False
			return True
			
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo"):
			
			TipoRuta = Args[2].replace('"',"")
				
			if  TipoRuta.lower() == "php"\
			 or TipoRuta.lower() == "asp"\
			 or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"  or TipoRuta.lower() == "php html"\
			 or TipoRuta.lower() == "asp php"  or TipoRuta.lower() == "asp html"\
			 or TipoRuta.lower() == "html php" or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
			 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php"\
			 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php":
				  return True
			else: return False
			
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-c" or Args[2].lower() == "--completo"):
			
			FullScan = True
			Robot = True
			return True
			
		elif (Args[1].lower() == "-c" or Args[1].lower() == "--completo")\
		 and (Args[2].lower() == "-r" or Args[2].lower() == "--robots"):
			
			FullScan = True
			Robot = True
			return True
			
		else: return False
		
	elif len(Args) == 2:
		
		if Args[1].lower() == "-r" or Args[1].lower() == "--robots":
			
			FullScan = False
			Robot = True
			return True
			
		elif Args[1].lower() == "-c" or Args[1].lower() == "--completo":
			
			FullScan = True
			Robot = False
			return True
			
		elif Args[1].lower() == "-h" or Args[1].lower() == "--help":
			
			os.system("Cls")
			Dat()
			print("\n" + Modo_De_Uso)
			sys.exit(1)
			
		else: return False
		
	elif len(Args) == 1: return True
	
	else: return False



#========================================================================
#========================================================================
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
			
		if http == 200:
			if   PythonVer == "2": print("\n ---> [+]  Admin Panel Encontrado: " + Ruta),		# 200 - OK.						Pagina Encontrada.
			elif PythonVer == "3": print(" ---> [+]  Admin Panel Encontrado: " + Ruta)
		elif http == 301:
			if   PythonVer == "2": print("\n [!] [301] Movido Permanentemente: " + Ruta),		# 301 - Moved Permanently.		Pagina Movida Permanentemente.
			elif PythonVer == "3": print(" [!] [301] Movido Permanentemente: " + Ruta)
		elif http == 302:
			if   PythonVer == "2": print("\n ---> [+]  Vulnerabilidad [EAR]: " + Ruta),			# 302 - Found.					Pagina Redireccionada.
			elif PythonVer == "3": print(" ---> [+]  Vulnerabilidad [EAR]: " + Ruta)
		elif http == 401:
			if   PythonVer == "2": print("\n [!] [401] Acceso No Autorizado: " + Ruta),			# 401 - Unauthorized.			Pagina No Autorizada.
			elif PythonVer == "3": print(" [!] [401] Acceso No Autorizado: " + Ruta)
		elif http == 403:
			if   PythonVer == "2": print("\n [!] [403] Acceso Prohibido: " + Ruta),				# 403 - Forbidden.				Pagina Restringida.
			elif PythonVer == "3": print(" [!] [403] Acceso Prohibido: " + Ruta)
		elif http == 404:
			if   PythonVer == "2": print("\n      [-]  " + Ruta),								# 404 - Not Found.				Pagina No Encontrada.
			elif PythonVer == "3": print("      [-]  " + Ruta)
		elif http == 410:
			if   PythonVer == "2": print("\n [!] [410] Ya No Existe: " + Ruta),					# 410 - Gone.					Pagina Que Existia y No Volvera.
			elif PythonVer == "3": print(" [!] [410] Ya No Existe: " + Ruta)
		elif http == 500:
			if   PythonVer == "2": print("\n [!] [500] Internal Server Error: " + Ruta),			# 500 - Internal Server Error.
			elif PythonVer == "3": print(" [!] [500] Internal Server Error: " + Ruta)
		else:
			if   PythonVer == "2": print ("\n [!] [" + str(http) + "] " + Ruta),
			elif PythonVer == "3": print (" [!] [" + str(http) + "] " + Ruta)
	
	except KeyboardInterrupt: exit(1)
	except Exception as e:
		
		if str(type(e).__name__) == "ConnectionError":
			if   PythonVer == "2": print("\n   X  [!]  " + Ruta + u" <--- Error De Conección."),
			elif PythonVer == "3": print("   X  [!]  " + Ruta + u" <--- Error De Conección.")
		else:
			if   PythonVer == "2": print("\n   X  [!]  " + Ruta + " <--- " + str(type(e).__name__)),
			elif PythonVer == "3": print("   X  [!]  " + Ruta + " <--- " + str(type(e).__name__))



def Filtrar(Ruta):
	
	if  TipoRuta.lower() == "php asp html" or TipoRuta.lower() == "php html asp"\
	 or TipoRuta.lower() == "html php asp" or TipoRuta.lower() == "html asp php"\
	 or TipoRuta.lower() == "asp php html" or TipoRuta.lower() == "asp html php":
			
		time.sleep(.01)
		if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
		else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	elif TipoRuta.lower() == "php asp" or TipoRuta.lower() == "asp php":
		if not Ruta.lower().endswith(".html"):
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	elif TipoRuta.lower() == "asp html" or TipoRuta.lower() == "html asp":
		if not Ruta.lower().endswith(".php"):
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	elif TipoRuta.lower() == "html php" or TipoRuta.lower() == "php html":
		if not Ruta.lower().endswith(".asp"):
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	elif TipoRuta.lower() == "php":
		if not Ruta.lower().endswith(".asp") and not Ruta.lower().endswith(".html"):
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	elif TipoRuta.lower() == "asp":
		if not Ruta.lower().endswith(".php") and not Ruta.lower().endswith(".html"):
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	elif TipoRuta.lower() == "html":
		if not Ruta.lower().endswith(".php") and not Ruta.lower().endswith(".asp"):
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()
			
		return True
		
	else: return False



#========================================================================
#========================================================================
#========================================================================



Pagina = None
Robot = None
Lista = None
FullScan = None
TipoRuta = None
EscaneoTipo = ""
Rutas = []

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

Modo_De_Uso = u"""\
 [+] Modo De Uso: ============================================================
  
  Angelaz.py [-P Pagina.com][-R][-T TIPO] {[-L Rutas.txt] | [-C]} | [-h]
  
  -h, --help                Muestra Este Mensaje y Sale del Script.
  
  -P, --Pagina PAGINA.COM   Página A Escanear.
  
  -L, --Lista LISTA.TXT     Archivo Con La Lista de Rutas.txt.
  
  -R, --Robots              Indica Si Se Desea Buscar El Archivo Robots.txt.
  
  -C, --Completo            Indica Hacer Un Escaneo Completo Con 483 Rutas.
  
  -T, --Tipo PHP,ASP,HTML   Filtra Por Tipo Las Rutas Que Se Usarán.
  
 [+] Ejemplos: ===============================================================
  
  > Angelaz.py                    [*] Corre El Script y Pide La Información
                                      Necesaria De Forma Interna.
  > Angelaz.py -h                 [*] Muestra El Modo De Uso.
  > Angelaz.py -P Pagina.com      [*] Realiza Escaneo a La Página Usando Las
                                      Rutas Una Lista Interna Con 140 Rutas.
  > Angelaz.py -P xD.com -L Rutas.txt -R    [*] Realiza Escaneo a La Página
                                                Usando Las Rutas Del Archivo
                                                Rutas.txt y Busca El Archivo
                                                Robots.txt.
  > Angelaz.py -P xD.com -R -C    [*] Agregar -C Hace Un Escaneo Completo Con
                                      483 Rutas. No Puedes Combinar -C y -L.
  > Angelaz.py -T PHP             [*] Filtrará Las Rutas Para Mostrar Solo PHP
                                      y Agregando Las Que No Tienen Extensión.
  > Angelaz.py -T "ASP HTML"      [*] Filtrará Las Rutas De Archivos Mostrando
                                      Con Extensión ASP y HTML solamente y
                                      Agregando Las Que No Tienen Extensión.
                                      
 =============================================================================
"""



#========================================================================
#========================================================================
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
				
				print("\n\n\t [~] " + str(len(Rutas)) + " Rutas Cargadas.")
				EscaneoTipo = "Escaeo Personalizado Con " + str(len(Rutas)) + " Rutas."
				FullScan  = ""
				
				time.sleep(1)
		
		else:
			os.system("Cls")
			Dat()
			print("\n\t [!] El Archivo " + Lis + " No Existe.\n\n")
			print("\n" + Modo_De_Uso)
			sys.exit(0)
	
	Chk = Pagina
	while True:
		
		if Chk == None:
			if PythonVer == "2": Pagina = "http://" + raw_input("\n\n\n\t [~] URL: ").replace("https://","").replace("http://","").split("/")[0]
			if PythonVer == "3": Pagina = "http://" + input("\n\n\n\t [~] URL: ").replace("https://","").replace("http://","").split("/")[0]
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
	
	if Robot == None:
		
		if PythonVer == "2": 
			if raw_input("\n\n\n\t [~] Buscar Robots.txt [S/N]: ").lower() in ["s","si","y","yes"]:
				
				print("\n\n\n [+] Buscando Robots.txt ...")
				print(Robots(Pagina))
		
		if PythonVer == "3": 
			if input("\n\n\n\t [~] Buscar Robots.txt [S/N]: ").lower() in ["s","si","y","yes"]:
				
				print("\n\n\n [+] Buscando Robots.txt ...")
				print(Robots(Pagina))
			
	elif Robot == True:
		
		print("\n\n\n [+] Buscando Robots.txt ...")
		print(Robots(Pagina))
	
	if   FullScan == True: EscaneoTipo = "Escaneo Completo Con " + str(len(RutasFull)) + " Rutas."; Rutas = RutasFull
	elif FullScan == False or FullScan == None: EscaneoTipo = u"Escaneo Rápido Con " + str(len(RutasFast)) + " Rutas."; Rutas = RutasFast
	
	if TipoRuta == None: print("\n\n\n [+] " + EscaneoTipo + "\n\n [+] Filtrado Por: Sin Filtros.\n\n\n [+] Buscando Admin Panels...")
	else: print("\n\n\n [+] " + EscaneoTipo + "\n\n [+] Filtrado Por: " + TipoRuta + ".\n\n\n [+] Buscando Admin Panels...")
	
	for Ruta in Rutas:
		
		if TipoRuta != None:
			
			if not Filtrar(Ruta):
				
				os.system("Cls")
				print(True)
				Dat()
				print("\n" + Modo_De_Uso)
				sys.exit(1)
		
		elif TipoRuta == None:
			
			time.sleep(.01)
			if Ruta.startswith("/"): threading.Thread(target=Escanear, args=(Pagina, Ruta, )).start()
			else: threading.Thread(target=Escanear, args=(Pagina, "/" + Ruta, )).start()


