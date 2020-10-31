
### List directories in GUI (WINDOWS)
    
    Root directory
    
        Windows C:\
        
        Linux /

#### Navigate the Directories in Windows with Powershell
  
  list directories
  
       ls c:\   - shows c directories (Parent and children directories)

Get full description
    
    Get-Help ls    / Get-Help ls -Full

Get Hidden Files in a directory
    
    ls -Force C:\

### List directories in Terminal (LINUX)

Root directory - Parent directory (......./..// uses forward Slash )
    
    /home/owen/desktop

List root directories
    
    ls /
Flag -
 
    A way to specify additional information
    
    ls --help (shows all flag commands and more info)
    
    man ls (Get more command help)
    
    ls -l / (Sow files in a more descent way)
    
    ls -l -a (show all files including hidden files)

#### changing directories in windows

Absolute path- starts from the root

Relative - current directory 

print working directory

    pwd - current working Directory
    
    cd ..\Desktop - one directory back and into Desktop
    
    cd~ . Navigate to root directory (cd~\Desktop )

#### Linux Changing Directories

pwd

    Current directory

cd /home/owen/documents
   
    changing directory
    
    cd ../Documents
    
    cd ~/Desktop

#### making directories in GUI

mkdir

    mkdir ma_new_folder

escaping space char

    mkdir 'my cool folder'
    
    mkdir my `cool` folder

#### Linux make directories in Bash

mkdir

    mkdir my\ cool\ folder
 
    mkdir my_cool_folder
   
    mkkdir 'my cool folder'

#### command History Windows

history

    shows all commands entered

ctr+R

    search for specific commands used

clear

    clear output in your screen

#### command History Linux Bash

history

    shows history commands

clear

    clears user commands history

#### Copying Files AND directories (Windows)

cp

    copies the folder to the specific directory

    cd my_cool_folder.txt C:\Users\Owe\Desktop

Wildcard
    
        char used to select files based on certain pattern
    
        cp *.jpg C:\Users\Owe\Desktop

Recurse

    copy over contents of a file directory

Verbsoe

    outline each file content being copied

#### Linux Copying Files and Directories

copy
   
   cp my_very_cool_file.txt ~/Desktop
   
   cp *.png ~/Desktop
   
   cp -r 'cat pictures' ~/Desktop  #(Copies all the file contents using (verbose-r))

#### Moving and Renaming files

mv

    rename files
    
    mv 'python scripts' 'python latest scripts'

moving doc

    mv 'python scripts' C:\Users\Owe\Desktop
    
    mv *_python.txt C:\Users\Owe\Desktop

#### moving documents in Linux
  
  rename files
  
    mv 'python scripts' 'python latest scripts'

moving doc

    mv 'python scripts' ~/Desktop
    
    mv *_documents ~/Desktop

#### Removing Files and Directories Windows

remove

    rm command
   
   

#### Removing Files and directories Linux OS

remove
    rm text1.txt
    
force remove

    rm -r linuxFolder

#### Files and Text manipulation

#### on windows

Open a file

    cat owen.txt

    more owen.txt        (q-quit back to terminal, Enter-scroll line by line ,spacebar-page by page scrolling)


View just first few lines of a file

    cat owen.txt -Head 10       (first 10 lines only)
    
View last line

    cat owen.txt -Tail 10

#### Linux display contents of a file

View

    cat important.txt
    
large doc

    less large.txt            (up&Down,pageup&down,g-moves to start file,G-end text file, /word_search, q-quit shell)
    
view first and last few lines of a file

    head owen.txt
    
    tail owen.txt


#### modifying Text files

start notepad++

    start notepad++ new_file_to_be_created.txt

#### modifying Text Files in Linux

start nano editor

    nano new_owen_file

#### POWERSHELL powerful commands

actual shell command

    Get-Alias ls
    
children

    Get-childItem C:\

#### Searching within files in Windows

search with select string

    select-string kabarak owen.txt
    
use wildcat from regular expression

    select-string kabarak *.txt

#### windows, searching within directories

Filter command

    ls 'C:\Program Files\' -Recurse -Filter *.exe

#### Linux searching within files

uses grep

    grep cow farm_animal.txt
    
multiple files search

    grep cow *.animal.txt


#### Windows input,output and pipeline

echo-writes output

    creates a new file
    
    echo woof > dogs.txt
    
Io

    stdin
    
    stdout
    
    stderr
    
> ---stdn output redirector

>> ---adds instead of overwiting a file

|----pipelines to pass output of a string into input of another

    cat owen.txt | select-string kaba
    
place it in a new file

    cat owen.txt | select-string kaba > new_words.txt

stderr:

    forwards error output to  file
    
    rm secure _file         ("permision denied erro")
    
    re secure_file 2> errors.txt
    
    re secure_file 2> $null

$null

    std char with definition of nothing


#### output redirection linux

create

    echo woof > dogs.txt - overwrite
    
    echo woof >> dogs.txt - no overwrite
    
input

    cat < file_input.txt
    
redirect stderr

    ls /dir/fake_data 2> output_error.txt
    
search

    ls -la /etc/ | grep bluetooth    # prints files with bluetooth
    
### USERS AND GROUPS

####
Network domain---> a network of computers, users, files,etc...added to a central database

UAC (User access control)----->prevents unauthorized changes to a system

#### check user account windows

check

    Get-LocalUser
    
Groups

    Get-LocalGroup
    
check admins

    Get-LocalGroupMember Administrators

#### linux file permission

permission

    sudo cat/home/doc.txt
    
check users

    cat /etc/password

#### Passwords Windows

GUI

    Computer management
    
CLI

    net user Owe *
    
NextLogin

    net user Owe /logonpasswordchng:yes


# Linux password

change

    passwd Owe
    
next login

    sudo passwd -e Owe


#### Adding and Removing Users in Windows

GUI

    computer management
    
CLI

    net user Chelsea * /add
    
    net user Cherono password /add /logonpasswordchng:yes
    
remove

    net user Chelsea /del
    
    Remove-LocalUser Cherono

#### Adding and removing files in Linux

add

    sudo useradd owen
    
remove

    sudo userdel owen


#### Files Permission
