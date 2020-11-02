
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
