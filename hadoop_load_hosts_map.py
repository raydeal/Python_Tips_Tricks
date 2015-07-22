# -*- coding: utf-8 -*-

"""
Laduje dane do tabeli dbimports.hosts_map z pliku CSV. UPDADE,DELETE w Hadoop dostepny jest dopiero od wersji 0.14
wiec, zeby podmienic dane trzeba usunac wszystkie i zaimportowac na nowo. Temu sluzy ten skrypt.

@attention: Skrypt CSV nie moze zawierac w pierwszej lini naglowkow - w pliku musza byc tylko dane.

@author: Albert Defler
@change: 2015-03-31 utworzenie
"""

from subprocess import call

def load_data():
    sql = 'INSERT OVERWRITE TABLE hosts_map SELECT * FROM ({0}) t'  
    subsql = ''
    with open('hosts_map.csv','r') as f:
        #pobieramy dane z pliku i skladamy podzapytanie SQL
        for lnr, line in enumerate(f):
            #print lnr, line
            if lnr == 0:
                subsql = "SELECT '{0}' ".format(line.strip().replace(';',"','")) #apostrofy sa wazne bo maja za zadanie utworzyc literaly znakowe z poszczegolnych elementow
            else:
                subsql += "UNION ALL SELECT '{0}' ".format(line.strip().replace(';',"','")) #apostrofy sa wazne bo maja za zadanie utworzyc literaly znakowe z poszczegolnych elementow
    insert =  sql.format(subsql)
    #print insert
    
    #wywolanie komenty w shell
    print 'Wywoluje hive i przetwarzam dane...'
    return_code = call('hive -e "USE dbimports; {0};"'.format(insert) , shell=True)
    print 'Wynik wykonania w shell: %s' % return_code
            
        
#wywolanie skryptu z lini komend, wywoluje to co trzeba 
if __name__ == '__main__': load_data()