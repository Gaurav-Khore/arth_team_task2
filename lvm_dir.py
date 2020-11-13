import os
os.system("tput setaf 80")
os.system("clear")
os.system("figlet -t -k LVM Hadoop")

print("Check the disk name")
os.system("fdisk -l")


os.system("tput setaf 10")
print("\n\n\nPhysical Volume Creation:-")
os.system("tput setaf 9")
nd = int(input("Enter the number of disk:-"))
for i in range(1,nd+1):
	print(i)
	npv = input("Enter the hard disk name:-")
	os.system("pvcreate {0}".format(npv))
os.system("tput setaf 226")
print("\n\n\nlist of physical volume:-")
os.system("pvdisplay")
os.system("tput setaf 10")
print("\n\n\nPhysical Volume created successfully....")

os.system("tput setaf 10")
print("\n\n\nVolume Group Creation:-")
os.system("tput setaf 9")
vgp = input("Enter your Physical Volume name:-")
nvg = input("Give name to the Volume Group:-")
os.system("vgcreate {0} {1}".format(nvg,vgp))
os.system("tput setaf 226")
print("\n\n\nVolume Group:-")
os.system("vgdisplay {}".format(nvg))
os.system("tput setaf 10")
print("\n\n\nVolume Group created successfully....")


os.system("tput setaf 10")
print("\n\n\nLogical Volume Creation:-")
os.system("tput setaf 9")
nlv = input("Give name to the Logical Volume:-")
slv = input("Give size of the Logical Volume (eg:- 5G,10g):-")
os.system("lvcreate --size {0} --name {1} {2}".format(slv,nlv,nvg))
os.system("tput setaf 226")
print("\n\n\nLogical Volume:-")
os.system("lvdisplay {0}/{1}".format(nvg,nlv))
os.system("tput setaf 10")
print("\n\n\nLogical Volume created successfully....")

os.system("tput setaf 10")
print("\n\n\nFomat the Logical Volume:-")
os.system("tput setaf 9")
os.system("mkfs.ext4 /dev/{0}/{1}".format(nvg,nlv))

df = input("Enter the data node directory:-")
os.system("mkdir /{0}".format(df))
os.system("mount /dev/{0}/{1} /{2}".format(nvg,nlv,df))

os.system("tput setaf 10")
print("\n\n\nLogical Volume mounted successfully....")
os.system("df -h")
print("\n\n\nNow You can Add /{0} directory to the DataNode of HDFS Cluster..".format(df))




os.system("tput setaf 7")

