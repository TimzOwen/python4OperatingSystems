
#### Software Distributions

#### software packages

#### installing from CLI Windows

install

    ~\Desktop\pubg.exe

#### s/w packages Linux

Debian and RPM (.deb .rpm)

install

    dbkg--->install
    
    sudo dbkg -i atom-amd64.deb
    
remove

    sudo dbkg -r atom
    
list package

    pbkg -l
    
search app

    dpkg -l | grep atom

#### mobile apps

side-loading

    install apps directly not from playstore

#### windows Archive ()7-Zip

archive

    contains one single files compressed into one
    
package archive

    source s/w files that are compressed into one
    
CLI compression

    compresss-Archive -path ~\Desktop ~\Desktop\cool_archive.zip

#### 7-zip linux

extract

    7z e my_archive.tar


### Package dependencies

DLL-Dynamic Link Libraries

    share memory to sav space
    
side-by-side assemblies(SxS)

    c:\Windows\WinSxS
    
system internals

    fix windows errors
    
    install-CLI
    
    Find-Package sysinstall -IncludeDependencies
    
Chocolatey

    where all kinds of s/w live inn windows
    
    Register-PackageSource - Name chocolatey -ProviderName chocolatey - Location http://chocolatey.org api/v2
    
verify now

    Get-PackageSource


#### Linux Package Dependencies

package managers

    help eliminate dependencies errors

#### Package Managers

Pckage mangers

    makes sure installation and removal pf s/w is easier
    
Configuration management tools

    SCCM
    
    Puppet
    
    
#### Package Managers Linux

apt(Advanced package Tool)

    sudo apt install gimp
    
remove

    sudo apt remove gimp
    
PPA (Personal Pckg Archive)

    s/w repo for uploading src packges fro apt
    
    /etc/apt/sources.list
    
updated

    sudo apt update
    
upgrade

    sudo apt upgrade


#### Behind the scenes of package manages Windows

check process

    process Monitoring
    
try Orca.exe


#### Behind the scene Linux

setup script

    ls -l example\app/

### DEVICE SOFTWARE MANAGEMENT

#### Devices and drivers

windows

    Device Manager
    
Ubuntu

    character devices
    
        transmit data in characters (keyboard and mouse etc)
        
    Block Devices
    
        USB, Hardrives CDROM transfer data in blocks
        
    kernel module for update drivers

####  Windows Operating system Update

security patch

    s/w ment to fix security hole
    
    update settings/advances

#### Linux OS Update

uname

     gives us system info
     
-r (check kernel version)

    shows the version you have
    
    uname -r
    
update first then full upgrade

    sudo apt update
    
    sudo apt full upgrade
