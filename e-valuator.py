import dns.resolver
import sys
import colorama
import platform
from colorama import init, Fore, Back, Style
import re

# pip install -r requirements.txt (colorama)

os = platform.platform()
if os.find('Windows')!= (-1):
	init(convert=True)


print("""



███████╗░░░░░░██╗░░░██╗░█████╗░██╗░░░░░██╗░░░██╗░█████╗░████████╗░█████╗░██████╗░
██╔════╝░░░░░░██║░░░██║██╔══██╗██║░░░░░██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░█████╗╚██╗░██╔╝███████║██║░░░░░██║░░░██║███████║░░░██║░░░██║░░██║██████╔╝
██╔══╝░░╚════╝░╚████╔╝░██╔══██║██║░░░░░██║░░░██║██╔══██║░░░██║░░░██║░░██║██╔══██╗
███████╗░░░░░░░░╚██╔╝░░██║░░██║███████╗╚██████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚══════╝░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝


\x1B[3mSimple Python3 Script for Checking SPF & DMARC Records.\x1B[0m
""" + '\n')
Domain = input('Domain: ')


# Checking SPF
print ('\n[+] Checking SPF Record...')
try:
 	obj_answer = dns.resolver.resolve(Domain, 'TXT')
except:
	sys.exit(Fore.RED + "\n[+] Domain can't be resolved! Check the domain name and try again..")

answer = str(obj_answer.response)
cond = answer.find("v=spf")
if cond != -1:
	print ('[+] SPF Record Found!')
	spf_pos= answer.find("v=spf")
	spf_end_tmp= (answer[spf_pos:].find("\n"))-1
	spf_end= answer[spf_pos:spf_pos+spf_end_tmp]
	print (Fore.GREEN + '[+] Domain: ' + Domain)
	print (Fore.GREEN + '[+] SPF Record: ' +spf_end)

	neutral_check = answer.find('?all')
	fail_check = answer.find('-all')
	soft_check = answer.find('~all')
	pass_check = answer.find('+all')


	if neutral_check != -1:
		print (Fore.RED +'[+] Result: ?all IS FOUND!! Domain emails can be spoofed!')

	elif fail_check != -1:
		print (Fore.GREEN +'[+] Result: -all is found. SPF is correctly configured.')

	elif soft_check != -1:
		print (Fore.GREEN +'[+] Result: ~all is found. SPF is correctly configured.')
	
	elif pass_check != -1:
		print (Fore.RED +'[+] Result: +all DOMAIN IS VERY BADLY CONFIGURED! Domain emails can be spoofed!')

	else:
		print (Fore.RED +'[+] Result: No condition is set for "all"! Domain emails can be spoofed!')	

else:
	print (Fore.RED +'[+] No SPF Record Found!!')



# Checking DMARC
print (Fore.WHITE + '\n\n[+] Checking DMARC Policy..')
try:
 	obj2_answer = dns.resolver.resolve('_dmarc.'+ Domain, 'TXT')
except:
	sys.exit(Fore.RED + "[+] The domain doesn't have DMARC policy configured!")

answer2 = str(obj2_answer.response)	
print (Fore.WHITE + '[+] DMARC Policy Found!')


none_check = re.search("[\;\s]p\=none\;", answer2)
reject_check = re.search("[\;\s]p\=reject\;", answer2)
quarantine_check = re.search("[\;\s]p\=quarantine\;", answer2)


if none_check:
	print (Fore.RED + '[+] Result: DMARC Policy is set as none! Domain emails can be spoofed!')
if reject_check:	
	print (Fore.GREEN + '[+] Result: DMARC Policy is set as reject! Domain emails are safe from spoofing.')
if quarantine_check:	
	print (Fore.GREEN + '[+] Result: DMARC Policy is set as quarantine! Domain emails are safe from spoofing.')