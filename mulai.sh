echo  #!/bin/bash

Yell="\033[33;1m"; # Yellow light
gre="\033[32;1m"; # Green light
Mer="\033[31;1m"; # Red light
Norm="\033[00m"; # White light
Ter="\033[95m"; # Purple Light
CL="\033[36;1m"; # Cyan Light
Bir="\033[96;1m"; # Blue Aqua

echo "____________________________________\n";
    echo $Mer"1).$gre Wp-injection tools";
    echo $Mer"2).$gre Mass mirror Hackersid";
    echo $Mer"3).$gre Bin Checker Script";
    echo "$Mer Creator$Yell r00t@star$Norm |$Ter Sunda Cyber Army";
    echo $Ter"Note :$gre If error please contact me ($YellReadme.md$gre)";
    echo $Norm"____________________________________";
    echo "<---- $BirAre you want?--->$Norm\n";
    read -p "--# " star; 
if [ $star = 1 ] || [ $star = 1 ]
then
sleep 2
python2 wp-inject.py
fi
if [ $star = 2 ] || [ $star = 2 ]
then
sleep 2
python2 mass.py
fi
