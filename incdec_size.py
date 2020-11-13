import os
os.system("tput setaf 80")
os.system("clear")
os.system("figlet -t -k LVM Hadoop")
os.system("tput setaf 10")
print("Check the logical VOlume attached to the DataNode Directory:-")
os.system("df -h")
os.system("tput setaf 9")
nlv = input("Enter the logical Volume name:-")

print("""Press:-
 1.For Increasing the size.
 2.To exit""")

ch = int(input("Enter Your Choice:-"))

while True:
	if ch == 1:
		sin = input("Enter the size to be added/increased(eg:- 5G,2G):-")
		os.system("lvextend --size +{0} {1}".format(sin,nlv))
		os.system("resize2fs {0}".format(nlv))
		os.system("tput setaf 226")
		os.system("df -h")
		os.system("tput setaf 10")
		print("\n\n\nCongrats Your DataNode Directory Size has been increased Successfully.....")
	elif ch == 2:
		exit()
	else:
		os.system("tput setaf 7")
		print("invalid Coice")

