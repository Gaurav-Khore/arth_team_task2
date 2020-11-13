import os 
os.system("tput setaf 80")
os.system("clear")
os.system("figlet -t -k LVM Hadoop")

os.system("tput setaf 10")

while True:
	os.system("tput setaf 80")
	os.system("clear")
	os.system("figlet -t -k LVM Hadoop")

	os.system("tput setaf 10")
	print("""Press:-
 1.For Creating Dir for DataNode using LVM.
 2.For increasing the size of the Dir.
 3.To exit""")

	os.system("tput setaf 9")
	ch = int(input("Enter Your Choice:-"))
	os.system("tput setaf 7")
	if ch == 1:
		os.system("python3 /root/task7.1/lvm_dir.py")
	elif ch == 2:
		os.system("python3 /root/task7.1/incdec_size.py")
	elif ch == 3:
		os.system("tput setaf 80")
		os.system("figlet -c Thanks For Using Tool......")
		os.system("tput setaf 7")
		exit()
	else:
		print("invalid Choice")



