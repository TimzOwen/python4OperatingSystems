

#### FileSystem Types

#### Partition tables

    Master  Boot Record(MBR)
    
    GUID Partition Table(GPT)
    
#### Partitioning and Formating

CMD Diskpart

    Diskpart
    
    list disk
    
    select disk1
    
    clean
    
    Create partition primary
    
    select partition 1
    
    active
    
formart

    formart FS=NTFS label=myDrive quick


### Linux Partitioning and Formatting Disk

parted used beacuse support many platform

list disk

    sudo parted -l
    
select disk

    sudo parted/dev/sdb
    
make label

    mklabel gpt
    
partition

    mkpart primary ext4 1MiB 5GiB
    
formart

    sudo mkfs -t ext4 /dev/sdb1
    
Mounting sd cards

    sudo mount /dev/sdb1/folder_created_to_be_mounted_to
    
unmount

    sudo unmount /dev/myusb


### Swap Space in Windows

pagefiles.sys

    store recent accessed files

### Linux Swap

select a drive

    sudo parted /dev/sdb
    
partition

    mkpart primary linux-swap 5GiB 100%
    
make swap

    sudo mkswap /dev/sdb2
    
enable swap

    sudo swapon /dev/sdb2

### File Data and Metadata Windows

creating shortcuts

    symbolick links (use cmd) mklink file1.txt
    
    HardLink (uses /H) mklink /H file1.txt

### Linux Files

stores data in inodes

create

    ls -l important_file
    
    ln -s important_file important_file.softlink
    
    ln important_file important_file.hardlink

#### Disk Usage Windows

check:

    computer management
    
    select partition then properties

#### Linux Disk usage

check usage

    du -h
    
check space

    df (disk free in full)

### File System Repair Windows

Data Coruptions

    handles by NTFS log sys file
    
self-healing

    changes made to a disk on small errors automatically

repair C

    fsutil repair query C:
    
specify drive to be checked

    chkdsk /F D:

### Linux File system Repairs

check file system

    sudo fsck /dev/sda


### Processes

windows

    starts of with the smss.exe to set up the os
    
    then login process winlogon.exe
    
    client runtime server csrss.exe (Running windows GUI and Commandline)
    
    Taskkill PID -->kills a process with specified ID
    
        taskkills /pid 5856
        
    TaskManager
    
        taskmgr.exe
        
Linux

    uses init to start up the kernel process ID = 1
    
    less  /etc/some_file | grep Hello

## Managing Process

Windows

    Kills a process on Task manager or cmd
    
    check PID
    
        tasklist
        
    powershel
    
        Get-Process
Linux

    check running process
    
        ps -x
        
        ps -ef (get all process for all users)
        
        ps -ef | grep Chrome (check if a process is running)
        
        ls -l /proc
        
### Signals on Processes

Windows

    SIGINT  (rendered with CTR + C)
    
Linux

    CTR + C

### Process Explorer Windows

Look  at running procceses

    cTR + F (find processes in a system)

### managing processes Linux

check process status

    ps -x
    
kills a proccess

    kill 202012
    
Kill without giving time for cleap up

    kill -KILL 202013
    
suspend a process

    kill - TSTP 202013
    
continue a process

    kill -CONT 202013

### Resource Monitoring Windows

Resource monitoring Tools

    GUI
    
terminal powershell

    Get-process
    
Get specific process

    Get-Process | Sort CPU -descending | Select -first 3 -Property ID,ProcessName,CPU

### Linux resource monitoring

most consuming resource

    top
    
check run time, users   load avarage

    uptime
    
check for open files and processes using them

    lsof
    

### REMOTE ACCESS

#### Remote connection and SSH

SSH - secure shell for securely accessing one computer from another

    private and public key

### Remote connection windows

powershell

    putty.exe -ssh owen@255.255.255
    
Remote Desktop

    GUI

### File Transfer linux

Secure copy

    copy files between computers in a nerwork on linux
    
    scp /home/desktop/owen.txt shem@255.255.256:

### File Transfer Windows

pUty secure client (pscp.exe)

    pscp.exe C:\Users\Desktop\owen.txt shem@255.255.256:
    
shared Folders

    Right click and ccheck on share with
    
powershell share to all

    net share sharingFolder=C:\Users\Owen\Desktop\sharingFolder /grant:everyone,full

### Virtualization

virtual box

    virtual box for windows


### Logging in Computing

Logging: (act of creatign Logging events)

### Windows event viewer

Event viewer

    eventvwr.msc

### Linux Logs

stored in

    /var/log
    
check log files list

    ls /var/log
    
logrotate

    rotate machine logging within a specified time
    
system logs

    less var/log/syslog

#### working with Logs

check on errors alone

    less /var/log/syslog | grep error
    
Tail and logging in realtime

    tail -f /var/log/syslog

### Deployment of Operating System

colnezella

    backup and restore single /backup more machines
    
symantec ghots

    imaging tool
    
Disk to cloning

    harddrive cloning
    
Copy files as image with dd in linux


    make sure its unmounted
    
    sudo dd if=/dev/sdd of=~/Desktop/my_usb_image.img bs=100M

