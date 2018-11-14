#!/bin/sh
# Ask the user for their name
echo Welcome User to the Pizza Bot, what is your name?
read varname
echo which option are you choosing today, delivery or carryout? $varname
read option1
	if [option1 == 'delivery']
		python webscript.py
	 then
	 	echo Bye
	 fi
