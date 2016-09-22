#!/bin/bash

post_install()
{
	source /etc/profile

	echo ">>>> Please note that this tools and some related projects (for example ChromeOS) use python2."
	echo ">>>> They assume that python2 is the default python interpreter. ArchLinux default is python3, so be prepared to fix python references in your works."
	echo ">>>> This package contains a repo_fix.sh script. Use it to fix python2 references in python's script created after 'repo init' command"
	echo ">>>> For getting started with depot_tools, visit this page: http://dev.chromium.org/developers/how-tos/depottools"
	echo ">>>> Run 'source /etc/profile' if you don't find any depot_tools related commands."
}

post_upgrade()
{
	source /etc/profile

	echo ">>>> Run 'source /etc/profile' if you don't find any depot_tools related commands."
}
