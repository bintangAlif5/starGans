import re,sys,time,os,random

try:
   import requests
except ImportError:
    print '---------------------------------------------------'
    print '  \033[00m[\033[91m*\033[00m] \033[92m pip install requests'
    print '   \033[00m[\033[91m-\033[00m]\033[92m  you need to install requests Module\033[00m'
    sys.exit()

os.system("clear")
time.sleep(0.9)
print "=====================================================\n"
os.system("figlet Mass | lolcat")
print
print "\033[96mAuthor\033[00m:\033[95m r00t@star\033[00m"
print "\033[96mTeam\033[00m:\033[95m Sunda Cyber Army"
print "\033[96mInfo\033[00m:\033[95m Mass Mirror Hackersid"
print "\033[96mNote\033[00m:\033[95m If Error Please Contact Me\033[93m(in Readme.md)\033[00m"
print "=====================================================\n"
nick = raw_input("\033[92mNick anda:\033[00m ")
team = raw_input("\033[92mTeam anda:\033[00m ")
team1 = team.replace(" ","+")
hasil = raw_input("\033[92mUrl to list (ext : list.txt) :\033[00m ")
fil = open(hasil,"r").readlines()
jml = len(fil)
for i in range(jml):
	url = "https://hackersid.com/api/mirrorNew?hacker=%s&team=%s&url=%s&poc=Not+available&reason=Not+available" %(nick,team1,fil[i])
	def buka(url):
		a = requests.get(url=url)
		b = a.text
		c = str(b)
		status = re.findall('"status":(.*?),',c)
		domain = re.findall('"domain":"(.*?)",',c)
		message = re.findall('"message":"(.*?)",',c)
		mirror = re.findall('"mirror":(."?)}',c)
		print("Status  : %s" %(status))
		print("Domain  : %s" %(domain))
		print("Message : %s" %(message))
		print("Mirror  : %s" %(mirror))
		print(">>>>")
	buka(url)
	time.sleep(2)

