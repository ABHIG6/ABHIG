echo "░█████╗░██████╗░██╗░░██╗██╗░██████╗░░█████╗░ ";
echo "██╔══██╗██╔══██╗██║░░██║██║██╔════╝░██╔═══╝░ ";
echo "███████║██████╦╝███████║██║██║░░██╗░██████╗░ ";
echo "██╔══██║██╔══██╗██╔══██║██║██║░░╚██╗██╔══██╗ ";
echo "██║░░██║██████╦╝██║░░██║██║╚██████╔╝╚█████╔╝ ";
echo "╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░╚═════╝░░╚════╝░ ";
echo "                                             ";

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/ABHIG/

clear

cd /etc/

clear

sudo rm -rf /etc/ABHIG

clear

mkdir ABHIG

clear

cd ABHIG

clear

git clone https://github.com/ABHIG6/ABHIG.git

clear

cd ABHIG

clear

sudo chmod +x install.sh

clear

./install.sh

clear
