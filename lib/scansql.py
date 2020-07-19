import urllib2
import urllib 
import re
class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    CYAN = ''
class colors():
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    ENDC = ''
def grabsqli(ip):
    try :
        print bcolors.OKBLUE  + "|- Sqli Taraniyor... "
        page = 1
        while page <= 21:
                bing = "http://www.bing.com/search?q=ip%3A"+ip+"+.php?id=&count=50&first="+str(page)
                openbing  = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
                sites = findwebs
                for i in sites :
                            try :
                                      response = urllib2.urlopen(i).read()									 
                                      checksqli(i)	
                            except urllib2.HTTPError, e:
                                       str(sites).strip(i)
								   
                page = page + 10 
    except : 
         pass
def checksqli(sqli):
                            responsetwo = urllib2.urlopen(sqli + "'").read()
                            find = re.findall("sql",responsetwo)
                            if find:
                                            print("[ + ] SQLI > " + sqli)    
ip = raw_input("Server IP >")
grabsqli(ip)