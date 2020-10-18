

#### size vs Disk
https://technet.microsoft.com/en-us/library/hh148159.aspx

===========================================================================
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
    
