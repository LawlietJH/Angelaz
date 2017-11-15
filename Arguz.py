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
#                                                               v1.2.4


def Arg8(Args):
	
	# 01 -P -T -L -R	# 02 -P -T -R -L
	# 03 -P -R -T -L	# 04 -P -R -L -T
	# 05 -P -L -R -T	# 06 -P -L -T -R
	
	# 07 -T -P -L -R	# 08 -T -P -R -L
	# 09 -T -R -P -L	# 10 -T -R -L -P
	# 11 -T -L -R -P	# 12 -T -L -P -R
	
	# 13 -L -P -T -R	# 14 -L -P -R -T
	# 15 -L -R -P -T	# 16 -L -R -T -P
	# 17 -L -T -R -P	# 18 -L -T -P -R
	
	# 19 -R -P -T -L	# 20 -R -P -L -T
	# 21 -R -L -P -T	# 22 -R -L -T -P
	# 23 -R -T -L -P	# 24 -R -T -P -L
	
	TipoRuta = ""
	Val= {}
	
	if len(Args) == 8:
		
		#01 Angelaz.py -P xD.com -T PHP -L Paths.txt -R
		if   (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-l" or Args[5].lower() == "--lista")\
		 and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			TipoRuta = Args[4].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[2]
				Val["Lista"]	= Args[6]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#02 Angelaz.py -P xD.com -T PHP -R -L Paths.txt
		if   (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-l" or Args[6].lower() == "--lista"):
			
			TipoRuta = Args[4].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[2]
				Val["Lista"]	= Args[7]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#03 Angelaz.py -P xD.com -R -T PHP -L Paths.txt
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-l" or Args[6].lower() == "--lista"):
			
			TipoRuta = Args[5].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[2]
				Val["Lista"]	= Args[7]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#04 Angelaz.py -P xD.com -R -L Paths.txt -T PHP
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-l" or Args[4].lower() == "--lista")\
		 and (Args[6].lower() == "-t" or Args[6].lower() == "--tipo"):
			
			TipoRuta = Args[7].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[2]
				Val["Lista"]	= Args[5]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#05 Angelaz.py -P xD.com -L Paths.txt -R -T PHP
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-t" or Args[6].lower() == "--tipo"):
			
			TipoRuta = Args[7].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[2]
				Val["Lista"]	= Args[4]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#06 Angelaz.py -P xD.com -L Paths.txt -T PHP -R
		elif (Args[1].lower() == "-p" or Args[1].lower() == "--pagina")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo")\
		 and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			TipoRuta = Args[6].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[2]
				Val["Lista"]	= Args[4]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#07 Angelaz.py -T PHP -P xD.com -L Paths.txt -R
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-l" or Args[5].lower() == "--lista")\
		 and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[4]
				Val["Lista"]	= Args[6]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#08 Angelaz.py -T PHP -P xD.com -R -L Paths.txt
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-l" or Args[6].lower() == "--lista"):
			
			TipoRuta = Args[2].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[4]
				Val["Lista"]	= Args[7]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#09 Angelaz.py -T PHP -R -P xD.com -L Paths.txt
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-l" or Args[6].lower() == "--lista"):
			
			TipoRuta = Args[2].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[5]
				Val["Lista"]	= Args[7]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#10 Angelaz.py -T PHP -R -P xD.com -L Paths.txt
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-l" or Args[4].lower() == "--lista")\
		 and (Args[6].lower() == "-p" or Args[6].lower() == "--pagina"):
			
			TipoRuta = Args[2].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[7]
				Val["Lista"]	= Args[5]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#11 Angelaz.py -T PHP -L Paths.txt -R -P xD.com
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-p" or Args[6].lower() == "--pagina"):
			
			TipoRuta = Args[2].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[7]
				Val["Lista"]	= Args[4]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#12 Angelaz.py -T PHP -L Paths.txt -P xD.com -R
		elif (Args[1].lower() == "-t" or Args[1].lower() == "--tipo")\
		 and (Args[3].lower() == "-l" or Args[3].lower() == "--lista")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina")\
		 and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			TipoRuta = Args[2].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[6]
				Val["Lista"]	= Args[4]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#13 Angelaz.py -L Paths.txt -P xD.com -T PHP -R
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-t" or Args[5].lower() == "--tipo")\
		 and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			TipoRuta = Args[6].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[4]
				Val["Lista"]	= Args[2]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#14 Angelaz.py -L Paths.txt -P xD.com -R -T PHP
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-p" or Args[3].lower() == "--pagina")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-t" or Args[6].lower() == "--tipo"):
			
			TipoRuta = Args[7].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[4]
				Val["Lista"]	= Args[2]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#15 Angelaz.py -L Paths.txt -R -P xD.com -T PHP
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-t" or Args[6].lower() == "--tipo"):
			
			TipoRuta = Args[7].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[5]
				Val["Lista"]	= Args[2]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#16 Angelaz.py -L Paths.txt -R -T PHP -P xD.com
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-r" or Args[3].lower() == "--robots")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-p" or Args[6].lower() == "--pagina"):
			
			TipoRuta = Args[5].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[7]
				Val["Lista"]	= Args[2]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#17 Angelaz.py -L Paths.txt -T PHP -R -P xD.com
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-r" or Args[5].lower() == "--robots")\
		 and (Args[6].lower() == "-p" or Args[6].lower() == "--pagina"):
			
			TipoRuta = Args[4].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[7]
				Val["Lista"]	= Args[2]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#18 Angelaz.py -L Paths.txt -T PHP -P xD.com -R
		elif (Args[1].lower() == "-l" or Args[1].lower() == "--lista")\
		 and (Args[3].lower() == "-t" or Args[3].lower() == "--tipo")\
		 and (Args[5].lower() == "-p" or Args[5].lower() == "--pagina")\
		 and (Args[7].lower() == "-r" or Args[7].lower() == "--robots"):
			
			TipoRuta = Args[4].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[6]
				Val["Lista"]	= Args[2]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#19 Angelaz.py -R -P xD.com -T PHP -L Paths.txt
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-l" or Args[6].lower() == "--lista"):
			
			TipoRuta = Args[5].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[3]
				Val["Lista"]	= Args[7]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#20 Angelaz.py -R -P xD.com -L Paths.txt -T PHP
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-p" or Args[2].lower() == "--pagina")\
		 and (Args[4].lower() == "-l" or Args[4].lower() == "--lista")\
		 and (Args[6].lower() == "-t" or Args[6].lower() == "--tipo"):
			
			TipoRuta = Args[7].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[3]
				Val["Lista"]	= Args[5]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#21 Angelaz.py -R -L Paths.txt -P xD.com -T PHP
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-l" or Args[2].lower() == "--lista")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-t" or Args[6].lower() == "--tipo"):
			
			TipoRuta = Args[7].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[5]
				Val["Lista"]	= Args[3]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#22 Angelaz.py -R -L Paths.txt -T PHP -P xD.com
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-l" or Args[2].lower() == "--lista")\
		 and (Args[4].lower() == "-t" or Args[4].lower() == "--tipo")\
		 and (Args[6].lower() == "-p" or Args[6].lower() == "--pagina"):
			
			TipoRuta = Args[5].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[7]
				Val["Lista"]	= Args[3]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#23 Angelaz.py -R -L Paths.txt -P xD.com -T PHP
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-l" or Args[4].lower() == "--lista")\
		 and (Args[6].lower() == "-p" or Args[6].lower() == "--pagina"):
			
			TipoRuta = Args[3].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[7]
				Val["Lista"]	= Args[5]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		#24 Angelaz.py -R -L Paths.txt -T PHP -P xD.com
		elif (Args[1].lower() == "-r" or Args[1].lower() == "--robots")\
		 and (Args[2].lower() == "-t" or Args[2].lower() == "--tipo")\
		 and (Args[4].lower() == "-p" or Args[4].lower() == "--pagina")\
		 and (Args[6].lower() == "-l" or Args[6].lower() == "--lista"):
			
			TipoRuta = Args[3].replace('"',"").strip()
			
			if  TipoRuta.lower() == "php"			or TipoRuta.lower() == "asp"			or TipoRuta.lower() == "html"\
			 or TipoRuta.lower() == "php asp"		or TipoRuta.lower() == "asp php"		or TipoRuta.lower() == "html php"\
			 or TipoRuta.lower() == "php html"		or TipoRuta.lower() == "asp html"		or TipoRuta.lower() == "html asp"\
			 or TipoRuta.lower() == "php asp html"	or TipoRuta.lower() == "asp php html"	or TipoRuta.lower() == "html php asp"\
			 or TipoRuta.lower() == "php html asp"	or TipoRuta.lower() == "asp html php"	or TipoRuta.lower() == "html asp php":
				
				Val["TipoRuta"]	= TipoRuta
				Val["Pagina"]	= Args[5]
				Val["Lista"]	= Args[7]
				Val["Robot"]	= True
				
				return Val
			
			else: return False
		
		else: return False
	
	return False

