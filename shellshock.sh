file=shellshock_Output.txt
echo "============================================================" >> $file
echo "	Machine Details 	  				">> $file
echo "============================================================" >> $file
uname -a >> $file
date  >> $file
hostname >> $file
ifconfig | grep 'inet addr' >> $file
echo " " >> $file
echo " " >> $file
echo "============================================================" >> $file
echo "	Result of the Test    " >> $file
echo "============================================================" >> $file
env x='() { :;}; echo Machine is vulnerable to Shellshock' bash -c  "echo Tested by Silent Ethical Hacker" >> $file
echo "" >> $file
echo "" >> $file
echo "" >> $file
echo "============================================================" >> $file
echo "	Shellshock Testing Script	  				">> $file
echo "	Author:   Shekhar Suman & Akriti Srivastava	  				">> $file
echo "============================================================" >> $file
