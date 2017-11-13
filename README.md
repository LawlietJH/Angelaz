# Angelaz
## Escáner de Admin Panels de Páginas Web y Extracción De Robots.txt Con Python
### Versión: 1.1.0
- - -
### Modo De Uso: 
    
        Angelaz.py [-P Pagina.com][-R] {[-L Rutas.txt] | [-C]} | [-h|--help]
        
        -h, --help            Muestra este Mensaje y Sale del Script.
        
        -P  PAGINA.COM        Página a Escanear.
        
        -L  LISTA.TXT         Archivo con la Lista de Rutas.txt.
        
        -R, --Robots          Indica Si Se Desea Buscar El Archivo Robots.txt.
        
        -C, --Completo        Indica Hacer Un Escaneo Completo Con 483 Rutas.

Ejemplos:

        > Angelaz.py                            Corre El Script y Pide La Información
                                                Necesaria De Forma Interna.
        
        > Angelaz.py -h                         Muestra El Modo De Uso.
        
        > Angelaz.py -P Pagina.com              Realiza Escaneo a La Página Usando Las
                                                Rutas Una Lista Interna Con 140 Rutas.
        
        > Angelaz.py -P xD.com -L Rutas.txt -R  Realiza Escaneo a La Página Usando
                                                Las Rutas Del Archivo Rutas.txt y
                                                Busca El Archivo Robots.txt.
        
        > Angelaz.py -P xD.com -R -C            Agregar -C Hace Un Escaneo Completo Con
                                                483 Rutas. No Puedes Combinar -C y -L.

