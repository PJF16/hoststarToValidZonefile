import os

f = open("hoststar.txt", "r")

if os.path.exists ("zonefile.txt"):
	os.remove ("zonefile.txt")

zonefile = open ("zonefile.txt", "w")

domain = input ("Enter Domain: ")

cline = ""
for line in f:
	line = line.strip()
	if (line != "A" and line != "CNAME" and line != "MX" and line != "SRV" and line != "TXT"):
		if (line == "*."+domain):
			cline="*"
		else:
			if (line == domain):
				cline = "@"
			else:
				cline = line.replace("."+domain,"")
	else:
		if (line == "MX"):
			cline = cline + " 3600 IN MX 10 " + f.readline()
		else:
			cline = cline + " 3600 IN " + line + " " + f.readline()
		zonefile.write(cline)
		cline = ""
zonefile.close()
f.close()
