# Angelaz v1.2.3
## Escáner de Admin Panels de Páginas Web y Extracción De Robots.txt Con Python
### Versión: 1.2.3
### Python 2 y 3
### Windows.

- - -

### Caracteristicas:

   + **Busca El Login de Admin (Admin Panels) y Vulnerabilidades EAR de Páginas Web.**
      
      + ***Argumento: -P, --Pagina PAGINA.COM***
      
   + **La Velocidad De Escaneo Dependerá de la respuesta de la página.**
      
      + ***Por Cada 100 Rutas Escaneadas Debería Tardar 1 Segundo.***
      
   + **Genera un Archivo De Logs Donde Contiene Las Rutas Encontradas En La Página Seleccionada.**
   + **Tiene Multiprocesamiento Usando Hilos de Ejecución (Threads).**
   + **Tiene 2 Grandes Listas Internas de Rutas.**
      
      + **140 Rutas: *Para Escaneo Por Defecto.***
      + **483 Rutas: *Para Escaneo Completo.***
      
      + ***Argumento: -C, --Completo.***
      
   + **Soporta Busqueda De Rutas Con Extensiones PHP, ASP y HTML.**
   + **Filtro De Rutas PHP, ASP y HTML. Se Pueden Combinar.**
      
      + ***Argumento: -T, --Tipo PHP, ASP, HTML.***
      
   + **Busca Posibles Vulnerabilidades de EAR.**
   + **Busca, Extrae y Guarda El Archivo Robots.txt De La Página Solicitada.**
      
      + ***Argumento: -R, --Robots.***
      
   + **Soporta Agregar Rutas Desde Una Lista Propia De Usuario.**
      
      + ***Argumento: -L, --Lista ARCHIVO.TXT.***
   
- - -

### Modo De Uso: 
    
        Angelaz.py [-P Pagina.com][-R][-T TIPO] {[-L Rutas.txt] | [-C]} | [-h]
        
         -h, --help                Muestra Este Mensaje y Sale del Script.
         
         -P, --Pagina PAGINA.COM   Página A Escanear.
         
         -L, --Lista LISTA.TXT     Archivo Con La Lista de Rutas.txt.
         
         -R, --Robots              Indica Si Se Desea Buscar El Archivo Robots.txt.
  
         -C, --Completo            Indica Hacer Un Escaneo Completo Con 498 Rutas.
  
         -T, --Tipo PHP,ASP,HTML   Filtra Por Tipo Las Rutas Que Se Usarán.

**Ejemplos:**

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
                                          498 Rutas. No Puedes Combinar -C y -L.
      > Angelaz.py -T PHP             [*] Filtrará Las Rutas Para Mostrar Solo PHP
                                          y Agregando Las Que No Tienen Extensión.
      > Angelaz.py -T "ASP HTML"      [*] Filtrará Las Rutas De Archivos Mostrando
                                          Con Extensión ASP y HTML solamente y
                                          Agregando Las Que No Tienen Extensión.

