import os
os.system("tput setaf 6")
print("\t\t\tWelcome to the Menu")
os.system("tput setaf 7")
print("\t\t\t--------------------")
print("\n\n\n")
f="y"
while True:
	if "y" in f:
		os.system("clear")
		print("Press 1 : to install docker")
		print("Press 2 : to check whether docker is installed or not")
		print("Press 3 : to start docker services")
		print("Press 4 : to know about the docker images present") 
		print("press 5 : to downlod docker image")
		print("Press 6 : to remove docker image")
		print("Press 7 : to run the os/container")
		print("Press 8 : to login to os")
		print("Press 9 : to exit from os which is currently running") 
		print("Press 10 : to terminate os")
		print("Press 11 : to remove perticular container")
		print("Press 12 : to remove all the running container")
		print("press 13 : to know how many os/containers are running under docker")
		print("Press 14 : to come out or dettach from os without stopping it")
		print("Press 15 : to enable docker permanently")
		print("Press 16 : to check docker state(active/inactive)")
		
		ch=input("Enter your choice : ")
		print(ch)
		
		if int(ch)==1:
			url=input("Enter the url of required docker : ")
			os.system("curl -sSL " +url)
			print("docker has installed pls check to confirm by pressing no two")
		elif int(ch)==2:
			os.system("rpm -q docker -ce")
		elif int(ch)==3:
			os.system("systemctl start docker")
		elif int(ch)==4:
			os.system("docker images")
		elif int(ch)==5:
			imgname=input("type the docker image name that you wish to download : ")
			os.system("docker pull" +imgname)
		elif int(ch)==6:
			img=input("type the image name alog with its version in the formate name:version 				that you wish to remove")
			os.system("docker rmi "+img+ "-f")
		elif int(ch)==7:
			dn=input("type os/container name that you wish to run : ")
			nm=input("type the name you wish to give this os : ")
			os.system("docker run -i -t --name" +nm+ ""+dn)
		elif int(ch)==8:
			on=input("type the os name where you wish to login : ")
			os.system("docker attach "+on)
		elif int(ch)==9:
			os.system("exit")
		elif int(ch)==10:
			ton=input("type the docker os name that you we to terminate : ")
			os.system("docker rm -f "+ton)
		elif int(ch)==11:
			cn=input("type the docker container name that you wish to remove : ")
			os.system("docker container rm "+cn)
		elif int(ch)==12:
			os.system("docker container rm -f $(docker conatiner ls -a -q)")
		elif int(ch)==13:
			os.system("docker ps -a")
		elif int(ch)==14:
			print("press left cntr+P+Q")
		elif int(ch)==15:
			os.system("systemctl enable docker")
		elif int(ch)==16:
			os.system("systemctl status docker")
		else:
			print("system has not found the specified command")
		f=input("to continue : y/n : ")
	elif "n" in f:
		break
	else:
		print("you can use only y or n")
		f=input("to continue : y/n : ")		

		

		

