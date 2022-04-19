# Pip_11


# top
# ps
# sudo su
# ps aux
# ps axjf
# kill 3772(pid)
# systemctl start httpd
# systemctl stop httpd
# systemctl restart httpd

# remote network information 
# dig google.com -- to lookup remote info
# nslookup google.com 
# traceroute --- hops 
# ping

# *** 
# server 


# for i in $(seq 1 2 20)
# do
#    echo "Welcome $i times"
# done


# for name in name
# do
#     echo Welcome $name
# done


# for name in Dan Prashant Anne
# do
#     echo Welcome $name
# done


# read x;
# echo "Welcome $x";

# for i in $(seq 50)
# do
#     echo $i
# done 


# x = 2
# y = 3 
# a = $(( $x + $y ))
# # s = x - y
# # m = x * y
# # d = x / y

# echo $a

# read x
# read y
# a=$(($x + $y))
# s=$(($x - $y))
# m=$(($x * $y))
# d=$(($x / $y))
# echo $a 
# echo $s $m $d 

# How to check the kernel version of a Linux system? device, os, version, release 
uname -a
uname -v
uname -r 

# How to see the current IP address on Linux?
ifconfig
ip addr show

# How to check for free disk space in Linux?
df -ah

# How to see if a Linux service is running?

# How to check the size of a directory in Linux?
du -sh 

# How to check for open ports in Linux?
netstat 
netstat -tulpn
# How to check Linux process information (CPU usage, memory, user information, etc.)?
top 
htop 
ps aux | grep nginx

# How to deal with mounts in Linux
ls /mnt  #mount 
mount /dev/sda2 /mnt # mounting new device on linux
mount # checking existing mount 
ls /etc/fstab # file system info 
# Man pages
man ps 
# Other resources
