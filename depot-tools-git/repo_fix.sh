#!/bin/bash
# usage: repo_fix.sh directory
# Fix python2 references in .repo/repo folder created after 'repo init' command
# Needed for work in ArchLinux! Or fix it by yourself!

# Check for a valid parameter
if [ -z $1 ]; then
	echo "Usage: repo_fix.sh repo_dir"
else
	# Check for a valid directory
	if [ -d $1 ]; then
		# Check for a valid repo repository
		if [ -d $1/.repo ]; then
			echo "repo repository found (maybe). Proced with patching."
			cd $1/.repo/repo
			# Patching all python scripts.
			# In my test with Android and ChromeOS repository, only main.py requires a patch, but I don't know if this thing will change in the future.
			# So we will patch every python script!
			for file in *.py
			do
				echo "Patching $file"
				sed 's/"exec" python /"exec" python2 /' $file > $file.tmp
				install -Dm 755 $file.tmp $file
				rm $file.tmp
			done
		else
			echo "This directory does not contain a valid repo repository!"
		fi
	else
		echo "Invalid directory!"
	fi
fi
